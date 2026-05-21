"""
update_docs.py
 
Called by the "Update Docs" GitHub Actions workflow.
Selects the correct file set based on the component and release type,
sends each file to the Anthropic API with release context, and writes
the updated content back to disk.
 
Required environment variables:
  ANTHROPIC_API_KEY  — Anthropic API key (stored as a GitHub secret)
  COMPONENT          — "Server", "Mobile", or "Desktop"
  RELEASE_TYPE       — e.g. "ESR", "Feature Release", "Patch / Dot Release"
  VERSION            — Version number, e.g. "11.7", "2.40", "6.2", "5.13.6"
  RELEASE_DATE       — Human-readable release date, e.g. "May 15, 2026"
 
Optional:
  INSTRUCTIONS       — Free-form additional context passed through to Claude
"""
 
import os
import sys
import anthropic
 
# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
 
COMPONENT = os.environ["COMPONENT"]          # Server | Mobile | Desktop
RELEASE_TYPE = os.environ["RELEASE_TYPE"]    # ESR | Feature Release | etc.
VERSION = os.environ["VERSION"]
RELEASE_DATE = os.environ["RELEASE_DATE"]
INSTRUCTIONS = os.environ.get("INSTRUCTIONS", "").strip()
 
# Upper bound on Claude's output per file. Most docs files are a few thousand
# tokens; 32 000 provides ample headroom without approaching the model's 64 k
# output limit. Raise this if a truncation error is ever hit.
MAX_TOKENS = 32000
 
# ---------------------------------------------------------------------------
# File lists per component / release type
#
# Desktop ESR and Desktop Patch/Dot releases touch different files:
#   - ESR: releases page + changelog + both install guides
#   - Patch/Dot: releases page + changelog only
# ---------------------------------------------------------------------------
 
SERVER_FILES = [
    "source/product-overview/mattermost-v11-changelog.md",
    "source/product-overview/mattermost-server-releases.md",
    "source/deployment-guide/server/linux/deploy-rhel.rst",
    "source/deployment-guide/server/linux/deploy-tar.rst",
    # Included because server ESR releases update the compatible desktop version
    # reference on this page. Remove if that is no longer the case.
    "source/product-overview/mattermost-desktop-releases.md",
    "source/product-overview/release-policy.md",
    "source/administration-guide/upgrade/open-source-components.rst",
    "source/product-overview/deprecated-features.rst",
    "source/deployment-guide/software-hardware-requirements.rst",
    "source/administration-guide/upgrade/important-upgrade-notes.rst",
    "source/product-overview/ui-ada-changelog.rst",
]
 
MOBILE_FILES = [
    "source/product-overview/mobile-app-changelog.md",
    "source/product-overview/mattermost-mobile-releases.md",
]
 
DESKTOP_BASE_FILES = [
    "source/product-overview/mattermost-desktop-releases.md",
    "source/product-overview/desktop-app-changelog.md",
]
 
DESKTOP_ESR_EXTRA_FILES = [
    "source/deployment-guide/desktop/linux-desktop-install.rst",
    "source/deployment-guide/desktop/desktop-msi-installer-and-group-policy-install.rst",
]
 
 
def get_files() -> list[str]:
    if COMPONENT == "Server":
        return SERVER_FILES
    elif COMPONENT == "Mobile":
        return MOBILE_FILES
    elif COMPONENT == "Desktop":
        if RELEASE_TYPE == "ESR":
            return DESKTOP_BASE_FILES + DESKTOP_ESR_EXTRA_FILES
        else:
            # Patch / Dot Release, Feature Release, etc. — base files only
            return DESKTOP_BASE_FILES
    else:
        print(f"ERROR: Unknown component '{COMPONENT}'. Expected Server, Mobile, or Desktop.")
        sys.exit(1)
 
 
# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------
 
