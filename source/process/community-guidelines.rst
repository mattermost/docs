============================================================
Mattermost Community Guidelines
============================================================

This document provides easy-to-follow community guidelines for:

- `GitHub Help Wanted Issues in Platform Repository`_
- `Mattermost Community Forums`_

----

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

Guidelines for Mattermost `community forums <https://forum.mattermost.org>`_.

*CM = community manager*

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
