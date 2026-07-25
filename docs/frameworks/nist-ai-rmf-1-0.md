# NIST AI Risk Management Framework (AI RMF) 1.0 Compliance-as-Code Rule Library

> Machine-readable implementation of the 72 NIST AI Risk Management Framework (AI RMF) 1.0 subcategories.

## Overview

The **NIST AI Risk Management Framework (AI RMF) 1.0 Compliance-as-Code Rule Library** transforms the framework's 72 subcategories into structured, machine-readable JSON for AI governance, compliance automation, enterprise risk management, and responsible AI implementation.

Designed for organizations deploying, governing, or assessing AI systems, the library enables AI risk requirements to be integrated into security workflows, governance platforms, development pipelines, and AI-assisted compliance processes.

---

## Framework Information

| Property | Value |
|---|---|
| Framework | NIST AI Risk Management Framework 1.0 |
| Publisher | National Institute of Standards and Technology |
| Coverage | 72 Subcategories |
| Core Functions | Govern, Map, Measure, Manage |
| Delivery Format | Structured JSON |
| Versioning | Supported |
| Commercial Status | Available |

---

## AI RMF Functions

The commercial library includes all subcategories across the four AI RMF functions:

- Govern (GV)
- Map (MP)
- Measure (MS)
- Manage (MG)

---

## Intended Audience

Designed for:

- AI Governance Teams
- Chief AI Officers
- Risk Managers
- Security Engineers
- Compliance Teams
- Internal Audit
- Legal & Privacy Professionals
- Enterprise Architects
- AI Platform Developers

---

## Rule Structure

Each AI RMF subcategory is represented as structured JSON.

Typical attributes include:

- Subcategory Identifier
- Function
- Category
- Plain-English Guidance
- Agent-Ready Instruction
- Framework Metadata
- Version Information
- Traceability Metadata

The commercial edition includes additional proprietary fields supporting AI governance automation and enterprise integrations.

---

## Illustrative Example

```json
{
  "control_id": "GV-1.1",
  "function": "Govern",
  "title": "AI Governance Policies",
  "guidance": "Establish governance processes for AI systems throughout their lifecycle.",
  "agent_instruction": "Verify documented governance processes exist for AI development, deployment, monitoring, and retirement."
}
```

> This example is illustrative only and does not represent a complete commercial rule.

---

## Common Use Cases

Organizations use this library for:

- AI Governance Programs
- Responsible AI initiatives
- AI Risk Assessments
- AI Compliance Automation
- AI Security Reviews
- Internal Audit
- Executive Reporting
- Continuous AI Governance

---

## Integration Opportunities

Designed for integration with:

- AI Governance Platforms
- GitHub Actions
- GitLab CI/CD
- Azure DevOps
- Internal GRC Platforms
- Python Automation
- AI Assistants
- Enterprise Dashboards

---

## Related Products

- NIST Cybersecurity Framework 2.0
- NIST SP 800-53 Rev. 5
- HIPAA Security Rule
- CCPA / CPRA

---

## Commercial Licensing

The complete AI RMF Compliance-as-Code Rule Library is a proprietary commercial product of First Step Technology LLC.

This repository provides documentation and illustrative examples only.

---

© 2026 First Step Technology LLC. All Rights Reserved.
