#!/usr/bin/env python3

"""
Simple Compliance-as-Code control search example.

First Step Technology LLC
Compliance-as-Code Platform
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE_FILE = ROOT / "docs" / "examples" / "compliance-rule-example.json"


def load_rule():
    with EXAMPLE_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def search(term: str):
    rule = load_rule()

    searchable = " ".join(
        [
            rule.get("framework", ""),
            rule.get("control_id", ""),
            rule.get("title", ""),
            rule.get("guidance", ""),
            rule.get("agent_instruction", ""),
        ]
    ).lower()

    if term.lower() in searchable:
        print("\nMatch Found\n")
        print(f"Framework : {rule['framework']}")
        print(f"Control ID: {rule['control_id']}")
        print(f"Title     : {rule['title']}")
        print()
        print(rule["guidance"])
    else:
        print("No matching controls found.")


def main():
    print("Compliance-as-Code Control Search")
    print("---------------------------------")

    term = input("Search: ").strip()

    if not term:
        print("Please enter a search term.")
        return

    search(term)


if __name__ == "__main__":
    main()
