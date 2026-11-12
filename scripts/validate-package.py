#!/usr/bin/env python3
"""Check Write-Paper-Like-a-Human package files and integrity without external dependencies."""

from __future__ import annotations

import json
import py_compile
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read_package_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise SystemExit(f"Cannot read {path.relative_to(ROOT)}: {error}")


SKILL_PATH = ROOT / "SKILL.md"
SKILL = read_package_file(SKILL_PATH)
README = read_package_file(ROOT / "README.md")
CHANGELOG = read_package_file(ROOT / "CHANGELOG.md")

try:
    PLUGIN = json.loads(read_package_file(ROOT / ".claude-plugin" / "plugin.json"))
except json.JSONDecodeError as error:
    raise SystemExit(f"Fix the JSON in .claude-plugin/plugin.json: {error}")

try:
    CURSOR_PLUGIN = json.loads(read_package_file(ROOT / ".cursor-plugin" / "plugin.json"))
except json.JSONDecodeError as error:
    raise SystemExit(f"Fix the JSON in .cursor-plugin/plugin.json: {error}")

try:
    MARKETPLACE = json.loads(read_package_file(ROOT / ".claude-plugin" / "marketplace.json"))
except json.JSONDecodeError as error:
    raise SystemExit(f"Fix the JSON in .claude-plugin/marketplace.json: {error}")

try:
    PACKAGE_JSON = json.loads(read_package_file(ROOT / "package.json"))
except json.JSONDecodeError as error:
    raise SystemExit(f"Fix the JSON in package.json: {error}")


def require_match(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


# 1. YAML Frontmatter checks in SKILL.md
yaml_metadata = require_match(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "SKILL.md must begin with YAML metadata",
).group(1)

for unsupported_field in ("version:", "compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(unsupported_field)}", yaml_metadata):
        raise SystemExit(f"Remove unsupported YAML field: {unsupported_field[:-1]}")

skill_version = require_match(
    re.search(r'(?m)^\s+version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)["\']?\s*$', yaml_metadata),
    "Add metadata.version to SKILL.md as a three-part semver version",
).group(1)

changelog_version = require_match(
    re.search(r"(?m)^## ([0-9]+\.[0-9]+\.[0-9]+)", CHANGELOG),
    "Add a version heading to CHANGELOG.md",
).group(1)

package_versions = {
    skill_version,
    changelog_version,
    str(PLUGIN.get("version", "")),
    str(CURSOR_PLUGIN.get("version", "")),
    str(PACKAGE_JSON.get("version", "")),
}
if len(package_versions) != 1:
    raise SystemExit(f"Use one unified package version across all files: {sorted(package_versions)}")

# 2. Skill loader configuration
if PLUGIN.get("skills") != ["./"]:
    raise SystemExit("Point the Claude plugin skill loader at the repo root ['/']")
if "skills" in CURSOR_PLUGIN:
    raise SystemExit("Omit skills from the Cursor plugin so it loads the root SKILL.md")

# 3. Description consistency
skill_description = " ".join(
    require_match(
        re.search(r"(?m)^description: \|\n((?:  .*\n)+)", yaml_metadata + "\n"),
        "Write the SKILL.md description as an indented block",
    ).group(1).split()
)

first_sentence = skill_description.split(".")[0].strip() + "."
package_descriptions = {
    str(PLUGIN.get("description", "")).strip(),
    str(CURSOR_PLUGIN.get("description", "")).strip(),
    *(str(plugin.get("description", "")).strip() for plugin in MARKETPLACE.get("plugins", [])),
}

for desc in package_descriptions:
    if not (desc == first_sentence or skill_description.startswith(desc)):
        raise SystemExit(
            f"Plugin manifests must match the first sentence of SKILL.md description:\n"
            f"Expected start: {first_sentence}\nFound: {desc}"
        )

# 4. Reference and exemplar files check
required_references = [
    "references/abstract.md",
    "references/claim-calibration.md",
    "references/corpus-profile.md",
    "references/experiments.md",
    "references/figures.md",
    "references/intake-form.md",
    "references/introduction.md",
    "references/latex-output.md",
    "references/method.md",
    "references/routing.md",
    "references/style-rules.md",
    "references/humanizer-patterns.md",
    "references/storyscope-discourse.md",
    "references/corpus/corpus_stats.json",
    "references/exemplars/moves.jsonl",
    "references/exemplars/paragraphs.jsonl",
    "references/exemplars/phrasebank.csv",
    "references/exemplars/cards/dpo.md",
    "references/exemplars/cards/dreambooth.md",
    "references/exemplars/cards/mip-nerf.md",
    "references/exemplars/cards/mip-splatting.md",
    "references/exemplars/cards/vggt.md",
]

for ref in required_references:
    ref_path = ROOT / ref
    if not ref_path.exists():
        raise SystemExit(f"Missing required reference asset: {ref}")

# 5. Python scripts compilation check
script_files = list((ROOT / "scripts").glob("*.py"))
for script in script_files:
    try:
        py_compile.compile(str(script), doraise=True)
    except py_compile.PyCompileError as err:
        raise SystemExit(f"Syntax error in script {script.name}: {err}")

# 6. Word count sanity check
word_count = len(SKILL.split())
if word_count > 6500:
    raise SystemExit(f"SKILL.md is {word_count} words; keep it under 6,500 words for optimal context window efficiency.")

print(f"Validation SUCCESS: Package version {skill_version} is consistent and all {len(script_files)} scripts compiled cleanly.")
