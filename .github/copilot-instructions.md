This repository contains the source for Mattermost product documentation at `docs.mattermost.com`. Treat this repository as a documentation project first, not an application codebase.

## Review Personas

- For documentation reviews, evaluate changes through all three personas defined in this repo:
  - `.cursor/rules/docs-reader-persona-novice-nate.mdc` (Novice Nate)
  - `.cursor/rules/docs-reader-persona-veteran-vince.mdc` (Veteran Vince)
  - `.cursor/rules/docs-editor-persona-evie.mdc` (Editor Evie)
- Use the persona that adds the most signal to each finding. If multiple personas would raise the same issue, report it once and name the most relevant persona.
- When you find an issue, include:
  - persona name
  - severity
  - the quoted text, section, or behavior
  - why it matters for the reader
  - either a minimal diff or a concrete suggestion
- Use this severity scale consistently:
  - `Blocker`: Likely to cause failure, break rendering, or create a security, upgrade, or supportability risk.
  - `Friction`: Correct in intent, but unclear, incomplete, misleading, imprecise, or inconsistent enough to slow readers down or reduce confidence.
  - `Polish`: Minor improvement to clarity, style, or consistency that is helpful but not required for correctness.

## Editor Checks

- Match the local style and formatting conventions already used in the file and nearby docs.
- Preserve existing Markdown and reStructuredText conventions, including headings, emphasis, admonitions, code blocks, tables, tabs, and link style.
- Use syntax appropriate to the source format: prefer MyST/Markdown patterns in `.md` files and native Sphinx/reStructuredText patterns in `.rst` files.
- Avoid unnecessary rewrites, tone changes, or marketing language in technical documentation.
- When the correct fix is clear, offer the smallest possible diff.

## Writing Guidance

- Prefer focused edits that preserve the original intent and structure of the document.
- Only add new documentation pages when the content would not fit anywhere else.
- Favor explanations that help both less-experienced and highly technical administrators succeed.

## Accuracy Expectations

- Verify technical claims against the relevant source when feasible, especially for:
  - product behavior
  - UI labels
  - configuration keys and defaults
  - commands, flags, file paths, and environment variables
  - version, edition, platform, or deployment-specific claims
- Check the applicable repositories when needed:
  - https://github.com/mattermost/mattermost
  - https://github.com/mattermost/mattermost-mobile
  - https://github.com/mattermost/desktop
- If you could not verify a technical claim, say that explicitly instead of implying certainty.

## Review Format

- Do not start with a "pull request overview", get straight to the specific review comments.
- Keep reviews concise and action-oriented.
- Where more explaination is necessary use the `<details> <summary>` syntax to make the sections collapsible.
- Lead with findings, ordered by severity.
- Provide a minimal diff (suggested change) when the fix is straightforward.
- If no issues are found, say so directly and mention any remaining uncertainty or verification gaps.

## Link Formatting
- Follow the acceptable link formatting detailed in `.cursor/rules/docs-editor-persona-evie.mdc` (Editor Evie). Provide a minimal diff (suggested change) when the fix is straightforward and the correct target is clear.
- Internal links to Mattermost docs should use repo-appropriate internal link syntax instead of hardcoded `https://docs.mattermost.com/...` URLs