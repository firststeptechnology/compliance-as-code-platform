# Compliance-as-Code Platform — Version 1.0 Architecture

This document designs the actual software platform, building on top of the
now-stable public repository structure (`docs/`, `examples/`, `src/`,
`tests/`, `scripts/`). It is grounded in your three already-published,
live JSON schemas (`compliance-rule`, `evidence-record`,
`framework-metadata`) and your existing OpenAPI surface
(`/frameworks`, `/frameworks/{framework}`, `/controls`, `/controls/{controlId}`,
`/schemas`, `/examples`) — nothing here contradicts what's already public.

---

## 1. Python Package Layout

```
src/
└── compliance_as_code/
    ├── __init__.py
    ├── __version__.py
    │
    ├── core/                      # Framework-agnostic domain models
    │   ├── __init__.py
    │   ├── models.py              # ComplianceRule, EvidenceRecord, FrameworkMetadata
    │   │                          # — dataclasses mirroring the 3 published JSON schemas exactly
    │   ├── enums.py               # Status, EvidenceType, Priority — mirrors schema enums
    │   └── exceptions.py          # RuleValidationError, FrameworkNotFoundError, etc.
    │
    ├── schemas/                   # Schema loading + validation
    │   ├── __init__.py
    │   ├── loader.py              # Loads docs/schemas/*.json at runtime
    │   └── validator.py           # Wraps jsonschema; validates any object against
    │                              # compliance-rule / evidence-record / framework-metadata
    │
    ├── frameworks/                # Framework abstraction layer
    │   ├── __init__.py
    │   ├── base.py                # Framework(ABC): load(), rules(), metadata(), search()
    │   ├── registry.py            # FrameworkRegistry — discovers installed framework
    │   │                          # packages via entry_points, not hardcoded imports
    │   └── loader.py              # Reads a framework's rule JSON + framework-metadata.json
    │                              # from a directory or installed package
    │
    ├── engine/                    # Rule engine — the actual compliance-checking logic
    │   ├── __init__.py
    │   ├── evaluator.py           # RuleEvaluator: takes a rule + evidence, returns a result
    │   ├── result.py              # EvaluationResult model (pass/fail/not_applicable + reasons)
    │   ├── pipeline.py            # Runs N rules against a target (repo, config, cloud
    │   │                          # account snapshot, etc.) and aggregates results
    │   └── plugins/                # Evaluator plugins — one file per "how do we check this"
    │       ├── __init__.py
    │       ├── file_pattern.py    # e.g. "does this file/config exist and match X"
    │       ├── json_query.py      # e.g. JSONPath assertions against a config snapshot
    │       └── manual.py          # Rules that can't be automated — flagged for human evidence
    │
    ├── search/                    # Search engine over rules/frameworks
    │   ├── __init__.py
    │   ├── index.py                # Builds an in-memory/SQLite FTS index from loaded rules
    │   └── query.py                 # Search API: by keyword, framework, control_id, tag, family
    │
    ├── ai/                         # AI integration layer
    │   ├── __init__.py
    │   ├── provider.py             # Abstract LLMProvider interface (provider-agnostic)
    │   ├── providers/
    │   │   ├── anthropic.py
    │   │   └── openai.py
    │   ├── rule_generation.py      # Draft new rules from source regulatory text
    │   │                          # (human-reviewed before publishing — never auto-published)
    │   ├── evidence_validation.py  # AI-assisted plausibility check of submitted evidence
    │   │                          # against a rule's guidance (advisory, not authoritative)
    │   └── prompts/                # Versioned prompt templates, not inline strings
    │
    ├── api/                        # REST API (FastAPI)
    │   ├── __init__.py
    │   ├── app.py                  # FastAPI app factory
    │   ├── routers/
    │   │   ├── frameworks.py       # mirrors /frameworks, /frameworks/{framework}
    │   │   ├── controls.py         # mirrors /controls, /controls/{controlId}
    │   │   ├── schemas.py          # mirrors /schemas
    │   │   ├── examples.py         # mirrors /examples
    │   │   ├── evaluate.py         # NEW in v1.0: POST /evaluate — run the engine
    │   │   └── search.py           # NEW in v1.0: GET /search
    │   ├── dependencies.py         # Auth, rate limiting, DB session injection
    │   └── schemas_api.py          # Pydantic request/response models (separate from
    │                          # the JSON Schema files — these are API contracts)
    │
    └── cli/                        # CLI (Typer)
        ├── __init__.py
        ├── main.py                 # Entry point: `compliance-as-code`
        ├── commands/
        │   ├── validate.py         # `compliance-as-code validate <file>`
        │   ├── search.py           # `compliance-as-code search <query>`
        │   ├── evaluate.py         # `compliance-as-code evaluate --framework cmmc-l1 --target .`
        │   └── frameworks.py       # `compliance-as-code frameworks list`
        └── output/
            ├── table.py            # Rich-formatted terminal output
            └── json.py             # Machine-readable output for piping

tests/
├── unit/                           # Mirrors src/ structure exactly, 1:1
├── integration/                    # Cross-module (e.g. engine + real framework data)
├── fixtures/                       # Sample rules/evidence — reuses examples/*.json,
│                                   # doesn't duplicate them
└── conftest.py

pyproject.toml
.gitignore                          # Flagged missing in Phase E — needed before this lands
```

