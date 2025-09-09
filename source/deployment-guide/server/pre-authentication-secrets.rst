Pre-authentication secrets
==========================

From Mattermost server v10.12 and mobile v2.32, Mattermost deployments can use a reverse proxy to validate pre-authentication secrets before allowing desktop and mobile requests to reach the Mattermost server. This adds an additional security layer by checking for the ``X-Mattermost-Preauth-Secret`` header.

Pre-authentication secrets are only supported for mobile and desktop applications. Web browser clients don't support this feature.

When pre-authentication secret validation fails, the reverse proxy must return the ``X-Reject-Reason: pre-auth`` header along with the 403 status code. This header allows mobile and desktop applications to specifically identify pre-authentication failures and provide appropriate error messaging to users.

.. important::

  We recommend whitelisting certain endpoints where the pre-authentication header may not be available. The specific endpoints depend on your authentication configuration:

  - ``/api/v4/notifications/ack`` - Required for proper notification acknowledgement functionality
  - ``/api/v4/config/client`` - Required for authentication flows that redirect to the browser, such as SAML, OAuth and OpenID.

  **Additional endpoints based on your authentication setup:**

  - SAML: ``/login/sso/saml``
  - OpenID: ``/oauth/{service:[A-Za-z0-9]+}/complete``, ``/oauth/{service:[A-Za-z0-9]+}/login``, ``/oauth/{service:[A-Za-z0-9]+}/mobile_login``, ``/oauth/{service:[A-Za-z0-9]+}/signup``
  - OAuth: ``/api/v3/oauth/{service:[A-Za-z0-9]+}/complete``, ``/signup/{service:[A-Za-z0-9]+}/complete``, ``/login/{service:[A-Za-z0-9]+}/complete``

NGINX configuration example
---------------------------

Here's an example partial NGINX configuration that validates the pre-authentication secret header:

.. code-block:: text

  server {
      # ...

      # Define the expected pre-auth secret
      set $expected_secret "your-secure-pre-auth-secret-here";

      # Whitelist endpoints where pre-auth secret may not be available
      location = /api/v4/notifications/ack {
         # Pass through without verifying pre-auth secret validation
         # ...
      }
      
      location = /api/v4/config/client {
         # Pass through without verifying pre-auth secret validation
         # ...
      }

      # Additional whitelisted endpoints based on authentication configuration
      # Uncomment and configure as needed for your setup:
      # Note: Replace {service:[A-Za-z0-9]+} with your specific service names
      # (e.g., google, gitlab, openid, office365) or use the regex pattern for multiple services
      
      # SAML
      # location = /login/sso/saml {
      #    # ...
      # }
      
      # OpenID/OAuth patterns (use regex for multiple services)
      # location ~ ^/oauth/[A-Za-z0-9]+/(complete|login|mobile_login|signup)$ {
      #    # ...
      # }
      # Or for specific services:
      # location ~ ^/oauth/(google|gitlab|office365)/(complete|login|mobile_login|signup)$ {
      #    # ...
      # }
      # location ~ ^/api/v3/oauth/[A-Za-z0-9]+/complete$ {
      #    # ...
      # }
      # location ~ ^/(signup|login)/[A-Za-z0-9]+/complete$ {
      #    # ...
      # }

      location / {
          # Check if X-Mattermost-Preauth-Secret header matches expected value
          if ($http_x_mattermost_preauth_secret != $expected_secret) {
              add_header X-Reject-Reason pre-auth always;
              add_header Cache-Control "no-store" always;
              return 403 "Forbidden: Invalid pre-authentication secret";
          }

          # ...
      }
  }

Replace ``your-secure-pre-auth-secret-here`` with a strong, unique secret that will be configured in your mobile and desktop applications. Store this secret securely and rotate it regularly as part of your security practices.

Desktop application security considerations
-------------------------------------------

The Mattermost desktop application stores pre-authentication secrets using Electron's ``safeStorage`` API, which integrates with the operating system's secure credential storage:

- **Windows**: Windows Credential Manager
- **macOS**: Keychain Access
- **Linux**: Secret Service API (requires kwallet, gnome-libsecret, or compatible backend)

.. warning::

  On Linux systems where no secure credential storage is available, the pre-authentication secret may be stored in **plain text**. This occurs when:
  
  - No secret store backend is available (kwallet, gnome-libsecret, etc.)
  - The desktop environment is not recognized
  - The system falls back to Electron's ``basic_text`` storage
  
  In these cases, consider the security implications before deploying pre-authentication secrets in your environment.

For more information about Electron's secure storage behavior, see the `Electron safeStorage documentation <https://www.electronjs.org/docs/latest/api/safe-storage>`_.
