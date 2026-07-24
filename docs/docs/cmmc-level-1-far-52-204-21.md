# CMMC Level 1 Compliance-as-Code Rule Library

> Machine-readable implementation of the 15 FAR 52.204-21 Basic Safeguarding Requirements.

---

# Overview

The **CMMC Level 1 Compliance-as-Code Rule Library** transforms the 15 safeguarding requirements from **FAR 52.204-21** into structured, machine-readable JSON suitable for compliance automation, AI-assisted workflows, and security engineering.

Rather than reading regulatory text manually, organizations can integrate standardized rule objects directly into internal tooling, governance processes, or development pipelines.

---

# Framework Information

| Property | Value |
|----------|-------|
| Framework | Cybersecurity Maturity Model Certification (CMMC) Level 1 |
| Regulatory Source | FAR 52.204-21 |
| Requirements | 15 |
| Format | Structured JSON |
| Versioning | Supported |
| Commercial Availability | Available |

---

# Intended Audience

This library is designed for:

- Defense contractors
- Small businesses entering the Defense Industrial Base (DIB)
- Managed Service Providers (MSPs)
- Compliance consultants
- Security engineers
- Governance, Risk & Compliance (GRC) teams
- Software developers building compliance automation

---

# Rule Structure

Each rule is represented as a structured JSON object.

Typical attributes include:

- Control Identifier
- Requirement Title
- Plain-English Guidance
- Agent-Ready Instruction
- Framework Metadata
- Version Information
- Traceability Metadata

The exact commercial schema contains additional proprietary fields used for automation and lifecycle management.

---

# Example (Illustrative)

```json
{
  "control_id": "AC.L1-3.1.1",
  "title": "Limit system access",
  "guidance": "Limit information system access to authorized users, processes acting on behalf of authorized users, and devices.",
  "agent_instruction": "Verify authentication and authorization controls are implemented before granting access."
}
```

> The example above is illustrative and does not represent the complete commercial rule.

---

# Common Use Cases

Organizations use this library to support:

- Compliance automation
- Internal assessments
- Secure software development
- AI-assisted compliance reviews
- DevSecOps workflows
- Policy development
- Evidence collection
- Readiness assessments

---

# Integration Opportunities

The rule library is designed to integrate with workflows such as:

- GitHub Actions
- GitLab CI/CD
- Azure DevOps
- Jenkins
- Custom Python automation
- Internal GRC platforms
- AI assistants
- Compliance dashboards

---

# Commercial Licensing

The complete Compliance-as-Code Rule Library is a commercial product provided by First Step Technology LLC.

This repository includes public documentation and examples only.

---

# Related Products

- CMMC Level 2 Compliance-as-Code Rule Library
- NIST SP 800-171 Rev. 2 Compliance-as-Code Rule Library
- NIST SP 800-53 Rev. 5 Core Controls Rule Library

---

# Learn More

Additional information, licensing, and purchasing details are available through First Step Technology LLC.

---

© 2026 First Step Technology LLC. All Rights Reserved.# FAR 52.204-21 Compliance-as-Code Rule Library

## Machine-Readable Basic Safeguarding Requirements

Stop manually re-reading FAR 52.204-21 every time you need to evaluate a system against CMMC Level 1 safeguarding requirements.

The FAR 52.204-21 Compliance-as-Code Rule Library converts all 15 Basic Safeguarding Requirements into structured JSON that can be integrated into AI-assisted development, compliance workflows, security reviews, and automation tools.

Developed by **First Step Technology LLC**.

---

## What Is FAR 52.204-21?

FAR 52.204-21 establishes basic safeguarding requirements and procedures for contractor information systems that process, store, or transmit Federal Contract Information.

These requirements are commonly associated with foundational cybersecurity obligations for organizations working within or supporting the federal defense supply chain.

---

## What Is Included?

The commercial rule library includes:

- All 15 FAR 52.204-21 Basic Safeguarding Requirements
- A documented, machine-readable JSON schema
- An actionable instruction for every requirement
- Traceability to the applicable regulatory text
- Plain UTF-8 JSON
- No proprietary software requirements
- A current regulatory snapshot
- Internal-use licensing for one organization

---

## Who Is This For?

This rule library is designed for:

- Small defense subcontractors
- MSPs supporting DoD-adjacent clients
- Cybersecurity and GRC professionals
- Software developers
- DevSecOps teams
- Compliance engineers
- AI-assisted development workflows
- Organizations preparing for CMMC Level 1

---

## Potential Uses

The rule library may be incorporated into:

- AI coding assistant system prompts
- Internal compliance review tools
- CI/CD compliance gates
- GRC workflows
- Security questionnaires
- Readiness assessments
- Control validation tools
- Evidence collection workflows
- Compliance dashboards

---

## Example Structure

The following simplified example demonstrates the type of structured information represented by the rule library.

```json
{
  "requirement_id": "example-id",
  "framework": "FAR 52.204-21",
  "requirement": "Example safeguarding requirement",
  "machine_actionable_instruction": "Evaluate whether the system satisfies the specified safeguarding requirement.",
  "source": "48 CFR 52.204-21"
}
