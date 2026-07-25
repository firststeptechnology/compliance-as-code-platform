# First Step Technology LLC Compliance-as-Code Platform

Machine-readable compliance rule libraries designed for AI, DevSecOps, Governance, Risk & Compliance (GRC), cloud security, and enterprise compliance automation.

---

## Overview

The First Step Technology LLC Compliance-as-Code Platform transforms regulatory frameworks into structured, machine-readable rule libraries suitable for modern engineering and governance workflows.

Rather than manually interpreting lengthy publications, organizations can consume standardized JSON objects that integrate directly into internal tooling, AI assistants, CI/CD pipelines, compliance platforms, and security operations.

This public repository serves as the developer portal for the platform.

It contains documentation, examples, schemas, roadmap information, and integration guidance.

The complete commercial rule libraries are licensed separately.

---

# Current Commercial Products

| Product | Coverage | Status |
|---|---:|:---:|
| CMMC Level 1 Compliance-as-Code | 15 Requirements | ✅ |
| CMMC Level 2 Compliance-as-Code | 110 Requirements | ✅ |
| NIST SP 800-171 Rev. 2 | 110 Requirements | ✅ |
| NIST SP 800-53 Rev. 5 Core Controls | 324 Controls | ✅ |
| NIST Cybersecurity Framework (CSF) 2.0 | 106 Subcategories | ✅ |
| NIST AI Risk Management Framework 1.0 | 72 Subcategories | ✅ |
| HIPAA Security Rule | 62 Safeguards | ✅ |
| CCPA / CPRA | 27 Privacy Sections | ✅ |

---

# Repository Contents

```
.
├── docs/
├── examples/
├── CATALOG.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── DISCLAIMER.md
├── FAQ.md
├── LICENSE.md
├── ROADMAP.md
├── SECURITY.md
└── SUPPORT.md
```

---

# Documentation

Documentation begins here:

**➡ [docs/README.md](docs/README.md)**

Framework documentation includes:

- [CMMC Level 1](docs/frameworks/cmmc-level-1.md)
- [CMMC Level 2](docs/frameworks/cmmc-level-2.md)
- [NIST SP 800-171 Rev. 2](docs/frameworks/nist-sp-800-171.md)
- [NIST SP 800-53 Rev. 5](docs/frameworks/nist-sp-800-53-rev-5-core-controls.md)
- [NIST CSF 2.0](docs/frameworks/nist-csf-2-0.md)
- [NIST AI RMF 1.0](docs/frameworks/nist-ai-rmf-1-0.md)
- [HIPAA Security Rule](docs/frameworks/hipaa-security-rule.md)
- [CCPA / CPRA](docs/frameworks/ccpa-cpra.md)

---

# Platform Capabilities

The commercial libraries are designed to support:

- Compliance Automation
- AI Governance
- DevSecOps
- Governance, Risk & Compliance (GRC)
- Internal Audit
- Continuous Compliance
- Evidence Collection
- Security Engineering
- Policy-as-Code initiatives
- AI-assisted assessments

---

# Typical Rule Structure

Commercial rule libraries contain structured JSON similar to:

```json
{
  "control_id": "AC-2",
  "framework": "NIST SP 800-53 Rev. 5",
  "title": "Account Management",
  "guidance": "Manage information system accounts throughout their lifecycle.",
  "agent_instruction": "Verify documented account lifecycle procedures are implemented."
}
```

The commercial editions include additional proprietary metadata supporting automation, traceability, lifecycle management, and enterprise integrations.

---

# Typical Integrations

Organizations commonly integrate the platform with:

- GitHub Actions
- GitLab CI/CD
- Azure DevOps
- Jenkins
- Terraform
- Python
- Internal GRC Platforms
- AI Assistants
- Security Dashboards
- Compliance Reporting Systems

---

# Repository Roadmap

See:

**[ROADMAP.md](ROADMAP.md)**

---

# Product Catalog

See:

**[CATALOG.md](CATALOG.md)**

---

# Licensing

This repository contains public documentation, schemas, and illustrative examples.

Commercial Compliance-as-Code rule libraries remain proprietary products of First Step Technology LLC and are licensed separately.

---

# Support

Questions, licensing inquiries, and partnership opportunities are available through First Step Technology LLC.

Website:

https://firststeptechnologyllc.com

Compliance Platform:

https://firststeptechnologyllc.com/compliance-as-code-compliance-automation/

For common questions, see the [FAQ](FAQ.md). To report an issue or contribute, see [CONTRIBUTING.md](CONTRIBUTING.md). For security disclosures, see [SECURITY.md](SECURITY.md). For general support channels, see [SUPPORT.md](SUPPORT.md).

---

© 2026 First Step Technology LLC. All Rights Reserved.
