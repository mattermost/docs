# Accepting Pull Requests

Per the [Contributor Guide](https://github.com/mattermost/platform/blob/master/CONTRIBUTING.md), only PRs that reference Jira tickets with the "accepting pull requests" (APR) label should be submitted to the [Mattermost/Platform](https://github.com/mattermost/platform) repo. This system ensures:

1. Volunteers are willing to test, document, and support the changes (authentication options must be manually tested with each monthly release in perpetuity)
2. The change meets the [fast, obvious, forgiving](http://www.mattermost.org/design-principles/) design principle for the project.
3. The change [aligns to the stated purpose of the project](http://www.mattermost.org/vision/#mattermost-teams-v1)
4. Proposed changes have been unambiguously specified so intended functionality is clear
 
Key contributors and core team members are responsible opening Jira tickets that meet the above requirements, which are then reviewed in triage meetings. 

#### Checklist for creating Accepting Pull Request Ticket 

When opening Jira tickets for accepting-pull-requests core team members should:

1. Use clear titles
  1. Concisely describe the change propose
  2. Include the words "(Proposed APR)" so triage team knows to add the `accepting-pull-requests` tag if appropriate
2. Provide unambiguous description so that feature can be implemented and tested by any volunteer, including explicit description of user interface and help text.
3. Description should include a Link back to community discussions related to this change
4. Link to Jira ticket should be posted in community channel where Jira ticket was needed 

The triage team will add `accepting-pull-requests` label to have the ticket appear in the [issues Accepting Pull Requests](https://mattermost.atlassian.net/issues/?filter=10101) list. 

