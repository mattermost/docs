Pre-authentication secrets
==========================

For mobile and desktop applications only, Mattermost deployments can use a reverse proxy to validate pre-authentication secrets before allowing requests to reach the Mattermost server. This adds an additional security layer by checking for the ``X-Mattermost-Preauth-Secret`` header.

Pre-authentication secrets are only supported for mobile and desktop applications. Web browser clients don't support this feature.

.. important::

  We recommend whitelisting the ``/api/v4/notifications/ack`` endpoint (allowed without pre-authentication secret validation) to ensure proper notification acknowledgement functionality for mobile applications.

NGINX configuration example
---------------------------

Here's an example partial NGINX configuration that validates the pre-authentication secret header:

.. code-block:: text

  server {
      # ...

      # Define the expected pre-auth secret
      set $expected_secret "your-secure-pre-auth-secret-here";

      # Whitelist the notifications/ack endpoint (no pre-auth secret required)
      location = /api/v4/notifications/ack {
         # ...
      }

      location / {
          # Check if X-Mattermost-Preauth-Secret header matches expected value
          if ($http_x_mattermost_preauth_secret != $expected_secret) {
              return 403 "Forbidden: Invalid pre-authentication secret";
          }

          # ...
      }
  }

.. important::

  Replace ``your-secure-pre-auth-secret-here`` with a strong, unique secret that will be configured in your mobile and desktop applications. Store this secret securely and rotate it regularly as part of your security practices.
