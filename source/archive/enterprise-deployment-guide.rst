
Enterprise Deployment Guide
===========================

About This Guide
----------------

Audience: IT Leaders, System Administrators, and/or Project Managers

.. note::
    Some features described in this guide are only available to Enterprise Edition E10 and/or E20. We will highlight specific licenses needed whenever applicable.

Learning Objectives
-------------------

This guide provides foundational information necessary when developing a plan for a proof of concept and/or production-level enterprise deployment of Mattermost.

It will not dive into the technical implementation, but will reference any relevant documentation.

By the end of this guide you should have an understanding of the high-level requirements for a successful Mattermost Enterprise deployment.

This includes:

- Choosing how to deploy the Mattermost Server application.
- Migrating from other ChatOps platforms.
- Integrating Mattermost with existing Single sign-on (SSO) providers.
- First steps/best practices for onboarding users.

Support
-------

If at any point you need additional help, we are ready to assist, just reach out using any of these methods:

- `Community <https://community.mattermost.com/>`_ - Our entire organization uses Mattermost, plus you’ll have the support of one of the best open source communities around.
- Documentation - We link to many parts of our `Administrator documentation <https://docs.mattermost.com/guides/administrator.html>`_ in this guide but encourage you to take a look at `all our documentation <https://docs.mattermost.com>`_.
- Enterprise Support  - If you are an Enterprise Edition subscriber, you may open a support ticket in the Enterprise Edition Support portal.

.. Recommendation::
    Visit the `Mattermost Community server <https://community.mattermost.com/>`_ and create an account. Join channel `Ask Anything <https://community.mattermost.com/core/channels/ask-anything>`_ to not only experience Mattermost right away but also for support if you get stuck at any point in this guide.

Before You Begin Your Deployment
--------------------------------

What Makes Mattermost Different?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost is a high-trust messaging platform for enterprise use. As enterprises come in all shapes and sizes, Mattermost has been built to provide an optimal experience for all customers.

The emergence of `ChatOps <https://mattermost.com/chatops>`_ means Mattermost is no longer a tool predominantly used by developers. In fact, it has the ability to enhance communication for many kinds of teams through a multitude of `integrations <https://integrations.mattermost.com>`_, extensions, and customization.

Here is a sample of the types of integrations our customers are deploying:

- Confluence
- Docker
- GitHub/GitLab
- Jira
- Outlook
- Trello

Taking this further, because Mattermost is an open source application, it can be customized, in many ways, to suit your organizational needs.

Mattermost Scaling
------------------

Growing your Mattermost installation from supporting a team to supporting an enterprise requires two types of `scaling <https://docs.mattermost.com/deployment/scaling.html>`_.

**Technical Scaling:** Whether used for teams or enterprises, the Mattermost server is designed to support tens of thousands of users on a single server with appropriate hardware. We officially support running Mattermost Server on multiple `Linux distributions and on-premises cloud solutions <https://docs.mattermost.com/guides/administrator.html#installing-mattermost>`_.

**Functional Scaling:** Scaling from a team to an enterprise is like going from a "virtual office" to a "virtual campus". Advanced features like enterprise authentication, granular permissions, compliance and auditing, and advanced reporting become increasingly important as organizations grow beyond teams.

Mattermost Licensing
--------------------

Mattermost Enterprise Edition comes with two licensing options: Enterprise E10 and Enterprise E20.

The E10 license suits smaller organizations with less need for automation and compliance, while the E20 license offers features like AD/LDAP, SAML 2.0, automated compliance export, and team-specific permissions. You can find a full comparison `here <https://mattermost.com/pricing-feature-comparison>`_.

Once you have installed and deployed Mattermost, activate your Enterprise E20 trial license via **Main Menu > System Console > Edition and License** and select **Start trial**.

.. Note::
    You can purchase and manage your Mattermost Enterprise subscriptions with our `Customer Portal <https://customers.mattermost.com/login>`_ or reach out to our Sales team by contacting sales@mattermost.com.

Client Usage
------------

