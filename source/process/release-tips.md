# Release Tips

**Changelog checklist**
 
 - Features
   - State benefits first.
   - Order features based on benefit for end users.
   - Include links to docs where appropriate.
 - Bugs
   - Check/test if the issue was in previous server version.
 - All sections
   - Check that all sections are written and formatted the same way as in previous changelogs.
 - API / Websocket / Database
   - Work with Dev Ops on this section.
 - Next version
   - If the changelog mentions items regarding upcoming versions, move them to the bottom of the changelog.
   
**Ways to meet deadlines**

 - Post a list of dates for next release at or soon after T-0 and ping all of the Teams.
 - For features and bugs, start pinging early enough before due dates and make public posts.
 - When pinging people, provide a clear due date and give a reason for the due date (e.g. Code Complete on Monday).
 - Ask if people need any help or have any questions.
 
**Translations**

 - Post a reminder at T-12 for translators about the release translations due date, e.g. https://community.mattermost.com/core/pl/466tkyxfdtftirxj31n8gpou5h.
 - Monitor progress of translations at https://translate.mattermost.com/projects/mattermost/ and ping language maintainers a few days before due date if they're 
not getting to 100%.
 - Ask Elias to hold on submitting final translations PR if some translators need more time, or ask him to submit a new one if a translations PR was already submitted.
 - Target date for final translations PR is T-5, but T-3 is acceptable.

**Ways how [features/bugs guidelines](https://docs.google.com/document/d/1QxB_A1qkEJBKAvQpRa7JiSQLZhwg6HAEajNRNa7ldGg/edit) are currently enforced**

 - Features guidelines: sometimes features are merged after T-12
    - Start to ping people already at T-15 or earlier for feature PRs that are still open.
 - Bugs guidelines:
   - Need to focus on fixing only S1 and S2 bugs after T-5 to avoid missing T-2 deadline for cutting the final.
   
**Ways to ensure features are tested for HA/mobile/scale**

 - Mobile: Added a release checklist item for QAs for T-11.
 - HA: Test server available.
 - Scale: Via loadtests.

**Release marketing**

 - Blog post:
    - Follow [guidelines](https://docs.mattermost.com/process/marketing-guidelines.html#guidelines-for-release-announcements).
    - Audience: end-users, admin/tech.
    - Include CTAs and avoid including external links unless they direct to Mattermost website or documentation.
    - Give release outline for all PMs and Rich before giving to Justin.
  - Email:
    - Check that the link on the email banner is correct.
