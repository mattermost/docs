# Enterprise Edition (pre-release)

Early customers who have deployed the pre-released version of Mattermost Enterprise Edition are providing feedback to shape the feature set, roadmap and pricing of the commercial verison of Mattermost. 

A pre-released version of Enterprise Edition v1.4 is available for organizations who have deployed the open source version and are open to providing feedback on commerical features, such as authentication with Active Directory/Lightweight Directory Access Protocol (AD/LDAP) and features for advanced compliance requirements. 

#### Accessing Enterprise Edition Pre-Release

You can request access to a pre-released version of _Mattermost Enterprise Edition v1.4_ at https://about.mattermost.com/contact/

#### Installing Pre-release

The pre-release deploys using the same [install guides](http://docs.mattermost.com/index.html#install-guides) as the open sourced Mattermost v1.4 Team Edition

#### Upgrading to Pre-release

You can also upgrade to the pre-released Enterprise Edition version from Mattermost v1.4 or Mattermost v1.3 using the [instructions in the upgrade guide](http://docs.mattermost.com/install/upgrade-guide.html)

You can verify your upgrade to Enterprise Edition by going into a team site and in the "About Mattermost" dialog box and next to **Build Number** you should see `ent-[RELEASE_NUMBER]`.

#### Activate Pre-release

If you don't see **LDAP Settings** in **System Console** or by going to `<mattermost-url>/admin_console/ldap_settings` you need to activate the features using a trial license key. 

Go to **System Console** > **Editions and License** > **License Key** > **Choose File** and select the license file provided, then click **Upload**. The **Edition** field should show **Mattermost Enterprise Edition** and the enteprise features should be activated. 

In the team site when you go to the main menu and open the "About Mattermost" dialog the **Licensed by** field should say `trial`.

#### Setting up Active Directory/LDAP

Instructions for setting up AD/LDAP SSO are available in the [deployment guide.](http://docs.mattermost.com/deployment/sso-ldap.html)

#### Support

After completing the [contact form](https://about.mattermost.com/contact/) to receive the pre-released version of Mattermost Enteprise Edition you should be in email contact with a support team who can help with your evaluation.

Note: If you received a requested a pre-release of Enterprise Edition before January 21 it was the v1.3 edition, you can [contact Mattermost](https://about.mattermost.com/contact/) to receive the v1.4 discussed here. 
