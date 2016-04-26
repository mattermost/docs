## Active Directory/LDAP Setup (Enterprise) 

### Enabling Active Directory/Lightweight Directory Access Protocol (AD/LDAP)

After installing Mattermost:

1. Create a team using email authentication    
    1. Log in using an account assigned to the “System Administrator” role. The first account you create on the server is automatically assigned this role. You may also assign the role to another account.    
    2. In the team site, go to **Main Menu** (the three dots at top left) > **System Console** > **LDAP Settings**     
    3. Fill in the fields to set up Mattermost authentication with your LDAP server.    
      - (Optional - _Available May 16, 2016_) Fill in the **User Filter** field to restrict Mattermost access to a subset of LDAP users. For example, to filter out disabled accounts in Active Directory enter `(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))`  
    4. After LDAP has been enabled, confirm that users can sign in using LDAP credentials. The **LDAP username** will be the attribute set in the **Id Attribute** field. 
  
    - Note: If you're using Active Directory with **nested security groups** you need to write a PowerShell script, or similar, to flatten and aggregate the tree into a single security group to map into Mattermost.  

2. (Optional) Change default Session Length for LDAP SSO     
    1. Go to **System Console** > **Service Settings** > **Session Length for SSO in days** to select the frequency with which users need to log into devices with LDAP credentials. Default is 30 days. 
  
    If a user attribute changes on the LDAP server it will be updated the next time the user enters their credentials to log in to Mattermost. This includes if a user is made inactive or removed from an LDAP server. The ability more quickly detect user attribute changes by polling the LDAP server as sessions start is planned for a future monthly release of Enterprise Edition. 

- Note: Organizations that run secured connections behind their firewalls can set up stunnel to port 389, the standard AD/LDAP port. The option to add TLS for LDAP is scheduled for May 16, 2016 release. 

### Restrict authentication to Active Directory/LDAP

1. Make sure your System Administrator authenticates with LDAP (see above instructions).    
2. Go to **System Console** > **Email Settings** and set **Allow Sign Up With Email** to `false`.    
3. Go to **System Console** > **Email Settings** and set **Allow Sign In With Email** to `false`.    

This should leave Active Directory/LDAP as the only single-sign-in option. If you've made a mistake you can [set an existing account to System Administrator using the commandline tool](http://docs.mattermost.com/deployment/on-boarding.html#creating-system-administrator-account-from-commandline). 

### Troubleshooting

The following are troubleshooting suggestions on common error messages and issues. 

##### `User not registered on LDAP server`

This means the query sent back to the Active Directory/LDAP server returned no results. 
- Check that you correctly entered Active Directory/LDAP user credentials (e.g. did not mix username with email).
- Check that the user account you're trying to use exists in the Active Directory/LDAP service.
- Check that your Active Directory/LDAP properties were propertly configured.  

##### "I updated a user account in LDAP, and they can no longer log in to Mattermost"

If the user can no longer log in to Mattermost with their LDAP credentials - for example, they get an error message `An account with that email already exists`, or a new Mattermost account is created when they try to log in - this means the ID attribute for their account has changed. 

The issue can be fixed by changing the value of the field used for the ID attribute back to the old value. 

Note: Currently the value is case sensitive. If the ID attribute is set to the username and the username changes from John.Smith to john.smith, the user would have problems logging in.   

### Switching System Administrator account to LDAP from email authentication 

A user interface supporting an easy switch from LDAP to email authentication will be available in the May 16, 2016 release. A manual process is currently offered: 

1. Create a new LDAP account to become the new System Administrator account     
    1. The new account should have a different email than the original System Administrator account. To change the email of the original System Administrator account go to **Main Menu** > **Account Settings** > **General** > **Email**.     
2. Promote your new LDAP account to System Administrator      
    1. Sign in with your original your email-based System Administrator account    
    2. Go to **System Console**> **Teams** > **[Team Name]** > **Users**, find your new LDAP user account and promote it to **System Administrator**. )     
3. Disable your original email-based System Administrator account      
    1. Sign in with your new LDAP-based System Administrator account     
    2. Go to **Teams** > **Team Name** > **Users**, and find your old email based System Administrator account and change it to **Inactive**.     

If you make a mistake in this process by deactivating your System Administrator account prematurely you can restore the role from [the commandline tool.](http://docs.mattermost.com/deployment/on-boarding.html#creating-system-administrator-account-from-commandline)
