#!/usr/bin/env python3
"""
Generate a changelog from merged PR release notes for a given milestone.
 
Expects these environment variables:
  GITHUB_TOKEN      - GitHub personal access token or Actions token
  REPOS             - Comma-separated list of repositories in "owner/repo" format
                      (e.g. "mattermost/mattermost,mattermost/enterprise")
  MILESTONE         - Milestone title (e.g. "v10.6")
  VERSION           - Version label for the changelog entry (e.g. "10.6")
  ANTHROPIC_API_KEY - (optional) If set, release notes are polished by Claude
                      before being written to the changelog.
"""
 
import os
import re
import sys
import requests
from datetime import date
 
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
REPOS = [r.strip() for r in os.environ["REPOS"].split(",") if r.strip()]
MILESTONE_TITLE = os.environ["MILESTONE"]
VERSION = os.environ["VERSION"]
 
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}
 
SYSTEM_PROMPT = """You are an expert technical writer and copyeditor for Mattermost software release notes. Your task is to transform raw, unstructured release notes from pull requests into a clean, categorized, and grammatically correct changelog entry that matches Mattermost's established changelog format exactly.
 
Here are your instructions:
 
1.  **Section structure:** Use `###` for top-level sections and `####` for subsections. Only include sections that have relevant content — do not output empty sections. Do NOT add horizontal rules or line separators between sections.
 
    Top-level sections and their subsections, in this order:
 
    - `### Upgrade Impact` — for changes that affect upgrading, with subsections as applicable:
        - `#### Database Schema Changes` — schema migrations such as new tables, new columns, changed columns, or new indexes. Example items: "Added a new ``Watermarks`` table.", "Added a new column ``DeleteAt`` to the ``ChannelMembers`` table."
        - `#### config.json` — new or changed configuration settings. Use this exact block format for each plan grouping:
 
          New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.
 
          - **Changes to Enterprise Advanced plan:**
            - Under ``ExperimentalSettings`` in ``config.json``, added ``EnableWatermark`` configuration setting to add watermarking toggle in the server.
 
          Adapt the plan name (e.g. "Changes to All plans:", "Changes to Enterprise plan:", "Changes to Enterprise Advanced plan:") and list each setting change as a bullet under the appropriate plan heading.
        - `#### Compatibility` — minimum version requirement changes for browsers, OS, or clients. Example: "Updated minimum Edge and Chrome versions to 146+."
    - `### Improvements` — for new features and enhancements only. Do NOT place items beginning with "Fixed..." here — those belong in Bug Fixes. Begin this section with the line `See [this blog post](BLOG_POST_URL) on the highlights in our latest release.` (use the exact placeholder `BLOG_POST_URL` — it will be replaced automatically). Then add subsections as applicable:
        - `#### User Interface` — UI/UX changes and new visual features. Pre-packaged plugin version updates go at the TOP of this subsection, before other items.
        - `#### Plugins/Integrations` — plugin and integration improvements (use as a separate subsection when there are enough items to warrant it)
        - `#### Administration` — System Console features, logging, support packet changes
        - `#### mmctl` — mmctl command additions or changes (use as a separate subsection when there are enough items to warrant it)
        - `#### Performance` — performance improvements
    - `### Bug Fixes` — corrections to defects. All items starting with "Fixed an issue..." go here, even if the raw note appeared in an Improvements context.
    - `### API Changes` — API additions, changes, or deprecations
    - `### WebSocket Event Changes` — new or changed WebSocket events, if applicable
    - `### Audit Log Event Changes` — new or changed audit log events
    - `### Open Source Components` — open source component additions or removals, if applicable
    - `### Go Version` — Go version updates
    - `### Security` — security-related fixes not already covered under Bug Fixes
 
2.  **Sentence patterns:** Follow these conventions consistently:
    - New features and additions: "Added [feature]..." or "Added support for [feature]..."
    - Bug fixes: "Fixed an issue where..." or "Fixed an issue with..."
    - Improvements to existing things: "Improved [thing]..." or "Updated [thing]..."
    - Removals: "Removed [thing]..."
 
3.  **Code formatting:** Use double backticks for all of the following:
    - Configuration settings (e.g., ``ServiceSettings.EnableDynamicClientRegistration``)
    - API endpoints (e.g., ``/api/v4/posts``)
    - Command names (e.g., ``mmctl license get``)
    - Environment variables (e.g., ``MM_LOG_PATH``)
    - Database table and column names (e.g., ``channelmembers.autotranslation``)
    - File names (e.g., ``config.json``)
    - Feature flags (e.g., ``MM_FEATUREFLAGS_CJKSEARCH``)
 
4.  **Markdown formatting:** Use `- ` bullet points for individual items within sections. Ensure correct and clean Markdown syntax throughout. Do not insert horizontal rules (`---`) or any other separators between sections.
 
5.  **License requirements:** When a feature requires a specific Mattermost license, note it inline at the end of the bullet point (e.g., "Requires Enterprise Advanced license" or "Requires Enterprise license").
 
6.  **Proofreading:** Correct any typos, grammatical errors, awkward phrasing, or inconsistencies. Aim for clear, concise, and professional language.
 
7.  **Tone:** Maintain a neutral, informative, and professional tone consistent with technical documentation.
 
8.  **Focus:** Output only the section content (headings and bullet points). Do not include the release version header line or any introductory or concluding remarks from yourself."""
 
 
def get_milestone_number(repo: str, title: str) -> int | None:
    """Look up the numeric ID for a milestone by its title in the given repo."""
    url = f"https://api.github.com/repos/{repo}/milestones"
    page = 1
    recent_titles = []
    while True:
        params = {
            "state": "all",
            "per_page": 100,
            "page": page,
            "sort": "due_on",       # sort by due date
            "direction": "desc",    # most recently due first, so active milestones are found quickly
        }
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        milestones = resp.json()
        if not milestones:
            break
        for m in milestones:
            if m["title"] == title:
                return m["number"]
        if page == 1:
            recent_titles = [m["title"] for m in milestones[:10]]
        page += 1
    print(f"  ⚠️  Milestone '{title}' not found in {repo} — skipping")
    if recent_titles:
        print(f"     Most recently due milestones: {', '.join(recent_titles)}")
    return None
 
 
