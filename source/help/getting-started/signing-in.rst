Signing in
==========

--------------

This documentation refers to Mattermost v3.0+. For v2.2, see `archived
documentation`_.

You can sign in to your team from the root page of your Mattermost site
``https://domain.com/``. After signing in, you will be able to view a
list of your teams and select which one to open.

Sign In Methods
---------------

There are several options for signing in to your team depending on how
your System Admin has configured your server.

Email Address or Username Sign In
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When enabled by your System Admin, you can sign in with the username or
email address used to create your account.

If you have forgotten your password, you can reset it by clicking **I
forgot my password** on the sign in screen, or contact your System Admin
for help resetting your password.

GitLab Single-Sign-On (SSO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When enabled by your System Admin, you can sign in using your GitLab
account using a one-click sign in option.

Google Single-Sign-On (`Enterprise Edition`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When enabled by your System Admin, you can sign in using your Google
account using a one-click sign in option.

Office 365 Single-Sign-On (Beta) (`Enterprise Edition`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When enabled by your System Admin, you can sign in using your Office 365
account using a one-click sign in option.

AD/LDAP Sign In (`Enterprise Edition`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When enabled by your System Admin, you can sign in with your AD/LDAP
credentials. This lets you use the same username and password for
Mattermost that you use for various other company services.

SAML Single-Sign-On (SSO) (`Enterprise Edition`_)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When enabled by your System Admin, you can sign in with your SAML
credentials. This lets you use the same username and password for
Mattermost that you use for various other company services. Mattermost
officially supports `Okta`_ and `Microsoft ADFS`_ as an identity
provider (IDP) for SAML, but you may use other SAML IDPs as well. Please
see `documentation`_ to learn more about configuring SAML for
Mattermost.

Switching Teams
---------------

You can switch between teams you have joined using the **Main Menu**,
accessed by clicking the three dots in the top header of any team site
on the server.

Logging Out
-----------

You can log out from the **Main Menu**, which is accessed by clicking
the three dots in the top header on the left side of the screen.
Clicking “Logout” logs you out of all teams that are signed in and open
in your browser.

iOS Setup
---------

Your Mattermost teams can be accessed on iOS mobile devices by
downloading the Mattermost App.

#. Open the [App Store](\ https://geo.itunes.apple.com/us/app/ma

.. _archived documentation: http://docs.mattermost.com/archives/docs-v2.2.html#signing-in
.. _Enterprise Edition: https://about.mattermost.com/pricing/
.. _Okta: http://developer.okta.com/docs/guides/saml_guidance.html
.. _Microsoft ADFS: https://msdn.microsoft.com/en-us/library/bb897402.aspx
.. _documentation: http://docs.mattermost.com/deployment/sso-saml.html
