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


