Upgrading Mattermost Server
===========================

In most cases you can upgrade Mattermost Server in a few minutes, but the upgrade can take longer depending on several factors, including the size and complexity of your installation, and the version that you're upgrading from.

.. _upgrade-table:

In the following table, look up your current version, review the applicable Important Notices, then click the link to the upgrade instructions.

.. csv-table::
  :header: "If your current version is:", "Read these Important Notices:", "Use these instructions:"
  :widths: auto

  "3.9.0", "Not Applicable", "`Upgrading to the latest version <../administration/upgrading-to-latest.html>`_"
  "3.8.x", "See `Important Notices`_ 7", "`Upgrading to the latest version <../administration/upgrading-to-latest.html>`_"
  "3.7.x", "See `Important Notices`_ 4 to 7", "`Upgrading to the latest version <../administration/upgrading-to-latest.html>`_"
  "3.6.x", "See `Important Notices`_ 4 to 7","`Upgrading to the latest version <../administration/upgrading-to-latest.html>`_"
  "3.5.x", "See `Important Notices`_ 2 to 7","`Upgrading to the latest version <../administration/upgrading-to-latest.html>`_"
  "3.4.0", "See `Important Notices`_ 2 to 7","`Upgrading to the latest version <../administration/upgrading-to-latest.html>`_"
  "3.3.0", "See `Important Notices`_ 1 to 7","`Upgrading to the latest version <../administration/upgrading-to-latest.html>`_"
  "3.2.0", "See `Important Notices`_ 1 to 7","`Upgrading to the latest version <../administration/upgrading-to-latest.html>`_"
  "3.1.0", "See `Important Notices`_ 1 to 7","`Upgrading to the latest version <../administration/upgrading-to-latest.html>`_"
  "3.0.3", "See `Important Notices`_ 1 to 7","`Upgrading to the latest version <../administration/upgrading-to-latest.html>`_"
  "2.2.0", "Not Applicable", "`Upgrading to version 3.0 <../administration/upgrading-to-3.0.html>`_"
  "2.1.0", "Not Applicable", "`Upgrading to version 3.0 <../administration/upgrading-to-3.0.html>`_"
  "2.0.0", "Not Applicable", "`Upgrading to version 3.0 <../administration/upgrading-to-3.0.html>`_"
  "1.4.0", "Not Applicable", "`Upgrading to version 2.0 <../administration/upgrading-to-2.0.html>`_"
  "1.3.0", "Not Applicable", "`Upgrading to version 2.0 <../administration/upgrading-to-2.0.html>`_"
  "1.2.1", "Not Applicable", "`Upgrading to version 2.0 <../administration/upgrading-to-2.0.html>`_"
  "1.2.0", "Not Applicable", "`Upgrading to version 2.0 <../administration/upgrading-to-2.0.html>`_"
  "1.1.1", "Not Applicable", "`Upgrading to version 2.0 <../administration/upgrading-to-2.0.html>`_"
  "1.1.0", "Not Applicable", "`Upgrading to version 2.0 <../administration/upgrading-to-2.0.html>`_"
  "1.0.0", "Not Applicable", "`Upgrading to version 2.0 <../administration/upgrading-to-2.0.html>`_"

.. toctree::
   :maxdepth: 1

   /administration/upgrading-to-latest.rst
   /administration/upgrading-to-3.0.rst
   /administration/upgrading-to-2.0.rst

Important Notices
-----------------

1. After upgrading to version 3.4: If public links are enabled, existing public links will no longer be valid. This is because in earlier versions, existing public links were not invalidated when the Public Link Salt was regenerated. You must update any place where you have published these links.

2. Enterprise Edition only: After upgrading to version 3.6.0, if you previously had values set for *RestrictPublicChannelManagement* and *RestrictPrivateChannelManagement*, the new settings for *RestrictPublicChannelCreation*, *RestrictPrivateChannelCreation*, *RestrictPublicChannelDeletion*, and *RestrictPrivateChannelDeletion* will take those settings as their default values.

