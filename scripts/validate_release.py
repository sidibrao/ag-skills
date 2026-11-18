#!/usr/bin/env python3
"""Validate the approved skill tree and production catalog."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
CATALOG = ROOT / "catalog" / "skills.json"
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def manifest_values(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("missing YAML frontmatter")
    values = {}
    for line in text.split("\n---\n", 1)[0][4:].splitlines():
        if line and not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"').strip("'")
    for line in text.split("\n---\n", 1)[0][4:].splitlines():
        if line.startswith("  ") and ":" in line:
            key, value = line.strip().split(":", 1)
            values[key] = value.strip().strip('"').strip("'")
    return values


def main() -> int:
    errors = []
    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
        entries = {entry["name"]: entry for entry in catalog.get("skills", [])}
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"ERROR: invalid production catalog: {exc}")
        return 1
    directories = [] if not SKILLS.exists() else sorted(p for p in SKILLS.iterdir() if p.is_dir())
    for skill in directories:
        directories_name = skill.name
        manifest = skill / "SKILL.md"
        if not NAME.fullmatch(directories_name) or not manifest.is_file():
            errors.append(f"{directories_name}: invalid directory or missing SKILL.md")
            continue
        try:
            values = manifest_values(manifest)
        except ValueError as exc:
            errors.append(f"{directories_name}: {exc}")
            continue
        if values.get("name") != directories_name:
            errors.append(f"{directories_name}: name mismatch")
        for key in ("description", "version", "owner", "risk", "source-commit"):
            if not values.get(key):
                errors.append(f"{directories_name}: missing {key}")
        if values.get("status") != "approved":
            errors.append(f"{directories_name}: status must be approved")
        if directories_name not in entries:
            errors.append(f"{directories_name}: missing from catalog")
    extra = sorted(set(entries) - {path.name for path in directories})
    errors.extend(f"{name}: catalog entry has no skill directory" for name in extra)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"Validated {len(directories)} approved skill release(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
