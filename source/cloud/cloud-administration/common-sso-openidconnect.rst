Mattermost provides OpenID Connect support for `GitLab <https://docs.mattermost.com/cloud/cloud-administration/sso-gitlab.html>`__, `Google Apps <https://docs.mattermost.com/cloud/cloud-administration/sso-google.html>`__, and `Office 365 <https://docs.mattermost.com/cloud/cloud-administration/sso-office.html>`__. With OpenID Connect, users can also use their login to Keycloak, Atlassian Crowd, Apple, Microsoft, Salesforce, Auth0, Ory.sh, Facebook, Okta, OneLogin, and Azure AD, as well as others, as a Single Sign-on (SSO) service for team creation, account creation, and user sign-in.

Follow these steps to configure a service provider using OpenID Connect.

Step 1: Create an OpenID Connect Application
---------------------------------------------

1. Follow service provider documentation for creating an OpenID Connect application. Most OpenID Connect service providers require authorization of all redirect URIs.
2. In the appropriate field, enter ``{your-mattermost-url}/signup/openid/complete`` For example: ``http://domain.com/signup/openid/complete``
3. Copy and paste values for the **Discovery Endpoint**, **Client ID**, and **Client Secret** values to a temporary location. You will enter these values when you configure Mattermost.

Step 2: Configure Mattermost for an OpenID Connect SSO
-------------------------------------------------------

1. Log in to Mattermost, then go to **System Console > Authentication > OpenID Connect**.
2. Select **OpenID Connect (Other)** as the service provider.
3. Enter the **Discovery Endpoint**.
4. Enter the **Client ID**.
5. Enter the **Client Secret**.
6. Specify a **Button Name** and **Button Color** for the OpenID Connect option on the Mattermost login page.
7. Select **Save**.
8. Restart your Mattermost server to see the changes take effect.

.. note::
  When Mattermost is configured to use OpenID Connect for user authentication, the following user attribute changes can't be made through the Mattermost API: first name, last name, or username. OpenID Connect must be the authoritative source for these user attributes.
