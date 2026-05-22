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
  ESR_END_DATE       — ESR end-of-support date, e.g. "November 15, 2026"
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
ESR_END_DATE = os.environ.get("ESR_END_DATE", "").strip()
 
# Upper bound on Claude's output per file. Most docs files are a few thousand
# tokens; 32 000 provides ample headroom without approaching the model's 64 k
# output limit. Raise this if a truncation error is ever hit.
MAX_TOKENS = 32000
 
# Maximum characters to send to Claude per file. Changelog files can grow very
# large over time, but new entries always go near the top so only the head is
# needed for context. The tail is preserved and re-appended after Claude's edit.
# Increase if Claude needs more history; decrease to reduce token usage.
MAX_SEND_CHARS = 50_000
 
# ---------------------------------------------------------------------------
# File lists per component / release type
#
# Desktop ESR and Desktop Patch/Dot releases touch different files:
#   - ESR: releases page + changelog + both install guides
#   - Patch/Dot: releases page + changelog only
# ---------------------------------------------------------------------------
 
SERVER_FILES = [
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
    esr_note = f"\n- ESR end-of-support date: {ESR_END_DATE}" if ESR_END_DATE else ""
 
    return f"""Update the following Mattermost documentation file for a new release.
 
Release details:
- Component: {COMPONENT}
- Version: {VERSION}
- Release type: {RELEASE_TYPE}
- Release date: {RELEASE_DATE}{esr_note}
 
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
 
def update_file(client: anthropic.Anthropic, filepath: str) -> str:
    """Update a single documentation file via the Claude API.
 
    Returns one of: "updated", "unchanged", "skipped", "not_found".
    Raises on hard failures (I/O errors, API errors) so the caller can track them.
    """
    print(f"  Reading {filepath}...")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            original = f.read()
    except FileNotFoundError:
        print(f"  WARNING: {filepath} not found — skipping.")
        return "not_found"
 
    # Large changelogs only need recent context; new entries go near the top.
    # Send only the head and reconstruct the full file afterward.
    truncated = len(original) > MAX_SEND_CHARS
    send_content = original[:MAX_SEND_CHARS] if truncated else original
    tail = original[MAX_SEND_CHARS:] if truncated else ""
 
    if truncated:
        print(
            f"  NOTE: File is {len(original):,} chars; "
            f"sending first {MAX_SEND_CHARS:,} chars to Claude."
        )
 
    print(f"  Sending to Claude...")
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": build_user_prompt(filepath, send_content)}],
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
 
    # --- Content quality guards (return "skipped", file not marked failed) ---
    # Safety: don't write empty content
    if not updated.strip():
        print(f"  WARNING: Claude returned empty content for {filepath} — skipping.")
        return "skipped"
 
    # Safety: skip if response is dramatically shorter than what was sent
    if len(updated) < len(send_content) * 0.5:
        print(
            f"  WARNING: Updated content for {filepath} is less than 50% of sent "
            "content length. Skipping to avoid data loss."
        )
        return "skipped"
 
    # No-op: the sent portion is unchanged (compare against what was sent, not full file)
    if updated.strip() == send_content.strip():
        print(f"  No changes needed — {filepath} left as-is.")
        return "unchanged"
 
    # Reconstruct: Claude's updated head + the untouched tail (if file was truncated)
    final_content = updated + tail if truncated else updated
 
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(final_content)
 
    print(f"  Done — {filepath} updated.")
    return "updated"
 
 
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
    if ESR_END_DATE:
        print(f"  ESR end date: {ESR_END_DATE}")
    print(f"  Files ({len(files)}):")
    for f in files:
        print(f"    {f}")
    print()
 
    client = anthropic.Anthropic(
        api_key=os.environ["ANTHROPIC_API_KEY"],
        timeout=120.0,   # seconds per request; prevents hung runs on slow responses
        max_retries=2,   # default is 2; made explicit for clarity
    )
 
    results: dict[str, list[str]] = {
        "updated": [],
        "unchanged": [],
        "skipped": [],
        "not_found": [],
    }
    errors: list[tuple[str, str]] = []
 
    for filepath in files:
        print(f"Processing: {filepath}")
        try:
            status = update_file(client, filepath)
            results[status].append(filepath)
        except (OSError, anthropic.APIStatusError, anthropic.APIConnectionError, RuntimeError) as e:
            print(f"  ERROR [{type(e).__name__}] processing {filepath}: {e}")
            errors.append((filepath, f"{type(e).__name__}: {e}"))
        print()
 
    # Summary — always printed so operators can see what actually happened
    print("--- Summary ---")
    print(f"  Updated:   {len(results['updated'])}")
    print(f"  Unchanged: {len(results['unchanged'])}")
    print(f"  Skipped:   {len(results['skipped'])}  (warnings above)")
    print(f"  Not found: {len(results['not_found'])}")
    print(f"  Errors:    {len(errors)}")
 
    if errors:
        print(f"\n{len(errors)} file(s) failed:")
        for fp, err in errors:
            print(f"  {fp}: {err}")
        sys.exit(1)
    elif results["skipped"] or results["not_found"]:
        print("\nCompleted with warnings — review skipped/not-found files above.")
    else:
        print("\nAll files processed successfully.")
 
 
if __name__ == "__main__":
    main()
