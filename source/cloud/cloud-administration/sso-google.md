# Google Single Sign-On

## Migrating from OAuth 2.0 to OpenID Connect

OAuth 2.0 is being deprecated and replaced by OpenID Connect. Refer to the product documentation to [convert your existing OAuth configuration](https://docs.mattermost.com/cloud/cloud-administration/converting-oauth-2.0-to-openid-connect) for Google Apps to the new OpenID Connect standard.

## Configuring Google Apps as a Single Sign-On (SSO) service

Follow these steps to configure Mattermost to use Google as a Single Sign-on (SSO) service for team creation, account creation, and sign-in.

**Note:** The [Google People API](https://developers.google.com/people) has replaced the Google+ API, which was deprecated by Google as of March 7th, 2019 [per their notice](https://developers.google.com/+/api-shutdown).

### Step 1: Create OpenID Connect project in Google API Manager

1. Go to [Google API Manager](https://console.developers.google.com).

2. Select **Credentials** in the left-hand sidebar, then select **OAuth client ID**.

3. Under **Credentials**, select **Create credentials**.

4. Select the **Web application application** type.

5. Enter `Mattermost - your-company-name` as the **Name**, then select **Create**.

6. Under **Authorized redirect URIs, enter `{your-mattermost-url}/signup/google/complete`. For example: `http://localhost:8065/signup/google/complete`.

7. Copy and paste the **Client ID** and **Client Secret** values to a temporary location. You will enter these values in the Mattermost System Console.

### Step 2: Enable Google People API

Go to the [Google People API](https://console.developers.google.com/apis/api/plus/overview), then select **Enable** in the header. This might take a few minutes to propagate through Google's systems.

![](../../../source/images/google_enable_api.png)

### Step 3: Configure Mattermost for Google Apps SSO

1. Log in to Mattermost, then go to **System Console > Authentication > OpenID Connect**.

2. Select **Google Apps** as the service provider.

3. The **Discovery Endpoint** for OpenID Connect with Google Apps is prepopulated with ``https://accounts.google.com/.well-known/openid-configuration``.

3. Paste in the **Client ID** from Google in Mattermost.

3. Paste in the **Client Secret** from Google in Mattermost.

4. Select **Save**.

5. Restart your Mattermost server to see the changes take effect.

**Note:**
- Alternatively, you may enter **Client ID** and **Client Secret** values directly into the `GoogleSettings` section of the Mattermost `config/config.json` file.
- The following default values are recommended:

```
"GoogleSettings": {
        "Enable": false,
        "Secret": "fake_secret",
        "Id": "fake_id",
        "Scope": "profile openid email",
        "AuthEndpoint": "",
        "TokenEndpoint": "",
        "UserApiEndpoint": "",
        "DiscoveryEndpoint": "https://accounts.google.com/.well-known/openid-configuration",
        "ButtonText": "",
        "ButtonColor": ""
    },
    ```
