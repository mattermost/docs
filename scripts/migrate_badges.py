#!/usr/bin/env python3
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "source"
BADGES_DIR = SRC / "_static" / "badges"

# Allowed final badge basenames
ALLOWED = {"all-commercial", "entry-ent", "pro-plus", "ent-plus", "ent-adv", "ent-cloud-dedicated"}

# Patterns to find include directives in .rst and .md
# Allow any relative depth before _static/badges/
RST_INCLUDE_RE = re.compile(r"(^\s*\.\.\s+include::\s+)(.+/_static/badges/)([\w\-]+)(\.(?:rst|md))\s*$")
MD_INCLUDE_RE = re.compile(r"(^\s*```\{include\}\s+)(.+/_static/badges/)([\w\-]+)(\.(?:rst|md))\s*$")


def map_badge(basename: str, page_text: str) -> str:
    # Preserve these as-is
    if basename in {"ent-cloud-dedicated"}:
        return basename

    # Normalize prior migration outputs and deployment-only leftovers
    if basename in {"entry-plus", "cloud-only", "cloud-selfhosted", "selfhosted-only", "ent-selfhosted"}:
        basename = "all-commercial"

    # All Plans -> all-commercial
    if basename.startswith("allplans"):
        return "all-commercial"

    # Generic deployment-only labels
    if basename in {"cloud-selfhosted", "selfhosted-only"}:
        return "entry-plus"

    # ent-adv family -> ent-adv
    if basename.startswith("ent-adv"):
        return "ent-adv"

    # ent-pro family -> pro-plus
    if basename.startswith("ent-pro") or basename.startswith("entpro"):
        return "pro-plus"

    # Remaining ent-* -> ent-plus
    if basename.startswith("ent-") or basename == "ent":
        # Avoid overriding preserved ones handled above
        return "ent-plus"

    # Exception keyword rules from page content
    text_lower = page_text.lower()
    entry_ent_keywords = [
        "kubernetes", "performance monitoring", "advanced logging", "ldap group", "ldap channel",
        "ldap team sync", "id-only push notifications", "boards", "ms teams", "microsoft teams", "shared channels"
    ]
    ent_plus_keywords = [
        "high availability", "scaling for enterprise", "enterprise search", "rtcd", "offloader",
        "delegated granular admin", "data retention", "legal hold", "compliance export", "e-discovery", "ediscovery",
        "channel export", "custom end user terms of service", "emm", "appconfig"
    ]

    if any(k in text_lower for k in entry_ent_keywords):
        return "entry-ent"
    if any(k in text_lower for k in ent_plus_keywords):
        return "ent-plus"

    # If previously set to entry-ent but no entry-ent keywords present, default to all-commercial
    if basename == "entry-ent":
        return "all-commercial"

    # Fallback: keep original basename if we didn't match any rule
    return basename


def desired_ext_for_file(file_path: Path) -> str:
    return ".md" if file_path.suffix == ".md" else ".rst"


def process_file(path: Path):
    changed = False
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines(True)
    new_lines = []
    for line in lines:
        m = RST_INCLUDE_RE.match(line)
        md = MD_INCLUDE_RE.match(line)
        if path.suffix == ".rst" and m:
            prefix, base_dir, name, ext = m.groups()
            new_name = map_badge(name, content)
            new_ext = desired_ext_for_file(path)
            # Preserve academy and other non-plan badges
            if name.startswith("academy-"):
                new_lines.append(line)
                continue
            if new_name != name or ext != new_ext:
                new_line = f"{prefix}{base_dir}{new_name}{new_ext}\n"
                new_lines.append(new_line)
                changed = True
            else:
                new_lines.append(line)
        elif path.suffix == ".md" and md:
            prefix, base_dir, name, ext = md.groups()
            new_name = map_badge(name, content)
            new_ext = desired_ext_for_file(path)
            if name.startswith("academy-"):
                new_lines.append(line)
                continue
            if new_name != name or ext != new_ext:
                new_line = f"{prefix}{base_dir}{new_name}{new_ext}\n"
                new_lines.append(new_line)
                changed = True
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    # Removed one-badge-per-page enforcement; preserve all includes

    if changed:
        path.write_text("".join(new_lines), encoding="utf-8")
    return changed


def main():
    changed_files = []
    for root, _dirs, files in os.walk(SRC):
        for fn in files:
            if fn.endswith((".rst", ".md")):
                p = Path(root) / fn
                if process_file(p):
                    changed_files.append(str(p.relative_to(ROOT)))

    # Verify includes
    invalid_includes = []
    missing_md_badges = set()
    include_re = re.compile(r"_static/badges([/\\])/([\w\-]+)\.(rst|md)")
    for root, _dirs, files in os.walk(SRC):
        for fn in files:
            if fn.endswith((".rst", ".md")):
                p = Path(root) / fn
                txt = p.read_text(encoding="utf-8")
                for m in include_re.finditer(txt):
                    name = m.group(2)
                    ext = m.group(3)
                    if name.startswith("academy-"):
                        continue
                    if name not in ALLOWED:
                        invalid_includes.append((str(p.relative_to(ROOT)), f"{name}.{ext}"))
                    if ext == "md":
                        badge_md = BADGES_DIR / f"{name}.md"
                        if not badge_md.exists():
                            missing_md_badges.add(f"{name}.md")

    report = []
    report.append("Changed files:\n" + "\n".join(changed_files))
    report.append("\nInvalid badge includes after migration (should be empty):\n" + "\n".join(f"{f} -> {badge}" for f, badge in invalid_includes))
    report.append("\nMissing .md badges to create (if any):\n" + "\n".join(sorted(missing_md_badges)))
    out_path = ROOT / "build" / "badge_migration_report.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n\n".join(report), encoding="utf-8")
    print(out_path)


if __name__ == "__main__":
    main()


