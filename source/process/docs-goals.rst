Mattermost Documentation 
========================

Hosted at docs.mattermost.com, Mattermost Documentation is jointly developed by our community and Mattermost, Inc. to accelerate the adoption of Mattermost software based on the following goals and principles: 

Goal
----

Increase Mattermost usage through more numerous and larger deployments via  timely, effective, easy-to-find documentation delivered by talented people from community and Mattermost, Inc. who are attracted, trained, engaged and celebrated through our processes.

Principles
----------

Situation Awareness 

- Everyone involved with the documentation process should be aware of relevant processes, criteria and timelines. It's okay for processes to take time, it's not okay to leave contributors in the dark. 

Shared Responsibility 

- People approving PRs have a shared responsibility for its success and accurancy. Reviewers may be asked to make corrections in future, if PR authors are not available. 

Appropriate Review 

- Reviews of PRs should be specific PR needs (e.g. grammar, testing verification, technical review, etc.) and be conducted by reviewers skilled in those review areas. 

Acknowledgement 

- Contributors and reviewers should be acknowledged for their short term and long term contributions. 

Trust but Verify 

- Trust everyone to have the right intentions, spot check to find blindspots. 

Process
----------

The processes and materials supporting the Mattermost Documentation goals and principles include: 

- Contributor's Guide for docs.mattermost.com XXX
- Reviewer's Guide for docs.mattermost.com XXX
- Documentation Style Guide XXX

Contributor's Guide for docs.mattermost.com
===========================================

Thank you for your interest in contributing to Mattermost documentation. Your contributions benefit thousands of organizations around the world deploying Mattermost. 

To start: 

Create a Ticket 
---------------

1. **Select a Help Wanted ticket** - Please select a `HELP WANTED ticket <https://github.com/mattermost/docs/issues?q=is%3Aopen+is%3Aissue+label%3A%22Help+Wanted%22>`_ that you'd like address with your contribution, or create a new ticket to discuss an improvement you'd like to make and wait for a project Member to approve and add the `Help Wanted` label so the change will be accepted.

If your update is small and an obvious improvement, you can skip this step and submit a PR directly. 

2. **Become an Approved Contributor** - Please complete the `contributor license agreement <https://www.mattermost.org/mattermost-contributor-agreement/>`_ (a.k.a. "CLA"). This is a standard form for most open source projects and it adds your the approved contributor's list for the Mattermost open source project. There are answers to frequently asked questions in the link above. 

3. **Create your Pull Request** - Please create a pull request for the documentation change you would like to make. Make sure to review and follow the `Style Guide <https://docs.mattermost.com/process/sg_mattermost-doc-style.html>`_. Please include a link to the Help Wanted ticket if you have one. 

4. **(Optional) Meet the Documentation Community** - You can join the Mattermost Documentation channel on the community server and introduce yourself to other contributors and project members. 

Once your ticket is submitted it goes into a review process: 

PR Review Process for Contributors 
----------------------------------

1. **New PR submitted** - Each PR created sends a notification to the `Documentation Channel <https://pre-release.mattermost.com/core/channels/documentation>`_ on the Mattermost contributors server, alerting reviewers. 

2. **Triage** - Project Member assigned to triage reviews doc repo within 1-2 working days and applies labels appropriate "approval required" labels. Use **Saved Reply** template linked to this page to let submitter know what to expect.

3. **Reviews** - Within 5-10 working days, for each "approval required" label, reviewers on call either leave feedback or mark PR "Approved" and removes appropriate label. The reviewer requiring changes adds "Awaiting Submitter Action" label. After submitter addresses feedback, 5-10 working day clock restarts

4. **Merge** - When all "approval required" labels are removed, the last approver reviewing merges the PR.

5. **Verification and Acknowledgement** - Member assigned to Verification reviews recently merged PRs and adds the "PR verified" label and thanks the contributor. 



Reviewer's Guide for docs.mattermost.com 
----------------------------------------

Review of pull requests to Mattermost documentation passes through the following high-level steps: 

1. Project Members and Approved Contributors submit PRs to the docs.mattermost.com repository. 
2. Incoming PRs are assessed and assigned review requirements (e.g. technical PRs, PRs requiring Sphinx changes, etc.). 
3. Reviewers with appropriate qualifications either approve and merge the changes, or leave feedback for the submitter to being the review cycle again. 
4. Once merged, PRs are verified by a Project Member and the submitter's work acknowledged. 
5. Reviewers with consistent performance are acknowledge with an increase in skill level. Reviewers with repeated inconsistency may have their level decreased (though this is rare). 

The following sections lay out the details for this process: 

Pre-reading 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Please read `Contributor's Guide for docs.mattermost.com XXXXXX <XXXX>`_ for the process by which Approved Contributors submit PRs and engage with reviewers. 

