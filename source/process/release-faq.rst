Frequently Asked Questions
===============

**Q1: When is release branch cut for a bug release?**
 
 - A: On the day prior feature release ships after final has been cut.

**Q2: When is release branch cut for a feature release?**
 
 - A: On feature cut-off date (T-12).

**Q3: How are PRs merged for release?**
 
 - A: PRs are first merged to master. The dev who submitted the fix is then responsible for cherry-picking it to the bug release branch.

**Q4: How are PRs merged for a feature release?**
 
 - A: PRs are submitted and merged to master (no change).

**Q5: How does Bug Fix release work?**

 - A: Bugs are branched off from previous release.

**Q6: What is community.mattermost on?**
 
 - A: For Feature releases community.mattermost is kept on the RCs. For Bug Fix releases keep it on master. 

**Q7: How to remove feature/bug from a release?**
 
 - A: Revert from release branch. Optionally revert from master.

**Q8: How are NOTICE.txt PRs submitted?**

 - A: Same as Q3.

**Q9: How are translation PRs submitted?**

 - A: Same as Q3.

**Q10: Is an improvement a feature or a bug?**

 - A: Usually features / Story tickets.

**Q11: How does release team monitor what changes went into a release?**

 - A: Monitor the commit history of the respective release branch, e.g. https://github.com/mattermost/mattermost-server/commits/release-5.4 contains commits that shipped with mattermost-server v5.4. Jira ticket is resolved after cherry picking is done.

**Q12: What changes were made to the dev release process to account for the rotating feature and bug fix releases? https://developers.mattermost.com/internal/release-process/**

 - A: PR with changes was merged `here <https://github.com/mattermost/mattermost-developer-documentation/pull/182>`_.

**Q13: What changes were made to the team release process to account for the rotating feature and bug fix releases? https://docs.mattermost.com/process/release-process.html**

 - A: Separate checklists for `Bug Fix release <https://docs.mattermost.com/process/bug-fix-release.html>`_ and `Feature release <https://docs.mattermost.com/process/feature-release.html>`_ were created.

**Q14: How does Redux branching work?**

 - A: TBD.

**Q15: How does translations branching work?**

 - A: Lock the translation server to the release branch. The translation PR will be done against the release branch and we can just merge it, forget about master and cherry-picking at this point, then when we lock the translation server back to master the next PR against master will include those translations that went in for the release branch.

**Q16: How does cutting mobile builds work?**

 - A: TBD.

**Q17: How does updating dependancies work?**
 
 - A: Dependancy updates will only occur in feature releases, unless they contain security fixes.

**Q18: What is the process for community PRs?**

 - A: Review, merge and cherry-pick.
