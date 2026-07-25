# Examples

This directory contains public examples demonstrating how the First Step Technology LLC Compliance-as-Code Platform can be integrated into applications, automation workflows, AI systems, and DevSecOps pipelines.

The examples are intentionally simplified and are provided for educational purposes only.

Commercial products include additional metadata, validation logic, enrichment, and automation capabilities.

---

# Contents

| File | Purpose |
|------|---------|
| compliance-rule-example.json | Example compliance rule |
| framework-metadata-example.json | Example framework metadata |
| evidence-record-example.json | Example evidence record |
| compliance-report.md | Sample generated report |
| python-example.py | Read a compliance rule |
| validate-rule.py | Validate JSON against the schema |
| search-controls.py | Search rule data |
| generate-report.py | Generate a Markdown report |
| requirements.txt | Python dependencies |
| github-actions-example.yml | GitHub Actions workflow |
| azure-pipelines.yml | Azure DevOps pipeline |
| gitlab-ci.yml | GitLab CI pipeline |
| Jenkinsfile | Jenkins pipeline |
| terraform-example.tf | Terraform integration |
| api-response-example.json | Example REST API response |

---

# Getting Started

Install the required dependency:

```bash
pip install -r requirements.txt
```

Run the validator:

```bash
python validate-rule.py
```

Search for a control:

```bash
python search-controls.py
```

Generate a report:

```bash
python generate-report.py
```

---

# Example Rule

```json
{
  "schema_version": "1.0.0",
  "framework": "NIST SP 800-53 Rev. 5",
  "control_id": "AC-2",
  "title": "Account Management",
  "guidance": "Manage information system accounts throughout their lifecycle.",
  "agent_instruction": "Verify documented account lifecycle procedures."
}
```

---

# Intended Audience

These examples are useful for:

- Developers
- Security Engineers
- Compliance Teams
- Internal Audit
- DevSecOps Teams
- GRC Professionals
- AI Developers
- Solution Architects

---

# Compatibility

The public examples are designed to work alongside the JSON schemas located in:

```
docs/schemas/
```

They may be used for testing, learning, validation, and proof-of-concept integrations.

---

# Commercial Platform

The commercial Compliance-as-Code Platform includes:

- Complete rule libraries
- Framework mappings
- Enhanced metadata
- Version management
- Lifecycle tracking
- AI optimization
- Enterprise integrations
- Premium documentation

---

# Related Documentation

- [Documentation Home](../docs/README.md)
- [JSON Schemas](../docs/schemas/README.md)
- [Framework Documentation](../docs/frameworks/README.md)
- [Product Catalog](../CATALOG.md)
- [Platform Roadmap](../ROADMAP.md)

---

© 2026 First Step Technology LLC. All rights reserved.
