Community Monitoring Process
============================

This document outlines the process for monitoring and responding to community questions in various channels.

Community Manager
-----------------

When responding to issues:

1. Identify what type of post it is:

  - Troubleshooting
  - Feature Proposal
  - Bug
  - Developer/Product Question

2. Ask questions to narrow down or understand the issue better:

  - Try to understand the issue yourself as much as possible first
  - If appropriate, ask a developer for assistance on technical questions

3. Respond:

  - Include a link to related documentation in your response (e.g. Jira ticket, feature proposal, etc.)
  - If there is no related documentation, write the documentation and include the link in your response:

    - For reproducible bugs, create a Jira ticket
    - For product questions or troubleshooting, update docs.mattermost.com if appropriate
    - For feature proposals, ask them to `create a feature proposal <https://www.mattermost.org/feature-ideas/>`__ and post the link back

  - If appropriate, ask if the community member would be interested in contributing the feature / bug fix


Community channels
------------------

The various community channels are outlined below. On a daily basis, the Community Manager helps with notifying team members about issues in need of a response and, if necessary, asks for help from a developer.

1. `Peer-to-peer Help Channel <https://community.mattermost.com/core/channels/peer-to-peer-help>`__: Forum Issues / GitLab / Stack Overflow

  - Description:

    - Community Manager reviews new `GitHub mattermost/mattermost-server <https://github.com/mattermost/mattermost-server>`__ and `GitHub mattermost/mattermost-mobile <https://github.com/mattermost/mattermost-mobile/issues>`__ issues daily, and responds to all new issues:

        - Bug Report: Try to reproduce, or ask another team member to reproduce
        - Troubleshooting: Request to move to forums
        - Feature Proposal: Request to move to feature idea forums

    - Community Manager posts "[Help Wanted] #forum #github @here @[dev on rotation] These forum posts are open to everyone in the community. If you find something you think you know the answer to or can help with, please help post a response and be part of creating a vibrant Mattermost community!" with a list that includes:

      - Forum and `GitHub mattermost/mattermost-server <https://github.com/mattermost/mattermost-server>`__ posts that are >=2 days old (this gives community members a chance to respond first)
      - New forum posts referencing Enterprise features or upgrade issues after a release
      - Forum posts with a new reply to questions asked by the core team

    - Everyone from the team/community can step in and answer forum posts

  - Community Manager Responsibility:

    - Review the list for posts that haven’t been answered, and either reply (with help from dev if needed) or route to the appropriate person, following up to make sure a response is posted
    
2. `Peer-to-peer Help Channel <https://community.mattermost.com/core/channels/peer-to-peer-help>`__: UserVoice Issues

  - Description:

    - Ops Team @mentions the Community PM with a list that includes issues:

      - where status requires updating
      
        - Under Review: After a ticket is created but the spec is not yet complete
        - Planned: Jira ticket with a plan on how to build the feature
        - Started: When a developer has begun to work on the Jira ticket (the ticket shows that it is in progress)
        - Help Wanted: Ticket that is open to any contributor wanting to work on the issue
        - Completed: When ticket is resolved
        - Declined: When the suggestion does not fit with the `product vision <https://www.mattermost.org/manifesto/>`__
        
      - where a PM might want to ask a question for clarification or ideas on how to design something
      - where the requester specifies they want to work on the feature
      
    - Community PM Responsibility - Team Edition:
    
      - The PM who is release manager for the current release cycle will update the issues after release date.

        - Thank you [NAME] for nominating the feature! It is now available in Mattermost [X.Y]. Would anyone like to help re-tweet the announcement? [LINK TO TWEET]
        
        - Updates a `spreadsheet <https://docs.google.com/spreadsheets/d/1nljd4cFh-9MXF4DxlUnC8b6bdqijkvi8KHquOmK8M6E/edit#gid=0>`__ that tracks UserVoice issues announced in upcoming releases.

    - Sales Responsibility - Enterprise Edition:
    
      - Responds to the issues and closes them after release date.
      
        - Thank you [NAME] for nominating the feature! It is now available in Mattermost [X.Y].
        
      - Updates `Spreadsheet <https://docs.google.com/spreadsheets/d/1nljd4cFh-9MXF4DxlUnC8b6bdqijkvi8KHquOmK8M6E/edit#gid=0>`__ to track UserVoice issues to be announced in upcoming releases.

3. Weekly, usually Wednesdays, `Peer-to-peer Help Channel <https://community.mattermost.com/core/channels/peer-to-peer-help>`__: GitHub , GitLab and StackOverflow issues with Activity Older than 7 days (that have not been created by Mattermost staff)

  - Description:

    - The Community Manager reviews “GitHub, GitLab and StackOverflow issues with activity older than 7 days” from the following repos and adds a list of issues to the daily Peer-to-peer Help channel post:

      - https://github.com/mattermost/mattermost-server/issues
      - https://github.com/mattermost/docs/issues
      - https://github.com/mattermost/mattermost-api-reference/issues
      - https://github.com/mattermost/mattermost-bot-sample-golang/issues 
      - https://github.com/mattermost/mattermost-load-test/issues
      - https://github.com/mattermost/mattermost-push-proxy
      - [a month or older - reviews are monthly] https://github.com/mattermost/android/pulls
      - [a month or older - reviews are monthly] https://github.com/mattermost/ios/pulls
      - http://stackoverflow.com/questions/tagged/mattermost?sort=newest&pageSize=15 
      - https://gitlab.com/search?utf8=%E2%9C%93&search=mattermost&group_id=&project_id=20699&scope=issues&repository_ref= 
      - https://gitlab.com/gitlab-org/gitlab-mattermost/issues 
      - https://gitlab.com/gitlab-org/omnibus-gitlab/issues?label_name=Mattermost
      - https://gitlab.com/gitlab-org/gitlab-ce/issues?label_name=mattermost

4. Help Wanted GitHub Issues:

 - Description:

   - New GitHub Help Wanted issues are automatically created from JIRA tickets and are open for community contributions.  The Community Manager can disregard these issues as they do not need to be posted to the Peer-to-peer Help channel.
