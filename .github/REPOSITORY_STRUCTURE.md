# Repository Structure

This document describes the high-level organization of the First Step Technology LLC Compliance-as-Code Platform repository.

---

# Top-Level Layout

```
.
├── .github/
├── docs/
├── examples/
├── src/
├── tests/
├── scripts/
├── assets/
├── CATALOG.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── DISCLAIMER.md
├── FAQ.md
├── LICENSE.md
├── README.md
├── ROADMAP.md
├── SECURITY.md
├── SUPPORT.md
└── SUPPORTED_VERSIONS.md
```

---

# .github

Repository automation and community health files.

Contents include:

- GitHub Actions workflows
- Issue templates
- Pull request template
- Funding configuration
- Repository documentation

---

# docs

Primary project documentation.

Includes:

- Architecture
- API documentation
- Examples
- Framework documentation
- Integration guides
- JSON schemas
- Technical documentation
- Roadmaps

---

# docs/api

Contains:

- OpenAPI specification
- API documentation
- Example responses

---

# examples

Contains sample implementations including:

- Python
- Terraform
- GitHub Actions
- Azure DevOps
- GitLab
- Jenkins
- JSON examples

Note: `examples/` is a repository-root-level directory, not nested under `docs/`.

---

# docs/frameworks

Framework reference documentation.

Examples include:

- CMMC
- NIST
- HIPAA
- NIST AI RMF
- NIST CSF

---

# docs/integrations

Platform integration guidance.

Includes:

- Python
- Terraform
- GitHub Actions
- Azure DevOps
- GitLab
- Jenkins

---

# docs/schemas

Machine-readable JSON schemas.

Current schemas:

- Compliance Rule
- Framework Metadata
- Evidence Record

---

# Root Documentation

The repository root contains project-wide documentation including:

- README
- Changelog
- Security Policy
- Contributing Guide
- Code of Conduct
- Supported Versions

---

# Repository Goals

The repository is organized to provide:

- Clear documentation
- Developer onboarding
- Public schemas
- Integration guidance
- Educational resources
- Compliance automation examples

---

© 2026 First Step Technology LLC. All rights reserved.
