Administrator onboarding tasks
==============================

.. include:: ../../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This document provides instructions for common administrator tasks, including some recommendations on tasks to prepare your Mattermost deployment to onboard users.

Getting started tasks
---------------------

1. Once you've installed and deployed Mattermost, ensure all configuration settings are appropriately set under **System Console > Environment** including:

 - Web server
 - Database
 - File storage
 - SMTP
 - Push Notification server
  
These settings can also be set in the ``config.json`` file. Please see our :doc:`configuration settings documentation </administration-guide/configuration-reference/configuration-settings>` for a full listing of all configuration settings.

2. Adjust settings under **System Console > Site Configuration** to brand and customize how users will interact with the site. Be sure to update the Support Email and Help Link in Mattermost under **System Console > Site Configuration > Customization** to provide your users a resource for password resets or questions on their Mattermost account.

 - The Support email is used on email notifications and during tutorial for users to ask support questions.
 - The Help Link is on the Mattermost login page, sign-up pages, and Main Menu and can be used to to link to your help desk ticketing system.
 
These settings can also be set in the ``config.json`` file.  Please see our :doc:`configuration settings documentation </administration-guide/configuration-reference/configuration-settings>` for a full listing of all configuration settings.

3. Begin to onboard users by enabling account creation or by connecting an authentication service to assist with user provisioning.

- Users can be pre-provisioned with migration and bulk loading data processes based on prior collaboration systems. Please see our :ref:`migration guide <administration-guide/getting-started/migrating-to-mattermost:migration guide>` and :doc:`bulk loading documentation </administration-guide/getting-started/bulk-loading-data>` for additional details.
- :doc:`AD/LDAP authentication </administration-guide/identity-access/ad-ldap>` and :doc:`SAML authentication </administration-guide/identity-access/authentication-methods/saml-based-sso/sso-saml>` are available for some subscription plans, providing identity management, single sign-on, and automatic account provisioning.

If your organization requires more structure and project management artifacts for the implementation of Mattermost, please see our :doc:`Enterprise roll out checklist </administration-guide/getting-started/enterprise-roll-out-checklist>`.

Important administration notes 
------------------------------

**DO NOT manipulate the Mattermost database**

- In particular, DO NOT manually delete data from the database directly. Mattermost is designed as a continuous archive and cannot be supported after manual manipulation.
- If you need to permanently delete a team or user, use the :ref:`mmctl user delete <administration-guide/admin-tools/mmctl-command-line-tool:mmctl user delete>` command or the :ref:`mmctl user deletall <administration-guide/admin-tools/mmctl-command-line-tool:mmctl user deleteall>` command.

Common tasks
------------

**Creating System admin account from the command line**

- If the System admin leaves the organization or is otherwise unavailable, you can use the :ref:`mmctl roles <administration-guide/admin-tools/mmctl-command-line-tool:mmctl roles>` commands to assign the *system_admin* role to an existing user. 
- The user needs to log out and log back in before the *system_admin* role is applied.
  
**Migrating to AD/LDAP or SAML from email-based authentication**

- If you have a Mattermost Enterprise or Professional plan, you can migrate from email authentication to Active Directory/LDAP or to SAML Single Sign-on. To set up Active Directory/LDAP, see :doc:`Active Directory/LDAP Setup </administration-guide/identity-access/ad-ldap>`. To set up SAML Single Sign-on, see :doc:`SAML Single-Sign-On </administration-guide/identity-access/authentication-methods/saml-based-sso/sso-saml>`.
- After the new authentication method is enabled, existing users cannot use the new method until they go to **Settings > Security > Sign-in method** and select **Switch to using AD/LDAP** or **Switch to using SAML Single Sign-on**. After they have switched, they can no longer use their email and password to log in.  
  
**Deactivating a user**

- System admins can go to **System Console > Users** for a list of all users on the server. The list can be searched and filtered to make finding the user easier. Click the user's role and in the menu that opens, click **Deactivate**.
- To preserve audit history, users are typically never deleted from the system. If permanently deleting a user is necessary (e.g. for the purposes of `GDPR <https://gdpr-info.eu/>`__), an :doc:`mmctl command </administration-guide/admin-tools/mmctl-command-line-tool>` can be used to do so.
- Note that AD/LDAP user accounts cannot be deactivated from Mattermost; they must be deactivated from your Active Directory.

