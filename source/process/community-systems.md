# Community Systems 

The goal of Mattermost community systems is to more effectively fulfill the [purpose of Mattermost](http://www.mattermost.org/vision/) through increased communication and feedback from community constituents. 

## Community Constituents 

Feedback from the Mattermost comes from different types of constituent: 

- **End Users** (~10-1000 per server) - Sharing messages and files using Mattermost day-to-day
- **Team Admins** (~1-10 per server) - Managing teams within Mattermost, defining business process
- **IT Admins** (~1-2 per server) - Installing, securing, deploying and managing Mattermost servers 
- **Developers** (~0-1 per server) - Customizing and extending Mattermost through APIs (does not include end users)

## Community Systems

Because types of feedback need to be handled in different ways (E.g. voting for feature requests, hierarchical labels and process documentation for broad discussion, integration with source control systems for bugs and pull requests), multiple systems are used to manage, prioritize and address community feedback. 

Systems include: 

###  Feature Idea Forum 

A forum for filing, upvoting and discussing feature ideas. Reviewed monthly by the core team as part of the planning process for new releases. 

See [Contributing Feature Ideas](http://www.mattermost.org/feature-requests/) for more details on how to use this system. 

_Note: If you want to promote an idea filed in the feature idea forum, or if you are out of votes and want to find like-minded colleagues to vote for you, consider posting to the [Feature Idea Discussion ](https://forum.mattermost.org/t/how-to-use-feature-idea-discussion/63/1) category in the General Forum._


###  Troubleshooting Forum 

A system for peer-to-peer support of installation and configuration questions. 

See [Troubleshooting Forum](https://forum.mattermost.org/t/about-the-trouble-shooting-category/150/1).


### GitHub Issues 

A system primarily used by Mattermost for reporting bugs with clear statements on repro steps and expected behavior. While it's okay to add feature requests and questions here to start conversations, moderators may ask a submitter's help to move discussions to one of the other channels. 

See [Filing Issues](http://www.mattermost.org/filing-issues/) for details on how to file issues for Mattermost in GitHub.

Please consider using more mainstream processes for [filing feature ideas to be upvoted](https://github.com/mattermost/platform/blob/master/doc/process/overview.md#feature-idea-forum), to ask [troubleshooting questions](https://github.com/mattermost/platform/blob/master/doc/process/overview.md#troubleshooting-forum), or [general questions](https://github.com/mattermost/platform/blob/master/doc/process/overview.md#general-forum). 

### GitHub Pull Requests 

A system for submitting pull requests for changes to Mattermost. See [Pull Requests](https://github.com/mattermost/platform/blob/master/doc/process/overview.md#merge-requests) section below. 

### General Forum 

A general, peer-to-peer discussion forum with topics organized by category for general questions, trouble shooting, design feedback requests, and FAQs. Monitored and moderated by core team, which is also active on the forum.

Read more about the [General Forum](https://forum.mattermost.org/t/welcome-to-mattermost-community-discussion/8). 

### Primary Research 

Core team members and key contributors may discuss Mattermost directly with users in a range of systems outside those listed here--in-person meetings, video-conference, usability testing, Twitter, email, etc. Those notes are shared in various Mattermost channels to inform designs. 


___

## Standard responses 

To minimize response times, templates and automation are used across community systems for common requests. 

### Category: Issue Submitter needs to do something

Start with "Please..."

#### GitHub Issues: Please move to Troubleshooting forum

```
Thanks @[GITHUB_USERNAME] for your question, 

Because this seems to be more a troubleshooting discussion than a product defect, could we have your help posting this to the [Troubleshooting Forum](http://www.mattermost.org/troubleshoot/)? 

Please include repro steps, so members from the community will better be able to help solve your issue. Please add a link back to your new post from this ticket and close this ticket so it’s easier to keep track of issues? 
```

##### GitHub Issues: Please move to Feature Ideas forum

```
Thanks @[GITHUB_USERNAME], appreciate your feedback, 

To keep feature idea discussions in one place, could we have your help: 

1. [Contributing this in the feature idea forum](http://www.mattermost.org/feature-requests/) so it can be discussed, upvoted and considered for a [ticket accepting pull requests](http://docs.mattermost.com/process/accepting-pull-request.html)? If you're interested in implementing, please say so and we'll prioritize the review. 

2. Posting a link back from the feature idea forum to this thread? 
```

##### Please add repro steps 

```
Thanks @[GITHUB_USERNAME] for the bug report, 

Can you help [add more information](http://www.mattermost.org/filing-issues/) so we can reproduce the issue? 
```

#### Please rebase 

```
Please rebase this Pull Request
```

### Category: We/community need to do something 

Start with "Needs..."

##### Needs PR reviewer

Needs Reviewer to add `+1` or share feedback to submitter on how to adjust pull request. 

##### Needs PR seconder

After code is reviewed, needs "Seconder" to add `+1` or share feedback to submitter on how to adjust pull request. 

##### Needs PM review

```
Thanks @[GITHUB_USERNAME] for your feedback. 

This ticket requires design review. Asking help from @[Core Team PM]
```

##### Needs merge (review complete)

PR has been reviewed and seconded and is awaiting merge. 

##### Needs Jira ticket

? + Assign to ?

Response after Jira ticket is created:

```
Thanks @[GITHUB_USERNAME], [Jira ticket]([LINK_TO_JIRA_TICKET]) created for this issue. 
```

#### Category: Help from community 

Start with "Asking..."

##### Asking community help to repro 

```
Thanks @[GITHUB_USERNAME] for the issue report, 

Would anyone from the community be able to help repro this issue to verify it can be reproduced? 
```

#### Category: Miscellanous Issues

##### Duplicate Jira ticket

```
Thanks @[GITHUB_USERNAME] for the report, 

We have a [Jira Ticket]([LINK_TO_JIRA_TICKET]) tracking the issue. 
```

##### Setup Test Server

Adding this label sets up a test server, removing it shuts down the test server. 

##### Substantial commit

A PR that requires careful review due to size. 

##### DO NOT MERGE 

A PR submitted for discussion that SHOULD NOT be merged.
