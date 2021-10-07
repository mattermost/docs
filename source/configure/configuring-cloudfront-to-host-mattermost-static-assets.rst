.. _config-cloudfront:

Configuring CloudFront to host Mattermost static assets
=======================================================

Configuring CloudFront to host Mattermost's static assets allows for improved caching performance and shorter load times for those members of your team geographically distributed throughout the world. 

1. Create an S3 bucket using your desired domain. In our example it will be ``mattermost.example.com``.
2. Enable static hosting for your S3 bucket.
3. If your SiteURL is configured with a subpath (such as https://example.com/company/mattermost), your static assets must be rewritten before uploading. You can use the command below to rewrite the assets for the given subpath:

    ``mattermost config subpath --path /company/mattermost``

4. From the Mattermost distribution, upload the ``client`` directory to S3 and rename it to ``static``. You can use the AWS CLI command below from within the ``client`` directory  to upload all the files to S3. The files must be publicly readable with the permission ``public-read``.

    ``aws s3 cp --acl public-read --recursive . s3://static.spinmint.com/static/``

5. Set up your Mattermost app server and create a record from a subdomain of your desired domain to point directly to your app server. This is to bypass CloudFront to connect WebSockets. For our example we will use the domain ``ws.mattermost.example.com``. If you have multiple app servers, this domain should point to the load balancer/proxy such as ALB or NGINX.
6. Create a Web CloudFront distribution with the following configuration.

   a. Set Origin Domain Name to the S3 bucket you created above.
   b. (Recommended) Set Redirect HTTP to ``HTTPS`` for Viewer Protocol Policy.
   c. Set allowed HTTP Methods to ``GET, HEAD, OPTIONS, POST, PATCH, DELETE``.
   d. Set Forward Cookies to ``All``.
   e. Set Query string forwarding and Caching to ``Forward all, cache based on all``.
   f. Set your Alternate Domain Names to the domain you want Mattermost to be accessible from, e.g. ``mattermost.example.com``.
   g. Select ``Custom SSL Certificate`` and set the certificate for your domain.
   h. Set Default Root Object to ``/static/root.html``.

7. After creating your distribution, you need to add an additional origin. Select the origins tab and create an origin. Set the origin domain name to your Mattermost load balancer.
8. Next, create a behavior. 

   a. Set the Path Pattern to ``/api/*``.
   b. Set the origin to your Mattermost app server or load balancer.
   c. Set allowed HTTP Methods to ``GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE``.
   d. Set Forward Cookies to `All`.
   e. Set Query string forwarding and Caching to ``Forward all, cache based on all``.

9. Next, set up some custom error responses under the Error Pages tab.

   a. Set HTTP Error Code to ``403``.
   b. Set Customize Error Response to ``Yes``.
   c. Set response page path to ``/static/root.html``.
   d. Set HTTP Response Code to ``200``.
   e. Repeat the above steps for HTTP Error Code 404.

10. Now you can set up the domain you want Mattermost to be served from to point to your CloudFront distribution. Setting up this domain is beyond the scope of this guide.
11. Finally, set these Mattermost ``config.json`` settings:

    a. SiteURL: ``https://mattermost.example.com``
    b. WebsocketURL: ``wss://ws.mattermost.example.com``
    c. AllowCorsFrom: ``https://mattermost.example.com``
    d. AllowCookiesForSubdomains: ``true``

Upgrade Notes
~~~~~~~~~~~~~~~

When you upgrade your Mattermost app servers, you will need to re-upload the new client to your S3 bucket (see steps 3 and 4 above).

You should also run a CloudFront invalidation for ``/static/root.html``. You can do this in the console under the invalidations tab. 
