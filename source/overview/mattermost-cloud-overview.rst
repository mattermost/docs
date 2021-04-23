=========================
Mattermost Cloud Overview
=========================

Mattermost Cloud delivers the industry’s leading open-source collaboration platform in a highly secure, dedicated cloud environment designed for privacy-conscious enterprises and developer collaboration.

Mattermost Cloud is built on open-source software powered by a thriving developer community. The open-source approach enables software with a modular architecture, built with modern software development practices. Open-source development and provides transparency in source code, extensibility, and public trust. Mattermost Cloud comes in two editions: Mattermost Cloud Professional and Mattermost Cloud Enterprise.

Mattermost Cloud Professional
-----------------------------

Mattermost Cloud Professional includes the full set of collaboration and DevOps features and is available from the Mattermost.com website. Signing up requires creating an account with an email and specifying a domain for the workspace. Once you sign up and create your workspace, a wizard will guide you through a quick setup, invitation for team members, and integration with developer tools. You can trial Mattermost Cloud Professional for free for 14 days.

Mattermost Cloud Professional offers all enterprise-grade administration features, including:

 - **Identity Management:** Single Sign-on, SAML and AD/LDAP user and group provisioning, guest management, and enterprise mobility management.
 - **Governance:** Message and file retention policies, system and team permission policies, custom terms of service, channel moderation settings, and compliance exports.  

To get started with Mattermost Cloud Professional, visit https://mattermost.com/mattermost-cloud.

Mattermost Cloud Enterprise
---------------------------

Mattermost Cloud Enterprise offers the isolation, security, and control of self-hosted editions but without the burden of managing deployment, maintaining uptime, or applying upgrades. Mattermost Cloud Enterprise offers all chat and administration features, integrated DevOps workflows, provides a 99.0% financially-backed guaranteed uptime, and enterprise-grade support.
  
Every Mattermost Cloud Enterprise instance is deployed in a private environment within an AWS VPC dedicated to a single customer. Within that VPC, all the required resources to run, monitor, and administer Mattermost are deployed in isolation. These resources include a dedicated RDS Aurora database cluster and a dedicated Kubernetes cluster, deployed across multiple Availability Zones and managed by Kubernetes experts.

This intentional isolation and dedicated deployment supports other privacy-centric features, such as VPC Peering, bring-your-own-domain and certificates, mutual TLS, access to monitoring tools, databases to run custom analysis, and more.

Future releases will include an enterprise network integration with VPC Peering, TLS mutual authentication, and additional data residency options.

To get started with Mattermost Cloud Enterprise, visit: https://mattermost.com/cloud to speak to a Mattermost Account Executive.

Frequently Asked Questions (FAQs)
---------------------------------

How much does Mattermost Cloud cost?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Cloud Professional is $10 USD per user, per month as a pay-as-you-go subscription. If you have over 1000 users please contact us.

Mattermost Cloud Enterprise is an annual subscription. Please contact us for a quote.    

How can customers trial Mattermost Cloud?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Cloud Professional edition is available to try free for up to 14 days. 

Mattermost Cloud Enterprise offers a discounted proof-of-concept program for a 60-day period. The proof-of-concept program includes a dedicated Customer Engineer.

When will support for other regions be available?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Cloud Enterprise will support data residency in 2021. We appreciate feedback from our customers on regional support for both editions.

How is Mattermost Cloud secured?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Cloud has encryption at-rest and in-transit. We are SOC2 Type 1 certified and working towards SOC2 Type 2.

Mattermost Cloud Enterprise is deployed in a private environment within an AWS VPC dedicated to a single customer. This architecture provides the isolation and security of an on-premises deployment while ensuring consistent performance and uptime of your Mattermost workspace.

What are the alternatives, and why should customers choose Mattermost Cloud?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Other SaaS offerings are closed-source and focus on a very broad usecase. Mattermost Cloud is built on our open source core offering, allowing customers to view our source code and have a high degree of transparency into Mattermost development processes. Mattermost provides a DevOps-centric offering and has deep integrations and workflows that help builders and operators be more effective.

Mattermost Cloud Enterprise is deployed in a private environment within an AWS VPC dedicated to a single customer. Other SaaS offerings are multi-tenant, meaning customers share resources.

Is Mattermost Cloud Enterprise a dedicated instance run on AWS systems?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, Mattermost Cloud Enterprise is a dedicated Mattermost environment running in a dedicated AWS account with separate infrastructure for that customer specifically, i.e. separate database, separate VMs, separate Kubernetes cluster.

How is customer data in Mattermost Cloud Enterprise encrypted?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost uses AWS-provided functionality to enable encryption-at-rest for both databases and file stores. See `Encrypting Amazon RDS resources - Amazon Relational Database Service <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>`__ and `Protecting data using server-side encryption - Amazon Simple Storage Service <https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html>`__ for details. 

Whether customer data should be stored in Mattermost Cloud depends heavily on the nature of the data and compliance requirements. We recommend that customers set up their own internal policies or controls around what can and cannot be put into Mattermost.

Are S3-managed keys used for server-side encryption? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. Customer-provided keys may be considered for a future release. 
