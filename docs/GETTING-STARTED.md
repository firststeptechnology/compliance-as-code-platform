# Getting Started

Welcome to the First Step Technology LLC Compliance-as-Code Platform.

This guide introduces the public repository and provides a recommended path for developers evaluating or integrating the platform.

---

# Step 1 — Explore the Documentation

Start with the primary documentation.

Recommended reading order:

1. README
2. Architecture
3. Security Architecture
4. AI Architecture
5. Data Model
6. API Documentation
7. JSON Schemas
8. Examples
9. Integrations

---

# Step 2 — Review Supported Frameworks

Current commercial framework libraries include:

- CMMC Level 1
- CMMC Level 2
- NIST SP 800-171 Rev. 2
- NIST SP 800-53 Rev. 5
- NIST CSF 2.0
- NIST AI RMF 1.0
- HIPAA Security Rule
- CCPA / CPRA

Framework documentation is available under:

```
docs/frameworks/
```

---

# Step 3 — Explore the JSON Schemas

The published schemas define the structure of Compliance-as-Code objects.

Available schemas include:

- Compliance Rule
- Framework Metadata
- Evidence Record

Location:

```
docs/schemas/
```

---

# Step 4 — Run the Examples

Example files are located in:

```
docs/examples/
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Validate the sample rule:

```bash
python validate-rule.py
```

Generate a sample report:

```bash
python generate-report.py
```

Search a rule:

```bash
python search-controls.py
```

---

# Step 5 — Review Integration Guides

Integration documentation currently includes:

- GitHub Actions
- Azure DevOps
- GitLab CI/CD
- Jenkins
- Terraform
- Python

Location:

```
docs/integrations/
```

---

# Step 6 — Review the API

The repository includes:

- OpenAPI Specification
- Example Responses
- Planned Endpoints

Location:

```
docs/api/
```

---

# Step 7 — Learn the Data Model

Understanding the data model helps developers build integrations that remain compatible with future platform releases.

Recommended reading:

- Data Model
- JSON Schemas
- API Documentation

---

# Next Steps

After reviewing the public documentation, organizations may:

- Build internal integrations
- Develop proof-of-concept implementations
- Evaluate commercial licensing
- Design AI-assisted compliance workflows
- Automate governance processes

---

# Related Documentation

- README
- Architecture
- Security Architecture
- AI Architecture
- Data Model
- JSON Schemas
- API Documentation
- Examples
- Integrations

---

© 2026 First Step Technology LLC. All rights reserved.
