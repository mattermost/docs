GitLab Process
============================

This document outlines the processes for supporting the Mattermost package in GitLab Omnibus.

.. contents::
    :backlinks: top

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
7. Once the MR is merged and included in an RC, `test upgrade following these steps <https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg>`_.

Testing
----------------

The following steps are taken to test the Mattermost package in GitLab Omnibus:

1. Each Mattermost version is tested on a GitLab Omnibus build at `http://ci-linux-gitlab-omnibus.mattermost.com/ <http://ci-linux-gitlab-omnibus.mattermost.com/>`_. Testing covers all core Mattermost features, including notifications and GitLab SSO.
2. Before each merge request to GitLab Omnibus, upgrade is tested `following these steps <https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg>`_, using the `nightly Omnibus packages <https://packages.gitlab.com/gitlab/nightly-builds>`_ to validate the integration. This is so the packaging code and OAuth setup can be tested as well, which has historically been the main source of issues. Other test areas include:

 - Pre-provisioning OAuth configuration automatically on the Omnibus package
 - Mattermost ChatOps slash command integration
 - OAuth team creation option in GitLab Omnibus

Communication
-------------------

Changes and features affecting GitLab Omnibus are communicated via `GitLab issues <https://gitlab.com/gitlab-org/gitlab-ce/issues>`_ and `GitLab Slack channel <https://gitlab.slack.com>`_.

Moreover, a recurring monthly meeting between a product manager at GitLab and Mattermost is organized to cover

 - concerns/issues from GitLab Omnibus team,
 - new upcoming changes or features in Mattermost affecting GitLab Omnibus, and
 - other miscellaneous queued items.

Optionally, an engineer from both GitLab and Mattermost teams also joins the recurring monthly meeting.

Service-Level Agreement (SLA)
-------------------------------

This process is still a work-in-progress, being developed together with GitLab.

GitLab Premier Support Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitLab has a `4-hour support window for their premier support customers <https://about.gitlab.com/features/premium-support/>`_. Mattermost is setting up a process to meet those requirements for relevant questions raised by the GitLab premier support customers.

GitLab is also working with their legal team to understand the process for sharing any sensitive customer information (e.g. logs) with Mattermost.

More details to be added.

GitLab Non-Premier Support Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost has created a `mattermost-support` account in GitLab for support issues. The plan is for Mattermost to

 - integrate GitLab issue reviews as part of existing forum issue monitoring processes,
 - aim to answer within one business day, or at best effort, and
 - subscribe to email alerts sent automatically when a `Mattermost` label is added to an issue, or when the `mattermost-support` account is assigned to a GitLab issue.
 
usiness day coverage should be more than enough.

Templates
--------------

GitLab announcement proposal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

  Proposed update for new version of [Mattermost](https://gitlab.com/gitlab-org/omnibus-gitlab/issues/1241).

  ## GitLab Mattermost 2.2

  [Mattermost 2.2](http://www.mattermost.org/mattermost-2-2-threaded-messages-and-more/) ships in GitLab 8.7 with threaded messages, French translation, new themes, new Trello and IRC support, plus many more new benefits.

  This version also includes [security updates](http://about.mattermost.com/security-updates/) and upgrade from earlier versions is recommended.

GitLab forum responses
~~~~~~~~~~~~~~~~~~~~~~~

See `sample forum responses listed here <https://docs.mattermost.com/process/community-guidelines.html#sample-responses>`_.

Upcoming Work
---------------

1. Environment variables support for `config.json` settings. - **Due: Mattermost v4.10 / GitLab v11.0**

 - `Disable Mattermost System Console settings that are configured via environment variables <https://mattermost.atlassian.net/browse/MM-9849>`_.
 - `Investigate what config.json-only settings need to be added to the Mattermost System Console <https://mattermost.atlassian.net/browse/MM-9850>`_.
 - `Update documentation <https://gitlab.com/gitlab-org/omnibus-gitlab/issues/3284>`_ and fully test the migration.

2. `Add timezones.json to GitLab Omnibus build <https://mattermost.atlassian.net/browse/MM-9873>`_ to support new Timezone user setting. - **Due: Mattermost v4.10 / GitLab v11.0**

3. `Add a config.json setting to disable the permanent API v4 delete team parameter <https://mattermost.atlassian.net/browse/MM-9916>`_. This allows Mattermost to disable the parameter without any changes to GitLab Omnibus. - **Due: Mattermost v5.0 / GitLab v11.1**

4. `Migrate Mattermost slash command integration in GitLab to Mattermost API v4 <https://gitlab.com/gitlab-org/gitlab-ce/issues/41631>`_. - **Due: Mattermost v5.0 / GitLab v11.1**

5. Releasing an extended support release (ESR) version of Mattermost, and shipping it in GitLab Omnibus. `A discussion is open in the Mattermost forums <https://forum.mattermost.org/t/extended-support-release-discussion/4598>`_. - **Due: TBD**

6. Bundling Mattermost Enterprise Edition in GitLab EE. `A discussion is open in GitLab repository <https://gitlab.com/gitlab-org/omnibus-gitlab/issues/1609>`_. - **Due: TBD**
