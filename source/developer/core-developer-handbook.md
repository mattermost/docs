Core Developer Handbook
-----------------------------

This handbook contains documentation useful for Mattermost core developers. A core developer is
a maintainer on the [Mattermost project](https://github.com/mattermost) that has merge access to the Mattermost repositories. They are responsible for reviewing pull requests, cultivating the Mattermost developer community and guiding the technical vision of Mattermost.

Come [join our "Contributors" community channel](https://pre-release.mattermost.com/core/channels/tickets) on our daily build server, where you can discuss questions with community members and the Mattermost core team. Join our ["Developers" channel](https://pre-release.mattermost.com/core/channels/developers) for technical discussions and our ["Integrations" channel](https://pre-release.mattermost.com/core/channels/integrations) for all integrations and plugins discussions.

### Current Core Developers ###

Below is the list of core developers working on Mattermost:
- **Corey Hulen**
  - @corey on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@corey) and [@coreyhulen](https://github.com/coreyhulen) on GitHub
  - Dev areas: High Availability, Orchestration/Kubernetes, Push Proxy, Classic Mobile Apps
- **Joram Wilander**
  - @joram on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@joram) and [@jwilander](https://github.com/jwilander) on GitHub
  - Dev areas: Webapp, Redux, REST API, Developer Toolkit, OAuth SSO, Statuses, WebSocket, Licensing
- **Christopher Speller**
  - @christopher on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@christopher) and [@crspeller](https://github.com/crspeller) on GitHub
  - Dev areas: Performance, Security, Build, LDAP, Load Tests, Webpack, Permissions
- **Harrison Healey**
  - @harrison on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@harrison) and [@hmhealey](https://github.com/hmhealey) on GitHub
  - Dev areas: Markdown, React Native, Autocomplete, UI, Emojis, Reactions, Files
- **Elias Nahum**
  - @elias on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@elias) and [@enahum](https://github.com/enahum) on GitHub
  - Dev areas: React Native, Redux, Localization, SAML, OAuth, WebRTC
- **George Goldberg**
  - @george on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@george) and [@grundleborg](https://github.com/grundleborg) on GitHub
  - Dev areas: Import/Export (Slack, Bulk Loading, etc.), Diagnostics/Telemetry, Search, Permissions
- **Saturnino Abril**
  - @saturnino on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@saturnino) and [@saturninoabril](https://github.com/saturninoabril) on GitHub
  - Dev areas: Webapp, React Native, REST API, UI Tests
- **Chris Duarte**
  - @uberchris on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@uberchris) and [@csduarte](https://github.com/csduarte) on GitHub
- **Carlos Panato**
  - @cpanato on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@cpanato) and [@cpanato](https://github.com/cpanato) on GitHub
  - Dev areas: Webapp, Redux, REST API, WebSocket Events
- **Martin Kraft**
  - @martin.kraft on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@martin.kraft) and [@mkraft](https://github.com/mkraft) on GitHub
  - Dev areas: All areas
- **Jesús Espino**
  - @jesus.espino on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@jesus.espino) and [@jespino](https://github.com/jespino) on GitHub
  - Dev areas: Webapp, Permissions and Compliance, Sample data generation
- **Jesse Hallam**
  - @jesse.hallam on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@jesse.hallam) and [@lieut-data](https://github.com/lieut-data) on GitHub
  - Dev areas: Performance, Webapp, Database
- **Sudheer Timmaraju**
  - @sudheerdev on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@sudheerdev) and [@sudheerDev](https://github.com/sudheerDev) on GitHub
  - Dev areas: Webapp, React, Redux, Performance

Below is the list of core developers working on individual Mattermost repositories:
- **Yuya Ochiai** - [desktop](https://github.com/mattermost/desktop)
  - @yuya-oc on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@yuya-oc) and [@yuya-oc](https://github.com/yuya-oc) on GitHub
- **Pan Luo** - [mattermost-docker](https://github.com/mattermost/mattermost-docker)
  - @compass on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@compass) and [@xcompass](https://github.com/xcompass) on GitHub
- **Kyâne Pichou** - [mattermost-docker](https://github.com/mattermost/mattermost-docker)
  - @pichouk on [pre-release.mattermost.com](https://pre-release.mattermost.com/core/messages/@pichouk) and [@pichouk](https://github.com/pichouk) on GitHub

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

**Note: To cut a build you need access to matterbuild. Please ask Christopher for access if you don't have it.**

On code complete day, work with the PM on rotation to get all the pull requests for the current release merged into `master`. Once that is done and you've confirmed with the PM, cut the first release candidate by following these steps:

1. Submit a PR to uncomment the upgrade code for the release version and add it to the version array. Use these PRs as examples, [https://github.com/mattermost/mattermost-server/pull/6336/files](https://github.com/mattermost/mattermost-server/pull/6336/files) and [https://github.com/mattermost/mattermost-server/pull/6600/files](https://github.com/mattermost/mattermost-server/pull/6600/files).
2. Once the above PR is merged, post `/mb cut X.X.X-rc1` into a private channel. Replace `X.X.X` with the release version, ex: `3.10.0`. This will begin cutting the build and make an automatic post to the Release Discussion channel.
3. Wait approximately 40 minutes for the build to finish. If the build fails, you will need to delete the version tags from the mattermost-server, mattermost-webapp and enterprise repositories by running `git push origin :vX.X.X-rc1` in all of them. Then simply repeat step 2. You can monitor build status from https://build.mattermost.com.
4. Once the build finishes, submit a PR to `master` to add the upgrade code for the next release. For example, [https://github.com/mattermost/mattermost-server/pull/6337/files](https://github.com/mattermost/mattermost-server/pull/6337/files) and [https://github.com/mattermost/mattermost-server/pull/6616/files](https://github.com/mattermost/mattermost-server/pull/6616/files).

The build automation will take care of updating all the CI and test servers, and it will make a post in the Release Discussion channel with all the download links. It will also create the release branch named `release-X.X`, with `X-X` replace by the major and minor version numbers.

Between now and the final release being cut, work with the PM on rotation to get priority fixes merged into the release branch. Note that all PRs to the release branch:

1. Must be for Jira tickets approved for this release by you and the PM on rotation.
2. Should be assigned to you and have the correct milestone set.

Work with the PM on rotation to decide when to cut new release candidates. The general guideline is cut a new RC after 3-5 fixes have been merged or it's been a day or two since any more issues have come up. Each release usually has 3-4 release candidates. To cut a new release candidate:

1. Post `/mb cut X.X.X-rcX` into a private channel, replacing `X.X.X-rcX` with the release version and the release candidate number we're on. For example, `3.10.0-rc2`.
2. Wait for the build to finish, deleting tags  (`git push origin :X.X.X-rcX`) and re-running if the build fails.

Again, the build automation will update all the servers and post in the Release Discussion channel.

When it's time to cut the final build, confirm with the PM that no more changes need to be merged. To cut the final release:

1. Post `/mb cut X.X.X` into a private channel, replacing `X.X.X` with the release version.
2. Just like before, if the build fails you can delete the tags and re-run it.

The links to download the final build will be posted in the Release Discussion channel. Congratulations you've cut a release!

After a couple days pass you will need to set the CI servers to point back to `master`. To do this:

1. Post `/mb setci master` into a private channel.
2. Post `/mb setprerelease master` into a private channel.

That's it!

### Useful Guides and Documentation ###
- [Adding a webapp component](https://docs.mattermost.com/developer/webapp-component.html)
- [Adding actions and selectors to Redux](https://docs.mattermost.com/developer/redux.html)
- [Migrating a webapp component to Redux](https://docs.mattermost.com/developer/webapp-to-redux.html)
- [Migrating redux file to Flow](https://docs.mattermost.com/developer/redux-to-flow.html)
- [Adding an endpoint to APIv4](https://docs.mattermost.com/developer/api4.html)
- [Developer workflow](https://docs.mattermost.com/developer/developer-flow.html)
- [Code style guide](https://docs.mattermost.com/developer/style-guide.html)
