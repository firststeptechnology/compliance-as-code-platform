# Compliance-as-Code Platform Architecture

This document provides a high-level overview of the architecture for the First Step Technology LLC Compliance-as-Code Platform.

The platform is designed to separate public documentation from proprietary commercial rule libraries while providing developers with a stable integration experience.

---

# Architecture Overview

```text
                    +--------------------------------------+
                    |        Commercial Rule Libraries     |
                    |--------------------------------------|
                    | CMMC Level 1                         |
                    | CMMC Level 2                         |
                    | NIST SP 800-171                      |
                    | NIST SP 800-53                       |
                    | NIST CSF 2.0                         |
                    | NIST AI RMF                          |
                    | HIPAA Security Rule                  |
                    | CCPA / CPRA                          |
                    +------------------+-------------------+
                                       |
                                       |
                          Machine Readable JSON
                                       |
                                       ▼
+---------------------------------------------------------------+
|           Compliance-as-Code Platform Engine                  |
+---------------------------------------------------------------+
|                                                               |
| Rule Processing                                               |
| Metadata                                                      |
| Validation                                                    |
| Version Management                                            |
| Framework Mapping                                             |
| Automation                                                    |
| Evidence Support                                              |
| AI Optimization                                               |
|                                                               |
+---------------------------------------------------------------+
                  │
                  │
      +-----------+-----------+
      |                       |
      ▼                       ▼
 JSON Schemas           Public Documentation
      │                       │
      ▼                       ▼
Developer APIs        Integration Guides
      │                       │
      +-----------+-----------+
                  │
                  ▼
           Customer Integrations
                  │
                  ▼
+---------------------------------------------------------------+
| GitHub | Azure DevOps | GitLab | Jenkins | Python | AI | GRC |
+---------------------------------------------------------------+
```

---

# Public Repository

This GitHub repository contains:

- Documentation
- JSON Schemas
- Example Objects
- Integration Guides
- API Documentation
- Sample Pipelines
- Developer Resources

No commercial rule libraries are published in this repository.

---

# Commercial Platform

Commercial offerings include:

- Complete rule libraries
- Framework mappings
- Enriched metadata
- Lifecycle management
- Enterprise support
- Versioned releases
- AI-ready enrichment
- Commercial licensing

---

# Design Principles

The platform is built around the following principles:

- Machine-readable compliance
- Standards-based design
- Vendor neutrality
- API-first architecture
- AI readiness
- DevSecOps compatibility
- Enterprise scalability
- Maintainable versioning

---

# Related Documentation

- Documentation Home
- API Documentation
- JSON Schemas
- Integration Guides
- Product Catalog
- Platform Roadmap

---

© 2026 First Step Technology LLC. All rights reserved.
