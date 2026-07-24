# JSON Schemas

This directory contains public JSON Schema documentation for the First Step Technology LLC Compliance-as-Code Platform.

The schemas define the expected structure of machine-readable compliance rule objects used across supported framework libraries.

## Purpose

The public schemas are designed to help developers:

- Validate rule objects
- Understand required and optional fields
- Build compatible integrations
- Create import and transformation workflows
- Develop internal compliance automation
- Test AI and DevSecOps implementations

## Planned Schema Files

```text
docs/schemas/
├── README.md
├── compliance-rule.schema.json
├── framework-metadata.schema.json
└── evidence-record.schema.json
```

## Core Rule Object

A typical Compliance-as-Code rule object may include:

```json
{
  "schema_version": "1.0.0",
  "control_id": "AC-2",
  "framework": "NIST SP 800-53 Rev. 5",
  "title": "Account Management",
  "guidance": "Manage system accounts throughout their lifecycle.",
  "agent_instruction": "Verify that account lifecycle controls are documented, implemented, and reviewed.",
  "metadata": {
    "family": "Access Control",
    "version": "Rev. 5",
    "status": "active"
  }
}
```

## Schema Design Principles

Public schemas follow these principles:

- Stable field names
- Predictable data types
- Framework-neutral core structure
- Extensible metadata
- Semantic versioning
- Human-readable validation errors
- Compatibility with standard JSON Schema validators
- Support for AI, CI/CD, GRC, and custom automation workflows

## Validation

Compatible JSON Schema validators may be used to confirm that rule objects meet the required structure before they are imported, processed, or evaluated.

Example validation workflow:

```text
Rule Library
     |
     v
JSON Schema Validation
     |
     v
Application or Automation Workflow
     |
     v
Results, Evidence, or Reporting
```

## Public and Commercial Content

The schemas in this repository describe public structural conventions.

They do not expose the complete commercial rule libraries, proprietary enrichment fields, transformation logic, source-processing methods, or internal lifecycle metadata.

Commercial rule libraries remain proprietary products of First Step Technology LLC and are licensed separately.

## Related Documentation

- [Documentation Home](../README.md)
- [Framework Documentation](../frameworks/)
- [Product Catalog](../../CATALOG.md)
- [Platform Roadmap](../../ROADMAP.md)

---

© 2026 First Step Technology LLC. All rights reserved.
