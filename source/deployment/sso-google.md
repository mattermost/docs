# Google Single-Sign-On (E20) 
___

Follow these steps to configure Mattermost to use Google as a single-sign-on (SSO) service for team creation, account creation and sign-in.

1 - [Log in](https://accounts.google.com/login) to your Google account.

2 - Go to [Google API Manager](https://console.developers.google.com), click **Credentials** in the left hand sidebar, click **Create a project** and enter "Mattermost - your-company-name" as the **Project Name**, then click **Create**.

![google_1_credentials](../../source/images/google_1_credentials.png)

3 - Click the **OAuth consent screen** header and enter "Mattermost" as the **Product name shown to users**, then click **Save**.

![google_2_oauth_consent_screen](../../source/images/google_2_oauth_consent_screen.png)

4 - Under the **Credentials** header, click **Create credentials**, choose **OAuth client ID** from the drop-down list.

![google_3_oauth_client_id](../../source/images/google_3_oauth_client_id.png)

5 - Select **Web Application** as the **Application type**, and choose a descriptive **Name** for the OAuth connection. 

Under **Restrictions** > **Authorized redirect URIs**, enter `your-mattermost-url/signup/google/complete` (example: `http://localhost:8065/signup/google/complete`). Click **Create**.

![google_4_web_app](../../source/images/google_4_web_app.png)

6 - Copy the **Client ID** and **Client Secret**, which will be used to configure Google SSO for Mattermost.

![google_5_client_id_secret](../../source/images/google_5_client_id_secret.PNG)

7 - Finally, go to [Google+ API](https://console.developers.google.com/apis/api/plus/overview) and click **Enable** in the header. This might take a few minutes to propagate through Google's systems.

8 - In **System Console > OAuth 2.0 > Select OAuth 2.0 service provider**, choose **Google Apps** as the service provider and enter **Client ID** and **Client Secret** from step 6 in their respective fields.

9 - Restart your Mattermost server to see the changes take effect.

Notes: 
- You may also enter **Client ID** and **Client Secret** fields from step 6 directly in `GoogleSettings` section of `config/config.json`.
- The following default values in `GoogleSettings` section of `config/config.json` are recommended:
    - `Scope`: `profile email`
    - `AuthEndpoint`: `https://accounts.google.com/o/oauth2/v2/auth` 
    - `TokenEndpoint`: `https://www.googleapis.com/oauth2/v4/token`  
    - `UserApiEndpoint`: `https://www.googleapis.com/plus/v1/people/me`  
