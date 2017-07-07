# Code Contribution Guidelines

Thank you for your interest in contributing to Mattermost. To help with translations, [see the localization process](https://docs.mattermost.com/developer/localization.html). For code contributions, here's the process:  

## Choose a Ticket

1. Choose a ticket from the [Help Wanted GitHub Issues](https://github.com/mattermost/platform/issues?utf8=%E2%9C%93&q=is%3Aissue%20is%3Aopen%20%5BHelp%20Wanted%5D) list.
    - Make sure that it doesn't have an [open pull request](https://github.com/mattermost/platform/pulls) for it.

2. Before starting to work on the ticket, comment to let people know you're working on it.

3. If you have questions, post them in [Mattermost forum](http://forum.mattermost.org/) or join the [Contributors](https://pre-release.mattermost.com/core/channels/tickets) channel and announce the ticket you'd like to work on so it can be assigned to you. 

It is fine to submit a PR for a bug or an incremental improvement with less than 20 lines of code change without a Help Wanted issue if the change to existing behaviour is small. Some examples include

 - [Fix a formatting error in help text](https://github.com/mattermost/platform/pull/5640)
 - [Fix success typo in Makefile](https://github.com/mattermost/platform/pull/5809)
 - [Fix broken Cancel button in Edit Webhooks screen](https://github.com/mattermost/platform/pull/5612)
 - [Fix Android app crashing when saving user notification settings](https://github.com/mattermost/mattermost-mobile/pull/364)
 - [Fix recent mentions search not working](https://github.com/mattermost/platform/pull/5878)

Core committers who review the PR are entitled to reject the PR if it significantly changes behavior or user expectations, which [requires a Help Wanted issue opened by the core team](http://docs.mattermost.com/process/help-wanted.html) so that the change can be tested, documented and supported.

The best way to discuss opening a Help Wanted ticket with the core team is by [starting a conversation in the feature idea forum](https://www.mattermost.org/feature-ideas/).

## Install Mattermost and set up a Fork

Once you have a ticket: 

1. Follow the [developer setup instructions](http://docs.mattermost.com/developer/developer-setup.html) to install Mattermost.

2. Create a branch with `<branch name>` set to the ID of the ticket you're working on, for example `PLT-394`, using the command: `git checkout -b <branch name>`

3. Take a look at the [developer flow](https://docs.mattermost.com/developer/developer-flow.html) to learn how to work with the Mattermost codebase.

## Preparing a Pull Request 

Before submitting a pull request (PR), check that:  

1. You’ve signed the [Contributor License Agreement](http://www.mattermost.org/mattermost-contributor-agreement/), so you can be added to the Mattermost [Approved Contributor List](https://docs.google.com/spreadsheets/d/1NTCeG-iL_VS9bFqtmHSfwETo5f-8MQ7oMDE5IUYJi_Y/pubhtml?gid=0&single=true).  
2. Your change has a [Help Wanted ticket](http://docs.mattermost.com/process/help-wanted.html)
3. Your code follows the [Mattermost Style Guide](http://docs.mattermost.com/developer/style-guide.html).  
4. Unit tests are included for new server side functionality. 
5. Strings in user interface are included in [.../i18n/en.json](https://github.com/mattermost/platform/blob/master/i18n/en.json) and [.../webapp/i18n/en.json](https://github.com/mattermost/platform/tree/master/webapp/i18n/en.json) localization files. Files for other languages will automatically be updated through the [Mattermost Translation Server](http://translate.mattermost.com) and do not need to be included in the pull request.
6. Change meets UX Guidelines of [Fast, Obvious, Forgiving](http://www.mattermost.org/design-principles/).
7. If change requires user to understand a new concept or make a decision, PR for help documentation is submitted to [mattermost/docs](https://github.com/mattermost/docs).
8. Change is thoroughly tested. If your change involves text processing, make sure to at least run markdown loadtests in [`/tests`](https://github.com/mattermost/platform/tree/master/tests) before submitting the PR. To run the loadtests:
    - Go to **System Console** > **Developer** and set **Enable Testing Commands** to true
    - Run `/test url test-markdown-basics.md` and follow the instructions
    - Run `/test url test-markdown-lists.md` and follow the instructions
    - Run `/test url test-tables.md` and follow the instructions
9. Confirm you have [squashed your commits](http://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#Squashing-Commits).

## Submitting a Pull Request 

When submitting a PR, check that:  

1. PR is submitted against `master`
2. PR title begins with the Jira Ticket ID (eg `PLT-394:`, [see examples](https://github.com/mattermost/platform/pulls?q=is%3Apr+is%3Aclosed))
3. PR comment describes the changes and how the feature is supposed to work

## Managing an Open Pull Request 

After submitting a PR, before it is merged:  

1. Automated build process must pass  
    - If the build fails, check the error log to narrow down the reason. 
    - Sometimes one of the multiple build tests will randomly fail due to issues in Travis CI. If you see just one build failure and no clear error message, it may be a random issue. Add a comment so the reviewer for your change can re-run the build for you, or close the PR and re-submit and that typically clears the issue. 
2. PM review must pass
    - A Product Manager will review the pull request to make sure it:
        - Fits with our product roadmap
        - Works as expected
        - Meets [UX guidelines](https://docs.mattermost.com/developer/fx-guidelines.html)
    - The Product Manager may come back with some bugs or UI improvements to fix before the pull request moves on to dev review.
3. CSS review must pass
    - Any pull request containing CSS changes should be reviewed by the UX and HTML/CSS dev.
4. Dev review must pass
    - Two core committers will review the pull request and either give feedback or approve the PR.
    - Any comments will need to be addressed before the pull request is ready to merge.

If you've included your mailing address in the signed [Contributor License Agreement](https://www.mattermost.org/mattermost-contributor-agreement/), you may receive a [Limited Edition Mattermost Mug](https://forum.mattermost.org/t/limited-edition-mattermost-mugs/143) as a thank you gift after your first pull request is merged. 

### Core Committers

Core committers on Mattermost repositories consist of vetted core team members, including both community contributors as well as staff from Mattermost, Inc., who are trusted to review and merge PRs.

Repository: https://github.com/mattermost/platform

- **Core committers include**: coreyhulen, crspeller, csduarte, enahum, grundleborg, hmhealey, jwilander

- **Product managers include**: asaadmahmood, esethna, it33, jasonblais, lfbrock

