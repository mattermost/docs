"""
update_docs.py

Called by the "Update Docs" GitHub Actions workflow.
Selects the correct file set based on the component and release type,
sends each file to the Anthropic API with release context, and writes
the updated content back to disk.

Required environment variables:
  ANTHROPIC_API_KEY  -- Anthropic API key (stored as a GitHub secret)
  COMPONENT          -- "Server", "Mobile", or "Desktop"
  RELEASE_TYPE       -- e.g. "ESR", "Feature Release", "Patch / Dot Release"
  VERSION            -- One or more version numbers, comma-separated.
                        e.g. "11.7" or "10.11.20, 11.6.5, 11.7.3"
                        When multiple versions are given, each file is updated
                        once per version in sequence. Enter oldest-to-newest so
                        the newest entry ends up at the top of changelogs.
  RELEASE_DATE       -- Human-readable release date, e.g. "May 15, 2026"

Optional:
  ESR_END_DATE       -- ESR end-of-support date, e.g. "November 15, 2026"
"""

import os
import sys
import threading
import anthropic
from concurrent.futures import ThreadPoolExecutor, as_completed

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

COMPONENT = os.environ["COMPONENT"]          # Server | Mobile | Desktop
RELEASE_TYPE = os.environ["RELEASE_TYPE"]    # ESR | Feature Release | etc.
RELEASE_DATE = os.environ["RELEASE_DATE"]
ESR_END_DATE = os.environ.get("ESR_END_DATE", "").strip()

# Parse VERSION as a comma-separated list so the workflow can be triggered once
# for multi-version releases (e.g. security patches across several branches).
# Each version is applied to every file in sequence; the output of one version
# becomes the input for the next, so entries accumulate correctly in changelogs.
VERSIONS: list[str] = [v.strip() for v in os.environ["VERSION"].split(",") if v.strip()]
if not VERSIONS:
    print("ERROR: VERSION environment variable is empty.")
    sys.exit(1)

# Guard against accidental long lists (e.g. a typo that produces many tokens).
# Each version multiplies API calls (one per file per version), so cap this early.
MAX_VERSIONS = 5
if len(VERSIONS) > MAX_VERSIONS:
    print(f"ERROR: {len(VERSIONS)} versions given; maximum is {MAX_VERSIONS}.")
    print("Split into multiple workflow runs or fix the version list.")
    sys.exit(1)

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