**Checking for a valid license in Enterprise Edition without logging in**

- Open the log file ``mattermost.log``. It's usually in the ``mattermost/logs/`` directory but might be elsewhere on your system. Find the last occurrence of a log entry that starts with the text ``[INFO] License key``. If the license key is valid, the complete line should be similar to the following example:

.. code-block:: text

  [2017/05/19 16:51:40 UTC] [INFO] License key valid unlocking enterprise features.
      
User experience optimizations
-----------------------------

We highly recommend the following best practices, configuration options, and features for an optimal Mattermost user experience.

**1. Upgrade your Mattermost server**

When you upgrade your Mattermost server frequently, your users can access new features, improved user experiences, bug fixes, security fixes, and mobile app compatibility.

Mattermost releases regular updates to `Mattermost Team Edition <https://mattermost.com/>`_ and `Mattermost Enterprise Edition <https://mattermost.com/pricing/>`_. See the :doc:`release life cycle </product-overview/releases-lifecycle>` documentation for component life cycle details details. 

Upgrading your Mattermost server only takes a few minutes. See the :doc:`Upgrade Guide </administration-guide/operations-scaling/upgrading-mattermost-server>` for step-by-step instructions.

**2. Install plugins**

You can enable plugins and integrations to connect your team's workflows and toolsets into Mattermost. Plugins and integrations customize and extend the Mattermost platform.

**Install and manage plugins**

To enable and manage plugins, go to **System Console > Plugins**. Next, install plugins from **Product menu > Marketplace**. See the `Marketplace  <https://developers.mattermost.com/integrate/admin-guide/admin-plugins-beta/#marketplace>`__ documentation for details.

Consider installing, configuring, and enabling the following community integrations for your users:   
  - Create polls with `Matterpoll <https://mattermost.com/marketplace/matterpoll/>`__.
  - Share GIFs with `GIF Commands <https://mattermost.com/marketplace/giphy-plugin/>`__.
  - Create and share memes with `Memes <https://mattermost.com/marketplace/memes-plugin/>`__.
  - Set personal reminders with `Remind <https://mattermost.com/marketplace/remind-plugin/>`__.
  - Create and share to do items with `Todo <https://github.com/mattermost/mattermost-plugin-todo>`__.
  - Customize welcome messages for new users with `WelcomeBot <https://mattermost.com/marketplace/welcomebot-plugin/>`__.

Explore all plugins and integrations available in the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__.

**Enable and manage integrations**

To enable integrations such as webhooks, slash commands, OAuth2.0, and bots, to go **System Console > Integrations**. More information on these integrations can be found `here <https://developers.mattermost.com/integrate/other-integrations/>`_. 

**3. Enable automatically extended sessions**

Keep your desktop and mobile users logged in and `extend user sessions automatically <https://mattermost.com/blog/session-expiry-experience/>`__ by setting **System Console > Sessions > Extend session length with activity** to **true**. See the :ref:`Extend session length with activity <administration-guide/configuration-reference/environment-configuration-settings:extend session length with activity>` configuration settings documentation for details.

**4. Enable full content push notifications**

Enable push notifications on mobile devices to deliver messages in real time by setting **System Console > Push Notification Server > Enable Push Notifications** to **Use TPNS**. See the :ref:`Push notification server <administration-guide/configuration-reference/environment-configuration-settings:push notification server>` configuration settings documentation for details.

Enable full content push notifications, including the sender’s name, the channel name, and the message text, by setting **System Console > Notifications > Push Notification Contents** to **Full message contents**. See the :ref:`Push notification contents <administration-guide/configuration-reference/site-configuration-settings:push notification contents>` configuration settings documentation for details.

.. note::

  - Mattermost subscription plans allow you to enable HPNS that includes production-level uptime SLAs.

  - Mattermost Enterprise customers can :ref:`enable ID-Only push notifications <administration-guide/configuration-reference/site-configuration-settings:push notification contents>` so push notification content is not passed through Apple Push Notification Service (APNS) or Google Firebase Cloud Messaging (FCM) before reaching the device. The ID-only push notification setting `offers a high level of privacy <https://mattermost.com/blog/id-only-push-notifications/>`__ while allowing team members to benefit from mobile push notifications.

