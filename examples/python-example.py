#!/usr/bin/env python3

"""
First Step Technology LLC
Compliance-as-Code Platform

Public Example:
Load and process a Compliance-as-Code rule.
"""

import json
from pathlib import Path


def load_rule(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def display_rule(rule):
    print("=" * 60)
    print("Compliance Rule")
    print("=" * 60)
    print(f"Framework : {rule['framework']}")
    print(f"Control ID: {rule['control_id']}")
    print(f"Title     : {rule['title']}")
    print(f"Status    : {rule['metadata']['status']}")
    print(f"Priority  : {rule['metadata']['priority']}")
    print()
    print("Guidance")
    print("-" * 60)
    print(rule["guidance"])
    print()
    print("Agent Instruction")
    print("-" * 60)
    print(rule["agent_instruction"])
    print()
    print("Tags")
    print("-" * 60)

    for tag in rule.get("tags", []):
        print(f"- {tag}")


def main():
    example_file = Path("compliance-rule-example.json")

    if not example_file.exists():
        print("Example JSON file not found.")
        return

    rule = load_rule(example_file)
    display_rule(rule)


if __name__ == "__main__":
    main()
