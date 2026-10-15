#!/usr/bin/env python3
"""Light pre-commit validation for the static Crecer site."""
import os
import re
import sys

HTML_FILES = [
    "index.html",
    "about.html",
    "services.html",
    "credentials.html",
    "contact.html",
    "projects.html",
    "privacy-policy.html",
    "terms-of-service.html",
    "cookie-policy.html",
]

errors = []


def tag_balance(content, tag):
    opens = len(re.findall(rf"<{tag}(?:\s|>)", content, flags=re.I))
    closes = len(re.findall(rf"</{tag}\s*>", content, flags=re.I))
    return opens, closes


for path in HTML_FILES:
    if not os.path.exists(path):
        errors.append(f"MISSING: {path}")
        continue
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    if not content.strip():
        errors.append(f"EMPTY: {path}")
        continue
    if "<html" not in content.lower() or "</html>" not in content.lower():
        errors.append(f"{path}: missing html root")
    if "viewport" not in content:
        errors.append(f"{path}: missing viewport meta")
    if "style.css" not in content:
        errors.append(f"{path}: missing style.css link")
    if "menu-toggle" not in content:
        errors.append(f"{path}: missing mobile menu-toggle")
    for tag in ("div", "section", "script", "header", "footer", "nav"):
        opens, closes = tag_balance(content, tag)
        if opens != closes:
            errors.append(f"{path}: mismatched <{tag}> ({opens} open, {closes} close)")

if not os.path.exists("style.css"):
    errors.append("MISSING: style.css")
else:
    with open("style.css", encoding="utf-8") as fh:
        css = fh.read()
    if css.count("{") != css.count("}"):
        errors.append(
            f"style.css: unbalanced braces "
            f"({{ {css.count('{')} }} {css.count('}')})"
        )
    for needle in ("overflow-x: clip", "safe-area-inset", "@media (max-width: 768px)"):
        if needle not in css:
            errors.append(f"style.css missing: {needle}")

with open("about.html", encoding="utf-8") as fh:
    about = fh.read()
for needle in (
    'data-org-conn="1-2"',
    "layoutOrgConnectors",
    "--clr-green-dark",
    "tier1-advisory-lines",
):
    if needle not in about:
        errors.append(f"about.html missing expected marker: {needle}")

with open("projects.html", encoding="utf-8") as fh:
    proj = fh.read()
for needle in (
    "As-Built &amp; Fire Evacuation Plans",
    "Targeted Renovation Works",
    "Fit-Out Works",
):
    if needle not in proj:
        errors.append(f"projects.html missing card text: {needle}")

# Secret / credential scan on changed-area markers
secret_patterns = [
    r"AKIA[0-9A-Z]{16}",
    r"-----BEGIN (RSA |OPENSSH )?PRIVATE KEY-----",
    r"api[_-]?key\s*[:=]\s*['\"][^'\"]{20,}",
]
for path in HTML_FILES + ["style.css"]:
    if not os.path.exists(path):
        continue
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    for pat in secret_patterns:
        if re.search(pat, text, flags=re.I):
            errors.append(f"{path}: possible secret matched {pat}")

if errors:
    print("VALIDATION FAILED:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("VALIDATION PASSED")
print(" - HTML integrity (tag balance, viewport, style link, menu-toggle)")
print(" - CSS brace balance + responsive markers")
print(" - About org-chart / Projects card content markers")
print(" - Basic secret-pattern scan")
print("NOTE: No npm/build pipeline or automated unit-test suite exists in this repo.")
