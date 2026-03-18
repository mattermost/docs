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
 
SYSTEM_PROMPT = """You are an expert technical writer and copyeditor for software release notes. Your task is to transform raw, unstructured release notes from a pull request into a clean, categorized, and grammatically correct changelog entry.
 
Here are your instructions:
1.  **Categorization:** Group related changes under appropriate Markdown headings. Use the following categories if applicable:
    *   `### User Interface` (for enhancements to existing functionality or UI/UX)
    *   `### Administration` (for enhancements to administrative features)
    *   `### Performance` (for enhancements to performance)
    *   `## Bug Fixes` (for corrections to defects)
    *   `## Breaking Changes` (for changes that require users to update their code or configuration)
    *   `## Deprecations` (for features being phased out)
    *   `## Security` (for security-related updates)
    *   `## Database` (for schema changes and migrations)
    *   `## Compatibility` (for compatibility changes)
    *   `## API Changes` (for API changes)
    *   `## Audit Log Event Changes` (for Audit Log Event changes)
    *   `## Go Version` (for Go version changes)
    Only include categories that have relevant content. Do not include empty categories.
2.  **Markdown Formatting:** Ensure all output uses correct and clean Markdown syntax. Use bullet points (`* ` or `- `) for individual items within categories.
3.  **Proofreading:** Correct any typos, grammatical errors, awkward phrasing, or inconsistencies. Aim for clear, concise, and professional language.
4.  **Tone:** Maintain a neutral, informative, and professional tone.
5.  **Focus:** Only output the processed changelog entry. Do not include any introductory or concluding remarks from yourself (e.g., "Here is the changelog entry:")."""
 
 
def get_milestone_number(repo: str, title: str) -> int | None:
    """Look up the numeric ID for a milestone by its title in the given repo."""
    url = f"https://api.github.com/repos/{repo}/milestones"
    params = {"state": "all", "per_page": 100}
    resp = requests.get(url, headers=HEADERS, params=params)
    resp.raise_for_status()
    milestones = resp.json()
    for m in milestones:
        if m["title"] == title:
            return m["number"]
    print(f"  ⚠️  Milestone '{title}' not found in {repo} — skipping")
    available = [m["title"] for m in milestones]
    if available:
        print(f"     Available milestones: {', '.join(available[:10])}")
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
 
    # Capture everything after '#### Release Note' up to the next #### header or EOF
    section_match = re.search(
        r"####\s+Release\s+Note\s*\n(.*?)(?=\n####|\Z)",
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
    """Prepend a new version entry to the changelog file."""
    existing = ""
    if os.path.exists(changelog_path):
        with open(changelog_path, "r") as f:
            existing = f.read()
 
    # If the file starts with a top-level heading, insert the new entry below it
    if existing.startswith("# "):
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
 
    today = date.today().strftime("%Y-%m-%d")
    entry = f"## {VERSION} - {today}\n\n"
 
    if all_notes:
        polished = polish_with_ai(all_notes)
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
