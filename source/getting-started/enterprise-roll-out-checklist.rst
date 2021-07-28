Enterprise Roll Out Checklist
==============================

This checklist is intended to serve as a guide to Enterprises who are rolling out Mattermost to thousands of users. 

Checklist Overview
-------------------

  - `Prepare for the Roll Out`_ 
   - `1. Define the Roll Out Project`_ 
   - `2. Validate Essential Security and Compliance Requirements`_ 
   - `3. Create Development, Staging, and Production Environments`_ 
   - `4. Configure and Customize Your Mattermost Site`_  
   - `5. Test Production Performance and Redundancy`_ 
  - `Roll Out Mattermost`_ 
   - `1. Define Your Team and Channel Strategy`_ 
   - `2. Enable Key Integrations`_ 
   - `3. Prepare for User Onboarding`_ 
   - `4. Deploy Client Apps`_  
   - `5. Roll Out to Groups of Users`_ 
   - `6. Drive Adoption`_ 
  - `Review the Roll Out`_ 
   - `1. Review Project Charter Success Metrics`_ 
   - `2. Review and Analyze Usage`_ 
   - `3. Analyze System Performance`_ 
   - `4. Harden Security`_  
   - `5. Perform Maintenance Tasks`_ 
   
Checklist Details
-------------------

Prepare for the Roll Out
~~~~~~~~~~~~~~~~~~~~~~~~

Much of the preparation work is focused on ensuring the environment is deployed and secured prior to onboarding users. 

1. Define the Roll Out Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Define key stakeholders and project team members
 - Example project team members: Project Manager, Network Administrator, Database Administrator, Corporate Directory Administrator, Security & Compliance Administrator(s), User Support, User Champions, User Trainers
  
- Define use cases and requirements for teams, their workflows and their integrations
 - Resource: https://mattermost.com/blog/27-things-enterprises-can-learn-startups-increase-productivity/
 
- Define success criteria, goals and metrics to measure success
 - Resource: https://docs.mattermost.com/getting-started/implementation-plan.html
  
- Create a Project Charter to document goals, tasks, deliverables, and decisions 
 - Get buy-in from project team members and key stakeholders on the project charter 

2. Validate Essential Security and Compliance Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Review Mattermost security features
 - Resource: https://docs.mattermost.com/overview/security.html#security-features
 
- Determine monitoring requirements
 - Database, network, storage, log integrity
 - Identify fields for log management tools (e.g. Splunk Enterprise event data)

- Determine environment access policies
 - Network access, physical access, group controlled access

- Determine encryption policies
 - Resource: https://docs.mattermost.com/deploy/encryption-options.html
 - Resource: https://docs.mattermost.com/install/transport-encryption.html

- Determine System Administration access policies
 - Identify list of users or groups who need administrative access for Mattermost System Console, Command Line Tools and API privileges

- Define and configure authentication policies
 - Resource: https://docs.mattermost.com/about/corporate-directory-integration.html 
- Determine requirements for multi-factor authentication
 - Resource: https://docs.mattermost.com/onboard/multi-factor-authentication.html

- Configure and test SSO or Corporate Directory integration (SAML or AD/LDAP)
 - Resource: https://docs.mattermost.com/onboard/sso-saml.html
 - Resource: https://docs.mattermost.com/onboard/ad-ldap.html

- Define your mobile usage policy
 - Resource: https://docs.mattermost.com/deploy/mobile-overview.html
 - Resource: https://docs.mattermost.com/deployment/mobile-app-deployment.html

3. Create Development, Staging, and Production Environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Finalize production environment design basing hardware on expected usage and requirements for high availability
 - Resource: https://docs.mattermost.com/getting-started/architecture-overview.html
 - Resource: https://docs.mattermost.com/deployment/deployment.html 
 - Resource: https://docs.mattermost.com/scale/scaling-for-enterprise.html 
 - Resource: https://docs.mattermost.com/scale/high-availability-cluster.html

- Create development and staging environments 
 - Recommend using to test early configurations for database, authentication, file storage, Elasticsearch, prior to setting up high availability and load balancing 
 - Recommend configuring staging to be an identical replication of your production environment

