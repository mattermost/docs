Development Process Overview
============================

This document describes the process through which feedback and design discussions flow into community systems, then into tickets, then into pull requests, then into monthly releases based on product purpose.

Purpose
-------

The core offer for users of Mattermost is: **All your team communication in one place, searchable and accessible anywhere.**

The design is successful if 100% of team members use Mattermost for internal communications, and are largely off of email and proprietary SaaS products that lock-in user data as part of their business model.

See `Mattermost Manifesto <https://docs.mattermost.com/overview/product.html>`__ for more details.

Community Systems
-----------------

Please see `Community Systems <http://docs.mattermost.com/process/community-systems.html>`__ documentation for how feedback from community constituents is processed into `tickets accepting pull requests <https://docs.mattermost.com/process/help-wanted.html>`_.

Tickets
-------

Mattermost priorities are managed in Jira tickets, which are created by the core team via feedback from community systems as well as through the planning processes.

Triage
~~~~~~

On non-holiday weekdays new tickets are reviewed in a process called "triage", and assigned either a numerical Fix Version for the current release to be prioritized, or a "Triage" Fix Version indicating the ticket has enough specificity that it can be assigned to a developer team to be completed but is not necessarily urgent for the current release.

By default, all tickets are created as public unless they contain sensitive information. The triage process reviews them for sufficient specificity. If the ticket is unclear, triage may reassign the ticket back to the original reporter to add more details.

View `current issues scheduled for the next triage meeting <https://mattermost.atlassian.net/browse/PLT-1203?filter=10105>`__.

Re-triage
^^^^^^^^^

If someone feels an existing ticket should be re-examined, they can add "global-triage" to the Fix Version and it will be routed to the triage team for review at the next meeting.

Release Planning
~~~~~~~~~~~~~~~~

Release planning sets the "Fix Version" of tickets to one of the upcoming monthly releases. The Fix Version is an estimate of when a feature might ship, which may change as the planning process continues, until the ticket is scheduled for a Sprint. 

Jira Fix Version
~~~~~~~~~~~~~~~~

Developers, Product Managers, Release and Quality Assurance teams use the Fix Version field for the following purposes:

 Developers: 
  - Fix Version field is the one that shows up on individual tickets in the backlog view.
  - For Story tickets, the Fix Version is used for soft guidelines for what is targeted for what release. 
  - For Bug tickets, the Fix Version is used to know which bugs are priority based on where we are in the release cycle.
 Product Managers:
  - To prioritize backlog.
  - To estimate/plan what Story tickets ship in what release.
 Release Manager:
  - Follow status of resolved, open and submitted tickets for current release.
  - Compose various release metrics.
 Quality Assurance:
  - Prioritize testing of tickets and associated PRs for the next release.
  - Assess completeness of a release before cutting final.
  - Track when changes actually went in, to help investigate bugs and expected behavior.
  - Report on issues, changes, and tests by release.

Sprint Planning
~~~~~~~~~~~~~~~

Tickets to be completed in the upcoming week are organized on Tuesdays, with input from developers.

Pull Requests
-------------

Core Team Weekly Rhythm
~~~~~~~~~~~~~~~~~~~~~~~

Core team work on tickets in the active sprint on a weekly basis, which flow into GitHub Pull Requests.

Each Pull Request needs a minimum of two reviews by other core team developers before it is merged, with possible feedback shared as reviews happen.

Key contributors might also pick up tickets, or through conversations with the core team contribute pull requests as needed.

Community Contributions
~~~~~~~~~~~~~~~~~~~~~~~

Community members following the `Contribution Guidelines <https://developers.mattermost.com/contribute/getting-started/>`__ might also submit pull requests. Pull requests that significantly change the user experience are opened `via the feature ideas process <http://www.mattermost.org/feature-requests/>`__.

Bug Fixes
^^^^^^^^^

If you see an obvious bug and want to submit a fix, pull requests following the `contribution guidelines <https://developers.mattermost.com/contribute/getting-started/>`__ are gladly accepted.

Examples: 

- `Fix: Unable to change password #1390 <https://github.com/mattermost/mattermost-server/pull/1390>`__
- `Fix isBrowserEdge typo #1260 <https://github.com/mattermost/mattermost-server/pull/1260>`__

Tickets Accepting Pull Requests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you'd like to improve the product beyond bug fixes, you can select from a list of tickets accepting pull requests prepared by the core team.

`Help Wanted GitHub issues <https://mattermost.com/pl/help-wanted>`__ and `Accepting Pull Requests <https://mattermost.atlassian.net/issues/?filter=10101>`__ (APR) tickets are intended to be unambiguous projects that could be reasonably completed by contributors outside the core team and are welcome contributions.

You can choose any ticket marked "Open", even if it's assigned, and comment to let people know you're working on it. If you have questions post in `Mattermost forum <http://forum.mattermost.org/>`__ or join the `Contributors <https://community.mattermost.com/core/channels/tickets>`__ channel.

It's okay to submit PRs to fix obvious bugs or add small improvements, but anything that significantly changes behavior or user expectations `requires an APR ticket opened by the core team <http://docs.mattermost.com/process/accepting-pull-request.html>`__ so that the change can be tested, documented and supported. 

Documentation Improvements
^^^^^^^^^^^^^^^^^^^^^^^^^^

Improvements to documentation are highly welcome.

Please see `documentation contribution guidelines <https://forum.mattermost.org/t/help-improve-mattermost-documentation/194>`_ for more details.

Examples: 

- `Production installation instructions for Debian Jessie with Systemd #1134 <https://github.com/mattermost/mattermost-server/pull/1134>`__ 
- `Fix dead link to AWS file in doc #622 <https://github.com/mattermost/mattermost-server/pull/622>`__

Documentation Pull Request Review
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you're assigned to a documentation pull request made by a core contributor and you see any minor grammar or spelling fixes, please make a commit to fix them to save time instead of including them in a review. Note that this should only be done for changes submitted by people familiar with the review process.

Minor Improvements
^^^^^^^^^^^^^^^^^^

Minor improvements without an Accepting Pull Request ticket may be accepted if:

1. The contribution aligns with product scope
2. The change is high quality, and does not impose a significant burden    for others to test, document and maintain your change.
3. The change aligns with the `fast, obvious,    forgiving <http://www.mattermost.org/design-principles/>`__ design principle.

Examples: 

- `Do not clear LastActivityAt for GetProfiles #1396 <https://github.com/mattermost/mattermost-server/pull/1396/files>`__ 
- `Update to proxy\_pass #1331 <https://github.com/mattermost/mattermost-server/pull/1331>`__

Release
-------

Mattermost ships stable releases on the 16th of every month. Releases begin with a planning process reviewing internal designs and community feedback in the context of the product purpose. Feature development is done in weekly sprints, and releases end with feature complete, stabilization, code complete and release candidate milestones prior to final release.

See `release process documentation <https://docs.mattermost.com/guides/core.html#release-process>`__ for more details.
