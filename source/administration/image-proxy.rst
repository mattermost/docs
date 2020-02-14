.. _image-proxy:

Image Proxy
================================

Using image proxies means that users make only secure requests for Markdown embedded images. By allowing image requests to go straight to third-party
servers, tracking pixels is allowed. Users can put invisible images in posts that logs time and location data
for every user that views the post. An image proxy protects user privacy by eliminating this direct interaction with 
third-party servers.

Proxy servers also provide a layer of caching, and can be made faster and more reliable than third-party sites. This caching 
also helps preserve posts by protecting them from dead images.

When enabled, the image proxy needs to be publicly accessible to both the Mattermost client and server.

Currently the image proxy only works for Markdown embedded images and not `image preview of plaintext URLs <https://github.com/mattermost/mattermost-server/issues/11857>`_.

You may alternatively use `atmos/camo <https://github.com/atmos/camo>`_ http proxy to route images through SSL:

Local Image Proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The local image proxy is enabled on the Mattermost server by default. When using the local image proxy, Mattermost apps will download external images through the Mattermost server itself.

.. note:: 
   With the local image proxy enabled, requests for images hosted on the local network are now affected by the ``AllowUntrustedInternalConnections`` setting. See `documentation <https://docs.mattermost.com/administration/config-settings.html#allow-untrusted-internal-connections-to>`_ for more information or if you are seeing unintentionally blocked images.

.. _atmos-camo:

atmos/camo Image Proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `atmos/camo <https://github.com/atmos/camo>`_ image proxy is a standalone image proxy that can be deployed separately from the Mattermost server. It provides additional configuration options over the built-in image proxy, and it can also be used if isolation between the Mattermost server and image proxy is desired.

This guide gives an example of how to set up an image proxy using ``atmos/camo``:

Deploy an ``atmos/camo`` (https://github.com/atmos/camo) instance to image-proxy.mattermost.com and update the 
configuration in **System Console > Files > Storage** in prior versions or **System Console > Environment > Image Proxy** in versions after 5.12. For example:
 - **Image Proxy Type**: ``atmos/camo``
 - **Remote Image Proxy URL**: ``https://image-proxy.mattermost.com``
 - **Remote Image Proxy Options**: ``CAMO_KEY``, which is the secret string used for the sample ``atmos/camo`` deployment.

.. image:: ../images/image-proxy.png

The URL will be replaced with something similar to the following (see `https://github.com/atmos/camo <https://github.com/atmos/camo>`__ for details):

.. code-block:: text

  https://image-proxy.mattermost.com/d7b4022717e8d015440cd70183b81196298b9453/687474703a2f2f692e726564642e69742f36636f687964636b6b363530312e6a7067
  
Next, if you post a message with an image, you will get a proxied image in your post. This will ensure that every image
is downloaded via HTTPS.
