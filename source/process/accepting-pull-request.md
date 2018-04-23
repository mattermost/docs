# Accepting Pull Requests

Per the [Code Contribution Guidelines](http://docs.mattermost.com/developer/contribution-guide.html), other than small fixes and improvements, only pull requests referencing [Jira tickets with the `accepting pull requests` (APR) label](https://mattermost.atlassian.net/issues/?filter=10101) should be submitted to Mattermost projects. This ensures:

1. Proposed changes have been unambiguously specified 
2. The change meets the [fast, obvious, forgiving](http://www.mattermost.org/design-principles/) design principle for the project
3. Volunteers are willing to test, document, support and maintain changes (authentication options are critical paths that need manual testing with each bi-monthly release in perpetuity)
4. The change [aligns to the stated purpose of the project](http://www.mattermost.org/vision/#mattermost-teams-v1)

Key contributors and core team members nominate changes for APRs by opening a Jira ticket. 

#### Nominating changes for Accepting Pull Request status 

Jira tickets nominating a feature for APR status should include: 

1. Title clearly and concisely describes change proposed
2. Title includes "(Proposed APR)" so triage knows to consider it for an `accepting-pull-requests` label
3. Description is unambiuous and includes UI description and help text so feature can be implemented and tested by any contributor
4. If related to a community discussion, include link to ticket in discussion and link to discussion in ticket

Tickets meeting APR criteria receive an `accepting-pull-requests` label by triage team and appear in [APR list](https://mattermost.atlassian.net/issues/?filter=10101) list. 