Review Labels 
^^^^^^^^^^^^^

The following labels are used to indicate the type of review required for each doc PR: 

- **Needs Style Guide Approval** - Review for `style guide requirements <https://docs.mattermost.com/process/sg_mattermost-doc-style.html>`_, and specifically: 

   - Verify all links work
   - Verify grammar is correct based on US English requirements 
   - Verify RST renders properly in GitHub preview

- **Needs Technical Approval** - Technical change requiring developer review, e.g. change in system requirements.

- **Needs Testing Approval** - Change requires manual testing, e.g. significant install process change. 

- **Needs Sphinx Approval** - Significant structural changes to CSS or Sphinx features, requires HTML generation and verification. 

- **Needs Structural Approval** - Approval required on changes to TOC or organization.

- **Needs Verification & Acknowledgement** - docs.mattermost.com needs to be verified and acknowledgement added to PR.

- **Post-Merge Editing Required** - PR can be merged and someone will follow-up with edits for minor corrections.

Levels 
^^^^^^^^^^^^^^^

The anticipated consistency of reviews by Reviewers is noted using the following levels: 

- **Level 1** - Self-identified expertise in a review criteria, and willing to help.
- **Level 2** - 80%+ track record of good reviews, or subjective promotion to this level by Level 3 or above. 
- **Level 3** - 90%+ track record of correct reviews, or subjective promotion to this level by Level 4 or above. 
- **Level 4** - 95%+ track record of correct reviews or maintainer of doc repo.

Extended periods of consistent performance are recognized by level increases. Repeated inconsistency reduces an reviwers level. 

Roles
^^^^^^^^^^^^^^^

The following lists roles involved in the PR review process: 

- **Approved Contributor** - Anyone who's completed the CLA. This is the minimum role to submit a PR for review. 
- **Project Member** - Approved Contributor granted ability to apply labels. Often a staff member from Mattermost, Inc. 
- **Project Member Reviewer on call** - Member assigned to review PRs in certain approval categories. 
- **Project Member Verifier on call** - Member assigned to verify and acknowledge merged doc PRs. 
- **Project Member Editor on call** - Member assigned to edit PRs with "Post-merge edit required".

Approved Contributors who are not Members can participate in the PR review process, and through consistent performance may be promoted to Members: 

- **Contributor Reviewer** - Approved Contributor who volunteers to review PRs prior to Member review. 
- **Contributor Verifier** - Approved Contributor who volunteers to verify PRs after merge.
- **Contributor Editor** - Approved Contributor who submits PRs editing merged changes with "Post-merge edit required" label.

Helping identify any items missed by Members is highly welcome and encouraged. 

PR Review Process for Reviewers 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following process is used determine how reviewers on-call leave feedback on doc PRs submitted: 

1. **Reviewers** - Reviewers on call should `browse open doc PRs <https://github.com/mattermost/docs/pulls>`_ at least once daily while on-call, and leave feedback, approve or merge any open PRs.
2. **Verifiers** - Verifier on call should `browse query of PRs needing verification XXX<linked_needed>`_ at least once daily while on-call and verify and acknowledge PRs as appropiate. If there's an issue, Verifier should message Reviewer to submit a PR to correct issues. 
3. **Editors** - Editor on call should `browse query of PRs needing editing XXX<XXX>`_ daily and submit a PR with appropriate edits. 

XXX: The process for assigning on-call times is to-be-determined. 

Reviewers 
^^^^^^^^^^^^^^^^^^

The following table summarizes Doc Repo approvers and levels: 

============================  == == == == == == == == == == == == == ==
Reviewer and Levels           LB ES JB LI IT YC AM JW CS CH EN HH GG SJ
============================  == == == == == == == == == == == == == ==
Style Guide Approval          3  3  3  3  3  3  3  3  3  3  3  3  3  3
Technical Approval            0  0  0  0  0  0  0  3  3  3  3  3  3  3
Testing Approval              0  0  0  0  0  0  0  3  3  3  3  3  3  3
Sphinx Approval               0  3  0  0  0  0  3  0  0  0  0  0  0  3
Structural Approval           3  0  0  0  3  0  0  0  0  0  0  0  0  3
Post-Merge Edit               3  3  3  3  3  3  3  3  3  3  3  3  3  3 
Verify & Acknowledge          3  3  3  3  3  3  3  3  3  3  3  3  3  3 
============================  == == == == == == == == == == == == == == 

- LB - lfbrock
- ES - esethna 
- JB - jasonblais
- LI - lindy65
- IT - it33
- YC - yangchen1
- AM - assadmahmoud
- JW - jwilander
- CH - coreyhulen
- CS - crspeller
- EN - enahum 
- GG - grundleborg 
- HH - hmhealey 
- SJ - shieldsjared
