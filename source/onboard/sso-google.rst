Google Single Sign-On
=====================

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Configuring Google Apps as a Single Sign-On (SSO) service
---------------------------------------------------------

Follow these steps to configure Mattermost to use Google as a Single Sign-on (SSO) service for team creation, account creation, and login.

.. note::

  The `Google People API <https://developers.google.com/people>`__ has replaced the Google+ API, which was deprecated by Google as of March 7th, 2019 `per their notice <https://developers.google.com/+/api-shutdown>`__.

Step 1: Create OpenID Connect project in Google API Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to `Google Cloud Platform <https://console.developers.google.com>`__.

2. Select **Credentials** in the left-hand sidebar.

3. Select **Create Credentials**, then select **OAuth client ID**.

4. Select the **Web application** as the application type.

5. Enter ``Mattermost-<your-company-name>`` as the **Name**, replacing ``<your-company-name>`` with the name of your organization.

6. Under **Authorized redirect URIs**, select **Add URL**, then enter ``{your-mattermost-url}/signup/google/complete``. For example: ``http://localhost:8065/signup/google/complete``.

7. Select **Create**.

8. Copy and paste the **Your Client ID** and **Your Client Secret** values to a temporary location. You will enter these values in the Mattermost System Console.

.. image:: /images/create-google-sso-credentials.png

.. image:: /images/select-google-sso-web-app.png

.. image:: /images/google-sso-web-app-name.png

.. image:: /images/google-sso-redirect-uri.png

.. image:: /images/google-sso-credentials.png

Step 2: Enable Google People API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to the `Google People API <https://console.developers.google.com/apis/api/plus/overview>`__, then select **Enable** in the header. This might take a few minutes to propagate through Google's systems.

Step 3: Configure Mattermost for Google Apps SSO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log in to Mattermost, then go to **System Console > Authentication > OpenID Connect**.

2. Select **Google Apps** as the service provider.

3. The **Discovery Endpoint** for OpenID Connect with Google Apps is prepopulated with ``https://accounts.google.com/.well-known/openid-configuration``.

4. Paste in the **Client ID** from Google in Mattermost.

5. Paste in the **Client Secret** from Google in Mattermost.

6. Select **Save**.

.. note::
  When Mattermost is configured to use OpenID Connect or OAuth 2.0 for user authentication, the following user attribute changes can't be made through the Mattermost API: first name, last name, or username. OpenID Connect or OAuth 2.0 must be the authoritative source for these user attributes.

Configure Mattermost ``config.json`` for Google Apps SSO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

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

3. Save your changes, then restart your Mattermost server. After the server restarts, users must change their login method before they can log in with Google Apps.

Frequently Asked Questions
--------------------------

How can I use LDAP attributes or Groups with OpenID?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At this time, LDAP data isn't compatible with OpenID. If you currently rely on LDAP to manage your users' teams, channels, groups, or attributes, you won't be able to do this automatically with users who have logged in with OpenID. If you need LDAP synced to each user, we suggest using SAML or LDAP as the login provider. Some OpenID providers can use SAML instead, like Keycloak.