Community Monitoring Process
============================

This document outlines the process for monitoring and responding to community questions in various channels.

Community Product Manager
--------------------------

Every week, we rotate which PM is responsible for making sure community questions get answered. We rotate alphabetically (for example, Eric -> Jason -> Lindsay).

When responding to issues:

1. Identify what type of post it is:

  - Troubleshooting
  - Feature Request
  - Bug
  - Developer/Product Question

2. Ask questions to narrow down or understand the issue better:

  - Try to understand the issue yourself as much as possible first
  - If appropriate, ask a developer for assistance on technical questions

3. Respond:

  - Include a link to related documentation in your response (eg Jira ticket, feature request, etc.)
  - If there is no related documentation, write the documentation and include the link in your response:

    - For reproducible bugs, create a Jira ticket
    - For product questions or troubleshooting, update docs.mattermost.com if appropriate
    - For feature requests, ask them to `create a feature request <https://www.mattermost.org/feature-ideas/>`_ and post the link back

  - If appropriate, ask if the community member would be interested in contributing the feature / bug fix


Community channels
------------------

The various community channels are outlined below, along with the responsibilities of the Ops Team and the PM on community rotation. Generally the Ops Team helps with notifying team members about issues in need of a response, and the Community PM coordinates to make sure the responses are made. 

1. Contributors Channel: Forum Issues / GitLab / Stack Overflow

  - Description:

    - Ops posts [Help Wanted] #forum @here can anyone help with these forum questions? These forum posts are open to everyone in the community. If you find something you think you know the answer to or can help with, please help post a response and be part of creating a vibrant Mattermost community!" with a list that includes:

      - Forum posts that are >=2 days old (this gives community members a chance to respond first)
      - New forum posts referencing Enterprise features or upgrade issues after a release
      - Forum posts with a new reply to questions asked by the core team

    - Everyone from the team/community can step in and answer forum posts

  - Community PM Responsibility:

    - Review the list for posts that haven’t been answered, and either reply (with help from dev if needed) or route to the appropriate person, following up to make sure a response is posted

2. Community Channel: GitHub Issues with Activity Older than 7 days

  - Description:

    - Ops Team @mentions the Community PM and posts a list of “GitHub issues with activity older than 7 days” from the following repos:

      - https://github.com/mattermost/platform/issues
      - https://github.com/mattermost/docs/issues
      - https://github.com/mattermost/ios/issues
      - https://github.com/mattermost/push-proxy/pulls
      - https://github.com/mattermost/mattermost-docker-preview/issues
      - https://github.com/mattermost/mattermost-bot-sample-golang/issues
      - https://github.com/mattermost/mattermost-load-test/issues
      - https://github.com/mattermost/mattermost-api-reference/issues
      - [a month or older - reviews are monthly] https://github.com/mattermost/android/pulls
      - [a month or older - reviews are monthly] https://github.com/mattermost/ios/pulls

  - Community PM Responsibility:

    - Review the list and either reply (with help from dev if needed) or route to the appropriate person, following up to make sure a response is posted

3. New GitHub Issues:

  - Description:

    - New GitHub issues are submitted by community members to Mattermost repos

  - Community PM Responsibility:

    - Review the repos daily, and respond to all new issues:

      - Bug Report: Try to reproduce, or ask another team member to reproduce
      - Troubleshooting: Request to move to forums
      - Feature Request: Request to move to feature idea forums

4. Customer Zendesk Issues:

  - Description:

    - Sales team will @mention the community PM in Mattermost with the Zendesk ticket that needs a response

  - Community PM Responsibility:

    - Click the Zendesk hashtag to review previous ticket conversation (or view directly in Zendesk)
    - In the Mattermost thread: Answer the question (with dev help if necessary), or draft a response asking follow up questions
    - @mention Hanna, and she will reply to the customer in Zendesk
