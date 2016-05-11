# Bugs, Feature Ideas, Troubleshooting

Here's how to engage with the Mattermost community: 

- **Bugs** - [Search for existing bugs and file a GitHub issue if your bug is new](http://www.mattermost.org/filing-issues/). 
- **Feature Ideas** - [Add a feature idea to be discussed or upvoted](http://www.mattermost.org/feature-requests/).
- **Troubleshoot** - [Search articles and add topic if issue is new](https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150).
- **General discussion** - [Join the Mattermost Forum](https://forum.mattermost.org/t/welcome-to-the-mattermost-general-forum/8). 
- **Contribute code** - Select tickets [accepting pull requests](https://mattermost.atlassian.net/browse/PLT-2244?filter=10101) and follow [guidelines to contribute](http://docs.mattermost.com/developer/contribution-guide.html). 
- **Contributor and tester discussion** - Contributors and testers can use [nightly builds server](https://pre-release.mattermost.com/core) to work on next release.
- **Approved changes** - See [Jira database](https://mattermost.atlassian.net/secure/Dashboard.jspa) to view open, in-progress, resolved and closed tickets. 
- **Licensing questions** - Please mail info@mattermost.com. 
- **Commercial support** - Mattermost Enterprise Edition customers can access [commercial support](https://about.mattermost.com/support/) based on their subscription option.

## How improvements are made to Mattermost

Every month, the Mattermost community plans, builds, tests, documents, releases and supports new product improvements for Team Edition to benefit the user community, and the Mattermost Enterprise Team does the same for Enterprise Edition to benefit the subscriber community. 

1. When a feature idea is within the scope of Team Edition, as [defined in the Mattermost Manifesto](http://www.mattermost.org/manifesto/#mattermost-teams) and considered a priority, a Jira ticket is created to define its implementation: 

    1. If the change is not complex, an [Accepting Pull Requests](http://docs.mattermost.com/process/accepting-pull-request.html) label may be added to the Jira ticket for any developer to contribute the change to the Mattermost Team Edition code base via the [contribution process](http://docs.mattermost.com/developer/contribution-guide.html). [A list of tickets accepting pull requests](https://mattermost.atlassian.net/browse/PLT-2667?filter=10101) is offered to all contributors who read the contributor's guide, and these provide a steady stream of improvements to Team Edition month after month. 
    2. If change is considered high priority without pre-requisites, a Fix Version may be applied to the Jira ticket for the Mattermost core team or key contributors to add for an upcoming monthly release. Priority decisions are influenced by discussion and voting in the feature idea forum and community systems as well as feedback from key contributors. 
    3. If change is not seen as high priority or has pre-requisites, it is assigned a Fix Version of `backlog` and will be considered monthly for inclusion in a future release.

2. When a feature idea does not fit the scope of Team Edition, as [defined in the Mattermost Manifesto](http://www.mattermost.org/manifesto/#mattermost-teams), but benefits Enterprise Edition subscribers, a similar process as above is undertaken by the Enterprise Team.

    1. If change is considered high priority without pre-requisites, a Fix Version may be applied to the Jira ticket for the Mattermost Enterprise Team to add for an upcoming monthly release. Priority decisions are influenced by discussion with Enterprise Edition subscribers, with special attention paid to members of the [Core Access](https://about.mattermost.com/core-access/) program. 
    2. If change is not seen as high priority or has pre-requisites, it is assigned a Fix Version of `backlog` until this situation changes.  
    3. If an existing or potential Enterprise Edition subscriber needs a specific change that has not yet been assigned a Fix Version, they can contact the Mattermost Enterprise Team to discuss sponsoring the feature with Non-Recurring Engineering (NRE) funding to have it delivered before it would otherwise be added. Feature sponsorship can only be applied to features where Jira tickets exist.
    
3. If a feature idea is not within the scope of either Team Edition or Enterprise Edition, you might consider: 

    1. Building an integration using Mattermost webhooks or Slash commands. There are [dozens of open source examples](http://www.mattermost.org/community-applications/) to help you start. Example: Suppose you want a link preview for an esoteric file type that Mattermost isn't able to support, you can create an outgoing webhook to reply with an image that offers a preview. 
    
    2. Building a client application using the Mattermost Web Service API. This is useful if you want to customize the user experience to your specific needs. Example: You can re-create the Mattermost web interface using Windows controls to define front end logic, similar to the [MattermostWPF project](https://github.com/limey98/MattermostWPF). 
    
    3. Creating an open source variation of Mattermost using the Team Edition source code. Example: The Mozilla Foundation created their own [open source Mattermost variation](https://github.com/mozilla/chat.mozillafoundation.org), which includes changes specific to their needs.

## GitHub Issues Workflow

To minimize response times, templates and automation are used across community systems for common requests. When misfiled requests are are posted in GitHub close them soon so the community does not confuse them as being appropriate. 

### Category: Issue Submitter needs to do something

Start with "Please..."

##### Label: Please move to Troubleshooting forum

```
Thanks @[GITHUB_USERNAME] for your question, 

Because this seems to be more a troubleshooting discussion than a product defect, could we have your help posting this to the [Troubleshooting Forum](http://www.mattermost.org/troubleshoot/)? 

Per above link, please include repro steps to make it easier to solve your issue. Also, please link back to your new post from this issue? 
```

##### Label: Please move to Feature Ideas forum

```
Thanks @[GITHUB_USERNAME], appreciate your feedback, 

To keep feature idea discussions in one place, could we have your help: 

1. [Contributing this in the feature idea forum](http://www.mattermost.org/feature-requests/) so it can be discussed, upvoted and considered for a [ticket accepting pull requests](http://docs.mattermost.com/process/accepting-pull-request.html)? 

   Please include a link back to this GitHub Issue. If you're interested in implementing, please say so and we'll prioritize the review. 

2. Posting a link back from the feature idea forum to this thread? 
```

##### Label: Please add repro steps 

```
Thanks @[GITHUB_USERNAME] for the bug report, 

Can you help [add more information](http://www.mattermost.org/filing-issues/) so we can reproduce the issue? 
```

##### Label: Please rebase 

```
Please rebase this Pull Request
```

### Category: We/community need to do something 

Start with "Needs..."

##### Label: Needs PR reviewer

Needs Reviewer to add `+1` or share feedback to submitter on how to adjust pull request. 

##### Label: Needs PR seconder

After code is reviewed, needs "Seconder" to add `+1` or share feedback to submitter on how to adjust pull request. 

##### Label: Needs PM review

```
Thanks @[GITHUB_USERNAME] for your feedback. 

This ticket requires design review. Asking help from @[Core Team PM]
```

##### Label: Needs merge (review complete)

PR has been reviewed and seconded and is awaiting merge. 

##### Label: Needs Jira ticket

? + Assign to ?

Response after Jira ticket is created:

```
Thanks @[GITHUB_USERNAME], [Jira ticket]([LINK_TO_JIRA_TICKET]) created for this issue. 
```

### Category: Miscellanous Issues

##### Label: Asking community help to repro 

```
Thanks @[GITHUB_USERNAME] for the issue report, 

Would anyone from the community be able to help repro this issue to verify it can be reproduced? 
```

##### Label: Duplicate Jira ticket

```
Thanks @[GITHUB_USERNAME] for the report, 

We have a [Jira Ticket]([LINK_TO_JIRA_TICKET]) tracking the issue. 
```

##### Label: Setup Test Server

Adding this label sets up a test server, removing it shuts down the test server. 

##### Label: Substantial commit

A PR that requires careful review due to size. 

##### Label: DO NOT MERGE 

A PR submitted for discussion that SHOULD NOT be merged.
