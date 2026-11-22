#!/usr/bin/env python3
"""Check the structure of the curated resources in README.md without network access."""

from pathlib import Path
import re
import sys
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- resources:start -->"
END = "<!-- resources:end -->"
ICONS = {"github": "image/alg_R.png", "web": "image/alg_I.png"}
ENTRY = re.compile(
    r"^!\[(?P<icon>github|web)\]\((?P<image>[^)]+)\) "
    r"\[(?P<name>[^\[\]]+)\]\((?P<url>[^\s()]+)\) - (?P<description>\S.*)$"
)
TOC_LINK = re.compile(r"^\s*- \[[^\]]+\]\(#([^)]+)\)\s*$")
HEADING = re.compile(r"^(#{1,6}) (.+)$")
INTRO = re.compile(r"^\*(?!\*)(\S(?:.*\S)?)\*$")
TRACKING_KEYS = {"aff", "aff_id", "affiliate", "fbclid", "gclid", "ref", "referral", "referrer"}


def heading_slug(title):
    """Match GitHub's heading anchors for the plain-text headings used here."""
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")


def heading_anchors(lines):
    """Map heading line numbers to GitHub-style anchors, including duplicates."""
    used = set()
    anchors = {}
    for line_number, line in enumerate(lines, 1):
        match = HEADING.fullmatch(line)
        if not match:
            continue
        base = heading_slug(match.group(2))
        anchor = base
        suffix = 0
        while anchor in used:
            suffix += 1
            anchor = f"{base}-{suffix}"
        used.add(anchor)
        anchors[line_number] = anchor
    return anchors


def normalise_url(parts):
    """Ignore fragments and trailing slashes; GitHub repository paths ignore case."""
    host = parts.hostname.lower()
    path = parts.path.rstrip("/")
    if host == "github.com":
        path = path.lower()
    # Queries can affect the resource. Preserve encoded separators when normalising.
    query = urlencode(sorted(parse_qsl(parts.query, keep_blank_values=True)))
    return urlunsplit(("https", parts.netloc.lower(), path, query, ""))


