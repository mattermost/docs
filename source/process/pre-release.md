# Enterprise Edition (pre-release)

Mattermost Enteprise Edition was officially released March 16th, 2016, and is [available for purchase online.](https://about.mattermost.com/pricing/)

The following instructions are for users of the Mattermost Enterprise Edition pre-release. 

- Pre-release versions `ENT-7`, `ENT-6`, `ENT-5`, and `ENT-4` can [upgrade directly](http://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-enterprise-edition) to Mattermost Enterprise Edition 2.1.0, which [upgrades to newer versions](http://docs.mattermost.com/administration/upgrade.html#upgrading-enterprise-edition). Users with earlier versions should contact their success manager for upgrade instructions. 

#### Installing Enterprise Edition 

1. Install the open source Mattermost Team Edition using any of the existing [install guides](http://docs.mattermost.com/index.html#install-guides).
2. Follow the upgrade procedure to change from [Mattermost Team Edition to Mattermost Enteprise Edition](http://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-enterprise-edition).
3. Follow the instructions received by email with the purchase of your license key to enable Enterprise Edition features.

Once activated you should see additional options in the System Console and the "About Dialog" in the team site should read "Mattermost Enterprise Edition". 

#### Setting up Active Directory/LDAP

Instructions for setting up AD/LDAP SSO are available in the [Active Directory/LDAP deployment guide.](http://docs.mattermost.com/deployment/sso-ldap.html)

#### Setting up SAML Single-Sign-On (SSO)

Instructions for setting up SAML SSO are available in the [SAML deployment guide.](http://docs.mattermost.com/deployment/sso-saml.html)

#### Downgrading from Enterprise Edition to Team Edition 

To downgrade from Enterprise Edition to Team Edition: 

1. Disable Active Directory/LDAP SSO and SAML SSO, and ensure all accounts have switched to another authentication method.
2. Use the "Remove Enterprise License and Downgrade Server" option in the licensing menu from System Console.

#### Support

After completing the [contact form](https://about.mattermost.com/contact/) to receive the pre-released version of Mattermost Enteprise Edition you should be in email contact with a support team who can help with your evaluation.


