Office 365 Single Sign-On (E20)
===============================

Available in `Enterprise Edition E20 <https://mattermost.com/pricing-self-managed/>`__.

.. include:: common-sso-office365.rst

Configure Mattermost ``config.json`` for Office 365 SSO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of using the System Console, you can add the Office 365 settings directly to the ``config.json`` file on your Mattermost server.

1. Open ``config.json`` as *root* in a text editor. It’s usually in ``/opt/mattermost/config`` but it might be elsewhere on your system.
2. Locate the ``Office365Settings`` section, then add or update the following information:

.. code-block:: text

  "Enable": false,
        "Secret": "i.hddd6Pu3--5dg~cRddddqOrBdd1a",
        "Id": "28ddd714-1f2f-4f9c-9486-90b8dddd27",
        "Scope": "profile openid email",
        "AuthEndpoint": "",
        "TokenEndpoint": "",
        "UserApiEndpoint": "",
        "DiscoveryEndpoint": "https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration",
        "DirectoryId": "common"
  }

3. Save your changes, then restart your Mattermost server. After the server restarts, users must change their sign-in method before they can sign in with Office 365.
