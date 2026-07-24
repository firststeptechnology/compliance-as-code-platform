# GitHub Actions Integration

The First Step Technology LLC Compliance-as-Code Platform can be integrated into GitHub Actions to automatically validate compliance rule libraries during software development and release workflows.

---

# Typical Workflow

```text
Developer Commit
        │
        ▼
GitHub Actions
        │
        ▼
Validate JSON
        │
        ▼
Validate JSON Schema
        │
        ▼
Compliance Checks
        │
        ▼
Pass / Fail
```

---

# Benefits

Using GitHub Actions allows organizations to:

- Validate Compliance-as-Code rule libraries
- Detect formatting errors
- Verify JSON Schema compliance
- Prevent invalid rule objects from entering production
- Automate quality assurance
- Support continuous compliance initiatives

---

# Example Workflow

```yaml
name: Validate Compliance Rule

on:
  workflow_dispatch:

jobs:

  validate:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install jsonschema

      - run: |
          echo "Validate compliance rules here."
```

---

# Common Validation Tasks

Typical automation includes:

- Validate JSON syntax
- Validate JSON Schema
- Verify required fields
- Detect duplicate control IDs
- Check schema version
- Verify metadata
- Generate validation reports

---

# CI/CD Benefits

Compliance validation becomes part of the normal software development lifecycle.

Benefits include:

- Earlier detection of errors
- Repeatable validation
- Automated quality control
- Consistent rule formatting
- Reduced manual review

---

# Related Documentation

- Documentation Home
- JSON Schemas
- Examples
- API Documentation

---

© 2026 First Step Technology LLC. All rights reserved.
