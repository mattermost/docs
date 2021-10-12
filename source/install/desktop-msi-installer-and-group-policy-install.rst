.. _desktop-msi-gpo:

Desktop MSI Installer and Group Policy Installation Guides (Beta) 
==================================================================

This guide provides steps to install the MSI and use Group Policies in Windows Pro or Enterprise. The MSI installer package can be downloaded `here <https://github.com/mattermost/desktop/releases/tag/5.0.0>`_. 

.. note::
    The Mattermost MSI installer and Group Policy (GPO) definitions are in Beta. If you are using this installer or GPOs and have feedback, particularly if you are an organization executing remote deployments, please contact us in the `MSI Installer channel on our Community server <https://community.mattermost.com/core/channels/msi-installer>`_ or on our `community forum <https://forum.mattermost.org/>`_. We hope to promote this installer out of Beta when the known issues are addressed and we are confident that the various deployment scenarios expected in production environments are tested sufficiently with the help of organizations using this Beta. Feedback is highly appreciated.

.. contents::
    :backlinks: top

Installation Guide
-------------------

Download Group Policy and MSI Installer files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Using a newly created Windows VM or dedicated Windows computer – make sure to use a Windows version that supports ``Edit group policy`` out of the box (i.e. Windows 10 Pro or Enterprise).

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00001.png

2. Navigate to the `Mattermost Desktop <https://github.com/mattermost/desktop>`__ repo on `Github.com <https://github.com/>`__.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00002.png

3. Navigate to the release page for `version v5.0.0 <https://github.com/mattermost/desktop/releases/tag/v5.0.0>`__ and download the appropriate installer for your version of Windows (32bit vs. 64bit).

4. Download the `source.zip <https://github.com/mattermost/desktop/archive/v5.0.0.zip>`__ file as well to extract group policy files.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00003.png

Installing Group Policy files locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Browse to the folder the above files were downloaded to and unzip the ``desktop-5.0.0.zip`` file in place.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00004.png

2. Navigate to the unzipped ``desktop-5.0.0\resources\windows\gpo`` folder and copy the contents.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00005.png

3. Navigate to the ``C:\Windows\PolicyDefinitions`` folder and paste the files copied in the last step. 

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00006.png

4. Verify the ``mattermost.admx`` file is in the ``C:\Windows\PolicyDefinitions`` folder.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00007.png

5. Verify the ``mattermost.adml`` file is in the ``C:\Windows\PolicyDefinitions\en-US`` folder.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00008.png

Notes:

* ``\\FQDNDomain\sysvol\FQDNDomain\Policies\PolicyDefinitions`` can be used instead of ``C:\Windows\PolicyDefinitions`` if available.
* ``\\FQDNDomain\sysvol\FQDNDomain\Policies\PolicyDefinitions\en-US`` can be used instead of ``C:\Windows\PolicyDefinitions\en-US`` if available.

Configure Mattermost using Group Policy settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Run the ``Edit group policy`` application by clicking ``Start``, typing ``gpedit`` into the search field and clicking on the resulting ``Edit group policy`` search option.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00009.png

2. In the ``Edit group policy`` window, navigate to ``Local Computer Policy\Computer Configuration\Administrative Templates\Mattermost``. A list of the available policies can be found `here <https://docs.mattermost.com/install/desktop.html#group-policies-gpo-and-msi-installer-support-alpha>`_. In this example, double click on ``DefaultServerList`` to set one or more default servers that will appear on app launch. 

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00010.png

3. In the resulting window for ``DefaultServerList``, click on ``Enabled`` to turn the feature on and then click on the ``Show…`` button in the ``Options:`` section of the window to add default servers.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00011.png

4. In the resulting window, add desired Mattermost servers using a memorable name (i.e. Community) and the web url of the Mattermost server (i.e. https://community.mattermost.com).

5. Click the ``OK`` button twice and close the ``Edit group policy`` application.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00012.png

Verify Group Policy settings have been applied
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. To verify the settings applied correctly, open up the ``Registry Editor`` by clicking on the ``Start`` button, typing ``Registry Editor`` in the search field and selecting the ``Registry Editor`` option in the search results.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00013.png

2. In the ``Registry Editor`` window, navigate to ``Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Mattermost\DefaultServerList`` and verify the servers you added using the ``Edit group policy`` app are listed.

3. Close the ``Registry Editor`` once verified.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00014.png

Install Mattermost Desktop using the MSI installer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Back in the folder the MSI installer was downloaded to, double click on the MSI installer to begin the Mattermost Desktop installation process.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00015.png

2. Installation of the MSI requires admin permission, so accept the resulting request to allow the installer to make changes to your device.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00016.png

3. Click the ``Finish`` button when the installation is complete.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00017.png

Verify Group Policy settings in the installed Desktop app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Launch the newly installed Mattermost app from the ``Start`` menu.

2. Verify the app loads the first server defined in the ``Edit group policy`` app.

   .. image:: ../images/desktop/msi_gpo/msi_gpo_installation_test_00018.png

Silent Installation Guide
--------------------------------------------

Perform a silent installation of MSI by running the following command:

``msiexec /i mattermost-desktop-v5.0.0-x64.msi /qn``

Note: Current version is 5.0.0. In the future, you may need to change this command accordingly.