# Files updated for every server release type.
SERVER_BASE_FILES = [
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

# These changelog files are only updated for Patch / Dot releases and Security releases.
# Feature and ESR releases have a dedicated changelog automation (generate-changelog.yml)
# that handles them separately.
# The files can be very large; MAX_SEND_CHARS limits what is sent to Claude per version
# pass to the most-recent portion where new entries are added.
SERVER_CHANGELOG_FILES = [
    "source/product-overview/mattermost-v10-changelog.md",
    "source/product-overview/mattermost-v11-changelog.md",
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
        if RELEASE_TYPE in ("Patch / Dot Release", "Security Release"):
            # Changelog included -- no dedicated automation for these release types.
            return SERVER_BASE_FILES + SERVER_CHANGELOG_FILES
        elif RELEASE_TYPE in ("Feature Release", "ESR"):
            # Changelog excluded -- generate-changelog.yml handles it for these types.
            return SERVER_BASE_FILES
        else:
            # "Other" and any future types -- skip the changelog to avoid unintended edits.
            # Add an explicit branch above if a new release type needs changelog updates.
            return SERVER_BASE_FILES
    elif COMPONENT == "Mobile":
        return MOBILE_FILES
    elif COMPONENT == "Desktop":
        if RELEASE_TYPE == "ESR":
            return DESKTOP_BASE_FILES + DESKTOP_ESR_EXTRA_FILES
        else:
            # Patch / Dot Release, Feature Release, etc. -- base files only
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
- Do not add placeholder text, commentary, or notes -- only real documentation content.
- If a file does not need changes for this release type, return it exactly as-is.
- Return ONLY the content you were given (the full file, or the provided portion if the user prompt says the file is truncated). No explanations, no markdown code fences, no preamble.
"""


def build_user_prompt(filepath: str, content: str, version: str, truncated: bool = False) -> str:
    esr_note = f"\n- ESR end-of-support date: {ESR_END_DATE}" if ESR_END_DATE else ""
    truncation_note = (
        "\nNOTE: This file was too large to send in full. You are seeing only the first "
        f"{MAX_SEND_CHARS:,} characters. Return only this portion (updated as needed) -- "
        "do NOT attempt to reconstruct or append the rest of the file."
    ) if truncated else ""

    return f"""Update the following Mattermost documentation file for a new release.

Release details:
- Component: {COMPONENT}
- Version: {version}
- Release type: {RELEASE_TYPE}
- Release date: {RELEASE_DATE}{esr_note}

Use the release details and your knowledge of Mattermost documentation conventions \
to determine what changes are needed. If this release type does not affect this file, \
return it unchanged.

File path: {filepath}{truncation_note}

--- BEGIN FILE CONTENT ---
{content}
--- END FILE CONTENT ---

Return the complete file content only."""


# ---------------------------------------------------------------------------
# File update logic
# ---------------------------------------------------------------------------

# Thread-safe print: keeps log lines from interleaving when files run in parallel.
_print_lock = threading.Lock()

def tprint(*args, **kwargs):
    with _print_lock:
        print(*args, **kwargs)


def update_file(client: anthropic.Anthropic, filepath: str) -> str:
    """Update a single documentation file via the Claude API.

    When VERSIONS contains multiple entries, the file is updated once per version
    in sequence: the output of version N becomes the input for version N+1.
    This keeps each Claude call small and well-defined, and ensures changelog
    entries accumulate correctly across versions.

    Returns one of: "updated", "unchanged", "not_found".
    Version-level quality failures (empty response, too-short response) are logged
    and skipped via continue -- they do not surface as a file-level status.
    Raises on hard failures (I/O errors, API errors) so the caller can track them.
    """
    tprint(f"[{filepath}] Reading...")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            original = f.read()
    except FileNotFoundError:
        tprint(f"[{filepath}] WARNING: not found -- skipping.")
        return "not_found"

    # Large changelogs only need recent context; new entries go near the top.
    # Capture the tail once from the original; it stays untouched across all versions.
    truncated = len(original) > MAX_SEND_CHARS
    tail = original[MAX_SEND_CHARS:] if truncated else ""
    if truncated:
        tprint(
            f"[{filepath}] NOTE: file is {len(original):,} chars; "
            f"sending first {MAX_SEND_CHARS:,} chars to Claude."
        )

    # current holds the working head (without tail) updated after each version pass.
    current = original[:MAX_SEND_CHARS] if truncated else original
    any_changed = False

    for version in VERSIONS:
        tprint(f"[{filepath}] Sending to Claude (version {version})...")
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": build_user_prompt(filepath, current, version, truncated)}],
        )

        # --- API response integrity checks (raise -> file marked as failed) ---
        # These guard against malformed or truncated API responses before we touch
        # the file. They are distinct from the content-quality guards below, which
        # are softer checks that skip a version with a warning rather than failing it.
        if not response.content or response.content[0].type != "text":
            raise RuntimeError(
                f"Unexpected API response structure for {filepath} (version {version}): "
                f"content={response.content!r}"
            )
        if response.stop_reason == "max_tokens":
            raise RuntimeError(
                f"Claude hit max_tokens ({MAX_TOKENS}) for {filepath} (version {version}); "
                "output is truncated. Increase MAX_TOKENS or split the file."
            )

        updated = response.content[0].text

        # For truncated files, Claude should return only the head portion, but it may
        # occasionally return slightly more. Cap the result at MAX_SEND_CHARS so that
        # subsequent version passes don't receive an ever-growing prompt.
        if truncated and len(updated) > MAX_SEND_CHARS:
            tprint(
                f"[{filepath}] WARNING: Claude returned {len(updated):,} chars "
                f"(version {version}); truncating to first {MAX_SEND_CHARS:,} chars."
            )
            updated = updated[:MAX_SEND_CHARS]

        # --- Content quality guards ---
        # These raise rather than continue so that a partial application (some versions
        # applied, some not) is surfaced as a hard failure. A PR opened with only some
        # versions applied is harder to detect than a failed run.
        if not updated.strip():
            raise RuntimeError(
                f"Claude returned empty content for {filepath} (version {version}). "
                "Aborting to prevent partial version application."
            )

        if len(updated) < len(current) * 0.5:
            raise RuntimeError(
                f"Updated content for {filepath} (version {version}) is less than 50% of "
                "sent content length. Aborting to prevent partial version application or data loss."
            )

        if updated.strip() == current.strip():
            tprint(f"[{filepath}] No changes needed for version {version}.")
            continue

        # This version changed the file -- chain its output as input to the next version.
        current = updated
        any_changed = True
        tprint(f"[{filepath}] Version {version} applied.")

    if not any_changed:
        tprint(f"[{filepath}] No changes needed -- left as-is.")
        return "unchanged"

    # Reconstruct: updated head + the untouched tail (if file was truncated)
    final_content = current + tail if truncated else current

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(final_content)

    tprint(f"[{filepath}] Done -- updated.")
    return "updated"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    files = get_files()

    print(f"\nMattermost Docs Update")
    print(f"  Component:    {COMPONENT}")
    print(f"  Release type: {RELEASE_TYPE}")
    print(f"  Version(s):   {', '.join(VERSIONS)}")
    print(f"  Release date: {RELEASE_DATE}")
    if ESR_END_DATE:
        print(f"  ESR end date: {ESR_END_DATE}")
    print(f"  Files ({len(files)}):")
    for f in files:
        print(f"    {f}")
    print()

    client = anthropic.Anthropic(
        api_key=os.environ["ANTHROPIC_API_KEY"],
        # Large files (e.g. the v11 changelog at 50 k chars input + up to 32 k output
        # tokens) can take several minutes. 300 s gives ample headroom without
        # letting a truly hung request block the workflow indefinitely.
        timeout=300.0,
        max_retries=2,   # default is 2; made explicit for clarity
    )

    results: dict[str, list[str]] = {
        "updated": [],
        "unchanged": [],
        "skipped": [],
        "not_found": [],
    }
    errors: list[tuple[str, str]] = []

    # Process files in parallel -- each file is an independent Claude API call so
    # there is no ordering constraint between files. Within a single file, versions
    # are still applied sequentially (inside update_file) because each version's
    # output becomes the next version's input. Cap workers at 5 to stay well within
    # Anthropic API rate limits while keeping the speedup significant.
    max_workers = min(len(files), 5)
    print(f"  Processing {len(files)} file(s) with up to {max_workers} parallel worker(s).\n")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {
            executor.submit(update_file, client, fp): fp
            for fp in files
        }
        for future in as_completed(future_to_file):
            filepath = future_to_file[future]
            try:
                status = future.result()
                results[status].append(filepath)
            except (OSError, anthropic.APIStatusError, anthropic.APIConnectionError, RuntimeError) as e:
                tprint(f"[{filepath}] ERROR [{type(e).__name__}]: {e}")
                errors.append((filepath, f"{type(e).__name__}: {e}"))
    print()

    # Summary -- always printed so operators can see what actually happened
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
        print("\nCompleted with warnings -- review skipped/not-found files above.")
    else:
        print("\nAll files processed successfully.")


if __name__ == "__main__":
    main()
