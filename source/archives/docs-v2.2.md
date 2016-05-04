# v2.2 Documentation
_____

## Signing in

You can sign in to your team from the web address of `https://domain.com/teamname`. 

### Sign In Methods
There are several options for signing in to your team depending on how your System Admin has configured your server. 

#### Email Address or Username Sign In  

When enabled by your System Admin, you can sign in with the username or email address used to create your account.

If you have forgotten your password, you can reset it by clicking **I forgot my password** on the sign in screen, or contact your System Admin for help resetting your password. 

#### GitLab Single-Sign-On (SSO)

When enabled by your System Admin, you can sign in using your GitLab account using a one-click sign in option. GitLab SSO lets you create teams, create accounts on teams, and sign in to teams using one username, email address, and password that works across everything on the server.  

### Switching Teams

When you've used the same email address to sign up and sign in to multiple teams, you can switch among those teams using the **Main Menu**, accessed by clicking the three dots in the top header of any team site on the server. By default, devices remember which teams you have signed into for 30 days.

### Logging Out

You can log out from the **Main Menu**, which is accessed by clicking the three dots in the top header on the left side of the screen. Clicking "Logout" logs you out of all teams that are signed in and open in your browser.

### iOS Setup

Your Mattermost teams can be accessed on iOS mobile devices by downloading the Mattermost App.

1. Open the App Store on your Apple device running iOS 9.0 or later.
2. Search for "Mattermost" and click **GET** to download the App for free.
3. Open Mattermost from your homescreen and input your team and account information to login:
    1. Enter Team URL: This is part of the web address that navigates to your team on the system domain. You can find the Team URL by asking your System Admin or looking at the address bar in a desktop browser tab with Mattermost open. It is in the form `https://domain.com/teamurl/`.
    2. Sign in to Mattermost: This is your account login information as decribed by one of the sign in methods above. 

---
    
## Creating Teams

New teams can be created if the System Admin has *Enable Team Creation* set to true from the System Console.

### Methods to Create a Team
Teams can be created from the main menu, system home page or team sign in page.

#### Main Menu
Click the **Three-Dot** menu in Mattermost, then select **Create a New Team**. If this option is not visible in the menu, then the System Admin has *Enable Team Creation* set to false.


#### System Home Page
Navigate to the web address of your system, `https://domain.com/`. Enter a valid email address and click **Create Team** to be guided through the rest of the set up steps. If this option is not visible on the web page, then the System Admin has *Enable Team Creation* set to false. It is not necessary to have an existing account on the system in order to create a team from the system home page.

#### Team Sign In Page
Navigate to the web address of your team, `https://domain.com/teamurl/`. If you are logged in, the web address will open Mattermost and you can create a new team from the main menu. If you are logged out, the web address will direct you to the sign in page where you can click **Create a New Team**. If this option is not visible on the web page, then the System Admin has *Enable Team Creation* set to false. It is not necessary to have an existing account on the system in order to create a team from the sign in page.

### Team Name and URL Selection
There are a few details and restrictions to consider when selecting a team name and team URL.

#### Team Name
This is the display name of your team that appears in menus and headings.

- It can contain any letters, numbers or symbols.
- It is case sensitive.
- It must be 4 - 15 characters in length.

#### Team URL
The team URL is part of the web address that navigates to your team on the system domain, `https://domain.com/teamurl/`. 

- It may contain only lowercase letters, numbers and dashes.
- It must start with a letter and cannot end in a dash.
- It must be 4 - 15 characters in length.

If the System Admin has *Restrict Team Names* set to true, the team URL cannot start with the following restricted words: www, web, admin, support, notify, test, demo, mail, team, channel, internal, localhost, dockerhost, stag, post, cluster, api, oauth.

### User Roles on Multiple Teams
Each user is distinct and owned by a team. A team creator is automatically granted Team Admin privileges for that team, even if they are a System Admin on another team. A System Admin with accounts on multiple teams must grant all their accounts *System Admin* privileges from the System Console. To do this, go to the **Main Menu > System Console**, then click **Users** under the *Teams* heading for the team you want to manage.

---

## Switching System Administrator account to LDAP from email authentication 

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

