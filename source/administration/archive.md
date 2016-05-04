# v2.2 Documentation
----

## Signing in

You can sign in to your team from the web address of `https://domain.com/teamname`.  

## Switching Teams

When you've used the same email address to sign up and sign in to multiple teams, you can switch among those teams using the **Main Menu**, accessed by clicking the three dots in the top header of any team site on the server. By default, devices remember which teams you have signed into for 30 days.

## iOS Setup

Your Mattermost teams can be accessed on iOS mobile devices by downloading the Mattermost App.

1. Open the App Store on your Apple device running iOS 9.0 or later.
2. Search for "Mattermost" and click **GET** to download the App for free.
3. Open Mattermost from your homescreen and input your team and account information to login:
    1. Enter Team URL: This is part of the web address that navigates to your team on the system domain. You can find the Team URL by asking your System Admin or looking at the address bar in a desktop browser tab with Mattermost open. It is in the form `https://domain.com/teamurl/`.
    2. Sign in to Mattermost: This is your account login information as decribed by one of the sign in methods above. 
    
## Creating Teams

#### System Home Page
Navigate to the web address of your system, `https://domain.com/`. Enter a valid email address and click **Create Team** to be guided through the rest of the set up steps. If this option is not visible on the web page, then the System Admin has *Enable Team Creation* set to false. It is not necessary to have an existing account on the system in order to create a team from the system home page.

#### Team Sign In Page
Navigate to the web address of your team, `https://domain.com/teamurl/`. If you are logged in, the web address will open Mattermost and you can create a new team from the main menu. If you are logged out, the web address will direct you to the sign in page where you can click **Create a New Team**. If this option is not visible on the web page, then the System Admin has *Enable Team Creation* set to false. It is not necessary to have an existing account on the system in order to create a team from the sign in page.

## User Roles on Multiple Teams
Each user is distinct and owned by a team. A team creator is automatically granted Team Admin privileges for that team, even if they are a System Admin on another team. A System Admin with accounts on multiple teams must grant all their accounts *System Admin* privileges from the System Console. To do this, go to the **Main Menu > System Console**, then click **Users** under the *Teams* heading for the team you want to manage.

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
