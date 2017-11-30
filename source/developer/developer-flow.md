Developer Flow
-----------------------------

If you haven't [set up your developer environment](https://docs.mattermost.com/developer/developer-setup.html), please do so before continuing with this section.

### Workflow ###

Here's a general workflow a Mattermost developer working on our [mattermost-server](https://github.com/mattermost/mattermost-server) and [mattermost-webapp](https://github.com/mattermost/mattermost-webapp) repositories follows:

1. Take a look at the [Repository structure](https://docs.mattermost.com/developer/developer-flow.html#repository-structure) to find out where to look for what you're working on.
2. On your fork, create a branch `PLT-####` where #### is the ticket number if it is a [Jira](https://mattermost.atlassian.net) ticket, or `GH-####` if it is a GitHub Issue without a Jira ticket.
3. Make the code changes required to complete your ticket, making sure to write or modify unit tests where appropriate.
4. To test your changes, run `make run` from the root directory of the server respository. This will start up the server and a watcher process that will build any changes to the client as you make them. To get changes to the webapp server it must be restarted with `make restart`. Your webapp server will be running at `http://localhost:8065`.
5. Once everything works to meet the ticket requirements, stop mattermost running `make stop` in the server repository and then run `make check-style` for check your syntax and `make test` for run the test in both repositories, server and webapp.
6. Commit your changes, push your branch and [create a pull request](https://docs.mattermost.com/developer/contribution-guide.html#preparing-a-pull-request).
7. Respond to feedback on your pull request and make changes as necessary by commiting to your branch and pushing it. You might need to [rebase your changes](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) if another pull request creates conflicts.
8. That's it! Rejoice that you've helped make Mattermost better.

### Useful server Makefile commands ###

Some other `make` commands that might be useful in addition to the ones mentioned above:

* `make run` will run only the server and not the client
* `make clean-docker` stops and removes your Docker images and is a good way to wipe your database
* `make clean` cleans your local environment of temporary files
* `make nuke` wipes your local environment back to a completely fresh start

### Useful webapp Makefile commands ###

* `make run-fullmap` will build the client with the full source map for easier debugging

### Running only specific server unit tests ###

Since running every single unit test takes a lot of time while making changes, you can run a subset of the serverside unit tests by using the following:
```
go test -v -run='<test name or regex>' ./<package containing test>
```
For example, if you wanted to run `TestPostUpdate` in `api/post_test.go`, you would run the following:
```
go test -v -run='TestPostUpdate' ./api
```

### Repository structure ###

For server work, you'll be working in the [server repository](https://github.com/mattermost/mattermost-server).
 * [./api/](https://github.com/mattermost/mattermost-server/tree/master/api) holds all API and application related code
 * [./model/](https://github.com/mattermost/mattermost-server/tree/master/model) holds all data model definitions and the Go driver
 * [./store/](https://github.com/mattermost/mattermost-server/tree/master/store) holds all database querying code
 * [./utils/](https://github.com/mattermost/mattermost-server/tree/master/utils) holds all utilities, such as the mail utility
 * [./i18n/](https://github.com/mattermost/mattermost-server/tree/master/i18n) holds all localization files for the server

For client work, you'll be working in the [webapp repository](https://github.com/mattermost/mattermost-webapp).
 * [./components/](https://github.com/mattermost/mattermost-webapp/tree/master/components) holds all the [React](https://facebook.github.io/react/) UI components and views
 * [./actions/](https://github.com/mattermost/mattermost-webapp/tree/master/actions) holds all [Flux actions](https://facebook.github.io/flux/docs/in-depth-overview.html#content) where the majority of the logic of the webapp takes place
 * [./stores/](https://github.com/mattermost/mattermost-webapp/tree/master/stores) holds the stores responsible for storing and providing the views with data
 * [./routes/](https://github.com/mattermost/mattermost-webapp/tree/master/routes) holds the definitions for all the [React-Router](https://github.com/ReactTraining/react-router) routes
 * [./i18n/](https://github.com/mattermost/mattermost-webapp/tree/master/i18n) holds the localization files for the client
 * [./utils/](https://github.com/mattermost/mattermost-webapp/tree/master/utils) holds all widely-used utilities
 * [./tests/](https://github.com/mattermost/mattermost-webapp/tree/master/tests) holds all the client unit tests

### Testing with GitLab Omnibus ###

To test a locally compiled version of Mattermost with GitLab Omnibus, replace the following GitLab files:
 * The compiled `platform` binary in `/opt/gitlab/embedded/bin/plattermost`
 * The assets (templates, i18n, fonts, webapp) in `/opt/gitlab/embedded/service/mattermost`
