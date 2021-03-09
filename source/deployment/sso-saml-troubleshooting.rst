Troubleshooting
---------------

The following are troubleshooting suggestions on common error messages and issues.

1. Unable to switch to SAML authentication successfully

  First, ensure you have installed the `XML Security Library <https://www.aleksey.com/xmlsec/download.html>`__ on your Mattermost instance and that **it is available in your** PATH.

  Second, ensure you have completed each step of the SAML configuration.

If you are still having trouble with configuration, see further troubleshooting notes below or feel free to post in our `Troubleshooting forum <https://mattermost.org/troubleshoot/>`__ and we'll be happy to help with issues during setup.

2. System Administrator locks themselves out of the system

  If the System Administrator is locked out of the system during SAML configuration process, they can set an existing account to System Administrator using `a command line tool <https://docs.mattermost.com/deployment/on-boarding.html#creating-system-administrator-account-from-commandline>`__.

3. Received error message: `An account with that username already exists. Please contact your Administrator.`

  This usually means an existing account has another authentication method enabled. If so, the user should sign in using that method (such as email and password), then change their sign-in method to SAML via **Account Settings > Security > Sign-in method**.

  This error message can also be received if the `Username Attribute` of their SAML credentials doesn't match the username of their Mattermost account. If so, the user can update the attribute at their identity provider (for instance, back to the old value if it had been previously updated).

4. Received error message: `An account with that email already exists. Please contact your Administrator.`

  This usually means an existing account has another authentication method enabled. If so, the user should sign in using that method (such as email and password), then change their sign-in method to SAML via **Account Settings > Security > Sign-in method**.

  This error message can also be received if the `Email Attribute` of their SAML credentials doesn't match the email address of their Mattermost account. If so, the user can update the attribute at their identity provider (for instance, back to the old value if it had been previously updated).

5. Received error message: `SAML login was unsuccessful because one of the attributes is incorrect. Please contact your System Administrator.`

  Confirm all attributes, including `Email Attribute` and `Username Attribute`, are correct in both the Identity Provider configuration and in **System Console > SAML**.
