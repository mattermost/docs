###########################
Enterprise Deployment Guide
###########################

================
About This Guide
================

********
Audience
********

IT Leaders, System Administrators, and/or Project Managers

.. Note::
    Some features described in this guide are only available to E10 and/or E20 (Enterprise Edition). We will highlight specific licenses needed whenever applicable.

*******************
Learning Objectives
*******************

This guide provides foundational information necessary when developing a plan for a proof of concept and/or production-level enterprise deployment of the Mattermost on-premises edition. 

It will not dive into the technical implementation, but will reference any relevant documentation.

By the end of this guide you should have an understanding of the high-level requirements for a successful Mattermost Enterprise deployment. 

This includes:

- Choosing how to deploy the Mattermost Server application
- Migrating from other ChatOps platforms
- Integrating Mattermost with existing Single Sign-On providers
- First Steps/Best Practices for Onboarding Users

*******
Support
*******

If at any point you need additional help, we’re ready to assist, just reach out using any of these methods:

- Community  - Our entire team is active within our public instance of Mattermost, plus you’ll have the support of one of the best open source communities around
- Documentation - We link to many parts of our `administrator  documentation <https://docs.mattermost.com/guides/administrator.html>`_ in this guide but encourage you to take a look at `all our documentation <https://docs.mattermost.com>`_
- Enterprise Support  - If you’re an Enterprise Edition subscriber, you may open a support ticket in the Enterprise Edition Support portal

.. Recommendation::
    Open our public instance of Mattermost right now in a separate browser tab and create a user. Join channel ..::TODO Specific Guide Support Channel?::.. to not only experience Mattermost right away but to ask if getting stuck at any point in this guide.

================================
Before You Begin Your Deployment
================================

********************************
What Makes Mattermost Different?
********************************

Mattermost is a high-trust messaging platform for enterprise use. As enterprises come in all shapes and sizes, Mattermost has been built to provide an optimal experience for all customers. 

Taking this a step further, the emergence of ChatOps means Mattermost is no longer an exclusive developer tool. In fact, it has the ability to enhance communication through a multitude of integrations, extensions, and customization.

Here’s just a sample of available integrations our customers are deploying:

- Confluence
- Docker
- GitHub / GitLab
- Jira
- Outlook
- Trello

Taking this further, because Mattermost is an Open Source application, it can be completely customized, in every way, to suit your organizational needs.

***************
Further Reading
***************

Mattermost Licensing
--------------------

Mattermost Enterprise Edition comes with two licensing options: Enterprise E10 and Enterprise E20 which can be tested with a `Free 30-Day Trial <https://mattermost.com/trial/>`_. We tailored the E10 licence to suit smaller organizations with less need for automation and compliance, where our E20 license will provide you with features like ADFS SAML 2.0 support, automated compliance export and team specific permissions. You can find a full comparison `here <https://mattermost.com/pricing-feature-comparison>`_.


.. Note::
    Reach out to our Sales team by contacting sales@mattermost.com to upgrade your license at any time.

Mattermost Server Environment
-----------------------------

At its core, Mattermost is an open source, hybrid-cloud alternative to proprietary SaaS messaging for teams. It is designed to increase the agility, efficiency and innovation in high trust organizations while keeping data and operations under IT control. Mattermost ensures you can own your data. An important step is to determine the environment for the Mattermost server.

We officially support running the Mattermost Server on multiple `Linux distributions, Docker and on-premises cloud solutions <https://docs.mattermost.com/guides/administrator.html#installing-mattermost>`_.

.. Note::
    Other Linux distributions might work too, but are not officially supported.

Client Usage
------------

Depending on your environment and your users, you have several options when deploying the Mattermost Client: Web Browser, `Desktop <https://docs.mattermost.com/install/desktop.html>`_, `Mobile <https://docs.mattermost.com/mobile/mobile-overview.html>`_ or all three. We `provide binaries <https://mattermost.com/download/#mattermostApps>`_ for MS Windows, macOS, Linux, iOS and Android. However, depending on your organization policies deployment on these platforms can vary.

======================
Deployment First Steps
======================

Deploying Mattermost Enterprise is not a small project. Depending on your use-case multiple physical machines have to be set up with Mattermost server, a proxy and a database while thousands of users need to be imported through AD/FS. While we strive to make this as easy as possible it will take time and iteration.

***********************
Determine Your Use-Case
***********************

As mentioned above it is essential for a successful deployment to know your specific use-case. To get started try answering the following questions:

- How many users will use Mattermost on initial deployment and is this number going to increase dramatically in the near future?
- What clients will be in use?
- Are you migrating from an existing ChatOps or different communications platform?
- Are you using an identity provider for single sign-on and if yes which one?
- What compliance requirements do you need to meet?
- What are your organization's security requirements?

************************
Planning Your Deployment
************************

Technical Requirements
----------------------

The hardware requirements for the Mattermost server and database `grow with the amount of users they need to support <https://jeffschering.github.io/mmdocs/upgrade/install/requirements.html#hardware-requirements>`_.

Depending on which clients your users will work with additional reading can be necessary:
- You are going to use the web app - no further reading required.
- You are going to use the desktop app - please also read `Desktop Application Install Guides <https://docs.mattermost.com/install/desktop.html>`_.
- You are going to use the mobile app - please also read `Mobile App Deployment Guide <https://docs.mattermost.com/deployment/mobile-app-deployment.html>`_.

Migration
---------

When migrating from an existing solution it is important to plan ahead. We recommend starting with a small dataset - limited users and content - to reduce the time spent debugging and ensuring all fields are imported correctly, before taking on a major import.

