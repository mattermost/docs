GitLab Process
============================

This document outlines the processes for supporting the Mattermost package in GitLab Omnibus.

.. contents::
    :backlinks: top

Merge Requests
-----------------

To submit a merge request (MR) to GitLab for taking the next Mattermost version, follow these steps. The MR must be merged by the 7th of the month to be included in a GitLab release.

1. Check out the latest version of GitLab Omnibus and make a branch with the following changes:

    - Changes to Mattermost version number (`default_version <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/config/software/mattermost.rb#L20>`_) and md5 sum of the final TE build (`source md5 <https://gitlab.com/jasonblais/omnibus-gitlab/blob/master/config/software/mattermost.rb#L23>`_) in  `config/software/mattermost.rb <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/config/software/mattermost.rb>`_
    - Update to the `GitLab changelog <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/CHANGELOG.md>`_
    - Config.json updates to `gitlab.rb <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/files/gitlab-config-template/gitlab.rb.template>`_, `attributes default.rb <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/files/gitlab-cookbooks/mattermost/attributes/default.rb>`_ and `config.json.erb <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/files/gitlab-cookbooks/mattermost/templates/default/config.json.erb>`_ with new TE config settings (`see example <https://gitlab.com/gitlab-org/omnibus-gitlab/merge_requests/1855>`_)
    - Update to `GitLab Mattermost documentation <https://docs.gitlab.com/omnibus/gitlab-mattermost/README.html>`_

2. Build GitLab and test it locally `following these steps <https://docs.mattermost.com/developer/developer-flow.html#testing-with-gitlab-omnibus>`_.
3. Submit a MR to the `master branch of Gitlab <https://gitlab.com/gitlab-org/omnibus-gitlab>`_, including a summary of updates in Team Edition that are relevant to GitLab
4. Post a link to the MR in the Release Discussion channel.
5. Check daily for updates until the MR is merged, ensuring it gets merged by the 7th of the month.
6. Once the MR is merged and included in an RC, `test upgrade following these steps <https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg>`_.

If the release contains a security update, PM owner emails @marin and @briann in GitLab with a link to the MR, and all subsequent backports.

Testing
----------------

The following steps are taken to test the Mattermost package in GitLab Omnibus:

1. Each Mattermost version is tested on a GitLab Omnibus build at `http://ci-linux-gitlab-omnibus.mattermost.com/ <http://ci-linux-gitlab-omnibus.mattermost.com/>`_. Testing covers all core Mattermost features, including notifications and GitLab SSO.
2. Before each merge request to GitLab Omnibus, upgrade is tested `following these steps <https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg>`_, using the `nightly Omnibus packages <https://packages.gitlab.com/gitlab/nightly-builds>`_ to validate the integration. This is so the packaging code and OAuth setup can be tested as well, which has historically been the main source of issues. Other test areas include:

 - Pre-provisioning OAuth configuration automatically on the Omnibus package
 - Mattermost ChatOps slash command integration
 - OAuth team creation option in GitLab Omnibus

Service-Level Agreement (SLA)
-------------------------------

Mattermost has created a ``mattermost-support`` account in GitLab for support issues, and has subscribed to the ``mattermost`` label in the following projects:

 - `omnibus-gitlab <https://gitlab.com/gitlab-org/omnibus-gitlab>`_
 - `gitlab-ce <https://gitlab.com/gitlab-org/gitlab-ce>`_
 - `gitlab-ee <https://gitlab.com/gitlab-org/gitlab-ee>`_

When a `mattermost` label is applied, an email notification is sent to the technical support team who answers the question within two business days using the ``mattermost-support`` account.

GitLab Premier Support Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitLab has a `4-hour support window for their premier support customers <https://about.gitlab.com/features/premium-support/>`_ and Mattermost has set up a process to support this window.

When a premier support issue requires escalation to the Mattermost support team, GitLab assigns the issue to the ``mattermost-support`` account. This assignment sends an email notification, which is automatically escalated to the critical level technical support who answers the question within 4 hours using the ``mattermost-support`` account.

Monthly Meetings
-------------------

Changes and features affecting GitLab Omnibus are communicated via `GitLab issues <https://gitlab.com/gitlab-org/gitlab-ce/issues>`_ and `GitLab Slack channel <https://gitlab.slack.com>`_.

Moreover, a recurring monthly meeting between a product manager at GitLab and Mattermost is organized to cover

 - concerns/issues from GitLab Omnibus team,
 - new upcoming changes or features in Mattermost affecting GitLab Omnibus, and
 - other miscellaneous queued items.

Optionally, an engineer from both GitLab and Mattermost teams also joins the meeting.

Upcoming Work
---------------

1. Environment variables support for `config.json` settings. - **Due: Mattermost v4.10 / GitLab v11.0**

 - `Disable Mattermost System Console settings that are configured via environment variables <https://mattermost.atlassian.net/browse/MM-9849>`_.
 - `Investigate what config.json-only settings need to be added to the Mattermost System Console <https://mattermost.atlassian.net/browse/MM-9850>`_.
 - `Support environment variable configuration options even if there's no entry for it in config.json <https://mattermost.atlassian.net/browse/MM-8400>`_.
 - `Update documentation <https://gitlab.com/gitlab-org/omnibus-gitlab/issues/3284>`_ and fully test the migration.

2. `Add a config.json setting to disable the permanent API v4 delete team parameter <https://mattermost.atlassian.net/browse/MM-9916>`_. This allows Mattermost to disable the parameter without any changes to GitLab Omnibus. - **Due: Mattermost v5.0 / GitLab v11.1**

3. `Migrate Mattermost slash command integration in GitLab to Mattermost API v4 <https://gitlab.com/gitlab-org/gitlab-ce/issues/41631>`_. - **Due: Mattermost v5.0 / GitLab v11.1**

4. Releasing an extended support release (ESR) version of Mattermost and shipping it in GitLab Omnibus. `A discussion is open in the Mattermost forums <https://forum.mattermost.org/t/extended-support-release-discussion/4598>`_. - **Due: TBD**

5. Bundling Mattermost Enterprise Edition in GitLab EE. `A discussion is open in GitLab repository <https://gitlab.com/gitlab-org/omnibus-gitlab/issues/1609>`_. - **Due: TBD**


Templates
--------------

GitLab announcement proposal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

  Proposed update for new version of [Mattermost](https://gitlab.com/gitlab-org/omnibus-gitlab/issues/1241).

  ### GitLab Mattermost 4.7

  GitLab 10.6 includes [Mattermost 4.7](https://about.mattermost.com/releases/mattermost-4-7/), an [open source Slack-alternative](https://about.mattermost.com/) whose newest release includes enhanced image preview and thumbnails, faster load times, upgraded desktop app, plus much more.

  This version also includes [security updates](https://about.mattermost.com/security-updates/) and upgrading is recommended.

GitLab forum responses
~~~~~~~~~~~~~~~~~~~~~~~

See `sample forum responses listed here <https://docs.mattermost.com/process/community-guidelines.html#sample-responses>`_.
