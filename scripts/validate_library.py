"""Validate the public skill library's registry, metadata, contexts, and links."""

import csv
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


CONNECTION_COLUMNS = ["From skill", "Decision", "What changes", "Mechanism",
                      "Record or field", "Receiving skill", "Owner"]


def connection_cells(line):
    body = line.strip().removeprefix("|").removesuffix("|")
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", body)]


def read_connections(path, skill_ids):
    connections = set()
    label = path.relative_to(ROOT).as_posix()
    if not path.is_file():
        errors.append(f"Missing connection map: {label}")
        return connections

    lines = path.read_text(encoding="utf-8-sig").splitlines()
    header = next((i for i, line in enumerate(lines)
                   if connection_cells(line) == CONNECTION_COLUMNS), None)
    if header is None:
        errors.append(f"{label}: missing table with columns {' | '.join(CONNECTION_COLUMNS)}")
        return connections

    separator = connection_cells(lines[header + 1]) if header + 1 < len(lines) else []
    if len(separator) != len(CONNECTION_COLUMNS) or not all(
        re.fullmatch(r":?-{3,}:?", cell) for cell in separator
    ):
        errors.append(f"{label}:{header + 2}: invalid connection table separator")
        return connections

    for line_number, line in enumerate(lines[header + 2:], start=header + 3):
        if not line.strip() or "|" not in line:
            break
        row_label = f"{label}:{line_number}"
        cells = connection_cells(line)
        if len(cells) != len(CONNECTION_COLUMNS):
            errors.append(f"{row_label}: expected {len(CONNECTION_COLUMNS)} connection fields, got {len(cells)}")
            continue
        values = [cell.strip("`").strip() for cell in cells]
        missing = [name for name, value in zip(CONNECTION_COLUMNS, values) if not value]
        check(not missing, f"{row_label}: blank connection fields: {', '.join(missing)}")
        source, receiver = values[0], values[5]
        check(not source or source in skill_ids, f"{row_label}: unknown source skill {source!r}")
        check(not receiver or receiver in skill_ids, f"{row_label}: unknown receiving skill {receiver!r}")
        if not missing and source in skill_ids and receiver in skill_ids:
            connections.add((source, receiver))
    return connections


def without_code(content):
    """Mask Markdown code while retaining offsets for link diagnostics."""
    def mask(text):
        return re.sub(r"[^\n]", " ", text)

    lines = []
    fence = None
    for line in content.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})([^\n]*)", line)
        if fence is None:
            if marker and (marker[1][0] == "~" or "`" not in marker[2]):
                fence = marker[1]
                lines.append(mask(line))
            else:
                lines.append(line)
        else:
            lines.append(mask(line))
            if marker and marker[1].startswith(fence) and not marker[2].strip():
                fence = None
    prose = "".join(lines)
    code_span = r"(?<!`)(`+)(?!`).*?(?<!`)\1(?!`)"
    return re.sub(code_span, lambda match: mask(match[0]), prose, flags=re.S)


def markdown_links(content, include_references):
    if include_references:
        content = without_code(content)
    for link in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", content):
        yield link.start(), link.group(1)
    if not include_references:
        return

    definitions = list(re.finditer(r"^[ \t]{0,3}\[([^]\n]+)\]:[ \t]*(<[^>\n]+>|\S+)", content, re.M))
    targets = {" ".join(match.group(1).casefold().split()): match.group(2) for match in definitions}
    references = r"\[([^\]\n]+)\](?:\[([^\]\n]*)\]|(?![\[:(]))"
    for link in re.finditer(references, content):
        name = " ".join((link.group(2) or link.group(1)).casefold().split())
        if name in targets:
            yield link.start(), targets[name]


registry_path = ROOT / "catalog" / "skill-packages.csv"
canonical_path = ROOT / "catalog" / "CANONICAL-CAPABILITIES.md"
foundation_path = ROOT / "GSTACK-FOUNDATION.md"
registry = read_rows(registry_path)
required_columns = {"capability_id", "package", "classification"}
check(required_columns <= set(registry[0]) if registry else False,
      "Package registry is missing required columns or rows")

capabilities = {}
for row in registry:
    capability_id = row.get("capability_id", "").strip()
    package = row.get("package", "").strip()
    check(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", capability_id)),
          f"Invalid capability ID: {capability_id!r}")
    check(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", package)),
          f"Invalid package name: {package!r}")
    check(capability_id not in capabilities, f"Duplicate capability ID: {capability_id}")
    capabilities[capability_id] = row
    check(row.get("classification", "").strip() == "skill",
          f"Unsupported classification for {capability_id}")

canonical_text = canonical_path.read_text(encoding="utf-8")
canonical_ids = set(re.findall(r"^\|\s*`([^`]+)`\s*\|", canonical_text, re.M))
check(canonical_ids == set(capabilities), "Canonical capability list and package registry differ")

