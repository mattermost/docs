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
2. For work in progress tickets or submitted pull requests, follow up with contributor once a week for status updates and questions to make sure contributors aren't blocked and feel more comfortable to ask questions. If there hasn't been activity in more than two weeks, ask if you can help them in some way.
3. Recognize everyone’s contributions (either intrinsic rewards like having their name listed on a contributor’s page or tangible like swag or gift cards)
4. If applicable, assign roles to top contributors (such as team lead, code reviewer, tester) to give a sense of ownership to the contributor

Off-boarding
~~~~~~~~~~~~~~~~~~~~~~~~~

1. When a campaign is finished, offer suggestions for other campaigns or projects they might be interested in.

GitHub Help Wanted Issues in Mattermost-Server Repository
-----------------------------------------------------------

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

To create a Help Wanted issue in the `mattermost-server repository <https://github.com/mattermost/mattermost-server>`__, follow these steps:

1 - Create a ticket in Jira that is well-defined and unambiguous.

The issue should be written with the mindset that the contributor might have no or limited experience with the Mattermost code base and limited exposure to the Mattermost product.

  .. note::
    Below are a few reasons why Jira tickets for Help Wanted issues are recommended:

      1. Jira tickets can be used to prioritize Help Wanted issues internally and are easily searchable by Mattermost staff, community, and customers
      2. Each Jira ticket goes through the  `triage meeting <https://docs.mattermost.com/process/training.html#triage-meeting>`__ for dev and PM approval
      3. Zapier integration automatically creates GitHub Help Wanted issues from labelled Jira tickets, requiring no additional mana
      4. Resolved Jira tickets are automatically assigned to a QA, who tests them against the ``master`` branch.

2 - After creating the ticket, add "(Proposed APR)" to its title, so the triage team knows to consider it for a ``help-wanted`` label.

3 - If the Jira ticket is accepted as a Help Wanted issue during `triage <https://docs.mattermost.com/process/training.html#triage-meeting>`__, a ``help-wanted`` label is added. This action automatically triggers a zap that creates a new issue in the `mattermost-server repository <https://github.com/mattermost/mattermost-server>`__.

    - To accept a ticket as a Help Wanted issue, the description should be unambiguous, and include UI description and help text so the change can be implemented and tested by any contributor
    - The triage team also adds the appropriate difficulty level (one of ``Introductory``, ``Intermediate`` and ``Advanced``) and programming language (``Go`` and ``ReactJS``) to the description of the Jira ticket

4 - After triage, PM on community rotation reviews formatting of the GitHub issue and adds appropriate labels for difficulty level and programming language as defined by the triage team.

`See an example Help Wanted issue here <https://github.com/mattermost/mattermost-server/issues/4755>`__.

Managing Help Wanted Issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once a Help Wanted issue is added, the PM on community rotation is responsible for:

- answering questions from community members, which get automatically posted in the `Community Heartbeat channel <https://pre-release.mattermost.com/core/channels/community-heartbeat>`__
- following up with a community member if there hasn't been a response for more than two weeks

Closing Help Wanted Issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once a pull request for an open GitHub Help Wanted issue is merged, please ensure:

- the corresponding GitHub Help Wanted issue is closed, thanking the contributor
- the corresponding JIRA ticket is resolved

Mattermost Community Forums
---------------------------------------------------------

Guidelines for Mattermost `community forums <https://forum.mattermost.org>`__ and public Mattermost `GitHub repositories <https://github.com/mattermost>`__.

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
- **Keep community end-user information secure**
  - If you come across a post that includes the person's IP address, domain name, or other information you think should not be disclosed publicly, edit the post to remove this information. Then click the **hide revision** button so that your edits won't be visible to others on the forum.
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

3. If an issue has a Jira ticket without a ``help-wanted`` label and assigned to the current release fix version for a developer to fix, it can be closed with the following note:

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

Respond to the issue with the following note:

