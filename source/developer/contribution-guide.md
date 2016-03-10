# Code Contribution Guidelines

Thank you for your interest in contributing to Mattermost. Here's the process:  

## Choose a Ticket

1. Choose a ticket from the [Accepting Pull Requests](https://mattermost.atlassian.net/issues/?filter=10101) (APR Tickets) list
    - Choose any ticket marked "Open", even if it's assigned, and comment to let people know you're working on it. 
    - If you're looking for a quick ticket, pick something from the [Good First Contribution](https://mattermost.atlassian.net/issues/?filter=10206) list instead

2. If you have questions post in [Mattermost forum](http://forum.mattermost.org/) or join the [Mattermost core team discussion](https://pre-release.mattermost.com/signup_user_complete/?id=rcgiyftm7jyrxnma1osd8zswby) and post in the "APR Tickets" channel

It's okay to submit PRs to fix obvious bugs or add small improvements, but anything that significantly changes behavior or user expectations [requires an APR ticket opened by the core team](http://docs.mattermost.com/process/accepting-pull-request.html) so that the change can be tested, documented and supported. 

The best way to discuss opening an APR ticket with the core team is by [starting a conversation in the feature idea forum](http://www.mattermost.org/feature-requests/) which is monitored via automation.

## Install Mattermost and set up a Fork

Once you have a ticket: 

1. Follow [developer setup instructions](https://github.com/mattermost/platform/blob/master/doc/developer/Setup.md) to install Mattermost

2. Create a branch with `<branch name>` set to the ID of the ticket you're working on, for example `PLT-394`, using command: `git checkout -b <branch name>`

## Preparing a Pull Request 

Before submitting a pull request (PR), check that:  

1. You’ve signed the [Contributor License Agreement](http://www.mattermost.org/mattermost-contributor-agreement/), so you can be added to the Mattermost [Approved Contributor List](https://docs.google.com/spreadsheets/d/1NTCeG-iL_VS9bFqtmHSfwETo5f-8MQ7oMDE5IUYJi_Y/pubhtml?gid=0&single=true).  
2. Your change has an [APR Ticket](http://docs.mattermost.com/process/accepting-pull-request.html).
3. Your code follows the [Mattermost Style Guide](http://docs.mattermost.com/developer/style-guide.html).  
4. Unit tests are included for new server side functionality. 
5. Strings in user interface are included in localization files.
6. Change meets UX Guidelines of [Fast, Obvious, Forgiving](http://www.mattermost.org/design-principles/).
7. If change requires user to understand a new concept or make a decision, PR for help documentation is submitted to [mattermost/docs](https://github.com/mattermost/docs).
8. Change is thoroughly tested. If your change involves text processing, make sure to run tests in [`/tests`](https://github.com/mattermost/platform/tree/master/doc/developer/tests).
9. Confirm you have [squashed your commits](http://git-scm.com/book/en/v2/Git-Tools-Rewriting-History#Squashing-Commits).

## Submitting a Pull Request 

When submitting a PR, check that:  

1. PR is submitted against `master`  
2. PR title begins with the Jira Ticket ID (eg `PLT-394:`, [see examples](https://github.com/mattermost/platform/pulls?q=is%3Apr+is%3Aclosed))  
3. PR comment describes the changes and how the feature is supposed to work  

## Managing an Open Pull Request 

After submitting a PR, before it is merged:  

1. Automated build process must pass  
    - If the build fails, check the error log to narrow down the reason  
    - Sometimes one of the multiple build tests will randomly fail due to issues in Travis CI. If you see just one build failure and no clear error message, it may be a random issue. Add a comment so the reviewer for your change can re-run the build for you, or close the PR and re-submit and that typically clears the issue. 
2. Pull requests require review by an approved reviewer and an approved seconder.
3. Feedback from reviewers needs to be addressed 
3. If user interface changes do not match specification in Jira ticket, PM approval is needed.

If you've included your mailing address in Step 1, you may receive a [Limited Edition Mattermost Mug](https://forum.mattermost.org/t/limited-edition-mattermost-mugs/143) as a thank you gift after your first pull request is merged. 

### Approved Reviewers

_Please DO NOT @-mention reviewers if they haven't yet commented on your PR._
_Pull requests are reviewed in sequence._

**Approved reviewers include**: coreyhulen, crspeller, hmhealey, jwilander  
**Approved seconders include**: coreyhulen, crspeller, hmhealey, jwilander