**Why this shape:**
- `core/` has zero dependencies on `frameworks/`, `engine/`, or `api/` — it's pure data models, so everything else can depend on it without circular imports
- `frameworks/registry.py` uses Python entry points so a commercial framework package (e.g. `compliance-as-code-cmmc-l1`, sold separately) can be `pip install`ed and auto-discovered, without this public repo ever importing proprietary code
- `engine/plugins/` is intentionally pluggable — CMMC and HIPAA rules aren't checked the same way, and new evaluator types (Terraform state inspection, cloud API calls) get added without touching the core evaluator
- `ai/` is isolated behind a provider interface so you're never locked into one vendor, and rule generation is explicitly one-way (draft → human review), never auto-publish, matching the "not a guarantee of compliance" language already in your FAQ/DISCLAIMER

---

## 2. Rule Engine

**Core loop:** `RuleEvaluator.evaluate(rule: ComplianceRule, evidence: EvidenceRecord | Target) -> EvaluationResult`

Three evaluation modes, matching what's realistic per control type:
1. **Automated** — plugin inspects a real target (file, config, API response) and returns pass/fail deterministically
2. **Evidence-based** — an `EvidenceRecord` already exists (status: `validated`) and the engine checks its `expires_at` and links it to the control
3. **Manual** — control is flagged `automation_ready: false` in metadata; engine returns `not_applicable` with a note directing to human review, never fakes a pass

`pipeline.py` runs a full framework against a target and produces a report — this is the direct, buildable path to the "Evidence to Report" workflow already described in your Cloud Permission Risk Review Toolkit, generalized to any framework instead of just AWS IAM.

---

## 3. Schema Validation

`schemas/validator.py` loads the three schemas already live at `docs/schemas/*.json` directly — **not** a copy baked into the Python package. At package build time, a `scripts/` step copies the current schema files into `src/compliance_as_code/schemas/data/` so the published package is self-contained, but the source of truth stays the public repo's `docs/schemas/`. This prevents the exact kind of drift Phase E caught everywhere else (two copies of the same thing silently diverging).

`json-validation.yml` (already in CI) gets a new companion check once `src/` has code: a test asserting the packaged schema copy is byte-identical to `docs/schemas/` — fails CI immediately if someone updates one and forgets the other.

---

## 4. Compliance Framework Abstraction

```python
class Framework(ABC):
    slug: str                      # e.g. "cmmc-level-1"
    metadata: FrameworkMetadata    # matches framework-metadata.schema.json exactly

    def rules(self) -> list[ComplianceRule]: ...
    def rule(self, control_id: str) -> ComplianceRule: ...
    def search(self, query: str) -> list[ComplianceRule]: ...
```

Commercial frameworks (the actual paid rule libraries) implement this as separate, privately-published packages — e.g. a customer who bought CMMC Level 1 `pip install`s `fst-compliance-cmmc-l1`, which registers itself via entry point. The public `compliance_as_code` package never contains proprietary rule content, matching CONTRIBUTING.md's existing "Commercial Content" exclusion and FAQ.md's "rule libraries are not included in this repository" — the architecture enforces what the docs already promise, rather than contradicting it.

---

## 5. Search Engine

v1.0: SQLite FTS5 (full-text search), built in-memory or to a local `.db` file from whatever `Framework` packages are installed. No external search service dependency for v1.0 — Elasticsearch/OpenSearch is a fair v2.0 conversation once there's a hosted multi-tenant API, not before.

Search surfaces: `control_id` exact match, `title`/`guidance` full-text, filter by `framework`, `tags`, `metadata.family`, `metadata.status`. This directly powers both `cli/commands/search.py` and `api/routers/search.py` — one index, two front ends.

