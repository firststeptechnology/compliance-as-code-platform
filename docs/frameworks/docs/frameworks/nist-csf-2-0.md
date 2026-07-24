# NIST Cybersecurity Framework (CSF) 2.0 Compliance-as-Code Rule Library

> Machine-readable implementation of the 106 NIST Cybersecurity Framework (CSF) 2.0 subcategories.

## Overview

The **NIST Cybersecurity Framework (CSF) 2.0 Compliance-as-Code Rule Library** converts the framework's 106 subcategories into structured, machine-readable JSON for cybersecurity governance, compliance automation, DevSecOps, AI-assisted security operations, and enterprise risk management.

The library enables organizations to consume the CSF as standardized data suitable for automation rather than manually interpreting framework documentation.

---

## Framework Information

| Property | Value |
|---|---|
| Framework | NIST Cybersecurity Framework 2.0 |
| Publisher | National Institute of Standards and Technology |
| Coverage | 106 Subcategories |
| Functions | Govern, Identify, Protect, Detect, Respond, Recover |
| Delivery Format | Structured JSON |
| Versioning | Supported |
| Commercial Status | Available |

---

## CSF Functions

The commercial library includes every subcategory across the six CSF Functions:

- Govern (GV)
- Identify (ID)
- Protect (PR)
- Detect (DE)
- Respond (RS)
- Recover (RC)

---

## Intended Audience

Designed for:

- Enterprise security teams
- CISOs
- GRC professionals
- Security consultants
- Risk managers
- DevSecOps teams
- Cloud security engineers
- Internal audit teams

---

## Rule Structure

Each subcategory is represented as structured JSON.

Typical attributes include:

- Subcategory Identifier
- Function
- Category
- Plain-English Guidance
- Agent-Ready Instruction
- Framework Metadata
- Version Information
- Traceability Metadata

Additional proprietary automation fields are included within the commercial edition.

---

## Illustrative Example

```json
{
  "control_id": "GV.OC-01",
  "function": "Govern",
  "title": "Organizational Context",
  "guidance": "Understand organizational mission and stakeholder expectations.",
  "agent_instruction": "Verify governance documentation defines cybersecurity objectives aligned to business goals."
}
```

> This example is illustrative only.

---

## Common Use Cases

- Cybersecurity program development
- Executive reporting
- Security maturity assessments
- Continuous compliance
- AI-assisted governance
- Risk management
- Internal audits
- Framework mapping

---

## Integration Opportunities

- GitHub Actions
- GitLab CI/CD
- Azure DevOps
- Jenkins
- Python
- Internal GRC Platforms
- AI Assistants
- Security Dashboards

---

## Commercial Licensing

The complete rule library is a proprietary commercial product of First Step Technology LLC.

This repository contains documentation and illustrative examples only.

---

## Related Products

- NIST SP 800-53 Rev. 5
- NIST SP 800-171 Rev. 2
- NIST AI RMF 1.0

---

© 2026 First Step Technology LLC. All Rights Reserved.