SYSTEM_PROMPT = """You are a technical documentation editor for Mattermost.
Your job is to update documentation files for a new software release.
 
Rules:
- Follow the exact same formatting, style, and conventions already present in the file.
- Add new entries in the correct location (usually at the top of a table or list, or after the most recent entry).
- Never remove or alter existing content unless it is explicitly outdated by this release.
- Do not add placeholder text, commentary, or notes — only real documentation content.
- If a file does not need changes for this release type, return it exactly as-is.
- Return ONLY the complete file content. No explanations, no markdown code fences, no preamble.
"""
 
 
def build_user_prompt(filepath: str, content: str) -> str:
    extra = f"\n\nAdditional instructions:\n{INSTRUCTIONS}" if INSTRUCTIONS else ""
 
    return f"""Update the following Mattermost documentation file for a new release.
 
Release details:
- Component: {COMPONENT}
- Version: {VERSION}
- Release type: {RELEASE_TYPE}
- Release date: {RELEASE_DATE}{extra}
 
Use the release details and your knowledge of Mattermost documentation conventions \
to determine what changes are needed. If this release type does not affect this file, \
return it unchanged.
 
File path: {filepath}
 
--- BEGIN FILE CONTENT ---
{content}
--- END FILE CONTENT ---
 
Return the complete file content only."""
 
 
# ---------------------------------------------------------------------------
# File update logic
# ---------------------------------------------------------------------------
 
def update_file(client: anthropic.Anthropic, filepath: str) -> None:
    print(f"  Reading {filepath}...")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            original = f.read()
    except FileNotFoundError:
        print(f"  WARNING: {filepath} not found — skipping.")
        return
 
    print(f"  Sending to Claude...")
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": build_user_prompt(filepath, original)}],
    )
 
    # --- API response integrity checks (raise → file marked as failed) ---
    # These guard against malformed or truncated API responses before we touch
    # the file. They are distinct from the content-quality guards below, which
    # are softer checks that skip a file with a warning rather than failing it.
    if not response.content or response.content[0].type != "text":
        raise RuntimeError(
            f"Unexpected API response structure for {filepath}: "
            f"content={response.content!r}"
        )
    if response.stop_reason == "max_tokens":
        raise RuntimeError(
            f"Claude hit max_tokens ({MAX_TOKENS}) for {filepath}; output is truncated. "
            "Increase MAX_TOKENS or split the file."
        )
 
    updated = response.content[0].text
 
    # --- Content quality guards (skip with warning, file not marked failed) ---
    # Safety: don't write empty content
    if not updated.strip():
        print(f"  ERROR: Claude returned empty content for {filepath} — skipping.")
        return
 
    # Safety: skip if response is dramatically shorter (possible truncation)
    if len(updated) < len(original) * 0.5:
        print(
            f"  WARNING: Updated content for {filepath} is less than 50% of original "
            "length. Skipping to avoid data loss."
        )
        return
 
    # No-op: file is unchanged
    if updated.strip() == original.strip():
        print(f"  No changes needed — {filepath} left as-is.")
        return
 
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(updated)
 
    print(f"  Done — {filepath} updated.")
 
 
# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
 
def main():
    files = get_files()
 
    print(f"\nMattermost Docs Update")
    print(f"  Component:    {COMPONENT}")
    print(f"  Release type: {RELEASE_TYPE}")
    print(f"  Version:      {VERSION}")
    print(f"  Release date: {RELEASE_DATE}")
    if INSTRUCTIONS:
        print(f"  Instructions: {INSTRUCTIONS}")
    print(f"  Files ({len(files)}):")
    for f in files:
        print(f"    {f}")
    print()
 
    client = anthropic.Anthropic(
        api_key=os.environ["ANTHROPIC_API_KEY"],
        timeout=120.0,   # seconds per request; prevents hung runs on slow responses
        max_retries=2,   # default is 2; made explicit for clarity
    )
 
    errors = []
    for filepath in files:
        print(f"Processing: {filepath}")
        try:
            update_file(client, filepath)
        except (OSError, anthropic.APIStatusError, anthropic.APIConnectionError, RuntimeError) as e:
            print(f"  ERROR [{type(e).__name__}] processing {filepath}: {e}")
            errors.append((filepath, f"{type(e).__name__}: {e}"))
        print()
 
    if errors:
        print(f"\n{len(errors)} file(s) failed:")
        for fp, err in errors:
            print(f"  {fp}: {err}")
        sys.exit(1)
    else:
        print("All files processed successfully.")
 
 
if __name__ == "__main__":
    main()
