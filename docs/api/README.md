# API Documentation

Welcome to the First Step Technology LLC Compliance-as-Code Platform API documentation.

This directory contains reference documentation for integrating with Compliance-as-Code datasets, schemas, examples, and future commercial API services.

---

# API Status

| Component | Status |
|-----------|:------:|
| REST API | Planned |
| JSON Rule Library | Available (Commercial) |
| JSON Schemas | Public |
| Example Responses | Public |
| SDKs | Planned |
| Authentication | Planned |
| Webhooks | Planned |

---

# Planned Endpoints

| Endpoint | Purpose |
|----------|---------|
| GET /frameworks | List supported frameworks |
| GET /frameworks/{framework} | Framework metadata |
| GET /controls/{id} | Retrieve a control |
| GET /controls | Search controls |
| GET /schemas | List JSON schemas |
| GET /examples | Retrieve example objects |

---

# Example Response

```json
{
  "status": "success",
  "framework": "NIST SP 800-53 Rev. 5",
  "control_id": "AC-2",
  "title": "Account Management"
}
```

---

# Response Format

All responses are returned as JSON.

Typical response fields include:

- status
- timestamp
- framework
- control_id
- title
- metadata
- links

---

# Authentication

Public documentation does not require authentication.

Future commercial API offerings may support:

- API Keys
- OAuth 2.0
- Service Accounts
- Enterprise Authentication

---

# Versioning

Future APIs will use semantic versioning.

Example:

```
v1
v1.1
v2
```

---

# Related Documentation

- Documentation Home
- JSON Schemas
- Examples
- Framework Documentation
- Product Catalog
- Roadmap

---

© 2026 First Step Technology LLC. All rights reserved.