def get_merged_prs(repo: str, milestone_number: int) -> list:
    """Fetch all merged PRs belonging to the given milestone in the given repo."""
    prs = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{repo}/issues"
        params = {
            "milestone": milestone_number,
            "state": "closed",
            "per_page": 100,
            "page": page,
        }
        resp = requests.get(url, headers=HEADERS, params=params)
        resp.raise_for_status()
        items = resp.json()
        if not items:
            break
        for item in items:
            # Issues and PRs share the same endpoint; filter to merged PRs only
            if "pull_request" in item and item["pull_request"].get("merged_at"):
                prs.append(item)
        page += 1
    return prs
 
 
 
def extract_release_notes(body: str) -> list[str] | None:
    """
    Extract release note text from a PR body.
 
    Looks for a '#### Release Note' section, then pulls the content of any
    fenced code blocks within it (plain ``` or ```release-note).
    Returns None if the section is missing or all entries are NONE.
    """
    if not body:
        return None
 
    # Normalize line endings (GitHub API may return \r\n on some PR bodies)
    body = body.replace("\r\n", "\n").replace("\r", "\n")
 
    # Capture everything after '#### Release Note(s)' up to the next #### header or EOF
    section_match = re.search(
        r"####\s+Release\s+Notes?\s*\n(.*?)(?=\n####|\Z)",
        body,
        re.DOTALL | re.IGNORECASE,
    )
    if not section_match:
        return None
 
    section = section_match.group(1)
 
    # Strip HTML comments (the instructional block in the template)
    section = re.sub(r"<!--.*?-->", "", section, flags=re.DOTALL)
 
    # Extract fenced code blocks (supports both ``` and ```release-note)
    code_blocks = re.findall(r"```(?:release-note)?\s*\n(.*?)\n?```", section, re.DOTALL)
 
    notes = []
    for block in code_blocks:
        content = block.strip()
        if content and content.upper() != "NONE":
            notes.append(content)
 
    # Fallback to plain text only when there are no code blocks at all in the section
    if not notes and "```" not in section:
        plain = section.strip()
        if plain and plain.upper() != "NONE":
            notes.append(plain)
 
    return notes if notes else None
 
 
