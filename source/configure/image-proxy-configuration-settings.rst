:orphan:
:nosearch:

An image proxy is used by Mattermost apps to prevent them from connecting directly to remote self-hosted servers. Configure an image proxy by going to **System Console > Environment > Image Proxy**, or by editing the ``config.json`` file as described in the following tables.

Enable image proxy
~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+---------------------------------------------------------------------+
| An image proxy anonymizes Mattermost app connections and      | - System Config path: **Environment > Image Proxy**                 |
| prevents them from accessing insecure content.                | - ``config.json setting``: ``".ImageProxySettings.Enable": true",`` |
|                                                               | - Environment variable: ``MM_IMAGEPROXYSETTINGS_ENABLE``            |
| - **true**: **(Default)** Enables an image proxy for loading  |                                                                     |
|   external images.                                            |                                                                     |
| - **false**: Disables the image proxy.                        |                                                                     |
+---------------------------------------------------------------+---------------------------------------------------------------------+
| See the `image proxy </deploy/image-proxy.html>`__ documentation to learn more.                                                     |
+---------------------------------------------------------------+---------------------------------------------------------------------+

Image proxy type
~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The type of image proxy used by Mattermost.                   | - System Config path: **Environment > Image Proxy**                           |
|                                                               | - ``config.json setting``: ``".ImageProxySettings.ImageProxyType": "local",`` |
| - **local**: **(Default)** The Mattermost server itself acts  | - Environment variable: ``MM_IMAGEPROXYSETTINGS_IMAGEPROXYTYPE``              |
|   as the image proxy.                                         |                                                                               |
| - **atmos/camo**: An external atmos/camo image proxy is used. |                                                                               |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| See the `image proxy </deploy/image-proxy.html>`__ documentation to learn more.                                                               |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

Remote image proxy URL
~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+---------------------------------------------------------------------------+
| The URL of the atmos/camo proxy. This setting isn't needed    | - System Config path: **Environment > Image Proxy**                       |
| when using the **local** image proxy.                         | - ``config.json setting``: ``".ImageProxySettings.RemoteImageProxyURL",`` |
|                                                               | - Environment variable: ``MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYURL``     |
+---------------------------------------------------------------+---------------------------------------------------------------------------+

Remote image proxy options
~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The URL signing key passed to an atmos/camo image proxy.      | - System Config path: **Environment > Image Proxy**                           |
| This setting isn't needed when using the **local** image      | - ``config.json setting``: ``".ImageProxySettings.RemoteImageProxyOptions",`` |
| proxy type.                                                   | - Environment variable: ``MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYOPTIONS``     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| See the `image proxy </deploy/image-proxy.html>`__ documentation to learn more.                                                               |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