- Create production environment
 - Install Mattermost
  - Install the number of nodes based on your high availability requirements outlined in your production environment design
  - Recommendation: Use Kubernetes and the Mattermost Operator, with external supported external database and file storage solutions. This will also provide blue/green deployment, rolling upgrades, and canary builds
   - Resource: https://docs.mattermost.com/install/install-kubernetes.html 
 - Install and configure database
  - Install the number of read and search replicas based on your high availability requirements outlined in your production environment design
   - Resource: https://docs.mattermost.com/overview/architecture.html#database-with-vips 
  - (Optional) Set up configuration management via the database instead of a config file for high available environments
   - Resource: https://docs.mattermost.com/administration/config-in-database.html
 - Install and configure File Storage
  - Resource: https://docs.mattermost.com/deployment/deployment.html#file-store
 - Install and configure proxy or load balancers
  - Note: If running Kubernetes and the Mattermost Operator, proxies will be created automatically. 
  - Add SSL Cert
   - Resource: https://docs.mattermost.com/deployment/ssl-client-certificate.html
   - Resource: https://docs.mattermost.com/deployment/cluster.html#proxy-server-configuration 
  - (Optional) Set up certificate-based authentication (CBA) for user or device-based authentication with a digital certificate
   - Resource: https://docs.mattermost.com/deployment/certificate-based-authentication.html
 - Configure SMTP for email notifications
  - Resource: https://docs.mattermost.com/install/smtp-email-setup.html
 - Set up Elasticsearch (highly recommended if your organization anticipates over 2 million posts)
  - Resource: https://docs.mattermost.com/deployment/elasticsearch.html

- Document network configuration
 - Example: https://docs.mattermost.com/overview/architecture.html#reference-architectures  

4. Configure and Customize Your Mattermost Site
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Login to Mattermost and access the System Console to connect your environment to Mattermost
 - Resource: https://docs.mattermost.com/administration/config-settings.html#environment
 - Upload your valid Enterprise License under Edition and License
 - Ensure site URL is set appropriately for your production, dev and staging environments
 - Add your database configuration to **System Console > Environment > Database**
 - Add your Elasticsearch configuration to **System Console > Environment > Elasticsearch**
 - Add your file storage system configuration to **System Console > Environment > File Storage** 
 - Add your proxy configuration to **System Console > Environment > Image Proxy** 
 - Add your SMTP configuration to **System Console > Environment > SMTP**
 - Enable Push Notifications by adding your server to **System Console > Environment > Push Notification Server**
 - Add your cluster configuration to **System Console > Environment > High Availability**

- Configure your site within the System Console
 - Resource: https://docs.mattermost.com/administration/config-settings.html#site-configuration

- Set site access policies including permissions for roles and guest access
 - Permissions Resource: https://docs.mattermost.com/deployment/advanced-permissions.html
 - Guest Access Resource: https://docs.mattermost.com/deployment/guest-accounts.html

5. Test Production Performance and Redundancy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Define and test disaster recovery policy and processes
 - Resource: https://docs.mattermost.com/install/install-kubernetes.html#using-mattermost-operator-functionality
 - Resource: https://docs.mattermost.com/deployment/cluster.html#upgrade-guide 

- Performance test production environment
 - Load test production environment to verify that it will handle anticipated user load
  - Resource: https://github.com/mattermost/mattermost-load-test 
 - Set up Prometheus and Grafana to monitor performance
  - Resource: https://docs.mattermost.com/deployment/metrics.html 
 - Set up alerts in Grafana
  - Resource: https://docs.mattermost.com/administration/performance-alerting-guide.html 

Roll Out Mattermost
~~~~~~~~~~~~~~~~~~~
Now that you have an environment in place, we recommend working through the following items in an iterative process. You may need to cycle through each of these topics multiple times to make adjustments to suit your organization as you onboard groups of users. 

1. Define Your Team and Channel Strategy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Determine and create team structure for your environment
 - Recommendation: Start with fewer teams in your early roll out
 - Resource: https://docs.mattermost.com/help/getting-started/organizing.html 

- Determine and create key channels to support your users. Town Square and Off-Topic are built in channels in every team
 - Recommendation: Add a “Support” channel for your users to escalate questions 

- (Optional) Migrate messages and channels from legacy systems 
 - Resource: https://docs.mattermost.com/administration/migrating.html

2. Enable Key Integrations
^^^^^^^^^^^^^^^^^^^^^^^^^^

- Build list of key integrations and tools used by your teams
 - Resource: https://docs.mattermost.com/guides/administrator.html#mattermost-integrations

