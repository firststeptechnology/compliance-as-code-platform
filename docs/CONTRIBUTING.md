# Contributing

Thank you for your interest in the First Step Technology LLC Compliance-as-Code Platform.

This repository exists to provide public documentation, schemas, developer examples, and integration guidance for the Compliance-as-Code Platform. Commercial rule libraries are not stored in this repository.

We welcome constructive contributions that improve the quality of the public documentation and developer experience.

---

# Repository Goals

This repository exists to:

- Document supported frameworks
- Publish public JSON schemas
- Demonstrate integrations
- Provide developer examples
- Support API documentation
- Encourage community learning

---

# Repository Structure

```text
compliance-as-code-platform/
│
├── docs/
│   ├── api/
│   ├── frameworks/
│   ├── integrations/
│   └── schemas/
│
└── examples/
```

Note: `examples/` is a repository-root-level directory, not nested under `docs/`. This keeps runnable example code accessible to CI pipelines without needing to path into the documentation tree.

---

# Documentation Contributors

Contributions are welcome in areas including:

- Documentation improvements
- Typographical corrections
- Example enhancements
- Integration documentation
- API documentation
- Architecture documentation
- Tutorials
- Educational content

## Documentation Standards

Documentation should:

- Use Markdown
- Be written in clear English
- Include descriptive headings
- Include examples where appropriate
- Link to related documentation
- Explain purpose before implementation
- Remain technically accurate

---

# Code Contributors

As the platform grows to include a Python SDK, REST API, CLI, and other tooling, code contributions should follow these principles:

## Coding Standards

- Use UTF-8 encoding
- Use descriptive filenames
- Prefer JSON over proprietary formats
- Follow semantic versioning
- Maintain backward compatibility whenever possible
- Keep examples concise
- Document new features

## JSON Standards

JSON examples and schema-adjacent content should:

- Validate against published schemas in `docs/schemas/`
- Use UTF-8 encoding
- Be consistently formatted
- Use descriptive property names
- Avoid unnecessary nesting
- Remain vendor neutral where practical

## Commit Standards

- Write clear, descriptive commit messages
- Keep commits focused on a single logical change
- Reference related Issues where applicable
- Avoid bundling unrelated changes into a single commit

---

# Before Contributing

Please:

- Read the documentation
- Review existing Issues
- Search existing Pull Requests
- Follow repository standards
- Keep changes focused
- Test examples before submitting

---

# Pull Request Standards

Please ensure that Pull Requests:

- Have a clear description
- Address a single topic
- Update documentation if needed
- Follow repository formatting
- Avoid unrelated changes

---

# Issues

GitHub Issues may be used for:

- Documentation improvements
- Bug reports
- Example corrections
- Enhancement suggestions
- Feature requests

---

# Excluded / Commercial Content

Please do not submit:

- Proprietary rule libraries or licensed framework content
- Customer information or confidential data
- Security credentials
- Commercial datasets or internal enterprise materials

Commercial Compliance-as-Code rule libraries are proprietary products and are not accepted through public pull requests.

---

# Future Development

As this repository grows to include a Python SDK, REST API, CLI, Terraform provider, and additional GitHub Actions, contribution guidance for those components will be added here rather than in a separate file, to keep a single source of truth for all contributors.

---

# Code of Conduct

By participating in this repository, contributors agree to follow the project's [Code of Conduct](../CODE_OF_CONDUCT.md).

---

# License

By submitting contributions, you agree that your contribution may be incorporated into the public repository under the repository's license.

---

# Contact

Website:

https://firststeptechnologyllc.com

Compliance Platform:

https://firststeptechnologyllc.com/compliance-as-code-compliance-automation/

---

© 2026 First Step Technology LLC. All rights reserved.
