Upgrading Mattermost Server
===========================

In most cases you can upgrade Mattermost Server in a few minutes, but the upgrade can take longer depending on several factors, including the size and complexity of your installation, and the version that you're upgrading from.

Upgrading to the Latest Version
-------------------------------

If you are upgrading from version 3.0 or later, these instructions apply to you.

If you are upgrading from a version earlier than 3.0.0 but later than 2.0.0, you must first `upgrade to version 3.0.3 <../administration/upgrading-to-3.0.html>`_.

If you are upgrading from a version earlier than 2.0.0, you must first `upgrade to version 2.0 <../administration/upgrading-to-2.0.html>`_.

.. _before-you-begin:

**Before you begin**

Read these instructions carefully from start to finish. Make sure that you understand each step before starting the upgrade. If you have questions or concerns, you can ask on the Mattermost forum at https://forum.mattermost.org/ or in the Mattermost *Peer-to-peer Help* channel at https://pre-release.mattermost.com/core/channels/peer-to-peer-help.

.. important::
  Review the :doc:`important-upgrade-notes` to make sure you are aware of any actions you need to take before or after upgrading from your particular version.

You should gather the following information before starting the upgrade:

Existing install directory - *{install-path}*
  If you don't know where Mattermost Server is installed, use the ``whereis platform`` command. The output should be similar to */opt/mattermost/bin/platform*. The install directory is everything before the last occurrence of the string */mattermost*. In this example, the *{install-path}* is ``/opt``.
Location of your local storage directory
  The local storage directory contains all the files that users have attached to their messages. If you don't know its location, open the System Console and go to **Files > Storage** and read the value in **Local Storage Directory**. Relative paths are relative to the ``mattermost`` directory. For example, if the local storage directory is ``./data/`` then the absolute path is ``{install-path}/mattermost/data``.
Owner and group of the install directory - *{owner}* and *{group}*
  Use the ``ls -l {install-path}/mattermost/bin/platform`` command to get the owner and group.

**To upgrade Mattermost Server**:

1. Review the :doc:`important-upgrade-notes` to make sure you are aware of any actions you need to take before or after upgrading from your particular version.

2. In a terminal window on the server that hosts Mattermost Server, change to your home directory.

  ``cd ~``

3. Delete any files and directories that might still exist from a previous download.

  .. code-block:: text

    rm mattermost*.gz
    rm -r mattermost

4. Download the latest version of Mattermost Server.

  Enterprise Edition
    ``wget https://releases.mattermost.com/4.0.1/mattermost-4.0.1-linux-amd64.tar.gz``
  Team Edition
    ``wget https://releases.mattermost.com/4.0.1/mattermost-team-4.0.1-linux-amd64.tar.gz``

5. Extract the Mattermost Server files.

  ``tar -xzf mattermost*.gz``

6. Make a copy of your configuration file. The existing file is overwritten during the upgrade, so it's important that you don't forget this step.

    ``cp {install-path}/mattermost/config/config.json config.json``

7. Stop Mattermost Server.

  On Ubuntu 14.04 and RHEL 6.6: ``sudo service mattermost stop``

  On Ubuntu 16.04 and RHEL 7.1: ``sudo systemctl stop mattermost``

8. Back up your data.
  a. Back up your database using your organization’s standard procedures for backing up MySQL or PostgreSQL.
  b. If you’re using local file storage, back up the location where files are stored.

9. Copy the files that you extracted earlier to the install directory.

  ``sudo cp -r mattermost {install-path}``

10. Restore your configuration file.

  ``sudo cp config.json {install-path}/mattermost/config``

11. Change ownership of the new files.

  ``sudo chown -R {owner}:{group} {install-path}/mattermost``

12. Start Mattermost server.

  On Ubuntu 14.04 and RHEL 6.6: ``sudo service mattermost start``

  On Ubuntu 16.04 and RHEL 7.1: ``sudo systemctl start mattermost``

13. If you have TLS set up on your Mattermost server, you must activate the CAP_NET_BIND_SERVICE capability to allow the new Mattermost binary to bind to low ports.

  1. ``cd {install-path}``
  2. ``sudo setcap cap_net_bind_service=+ep ./bin/platform``

