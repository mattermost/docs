# Enterprise Edition (pre-release)

Note: If you received a pre-release of Enterprise Edition before February 22, 2016 you can [contact Mattermost](https://about.mattermost.com/contact/) to receive the latest version, `ENT-7`, which supports upgrades from all other `ENT-` versions. 

Early customers who have deployed the pre-released version of Mattermost Enterprise Edition are providing feedback to shape the feature set, roadmap and pricing of the commercial verison of Mattermost. 

Pre-released versions of Enterprise Edition are available for organizations who have deployed the open source version and are seeking to evaluate commerical features, such as authentication with Active Directory/Lightweight Directory Access Protocol (AD/LDAP), organization-wide reporting, and audit and compliance reporting. 

#### Accessing Enterprise Edition Pre-Release

You can request access to a pre-released version of _Mattermost Enterprise Edition_ at https://about.mattermost.com/contact/

#### Installing Enterprise Edition Pre-released

The pre-release of Mattermost Enterprise deploys using the same [install guides](http://docs.mattermost.com/index.html#install-guides) as the open sourced Mattermost Team Edition. 

Just replace the `mattermost.tar.gz` file with the pre-released Enterprise Edition file provided during the installation process. 

#### Upgrading to Enterprise Edition pre-release 

To upgrade an existing Mattermost Team Edition deployment: 

1. Upgrade your existing Mattermost deployment to v1.4 using the [standard upgrade process](http://docs.mattermost.com/install/upgrade-guide.html) 
2. Run the [standard upgrade process](http://docs.mattermost.com/install/upgrade-guide.html) one more time using the  `mattermost.tar.gz` provided for the Mattermost Enterprise Edition pre-release.

You can verify your upgrade to Enterprise Edition by going into a team site and in the "About Mattermost" dialog box and next to **Build Number** you should see `ENT-7`.

#### Activate Pre-release

If you don't see **LDAP Settings** in **System Console** or by going to `<mattermost-url>/admin_console/ldap_settings` you need to activate the features using a trial license key. 

Go to **System Console** > **Editions and License** > **License Key** > **Choose File** and select the license file provided, then click **Upload**. The **Edition** field should show **Mattermost Enterprise Edition** and the enteprise features should be activated. 

In the team site when you go to the main menu and open the "About Mattermost" dialog the **Licensed by** field should say `trial_1000users`.

#### Setting up Active Directory/LDAP

Instructions for setting up LDAP/AD SSO are available in the [deployment guide.](http://docs.mattermost.com/deployment/sso-ldap.html)

#### Downgrading from Enterprise Edition to Team Edition 

To downgrade from Enterprise Edition to Team Edition: 

1. Disable Active Directory/LDAP SSO.
2. Use the "Remove Enterprise License and Downgrade Server" option in the licensing menu from System Console.

#### Support

After completing the [contact form](https://about.mattermost.com/contact/) to receive the pre-released version of Mattermost Enteprise Edition you should be in email contact with a support team who can help with your evaluation.