def polish_with_ai(raw_notes: list[str]) -> str:
    """
    Send raw release notes to Claude for categorization, formatting, and proofreading.
    Falls back to a simple bullet list if ANTHROPIC_API_KEY is not set.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ℹ️  ANTHROPIC_API_KEY not set — skipping AI polish, using raw notes")
        return "\n".join(f"- {note}" for note in raw_notes)
 
    try:
        import anthropic
    except ImportError:
        print("⚠️  anthropic package not installed — skipping AI polish")
        return "\n".join(f"- {note}" for note in raw_notes)
 
    print("✨ Sending notes to Claude for categorization and proofreading...")
    client = anthropic.Anthropic(api_key=api_key)
 
    raw_text = "\n\n---\n\n".join(raw_notes)
    user_message = f"Here are the raw release notes to process:\n\n{raw_text}"
 
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )
 
    return response.content[0].text.strip()
 
 
def prepend_to_changelog(entry: str, changelog_path: str = "CHANGELOG.md") -> None:
    """Insert a new version entry into the changelog after the static file header block."""
    existing = ""
    if os.path.exists(changelog_path):
        with open(changelog_path, "r") as f:
            existing = f.read()
 
    # The v11 changelog file has a static header block ending with the platform scope note.
    # New entries are inserted immediately after this block so the header is preserved.
    HEADER_END_MARKER = "may not represent all affected configurations.\n```"
 
    if HEADER_END_MARKER in existing:
        idx = existing.index(HEADER_END_MARKER) + len(HEADER_END_MARKER)
        new_content = existing[:idx] + "\n\n\n" + entry + existing[idx:]
    elif existing.startswith("# "):
        # Fallback: insert after the first top-level heading line
        parts = existing.split("\n", 2)
        new_content = parts[0] + "\n\n" + entry + ("\n" + parts[2] if len(parts) > 2 else "")
    else:
        new_content = entry + "\n" + existing
 
    with open(changelog_path, "w") as f:
        f.write(new_content)
 
 
def main():
    print(f"🔍 Milestone: {MILESTONE_TITLE} | Repos: {', '.join(REPOS)}\n")
 
    all_notes = []
    total_prs = 0
    no_notes_prs = []
 
    for repo in REPOS:
        print(f"── {repo}")
        milestone_number = get_milestone_number(repo, MILESTONE_TITLE)
        if milestone_number is None:
            continue
 
        prs = get_merged_prs(repo, milestone_number)
        print(f"   📋 Found {len(prs)} merged PR(s)")
        total_prs += len(prs)
 
        for pr in sorted(prs, key=lambda p: p["number"]):
            notes = extract_release_notes(pr.get("body") or "")
            if notes:
                for note in notes:
                    all_notes.append(note)
                print(f"   ✅ #{pr['number']}: {pr['title']}")
            else:
                no_notes_prs.append((repo, pr))
                print(f"   ⏭️  #{pr['number']}: {pr['title']} (NONE / no notes)")
        print()
 
    # Derive short version for heading/anchor: "v11.7.0" → "v11.7", "11.7.0" → "v11.7"
    version_short = "v" + re.sub(r"\.0$", "", VERSION.lstrip("v"))
 
    release_date = os.environ.get("RELEASE_DATE", "").strip() or date.today().strftime("%Y-%m-%d")
 
    # e.g. (release-v11.7-extended-support-release)=
    anchor = f"(release-{version_short}-extended-support-release)="
    heading = (
        f"## Release {version_short} - "
        f"[Extended Support Release]"
        f"(https://docs.mattermost.com/product-overview/release-policy.html#release-types)"
    )
    entry = f"{anchor}\n{heading}\n\n**Release day: {release_date}**\n\n"
 
    if all_notes:
        polished = polish_with_ai(all_notes)
        blog_url = os.environ.get("BLOG_POST_URL", "").strip()
        if not blog_url:
            # Auto-construct from version: v11.7.0 → https://mattermost.com/blog/mattermost-v11-7-0-is-now-available/
            version_slug = VERSION.lstrip("v").replace(".", "-")
            blog_url = f"https://mattermost.com/blog/mattermost-v{version_slug}-is-now-available/"
            print(f"ℹ️  No blog post URL provided — using auto-constructed URL: {blog_url}")
        polished = polished.replace("BLOG_POST_URL", blog_url)
        entry += polished + "\n"
    else:
        entry += "_No release notes for this version._\n"
 
    changelog_path = os.environ.get("CHANGELOG_PATH", "CHANGELOG.md")
    prepend_to_changelog(entry, changelog_path)
 
    prs_with_notes = total_prs - len(no_notes_prs)
    print(f"✅ CHANGELOG.md updated with notes from {prs_with_notes} PR(s) across {len(REPOS)} repo(s)")
 
    if no_notes_prs:
        print(f"\n⚠️  {len(no_notes_prs)} PR(s) had no release notes (marked NONE or section missing):")
        for repo, pr in no_notes_prs:
            print(f"   [{repo}] #{pr['number']}: {pr['title']}")
 
 
if __name__ == "__main__":
    main()