---

## Team Settings  

The Team Settings menu offers Team Administrators, Team Owners and System Administrators the ability to adjust settings applied to a specific team. 

The following settings are found in a Team Site from the **Three-Dot** menu at the top of the left sidebar under **Team Settings**. 

### General  

General settings under the **Team Settings** > **General** configure how a team is displayed to users. 

#### Team Name

Your **Team Name** is displayed on the sign-in page, and in the top of the left-hand sidebar for your team. 

#### Allow anyone to sign-up from login page

Setting this option to **Yes** shows a link to the account creation page on the sign-in page of this team. 

Team Administrators would set this to **Yes** when they:  
 1. Operate on a closed network and want to make sign-up easy.  
 2. Operate on the open internet with sign-up restricted to specific domains, and want to allow easy sign-up from users with email addresses. Note: System Administrators can restrict sign-up to specific domains via the System Console.  
 3. Operate on the open internet and want to allow anyone to sign-up.

Team Administrators would set this to **No** when they:  
 1. Operate on the open internet and want a small, private team that is email-invite-only.

#### Include this team in the Team Directory

Setting this option to **Yes** includes the Team Name on the Home Page and a link to this team's sign-in page. 

Team Administrators would set this to **Yes** when they:  
 1. Operate on a closed network and want to make it easy to discover their team from the Home Page of the Mattermost server.
 2. Operate on the open internet with sign-up restricted to specific domains, and want to allow easy sign-up from users with email addresses. Note: System Administrators can restrict sign-up to specific domains via the System Console.  
 3. Operate on the open internet and want to allow anyone to sign-up to their team from the Home Page of the Mattermost server.

Team Administrators would set this to **No** when they:  
 1. Operate on the open internet and want a small, private team that is email-invite-only.

System Administrators may choose to disable the Team Directory for their entire system by settings **System Console** > **Team Settings** > **Enable Team Directory** to false.

#### Invite Code 

The **Invite Code** is used as part of the URL in the team invitation link retrieved from the **Main Menu** > **Get Team Invite Link**. Click **Re-Generate** and then **Save** to generate a new team invitation link and invalidate the previous link.

### Import

#### Import from Slack (Beta) 

*Note: As a proprietary SaaS service, Slack is able to change its export format quickly and without notice. If you encounter issues not mentioned in the documentation below, please alert the product team by [filing an issue](https://github.com/mattermost/platform/issues).*

The Slack Import feature in Mattermost is in "Beta" and focus is on supporting migration of teams of less than 100 registered users. To use: 

1. Generate a Slack "Export" file from **Slack > Team Settings > Import/Export Data > Export > Start Export**.  

2. In Mattermost go to **Team Settings > Import > Import from Slack**. _Team Owner_ or _Team Administrator_ role is required to access this menu option.

3. Click **Select file** to upload Slack export file and click **Import**.   

4. Emails and usernames from Slack are used to create new Mattermost accounts. 

5. Slack users can activate their new Mattermost accounts by using Mattermost's Password Reset screen with their email addresses from Slack to set new passwords for their Mattermost accounts.  

6. Once logged in, the Mattermost users will have access to previous Slack messages in the public channels imported from Slack.

**It is highly recommended that you test Slack import before applying it to an instance intended for production.** If you use Docker, you can spin up a test instance in one line (`docker run --name mattermost-dev -d --publish 8065:80 mattermost/platform`). If you don't use Docker, there are [step-by-step instructions](../../install/docker-ebs.md) to install Mattermost in preview mode in less than 5 minutes.

#### Limitations 

- Users are not automatically added to channels or groups when importing from Slack.
- Newly added markdown support in Slack's Posts 2.0 feature announced on September 28, 2015 is not yet supported.
- Slack does not export files or images your team has stored in Slack's database. Mattermost will provide links to the location of your assets in Slack's web UI.
- Slack does not export any content from private groups or direct messages that your team has stored in Slack's database. 
- In Beta, Slack accounts with usernames or email addresses identical to existing Mattermost accounts will not import and mentions do not resolve as Mattermost usernames (still shows Slack ID). No pre-check or roll-back is currently offered. 
