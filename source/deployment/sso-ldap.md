## Active Directory/LDAP Setup

_Available in Enterprise Edition E10 & E20_

### Overview

Active Directory/LDAP integration offers the following benefits:

- **Single sign-on.** Users can sign-in to Mattermost with their AD/LDAP credentials.
- **Centralized identity management.** Mattermost accounts can display user information from AD/LDAP, such as first and last name, email and username.
- **Automatic account provisioning.** New Mattermost user accounts are automatically created the first time a user signs in with their AD/LDAP credentials on the Mattermost server.

### Pre-installation notes

- If you're using Active Directory with **nested security groups** you need to write a PowerShell script, or similar, to flatten and aggregate the tree into a single security group to map into Mattermost.   

### Getting started

There are two ways to setup AD/LDAP:

1. **Configure AD/LDAP using the System Console user interface**
     - Start the Mattermost server and create a new account using email and password, which is assigned the System Administrator role as the first user created, then configure AD/LDAP and then convert your System Administrator account to use the AD/LDAP sign-in method.
2. **Configure AD/LDAP by editing `config.json`**
     - Before starting the Mattermost server, edit `config.json` to enable AD/LDAP based on [AD/LDAP settings documentation](http://docs.mattermost.com/administration/config-settings.html#ad-ldap). When you start the Mattermost server the first user to log in with valid AD/LDAP credentials will be assigned the System Administrator role.

#### Configure AD/LDAP sign-in

After installing Mattermost:

1. Create a System Administrator account using email authentication. On a new server create an account using email and password, which is automatically assigned the **System Administrator** role since it is the first account created. You may also assign the role to another account.    

2. Configure AD/LDAP. Go to **System Console > AD/LDAP** and fill in AD/LDAP settings based on [configuration settings documentation](http://docs.mattermost.com/administration/config-settings.html#ad-ldap)    

3. Confirm AD/LDAP sign-on is enabled.  After AD/LDAP has been enabled, confirm that users can sign in using AD/LDAP credentials.

4. Switch your System Administrator account from email to AD/LDAP authentication. Go to **Account Settings** > **Security** > **Sign-in Method** > **Switch to AD/LDAP** and sign-in with your AD/LDAP credentials to complete the switch.

5. (Optional) Restrict authentication to AD/LDAP. Go to **System Console** > **Authentication** > **Email** and set **Allow Sign Up With Email** to `false` and **Allow Sign In With Email** to `false`. This should leave Active Directory/LDAP as the only single sign-in option.

6. (Optional) If you configured First Name Attribute and Last Name Attribute in the System Console, go to **System Console > General > Users and Teams** and set **Teammate Name Display** to *Show first and last name*. This is recommended for a better user experience.

If you've made a mistake and lock yourself out of the system somehow, you can [set an existing account to System Administrator using the commandline tool](http://docs.mattermost.com/deployment/on-boarding.html#common-tasks).

#### Configure AD/LDAP synchronization

In addition to configuring AD/LDAP sign-in, you can also configure AD/LDAP synchronization. When synchronizing, Mattermost queries AD/LDAP for relevant account information and updates Mattermost accounts based on changes to attributes (first name, last name, and nickname). When accounts are disabled in AD/LDAP users are made inactive in Mattermost, and their active sessions are revoked once Mattermost synchronizes attributes.

Note that the AD/LDAP sync depends on email. Make sure all users on your AD/LDAP server have an email address or that their account is deactivated in Mattermost. 

To configure AD/LDAP synchronization with AD/LDAP sign-in:

1. Go to **System Console > AD/LDAP** and set **Enable Synchronization with AD/LDAP** to `true`.
2. Set **Syncronization Interval** to specify how often Mattermost accounts synchronize attributes with AD/LDAP. The default setting is 60 minutes.

If you want to synchronize immediately after disabling an account, use the "AD/LDAP Synchronize Now" button in **System Console > AD/LDAP**.

To configure AD/LDAP synchronization with SAML sign-in, see the [SAML documentation](https://about.mattermost.com/default-saml-ldap-sync).

#### Configure AD/LDAP deployments with multiple domains

Organizations using multiple domains can integrate with Mattermost using a "Forest" configuration to bring together multiple domains. Please see [Forests as Collections of Domain Controllers that Trust Each Other](https://technet.microsoft.com/en-us/library/cc759073%28v=ws.10%29.aspx?f=255&MSPPError=-2147217396) for more information.

For forest configurations that contain multiple domains which do NOT share a common root, you can search across all of the domains using the Global Catalog. To do so, update your config.json as follows:

1. Set the LdapPort to 3268 (instead of 389)
2. Set the BaseDN to " " (A single space character)

See [Global Catalog and LDAP Searches](https://technet.microsoft.com/en-us/library/cc978012.aspx) for additional details.

#### Pulling additional user attributes

You can use a pre-packaged Mattermost plugin to pull additional user attributes from your AD/LDAP.

**This endpoint only requires a valid session and no other permissions. Only non-confidential AD/LDAP fields should be exposed.**

1. Configure the LdapServer, LdapPort, BaseDN, BindUsername, BindPassword, UserFilter and IdAttribute fields under LdapSettings in config.json. 
  - When using SAML SSO, the IdAttribute must be the email field in LDAP that is mapped to the user in SAML.

2. Add the plugin configuration under PluginSettings.Plugins in config.json. The list under “Attributes” will specify which AD/LDAP attributes the API endpoint pulls.

```
"PluginSettings": {
    “Enable”: true,
    "Plugins": {
        "ldapextras": {
            "Enabled": true,
            "Attributes": ["attribute1", "attribute2"]
        }
    }
}
```

3. Restart the Mattermost server.
4. To confirm the plugin works, perform an HTTP GET against your-mattermost-url.com/plugins/ldapextras/users/{user_id}/attributes which will return a JSON object with attribute names as keys with the appropriate values.

### Troubleshooting / FAQ

The following are frequently asked questions and troubleshooting suggestions on common error messages and issues.

#### If "AD/LDAP Test" button fails, how can I troubleshoot the connection? 

1. Check that your AD/LDAP connection settings are correct by running an AD/LDAP user query in an external system. See [LDAP Connection Test Example](http://ldaptool.sourceforge.net).  

If the AD/LDAP connection is verified to be working out side of Mattermost, try the following: 

2. Check your AD/LDAP system to verify your `Bind Username` format.

3. Check your `AD/LDAP Port` and `Connection Security` settings. (`AD/LDAP Port` set to `389` typically uses `Connection Security` set to `None`. `AD/LDAP Port` set to `636` typically ties to `Connection Security` set to `TLS`). 

If these options don't work, please contact Mattermost support via the email address that came with your license key. 

##### When I first set up and synchronize AD/LDAP, are the users automatically created in Mattermost? 

No, each user is created on their first login. 

##### When I try to synchronize AD/LDAP, why does the Status show as ``Pending`` and not complete? 

Go to **System Console > AD/LDAP** and make sure that the **Enable Synchronization with AD/LDAP** setting is set to ``true``.  If the issue persists, try performing a sync with the **User Filter** field blank. If the sync completes in this scenario, then the general syntax was formatted incorrectly. Refer to this [document](https://docs.mattermost.com/administration/config-settings.html#user-filter) for guidance on setting a correct syntax format.

##### If I want to add people to channels, can I pre-create users somehow? 

Yes, using the [bulk import tool](https://docs.mattermost.com/deployment/bulk-loading.html#bulk-loading-data).

##### How does deactivating users work? 

When AD/LDAP authentication is used in Mattermost, user deactivation must be done via the AD/LDAP server. 

There are two main ways to do this: 

1. User Deletion: If the user is completely removed from the AD/LDAP server, they will be deactivated in Mattermost on the next synchronization. 
2. User Filter: Set the [user filter](https://docs.mattermost.com/administration/config-settings.html#user-filter) to only select the subset of AD/LDAP users you want to have access to Mattermost. When someone is removed from the selected group, they will be deactivated in Mattermost on the next synchronization. 

For Active Directory, to filter out deactivated users you must set the user filter to `(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))`.  

##### Can I connect to multiple Active Directory servers? 

There is currently no built-in way to connect to multiple AD servers. You will need to connect the instances in a forest before connecting to Mattermost.

Consider upvoting the [feature request](https://mattermost.uservoice.com/forums/306457-general/suggestions/13589904-add-the-abilitiry) on our forum.

##### When trying to sign in, I see the error `AD/LDAP not available on this server`

This indicates that there is a problem somewhere with your configuration. We recommend that you: 
1. Confirm Enterprise Edition is installed
2. Check your license to confirm it's uploaded and not expired 
3. Check your Mattermost configuration settings to ensure that AD/LDAP is enabled, and the settings are correct

If you are still having issues, you can [contact support](https://about.mattermost.com/support/) for additional troubleshooting. 

##### I see the error `User not registered on AD/LDAP server`

This means the query sent back to the Active Directory/LDAP server returned no results. We recommend that you: 
1. Check that the user credentials were entered properly - you should login with the field set as the [`ID Attribute`](https://docs.mattermost.com/administration/config-settings.html#id-attribute)
2. Check that the user account exists in the Active Directory/LDAP server
3. Check the Active Directory/LDAP configuration settings are correct 

If you are still having issues, you can [contact support](https://about.mattermost.com/support/) for additional troubleshooting. 

##### I updated a user account in AD/LDAP, and they can no longer log in to Mattermost

If the user can no longer log in to Mattermost with their AD/LDAP credentials - for example, they get an error message `An account with that email already exists`, or a new Mattermost account is created when they try to log in - this means the ID attribute for their account has changed.

The issue can be fixed by changing the value of the field used for the ID attribute back to the old value.

Note: Currently the value is case sensitive. If the ID attribute is set to the username and the username changes from `John.Smith` to `john.smith`, the user would have problems logging in.   

##### I see the log error `LDAP Result Code 4 "Size Limit Exceeded"`

This indicates your AD/LDAP server configuration has a maximum page size set and the query coming from Mattermost is returning a result set in excess of that limit.

To address this issue you can set the [max page size](https://docs.mattermost.com/administration/config-settings.html#maximum-page-size) in your Mattermost configuration to match the limit on your AD/LDAP server. This will return a sequence of result sets that do not exceed the max page size, rather than returning all results in a single query.

##### Where can I find help on AD/LDAP configuration settings in config.json?

You can find an explanation of each of the configuration settings [here](https://docs.mattermost.com/administration/config-settings.html#ad-ldap).

##### Can the AD/LDAP User Filter read Security groups?

Yes it can, but make sure that:
 - permissions are correctly configured on the service account you are using
 - each user object is a direct member of the security group
