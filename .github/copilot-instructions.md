# GitHub Copilot Instructions

This repository contains the source for Mattermost product documentation at `docs.mattermost.com`. Treat this repository as a documentation project first, not an application codebase.

## Reviewer Personas

- Review changes from the persona defined in this repo at: `.cursor/rules/docs-reader-persona-novice-nate.mdc`
- Review changes from the persona defined in this repo at: `.cursor/rules/docs-reader-persona-veteran-vince.mdc`
- Review changes from the persona defined in this repo at: `.cursor/rules/docs-editor-persona-evie.mdc`
- When you find issues reviewing as these personas, reference the specific persona (ie Novice Nate or Editor Evie) and how severe the issue would be for that persona. Use the framework of "Blocker", "Friction", "Polish".

## Editor Checks

- Match the existing style and formatting conventions already used in the file you are editing and the repository as a whole.
- Preserve existing Markdown and reStructuredText conventions, including the usage of headings, bold, admonitions, code blocks, tables, tabs, and link style. Flag it if the usage of any formatting type does not match standard conventions.
- Use syntax appropriate to the source format: prefer MyST/Markdown patterns in `.md` files and native Sphinx/reStructuredText patterns in `.rst` files.
- Follow the detailed link conventions and examples in `.cursor/rules/docs-editor-persona-evie.mdc`.
- Check that admonition type matches the severity of the content: use `note` for context, `tip` for optional guidance, `important` for prerequisites or high-impact constraints, and `warning` for meaningful risk. Treat `attention` as rare.
- When flagging a link issue and the correct target is clear, provide a minimal suggested diff that fixes the link in the syntax appropriate for the file type.
- Avoid unnecessary rewrites, tone changes, or marketing language in technical documentation.
- Offer a minimal diff when the fix is straightforward and the correct target is clear

## Writing Guidance

- Prefer focused edits that preserve the original intent and structure of the document.
- Only add new documentation pages when the content would not fit anywhere else.

## Accuracy Expectations

- Verify documentation changes against the applicable source code at:
  - https://github.com/mattermost/mattermost
  - https://github.com/mattermost/mattermost-mobile
  - https://github.com/mattermost/desktop



