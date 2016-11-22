# Office 365 Single-Sign-On (E20)
___

Follow these steps to configure Mattermost to use Office 365 as a single-sign-on (SSO) service for team creation, account creation and sign-in.

**The system must be using SSL for use with Office365 as Microsoft only allows OAuth redirect URIs that are SSL enabled.**

1 - [Log in](https://login.microsoftonline.com/) to your Microsoft or Office 365 account. If you use Azure Active Directory, make sure it's the account on the [same tenant](https://docs.mattermost.com/deployment/sso-office.html#note-about-microsoft-active-directory-tenants) that you would like your users to log in with.

2 - Go to [Application Registration Portal](https://apps.dev.microsoft.com), click **Go to app list** > **Add an app** and use "Mattermost - your-company-name" as the **Application Name**.

![office_1_add_app](../../source/images/office_1_add_app.png)

3 - Under **Application Secrets**, click **Generate New Password** and copy it, as it will be used to configure Office 365 SSO for Mattermost.

![office_2_generate_password](../../source/images/office_2_generate_password.png)

4 - Under **Platforms**, click **Add Platform**, choose **Web** and enter `your-mattermost-url/signup/office365/complete` (example: `http://localhost:8065/signup/office365/complete`) under **Redirect URIs**. Also uncheck **Allow Implicit Flow**.

![office_3_platform](../../source/images/office_3_platform.png)

5 - Click **Save** and copy the **Application ID**.

![office_4_application_id](../../source/images/office_4_application_id.png)

6 - In **System Console > OAuth 2.0 > Select OAuth 2.0 service provider**, choose **Office 365 (Beta)** as the service provider and enter **Application ID** from step 5 and **Application Secret Password** from step 3 in their respective fields.

7 - Restart your Mattermost server to see the changes take effect.

You may also enter **Application ID** and **Application Secret Password** fields from steps 5 and 3 directly in `Office365Settings` section of `config/config.json`. Moreover, the following default values in `Office365Settings` section of `config/config.json` are recommended:
 - `Scope`: `User.Read`
 - `AuthEndpoint`: `https://login.microsoftonline.com/common/oauth2/v2.0/authorize` 
 - `TokenEndpoint`: `https://login.microsoftonline.com/common/oauth2/v2.0/token`  
 - `UserApiEndpoint`: `https://graph.microsoft.com/v1.0/me`  

### Note about Microsoft Active Directory Tenants

A Microsoft Active Directory (AD) tenant is a dedicated instance of Azure Active Directory (Azure AD) that you own and would have received when signing up for a Microsoft cloud service such as Azure or Office 365. Tenants are commonly used by organizations who want to store information about their users such as passwords, user profile data and permissions. You can learn more about [getting an Azure AD tenant here](https://docs.microsoft.com/en-us/azure/active-directory/active-directory-howto-tenant).

To allow your Azure AD users to sign in to Mattermost using Office 365 SSO, you must register Mattermost in the Microsoft Azure AD tenant that contains the users' information. The registration can be done from the [Microsoft Azure portal](https://manage.windowsazure.com/). The steps to register the Mattermost account in the tenant should be similar to those provided above, and you can find more information about [integrating apps with Azure AD here](https://azure.microsoft.com/en-us/documentation/articles/active-directory-integrating-applications/). 

If you don't register Mattermost in the Microsoft Azure AD tenant your organization uses, Office 365 SSO will likely fail for your users. 

If you're interested in configuring a multi-tenant Mattermost application, which allows access to users from several organizations, you can [find out more here](https://azure.microsoft.com/en-us/documentation/articles/active-directory-integrating-applications/#configuring-multi-tenant-applications).

Note that if you do not use Azure Active Directory, you may simply register Mattermost with your Office 365 or Azure account (either your personal, work or school account) and set up Office 365 SSO with Mattermost using the steps provided above.
