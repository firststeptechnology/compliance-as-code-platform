# Jenkins Integration

The First Step Technology LLC Compliance-as-Code Platform integrates with Jenkins to automate compliance validation during continuous integration and continuous delivery (CI/CD) workflows.

---

# Overview

Jenkins pipelines can validate Compliance-as-Code rule libraries before software, infrastructure, or configuration changes are promoted to production environments.

Typical objectives include:

- Continuous Compliance
- DevSecOps
- Governance Automation
- Security Validation
- Audit Readiness
- Release Quality

---

# Typical Workflow

```text
Developer Commit
        │
        ▼
Git Repository
        │
        ▼
Jenkins Pipeline
        │
        ▼
JSON Validation
        │
        ▼
JSON Schema Validation
        │
        ▼
Compliance Validation
        │
        ▼
Pass / Fail
        │
        ▼
Deployment
```

---

# Example Jenkins Pipeline

```groovy
pipeline {

    agent any

    stages {

        stage('Validate Compliance Rules') {

            steps {

                sh 'pip install jsonschema'

                sh 'echo "Run Compliance-as-Code validation here."'

            }

        }

    }

}
```

---

# Common Validation Tasks

Typical Jenkins automation includes:

- Validate JSON syntax
- Validate JSON Schema
- Verify required fields
- Detect duplicate control IDs
- Validate metadata
- Verify schema versions
- Generate compliance reports

---

# Benefits

Using Jenkins with Compliance-as-Code helps organizations:

- Improve deployment quality
- Reduce manual compliance reviews
- Automate validation
- Standardize governance workflows
- Increase audit readiness
- Support continuous compliance initiatives

---

# Best Practices

Recommended implementation practices include:

- Validate every build
- Store schemas in version control
- Automate compliance testing
- Archive validation reports
- Track schema versions
- Review failed validations before deployment

---

# Related Documentation

- Documentation Home
- API Documentation
- JSON Schemas
- Examples
- GitHub Actions Integration
- Azure DevOps Integration
- GitLab CI/CD Integration
- Python Integration
- Terraform Integration

---

© 2026 First Step Technology LLC. All rights reserved.
