.. _config-cloudfront:

Configuring CloudFront to host Mattermost static assets
=======================================================

1. Create an S3 bucket using your desired domain. In our example it will be mattermost.example.com.
2. Enable static hosting for you S3 bucket.
3. From the Mattermost distribution, upload the ``client`` directory to s3. Renaming it to ``static``. You can use aws CLI command below from within the client directory. Be sure however you do this that the files are public readable.

    ``aws s3 cp --acl public-read --recursive . s3://static.spinmint.com/static/``

4. Setup your Mattermost app server and create a record from a subdomain of your desired domain to point directly to your app server. This is to bypass CloudFront to connect websockets. For our example we will use the domain ws.mattermost.example.com. If you have multiple app servers, this domain should point to the load balancer/proxy such as ALB or nginx.
5. Create a Web CloudFront distribution.
   a. Set Origin Domain Name to the S3 bucket you created above.
   b. For Viewer Protocol Policy we recomend Redirect HTTP to HTTPS.
   c. Allowed HTTP Methods should be set to GET, HEAD, OPTIONS, POST, PATCH, DELETE.
   d. Forward Cookies should be set to All.
   e. Query string forwarding and Caching should be set to Forward all, cache based on all.
   f. You should set your Alternate Domain Names to the domain you want Mattermost to be accessible from, mattermost.example.com in our example.
   g. Select ``Custom SSL Certificate`` and set the certificate for your domain.
   h. Default Root Object should be set to ``/static/root.html``.
6. After creating your distribution. You need to add an aditional origin. Select the origins tab and create an origin. Set the origin domain name to your Mattermost load balancer.
7. Next create a behavior. 
   a. Set the Path Pattern to ``/api/*``.
   b. Set the origin to your Mattermost app server or load balancer.
   c. Set allowed HTTP Methods to GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE.
   d. Forward Cookies should be set to All.
   e. Query string forwarding and Caching should be set to Forward all, cache based on all.
8. Next setup some custom error responses under the Error Pages tab.
   a. Set HTTP Error Code to 403.
   b. Set Customize Error Response to Yes.
   c. Set response page path to ``/static/root.html``.
   d. Set HTTP Response Code to 200.
   e. Create and do the same for the HTTP Error Code 404.
9. Now you can setup the domain you want Mattermost to be served from to point to your CoudFront distribution.
10. Set these Mattermost config.json settings:
    a. SiteURL: ``https://mattermost.example.com``
    b. WebsocketURL: ``wss://ws.mattermost.example.com``
    c. AllowCorsFrom: ``https://mattermost.example.com``
    d. AllowCookiesForSubdomains: ``true``
