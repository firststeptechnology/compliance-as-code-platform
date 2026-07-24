#!/usr/bin/env python3

"""
Validate a Compliance-as-Code rule against the public JSON Schema.

First Step Technology LLC
Compliance-as-Code Platform
"""

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError


ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "docs" / "schemas" / "compliance-rule.schema.json"
EXAMPLE_PATH = ROOT / "docs" / "examples" / "compliance-rule-example.json"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> int:
    try:
        schema = load_json(SCHEMA_PATH)
        example = load_json(EXAMPLE_PATH)

        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)

        errors = sorted(
            validator.iter_errors(example),
            key=lambda error: list(error.absolute_path),
        )

        if errors:
            print("Compliance rule validation failed.")

            for error in errors:
                location = ".".join(str(item) for item in error.absolute_path)
                location = location or "<root>"
                print(f"- {location}: {error.message}")

            return 1

        print("Compliance rule validated successfully.")
        return 0

    except FileNotFoundError as error:
        print(f"Required file not found: {error.filename}")
        return 1

    except json.JSONDecodeError as error:
        print(
            f"Invalid JSON in {error.doc}: "
            f"line {error.lineno}, column {error.colno}"
        )
        return 1

    except SchemaError as error:
        print(f"Invalid JSON Schema: {error.message}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
