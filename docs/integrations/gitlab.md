# GitLab CI/CD Integration

The First Step Technology LLC Compliance-as-Code Platform can integrate with GitLab CI/CD to automate compliance validation as part of software delivery pipelines.

---

# Overview

GitLab CI/CD enables organizations to validate Compliance-as-Code rule libraries before applications and infrastructure are deployed.

Typical objectives include:

- Continuous Compliance
- DevSecOps
- Governance Automation
- Security Validation
- Compliance Reporting
- Release Quality

---

# Typical Workflow

```text
Developer Push
        │
        ▼
GitLab Repository
        │
        ▼
GitLab Pipeline
        │
        ▼
JSON Validation
        │
        ▼
JSON Schema Validation
        │
        ▼
Compliance Review
        │
        ▼
Pass / Fail
```

---

# Example Pipeline

```yaml
stages:
  - validate

validate-compliance:
  image: python:3.12

  stage: validate

  script:
    - pip install jsonschema
    - echo "Run Compliance-as-Code validation here."
```

---

# Common Validation Tasks

Organizations typically automate:

- JSON syntax validation
- JSON Schema validation
- Required field verification
- Duplicate control detection
- Metadata validation
- Rule version validation
- Compliance reporting

---

# Benefits

Integrating Compliance-as-Code into GitLab CI/CD provides:

- Earlier issue detection
- Automated validation
- Repeatable quality assurance
- Reduced manual effort
- Continuous compliance
- Improved audit readiness

---

# Best Practices

Recommended practices include:

- Validate every merge request
- Store schemas in version control
- Automate validation in every pipeline
- Review validation reports
- Track schema versions
- Document approved exceptions

---

# Related Documentation

- Documentation Home
- API Documentation
- JSON Schemas
- Examples
- GitHub Actions Integration
- Azure DevOps Integration
- Python Integration
- Terraform Integration

---

© 2026 First Step Technology LLC. All rights reserved.
