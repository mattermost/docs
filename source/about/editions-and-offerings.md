<!--IMPORTANT: ANY CHANGES REQUIRE APPROVAL FROM EITHER VP PRODUCT, CHIEF PRODUCT OFFICER OR CEO. 

THERE HAS BEEN MATERIAL CONFUSION IN HOW WE DESCRIBE OUR FEATURES (e.g. https://www.reddit.com/r/Mattermost/comments/wlbdbc/team_edition_limitation_confirmation/) AND UNTIL WE CAN SYSTEMATICALLY SOLVE THIS, PRODUCT LEADERSHIP IS ACCOUNTABLE FOR HOW WE COMMUNICATE OUR OFFERINGS TO THE TECHNICAL COMMUNITY. ALSO, THIS DOC WILL BE IN MD, INSTEAD OF RST TO MAKE IT EASIER TO MAINTAIN

-->

<!--

DOC TEAM - OKAY FOR GRAMATICAL EDITS, BUT PLEASE DO NOT CHANGE CONTENT--PLEASE PUBLISH AND OPEN A TICKET ON ANY ISSUES WITH MENTION TO THE CONTRIBUTING AUTHOR. 

<!--

AUDIENCE: Developer and IT Administrator 
PURPOSE: Educate audience on thematic and technical packaging of our offerings, with links to specific details and how to activate and use each feature

-->

# Mattermost editions and plans 

Mattermost offers open core, workplace collaboration for developers. 

"Open core" means we develop both an open source, self-hosted edition of our software provided free to our community, as well as a commercial edition that extends and enhances our open source software with paid, subscription-based offerings available both in self-hosted and cloud-hosted deployment modes.

"Workplace collaboration for developers" means we offer a suite of tools for technical teams to increased their productivity, including real time messaging, audio calling and screensharing, incident management, project management, and an extensive platform for integrating their development toolchains. 

You can choose between one of two compiled code bases, either open source ([Team Edition](#mattermost-team-edition)) or commercial ([Enterprise Edition](#mattermost-enterprise-edition)).

We offer a range of plans, which are sets of features and entitlements available either free or as a paid subscription service. Mattermost sells subscriptions for both self-hosted and cloud deployments.

## Self-hosted editions

Self-hosted editions support deploying Mattermost within IT-controlled private environments in public clouds, including AWS, Azure, GCP and Oracle Cloud, as well as on-premises in private clouds and virtual or physical servers. 

When you're using a self-hosted deployment, a license key is provided and needs to be uploaded to activate your subscription.

### Mattermost Team Edition

Team Edition is a free-to-use, open source, self-hosted collaboration platform offering all the core productivity benefits of competing SaaS solutions. It deploys as a single Linux binary with MySQL or PostgreSQL under an MIT license.

Mattermost Team Edition is also bundled inside of the free Mattermost Enterprise Edition code base, which provides the same functionality as Mattermost Team Edition, with the additional benefit of being able to trial as well as upgrade into an expanded set of features available with paid subscription, including Mattermost Professional and Mattermost Enterprise. 

Because of the benefits of Mattermost Enterprise Edition, we recommend installing it instead of Mattermost Team Edition, even if you don’t currently need a subscription, so you'll have the flexibility to trial or enable additional features should you need them. However, if you only want to install software with a fully open source license, then Mattermost Team Edition is the best choice.

### Mattermost Enterprise Edition 

Our commercial, self-hosted software is called Mattermost Enterprise Edition, and it's available as a Linux binary that deploys identically to our open source version - including upgrading in an identical fashion - with two key differences: First, it contains code for advanced commercial features and second, it's offered under a [commercial license](https://mattermost.com/enterprise-edition-license/). The commercial license prohibits reverse engineering and tampering with our license key mechanism unlocking paid features so that we can run a compliant and fair commercial business, and it references the terms of our commercial subscription service, should you choose to purchase a subscription. 

Once you’ve downloaded and installed Mattermost Enterprise Edition within your preferred environment, you have the option to use it as-is in a "free forever" mode, or you can access Mattermost's commercial features by starting a trial or by purchasing a subscription. You can start a 30-day free Enterprise trial via **System Console > Edition and License > Start trial**, or request a trial online at https://mattermost.com/trial/.

## Mattermost plans

Mattermost plans consist of features and entitlements available either free or as a paid subscription service. 

We have three primary plans available to our self-hosted and cloud users: 

* **Mattermost Free** - This a free version of our collaboration suite designed for single teams.
* **Mattermost Professional** - This is a paid subscription service providing advance access controls and user management for managers leading teams of teams.
* **Mattermost Enterprise** - This is a paid subscription service for large, complex, enterprise-scale deployments.

For customers using our service in a self-hosted deployment, the Mattermost Cloud offering is available in both our open source and commercial code bases (called [Mattermost Team Edition](#mattermost-team-edition) and [Mattermost Enterprise Edition](#mattermost-enterprise-edition), respectively). 

The [Mattermost Professional](#mattermost-professional) and [Mattermost Enterprise](#mattermost-enterprise) plans are only available after deploying our Mattermost Enterprise Edition code base, and then applying a valid license key that comes with a subscription purchase, or by starting a 30-day free trial that can be activated either in-product (**System Console > Edition and License > Start trial**) or online at https://mattermost.com/trial/.

### Mattermost Free

Mattermost Free offers workplace collaboration for accelerating a technical team’s productivity, ideally up to around 25 users. While there aren't limits on the number of users that can be added, to control cost of providing free hosting the cloud version of the Mattermost Free plan have [usage limits](https://docs.mattermost.com/onboard/mattermost-limits.html). The cloud version limits on Mattermost Free do not apply to the self-hosted version. 

* *Self-hosted deployments* - **Mattermost Free** is available to our self-hosted community through both our open source Mattermost Team Edition offering, and in our commercial Mattermost Enterprise Edition offering (when no subscription license key is active). See deployment options at: https://mattermost.com/deploy/.
* *Cloud deployments* - **Mattermost Free** is also available in Cloud. It provides the functionality of Mattermost Free to unlimited users for free, with [usage limits](https://docs.mattermost.com/onboard/mattermost-limits.html). Get started today via https://mattermost.com/sign-up/.

Workplace Collaboration features include: 

- [**Channels**](https://docs.mattermost.com/guides/channels.html) for one-to-one and group messaging, threaded messaging, file sharing, archiving and search, emojis, and Custom Emojis.
- [**Playbooks**](https://docs.mattermost.com/guides/playbooks.html) for structured ChatOps and incident management with task automation and process dashboarding and reporting.
- [**Boards**](https://docs.mattermost.com/guides/boards.html) for project management with table, gallery, list views, a single workspace per channel, shareable read-only boards, and data import.
- **Workspaces** for organizing Channels, Playbooks and Boards by organization and user groups. 
- [**Mobile Applications**](https://developers.mattermost.com/contribute/mobile/) for iOS and Android in Apple Store and Google Play respectively, as well as [full source code](https://github.com/mattermost/mattermost-mobile) for [building and distributing custom mobile apps](https://docs.mattermost.com/deploy/build-custom-mobile-apps.html) to an internal Enterprise App Store, or securing with Enterprise Mobility Management. 
- **Desktop Application** for Windows, MacOS, and Linux (Ubuntu/Debian, CentOS/RHEL, Generic Linux) including support for [Desktop MSI and Group Policies (Beta)](https://docs.mattermost.com/install/desktop-msi-installer-and-group-policy-install.html), [silent installation](https://docs.mattermost.com/install/desktop-msi-installer-and-group-policy-install.html#silent-installation-guide), and [managed resources](https://docs.mattermost.com/install/desktop-app-managed-resources.html). 
- [**Integrations**](https://docs.mattermost.com/about/integrations.html) including connected workflows with common developer tools, including Jira, Confluence, GitHub, GitLab, CircleCI, Zoom, and Jitsi, as well as an extensible support for [bots and plug-ins](https://mattermost.com/marketplace/#publicApps) as well as [webhooks, APIs, and drivers](https://developers.mattermost.com/integrate/other-integrations). 
- **Multi-language support** including English (U.S. and Australian), Bulgarian, Chinese (Simplified and Traditional), Dutch, French, German, Italian, Japanese, Korean, Persian, Polish, Portuguese (Brazil), Romanian, Russian, Spanish, Swedish, Turkish, and Ukrainian.

System management and customization features include:  
- [Tools for Custom Branding](https://docs.mattermost.com/configure/custom-branding-tools.html) including customization of login page. 
- [Custom Themes and Colors](https://docs.mattermost.com/messaging/customizing-theme-colors.html) including ability to import templates. 
- [Multi-factor authentication](https://docs.mattermost.com/onboard/multi-factor-authentication.html) via Google Authenticator in addition to username/password and [password policy enforcement](https://docs.mattermost.com/configure/configuration-settings.html#password). 
- (Self-hosted Only) [Command Line Tool](https://docs.mattermost.com/manage/mmctl-command-line-tool.html) for configuration and [server upgrade](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html). 

Support entitlements from Mattermost, Inc: 
- [Knowledge base and troubleshooting documentation](https://support.mattermost.com/hc/en-us) is available for common techincal issues. 
- [Peer-to-Peer community support](https://mattermost.com/support/) via on-line forums. 

Service entitlements from Mattermost, Inc: 
- (Cloud Only) [SOC 2 Type 1 certification](https://mattermost.com/security/) with plans to add SOC 2 Type 2 in 2023. 


### Mattermost Professional 

Mattermost Professional is a paid subscription offering advanced configuration for software organizations from 25 to 100 users. 

* *Self-hosted deployments* - **Mattermost Professional** is available to our self-hosted community who either run, or upgrade to, our self-hosted commercial Mattermost Enterprise Edition (see [deployment guides](https://docs.mattermost.com/guides/deployment.html#install-guides)), who purchase the appropriate subscription license key either through [online purchase](https://docs.mattermost.com/about/self-hosted-subscriptions.html), through a [channel reseller](https://mattermost.com/partners/#resellers) or by contacting [the Mattermost sales organization](https://mattermost.com/contact-sales/), and who then install the license key onto their Mattermost server. A 30-day free trial to preview the features in this subscription can be activated either in-product (**System Console > Edition and License > Start trial**) or via an online request at https://mattermost.com/trial/.
* *Cloud deployments* - For our cloud community, the Mattermost Professional feature set is available through [online purchase](https://docs.mattermost.com/about/self-hosted-subscriptions.html). Some [workspace limits](https://docs.mattermost.com/onboard/mattermost-limits.html) may apply.

This offering includes all the features of Mattermost Starter, plus: 

- [**Guest accounts**](https://docs.mattermost.com/onboard/guest-accounts.html) offering permission-limited accounts for guests (such as customers, vendors and partners) to join a workpace. Note: For billing purposes Guests are treated as a Registered User. 
- `Active Directory/LDAP Single Sign-on and user synchronization <https://docs.mattermost.com/onboard/ad-ldap.html>`__.
- Single Sign-on with SAML, `Google <https://docs.mattermost.com/onboard/sso-google.html>`__, `Office365 <https://docs.mattermost.com/onboard/sso-office.html>`__ or `OpenID Connect <https://docs.mattermost.com/onboard/sso-openidconnect.html>`__.
- `MFA enforcement <https://docs.mattermost.com/onboard/multi-factor-authentication.html#enforcing-mfa-e10>`__.
- `Advanced team permissions <https://docs.mattermost.com/onboard/advanced-permissions.html#team-override-schemes-e20>`__.
- `Read-only announcement channels <https://docs.mattermost.com/manage/team-channel-members.html#channel-moderation-e20>`__.
- `System-wide announcement banners <https://docs.mattermost.com/manage/announcement-banner.html>`__.
- O365 integration with `Microsoft Teams Calling <https://mattermost.com/marketplace/microsoft-teams-meetings/>`_ and `Jira multi-server <https://mattermost.com/marketplace/jira-plugin/>`_.
- [Granular system permissions](https://docs.mattermost.com/onboard/advanced-permissions.html) providing role-based access controls and delegated permissions. 
- (Cloud Only) [Higher Mattermost Usage Limits](https://docs.mattermost.com/onboard/mattermost-limits.html) with increased or unlimited usage on limits set in Mattermost Free plan. 

Support entitlements from Mattermost, Inc: 
- [Next business day support](https://mattermost.com/support/) via online ticketing system. 

### Mattermost Enterprise 

Mattermost Enterprise is an enterprise-grade collaboration system that supports and helps you scale your mission-critical enterprise workflows, meet strict enterprise security, compliance, and privacy requirements, as well as provide executive reporting, dashboards, and productivity metrics.

* *Self-hosted deployments* - **Mattermost Enterprise** is available to our self-hosted community who either run, or upgrade to, our self-hosted commercial Mattermost Enterprise Edition, who purchase by `contacting the Mattermost sales organization <https://mattermost.com/contact-sales/>`__, and who then install the license key onto their Mattermost server. A 30-day free trial to preview the features in this subscription can be activated either in-product (**System Console > Edition and License > Start trial**) or via an online request at https://mattermost.com/trial/.
* *Cloud deployments* - For our cloud community, the Mattermost Enterprise can be purchased by `contacting the Mattermost sales organization <https://mattermost.com/contact-sales/>`__.

This offering includes all the features of Mattermost Professional, plus: 

- `Enterprise-scale search with dedicated indexing and usage resourcing via cluster support <https://docs.mattermost.com/scale/elasticsearch.html>`__.
- `Sychronization of access controls, channels, and teams with AD/LDAP Groups <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__.
- `eDiscovery and compliance export automation <https://docs.mattermost.com/comply/compliance-export.html>`__.
- `Enterprise mobile device management with custom EMM support via AppConfig <https://docs.mattermost.com/deploy/mobile-appconfig.html>`__.
- `Advanced legal controls with customizable end-user terms of service and re-acceptance duration <https://docs.mattermost.com/comply/custom-terms-of-service.html>`__.
- `Private mobility with ID-only push notifications <https://docs.mattermost.com/configure/configuration-settings.html#push-notification-contents>`__.
- `Enhanced compliance with global and custom retention policies for messages and files <https://docs.mattermost.com/comply/data-retention-policy.html>`__.
- `Granular administrative control with custom system admin roles <https://docs.mattermost.com/onboard/system-admin-roles.html>`__.
- `Advanced configuration of playbook permissions, analytics dashboards, and channel exports <https://docs.mattermost.com/playbooks/setting-up-playbooks.html>`__.
- `Enhanced compliance controls and granular audit logs with data export <https://docs.mattermost.com/comply/audit-log.html>`__.
- `Advanced collaboration with shared channels across Mattermost instances <https://docs.mattermost.com/onboard/shared-channels.html>`__.
- `High availability support with multi-node database deployment <https://docs.mattermost.com/scale/high-availability-cluster.html>`__.
- `Horizontal scaling through cluster-based deployment <https://docs.mattermost.com/scale/scaling-for-enterprise.html#cluster-based-deployment>`__.
- `Advanced performance monitoring <https://docs.mattermost.com/scale/performance-monitoring.html>`__.
- `Eligibility for Premier Support add-on <https://mattermost.com/support/>`__.
- 99% uptime SLA guarantee (Cloud only, via dedicated virtual secure Cloud add-on option).

## Limits

Mattermost Cloud plans have [usage limits](https://docs.mattermost.com/onboard/mattermost-limits.html) to contain the cost of hosting, primarily for our free offering. These limits may change over time as usage evolves. 

## Legacy Mattermost plans

Mattermost introduced a new pricing and packaging structure on October 13, 2021. The plans listed below will reach end-of-life on October 31, 2023. We're no longer selling these products to new customers. For existing customers, we highly recommend working with your Mattermost Account team to plan for a migration to our new plans, but we will honor existing pricing and features for renewals and expansions of E10/20 until October 31, 2022. Please contact our `Sales team <https://mattermost.com/contact-us/>`__ with questions.

** Mattermost Enterprise Edition E10** - Mattermost E10 was offered as a commercial enterprise messaging solution for teams, groups, and departments working on multiple projects scaling from hundreds to thousands of users. Many E10 features are now offered in Mattermost Professional. Features include: Active Directory/LDAP Single Sign-on; OAuth 2.0 authentication for team creation, account creation, and user login; encrypted push notifications with service level agreements (SLAs) via HPNS; advanced access control policy; next business day support via online ticketing system; scale to handle hundreds of users per team.

** Mattermost Enterprise Edition E20** - Mattermost Enterprise E20 was offered as a commercial enterprise-grade messaging system that scales from hundreds to tens of thousands of users. Enterprise Edition E20 authentication features are now offered in Mattermost Professional and High Availability and compliance features are offered in Mattermost Enterprise.

Features include: Advanced SAML 2.0 authentication with Okta, OneLogin, and Active Directory Federation Services; Active Directory/LDAP group synchronization; OpenID Connect authentication for team creation, account creation, and user login; compliance exports of message histories with oversight protection; custom retention policies for messages and files; high availability support with multi-node database deployment; horizontal scaling through cluster-based deployment; Elasticsearch support for highly efficient database searches in a cluster environment; advanced performance monitoring; eligibility for Premier Support add-on.

# Product decisions

As the platform matures and new features are added, they're evaluated to be included in the plan that best aligns with the organizational use cases outlined by the editions above. Multiple factors are considered in determining the appropriate plan to include a feature including mission-critical impact, relative value to a single team, cross-functional teams, and the enterprise, as well as security, compliance, and scalability.

We recognize there aren't any features that are only useful to managers, directors, and executives. Individual practitioners may want certain features; however, we think that other buyers are relatively more likely to care about it. We also recognize that there may be some features that are put into an edition to find later there is much demand for it by individuals or a singular team; we will not hesitate to move that feature. We value feedback from our community and iterate based on that feedback. Simultaneously, we also need to offer commercial products that hold value and do our best to find the right balance. We believe the more of Mattermost that you use, the more likely it is that you benefit from the advanced editions we offer.

You can provide us with feedback via `our forum <https://mattermost.uservoice.com/>`__, where ideas and input influences the future of the platform.


