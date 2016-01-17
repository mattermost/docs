# Troubleshooting

#### Important notes

##### **DO NOT manipulate the Mattermost database**
  - In particular, DO NOT delete data from the database, as Mattermost is designed to stop working if data integrity has been compromised. The system is designed to archive content continously and generally assumes data is never deleted. 


#### Common Issues 

##### Lost System Administrator account
  - If the System Administrator account becomes unavailable, a person leaving the organization for example, you can set a new system admin from the commandline using `./platform -assign_role -team_name="yourteam" -email="you@example.com" -role="system_admin"`. 
  - After assigning the role the user needs to log out and log back in before the System Administrator role is applied.

##### Switching System Administrator Account to SSO Sign-in

When Mattermost is initially set up, the first account created becomes the System Administrator account. This account will typically use email authentication to sign-in, since it is usually created before other sign-in methods are configured. 

After setting up SSO authentication, it is common for the System Administrator to want to turn off email sign-in so users will only have SSO as a sign-in option. 

Before doing this, the System Administrator needs to change their sign-in method to SSO by doing the following:  
  1. Sign in to Mattermost using email and password
  2. Go to Account Settings > Security > Sign-in Method
  3. Click the "Switch" button for the sign in method you would like to use, and complete the process for switching sign-in method.
  
The System Administrator can now turn off email sign-in and still access their account. (To avoid locking other existing users out of their accounts, it is recommended the System Administrator ask them to switch authentication methods as well.)

##### Locked out of System Administrator account
If email sign-in was turned off before the System Administrator switched sign-in methods, sign up for a new account and promote it to System Administrator from the command line. 

#### Mattermost Error Messages

The following is a list of common error messages and solutions: 

###### `Please check connection, Mattermost unreachable. If issue persists, ask administrator to check WebSocket port.`
- Message appears in blue bar on team site. 
- **Solution:** Check that [your websocket port is properly configured](https://github.com/mattermost/platform/blob/master/doc/install/Production-Ubuntu.md#set-up-nginx-server). 


###### `x509: certificate signed by unknown authority` in server logs when attempting to sign-up
  - This error may appear when attempt to use a self-signed certificate to setup SSL, which is not yet supported by Mattermost. 
  - **Solution:** Set up a load balancer like Ngnix [per production install guide](https://github.com/mattermost/platform/blob/master/doc/install/Production-Ubuntu.md#set-up-nginx-with-ssl-recommended). A ticket exists to [add support for self-signed certificates in future](x509: certificate signed by unknown authority). 

###### `panic: runtime error: invalid memory address or nil pointer dereference`
 - This error can occur if you have manually manipulated the Mattermost database, typically with deletions. Mattermost is designed to serve as a searchable archive, and manual manipulation of the database elements compromises integrity and may prevent upgrade. 
 - **Solution:** Restore from database backup created prior to manual database updates, or reinstall the system.

###### `We couldn't find an existing account matching your email address for this team. This team may require an invite from the team owner to join.`
- This error appears when a user tries to sign in, and Mattermost can't find an account matching the credentials they entered.
- **Solution:**

  1. **If you're signing in with email and have previously created an account:**
    1. Check that you are using the correct email address. If you can't remember what email address was used, contact the System Administrator for assistance.

  2. **If you haven't signed up for an account on this team yet:**
    1. Click the link at the bottom of the sign-in page that says “Don't have an account? Create one now” to create an account. If the link is not available, contact a Team or System Administrator for an invitation.

  3. **If your account uses a different sign-in method** (for example, the account was created with email but the user is trying to use SSO to sign in):
    1. Check the sign-in page.
    2. If the sign-in method the account was created with is available, use that to sign in. 
      - *Note: You may then switch authentication methods from Account Settings > Security > Sign-in Method.* 
    3. If the sign-in method is not available, contact the System Administrator.
      - This can happen if the site was originally set up to allow an account to be created using either GitLab or Email, but then the System Administrator turned one of the options off.
      - The System Administrator can fix this issue by:
          1. Turning the sign-in option back on.
          2. Asking the user to switch sign-in methods before turning the sign-in option back off.

### Troubleshooting GitLab Mattermost

- If you're having issues installing GitLab Mattermost with GitLab Omnibus, as a first step please turn on logging by updating the [log settings](https://github.com/mattermost/platform/blob/master/doc/install/Configuration-Settings.md#log-file-settings) section in your `config.json` file installed by omnibus, and they try a general web search for the error message you receive. 

#### GitLab Mattermost Error Messages

###### `We received an unexpected status code from the server (200)`

- If you have upgraded from a pre-released version of GitLab Mattermost or if an unforseen issue has arrisen during the [upgrade procedure](https://github.com/mattermost/platform/blob/master/doc/install/Upgrade-Guide.md), you may be able to restore Mattermost using the following procedure: 
  - `sudo stop mattermost`, so DB can be dropped 
  - `sudo gitlab-ctl reconfigure`
  - `sudo -u gitlab-psql /opt/gitlab/embedded/bin/dropdb -h /var/opt/gitlab/postgresql mattermost_production`
  - `sudo start mattermost`
  - `sudo gitlab-ctl reconfigure`
  - [Manually set up GitLab SSO](https://github.com/mattermost/platform/blob/master/doc/integrations/Single-Sign-On/Gitlab.md) by copying Secret and ID into `/var/opt/gitlab/mattermost/config.json` 
  - `sudo gitlab-ctl restart`

###### `Token request failed`
 - This error can appear in the web browser after attempting to create a new team with GitLab SSO enabled
 - **Solutions:** 
   1. Check that your SSL settings for the SSO provider match the `http://` or `https://` choice selected in `config.json` under `GitLabSettings`
   2. Follow steps 1 to 3 of the manual [GitLab SSO configuration procedure](https://github.com/mattermost/platform/blob/master/doc/integrations/Single-Sign-On/Gitlab.md) to confirm your `Secret` and `Id` settings in `config.json` match your GitLab settings, and if they don't, manually update `config.json` to the correct settings and see if this clears the issue. 
