## Active Directory/LDAP Setup

_Available in Enterprise Edition E10 & E20_

### Overview 

Active Directory/LDAP integration offers the following benefits: 

- **Single-sign-on.** Users can sign-in to Mattermost with their AD/LDAP credentials.
- **Centralized identity management.** Mattermost accounts can display user information from AD/LDAP, such as first and last name, email and username.
- **Automatic account provisioning.** New Mattermost user accounts are automatically created the first time a user signs in with their AD/LDAP credentials on the Mattermost server. 

### Pre-installation notes

- If you're using Active Directory with **nested security groups** you need to write a PowerShell script, or similar, to flatten and aggregate the tree into a single security group to map into Mattermost.   

### Getting started

There are two ways to setup AD/LDAP: 

1. **Configure AD/LDAP using the System Console user interface**
     - Start the Mattermost server and create a new account using email and password, which is assigned the System Administrator role as the first user created, then configure AD/LDAP and then convert your System Administror account to use the AD/LDAP sign-in method.
2. **Configure AD/LDAP by editing `config.json`**
     - Before starting the Mattermost server, edit `config.json` to enable AD/LDAP based on [AD/LDAP settings documentation](http://docs.mattermost.com/administration/config-settings.html#ldap-settings-enterprise). When you start the Mattermost server the first user to log in with valid AD/LDAP credentials will be assigned the System Administrator role. 

#### Configure AD/LDAP using the System Console user interface 

After installing Mattermost:

1. **Create a System Administrator account using email authentication**. On a new server create an account using email and password, which is automatically assigned the **System Administrator** role since it is the first account created. You may also assign the role to another account.    

2. **Configure AD/LDAP**. Select **System Console** from the main screen, go to **AD/LDAP** and fill in AD/LDAP settings based on [configuration settings documentation](http://docs.mattermost.com/administration/config-settings.html#ldap-settings-enterprise)    

3. **Confirm AD/LDAP sign-on is enabled**.  After AD/LDAP has been enabled, confirm that users can sign in using AD/LDAP credentials. 

4. **Switch your System Administrator account from email to AD/LDAP authentication**. Go to **Account Settings** > **General** > **Sign-in Method** > **Switch to AD/LDAP** and sign-in with your AD/LDAP credentials to complete the switch. 

5. **(Optional) Restrict authentication to AD/LDAP**. Go to **System Console** > **Authentication** > **Email** and set **Allow Sign Up With Email** to `false` and **Allow Sign In With Email** to `false`. This should leave Active Directory/LDAP as the only single-sign-in option. 

If you've made a mistake and lock yourself out of the system somehow, you can [set an existing account to System Administrator using the commandline tool](http://docs.mattermost.com/deployment/on-boarding.html#creating-system-administrator-account-from-commandline). 

Notes: 
- Mattermost 3.0 checks AD/LDAP credentials at the time of sign-in and issues session tokens with configurable durations, defaulting to 30 days. If a shorter time intervals is required, this session length for SSO can be changed in **System Console** > **Security** > **Sessions**.
- Any user attributes updated in the AD/LDAP Server will be reflected in Mattermost when AD/LDAP Synchronization occurs. The time interval for synchronization can be set in the **System Console** > **Authentication** > **AD/LDAP** > **Syncronization Interval**.

#### Configure AD/LDAP deployments with multiple domains 

Organizations using multiple domains can integrate with Mattermost using a "Forest" configuration to bring together multiple domains. Please see [Forests as Collections of Domain Controllers that Trust Each Other](https://technet.microsoft.com/en-us/library/cc759073%28v=ws.10%29.aspx?f=255&MSPPError=-2147217396) for more information. 

### Troubleshooting

The following are troubleshooting suggestions on common error messages and issues. 

##### User not registered on AD/LDAP server

This means the query sent back to the Active Directory/LDAP server returned no results. 
- Check that you correctly entered Active Directory/LDAP user credentials (e.g. did not mix username with email).
- Check that the user account you're trying to use exists in the Active Directory/LDAP service.
- Check that your Active Directory/LDAP properties were propertly configured.  

##### "I updated a user account in AD/LDAP, and they can no longer log in to Mattermost"

If the user can no longer log in to Mattermost with their AD/LDAP credentials - for example, they get an error message `An account with that email already exists`, or a new Mattermost account is created when they try to log in - this means the ID attribute for their account has changed. 

The issue can be fixed by changing the value of the field used for the ID attribute back to the old value. 

Note: Currently the value is case sensitive. If the ID attribute is set to the username and the username changes from `John.Smith` to `john.smith`, the user would have problems logging in.   

##### System Log Error: LDAP Result Code 4 "Size Limit Exceeded" 

This indicates your AD/LDAP server configuration has a maximum page size set and the query coming from Mattermost is returning a result set in excess of that limit. 

To address this issue you can set the [max page size](https://docs.mattermost.com/administration/config-settings.html#maximum-page-size) for Mattermost's AD/LDAP configuration. This will return a sequence of result sets below the max page size set in AD/LDAP, rather than returning all results in a single query. 