.. code-block:: text

  Thanks, appreciate your feedback @{username}.  

  Would you like to [contribute this in the feature idea forum](https://mattermost.uservoice.com/forums/306457-general/) so it can be discussed, upvoted and considered for a [help wanted ticket](https://docs.mattermost.com/process/help-wanted.html)?

  Please include a link back to this GitHub issue. If you're interested in implementing, please say so and we'll prioritize the review. 

  You get **10** votes in the feature idea forum, and each one influences the future of the project.

Licensing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ask someone to add a license to a GitHub repo, open an issue with the following note, titled ``Add an open source license?``:

.. code-block:: text

  Thanks for sharing this project! We'd love to use it as part of the Mattermost open source project (https://about.mattermost.com/) in our [React Native mobile app](https://github.com/mattermost/mattermost-mobile) (which uses an [Apache 2.0 license](https://github.com/mattermost/mattermost-mobile/blob/master/LICENSE.txt)). 

  Would you consider adding a license, such as an MIT or an Apache 2.0 license? 

  To do so, in GitHub you can hit "Create new file" and name a file `LICENSE.txt`

  ![image](https://cloud.githubusercontent.com/assets/177788/19657017/36238482-99d7-11e6-9fd0-f507970891c7.png)

  This will prompt GitHub to offer a license template: 

  ![image](https://cloud.githubusercontent.com/assets/177788/19657044/5a2d8b66-99d7-11e6-8164-ac7f90b10646.png)

  If you use a license it would make it easy to promote your open source project with the Mattermost community.

  Thanks kindly for your consideration.

Difficult Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To respond to tough questions, use the `SCIPAB method <https://www.mandel.com/top-ten-reasons/tools-methodology/scipab>`__ to help formulate a response and send for community lead to review. 

Situation:
  State what you know about your listeners' circumstances that are relevant to your discussion or presentation, e.g., current state of their business, technology, industry, or plans. 

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

Mattermost Twitter
---------------------------------------------------------

Guidelines for Mattermost `Twitter responses <https://twitter.com/mattermost>`__.

Principles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Avoid acronyms**. Avoid acronyms when possible. For example, say "pull request" instead of "PR", since only a subset of tweet readers are active GitHub users. 
2. **Use the active voice**. Avoid "has", "was", "have been" when possible. For example, instead of "Hackfest has started!" say "Hackfest starts now!" 
3. **Include at most one link**. To provide a clear call to action, include at most one link per tweet and place it near the end of the tweet.
4. **Use exclamation marks only for exciting announcements**. An exclamation mark can be used when the announcement is exciting, but using an exclamation mark should be avoided when it can be confused with a signal for community to panic, e.g. "Security update released!".
5. **Be welcoming**. When asking someone to take action, use "Would you be open to" instead of "Would you like to".

Response Writing Tips
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. When to like (heart) a tweet where Mattermost is mentioned?

 - Our team is on site at an event and tags our handle.
 - A community member shares an event we are at, received a Mattermug, or shared a positive experience and mentions us.

2. When to retweet a post?

 - A community member released an integration and mentions us.
 - Mattermug tweets from community members.
  
Sample Responses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Requests for more information such as a preview of our product.

.. code-block:: text

  Thank you for your interest in Mattermost. You can learn more about us at www.mattermost.com where you can also download a trial of our product.

2. Requests for a specific feature or group of features. 

 - Multiple Feature Requests:

  .. code-block:: text

    Thank you for the suggestions @username. Would you be open to contributing them in the feature idea forum so they can discussed and upvoted by the community? You get 10 votes in the feature idea forum, and each one influences the future of the project.

    https://mattermost.uservoice.com/

 - Single Feature Request: 

  .. code-block:: text

    Thank you for the suggestion @username. Would you be open to contributing it in the feature idea forum so it can discussed and upvoted by the community? You get 10 votes in the feature idea forum, and each one influences the future of the project.

    https://mattermost.uservoice.com/

 - Planned Feature Request: 

  .. code-block:: text

    Thank you for your feedback.  We are excited to share that [feature] will be available in our [edition] Edition soon.  Please see our forum post for more information: [link to forum post]

 - Shipped Feature Request: 

  .. code-block:: text

    Thank you for your feedback.  Mattermost already supports [feature].  You can learn more about it in our documentation:  [link to docs]

3. Feedback about their experience, not specific to a feature or a product.

  .. code-block:: text

    Appreciate the feedback. If your team has suggestions on how to improve Mattermost, we would love to hear more in our feature proposal forum. You get 10 votes there, and each one influences the future of the project: https://mattermost.uservoice.com/

  .. code-block:: text

    Thanks @{username}, highly appreciate your feedback. If you have additional feedback about your experience, we'd love to hear. You can share at http://forum.mattermost.org to start a discussion.

4. Tweet of forum post, asking someone from Mattermost team to respond.

  .. code-block:: text

    Thank you for reaching out. Our team responded to you in the forums and we're happy to help with further questions there.

  .. code-block:: text

    Thank you for reaching out. Our team monitors and responds to forum inquiries. We're happy to help with further questions there.

5. Customer requesting help to address an issue they are having with a deployment or specific feature in the system.

  .. code-block:: text

    Thank you for reaching out. We recommend opening a support ticket where our team can best help you troubleshoot the issue. For more information about Enterprise Edition support levels, see https://about.mattermost.com/support/. 
