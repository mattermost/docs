============================================================
Mattermost Community Guidelines
============================================================

This document provides easy-to-follow community guidelines for:

.. contents::
  :backlinks: top
  :local:
  :depth: 2

----

Mattermost Community Playbook
---------------------------------------------------------

How to get community involved in a campaign?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Examples include React Native Apps, Redux and APIv4 campaigns.

On-boarding
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a forum post letting developers know about the campaign and ways to contribute
2. Create a contribution guide including developer machine set up
3. Create help wanted tickets that a community member could work on
 
 - For a high priority Help Wanted ticket, reach out to contributors directly in the GitHub repository for best engagement

Retention
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Identify active contributors and thank them personally for their work
2. For work in progress tickets or submitted pull requests, follow up with contributor once a week for status updates and questions
3. Recognize everyone’s contributions (either intrinsic rewards like having their name listed on a contributor’s page or tangible like swag or gift cards)
4. If applicable, assign roles to top contributors (such as team lead, code reviewer, tester) to give a sense of ownership for the contributor

Off-boarding
~~~~~~~~~~~~~~~~~~~~~~~~~

1. When a campaign is finished, try to pull them to another campaign or project to work on

GitHub Help Wanted Issues in Platform Repository
---------------------------------------------------------

Goal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Increase Mattermost usage through larger and more numerous deployments via a vibrant open source community that contributes features that would not otherwise be offered.

Principles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Contributors get a worthwhile benefit from their contributions, from the feature directly and/or from social recognition
- Community members should have a low barrier to contribute
- Community development workflow should be clear, efficient and effective

Creating Help Wanted Issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a Help Wanted issue in the `platform repository <https://github.com/mattermost/platform>`_, follow these steps:

1 - Create a ticket in Jira that is well-defined and unambiguous.

The issue should be written with the mindset that the contributor might have no or limited experience with the Mattermost code base and limited exposure to the Mattermost product.

  .. note::
    Below are a few reasons why Jira tickets for Help Wanted issues are recommended:

      1. Jira tickets can be used to prioritize Help Wanted issues internally and are easily searchable by Mattermost staff, community, and customers
      2. Each Jira ticket goes through the  `triage meeting <https://docs.mattermost.com/process/training.html#triage-meeting>`_ for dev and PM approval
      3. Zapier integration automatically creates GitHub Help Wanted issues from labelled Jira tickets, requiring no additional mana
      4. Resolved Jira tickets are automatically assigned to a QA, who tests them against the ``master`` branch.

2 - After creating the ticket, add "(Proposed APR)" to its title, so the triage team knows to consider it for a ``help-wanted`` label.

3 - If the Jira ticket is accepted as a Help Wanted issue during `triage <https://docs.mattermost.com/process/training.html#triage-meeting>`_, a ``help-wanted`` label is added. This action automatically triggers a zap that creates a new issue in the `platform repository <https://github.com/mattermost/platform>`_.

    - To accept a ticket as a Help Wanted issue, the description should be unambiguous, and include UI description and help text so the change can be implemented and tested by any contributor
    - The triage team also adds the appropriate difficulty level (one of ``Introductory``, ``Intermediate`` and ``Advanced``) and programming language (``Go`` and ``ReactJS``) to the description of the Jira ticket

4 - After triage, PM on community rotation reviews formatting of the GitHub issue and adds appropriate labels for difficulty level and programming language as defined by the triage team.

`See an example Help Wanted issue here <https://github.com/mattermost/platform/issues/4755>`_.

Managing Help Wanted Issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once a Help Wanted issue is added, the PM on community rotation is responsible for:

- answering questions from community members, which get automatically posted in the `Community Heartbeat channel <https://pre-release.mattermost.com/core/channels/community-heartbeat>`_
- following up with a community member if there hasn't been a response for more than two weeks

Closing Help Wanted Issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once a pull request for an open GitHub Help Wanted issue is merged, please ensure:

- the corresponding GitHub Help Wanted issue is closed, thanking the contributor
- the corresponding JIRA ticket is resolved

Mattermost Community Forums
---------------------------------------------------------

Guidelines for Mattermost `community forums <https://forum.mattermost.org>`_ and public Mattermost `GitHub repositories <https://github.com/mattermost>`_.