---

## 6. CLI

Built on Typer (not argparse/Click directly) for auto-generated `--help` and type-safe arguments with minimal boilerplate.

```
compliance-as-code validate <file.json>              # validates against the 3 public schemas
compliance-as-code frameworks list                    # lists installed framework packages
compliance-as-code search "account management"        # full-text search across installed frameworks
compliance-as-code evaluate --framework cmmc-level-1 --target ./my-project
compliance-as-code report --framework cmmc-level-1 --format markdown
```

`validate` works with **zero paid frameworks installed** — it's useful against your own public `examples/*.json` files immediately, which makes it a real, working, demonstrable open-source tool from day one, not just a stub waiting for commercial add-ons.

---

## 7. REST API

FastAPI, matching your existing OpenAPI spec's 6 paths exactly for v1.0 parity, plus 2 new ones the spec doesn't have yet (`/evaluate`, `/search`) — I'd update `docs/api/openapi.yaml` alongside actual endpoint implementation, not after, so the public spec never drifts from real behavior (the exact class of bug we spent Phases E/Addendum/F fixing in documentation).

Auth: API key header for v1.0 (`X-API-Key`), OAuth2/enterprise SSO deferred to a later version — matches "REST API services are planned for future releases" already in your FAQ, and avoids over-building auth infrastructure before there's a paying API customer to validate it against.

---

## 8. AI Integration Layer

Two distinct, clearly-separated capabilities — deliberately not blended into one "AI does compliance" black box, because that would contradict your own FAQ's "do not guarantee compliance" and DISCLAIMER's positioning:

- **AI rule generation** (`ai/rule_generation.py`) — given source regulatory text, drafts a candidate rule matching `compliance-rule.schema.json`. Output is always `status: draft`, always requires a human to review and flip to `active` before it enters any framework package. This is an internal authoring tool for you, not a customer-facing feature in v1.0.
- **AI evidence validation** (`ai/evidence_validation.py`) — given a submitted `EvidenceRecord`, an LLM provides an advisory plausibility opinion (does this evidence plausibly satisfy this control's guidance) — surfaced as a suggestion in a report, never silently auto-flips evidence `status` to `validated`. A human always makes that call.

---

## 9. Testing Strategy

- **Unit tests** (`tests/unit/`) mirror `src/` 1:1 — every module gets a corresponding test module
- **Schema conformance tests** — every file in `examples/*.json` is asserted valid against its schema in CI (this test would have caught nothing new today since your examples are already valid, but it's the regression guard going forward)
- **Integration tests** — engine + a real (public, non-proprietary) sample framework built from `examples/` data, since commercial framework packages can't be test dependencies of the public repo
- **Coverage target**: 90% for `core/`, `engine/`, `schemas/` (the trust-critical paths); 70% floor for `api/`, `cli/` (more integration-tested than unit-tested by nature)
- New CI workflow needed: `.github/workflows/python-tests.yml`, triggered on `src/**` and `tests/**` — doesn't exist yet, flagged in the Phase E audit as a pre-code requirement

---

## 10. Packaging and Release Strategy

- `pyproject.toml` (PEP 621), built with `hatchling` or `setuptools` — either is fine, `hatchling` has less legacy config surface
- SemVer from v0.1.0 (pre-1.0 = API may still shift) through v1.0.0 (first stable public API contract)
- Published to PyPI as `compliance-as-code` if available, `fst-compliance-as-code` as fallback — worth checking availability before the first release, not after
- `CHANGELOG.md` (already exists at root) becomes the real release changelog starting with v0.1.0 — currently likely still describing the doc-repo-only phase
- Release workflow: tag `v*` → GitHub Actions builds + publishes to PyPI + creates a GitHub Release with changelog excerpt — new workflow, doesn't exist yet
- Commercial framework packages follow the same PyPI-private-index or direct-download-with-license-key pattern — decide this once the first paying API customer is closer, not speculatively now

---

## What Should Exist Before Any Code Lands (carried over from Phase E's Future Readiness section)

1. `.gitignore` at root — real risk once `src/` produces `__pycache__/`, `.pytest_cache/`, `*.egg-info/`
2. `pyproject.toml` — formally establishes the package before the first module is written
3. `.github/workflows/python-tests.yml` — CI should exist before the first test does, not after
4. A decision on PyPI package name availability

None of these require touching repository structure again — they're additive, and fit cleanly into the `src/`, `tests/`, root-level scaffolding already in place from Phase D.
