## Team Settings  
___ 

This documentation refers to Mattermost v3.0. For v2.2, see [archived documentation](http://docs.mattermost.com/archives/docs-v2.2.html#team-settings).

The Team Settings menu offers Team Administrators and System Administrators the ability to adjust settings applied to a specific team. 

The following settings are found in a Team Site from the **Three-Dot** menu at the top of the left sidebar under **Team Settings**. 

### General  

General settings under the **Team Settings** > **General** configure how a team is displayed to users. 

#### Team Name

Your **Team Name** is displayed on the sign-in page, and in the top of the left-hand sidebar for your team. 

#### Allow anyone to join this team (*Available May 16th*)

After a user logs in to the site, they are shown a Team Selection page. Any team with **Allow anyone to join this team** option set to **Yes** will show up on this page under "Open teams you can join".

#### Invite Code 

The **Invite Code** is used as part of the URL in the team invitation link retrieved from the **Main Menu** > **Get Team Invite Link**. Click **Re-Generate** and then **Save** to generate a new team invitation link and invalidate the previous link.

### Import

#### Import from Slack (Beta) 

*Note: As a proprietary SaaS service, Slack is able to change its export format quickly and without notice. If you encounter issues not mentioned in the documentation below, please alert the product team by [filing an issue](https://github.com/mattermost/platform/issues).*

The Slack Import feature in Mattermost is in "Beta" and focus is on supporting migration of teams of less than 100 registered users. To use: 

1. Generate a Slack "Export" file from **Slack > Team Settings > Import/Export Data > Export > Start Export**.  

2. In Mattermost go to **Team Settings > Import > Import from Slack**. _Team Administrator_ or _System Administrator_ role is required to access this menu option.

3. Click **Select file** to upload Slack export file and click **Import**.   

4. Emails and usernames from Slack are used to create new Mattermost accounts. 

5. Slack users can activate their new Mattermost accounts by using Mattermost's Password Reset screen with their email addresses from Slack to set new passwords for their Mattermost accounts.  

6. Once logged in, the Mattermost users will have access to previous Slack messages in the public channels imported from Slack.

**It is highly recommended that you test Slack import before applying it to an instance intended for production.** If you use Docker, you can spin up a test instance in one line (`docker run --name mattermost-dev -d --publish 8065:80 mattermost/platform`). If you don't use Docker, there are [step-by-step instructions](http://docs.mattermost.com/install/docker-local-machine.html) to install Mattermost in preview mode in less than 5 minutes.

#### Limitations 

- Users are not automatically added to channels or groups when importing from Slack.
- Newly added markdown support in Slack's Posts 2.0 feature announced on September 28, 2015 is not yet supported.
- Slack does not export files or images your team has stored in Slack's database. Mattermost will provide links to the location of your assets in Slack's web UI.
- Slack does not export any content from private groups or direct messages that your team has stored in Slack's database. 
- In Beta, Slack accounts with usernames or email addresses identical to existing Mattermost accounts will not import and mentions do not resolve as Mattermost usernames (still shows Slack ID). No pre-check or roll-back is currently offered. 
