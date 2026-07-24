# Compliance-as-Code Examples

This directory contains working examples that demonstrate how developers can integrate the First Step Technology LLC Compliance-as-Code Platform into their own applications and automation workflows.

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

# Intended Audience

These examples are intended for:

- Developers
- Security Engineers
- GRC Teams
- Compliance Professionals
- Internal Audit
- DevSecOps Engineers
- AI Developers
- Solution Architects

---

# Related Documentation

- ../README.md
- ../schemas/
- ../api/
- ../integrations/

---

© 2026 First Step Technology LLC. All rights reserved.