Principles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Support (answer everything correctly)
- Prioritize (focus help on those who help others)
- Empower (give them time to answer)
- Elevate (thank, recognize and approve their work)
- Grow (invite people to help as experts, promote people)

Response Writing Tips
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Don't answer if unsure**
  - Ask someone who knows for sure instead of replying with an assumption or incomplete understanding
  - Don't be afraid to re-route if you don't have the answer and are having trouble figuring it out
- **Don't make promises**
  - Don’t say “we’ll work on it” or something similar that sets expectations that aren’t met later (e.g. after presenting to core team it turns out you can’t do it)
  - Be careful saying “that’s a good idea”, don’t just say it to be polite. Instead say something akin to “thanks for the idea”
- **Choose positivity over negativity**
  - Avoid excuses like “we’re busy”, or “our team is small” and turn a missing feature into an invitation to share a feature idea to be upvoted
- **Do your best to link documentation as answers**
  - Allows answers to be easily updated dynamically as documentation is updated
  - Any questions that should be answered in docs that aren’t should turn into tickets to create that documentation (and post ticket in response)
- **Be thankful**
  - Communities really respond well to being praised and thanked for their work
  
Sample Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

General Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. If an issue has a PR submitted by community, but no associated Jira ticket, leave it open until the PR is merged

2. If an issue has a Jira ticket with a ``help-wanted`` label, there is a Help Wanted ticket in GitHub. It can be closed with the following note:

.. code-block:: text
  Hi @username

  Thanks for the report! We have created a [Help Wanted issue here](link to GitHub issue) and are looking for community's help. Would you be interested helping with a pull request?

3. If an issue has a Jira ticket without a ``help-wanted`` label and assigned to the current release fix version for a developer to fix, it can be closed with the following note

.. code-block:: text

  Hi @username

  Thanks for the report! We have created a [Jira ticket](link to Jira ticket) to track it. If you're interested helping with a pull request, please let us know.

4. If an issue has a Jira ticket without a ``help-wanted`` label but not assigned to the current release fix version, queue Jira ticket back to triage to ask if a help wanted issue could be created for it.

5. If the reporter doesn’t respond in two weeks, close the issue with the following note:

.. code-block:: text

  Hi @username, we haven't received an update so we'll assume that the problem is fixed or is no longer valid. 

  If you still experience the same problem, try upgrading to the latest version. 

  If the issue persists, reopen this issue with the relevant information and we'd be glad to help you where we can.

Feature Requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Respond to the issue with the following note

.. code-block:: text

  Thanks, appreciate your feedback @{username}.  

  Would you like to [contribute this in the feature idea forum](https://mattermost.uservoice.com/forums/306457-general/) so it can be discussed, upvoted and considered for a [help wanted ticket](https://docs.mattermost.com/process/help-wanted.html)?

  Please include a link back to this GitHub issue. If you're interested in implementing, please say so and we'll prioritize the review. 

  You get **10** votes in the feature idea forum, and each one influences the future of the project.

Licence Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sample reponse for the following question: Is it okay to implement an Enterprise policy feature in a custom Team Edition fork?

.. code-block:: text

  Thanks @{username} for the response,

  You're welcome to use the software per the open source license in the source code, just two things to keep in mind: 

  1. Per the [trademark guidelines](https://www.mattermost.org/trademark-standards-of-use/) when you're offering a fork for use by others, please remove Mattermost branding (name and logos). This is standard in open source.

  2. We'd encourage you to merge in [security updates](http://about.mattermost.com/security-updates/) as they're released.

Hard Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To respond to tough questions, use the `SCIPAB method <https://www.mandel.com/top-ten-reasons/tools-methodology/scipab>`_ to help formulate a response and send for community lead to review. 

Situation:
  State what you know about your listeners' circumstances that is relevant to your discussion or presentation, e.g., current state of their business, technology, industry, or plans. 

Complication:
  Identify the critical issues (changes, pressures, demands, etc.) that are impacting the Situation and creating problems, challenges, or opportunities. 

Implication:
  Show the personal or business consequences of failing to act on the problems or opportunities described in the Complication. 

Position:
  State clearly and confidently your opinion about what needs to be done to solve your listeners' problem. 

Action:
  Help listeners understand the role you want them to play, or the questions you'd like them to consider, during your presentation or conversation. 

Benefit:
  Describe how your recommended Position and Action will address listeners' specific needs. State the results clearly and quantifiably. 
