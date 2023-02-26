Office 365 Single Sign-On
=========================

.. include:: ../_static/badges/entpro-cloud-free.rst
  :start-after: :nosearch:

*Available in legacy Mattermost Enterprise Edition E20*

.. include:: common-sso-office365.rst
  :start-after: :nosearch:

Configure Mattermost ``config.json`` for Office 365 SSO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/entpro-cloud-free.rst
  :start-after: :nosearch:

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

3. Save your changes, then restart your Mattermost server. After the server restarts, users must change their login method before they can log in with Office 365.

Frequently Asked Questions
--------------------------

How can I use LDAP attributes or Groups with OpenID?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At this time, LDAP data isn't compatible with OpenID. If you currently rely on LDAP to manage your users' teams, channels, groups, or attributes, you won't be able to do this automatically with users who have logged in with OpenID. If you need LDAP synced to each user, we suggest using SAML or LDAP as the login provider. Some OpenID providers can use SAML instead, like Keycloak.