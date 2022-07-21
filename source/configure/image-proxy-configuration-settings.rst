:orphan:

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 25
  :target: https://mattermost.com/sign-up
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 25
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

:nosearch:

An image proxy is used by Mattermost apps to prevent them from connecting directly to remote self-hosted servers. Configure an image proxy by going to **System Console > Environment > Image Proxy**, or by editing the ``config.json`` file as described in the following table.

.. include:: common-config-settings-notation.rst
    :start-after: :nosearch:

Enable image proxy
~~~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+---------------------------------------------------------------------+
| An image proxy anonymizes Mattermost app connections and      | - System Config path: **Environment > Image Proxy**                 |
| prevents them from accessing insecure content.                | - ``config.json setting``: ``".ImageProxySettings.Enable": true",`` |
|                                                               | - Environment variable: ``MM_IMAGEPROXYSETTINGS_ENABLE``            |
| - **true**: **(Default)** Enables an image proxy for loading  |                                                                     |
|   external images.                                            |                                                                     |
| - **false**: Disables the image proxy.                        |                                                                     |
+---------------------------------------------------------------+---------------------------------------------------------------------+
| See the `image proxy <https://docs.mattermost.com/deploy/image-proxy.html>`__ documentation to learn more.                          |
+---------------------------------------------------------------+---------------------------------------------------------------------+

Image proxy type
~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The type of image proxy used by Mattermost.                   | - System Config path: **Environment > Image Proxy**                           |
|                                                               | - ``config.json setting``: ``".ImageProxySettings.ImageProxyType": "local",`` |
| - **local**: **(Default)** The Mattermost server itself acts  | - Environment variable: ``MM_IMAGEPROXYSETTINGS_IMAGEPROXYTYPE``              |
|   as the image proxy.                                         |                                                                               |
| - **atmos/camo**: An external atmos/camo image proxy is used. |                                                                               |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| See the `image proxy <https://docs.mattermost.com/deploy/image-proxy.html>`__ documentation to learn more.                                    |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

Remote image proxy URL
~~~~~~~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+---------------------------------------------------------------------------+
| The URL of the atmos/camo proxy. This setting isn't needed    | - System Config path: **Environment > Image Proxy**                       |
| when using the **local** image proxy.                         | - ``config.json setting``: ``".ImageProxySettings.RemoteImageProxyURL",`` |
|                                                               | - Environment variable: ``MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYURL``     |
+---------------------------------------------------------------+---------------------------------------------------------------------------+

Remote image proxy options
~~~~~~~~~~~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The URL signing key passed to an atmos/camo image proxy.      | - System Config path: **Environment > Image Proxy**                           |
| This setting isn't needed when using the **local** image      | - ``config.json setting``: ``".ImageProxySettings.RemoteImageProxyOptions",`` |
| proxy type.                                                   | - Environment variable: ``MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYOPTIONS``     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| See the `image proxy <https://docs.mattermost.com/deploy/image-proxy.html>`__ documentation to learn more.                                    |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+