- Define use cases and requirements for plugins, bots, webhooks, slash commands 
 - Resource: https://docs.mattermost.com/guides/integration.html

- Set up key integrations (or migrate from POC environments)
 - Resource: https://integrations.mattermost.com/

- Understand Mattermost API capabilities
 - Resource: https://api.mattermost.com/

3. Prepare for User Onboarding
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Onboard champion users 

- Onboard trainers and support team
- Create a training plan
 - Resource: https://academy.mattermost.com/
 - Resource: End User Guide https://docs.mattermost.com/guides/user.html  

- Define user escalation and support processes
 - Ensure you have set the site’s support URL to your own support team under **System Console > Site Configuration > Customization**

- Notify users in advance of roll out
 - Sample email: https://docs.mattermost.com/getting-started/welcome_email.html

4. Deploy Client Apps
^^^^^^^^^^^^^^^^^^^^^

- Roll out Desktop App 
 - Resource: https://docs.mattermost.com/install/desktop.html
 - Resource: https://docs.mattermost.com/deployment/desktop-app-deployment.html
 - (Optional) Use the MSI installer to install on Windows machines
  - Resource: https://docs.mattermost.com/install/desktop-msi-gpo.html

- Roll out Mobile App
 - Resource: https://docs.mattermost.com/deployment/mobile-app-deployment.html
 - (Optional) Use an EMM provider
  - Resource: https://docs.mattermost.com/mobile/mobile-overview.html#use-an-emm-provider-with-managed-app-configuration 

5. Roll Out to Groups of Users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Provision user accounts
 - Resource: https://docs.mattermost.com/administration/user-provisioning.html 

- (Optional) Bulk Load users
 - Resource: https://docs.mattermost.com/deployment/bulk-loading.html 

- Onboard users to teams and channels
 - Recommendation: Use LDAP Group Sync to automate this process
  - Resource: https://docs.mattermost.com/deployment/ldap-group-sync.html

- Implement your training plan to end users on how to use Mattermost 
 - Train on using Mattermost
 - Train on how to use integrations

6. Drive Adoption
^^^^^^^^^^^^^^^^^

- Incrementally roll out to additional user groups
 - See “Roll Out to Groups of Users”

- Manage support requests and product requests from your end users
 - Resource: https://mattermost.com/support/ 
 - See process below for escalating to Mattermost

- Enable additional integrations and plugins to support user workflows
 - Resource: https://integrations.mattermost.com/

- Understand management tools available to support users
 - Command Line Tools Resource: https://docs.mattermost.com/administration/command-line-tools.html
 - Database Scripts Resource: https://docs.mattermost.com/administration/scripts.html 

Review the Roll Out 
~~~~~~~~~~~~~~~~~~~

We recommend that you review your rollout on a cadence that matches your iterative approach to rolling out to users. Below are some areas to consider.  

1. Review Project Charter Success Metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Perform end-user surveys and measure satisfaction
 - Optional resource within Mattermost: https://integrations.mattermost.com/matterpoll/

- Verify use case fulfillment from original requirements gathering

- Measure your response time and resolution rate for user support issues

- Identify usage gaps and address or create a plan for addressing

2. Review and Analyze Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Review Project Charter success metrics - identify usage gaps and address or create a plan for addressing

- Monitor site and team statistics 
 - Resource: https://docs.mattermost.com/administration/statistics.html 
 - Review: Total posts, total teams, total channels, total group chats, total direct chats, top channels, top teams

- Analyze usage by lines of business and peak usage times
 - Resources: https://docs.mattermost.com/administration/scripts.html

3. Analyze System Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Monitor trends in CPU/memory usage

- Review trends in database connections

- Review trends in Go routines 

- Review trends in concurrent sessions 

4. Harden Security
^^^^^^^^^^^^^^^^^^

- Harden security controls around web, desktop and mobile security

- Harden configuration management 

- Harden network security
 - Identify additional tests and scans
 - (Optional) Enable Compliance Reporting
  - Resource: https://docs.mattermost.com/administration/compliance-export.html

5. Perform Maintenance Tasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Monitor for security updates (or sign up for email updates)
 - Resource: https://mattermost.com/security-updates/

- Perform first upgrade
 - Resource: https://docs.mattermost.com/administration/upgrade.html

- Determine upgrade schedule based on Mattermost release schedules and lifecycle
 - Resource: https://docs.mattermost.com/administration/release-lifecycle.html

- Run System checks and either address or set address-by date	
