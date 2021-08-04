Google Single Sign-On (E20)
===========================

Available in `Enterprise Edition E20 <https://mattermost.com/pricing-self-managed/>`__.

.. include:: common-sso-google.rst

Configure Mattermost ``config.json`` for Google Apps SSO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of using the System Console, you can add the Google settings directly to the ``config.json`` file directly on your Mattermost server.

1. Open ``config.json`` as *root* in a text editor. It’s usually in ``/opt/mattermost/config``, but it might be elsewhere on your system.
2. Locate the ``GoogleSettings`` section, then add or update the following information:

.. code-block:: text

  "Enable": true,
        "Secret": "P-k9R-7E7ayX9LdddddWdXVg",
        "Id": "1022ddddd5846-bkddddd4a1ddddd9d88j1kb6eqc.apps.googleusercontent.com",
        "Scope": "profile openid email",
        "AuthEndpoint": "",
        "TokenEndpoint": "",
        "UserApiEndpoint": "",
        "DiscoveryEndpoint": "https://accounts.google.com/.well-known/openid-configuration",
        "ButtonText": "",
        "ButtonColor": ""
  }

3. Save your changes, then restart your Mattermost server. After the server restarts, users must change their sign-in method before they can sign in with Google Apps.
