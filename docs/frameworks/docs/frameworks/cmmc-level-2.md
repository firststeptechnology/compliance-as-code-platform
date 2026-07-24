# CMMC Level 2 Compliance-as-Code Rule Library

> Machine-readable implementation of the 110 CMMC Level 2 security requirements.

## Overview

The **CMMC Level 2 Compliance-as-Code Rule Library** provides structured JSON representing the 110 CMMC Level 2 security requirements for compliance automation, AI-assisted governance, DevSecOps, and enterprise security programs.

---

## Framework Information

| Property | Value |
|---|---|
| Framework | CMMC Level 2 |
| Coverage | 110 Security Requirements |
| Foundation | NIST SP 800-171 Rev. 2 |
| Format | Structured JSON |
| Versioning | Supported |
| Commercial Status | Available |

---

## Intended Audience

- Defense Contractors
- DIB Suppliers
- Compliance Consultants
- Security Engineers
- GRC Teams
- DevSecOps Teams
- Internal Audit

---

## Rule Structure

Each requirement includes:

- Requirement Identifier
- Requirement Family
- Plain-English Guidance
- Agent-Ready Instruction
- Framework Metadata
- Version Metadata
- Traceability Information

---

## Example

```json
{
  "control_id": "AC.L2-3.1.1",
  "title": "Limit System Access",
  "guidance": "Limit information system access to authorized users.",
  "agent_instruction": "Verify authentication and authorization controls are enforced."
}
```

---

## Common Use Cases

- CMMC Readiness
- Internal Assessments
- Continuous Compliance
- Evidence Collection
- AI Compliance Reviews
- Executive Reporting

---

## Integrations

- GitHub Actions
- Azure DevOps
- GitLab
- Jenkins
- Python
- AI Assistants
- GRC Platforms

---

## Related Products

- NIST SP 800-171 Rev. 2
- CMMC Level 1
- NIST SP 800-53 Rev. 5

---

## Commercial Licensing

This repository contains documentation only.

The complete rule library is a proprietary commercial product of First Step Technology LLC.

---

© 2026 First Step Technology LLC.