14. Upgrade your ``config.json`` schema:

  a. Open the System Console and a change a setting, then revert it. This should enable the Save button for that page.
  b. Click **Save**.
  c. Refresh the page.

  Your current settings are preserved, and new settings are added with default values.

After the server is upgraded, users might need to refresh their browsers to experience any new features.

Upgrading Team Edition to Enterprise Edition
--------------------------------------------

To upgrade from the Team Edition to the Enterprise Edition, follow the normal upgrade instructions above, but make sure that you download the Enterprise Edition in Step 3.

After the Enterprise Edition is running, open the *System Console* and go to **OTHER > Edition and License > License Key** and upload your license key file.

Version Archive
---------------

Mattermost Enterprise Edition - Supported Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Enterprise Edition v4.0.1 - `View Changelog <./changelog.html#release-v4-0-1>`_ - `Download <https://releases.mattermost.com/4.0.1/mattermost-4.0.1-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/4.0.1/mattermost-4.0.1-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``dc675eae9bcc0dd465e6e8286c4b513a7117616591ed978bb251ae6d25fc3087``
Mattermost Enterprise Edition v3.10.1 - `View Changelog <./changelog.html#release-v3-10-1>`_ - `Download <https://releases.mattermost.com/3.10.1/mattermost-3.10.1-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.10.1/mattermost-3.10.1-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``1cef548b916972a2a932bc9c819a3928162e3a6aaee8762259174d8cdc003b00``
Mattermost Enterprise Edition v3.9.1 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-9-1>`_ - `Download <https://releases.mattermost.com/3.9.1/mattermost-3.9.1-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.9.1/mattermost-3.9.1-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``2c7419a768ac0ae1eb58fd4c578849670ecc226568efc3f76ac21f7f9147470a``

Mattermost Enterprise Edition - Unsupported Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Enterprise Edition v3.8.3 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-8-3>`_ - `Download <https://releases.mattermost.com/3.8.3/mattermost-3.8.3-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.8.3/mattermost-3.8.3-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``c223320a82222ebff002071633c6331dce0da6ff6ac8e22d0ab0d7055356ff9c``
Mattermost Enterprise Edition v3.7.5 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-7-5>`_ - `Download <https://releases.mattermost.com/3.7.5/mattermost-3.7.5-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.7.5/mattermost-3.7.5-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``65e65da661edbc7b7b2b02411f13dbe498fd704d5ae1289789feca79fe00b58a``
Mattermost Enterprise Edition v3.6.7 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-6-7>`_ - `Download <https://releases.mattermost.com/3.6.7/mattermost-3.6.7-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.6.7/mattermost-3.6.7-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``8e666708fead5fbfcf1f20617b07fda21cc8cbc85f9690321cbf4a41bfc1dd89``
Mattermost Enterprise Edition v3.5.1 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-5-1>`_ - `Download <https://releases.mattermost.com/3.5.1/mattermost-3.5.1-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.5.1/mattermost-3.5.1-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``b972ac6f38f8b4c4f364e40a7c0e7819511315a81cb38c8a51c0622d7c5b14a1``
Mattermost Enterprise Edition v3.4.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-4-0>`_ - `Download <https://releases.mattermost.com/3.4.0/mattermost-3.4.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.4.0/mattermost-3.4.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``3329fe3ef4d6bd7bd156eec86903b5d9db30d8c62545e4f5ca63633a64559f16``
Mattermost Enterprise Edition v3.3.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-3-0>`_ - `Download <https://releases.mattermost.com/3.3.0/mattermost-3.3.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.3.0/mattermost-3.3.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``d12d567c270a0c163e07b38ff41ea1d7839991d31f7c10b6ad1b4ef0f05f4e14``
Mattermost Enterprise Edition v3.2.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-2-0>`_ - `Download <https://releases.mattermost.com/3.2.0/mattermost-3.2.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.2.0/mattermost-3.2.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``f66597ad2fa94d3f75f06135129aa91cddd35dd8b94acab4aa15dfa225596422``
Mattermost Enterprise Edition v3.1.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-1-0>`_ - `Download <https://releases.mattermost.com/3.1.0/mattermost-3.1.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.1.0/mattermost-3.1.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``9e29525199e25eca6b7fe6422b415f6371d21e22c344ca6febc5e64f69ec670b``
Mattermost Enterprise Edition v3.0.3 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-0-3>`_ - `Download <https://releases.mattermost.com/3.0.3/mattermost-enterprise-3.0.3-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.0.3/mattermost-enterprise-3.0.3-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``3c692f8532b1858aefd2f0c2c22721e6b18734580a84a8ae5d6ce891f0e16f07``
Mattermost Enterprise Edition v2.2.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v2-2-0>`_ - `Download <https://releases.mattermost.com/2.2.0/mattermost-enterprise-2.2.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/2.2.0/mattermost-enterprise-2.2.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``a7e997526d9204eab70c74a31d51eea693cca0d4bf0f0f71760f14f797fa5477``
Mattermost Enterprise Edition v2.1.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v2-1-0>`_ - `Download <https://releases.mattermost.com/2.1.0/mattermost-enterprise-2.1.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/2.1.0/mattermost-enterprise-2.1.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``9454c3daacae602025b03950590e3f1ecd540b85a4bb7ad73bdca212ba85cf7a``

