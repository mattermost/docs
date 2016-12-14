============================================================
Mattermost Community Guidelines
============================================================

In this document we set out some easy-to-follow community guidelines, including:
- `GitHub Help Wanted Issues`_ - Guidelines for managing Help Wanted issues in GitHub
- `Community Forums`_ - Guidelines for responding to `Mattermost Forum posts <forum.mattermost.org>`_

GitHub Help Wanted Issues
---------------------------------------------------------

Goal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Increase Mattermost usage through more numerous and larger deployments via vibrant open source community by contributing features that would not otherwise be offered

Principles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Contributors get a worthwhile benefit from their contributions from the feature directly, and/or from social recognition
- Help Wanted issues should have a low barrier to contribute

Creating help wanted issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before creating a help wanted issue in the `platform repository <https://github.com/mattermost/platform>`_, confirm the issue you're planning to add has a JIRA ticket associated with it

    - JIRA can be used to prioritize help wanted issues internally
    - each issue goes through `Triage meeting <https://docs.mattermost.com/process/training.html#triage-meeting>`_ to ensure the ticket is clear and is approved by at least one developer and product manager

When creating a help wanted issue, please ensure it:

 - is well-defined and unambiguous
 
    - create the issue with the mindset that the contributor might have no or limited experience with the Mattermost code base and limited exposure to the Mattermost product
    
 - has an introductory section, with
 
    - an invitation to join the `Contributors channel <https://pre-release.mattermost.com/core/channels/tickets>`_
    - an invitation to join the `Developers channel <https://pre-release.mattermost.com/core/channels/developers>`_ for technical questions
    - A link to the `developer’s guide <https://docs.mattermost.com/guides/developer.html>`_ for `machine setup <https://docs.mattermost.com/developer/developer-setup.html>`_ and `developer workflow <https://docs.mattermost.com/developer/developer-flow.html>`_
    - A link to the `code contribution guidelines <https://docs.mattermost.com/developer/contribution-guide.html>`_
    
 - has a well-defined difficulty level, both in the description and with the corresponding label
 
    - Introduction: for someone new to the codebase. Guideline: 2-mana tickets are typically introductory
    - Intermediate: for someone with a general knowledge of the codebase. Guideline: 4-mana tickets are typically introductory
    - Advanced: for someone with a strong grasp of the codebase, e.g. implementing a major feature. Guideline: 8-mana tickets (or higher) are typically introductory     
    
 - has a “Go” or “ReactJS” label
 
    - helps contributors know what programming languages will be involved
    - motivates contributors to work on specific tickets, e.g. someone learning Go might be motivated to tackle introductory Go tickets
    - in general, for the `platform repository <https://github.com/mattermost/platform>`_, if the work is all UI (client-side), add a ReactJS label - if it's server side then add a Go label.

 - has a link to the corresponding JIRA ticket

 - gets noted in the corresponding JIRA ticket
 
    - ensures core devs are aware a help wanted issue was created, and to check whether someone in the community already has it in progress
    - example text: ``GitHub Help Wanted issue here: [Link]. Before starting to work on this ticket, please check whether a community member has it in progress by checking the GitHub issue or by asking a PM.``

Closing help wanted issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once a pull request for an open GitHub help wanted issue is merged, please ensure:

 - the corresponding GitHub help wanted issue is closed, thanking the contributor
 - the corresponding JIRA ticket is resolved

----

Community Forums
---------------------------------------------------------

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
- Enterprise Edition issues: Respond right away, as these are customers or potential customers. CM posts to Key Contributors room.
- Places where community can help:
  - Wait 24 hours then CM nudges community or routes (feature idea, troubleshooting, etc.)
  - If 48 hours go by without community response, CM nudges Contributors room (which includes core team) by asking for someone to help answer
  - If 72 hours go by and no one in Contributors room has stepped up, then CM (at)-mentions the PM who's managing community issues that week, who can take ownership of responding or routing to someone either in community or core team.
- For troll bait (sensitive questions or attacking questions), CM routes to designated anti-troll operator
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
  - Don't be afraid to close GitHub issues if you think you've solved them
- CM monitors for issues solved by community members
  - If a thread seems solved but it is not obvious, post to thread asking questioner if the issue is solved
  - If 24 hours go by without a response, ask a core team member if they can confirm if the issue is solved
  - If it is solved add [Solved] to the beginning of the title of the question

Elevating the community
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- CM post questions and/or answers in Community room that s/he thinks are well-written
- If a core team member agrees/confirms that the question or answer is good, then CM posts in Key Contributors room asking core team members and key contributors to go “Like” the answer