def check_readme(text, root=ROOT):
    """Return actionable error messages; an empty list means the README passes."""
    lines = text.splitlines()
    errors = []

    def error(line_number, message):
        location = f"README.md:{line_number}" if line_number else "README.md"
        errors.append(f"{location}: {message}")

    for path in ICONS.values():
        if not (Path(root) / path).is_file():
            error(None, f"missing icon file: {path}")

    starts = [i for i, line in enumerate(lines) if line == START]
    ends = [i for i, line in enumerate(lines) if line == END]
    if len(starts) != 1 or len(ends) != 1 or starts[0] >= ends[0]:
        error(None, "expected exactly one ordered resources:start/resources:end marker pair")
        return errors
    start, end = starts[0], ends[0]

    # Check TOC links against all headings, including repeated heading suffixes.
    anchors = heading_anchors(lines)
    known_anchors = set(anchors.values())
    toc_headings = [i for i, line in enumerate(lines) if line == "## Table of Contents"]
    toc_links = set()
    if len(toc_headings) != 1:
        error(None, "expected exactly one Table of Contents heading")
    else:
        for i in range(toc_headings[0] + 1, len(lines)):
            line = lines[i]
            if line.startswith("## "):
                break
            if line.lstrip().startswith("- "):
                match = TOC_LINK.fullmatch(line)
                if not match:
                    error(i + 1, "malformed table-of-contents link")
                    continue
                anchor = match.group(1)
                toc_links.add(anchor)
                if anchor not in known_anchors:
                    error(i + 1, f"table-of-contents anchor does not exist: #{anchor}")
        for line_number, anchor in anchors.items():
            if start < line_number - 1 < end and lines[line_number - 1].startswith(("## ", "### ")):
                if anchor not in toc_links:
                    error(line_number, f"heading is missing from the table of contents: #{anchor}")

    seen_names = {}
    seen_urls = {}
    section = None
    subsection = None
    section_groups = {}
    section_intros = {}
    group_entries = {}
    previous_name = None
    entries = 0

    for i in range(start + 1, end):
        line_number = i + 1
        line = lines[i]
        if not line.strip() or line == "---":
            continue
        if line.startswith("## "):
            section = line[3:]
            subsection = None
            previous_name = None
            section_groups[line_number] = 0
            section_intros[line_number] = False
            current_section_line = line_number
            continue
        if line.startswith("### "):
            if section is None:
                error(line_number, "subsection must be inside a category")
                continue
            subsection = line[4:]
            previous_name = None
            section_groups[current_section_line] += 1
            group_entries[line_number] = 0
            current_group_line = line_number
            continue
        if INTRO.fullmatch(line):
            if section is None or subsection is not None:
                error(line_number, "italic introduction must follow a category before its first subsection")
            elif section_intros[current_section_line]:
                error(line_number, "category must have only one italic introduction")
            else:
                section_intros[current_section_line] = True
            continue

        match = ENTRY.fullmatch(line)
        if not match:
            error(line_number, "expected an icon, linked name, ' - ', and description on one line")
            continue
        if section is None or subsection is None:
            error(line_number, "resource must be inside a category and subsection")
            continue

        if i > start + 1 and lines[i - 1].startswith(("![github]", "![web]")):
            error(line_number, "leave a blank line between resource entries")
        entries += 1
        group_entries[current_group_line] += 1
        icon, image, name, url, description = (
            match.group("icon"), match.group("image"), match.group("name"),
            match.group("url"), match.group("description"),
        )
        if image != ICONS[icon]:
            error(line_number, f"{icon} icon must use {ICONS[icon]}")
        if name != name.strip() or description != description.strip():
            error(line_number, "remove surrounding whitespace from the name and description")
        if not description.endswith("."):
            error(line_number, "description must end with a period")

        key = name.strip().casefold()
        if key in seen_names:
            error(line_number, f"duplicate resource name '{name}' (first on line {seen_names[key]})")
        else:
            seen_names[key] = line_number
        if previous_name is not None and key < previous_name:
            error(line_number, f"'{name}' is not in alphabetical order within '{subsection}'")
        previous_name = key

        try:
            parts = urlsplit(url)
            host = parts.hostname
            # Accessing .port catches invalid port numbers as well.
            port = parts.port
        except ValueError:
            error(line_number, f"invalid URL: {url}")
            continue
        if (parts.scheme != "https" or not host or parts.username is not None
                or parts.password is not None or port is not None):
            error(line_number, "resource URL must be an HTTPS URL without credentials or a custom port")
            continue
        expected_icon = "github" if host.lower() == "github.com" else "web"
        if icon != expected_icon:
            error(line_number, f"use the {expected_icon} icon for {host}")
        if host.lower() == "github.com" and len([part for part in parts.path.split("/") if part]) < 2:
            error(line_number, "GitHub links must point to a repository")
        for parameter, _ in parse_qsl(parts.query, keep_blank_values=True):
            key = parameter.casefold()
            if key.startswith("utm_") or key in TRACKING_KEYS:
                error(line_number, f"remove tracking or referral parameter: {parameter}")
        normalised = normalise_url(parts)
        if normalised in seen_urls:
            error(line_number, f"duplicate resource URL (first on line {seen_urls[normalised]})")
        else:
            seen_urls[normalised] = line_number

    if entries == 0:
        error(None, "no resource entries found between the markers")
    for line_number, count in section_groups.items():
        if not section_intros[line_number]:
            error(line_number, "category must have an italic introduction")
        if count == 0:
            error(line_number, "category must contain at least one subsection")
    for line_number, count in group_entries.items():
        if count == 0:
            error(line_number, "subsection must contain at least one resource")
    return errors


def main():
    readme = ROOT / "README.md"
    try:
        text = readme.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Could not read {readme}: {exc}", file=sys.stderr)
        return 1
    errors = check_readme(text)
    if errors:
        for message in errors:
            print(message, file=sys.stderr)
        return 1
    print("README resource structure and table of contents are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
