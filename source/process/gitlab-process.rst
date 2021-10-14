GitLab Process
============================

This document outlines the processes for supporting the Mattermost package in GitLab Omnibus.

.. contents::
    :backlinks: top

Merge Requests
-----------------

To submit a merge request (MR) to GitLab for taking the next Mattermost version, follow these steps. The MR must be merged by the 7th of the month to be included in a GitLab release.

1. Check out the latest version of GitLab Omnibus and make a branch with the following changes:

    - Changes to Mattermost version number (`default_version <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/config/software/mattermost.rb#L20>`__) and md5 sum of the final TE build (`source md5 <https://gitlab.com/jasonblais/omnibus-gitlab/blob/master/config/software/mattermost.rb#L23>`__) in  `config/software/mattermost.rb <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/config/software/mattermost.rb>`__
    - Update to the `GitLab changelog <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/CHANGELOG.md>`__ by using ``/scripts/changelog`` script to create a changelog entry
    - Config.json updates to `gitlab.rb <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/files/gitlab-config-template/gitlab.rb.template>`__, `attributes default.rb <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/files/gitlab-cookbooks/mattermost/attributes/default.rb>`__ and `config.json.erb <https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/files/gitlab-cookbooks/mattermost/templates/default/config.json.erb>`__ with new TE config settings (`see example <https://gitlab.com/gitlab-org/omnibus-gitlab/merge_requests/1855>`__)
    - Update to `GitLab Mattermost documentation <https://docs.gitlab.com/omnibus/gitlab-mattermost/README.html>`__

2. Build GitLab and test it locally `following these steps <https://docs.mattermost.com/developer/developer-flow.html#testing-with-gitlab-omnibus>`__.
3. Submit a MR to the `master branch of Gitlab <https://gitlab.com/gitlab-org/omnibus-gitlab>`__, including a summary of updates in Team Edition that are relevant to GitLab
4. Post a link to the MR in the Release Discussion channel.
5. Check daily for updates until the MR is merged, ensuring it gets merged by the 7th of the month.
6. Once the MR is merged and included in an RC, `test upgrade following these steps <https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg>`__.

If the release contains a security update, PM owner emails @marin and @briann in GitLab with a link to the MR, and all subsequent backports.

Testing
----------------

The following steps are taken to test the Mattermost package before each merge request to GitLab Omnibus:

1. Pull the latest master build of GitLab Omnibus, using the `nightly Omnibus packages <https://packages.gitlab.com/gitlab/nightly-builds>`_.
2. Update ``default_version`` and ``md5`` variables for the new Mattermost version in `config/softwater/mattermost.rb`.

.. code-block:: none

  name 'mattermost'
  default_version '5.19.0-rc2'

  source url: "https://releases.mattermost.com/#{version}/mattermost-team-#{version}-linux-amd64.tar.gz",
  md5: 'fe49d764324334480b296fc6c500b706'

3. Update the list of Mattermost versions associated with each GitLab release `in the GitLab documentation <https://docs.gitlab.com/omnibus/gitlab-mattermost/#upgrading-gitlab-mattermost>`_, and add a changelog entry.
4. Build GitLab Omnibus `using these instructions <https://gist.github.com/hmhealey/b6d3e42a88563ca43f03152e8b86592b#gitlab-omnibus>`_.
5. Install the generated ``.deb`` file on a local test server.

The Mattermost team then tests the upgrade process and validates the packaging code and OAuth setup which have historically been the main source of issues. Other test areas include:

- Pre-provisioning OAuth configuration automatically on the Omnibus package.
- Mattermost ChatOps slash command integration.
- OAuth team creation option in GitLab Omnibus.

Upgrade Process
~~~~~~~~~~~~~~~~~~

Follow these steps to test the upgrade process for Mattermost in GitLab Omnibus.

The current test servers are located at:

 - `http://gitlab-rc-testing.spinmint.com <http://gitlab-rc-testing.spinmint.com>`__ - The GitLab instance itself
 - `http://gitlab-rc-testing2.spinmint.com <http://gitlab-rc-testing2.spinmint.com>`__ - GitLab Mattermost