Mattermost Team Edition Server Archive - Supported Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Team Edition v4.0.1 - `View Changelog <./changelog.html#release-v4-0-1>`_ - `Download <https://releases.mattermost.com/4.0.1/mattermost-team-4.0.1-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/4.0.1/mattermost-team-4.0.1-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``55591dcbba490617b5d754316d9c76515770e53146ac293c830704d8a55fc53a``
Mattermost Team Edition v3.10.1 - `View Changelog <./changelog.html#release-v3-10-1>`_ - `Download <https://releases.mattermost.com/3.10.1/mattermost-team-3.10.1-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.10.1/mattermost-team-3.10.1-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``6e4976e500e9e31358256a8a169378fb99bed643c8ad10005f3695cfb3041de4``
Mattermost Team Edition v3.9.1 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-9-1>`_ - `Download <https://releases.mattermost.com/3.9.1/mattermost-team-3.9.1-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.9.1/mattermost-team-3.9.1-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``f7f878c7d195e1f336b7025fbb4063c1796fa16296ac2d7437d2a5067750966e``

Mattermost Team Edition Server Archive - Unsupported Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Team Edition v3.8.3 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-8-3>`_ - `Download <https://releases.mattermost.com/3.8.3/mattermost-team-3.8.3-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.8.3/mattermost-team-3.8.3-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``1a5de4052c007c54fce6cd844ab3e89aabc8d1a05b8bac72ef58f6896760c4e1``
Mattermost Team Edition v3.7.5 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-7-5>`_ - `Download <https://releases.mattermost.com/3.7.5/mattermost-team-3.7.5-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.7.5/mattermost-team-3.7.5-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``eaee6a57ab9e2924f71853cbebf465d63f7dbf1112716c0e4768984de39f83a2``
Mattermost Team Edition v3.6.7 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-6-7>`_ - `Download <https://releases.mattermost.com/3.6.7/mattermost-team-3.6.7-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.6.7/mattermost-team-3.6.7-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``8378f15a6bd070386077798f36d8e521b63844bc838f6553915c6fd4fba3b01d``
Mattermost Team Edition v3.5.1 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-5-1>`_ - `Download <https://releases.mattermost.com/3.5.1/mattermost-team-3.5.1-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.5.1/mattermost-team-3.5.1-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``2c6bc8b1c25e48d1ac887cd6cbef77df1f80542127b4d98c4d7c0dfbfade04d5``
Mattermost Team Edition v3.4.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-4-0>`_ - `Download <https://releases.mattermost.com/3.4.0/mattermost-team-3.4.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.4.0/mattermost-team-3.4.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``c352f6c15466c35787bdb5207a6efe6b471513ccdd5b1f64a91a8bd09c3365da``
Mattermost Team Edition v3.3.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-3-0>`_ - `Download <https://releases.mattermost.com/3.3.0/mattermost-team-3.3.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.3.0/mattermost-team-3.3.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``09948edb32ebb940708e30a05c269e69568dfd2e0c05495392f353b26139b79a``
Mattermost Team Edition v3.2.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-2-0>`_ - `Download <https://releases.mattermost.com/3.2.0/mattermost-team-3.2.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.2.0/mattermost-team-3.2.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``14e5c1460a991791ef3dccd6b5aeab40ce903090c5f6c15e7974eb5e4571417a``
Mattermost Team Edition v3.1.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-1-0>`_ - `Download <https://releases.mattermost.com/3.1.0/mattermost-team-3.1.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.1.0/mattermost-team-3.1.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``dad164d2382428c36623b6d50e3290336a3be01bae278a465e0d8d94b701e3ff``
Mattermost Team Edition v3.0.3 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-0-3>`_ - `Download <https://releases.mattermost.com/3.0.3/mattermost-team-3.0.3-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.0.3/mattermost-team-3.0.3-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``b60d26a13927b614e3245384559869ae31250c19790b1218a193d52599c09834``
Mattermost Team Edition v2.2.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v2-2-0>`_ - `Download <https://releases.mattermost.com/2.2.0/mattermost-team-2.2.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/2.2.0/mattermost-team-2.2.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``d723fe9bf18d2d2a419a8d2aa6ad94fc99f251f8382c4342f08a48813501ca06``
Mattermost Team Edition v2.1.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v2-1-0>`_ - `Download <https://releases.mattermost.com/2.1.0/mattermost-team-2.1.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/2.1.0/mattermost-team-2.1.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``2825434aad23db1181e03b036bd826e66d6d4f21d337d209679a095a3ed9a4d2``
Mattermost Team Edition v2.0.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v2-0-0>`_ - `Download <https://releases.mattermost.com/2.0.0/mattermost-team-2.0.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/2.0.0/mattermost-team-2.0.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``005687c6a8128e1e40d01933f09d7da1a1b70b149a6bef96d923166bc1e7ce8f``
Mattermost Team Edition v1.4.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v1-4-0>`_ - `Download <https://releases.mattermost.com/1.4.0/mattermost-team-1.4.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/1.4.0/mattermost-team-1.4.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``0874dad79415066466c22ac584e599897124106417e774818cf40864d202dbb0``
Mattermost Team Edition v1.3.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v1-3-0>`_ - `Download <https://releases.mattermost.com/1.3.0/mattermost-team-1.3.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/1.3.0/mattermost-team-1.3.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``57af87ae8a98743b5379ed70f93a923654f7b8547f89b7f99ef9a718f472364d``
Mattermost Team Edition v1.2.1 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v1-2-1>`_ - `Download <https://releases.mattermost.com/1.2.1/mattermost-team-1.2.1-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/1.2.1/mattermost-team-1.2.1-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``f4cc5b0e1026026ff0cea4cc915b92967f9dfdf497c249731dc804a9a2ff156d``
Mattermost Team Edition v1.1.1 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v1-1-1>`_ - `Download <https://releases.mattermost.com/1.1.1/mattermost-team-1.1.1-linux-amd64.tar.gz>`_
   - ``https://releases.mattermost.com/1.1.1/mattermost-team-1.1.1-linux-amd64.tar.gz``
   - SHA-256 Checksum: ``e6687b9d7f94538e1f4a9f93a0bcb8a66e293e2260433ed648964baa53c3e561``
