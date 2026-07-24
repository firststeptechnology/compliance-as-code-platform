# Azure DevOps Integration

The First Step Technology LLC Compliance-as-Code Platform integrates with Azure DevOps to help organizations automate compliance validation throughout the software development lifecycle.

---

# Overview

Azure DevOps pipelines can execute validation workflows that ensure compliance rule libraries and supporting artifacts meet organizational standards before deployment.

Typical uses include:

- Continuous Compliance
- DevSecOps
- Security Gates
- Release Validation
- Governance Automation
- Audit Readiness

---

# Typical Workflow

```text
Developer Commit
        │
        ▼
Azure Repos
        │
        ▼
Azure Pipelines
        │
        ▼
Compliance Validation
        │
        ▼
JSON Schema Validation
        │
        ▼
Security Review
        │
        ▼
Deploy or Reject
```

---

# Example Pipeline

```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:

- checkout: self

- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.12'

- script: |
    pip install jsonschema
    echo "Run compliance validation here."
  displayName: Validate Compliance Rules
```

---

# Common Validation Tasks

Organizations commonly automate:

- JSON validation
- JSON Schema validation
- Required field verification
- Duplicate control detection
- Metadata validation
- Version verification
- Compliance reporting

---

# Benefits

Integrating Compliance-as-Code into Azure DevOps helps organizations:

- Detect compliance issues earlier
- Improve deployment quality
- Standardize validation processes
- Reduce manual reviews
- Support continuous compliance initiatives
- Increase audit readiness

---

# Best Practices

Recommended implementation practices include:

- Validate every pull request
- Version control rule libraries
- Automate schema validation
- Generate pipeline reports
- Document validation failures
- Review exceptions through change management

---

# Related Documentation

- Documentation Home
- API Documentation
- JSON Schemas
- Examples
- GitHub Actions Integration
- Python Integration
- Terraform Integration

---

© 2026 First Step Technology LLC. All rights reserved.