Depending on your environment and your users, you have several options when deploying Mattermost: web browser, `desktop <https://docs.mattermost.com/install/desktop.html>`_, `mobile <https://docs.mattermost.com/mobile/mobile-overview.html>`_, or all three. We `provide binaries <https://mattermost.com/download/#mattermostApps>`_ for MS Windows, macOS, Linux, iOS, and Android. However, depending on your organization policies deployment on these platforms can vary.

Deployment First Steps
----------------------

Deploying Mattermost with an enterprise environment is not a small project. Depending on your use case multiple physical machines have to be set up with Mattermost server, a proxy, and a database while thousands of users need to be imported through AD/LDAP. While we strive to make this as easy as possible it will take time and iteration.

Determine Your Use Case
~~~~~~~~~~~~~~~~~~~~~~~

As mentioned above it is essential for a successful deployment to know your specific use case. To get started try answering the following questions:

- How many users will use Mattermost on initial deployment and is this number going to increase dramatically in the near future?
- What clients will be in use?
- Are you migrating from an existing ChatOps or different communications platform?
- Are you using an identity provider for Single sign-on and if yes which one?
- What compliance requirements do you need to meet?
- What are your organization's security requirements?

Planning Your Deployment
------------------------

Technical Requirements
~~~~~~~~~~~~~~~~~~~~~~

The hardware requirements for the Mattermost server and database `grow based on the number of users <https://docs.mattermost.com/install/requirements.html>`_.

Depending on which clients your users will work with additional reading can be necessary:
- You are going to use the web app - no further reading required.
- You are going to use the desktop app - please also read `Desktop Application Install Guides <https://docs.mattermost.com/install/desktop.html>`_.
- You are going to use the mobile app - please also read `Mobile App Deployment Guide <https://docs.mattermost.com/deployment/mobile-app-deployment.html>`_.

Migration
---------

When migrating from an existing solution it is important to plan ahead. We recommend starting with a small dataset - limited users and content - to reduce the time spent debugging and ensuring all fields are imported correctly, before taking on a major import.

We provide our customers with easy to use migration solutions for many scenarios:

- Mattermost - Migrating from Mattermost Team Edition is common and only requires you to `upgrade to the most recent Enterprise Edition <https://docs.mattermost.com/administration/upgrade.html#upgrading-team-edition-to-enterprise-edition>`_ and add your license key.
- Slack - There is support for two methods of importing data from Slack.
    - For small datasets with few users and without post attachments the `Mattermost web app can be used <https://docs.mattermost.com/administration/migrating.html?highlight=slack#migrating-from-slack-using-the-mattermost-web-app>`_.
    - If at all possible we recommend the use of `Mattermost CLI for the migration process <https://docs.mattermost.com/administration/migrating.html?highlight=slack#migrating-from-slack-using-the-mattermost-cli>`_.
- HipChat - We recommend using `Group Export Dashboard <https://docs.mattermost.com/administration/hipchat-migration-guidelines.html>`_ to export your data in combination with the `Mattermost Bulk Load Tool <https://docs.mattermost.com/deployment/bulk-loading.html>`_.
- Jabber - You can use `BrightScout’s Extract, Transform and Load (ETL) <https://github.com/Brightscout/mattermost-etl>`_ tool to migrate from Jabber.
- Bespoke Messaging Solutions - Mattermost is designed to replace bespoke messaging solutions and provide additional `security features <https://docs.mattermost.com/overview/security.html>`_, but migrating from bespoke messengers can prove to be challenging, because the data format of such tools is unpredictable. Nonetheless we provide `multiple tools <https://docs.mattermost.com/administration/migrating.html?highlight=slack#bringing-data-from-bespoke-solutions-into-mattermost>`_ to attempt migration and have had many successful migrations with our customers.

.. Note::
    If your data in the bespoke messenger is not vital we recommend a hard switch after a period of running both systems in parallel.

Single Sign-On
--------------

Mattermost can act as a `SAML 2.0 <https://docs.mattermost.com/deployment/sso-saml.html>`_ provider so setting up Single sign-on is a straightforward matter.

We support these SSO services:

- `OneLogin <https://docs.mattermost.com/deployment/sso-saml-onelogin.html>`_
- `Okta <https://docs.mattermost.com/deployment/sso-saml-okta.html>`_
- `GitLab <https://docs.mattermost.com/deployment/sso-gitlab.html>`_
- `Google People API <https://docs.mattermost.com/deployment/sso-google.html>`_
- `AD/LDAP <https://docs.mattermost.com/deployment/sso-ldap.html>`_
- `Azure Active Directory and Office 365 <https://docs.mattermost.com/deployment/sso-office.html>`_
- `Microsoft ADFS <https://docs.mattermost.com/deployment/sso-saml-adfs-msws2016.html>`_

Compliance
----------

When you have to meet compliance requirements - especially when working with proxies - make sure to plan ahead to avoid infrastructure redesign while deploying Mattermost. Here is how Mattermost supports your compliance needs:

- Outbound Proxy - In some scenarios, like monitoring outbound traffic or controlling which websites can appear in link previews, you may wish to `use Mattermost behind a proxy <https://docs.mattermost.com/install/outbound-proxy.html>`_.
- Electronic Discovery - Electronic Discovery (eDiscovery) is the process of searching electronic data to be used as evidence in a legal case. We have put together the `eDiscovery documentation <https://docs.mattermost.com/administration/ediscovery.html>`_ to help.
- Compliance Export - This feature enables `Compliance Exports <https://docs.mattermost.com/administration/compliance-export.html>`_ to be produced from the System Console, containing all messages.
- Data Retention - By default, Mattermost provides unlimited search history storing all messages without an expiration date. These defaults can be `changed by setting Message Retention and File Retention <https://docs.mattermost.com/administration/data-retention.html>`_ to a specific duration in the System Console.
- Custom Terms of Service - If your organization requires the use of `custom ToS <https://docs.mattermost.com/administration/custom-terms-of-service.html>`_, this can be done in the System Console.

Security
--------

Security is a major concern with regard to selecting the right tools. Mattermost software is continually reviewed for security by developers, IT administrators, and security researchers. In contrast to SaaS solutions Mattermost can be deployed on-premises in your private cloud giving you full control of not only the software but the hardware side as well. Here is a non-exhaustive list of our security features:

- Private cloud deployment
- Secure mobile apps
- Transmission security
- Integrity and audit controls
- Authentication safeguards
- Access Control Policy
- More details on this topic are available at the `Mattermost security <https://docs.mattermost.com/overview/security.html>`_ section in our documentation.
- HIPAA und FINRA - Mattermost can be deployed `Health Insurance Portability and Accountability Act - HIPAA <https://docs.mattermost.com/overview/security.html#hipaa-compliance>`_ and `Financial Industry Regulatory Authority - FINRA <https://docs.mattermost.com/overview/security.html#finra-compliance>`_ compliant.
- Certificate-Based Authentication - `Certificate-Based Authentication <https://docs.mattermost.com/deployment/certificate-based-authentication.html>`_ is available as an experimental feature.
- Multi-factor Authentication - Mattermost supports `multi factor authentication <https://docs.mattermost.com/deployment/auth.html>`_.

User Onboarding and Adoption
----------------------------

Integrations and Plugins
~~~~~~~~~~~~~~~~~~~~~~~~

On the first look considering `integrations <https://integrations.mattermost.com>`_ and `plugins <https://docs.mattermost.com/administration/plugins.html>`_ as part of the deployment might seem counterintuitive. But they are essential parts of the adoption process, empowering your organization to better understand the tools used by each department.

When choosing integrations and plugins for your deployment, focus on those bringing value to the organization. For example, if your organization is mostly working remotely the Zoom plugin might be essential, whereas a single office organization might not need it but heavily relies on Outlook integration.

Notifications
~~~~~~~~~~~~~

Notifications have gained importance in our daily lives. Modern operating systems all have a way to point the user's attention towards important events from specific apps. There are three different types of notifications in Mattermost: desktop, email, and mobile push notifications. Mattermost will notify you of messages with any of these characteristics:

- Direct Messages.
- Your username or first name is mentioned in a channel.
- A channel you’re in is notified with @channel, @here, or @all.
- Any of `your configured keywords <https://docs.mattermost.com/help/settings/account-settings.html#words-that-trigger-mentions>`_ are used.

.. note::
    
    All notification behavior can be controlled globally or individually by channel. Desktop, email, and mobile push notifications have separate settings.
