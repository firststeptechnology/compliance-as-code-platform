# FAR 52.204-21 Compliance-as-Code Rule Library

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
