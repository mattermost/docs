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

Creating Help Wanted issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a Help Wanted issue in the `platform repository <https://github.com/mattermost/platform>`_, follow these steps:

1 - Create a ticket in Jira that is well-defined and unambiguous. 

The issue should be written with the mindset that the contributor might have no or limited experience with the Mattermost code base and limited exposure to the Mattermost product.

  .. note::
    Below are a few reasons why Jira ticket for Help Wanted issues is recommended:
    
      1. Jira can be used to prioritize Help Wanted issues internally and are easily searchable by Mattermost staff, community, and customers
      2. Each Jira ticket goes through the  `triage meeting <https://docs.mattermost.com/process/training.html#triage-meeting>`_ for dev and PM approval
      3. Zapier integration automatically creates GitHub Help Wanted issues from labelled Jira tickets, requiring no additional mana
      4. resolved Jira tickets are automatically assigned to a QA, who tests them on the CI

2 - After creating the ticket, add "(Proposed APR)" to its title, so the triage team knows to consider it for a ``help-wanted`` label.

3 - If the Jira ticket is accepted as a Help Wanted issue during `triage <https://docs.mattermost.com/process/training.html#triage-meeting>`_, a ``help-wanted`` label is added. This action automatically triggers a zap that creates a new issue in the `platform repository <https://github.com/mattermost/platform>`_.

4 - After triage, PM on community rotation reviews formatting of the GitHub issue and asks a developer to add appropriate labels for difficulty level (one of ``Introductory``, ``Intermediate`` and ``Advanced``) and programming language (``Go`` and ``ReactJS``).

`See an example Help Wanted issue here <https://github.com/mattermost/platform/issues/4755>`_.

Managing Help Wanted issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once a Help Wanted issue is added, the PM on community rotation is responsible for:

- answering questions from community members, which get automatically posted in the `Community Heartbeat channel <https://pre-release.mattermost.com/core/channels/community-heartbeat>`_
- following up with a community member if there hasn't been a response for more than two weeks

Closing Help Wanted issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once a pull request for an open GitHub Help Wanted issue is merged, please ensure:

- the corresponding GitHub Help Wanted issue is closed, thanking the contributor
- the corresponding JIRA ticket is resolved

----

Mattermost Community Forums
---------------------------------------------------------

Guidelines for `Mattermost community forums <forum.mattermost.org>`_.

*CM = community manager*

Principles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Support (answer everything correctly)
- Prioritize (focus help on those who help others)
- Empower (give them time to answer)
- Elevate (thank, recognize and approve their work)
- Grow (invite people to help as experts, promote people)

Response timeline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Things only Mattermost knows: Respond right away (such as bugs in recent release)
- Enterprise Edition issues: Respond right away, as these are customers or potential customers. CM posts to Community channel.
- Places where community can help:
  - Wait 24 hours then CM nudges community or routes (feature idea, troubleshooting, etc.)
  - If 48 hours go by without community response, CM nudges Contributors channel (which includes core team) by asking for someone to help answer
  - If 72 hours go by and no one in Contributors room has stepped up, then CM (at)-mentions the PM who's managing community issues that week, who can take ownership of responding or routing to someone either in community or core team.
- On holidays, let the community step up

Response writing tips
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Don't answer if unsure
  - Ask someone who knows for sure instead of replying with an assumption or incomplete understanding
  - Don't be afraid to re-route if you don't have the answer and are having trouble figuring it out
- Don't make promises
  - Don’t say “we’ll work on it” or something similar that sets expectations that aren’t met later (e.g. after presenting to core team it turns out you can’t do it)
  - Be careful saying “that’s a good idea”, don’t just say it to be polite. Instead say something akin to “thanks for the idea”
- Choose positivity over negativity
  - Avoid excuses like “we’re busy”, or “our team is small” and turn a missing feature into an invitation to share a feature idea to be upvoted
- Do your best to link documentation as answers
  - Allows answers to be easily updated dynamically as documentation is updated
  - Any questions that should be answered in docs that aren’t should turn into tickets to create that documentation (and post ticket in response)
- Be thankful
  - Communities really respond well to being praised and thanked for their work
  
Resolving issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- After responding to an issue, if the asker comes back and lets you know that the issue is solved, please add [Solved] to the beginning of the title of the question
- CM monitors for issues solved by community members
  - If a thread seems solved but it is not obvious, post to thread asking questioner if the issue is solved
  - If 24 hours go by without a response, ask a core team member if they can confirm if the issue is solved
  - If it is solved add [Solved] to the beginning of the title of the question

Elevating the community
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- CM post questions and/or answers in Contributors room that s/he thinks are well-written
- If a core team member agrees/confirms that the question or answer is good, then CM posts in Contributors room asking core team members and key contributors to go “Like” the answer
