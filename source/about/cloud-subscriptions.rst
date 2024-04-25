Cloud subscriptions
===================

Mattermost Cloud Subscriptions are offered as an annual subscription.

Buy a Cloud subscription
------------------------

To upgrade to Mattermost Enterprise, `contact sales <https://mattermost.com/contact-sales/>`_.

View subscription information
-----------------------------

When you've purchased a subscription, you can view the details of your Mattermost Cloud account, including the annual cost per user and the number of users currently registered in your workspace.

Sales tax and VAT
~~~~~~~~~~~~~~~~~

Mattermost reserves the right to assess applicable taxes as required by local law. Depending on location, you may be charged transaction taxes when purchasing our product. Prices on our website are exclusive of sales tax or VAT.

Renew your subscription
-----------------------

To renew your subscription to Mattermost Enterprise, `contact sales <https://mattermost.com/contact-sales/>`_.

Frequently asked questions
---------------------------

How am I billed for my annual Cloud subscription?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you purchase your subscription, your credit card is charged immediately.

What happens if I want to buy Mattermost Enterprise during my trial?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will have to contact our sales team to upgrade to Mattermost Enterprise. Your plan immediately changes to the plan you've upgraded to. You will be invoiced as per your agreement with our sales team.

How do I cancel my subscription? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have an annual subscription to Mattermost Professional or Cloud Enterprise and you wish to cancel, please `contact sales <https://mattermost.com/contact-sales/>`_.

When will support for other regions be available?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud Enterprise will support data residency based on feedback from our customers.

If you require your data to reside in an area outside of the United States, please contact the product team via `feedback-cloud@mattermost.com <feedback-cloud@mattermost.com>`_, or consider `deploying one of our Self-Hosted options <https://mattermost.com/deploy>`_ that provides full control of your data. You may also work with `one of our European partners <https://mattermost.com/partners>`_ for deploying and hosting your Mattermost server.

How is Mattermost Cloud secured?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud has encryption at-rest and in-transit. We're SOC2 Type 1 certified and working towards SOC2 Type 2.

Mattermost Cloud Enterprise is available to be deployed in a secure, private environment within a dedicated cloud offering to a single customer. This architecture provides the isolation and security of an on-premises deployment while ensuring consistent performance and uptime of your Mattermost workspace. Contact `Mattermost Sales <https://mattermost.com/contact-sales/>`_ for more information on this option.

What are the alternatives, and why should I choose Mattermost Cloud?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Other SaaS offerings are closed-source and focus on a very broad use case. Mattermost Cloud is built on our open source core offering, allowing customers to view our source code and have a high degree of transparency into Mattermost development processes. Mattermost provides a DevOps-centric offering and has deep integrations and workflows that help builders and operators be more effective.

Mattermost Cloud Enterprise is available to be deployed in a private environment within an AWS VPC dedicated to a single customer. Other SaaS offerings are multi-tenant, meaning customers share resources. Please contact sales for more inforamtion on this option.

Is Mattermost Cloud Enterprise a dedicated instance run on AWS systems?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud Enterprise can be deployed as a dedicated Mattermost environment running with separate infrastructure for your requirements (e.g., separate database, separate VMs, separate Kubernetes cluster). Please contact Mattermost Sales for more information on this option.

How is customer data in Mattermost Cloud Enterprise encrypted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost uses AWS-provided functionality to enable encryption-at-rest for both databases and file stores. See `Encrypting Amazon RDS resources - Amazon Relational Database Service <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>`_ and `Protecting data using server-side encryption - Amazon Simple Storage Service <https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html>`_ for details.

Whether customer data should be stored in Mattermost Cloud depends heavily on the nature of the data and compliance requirements. We recommend that customers set up their own internal policies or controls around what can and cannot be put into Mattermost.

Are S3-managed keys used for server-side encryption? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Customer-provided keys may be considered for a future release. 

Do you provide cross-region failover in the event of an outage in AWS us-east-1 region?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud is hosted in AWS `us-east-1` region. Cross-region failover is planned, but not yet in the roadmap. If you have feedback or require cross-region failover, please reach out to our product team via feedback-cloud[at]mattermost.com.

What environments and rings are Cloud offerings deployed with?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud provides `two offerings <https://mattermost.com/pricing/>`_: Professional, Enterprise, with a virtual private Cloud add-on available for Enterprise.

These offerings are deployed in the following ways:

 - **Professional**: Single application layer, shared infrastructure, shared network, professional group ring.
 - **Enterprise**: Single application layer, shared infrastructure, shared network, enterprise group ring.
 - **Enterprise plus dedicated add-on**: Single application layer, dedicated network via VPC (Virtual Private Cloud), dedicated infrastructure, enterprise group ring.
