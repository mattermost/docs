Image Proxy
================================

Using image proxies means that users make only secure requests. By allowing image requests to go straight to third-party
servers, tracking pixels is allowed. Users can put invisible images in posts that logs time and location data
for every user that views the post. An image proxy protects user privacy by eliminating this direct interaction with 
third-party servers.

Many proxy servers also provide resizing-as-a-service. For example, if you use `atmos/camo image proxy server <https://github.com/atmos/camo>`_, you can configure 
``ImageProxyOptions`` to resize images if they're more than ``x`` pixels tall. Users can save bandwidth by downloading 
only the resolution they need.

Proxy servers also provide a layer of caching, and can be made faster and more reliable than third-party sites. This caching 
also helps preserve posts by protecting them from dead images.

Configuration Keys
~~~~~~~~~~~~~~~~~

Three configuration keys are included: ``ImageProxyType``, ``ImageProxyURL``, ``ImageProxyOptions``. When these
keys are configured, posts served to the client will have their markdown modified such that all images are 
loaded through a proxy.

Image Proxy Type
........................

Configure an image proxy to load all Markdown images through a proxy. The image proxy prevents users from making 
insecure image requests to Mattermost, provides caching for increased performance, and automates image adjustments 
such as resizing.

Image Proxy URL
........................

URL of your image proxy server.

Image Proxy Options
........................

Additional options for basic image adjustments such as resizing, cropping and rotation. Contact your image proxy 
service provider to learn more about what options are supported.

Setup Guide
~~~~~~~~~~~~~~~~~

This guide gives an example of how to set up an image proxy using ``atmos/camo``:

Deploy an ``atmos/camo`` (https://github.com/atmos/camo) instance to image-proxy.mattermost.com and update the 
configuration in the system console. For example:
 - "ImageProxyType": "atmos/camo",
 - "ImageProxyURL": "https://image-proxy.mattermost.com",
 - "ImageProxyOptions": "500,fit"

.. image:: ../images/image-proxy.png

The URL will be replaced with something similar to the following: https://imageproxy.mysite.com/x500,s5xQmRR3GQa13jFHdJJb01fqATSoZkbBvMXG7Vs4jFGU=/https://i.redd.it/6cohydckk6501.jpg
(See `https://github.com/atmos/camo <https://github.com/atmos/camo>`_).
  
Next, if you post a message with an image, you will get a proxied image in your post. This will ensure that every image
is downloaded via HTTPS. In this specific example, having ``ImageProxyOptions`` set to ``500,fit`` will also resize images
for clients to a maximum of 500 pixels in either dimension.
