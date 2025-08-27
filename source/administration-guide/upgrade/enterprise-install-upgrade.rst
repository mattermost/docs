Upgrade Team Edition to Enterprise Edition
=============================================

If you're evaluating Mattermost using Team Edition, you'll need to upgrade to Mattermost Enterprise Edition before you can start a trial or upload a license that enables Enterprise features. The open source Mattermost Team Edition is functionally identical to the commercial Enterprise Edition, but there is no ability to start a trial or unlock paid features.

Upgrade to Enterprise Edition
-------------------------------

Check your edition and version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open **Product menu > About Mattermost** to check your edition and version from the web or desktop interface.

- **Mattermost Enterprise Edition** indicates you can apply a license key to enable Enterprise features.
- **Mattermost Team Edition** indicates you're using the open source version and need to upgrade before a license key can be applied.

Upgrade via System Console (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most standalone servers can upgrade Team Edition to Enterprise Edition in minutes using the built-in conversion tool in the System Console, and this is our recommended approach.

Go to **Product menu > System Console > Edition and License** and select **Upgrade to Enterprise Edition**.

During the upgrade process, the Mattermost Enterprise Edition binary file that matches your current server version is downloaded, decompressed, and extracted. The Team Edition binary is then replaced by the Enterprise Edition version. 

.. note::
  If you're using a modified version of Mattermost, using this tool will overwrite your changes and replace them with the official Enterprise Edition binary. 

Once this process is complete, you're prompted to restart your server. The Mattermost version listed in **Product menu > System Console > Edition and License** will change from **Team Edition** to **Enterprise Edition**, and you can now start a trial or upload a license to unlock paid features.

Upgrade manually
~~~~~~~~~~~~~~~~~

You can alternatively replace the Mattermost Team Edition binary with a Mattermost Enterprise Edition binary when running a regularly scheduled server upgrade via this :doc:`upgrade procedure </administration-guide/upgrade/upgrading-mattermost-server>`.

We recommend backing up Mattermost prior to upgrading. The :doc:`migration guide </administration-guide/onboard/migrating-to-mattermost>` documentation outlines the process required to back up and restore your database.

Upgrade to Enterprise Edition in GitLab Omnibus
-------------------------------------------------

.. warning::

  GitLab Omnibus support is deprecated as of Mattermost server v11.0.0. The last ``mattermost-omnibus`` release is v10.12. System administrators should plan to migrate to alternative deployment methods when upgrading beyond Mattermost v10.12. See the :doc:`deployment guide </deployment-guide/server/server-deployment-planning>` for recommended alternatives.

GitLab Omnibus runs the open source Mattermost Team Edition. To upgrade to Mattermost Enterprise Edition, follow these steps:

1. Disable the built-in Mattermost instance on GitLab Omnibus by going to ``/etc/gitlab/gitlab.rb`` and setting the following line to ``false``:

  .. code-block:: text

    mattermost['enable'] = false

  Then run the following command to apply the updated setting:

  .. code-block::

    sudo gitlab-ctl reconfigure

2. Install Mattermost using one of the guides above.
3. Migrate the database used by GitLab Mattermost for your new Enterprise Edition instance.
4. (Optional) Set up `GitLab slash command integration <https://docs.gitlab.com/ee/user/project/integrations/mattermost_slash_commands.html>`_ with your Mattermost instance.

Troubleshooting
---------------

Permissions and limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're using a package manager, such as Gitlab Omnibus, to manage your Mattermost installation, the Mattermost system user won't have sufficient permissions to perform the upgrade. If this is the case, you'll need to change the file permissions manually.

Changing the permissions in this way doesn't affect your Mattermost deployment or impact any data. The permission change is done solely for the upgrade.

To change the permissions using the command line on the Mattermost server, you need access to the command line tool as *mattermost* user:

1. Open the command line tool on the Mattermost server and ``cd`` to the Mattermost installation directory. 
2. Run the following commands, replacing ``<PathToBinaryFile>`` with the appropriate path - typically ``/opt/mattermost/bin/mattermost``) to change the ownership of the binary file to *mattermost* user and grant write access:

  .. code-block:: sh

    chown mattermost <PathToBinaryFile>
    chmod +w <PathToBinaryFile>

3. In the Mattermost System Console, retry the upgrade. 
4. When the upgrade is complete, return to the command prompt on the Mattermost server and run the following command to restore the file permissions, replacing ``<OriginalFileOwner>`` with the appropriate value:

  .. code-block:: sh

    chown <OriginalFileOwner> <PathToBinaryFile>
    chmod -w <PathToBinaryFile>

Mattermost has reverted to Team Edition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On a managed deployment, if you upgraded Team Edition to Enterprise Edition, and then upgraded again, the upgrade will have overwritten Enterprise Edition with the latest version of Team Edition.

You can convert to Enterprise Edition again by following the steps above. If you plan to use Mattermost Enterprise Edition permanently, we recommend migrating your server to a self-hosted deployment.

Incompatible system architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This System Console tool is only compatible with Linux systems using x86-64 architecture. If you're running Mattermost on a different architecture, follow the `manual upgrade process <#upgrade-manually>`__ instead.

Can't retrieve Enterprise Edition binary file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the upgrade fails due to file retrieval failure, unavailable binary, or connectivity error, please check your proxy settings and try again. If the problem persists, follow the `manual upgrade process <#upgrade-manually>`__ instead.