Mattermost Team Edition v1.0.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html##release-v1-0-0>`_ - `Download <https://releases.mattermost.com/1.0.0/mattermost-team-1.0.0-linux-amd64.tar.gz>`_
   - ``https://releases.mattermost.com/1.0.0/mattermost-team-1.0.0-linux-amd64.tar.gz``
   - SHA-256 Checksum: ``208b429cc29119b3d3c686b8973d6100eb02845b1da2f18744195f055521cbc8``
Mattermost Team Edition v0.7.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v0-7-0-beta>`_ - `Download <https://releases.mattermost.com/0.7.0/mattermost-team-0.7.0-linux-amd64.tar.gz>`_
   - ``https://releases.mattermost.com/0.7.0/mattermost-team-0.7.0-linux-amd64.tar.gz``
   - SHA-256 Checksum: ``f0a0e5b5fab3aeb5dc638ab3059b3ea5bf7bc1ec5123db1199aa10db41bfffb1``
Mattermost Team Edition v0.6.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v0-6-0-alpha>`_ - `Download <https://releases.mattermost.com/0.6.0/mattermost-team-0.6.0-linux-amd64.tar.gz>`_
   - ``https://releases.mattermost.com/0.6.0/mattermost-team-0.6.0-linux-amd64.tar.gz``
   - SHA-256 Checksum: ``9eb364f7f963af32d4a9efe3bbb5abb2a21ca5d1a213b50ca461dab047a123b6``