**5. Enable custom emoji**

:doc:`Emojis </end-user-guide/collaborate/react-with-emojis-gifs>` enable users to express concepts such as emotions and physical gestures in messages. Enable the emoji picker by setting **System Console > Emoji > Enable Emoji Picker** to **true**. See the :ref:`Enable emoji picker <administration-guide/configuration-reference/site-configuration-settings:enable emoji picker>` configuration settings documentation for details.

Empower users to create and share their own custom emojis by setting **System Console > Emoji > Enable Custom Emoji** to **true**. See the :ref:`Enable custom emoji <administration-guide/configuration-reference/site-configuration-settings:enable custom emoji>` configuration settings documentation for details.

**6. Enable GIF picker**

GIFs are animated images that can make messaging more fun and engaging. Enable users to access the Mattermost GIF picker from the message draft area by setting **System Console > GIF (Beta) > Enable GIF Picker** to **true**. See the :ref:`Enable GIF picker <administration-guide/configuration-reference/integrations-configuration-settings:enable gif picker>` configuration settings documentation for details.

**7. Enable link previews**

Link previews provide a visual glimpse of relevant content for links shared in messages. Enable link previews by setting **System Console > Posts > Enable Link Previews** to **true**. See the :ref:`Enable link previews <administration-guide/configuration-reference/site-configuration-settings:enable website link previews>` configuration settings documentation for details.
 
**8. Enable batched email notifications**

Email notifications can be batched together so users don’t get overwhelmed with too many emails.

Enable email notifications first by setting **System Console > Notifications > Enable Email Notifications** to **true**. See the :ref:`Enable email notifications <administration-guide/configuration-reference/site-configuration-settings:enable email notifications>` configuration settings documentation for details. Note that email notifications require an :ref:`SMTP email server <administration-guide/configuration-reference/environment-configuration-settings:smtp server>` to be configured.

Then, enable batched email notifications by setting **System Console > Notifications > Enable Email Batching** to **true**. See the :ref:`Enable email batching <administration-guide/configuration-reference/site-configuration-settings:enable email batching>` configuration settings documentation for details. Note that email batching is not available if you are running your deployment in :doc:`High Availability </administration-guide/operations-scaling/high-availability-cluster-based-deployment>`.

**9. Enable Elasticsearch**

Mattermost Enterprise customers can enable :doc:`enterprise search </administration-guide/operations-scaling/enterprise-search>` for optimized search performance at enterprise-scale. Both Elasticsearch and AWS OpenSearch solve many known issues with full text database search, such as dots, dashes, and email addresses returning unexpected results.

Enable Elasticsearch by setting **System Console > Elasticsearch > Enable Indexing** to **true**. See the :ref:`Elasticsearch <administration-guide/configuration-reference/environment-configuration-settings:enterprise search>` configuration settings documentation for details. Enabling Elasticsearch requires :ref:`setting up an Elasticsearch server <administration-guide/operations-scaling/elasticsearch-setup:set up elasticsearch>`.

Checklist overview
-------------------

Prepare for the roll out
~~~~~~~~~~~~~~~~~~~~~~~~

- `1. Define the roll out project`_ 
- `2. Validate essential security and compliance requirements`_ 
- `3. Create development, staging, and production environments`_ 
- `4. Configure and customize your Mattermost site`_  
- `5. Test production performance and redundancy`_ 

Roll out Mattermost
~~~~~~~~~~~~~~~~~~~~

- `1. Define your team and channel strategy`_ 
- `2. Enable key integrations`_ 
- `3. Prepare for user onboarding`_ 
- `4. Deploy client apps`_  
- `5. Roll out to groups of users`_ 
- `6. Drive adoption`_ 

Review the roll out
~~~~~~~~~~~~~~~~~~~

- `1. Review project charter success metrics`_ 
- `2. Review and analyze usage`_ 
- `3. Analyze system performance`_ 
- `4. Harden security`_  
- `5. Perform maintenance tasks`_ 

Checklist details
-------------------

Prepare for the roll out
~~~~~~~~~~~~~~~~~~~~~~~~

Much of the preparation work is focused on ensuring the environment is deployed and secured prior to onboarding users. 

