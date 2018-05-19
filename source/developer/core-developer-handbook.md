Core Developer Handbook
-----------------------------

This handbook contains documentation useful for Mattermost core developers. A core developer is
a maintainer on the [Mattermost project](https://github.com/mattermost) that has merge access to the Mattermost repositories. They are responsible for reviewing pull requests, cultivating the Mattermost developer community and guiding the technical vision of Mattermost.

Come [join our "Contributors" community channel](https://pre-release.mattermost.com/core/channels/tickets) on our daily build server, where you can discuss questions with community members and the Mattermost core team. Join our ["Developers" channel](https://pre-release.mattermost.com/core/channels/developers) for technical discussions and our ["Integrations" channel](https://pre-release.mattermost.com/core/channels/integrations) for all integrations and plugins discussions.

### Current Core Committers ###

See list of current core committers at [developers.mattermost.com](https://developers.mattermost.com/contribute/getting-started/core-committers).

### Technical Development Goals ###

We discuss these goals every other week during the [weekly developer meeting](https://docs.mattermost.com/process/training.html#developer-meeting).

#### Short Term ####
- Performance for 20,000 daily active users (complete)
- React Native mobile apps (complete)

#### Long Term ####
- Performance for 200,000 daily active users, 200 million messages per month
- Orchestration/SAAS
- Developer Toolkit (APIs, plugins, integrations, samples, documentation)

### Developer Decisions ###

We track decisions made during the [weekly developer meeting](https://docs.mattermost.com/process/training.html#developer-meeting) in a [Google doc here](https://docs.google.com/document/d/1iPzYkqM8Q0oZ1u1VkETUG18lyY47vKN0vAa3WIgvaiI).

### Reviewing & Merging Pull Requests ###

Core developers are expected to code review pull requests submitted to the Mattermost repositories. Below are some guidelines for reviewing code:

- Responsibility for the submitted code relies on the submitter, it is their responsibility to test and implement any changes at high quality. As a result, code reviewers are not required to do a full audit of code changes but should read through the code to:
  - Make sure the implementation matches the description of the ticket being completed
  - Ask questions about anything that is not clear
  - To request changes when the code looks incorrect or doesn't match the correct design patterns
- Stable respositories that have had a 1.0.0 release require two approved reviews before the changes can be merged
- Unstable repositories that are still in development may be merged with a single approved review
- Trivial changes, such as PM-approved text changes or typo fixes, maybe merged with only a single approved review for both stable and unstable repositories

### Release Cutting Process ###

See release cutting process at [developers.mattermost.com](https://developers.mattermost.com/internal/release-process).

### Useful Guides and Documentation ###
- [Adding a webapp component](https://docs.mattermost.com/developer/webapp-component.html)
- [Adding actions and selectors to Redux](https://docs.mattermost.com/developer/redux.html)
- [Migrating a webapp component to Redux](https://docs.mattermost.com/developer/webapp-to-redux.html)
- [Adding an endpoint to APIv4](https://docs.mattermost.com/developer/api4.html)
- [Developer workflow](https://docs.mattermost.com/developer/developer-flow.html)
- [Code style guide](https://docs.mattermost.com/developer/style-guide.html)