The root admin account for them has username `root` and password `Password1`.

1. Connect to the previously configured instance using the key you used to set it up. The host name is ``ubuntu@gitlab-rc-testing.spinmint.com``.
2. Make sure your package manager is configured to allow for Gitlab RCs:

 - Go to `https://packages.gitlab.com/gitlab/unstable <https://packages.gitlab.com/gitlab/unstable>`__.
 - Click on the newest release candidate that’s marked CE and is for Ubuntu/Trusty.
 - Run the first command listed on that page on your server. It looks something like:

   .. code-block:: text

     curl -s https://packages.gitlab.com/install/repositories/gitlab/unstable/script.deb.sh | sudo bash

3. Update the package manager

  .. code-block:: text

    sudo apt-get update

4. Update GitLab by running the second command listed on the page you opened on step 2. It looks something like:

   .. code-block:: text

     sudo apt-get install gitlab-ce=8.10.0-rc13.ce.0

5. Reconfigure GitLab:

  .. code-block:: text

   sudo gitlab-ctl reconfigure

6. Restart GitLab:

  .. code-block:: text

   sudo gitlab-ctl restart

7. To confirm the upgrade was successful:

 - Go to `http://gitlab-rc-testing2.spinmint.com  <http://gitlab-rc-testing2.spinmint.com >`__.
 - Create an account and log in.
 - Confirm the correct version number in **Main Menu** > **About Mattermost**.

To help with debugging, including a list of useful commands, see the `support handbook <https://docs.mattermost.com/process/support.html#gitlab-issues>`_.

Service-Level Agreement (SLA)
-------------------------------

Mattermost has created a ``mattermost-support`` account in GitLab for support issues, and has subscribed to the ``mattermost`` label in the following projects:

 - `omnibus-gitlab <https://gitlab.com/gitlab-org/omnibus-gitlab>`__
 - `gitlab-ce <https://gitlab.com/gitlab-org/gitlab-ce>`__
 - `gitlab-ee <https://gitlab.com/gitlab-org/gitlab-ee>`__

When a `mattermost` label is applied, an email notification is sent to the technical support team who answers the question within two business days using the ``mattermost-support`` account.

GitLab Premier Support Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitLab has a `4-hour support window for their premier support customers <https://about.gitlab.com/features/premium-support/>`__ and Mattermost has set up a process to support this window.

When a premier support issue requires escalation to the Mattermost support team, GitLab assigns the issue to the ``mattermost-support`` account. This assignment sends an email notification, which is automatically escalated to the critical level technical support who answers the question within four hours using the ``mattermost-support`` account.

Monthly Meetings
-------------------

Changes and features affecting GitLab Omnibus are communicated via `GitLab issues <https://gitlab.com/gitlab-org/gitlab-ce/issues>`__ and `GitLab Slack channel <https://gitlab.slack.com>`__.

Moreover, a recurring monthly meeting between a product manager at GitLab and Mattermost is organized to cover

 - concerns/issues from GitLab Omnibus team,
 - new upcoming changes or features in Mattermost affecting GitLab Omnibus, and
 - other miscellaneous queued items.

Optionally, an engineer from both GitLab and Mattermost teams also joins the meeting.

Templates
--------------

GitLab announcement proposal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

  Proposed update for new version of [Mattermost](https://gitlab.com/gitlab-org/omnibus-gitlab/issues/1241).

  ### GitLab Mattermost 4.7

  GitLab 10.6 includes [Mattermost 4.7](https://about.mattermost.com/releases/mattermost-4-7/), an [open source Slack-alternative](https://about.mattermost.com/) whose newest release includes enhanced image preview and thumbnails, faster load times, upgraded desktop app, plus much more.

  This version also includes [security updates](https://mattermost.com/security-updates/) and upgrading is recommended.

GitLab forum responses
~~~~~~~~~~~~~~~~~~~~~~~

See `sample forum responses listed here <https://docs.mattermost.com/process/community-guidelines.html#sample-responses>`__.