1. Define the roll out project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Define key stakeholders and project team members

 - Example project team members: Project Manager, Network Administrator, Database Administrator, Corporate Directory Administrator, Security & Compliance Administrator(s), User Support, User Champions, User Trainers
  
- Define use cases and requirements for teams, their workflows and their integrations

 - Resource: https://mattermost.com/blog/27-things-enterprises-can-learn-startups-increase-productivity/
 
- Define success criteria, goals and metrics to measure success
  
- Create a Project Charter to document goals, tasks, deliverables, and decisions 

 - Get buy-in from project team members and key stakeholders on the project charter 

2. Validate essential security and compliance requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Review Mattermost security features

 - Resource: https://docs.mattermost.com/security-guide/security-guide-index.html

- Determine monitoring requirements

 - Database, network, storage, log integrity
 - Identify fields for log management tools (e.g. Splunk Enterprise event data)

- Determine environment access policies

 - Network access, physical access, group controlled access

- Determine encryption policies

 - Resource: https://docs.mattermost.com/deployment-guide/encryption-options.html
 - Resource: https://docs.mattermost.com/deployment-guide/transport-encryption.html

- Determine system administration access policies

 - Identify the list of users or groups who need administrative access for Mattermost System Console, Command Line Tools, and API privileges

- Define and configure authentication policies

 - Resource: https://docs.mattermost.com/product-overview/corporate-directory-integration.html

- Determine requirements for multi-factor authentication

 - Resource: https://docs.mattermost.com/administration-guide/identity-access/multi-factor-authentication.html

- Configure and test SSO or Corporate Directory integration (SAML or AD/LDAP)

 - Resource: https://docs.mattermost.com/administration-guide/identity-access/authentication-methods/saml-based-sso/sso-saml.html
 - Resource: https://docs.mattermost.com/administration-guide/identity-access/ad-ldap.html

- Define your mobile usage policy

 - Resource: https://docs.mattermost.com/deployment-guide/mobile/mobile-app-deployment.html

- Evaluate external network access requirements
 
 - The `Mattermost Marketplace <https://mattermost.com/marketplace>`_ is a service hosted by Mattermost that functions as a central place to store the current versions of available Mattermost integrations.  See :ref:`Enable Remote Marketplace <administration-guide/configuration-reference/plugins-configuration-settings:enable remote marketplace>` documentation for details about required external network access.
 - Mattermost supports external GIF providers. See :ref:`GIF Commands <administration-guide/configuration-reference/integrations-configuration-settings:enable gif picker>` configuration documentation for details about required external network access.

3. Create development, staging, and production environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Finalize production environment design basing hardware on expected usage and requirements for high availability

 - Resource: https://docs.mattermost.com/deployment-guide/application-architecture.html
 - Resource: https://docs.mattermost.com/deployment-guide/deployment-guide-index.html 
 - Resource: https://docs.mattermost.com/administration-guide/operations-scaling/scaling-for-enterprise.html 
 - Resource: https://docs.mattermost.com/administration-guide/operations-scaling/high-availability-cluster-based-deployment.html

- Create development and staging environments

 - Recommend using to test early configurations for database, authentication, file storage, Elasticsearch, prior to setting up high availability and load balancing 
 - Recommend configuring staging to be an identical replication of your production environment

- Create a production environment

 - Install Mattermost

  - Install the number of nodes based on your high availability requirements outlined in your production environment design
  - Recommendation: Use Kubernetes and the Mattermost Operator, with external supported external database and file storage solutions. This will also provide blue/green deployment, rolling upgrades, and canary builds

   - Resource: https://docs.mattermost.com/deployment-guide/server/deploy-kubernetes.html

 - Install and configure database

  - Install the number of read and search replicas based on your high availability requirements outlined in your production environment design

   - Resource: https://docs.mattermost.com/deployment-guide/server/server-architecture.html#database-with-virtual-ips

  - (Optional) Set up configuration management via the database instead of a config file for high available environments

   - Resource: https://docs.mattermost.com/administration-guide/configuration-reference/configuration-in-your-database.html

 - Install and configure File Storage

  - Resource: https://docs.mattermost.com/deployment-guide/server/preparations.html#file-storage-preparation

 - Install and configure proxy or load balancers

  - Note: If running Kubernetes and the Mattermost Operator, proxies will be created automatically. 
  - Add SSL Cert

   - Resource: https://docs.mattermost.com/administration-guide/identity-access/ssl-client-certificate.html
   - Resource: https://docs.mattermost.com/administration-guide/operations-scaling/high-availability-cluster-based-deployment.html#proxy-server-configuration

  - (Optional) Set up certificate-based authentication (CBA) for user or device-based authentication with a digital certificate

   - Resource: https://docs.mattermost.com/administration-guide/identity-access/certificate-based-authentication.html

 - Configure SMTP for email notifications

  - Resource: https://docs.mattermost.com/administration-guide/configuration-reference/smtp-email.html

 - Set up Elasticsearch (highly recommended if your organization anticipates over two million posts)

  - Resource: https://docs.mattermost.com/administration-guide/operations-scaling/elasticsearch-setup.html

