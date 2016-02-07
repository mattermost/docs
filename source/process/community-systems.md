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

## Automated responses 

To minimize response times, templates and automation are used across community systems. 

### Automated responses for GitHub Issues 

Below is a list of template responses for working with GitHub issues effectively. 

#### Feature Requests

##### Please add to feature request forum

This response should be used when there's a **Move to Troubleshooting** label attached to a response. 

```
Thanks @[GITHUB_USERNAME], appreciate your feedback, 

To keep feature idea discussions in one place, could we have your help: 

1. [Contributing this in the feature idea forum](http://www.mattermost.org/feature-requests/) so it can be upvoted, discussed and considered for a ticket accepting pull requests?
2. Posting a link back from the feature idea forum to this thread? 

This issue may be closed in 7-10 days. 
```

##### Changes required before accepting feature request

```

Thanks @[GITHUB_USERNAME] for the feature idea, 

Some thoughts below for your consideration: 

[FEEDBACK]

Let us know your feedback and we can add a ticket to [**accepting-pull-requests**](https://mattermost.atlassian.net/issues/?filter=10101) list for this? 
```

#### Duplicate of issue Accepting Pull Request

```
Hi @[GITHUB_USERNAME], thanks for the report!

There's a [known issue accepting pull requests](https://mattermost.atlassian.net/browse/PLT-835) and we're hoping to have it resolved before the next release. 

Our hope is to find a community member who'd like to knock this out as a [good first contribution project](https://mattermost.atlassian.net/issues/?filter=10206), and if not, then it'll fall into the core team's priority queue, 

We try to balance providing opportunities for the community to participate with product quality, 
```

#### Bug Reports

#### Add repro steps per mattermost.org/filing-issues/?

```
Thanks @[GITHUB_USERNAME] for the bug report, 

Please help by adding repro steps and information on your browser/OS so it is easier for others to reproduce and later fix.
````

####  Can anyone from community repro this?

```
Thanks @[GITHUB_USERNAME] for the issue report, 

We haven’t been able to get repro steps for this on the Core team.  Is anyone from the community able to repro?
```

#### Move per mattermost.org/troubleshoot?

```
Thanks @[GITHUB_USERNAME] for your query, 

Please help by moving it to our [Troubleshooting Forum](http://www.mattermost.org/troubleshoot/), where you will have peer-to-peer help solving your issue.
```