3. In version 3.6, update the maximum number of files that can be open:

  On RHEL6 and Ubuntu 14.04
    Verify that the line ``limit nofile 50000 50000`` is included in the ``/etc/init/mattermost.conf`` file.
  On RHEL7 and Ubuntu 16.04
    Verify that the line ``LimitNOFILE=49152`` is included in the ``/etc/systemd/system/mattermost.service`` file.

4. In version 3.8, backwards compatibility with the old CLI tool was removed. If you have any scripts that rely on the old CLI, they must be revised to use the new CLI. For more information about the new CLI tool, see `Command Line Tools <../administration/command-line-tools.html>`_

5. Changes were made in 3.8.0 that require a change in the proxy configuration. If you're using NGINX:
  1. Open the NGINX configuration file as root. The file is usually ``/etc/nginx/sites-available/mattermost`` but might be different on your system.
  2. Locate the following line:
     `location /api/v3/users/websocket {`
  3. Replace the  line with ``location ~ /api/v[0-9]+/(users/)?websocket$ {``.

  If you are using a proxy other than NGINX, make the equivalent change to that proxy's configuration.

6. Security-related changes were made in 3.7.5 and 3.8.0 that require you to verify settings in the System Console before upgrading from version 3.7.4 and earlier.

  1. In the GENERAL section of the System Console, click **Configuration** and make sure that the **Site URL** is specified. It must not be empty. For more information about SiteURL, see `Configuration Settings <config-settings.html#site-url>`_
  2. In the GENERAL section of the System Console, click **Logging** and make sure that the **File Log Directory** field is either empty or has a directory path only. It must not have a filename as part of the path.

7. Security related changes were made in version 3.9.0 that cause any previously created team invite links, password reset links, and email verification links to no longer work. You must update any place where you have published these links.


Version Archive
---------------

Mattermost Enterprise Edition - Supported Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Enterprise Edition v3.10.0 - `View Changelog <./changelog.html#release-v3-10-0>`_ - `Download <https://releases.mattermost.com/3.10.0/mattermost-3.10.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.10.0/mattermost-3.10.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``3977cb70b88a6def7009176bf23880fe5ad864cead05a1f2cae7792c8ac9148c``
Mattermost Enterprise Edition v3.9.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-9-0>`_ - `Download <https://releases.mattermost.com/3.9.0/mattermost-3.9.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.9.0/mattermost-3.9.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``6e88c8a89c1320804960d215b8d5e6914075ad156f4590bbcd763252597e506c``
Mattermost Enterprise Edition v3.8.2 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-8-2>`_ - `Download <https://releases.mattermost.com/3.8.2/mattermost-3.8.2-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.8.2/mattermost-3.8.2-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``b99c86a2667f636eaee26331aa61a71a51b2d3d412eaa83fdebf8b53cddc6aeb``

Mattermost Enterprise Edition - Unsupported Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Mattermost Team Edition v3.10.0 - `View Changelog <./changelog.html#release-v3-10-0>`_ - `Download <https://releases.mattermost.com/3.10.0/mattermost-team-3.10.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.10.0/mattermost-team-3.10.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``ed64cb5357a8a3669386fd73b9a3f4934a10f0a9da02dc4be085e3d2e36886ed``
Mattermost Team Edition v3.9.0 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-9-0>`_ - `Download <https://releases.mattermost.com/3.9.0/mattermost-team-3.9.0-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.9.0/mattermost-team-3.9.0-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``c6179f7b2282cfbc8f0a691a90b41b554b62726f1dfb036fc59eed635556c8d9``
Mattermost Team Edition v3.8.2 - `View Changelog <https://docs.mattermost.com/administration/changelog.html#release-v3-8-2>`_ - `Download <https://releases.mattermost.com/3.8.2/mattermost-team-3.8.2-linux-amd64.tar.gz>`_
  - ``https://releases.mattermost.com/3.8.2/mattermost-team-3.8.2-linux-amd64.tar.gz``
  - SHA-256 Checksum: ``82cc85557dc21b3871ec89326769c11d3a89c9c41362fb3945247f8fba562ce7``

Mattermost Team Edition Server Archive - Unsupported Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
