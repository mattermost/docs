.. _image-proxy:

Image Proxy
================================

Using image proxies means that users make only secure requests. By allowing image requests to go straight to third-party
servers, tracking pixels is allowed. Users can put invisible images in posts that logs time and location data
for every user that views the post. An image proxy protects user privacy by eliminating this direct interaction with 
third-party servers.

Proxy servers also provide a layer of caching, and can be made faster and more reliable than third-party sites. This caching 
also helps preserve posts by protecting them from dead images.

The local proxy is using `willnorris/imageproxy <https://github.com/willnorris/imageproxy>`_, and is enabled by the Mattermost server by default.

You may alternatively use `atmos/camo <https://github.com/atmos/camo>`_ http proxy to route images through SSL:

.. _atmos-camo:

Set Up Guide for atmos/camo Proxy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This guide gives an example of how to set up an image proxy using ``atmos/camo``:

Deploy an ``atmos/camo`` (https://github.com/atmos/camo) instance to image-proxy.mattermost.com and update the 
configuration in **System Console > Files > Storage**. For example:
 - **Image Proxy Type**: ``atmos/camo``
 - **Remote Image Proxy URL**: ``https://image-proxy.mattermost.com``
 - **Remote Image Proxy Options**: ``CAMO_KEY``, which is the secret string used for the sample ``atmos/camo`` deployment.

.. image:: ../images/image-proxy.png

The URL will be replaced with something similar to the following: https://image-proxy.mattermost.com/d7b4022717e8d015440cd70183b81196298b9453/687474703a2f2f692e726564642e69742f36636f687964636b6b363530312e6a7067 (See `https://github.com/atmos/camo <https://github.com/atmos/camo>`__).
  
Next, if you post a message with an image, you will get a proxied image in your post. This will ensure that every image
is downloaded via HTTPS.
