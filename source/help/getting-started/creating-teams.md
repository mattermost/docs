# Creating Teams
___

This documentation refers to Mattermost v3.0. For v2.2, see [archived documentation](http://docs.mattermost.com/archives/docs-v2.2.html#creating-teams).

New teams can be created if the System Admin has *Enable Team Creation* set to true from the System Console.

## Methods to Create a Team
Teams can be created from the main menu, system home page or team sign in page. The person who creates a team will automatically be given the Team Administrator role for that team. 

#### Main Menu
Click the **Three-Dot** menu in Mattermost, then select **Create a New Team**. If this option is not visible in the menu, then the System Admin has *Enable Team Creation* set to false.

#### System Home Page
Navigate to the web address of your system, `https://domain.com/`. Sign in using your credentials. Click **Create a new team** to be guided through the rest of the set up steps. If this option is not visible on the web page, then the System Admin has *Enable Team Creation* set to false. It is necessary to have an existing account on the system in order to create a team from the system home page, so if you do not have an account you will need to create one.

## Team Name and URL Selection
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