- Document network configuration

 - Example: https://docs.mattermost.com/administration-guide/operations-scaling/backing-storage-benchmarks.html 

4. Configure and customize your Mattermost site
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Login to Mattermost and access the System Console to connect your environment to Mattermost

 - Resource: https://docs.mattermost.com/administration-guide/configuration-reference/configuration-settings.html#environment-variables
 - Upload your valid Enterprise License under Edition and License
 - Ensure site URL is set appropriately for your production, dev and staging environments
 - Add your database configuration to **System Console > Environment > Database**
 - Add your Elasticsearch or AWS OpenSearch configuration to **System Console > Environment > Elasticsearch**
 - Add your file storage system configuration to **System Console > Environment > File Storage** 
 - Add your proxy configuration to **System Console > Environment > Image Proxy** 
 - Add your SMTP configuration to **System Console > Environment > SMTP**
 - Enable Push Notifications by adding your server to **System Console > Environment > Push Notification Server**
 - Add your cluster configuration to **System Console > Environment > High Availability**

- Configure your site within the System Console

 - Resource: https://docs.mattermost.com/administration-guide/configuration-reference/configuration-settings.html#site-configuration

- Set site access policies including permissions for roles and guest access

 - Permissions Resource: https://docs.mattermost.com/administration-guide/onboard/advanced-permissions.html
 - Guest Access Resource: https://docs.mattermost.com/administration-guide/onboard/guest-accounts.html

5. Test production performance and redundancy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Define and test disaster recovery policy and processes

 - Resource: https://docs.mattermost.com/deployment-guide/server/deploy-kubernetes.html
 - Resource: https://docs.mattermost.com/administration-guide/operations-scaling/high-availability-cluster-based-deployment.html#upgrade-guide 

- Performance test production environment

 - Load test production environment to verify that it will handle anticipated user load

  - Resource: https://github.com/mattermost/mattermost-load-test

 - Set up Prometheus and Grafana to monitor performance

  - Resource: https://docs.mattermost.com/administration-guide/operations-scaling/deploy-prometheus-grafana-for-performance-monitoring.html 

 - Set up alerts in Grafana

  - Resource: https://docs.mattermost.com/administration-guide/operations-scaling/deploy-prometheus-grafana-for-performance-monitoring.html

Roll out Mattermost
~~~~~~~~~~~~~~~~~~~
Now that you have an environment in place, we recommend working through the following items in an iterative process. You may need to cycle through each of these topics multiple times to make adjustments to suit your organization as you onboard groups of users. 

1. Define your team and channel strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Determine and create a team structure for your environment

 - Recommendation: Start with fewer teams in your early roll out
 - Resource: https://docs.mattermost.com/end-user-guide/collaborate/channel-naming-conventions.html 

- Determine and create key channels to support your users. A default Town Square channel is created automatically and available on every team.

 - Recommendation: Add a “Support” channel for your users to escalate questions 

- (Optional) Migrate messages and channels from legacy systems

 - Resource: https://docs.mattermost.com/administration-guide/getting-started/migrating-to-mattermost.html

2. Enable key integrations
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Build the list of key integrations and tools used by your teams

 - Resource: https://developers.mattermost.com/integrate/getting-started/

- Define use cases and requirements for plugins, bots, webhooks, slash commands 

 - Resource: https://developers.mattermost.com/integrate/other-integrations/

- Set up key integrations (or migrate from POC environments)

 - Resource: https://mattermost.com/marketplace/

- Understand Mattermost API capabilities

 - Resource: https://api.mattermost.com/

