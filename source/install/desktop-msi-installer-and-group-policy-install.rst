.. _desktop-msi-gpo:

Desktop MSI installer and group policy installation guides (beta) 
==================================================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This guide provides steps to install the MSI and use Group Policies in Windows Professional or Enterprise. The MSI installer package can be downloaded `here <https://github.com/mattermost/desktop/releases/tag/v5.0.3>`_. 

.. note::
    The Mattermost MSI installer and Group Policy (GPO) definitions are in Beta. If you are using this installer or GPOs and have feedback, particularly if you are an organization executing remote deployments, please contact us in the `MSI Installer channel on our Community server <https://community.mattermost.com/core/channels/msi-installer>`_ or on our `community forum <https://forum.mattermost.com/>`_. We hope to promote this installer out of Beta when the known issues are addressed and we are confident that the various deployment scenarios expected in production environments are tested sufficiently with the help of organizations using this Beta. Feedback is highly appreciated.

.. contents::
    :backlinks: top

Installation guide
-------------------

Download group policy and MSI installer files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Using a newly created Windows VM or dedicated Windows computer, make sure to use a Windows version that supports ``Edit group policy`` out of the box (i.e. Windows 10 Pro or Enterprise).

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00001.png

2. Navigate to the `Mattermost Desktop <https://github.com/mattermost/desktop>`__ repo on `Github.com <https://github.com/>`__.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00002.png

3. Navigate to the release page for `version v5.0.4 <https://github.com/mattermost/desktop/releases/tag/v5.0.4>`__ and download the appropriate installer for your version of Windows (32-bit vs. 64-bit).

4. Download the `source.zip <https://github.com/mattermost/desktop/archive/v5.0.4.zip>`__ file as well to extract group policy files.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00003.png

Installing group policy files locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Browse to the folder the above files were downloaded to and unzip the ``desktop-5.0.4.zip`` file in place.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00004.png

2. Navigate to the unzipped ``desktop-5.0.4\resources\windows\gpo`` folder and copy the contents.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00005.png

3. Navigate to the ``C:\Windows\PolicyDefinitions`` folder and paste the files copied in the last step. 

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00006.png

4. Verify the ``mattermost.admx`` file is in the ``C:\Windows\PolicyDefinitions`` folder.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00007.png

5. Verify the ``mattermost.adml`` file is in the ``C:\Windows\PolicyDefinitions\en-US`` folder.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00008.png

.. notes::

   * ``\\FQDNDomain\sysvol\FQDNDomain\Policies\PolicyDefinitions`` can be used instead of ``C:\Windows\PolicyDefinitions`` if available.
   * ``\\FQDNDomain\sysvol\FQDNDomain\Policies\PolicyDefinitions\en-US`` can be used instead of ``C:\Windows\PolicyDefinitions\en-US`` if available.

Configure Mattermost using group policy settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Run the ``Edit group policy`` application by selecting ``Start``, typing ``gpedit`` into the search field, then selecting the resulting ``Edit group policy`` search option.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00009.png

2. In the ``Edit group policy`` window, navigate to ``Local Computer Policy\Computer Configuration\Administrative Templates\Mattermost``. In this example, double-click on ``DefaultServerList`` to set one or more default servers that will appear on app launch. 

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00010.png

3. In the resulting window for ``DefaultServerList``, select **Enabled** to turn the feature on, then select the **Show…** button in the **Options:** section of the window to add default servers.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00011.png

4. In the resulting window, add desired Mattermost servers using a memorable name (i.e., Community) and the web URL of the Mattermost server (i.e., https://community.mattermost.com).

5. Select **OK** twice, then close the **Edit group policy** app.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00012.png

Verify group policy settings have been applied
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open up the ``Registry Editor`` by selecting **Start**, typing ``Registry Editor`` in the search field, then selecting the **Registry Editor** option in the search results.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00013.png

2. In the **Registry Editor** window, navigate to ``Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Mattermost\DefaultServerList`` and verify the servers you added using the **Edit group policy** app are listed.

3. Once verified, close the **Registry Editor**.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00014.png

Install the Mattermost Desktop App using the MSI installer:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Within the folder the MSI installer was downloaded to, double-click on the MSI installer to begin the Mattermost Desktop installation process.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00015.png

2. Installation of the MSI requires admin permission, so accept the resulting request to allow the installer to make changes to your device.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00016.png

3. Select ``Finish`` when the installation is complete.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00017.png

Verify group policy settings in the installed Desktop App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Launch the newly installed Mattermost app from the **Start** menu.

2. Verify the app loads the first server you defined in the **Edit group policy** app.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00018.png

Silent installation guide
-------------------------

Perform a silent installation of MSI by running the following command:

``msiexec /i mattermost-desktop-v5.0.4-x64.msi /qn``

.. note::
   Current version is 5.0.4. In the future, you may need to change this command accordingly.