We provide our customers with easy to use migration solutions for many scenarios:

- Mattermost - Migrating from Mattermost Team Edition is common and only requires you to `upgrade to the most recent Enterprise Edition <https://docs.mattermost.com/administration/upgrade.html#upgrading-team-edition-to-enterprise-edition>`_ and add your License Key.
- Slack - There is support for two methods of importing data from Slack.
    - For small datasets with few users and without post attachments the `Mattermost Web App can be used <https://docs.mattermost.com/administration/migrating.html?highlight=slack#migrating-from-slack-using-the-mattermost-web-app>`_.
    - If at all possible we recommend the use of `Mattermost CLI for the migration process <https://docs.mattermost.com/administration/migrating.html?highlight=slack#migrating-from-slack-using-the-mattermost-cli>`_.
- HipChat - We recommend using `Group Export Dashboard <https://docs.mattermost.com/administration/hipchat-migration-guidelines.html>`_ to export your data in combination with the `Mattermost Bulk Load Tool <https://docs.mattermost.com/deployment/bulk-loading.html>`_.
- Jabber - You can use `BrightScout’s Extract, Transform and Load (ETL) <https://github.com/Brightscout/mattermost-etl>`_ tool to migrate from Jabber.
- Bespoke Messaging Solutions - Mattermost is designed to replace bespoke messaging solutions and provide additional `security features <https://docs.mattermost.com/overview/security.html>`_, but migrating from bespoke messengers can prove to be challenging, because the data format of such tools is unpredictable. Nonetheless we provide `multiple tools <https://docs.mattermost.com/administration/migrating.html?highlight=slack#bringing-data-from-bespoke-solutions-into-mattermost>`_ to attempt migration and have had many successful migrations with our customers.

.. Note::
    If your data in the bespoke messenger is not vital we recommend a hard switch after a period of running both systems in parallel.

Single Sign-On
--------------

Mattermost can act as a `SAML 2.0 <https://docs.mattermost.com/deployment/sso-saml.html>`_ provider so setting up single sign-on is a straightforward matter.

We support these SSO-Services:

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

- Outbound Proxy - In some scenarios, like monitoring outbound traffic or controlling which websites can appear in link previews, you may wish to `use Mattermost behind a proxy <https://docs.mattermost.com/install/outbound-proxy.html>`_
- Electronic Discovery - Electronic Discovery (eDiscovery) is the process of searching electronic data to be used as evidence in a legal case. We have put together the `eDiscovery documentation <https://docs.mattermost.com/administration/ediscovery.html>`_ to help.
- Compliance Export - This feature enables `compliance exports <https://docs.mattermost.com/administration/compliance-export.html>`_ to be produced from the System Console, containing all messages
- Data Retention - By default, Mattermost provides unlimited search history storing all messages without an expiration date. These defaults can be `changed by setting Message Retention and File Retention <https://docs.mattermost.com/administration/data-retention.html>`_ to a specific duration in the System Console.
- Custom Terms of Service - If your Organization requires the use of `custom ToS <https://docs.mattermost.com/administration/custom-terms-of-service.html>`_, this can be done in the Mattermost System Console.

Security
--------

Security is a major concern with regard to selecting the right tools. Mattermost software is continually reviewed for security by developers, IT administrators and security researchers. In contrast to SaaS solutions mattermost can be deployed on premises in your private cloud giving you full control of not only the software but the hardware side as well. Here is a non exhausting list of our security features: 

- Private Cloud Deployment
- Secure Mobile Apps
- Transmission Security
- Integrity and Audit Controls
- Authentication Safeguards
- Access Control Policy
- More details on this topic are available at the `Mattermost security <https://docs.mattermost.com/overview/security.html>`_ section in our documentation.
- HIPAA und FINRA - Mattermost can be deployed `Health Insurance Portability and Accountability Act - HIPAA <https://docs.mattermost.com/overview/security.html#hipaa-compliance>`_ and `Financial Industry Regulatory Authority - FINRA <https://docs.mattermost.com/overview/security.html#finra-compliance>`_ compliant.
- Certificate-Based Authentication - `Certificate-Based Authentication <https://docs.mattermost.com/deployment/certificate-based-authentication.html>`_ is available as an experimental feature.
- Multi Factor Authentication - Mattermost supports `multi factor authentication <https://docs.mattermost.com/deployment/auth.html>`_.

============================
User Onboarding and Adoption
============================

************************
Integrations and Plugins
************************

On the first look considering `integrations <https://integrations.mattermost.com>`_ and `plugins <https://docs.mattermost.com/administration/plugins.html>`_ as part of the deployment might seem counterintuitive. But they are essential parts of the adoption process, empowering your organization to better understand the tools used by each department.

When choosing integrations and plugins for your deployment focus on those bringing value to the organization. E.g. if your organization is mostly working remotely the Zoom-Plugin might be essential, whereas a single office organization might not need it but heavily relies on Outlook integration.

*************
Notifications
*************

Notifications have gained importance in our daily lives. Modern operating systems all have a way to point their users attention towards important events from specific apps. There are three different types of notifications in Mattermost - desktop, email and mobile push notifications. Mattermost will notify you of messages with any of these characteristics:

- Direct Messages addressed to you
- Your username or first name is mentioned in a channel
- A channel you’re in using is notified with @channel or @all
- Any of `your configured keywords <https://docs.mattermost.com/help/settings/account-settings.html#words-that-trigger-mentions>`_ are used

.. Note::
    All notification behaviour can be controlled globally or individually by channel. Desktop, email and mobile push notifications have separate settings.
