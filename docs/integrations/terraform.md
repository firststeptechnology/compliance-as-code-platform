# Terraform Integration

The First Step Technology LLC Compliance-as-Code Platform can be incorporated into Infrastructure-as-Code (IaC) workflows using Terraform to support automated governance, security validation, and continuous compliance.

---

# Overview

Terraform enables organizations to provision and manage cloud infrastructure through code.

By integrating Compliance-as-Code rule libraries into Terraform workflows, security and compliance checks can occur before infrastructure is deployed.

---

# Typical Workflow

```text
Terraform Configuration
          │
          ▼
Terraform Plan
          │
          ▼
Compliance Rule Validation
          │
          ▼
Policy Evaluation
          │
          ▼
Approve or Reject Deployment
          │
          ▼
Terraform Apply
```

---

# Common Use Cases

Organizations commonly use Terraform integrations to:

- Validate cloud infrastructure
- Support continuous compliance
- Enforce security baselines
- Verify configuration standards
- Reduce deployment risk
- Standardize infrastructure reviews

---

# Supported Cloud Platforms

Terraform integrations may be used with:

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud Platform (GCP)
- Oracle Cloud Infrastructure (OCI)
- VMware
- Kubernetes

---

# Example Workflow

```text
Developer
     │
     ▼
Git Repository
     │
     ▼
Terraform Plan
     │
     ▼
Compliance Validation
     │
     ▼
Security Review
     │
     ▼
Deployment
```

---

# Benefits

Using Terraform together with Compliance-as-Code provides:

- Repeatable infrastructure validation
- Automated compliance checks
- Reduced manual review
- Faster deployments
- Improved governance
- Better audit readiness

---

# Best Practices

Recommended practices include:

- Validate infrastructure before deployment
- Store compliance rules in version control
- Review changes through pull requests
- Integrate validation into CI/CD pipelines
- Maintain versioned compliance libraries
- Document exceptions when required

---

# Related Documentation

- Documentation Home
- JSON Schemas
- Examples
- API Documentation
- GitHub Actions Integration
- Python Integration

---

© 2026 First Step Technology LLC. All rights reserved.
