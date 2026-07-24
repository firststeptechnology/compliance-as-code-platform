# NIST SP 800-171 Revision 2 Compliance-as-Code Rule Library

> Machine-readable implementation of the 110 security requirements from NIST Special Publication 800-171 Revision 2.

---

# Overview

The **NIST SP 800-171 Revision 2 Compliance-as-Code Rule Library** converts the publication's 110 security requirements into structured, machine-readable JSON for compliance automation, AI-assisted workflows, Governance, Risk & Compliance (GRC), and secure software development.

The library enables organizations to consume NIST requirements as standardized data instead of manually interpreting lengthy documentation.

---

# Framework Information

| Property | Value |
|----------|-------|
| Framework | NIST SP 800-171 Revision 2 |
| Publisher | National Institute of Standards and Technology (NIST) |
| Security Requirements | 110 |
| Requirement Families | 14 |
| Format | Structured JSON |
| Versioning | Supported |
| Commercial Availability | Available |

---

# Requirement Families

The commercial library includes requirements across all fourteen NIST SP 800-171 families:

- Access Control (AC)
- Awareness and Training (AT)
- Audit and Accountability (AU)
- Configuration Management (CM)
- Identification and Authentication (IA)
- Incident Response (IR)
- Maintenance (MA)
- Media Protection (MP)
- Personnel Security (PS)
- Physical Protection (PE)
- Risk Assessment (RA)
- Security Assessment (CA)
- System and Communications Protection (SC)
- System and Information Integrity (SI)

---

# Intended Audience

This library is designed for:

- Defense contractors
- Organizations handling Controlled Unclassified Information (CUI)
- Security engineers
- GRC professionals
- DevSecOps teams
- Compliance consultants
- Software developers
- Internal audit teams

---

# Rule Structure

Each requirement is represented as a structured JSON object.

Typical attributes include:

- Requirement Identifier
- Requirement Title
- Plain-English Guidance
- Agent-Ready Instruction
- Framework Metadata
- Requirement Family
- Version Information
- Traceability Metadata

Additional proprietary attributes are included in the commercial release.

---

# Example (Illustrative)

```json
{
  "control_id": "3.1.1",
  "family": "Access Control",
  "title": "Limit system access",
  "guidance": "Limit information system access to authorized users, processes acting on behalf of authorized users, and devices.",
  "agent_instruction": "Verify authentication and authorization controls are enforced for all covered systems."
}
```

> This example is provided for illustration only and does not represent the complete commercial rule library.

---

# Common Use Cases

Organizations use this library to support:

- NIST 800-171 compliance programs
- CMMC Level 2 readiness
- Compliance automation
- Internal assessments
- Continuous compliance
- Secure software development
- AI-assisted compliance reviews
- Evidence collection
- Executive reporting

---

# Integration Opportunities

Designed for integration with:

- GitHub Actions
- GitLab CI/CD
- Azure DevOps
- Jenkins
- Python automation
- Internal GRC platforms
- AI assistants
- Security dashboards
- Compliance reporting systems

---

# Relationship to CMMC Level 2

CMMC Level 2 incorporates the 110 security requirements from NIST SP 800-171 Revision 2 as its technical foundation while adding assessment and certification requirements established by the CMMC Program.

Organizations pursuing CMMC Level 2 frequently use both rule libraries together.

---

# Commercial Licensing

The complete Compliance-as-Code Rule Library is a commercial product provided by First Step Technology LLC.

This repository contains documentation and illustrative examples only.

---

# Related Products

- CMMC Level 1 Compliance-as-Code Rule Library
- CMMC Level 2 Compliance-as-Code Rule Library
- NIST SP 800-53 Rev. 5 Core Controls Rule Library

---

# Learn More

Additional product information, licensing, and purchasing details are available through First Step Technology LLC.

---

© 2026 First Step Technology LLC. All Rights Reserved.
