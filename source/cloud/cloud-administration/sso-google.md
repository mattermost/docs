# Google Single Sign-On

## Migrating from OAuth 2.0 to OpenID Connect

OAuth 2.0 is being deprecated and replaced by OpenID Connect. Refer to the product documentation to [convert your existing OAuth configuration] for Google Apps to the new OpenID Connect standard.

## Configuring Google Apps as a Single Sign-On (SSO) service

Follow these steps to configure Mattermost to use Google as a Single Sign-on (SSO) service for team creation, account creation, and sign-in.

**Note:** The [Google People API](https://developers.google.com/people) has replaced the Google+ API, which was deprecated by Google as of March 7th, 2019 [per their notice](https://developers.google.com/+/api-shutdown).

### Step 1: Create an OpenID Connect project in Google API Manager

1. Go to [Google API Manager](https://console.developers.google.com).

2. Select **Credentials** in the left hand sidebar, then select **Create a project**.

3. Enter "Mattermost - your-company-name" as the **Project Name**, then select **Create**.

![](../../../source/images/google_1_credentials.png)

### Step 2: Enable APIs and Services

1. In the **Dashboard** select the option to **ENABLE APIS AND SERVICES**.

2. In the API Library, scroll down to [Google People API](https://console.developers.google.com/apis/api/plus/overview), then select **Enable** in the header. This might take a few minutes to propagate through Google's systems.

![](../../../source/images/google_enable_api.png)

### Step 3: Add Mattermost as an authorized domain

1. Leave the **Google+ API menu** to return to the **APIs & Services menu**. 

2. In the left-hand sidebar, select **Credentials**, select the **OAuth consent screen** header, enter "Mattermost" as the **Application Name**, then select **Save**.

3. Scroll further down to add your Mattermost instance to a list of authorized domains that can access the API. For example, if it is hosted on `mattermost.yourdomain.com` add `yourdomain.com`.

4. Select **Credentials** and select **Create credentials**, then choose **OAuth client ID** from the drop-down list.

5. Select **Web Application** as the **Application type**, and choose a descriptive **Name** for the OAuth connection.

6. Under **Restrictions > Authorized redirect URIs**, enter `your-mattermost-url/signup/google/complete` (example: `http://localhost:8065/signup/google/complete`), then select **Create**.

7. Copy and paste the **Client ID** and **Client Secret** values to a temporary location. You will enter these values in the Mattermost System Console.

![](../../../source/images/google_3_oauth_consent_screen.png)

![](../../../source/images/google_authorised_domains.png)

![](../../../source/images/google_3_oauth_client_id.png)

![](../../../source/images/google_4_web_app.png)

![](../../../source/images/google_5_client_id_secret.PNG)

### Step 4: Configure Mattermost for Google Apps SSO

1. Log in to Mattermost, then go to the **System Console > Authentication > OpenID Connect**.

2. Select **Google Apps** as the service provider.

3. The **Discovery Endpoint** for OpenID Connect with Google Apps is prepopulated with ``https://accounts.google.com/.well-known/openid-configuration``.

3. Paste in the **Client ID** from Google in Mattermost.

3. Paste in the **Client Secret** from Google in Mattermost.

4. Select **Save**.

5. Restart your Mattermost server to see the changes take effect.

**Note:**
- Alternatively, you may enter **Client ID** and **Client Secret** values directly into the `GoogleSettings` section of the Mattermost `config/config.json` file.
- The following default values are recommended:
    - `Scope`: `profile email`
    - `AuthEndpoint`: `https://accounts.google.com/o/oauth2/v2/auth`
    - `TokenEndpoint`: `https://www.googleapis.com/oauth2/v4/token`
