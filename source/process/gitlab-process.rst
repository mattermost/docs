GitLab Process
============================

This document outlines the processes for supporting the Mattermost package in GitLab Omnibus.

Merge Requests
-----------------

To submit a merge request (MR) to GitLab for taking the next Mattermost version, follow these steps. The MR must be merged by the 7th of the month to be included in a GitLab release.

1. Download the latest Team Edition release from `the download page <https://about.mattermost.com/download>`_.
2. Test the Mattermost version locally with GitLab Omnibus `following these steps <https://docs.mattermost.com/developer/developer-flow.html#testing-with-gitlab-omnibus>`_.
3. Once tested and all issues are resolved, submit an MR to the `master branch <https://gitlab.com/gitlab-org/omnibus-gitlab>`_. Include the following:

    - Changes to Mattermost version number (`default_version <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/config/software/mattermost.rb#L20>`_) and md5 sum of the final TE build (`source md5 <https://gitlab.com/jasonblais/omnibus-gitlab/blob/master/config/software/mattermost.rb#L23>`_) in  `config/software/mattermost.rb <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/config/software/mattermost.rb>`_
    - Update to the `GitLab changelog <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/CHANGELOG.md>`_
    - Config.json updates to `gitlab.rb <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/files/gitlab-config-template/gitlab.rb.template>`_, `attributes default.rb <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/files/gitlab-cookbooks/mattermost/attributes/default.rb>`_ and `config.json.erb <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/files/gitlab-cookbooks/mattermost/templates/default/config.json.erb>`_ with new TE config settings (`see example <https://gitlab.com/gitlab-org/omnibus-gitlab/merge_requests/1855>`_)
    - Update to `GitLab Mattermost documentation <https://docs.gitlab.com/omnibus/gitlab-mattermost/README.html>`_
    - Summary of updates in Team Edition that are relevant to GitLab

4. If the release contains a security update, email @marin and @briann in GitLab with a link to the MR, and all subsequent backports.
5. Post a link to the MR in the Release Discussion channel.
6. Check daily for updates until the MR is merged, ensuring it gets merged by the 7th of the month.
7. Once the MR is merged and included in an RC, `test upgrade following these steps <https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg>`_

Testing
--------

The following steps are taken to test the Mattermost package in GitLab Omnibus:

1. Each Mattermost version is tested on a GitLab Omnibus build at `http://ci-linux-gitlab-omnibus.mattermost.com/ <http://ci-linux-gitlab-omnibus.mattermost.com/>`_. Testing covers all core Mattermost features.
2. Before each merge request to GitLab Omnibus, // XXX add areas mentioned by Josh (slash commands, creating a Mattermost group), GitLab SSO
3. After each merge request, upgrade is tested `following these steps <https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg>`_



## Templates

Templates for GitLab announcement proposal
```
Proposed update for new version of [Mattermost](https://gitlab.com/gitlab-org/omnibus-gitlab/issues/1241).

## GitLab Mattermost 2.2

[Mattermost 2.2](http://www.mattermost.org/mattermost-2-2-threaded-messages-and-more/) ships in GitLab 8.7 with threaded messages, French translation, new themes, new Trello and IRC support, plus many more new benefits.

This version also includes [security updates](http://about.mattermost.com/security-updates/) and upgrade from earlier versions is recommended.
```


SLA

Communication
---------------

Changes and features affecting GitLab Omnibus are communicated via `GitLab issues <https://gitlab.com/gitlab-org/gitlab-ce/issues>`_ and `GitLab Slack channel <https://gitlab.slack.com>`.

Moreover, a recurring monthly meeting between a product manager at GitLab and Mattermost is organized to cover

concerns/issues from GitLab Omnibus team
- new upcoming changes or features in Mattermost affecting GitLab Omnibus
- other miscellaneous queued items

The original proposed API change for the delete team API endpoint wasn’t communicated properly, resulting in confusion on both sides. We could have also done a better job communicating environment variables.

One quick way to keep GitLab and Mattermost teams in sync is to have a 20-minute call once or twice a month. We can start small with, perhaps Marin on the call with two of our engineers. The meeting agenda could follow something like:


concerns/issues from GitLab Omnibus team
new upcoming changes or features in Mattermost affecting GitLab Omnibus
other miscellaneous queued items

https://gitlab.slack.com
monthyl meeting


Upcoming work
