Release Overview
==========================

Mattermost adopts a monthly tick-tock release cycle, with a new version shipping on the 16th of each month in `binary form <http://docs.mattermost.com/administration/upgrade.html#mattermost-team-edition>`_. 

Tick-tock refers to even-numbered releases (e.g., v5.6) containing new features, and odd-numbered releases (e.g., v5.7) containing only bug fixes and performance improvements.

The primary goal of our release cycle is to improve quality and build trust with our users in every release. A tick-tock release cycle allows new features to soak in our test environments for longer, allowing us to identify and fix bugs before releasing the features. 

There is no change to the process or release schedule for security issues. When security issues are found that warrant a patch release, we follow the `security release process outlined here <https://docs.mattermost.com/process/security-release.html>`_.

Release Numbering
-----------------

Mattermost numbers stable releases in the following format: 
**[Version Number].[Major Build Number].[Minor Build Number]**

**Version Number:**

- Purpose: Major system releases introduce significantly new functionality or change existing product behaviour 
- Release frequency: Unscheduled. Major system releases are infrequent
- Example: v1.x.x, v2.x.x

**Major Build Number:**

- Purpose: Introduce new features, bug fixes and performance improvements
- Release frequency: Monthly on the 16th of each month
- Example:

  - Even numbers (e.g. v1.2.x, v1.4.x): New features and bug fixes
  - Odd numbers (e.g. v1.3.x, v1.5.x): Quality release including performance improvements and bug fixes

**Minor Build Number:** 

- Purpose: Patch existing releases when severe bug fixes or security patches are required
- Release frequency: As required
- Example: v1.2.5, v1.2.6

Frequently Asked Questions
--------------------------

**Q: Will tick-tock releases delay features?**

- A: You can view current, near term, and future priorities on `our website here <https://mattermost.com/roadmap/>`_. While tick-tock releases mean only shipping new features every other release, it improves the quality of features shipped. We want to avoid rushing to ship new features and then fixing bugs over a number of releases, and instead we focus on shipping high-quality features out the gate.

**Q: What is the release cycle for the React Native mobile apps?**

- A: The mobile apps follow the same monthly tick-tock release cycle as Mattermost Server/Webapp, releasing on the 16th of each month.

**Q: What is the release cycle for the Mattermost Desktop app?**

- A: Desktop releases are currently released as required. We hope to move Desktop to a more frequent and scheduled release cycle in the near future.

**Q: When is release branch cut for a quality release?**
 
- A: On the day prior feature release ships after final has been cut.

**Q: When is release branch cut for a feature release?**
 
- A: On feature cut-off date (T-20).

**Q: How are PRs merged for release?**
 
- A: PRs are first merged to master. The dev who submitted the fix is then responsible for cherry-picking it to the quality release branch.

**Q: How are PRs merged for a feature release?**
 
- A: PRs are submitted and merged to master (no change).

**Q: How does quality release work?**

- A: Bugs are branched off from the previous feature release.
 
**Q: How is cherry-picking done?**

- A: See the `cherry pick process documentation <https://developers.mattermost.com/contribute/getting-started/branching/#cherry-pick-process-developer/>`_ for details. 

**Q: What is community.mattermost kept on?**
 
- A: For Feature releases community.mattermost is kept on the RCs. For Quality releases keep it on master.
 
**Q: What is community-daily.mattermost kept on?**
 
- A: Normally on master.

**Q: How to remove a feature/bug from a release?**
 
- A: Revert from release branch. Optionally revert from master.

**Q: How are NOTICE.txt PRs submitted?**

- A: PRs are first merged to master. The dev who submitted the fix is then responsible for cherry-picking it to the release branch.

**Q: Is an improvement a feature or a bug?**

- A: Usually features/story tickets.
 
**Q: How does release team monitor what changes went into a release?**

- A: Monitor the commit history of the respective release branch, e.g., https://github.com/mattermost/mattermost-server/commits/release-5.4 contains commits that shipped with mattermost-server v5.4. Jira ticket is resolved after cherry picking is done.

**Q: What changes were made to the dev release process to account for the rotating feature and quality releases? https://developers.mattermost.com/internal/release-process/**

- A: PR with changes was merged `here <https://github.com/mattermost/mattermost-developer-documentation/pull/182>`__.

**Q: What changes were made to the team release process to account for the rotating feature and quality releases? https://docs.mattermost.com/process/release-process.html**

- A: Separate checklists for `Quality release <https://docs.mattermost.com/process/bug-fix-release.html>`__ and `Feature release <https://docs.mattermost.com/process/feature-release.html>`__ were created.

**Q: How does translations branching work?**

- A: Lock the translation server to the release branch. The translation PR will be submitted against the release branch and it can just be merged directly to the release branch without cherry-picking. When the translation server is locked back to master, the next PR against master will include those translations that went in for the release branch.

**Q: How does cutting mobile builds work?**

- A: See instructions here: https://developers.mattermost.com/internal/mobile-build-process/.

**Q: How does updating dependancies work?**
 
- A: Dependancy updates will only occur in feature releases, unless they contain security fixes.

**Q: What is the process for community PRs?**

- A: Review, merge, and cherry-pick.
