Signing in
==========

--------------

To sign in, navigate to the Mattermost sign-in page. You can get the URL of the sign-in page from your administrator. 

After signing in, the team that appears first on your team sidebar will open.  If you have not joined a team, the Team Selection 
page opens where you can view a list of teams that you can join.

Sign In Methods
---------------

There are several options for signing in to your team depending on how
your System Admin has configured your server.

Email Address or Username Sign In
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When enabled by your System Admin, you can sign in with the username or
email address used to create your account.

If you have forgotten your password, you can reset it by clicking **I
forgot my password** on the sign in screen, or contact your System Admin
for help resetting your password.

GitLab Single-Sign-On (SSO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When enabled by your System Admin, you can sign in using your GitLab
account using a one-click sign in option.

Google Single-Sign-On
~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E20*

When enabled by your System Admin, you can sign in using your Google
account using a one-click sign in option.

Office 365 Single-Sign-On (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E20*

When enabled by your System Admin, you can sign in using your Office 365
account using a one-click sign in option.

AD/LDAP Sign In
~~~~~~~~~~~~~~~
*Available in Enterprise Edition E10 & E20*

When enabled by your System Admin, you can sign in with your AD/LDAP
credentials. This lets you use the same username and password for
Mattermost that you use for various other company services.

SAML Single-Sign-On (SSO)
~~~~~~~~~~~~~~~~~~~~~~~~~
*Available in Enterprise Edition E20*

When enabled by your System Admin, you can sign in with your SAML
credentials. This lets you use the same username and password for
Mattermost that you use for various other company services. Mattermost
officially supports `Okta`_ and `Microsoft ADFS`_ as an identity
provider (IDP) for SAML, but you may use other SAML IDPs as well. Please
see `documentation`_ to learn more about configuring SAML for
Mattermost.

Switching Teams
---------------

You can switch between teams you have joined using the team sidebar 
that appears left of your channel list on the left-hand sidebar.

.. image:: ../../images/team-sidebar.png

Logging Out
-----------

You can log out from the **Main Menu**, which is accessed by clicking
the three dots in the top header on the left side of the screen.
Clicking **Logout** logs you out of all teams on the server.

iOS Setup
---------

Your Mattermost teams can be accessed on iOS mobile devices by
downloading the Mattermost App.

#. Open the `App Store` on your Apple device running iOS 9.0 or later.
#. Search for “Mattermost” and click **GET** to download the App for
   free.
#. Open Mattermost from your homescreen and input your team and account
   information to login:

   #. Enter Server URL: This is the web address you go to when you want
      to access Mattermost. You can find the Server URL by asking your
      System Admin or by looking at the address bar in a desktop browser
      tab with Mattermost open. It is in the form
      ``https://domain.com``.
   #. Sign in to Mattermost: This is your account login information as
      described by one of the sign in methods above.

Android Setup
-------------

Your Mattermost teams can be accessed on Android mobile devices by
downloading the Mattermost App.

#. Open the `Google Play Store`_ on your Android device.
#. Search for “Mattermost” and click **INSTALL** to download the App for
   free.
#. Open Mattermost from your homescreen and input your team and account
   information to login:

   #. Enter Server URL: This is the web address you go to when you want
      to access Mattermost. You can find the Server URL by asking your
      System Admin or by looking at the address bar in a desktop browser
      tab with Mattermost open. It is in the form
      ``https://domain.com``.
   #. Sign in to Mattermost: This is your account login information as
      described by one of the sign in methods above.

.. _Okta: http://developer.okta.com/docs/guides/saml_guidance.html
.. _Microsoft ADFS: https://msdn.microsoft.com/en-us/library/bb897402.aspx
.. _documentation: http://docs.mattermost.com/deployment/sso-saml.html
.. _App Store: https://geo.itunes.apple.com/us/app/mattermost/id984966508?mt=8
.. _Google Play Store: https://play.google.com/store/apps/details?id=com.mattermost.mattermost&hl=en
