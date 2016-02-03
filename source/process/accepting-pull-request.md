# Accepting Pull Requests

Per the [Code Contribution Guidelines](http://docs.mattermost.com/developer/contribution-guide.html), other than small fixes and improvements, only pull requests referencing Jira tickets with the "accepting pull requests" (APR) label should be submitted to Mattermost projects. This system ensures:

1. Proposed changes have been unambiguously specified 
2. The change meets the [fast, obvious, forgiving](http://www.mattermost.org/design-principles/) design principle for the project
3. Volunteers are willing to test, document, support and maintain changes (authentication options need manually testing with each monthly release in perpetuity)
4. The change [aligns to the stated purpose of the project](http://www.mattermost.org/vision/#mattermost-teams-v1)

Key contributors and core team members are responsible for nominating changes for APR status by opening a Jira ticket. 

#### Nominating changes for Accepting Pull Request status 

Jira tickets nominating a feature for APR status should include the following: 

1. Title clearly and concisely describes change proposed
2. Title includes "(Proposed APR)" so triage knows to consider it for an `accepting-pull-requests` label
3. Description is unambiuous and includes UI description and help text so feature can be implemented and tested by any contributor
4. If this ticket came from a community discussion, include a link in description to community channel, and in community channel link to Jira ticket

So long as tickets meet the APR criteria, triage team will add `accepting-pull-requests` label to have the ticket appear in the [issues Accepting Pull Requests](https://mattermost.atlassian.net/issues/?filter=10101) list. 

