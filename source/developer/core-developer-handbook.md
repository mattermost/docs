Core Developer Handbook
-----------------------------

This handbook contains documentation useful for Mattermost core developers. A core developer is 
a maintainer on the [Mattermost project](https://github.com/mattermost) that has merge access to the Mattermost repositories. They are responsible for reviewing pull requests, cultivating the Mattermost developer community and guiding the technical vision of Mattermost.

### Current Core Developers ###

Below is the list of core developers working on Mattermost:
* Corey Hulen - @corey on [pre-release.mattermost.com](https://pre-release.mattermost.com/) and [@coreyhulen](https://github.com/coreyhulen) on GitHub
* Joram Wilander - @joram on [pre-release.mattermost.com](https://pre-release.mattermost.com/) and [@jwilander](https://github.com/jwilander) on GitHub
* Christopher Speller - @christopoher on [pre-release.mattermost.com](https://pre-release.mattermost.com/) and [@crspeller](https://github.com/crspeller) on GitHub
* Harrison Healey - @harrison on [pre-release.mattermost.com](https://pre-release.mattermost.com/) and [@hmhealey](https://github.com/hmhealey) on GitHub
* Elias Nahum - @elias on [pre-release.mattermost.com](https://pre-release.mattermost.com/) and [@enahum](https://github.com/enahum) on GitHub
* George Goldberg - @george on [pre-release.mattermost.com](https://pre-release.mattermost.com/) and [@grundleborg](https://github.com/grundleborg) on GitHub

### Reviewing & Merging Pull Requests ###

Core developers are expected to code review pull requests submitted to the Mattermost repositories. Below are some guidelines for reviewing code:

* Responsibility for the submitted code relies on the submitter, it is their responsibility to test and implement any changes at high quality. As a result, code reviewers are not required to do a full audit of code changes but should read through the code to:
 * Make sure the implementation matches the description of the ticket being completed
 * Ask questions about anything that is not clear
 * To request changes when the code looks incorrect or doesn't match the correct design patterns
* Stable respositories that have had a 1.0.0 release require two approved reviews before the changes can be merged
* Unstable repositories that are still in development may be merged with a single approved review
* Trivial changes, such as PM-approved text changes or typo fixes, maybe merged with only a single approved review for both stable and unstable repositories

### Technical Direction Resolutions ###

Technical direction resolutions are any decisions made by the team affecting the technical direction of Mattermost. The current resolutions in effect are listed below:

1. Removing usage of jQuery. When working in a file that imports jQuery, developers should mke an effort to replace it with vanilla JavaScript and remove the import. When reviewing pull requests that add more jQuery, please ask the submitter to use vanilla JS.
2. Server and client changes for the [platform respository](https://github.com/mattermost/platform) must be submitted in separate pull requests. First add server support, then add client support.
3. As of server 3.8, all new API endpoints should be made in API version 4. API version 3 should only be modified for bug fixes, security and/or performance issues. ([https://pre-release.mattermost.com/core/pl/xcyqqdpkgtb4mcexxxu7mpfssh](https://pre-release.mattermost.com/core/pl/xcyqqdpkgtb4mcexxxu7mpfssh))
4. Moving the webapp over to share a service layer built on top of Redux. ([https://pre-release.mattermost.com/core/pl/x49ra6zk9frq7yccpo753a377o](https://pre-release.mattermost.com/core/pl/x49ra6zk9frq7yccpo753a377o))