3. Prepare for user onboarding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Onboard champion users 

- Onboard trainers and support team
- Create a training plan

 - Resource: https://academy.mattermost.com/

- Define user escalation and support processes

 - Ensure you have set the site’s support URL to your own support team under **System Console > Site Configuration > Customization**

- Notify users in advance of roll out

 - Sample email: https://docs.mattermost.com/administration-guide/operations-scaling/welcome-email-to-end-users.html

4. Deploy client apps
^^^^^^^^^^^^^^^^^^^^^

- Roll out desktop app 

 - Resource: https://docs.mattermost.com/deployment-guide/desktop/desktop-app-deployment.html
 - (Optional) Use the MSI installer to install on Windows machines

  - Resource: https://docs.mattermost.com/deployment-guide/desktop/desktop-msi-installer-and-group-policy-install.html

- Roll out mobile app

 - Resource: https://docs.mattermost.com/deployment-guide/mobile/mobile-app-deployment.html
 - (Optional) Use an EMM provider

  - Resource: https://docs.mattermost.com/deployment-guide/mobile/deploy-mobile-apps-using-emm-provider.html 

5. Roll out to groups of users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Provision user accounts

 - Resource: https://docs.mattermost.com/administration-guide/onboard/user-provisioning-workflows.html 

- (Optional) Bulk Load users

 - Resource: https://docs.mattermost.com/administration-guide/getting-started/bulk-loading-data.html 

- Onboard users to teams and channels

 - Recommendation: Use LDAP Group Sync to automate this process

  - Resource: https://docs.mattermost.com/administration-guide/identity-access/ad-ldap-groups-synchronization.html

- Implement your training plan to end users on how to use Mattermost

 - Train on using Mattermost
 - Train on how to use integrations

6. Drive adoption
^^^^^^^^^^^^^^^^^

- Incrementally roll out to additional user groups

 - See “Roll Out to Groups of Users”

- Manage support requests and product requests from your end users

 - Resource: https://mattermost.com/support/ 
 - See the process below for escalating to Mattermost

- Enable additional integrations and plugins to support user workflows

 - Resource: https://mattermost.com/marketplace/

- Understand management tools available to support users

 - mmctl Command Line Tool Resource: https://docs.mattermost.com/administration-guide/admin-tools/mmctl-command-line-tool.html
 - Command Line Tools Resource: https://docs.mattermost.com/administration-guide/admin-tools/command-line-tools.html

Review the roll out 
~~~~~~~~~~~~~~~~~~~

We recommend that you review your rollout on a cadence that matches your iterative approach to rolling out to users. Below are some areas to consider.  

1. Review project charter success metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Perform end-user surveys and measure satisfaction

- Verify use case fulfillment from original requirements gathering

- Measure your response time and resolution rate for user support issues

- Identify usage gaps and address or create a plan for addressing

2. Review and analyze usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Review Project Charter success metrics - identify usage gaps and address or create a plan for addressing

- Monitor site and team statistics

 - Resource: https://docs.mattermost.com/administration-guide/admin-tools/statistics.html 
 - Review: Total posts, total teams, total channels, total group chats, total direct chats, top channels, top teams

- Analyze usage by lines of business and peak usage times

3. Analyze system performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Monitor trends in CPU/memory usage

- Review trends in database connections

- Review trends in Go routines 

- Review trends in concurrent sessions 

4. Harden security
^^^^^^^^^^^^^^^^^^

- Harden security controls around the web, desktop, and mobile security

- Harden configuration management 

- Harden network security

 - Identify additional tests and scans
 - (Optional) Enable Compliance Reporting

  - Resource: https://docs.mattermost.com/administration-guide/compliance-security-auditing/compliance-export.html

5. Perform maintenance tasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Monitor for security updates (or sign up for email updates)

 - Resource: https://mattermost.com/security-updates/

- Perform the first upgrade

 - Resource: https://docs.mattermost.com/administration-guide/operations-scaling/upgrading-mattermost-server.html

- Determine upgrade schedule based on Mattermost release schedules and life cycle

 - Resource: https://docs.mattermost.com/product-overview/releases-lifecycle.html

- Run System checks and either address or set address-by date	


- :doc:`Welcome email to end users </administration-guide/operations-scaling/welcome-email-to-end-users>`
