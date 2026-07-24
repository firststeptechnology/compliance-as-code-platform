# Compliance-as-Code Data Model

The First Step Technology LLC Compliance-as-Code Platform is built around a standardized data model that enables interoperability across compliance frameworks, developer tools, AI systems, and enterprise platforms.

---

# Design Goals

The data model is designed to be:

- Machine-readable
- Human-readable
- Framework-neutral
- Extensible
- Versioned
- AI-ready
- API-friendly
- Easy to validate

---

# Core Object Model

```text
Framework
    │
    ▼
Rule Library
    │
    ▼
Compliance Rule
    │
    ├──────────────┐
    ▼              ▼
Metadata      References
    │              │
    └──────┬───────┘
           ▼
Evidence
           │
           ▼
Assessment
           │
           ▼
Report
```

---

# Primary Objects

The platform is centered around the following object types:

| Object | Purpose |
|---------|---------|
| Framework | Represents a compliance framework |
| Rule | Individual compliance requirement |
| Metadata | Describes a rule |
| Evidence | Supporting assessment artifacts |
| Assessment | Evaluation of a rule |
| Report | Human-readable assessment output |

---

# Rule Object

Every rule contains information similar to:

```json
{
  "control_id": "AC-2",
  "framework": "NIST SP 800-53 Rev. 5",
  "title": "Account Management",
  "guidance": "...",
  "agent_instruction": "...",
  "metadata": {}
}
```

---

# Metadata

Metadata may include:

- Framework
- Version
- Status
- Priority
- Category
- Family
- Tags
- Publication

---

# Relationships

The platform supports relationships between:

- Rules
- Frameworks
- Evidence
- Assessments
- Reports
- Integrations

---

# Versioning

Objects are designed to support semantic versioning.

Example:

```
1.0.0
```

Future releases may introduce additional optional properties while maintaining backward compatibility whenever practical.

---

# Validation

Objects are validated using published JSON Schemas located in:

```
docs/schemas/
```

---

# Extensibility

Organizations may extend objects with their own metadata while preserving compatibility with the public schemas.

---

# Related Documentation

- Architecture
- JSON Schemas
- API Documentation
- Examples
- Integrations

---

© 2026 First Step Technology LLC. All rights reserved.
