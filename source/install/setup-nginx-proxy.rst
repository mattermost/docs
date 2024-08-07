Set up an NGINX proxy
=====================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: install-nginx.rst
  :start-after: :nosearch:

.. include:: config-proxy-nginx.rst
  :start-after: :nosearch:

.. include:: config-ssl-http2-nginx.rst
  :start-after: :nosearch:

NGINX configuration FAQ
-----------------------

Why am I seeing the error "Too many redirects?"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may see this error if you're setting Mattermost in a sub-path. To resolve this error, add the following block to the HEAD request:

.. code-block:: text

  location ~* ^/sub-path {
      client_max_body_size 250M;
      proxy_set_header Connection "";

      if ($request_method = HEAD) {
          return 200;
      }
  }

Why are Websocket connections returning a 403 error?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is likely due to a failing cross-origin check. A check is applied for WebSocket code to see if the ``Origin`` header is the same as the host header. If it's not, a 403 error is returned. Open the file ``/etc/nginx/sites-available/mattermost`` as *root* in a text editor and make sure that the host header being set in the proxy is dynamic:

.. code-block:: text
  :emphasize-lines: 4

  location ~ /api/v[0-9]+/(users/)?websocket$ {
    proxy_pass            http://backend;
    (...)
    proxy_set_header      Host $host;
    proxy_set_header      X-Forwarded-For $remote_addr;
  }

Then in ``config.json`` set the ``AllowCorsFrom`` setting to match the domain being used by clients. You may need to add variations of the host name that clients may send. Your NGINX log will be helpful in diagnosing the problem.

.. code-block:: text
  :emphasize-lines: 2

  "EnableUserAccessTokens": false,
  "AllowCorsFrom": "domain.com domain.com:443 im.domain.com",
  "SessionLengthWebInDays": 30,

How do I setup an NGINX proxy with the Mattermost Docker installation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Find the name of the Mattermost network and connect it to the NGINX proxy.

.. code-block:: sh

  docker network ls
  # Grep the name of your Mattermost network like "mymattermost_default".
  docker network connect mymattermost_default nginx-proxy

2. Restart the Mattermost Docker containers.

.. code-block:: sh

  docker-compose stop app
  docker-compose start app

.. tip::

  You don't need to run the 'web' container, since NGINX proxy accepts incoming requests.

3. Update your ``docker-compose.yml`` file to include a new environment variable ``VIRTUAL_HOST`` and an ``expose`` directive.

.. code-block:: text

  environment:
    # set same as db credentials and dbname
    - MM_USERNAME=mmuser
    - MM_PASSWORD=mmuser-password
    - MM_DBNAME=mattermost
    - VIRTUAL_HOST=mymattermost.tld
  expose:
    - "80"
    - "443"

Why does NGINX fail when installing GitLab CE with Mattermost on Azure?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may need to update the Callback URLs for the Application entry of Mattermost inside your GitLab instance.

1. Log in to your GitLab instance as the admin.
2. Go to **Admin > Applications**.
3. Select **Edit** on GitLab-Mattermost.
4. Update the callback URLs to your new domain/URL.
5. Save the changes.
6. Update the external URL for GitLab and Mattermost in the ``/etc/gitlab/gitlab.rb`` configuration file.

Why does Certbot fail the http-01 challenge?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

  Requesting a certificate for yourdomain.com
  Performing the following challenges:
  http-01 challenge for yourdomain.com
  Waiting for verification...
  Challenge failed for domain yourdomain.com
  http-01 challenge for yourdomain.com
  Cleaning up challenges
  Some challenges have failed.

If you see the above errors this is typically because Certbot wasn't able to access port 80. This can be due to a firewall or other DNS configuration. Make sure that your A/AAAA records are pointing to this server and your ``server_name`` within the NGINX config doesn't have a redirect.

.. note::
   If you're using Cloudflare you'll need to disable ``force traffic to https``.

Certbot rate limiting
^^^^^^^^^^^^^^^^^^^^^^

If you're running certbot as stand-alone you'll see this error:

.. code-block:: text

      Error: Could not issue a Let's Encrypt SSL/TLS certificate for example.com.
      One of the Let's Encrypt rate limits has been exceeded for example.com.
      See the related Knowledge Base article for details.
      Details
      Invalid response from https://acme-v02.api.letsencrypt.org/acme/new-order.
      Details:
      Type: urn:ietf:params:acme:error:rateLimited
      Status: 429
      Detail: Error creating new order :: too many failed authorizations recently: see https://letsencrypt.org/docs/rate-limits/

If you're running Let's Encrypt within Mattermost you'll see this error:

.. code-block:: json

    {"level":"error","ts":1609092001.752515,"caller":"http/server.go:3088","msg":"http: TLS handshake error from ip:port: 429 urn:ietf:params:acme:error:rateLimited: Error creating new order :: too many failed authorizations recently: see https://letsencrypt.org/docs/rate-limits/","source":"httpserver"}

This means that you've attempted to generate a cert too many times. You can find more information `here <https://letsencrypt.org/docs/rate-limits>`_.