packages = {row.get("package", "").strip() for row in registry}
actual_packages = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
check(packages == actual_packages, "Skill directories and package registry differ")
skill_ids = {package for package in actual_packages if (ROOT / "skills" / package / "SKILL.md").is_file()}
connections = read_connections(ROOT / "catalog" / "connections.md", skill_ids)

foundation_text = foundation_path.read_text(encoding="utf-8")
contexts = {}
in_context_table = False
for line in foundation_text.splitlines():
    if line.strip() == "## Context identifiers":
        in_context_table = True
        continue
    if in_context_table and line.startswith("## "):
        break
    match = re.match(r"\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|", line)
    if in_context_table and match:
        contexts[match.group(1)] = set(re.findall(r"`([^`]+)`", match.group(2)))


def validate_predicate(predicate, label):
    """Check a compact context predicate when its form is machine-readable."""
    item = predicate.strip()
    if not item:
        return
    match = re.fullmatch(r"([\w.]+)(!?=)?([\w|_-]*)", item)
    if not match:
        return
    key, operator, value = match.groups()
    check(key in contexts, f"{label}: unknown context key {key}")
    if operator and key in contexts and key != "systems.connector":
        check(set(value.split("|")) <= contexts[key],
              f"{label}: unknown value in {item}")


for package in sorted(packages):
    path = ROOT / "skills" / package / "SKILL.md"
    check(path.is_file(), f"Missing skill entrypoint: {package}")
    if not path.is_file():
        continue
    content = path.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---(?:\s|$)", content, re.S)
    check(frontmatter is not None, f"Missing YAML frontmatter: {package}")
    if frontmatter is None:
        continue
    try:
        metadata = yaml.safe_load(frontmatter.group(1)) or {}
    except yaml.YAMLError as exc:
        errors.append(f"Invalid YAML metadata: {package}: {exc}")
        continue
    check(isinstance(metadata, dict), f"Metadata must be a mapping: {package}")
    if not isinstance(metadata, dict):
        continue
    check(metadata.get("name") == package, f"Name mismatch: {package}")
    package_metadata = metadata.get("metadata", {})
    check(isinstance(package_metadata, dict), f"Metadata section must be a mapping: {package}")
    if not isinstance(package_metadata, dict):
        continue
    declared = set(package_metadata.get("capabilities", []))
    expected = {row["capability_id"] for row in registry if row.get("package", "").strip() == package}
    check(declared == expected, f"Capability metadata mismatch: {package}: {declared ^ expected}")
    context_metadata = package_metadata.get("context", {})
    check(isinstance(context_metadata, dict), f"Context metadata must be a mapping: {package}")
    if not isinstance(context_metadata, dict):
        continue
    for field, predicates in context_metadata.items():
        check(field in {"required", "adapts_by", "excluded_when"},
              f"Unknown context section: {package}/{field}")
        check(isinstance(predicates, list), f"Context predicates must be a list: {package}/{field}")
        if isinstance(predicates, list):
            for predicate in predicates:
                validate_predicate(str(predicate), package)

public_roots = [ROOT, ROOT / "skills", ROOT / "frameworks", ROOT / "catalog", ROOT / "licenses"]
markdown = set()
for base in public_roots:
    if not base.exists():
        continue
    if base == ROOT:
        markdown.update(path for path in ROOT.glob("*.md") if path.is_file())
    else:
        markdown.update(path for path in base.rglob("*.md") if path.is_file())

local_links = 0
for path in sorted(markdown):
    content = path.read_text(encoding="utf-8")
    source_path = path.relative_to(ROOT)
    is_skill = path.name == "SKILL.md" and len(source_path.parts) >= 3 and source_path.parts[0] == "skills"
    for offset, raw_target in markdown_links(content, include_references=is_skill):
        target = raw_target.strip().strip("<>")
        parts = urlsplit(target)
        if not parts.path or parts.scheme or parts.netloc:
            continue
        local_links += 1
        destination = (path.parent / unquote(parts.path)).resolve()
        try:
            destination_path = destination.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"Link leaves public library: {source_path} -> {target}")
            continue
        check(destination.exists(), f"Broken link: {source_path} -> {target}")
        if not is_skill or len(destination_path.parts) < 2 or destination_path.parts[0] != "skills":
            continue
        source, receiver = source_path.parts[1], destination_path.parts[1]
        if source == receiver or source not in actual_packages or receiver not in actual_packages:
            continue
        line_number = content.count("\n", 0, offset) + 1
        check((source, receiver) in connections,
              f"Missing directed connection in catalog/connections.md: {source_path.as_posix()}:{line_number}"
              f" -> {target} ({source} -> {receiver})")

result = {
    "capabilities": len(capabilities),
    "packages": len(packages),
    "markdown_files": len(markdown),
    "local_links": local_links,
    "errors": errors,
    "scope": "Public registry structure, skill metadata, context predicates, local Markdown links, and directed skill connections.",
}
print(json.dumps(result, indent=2))
raise SystemExit(bool(errors))
