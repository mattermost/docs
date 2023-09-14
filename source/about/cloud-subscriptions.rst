Cloud subscriptions
===================

.. contents:: On this page
    :backlinks: top
    :depth: 2

Mattermost Cloud Subscriptions are offered as an annual subscription.

Buy a Cloud subscription
------------------------

1. Select **View Plans** at the top of the Mattermost window.
2. Select Professional by clicking **Upgrade**.
3. Provide your credit card details.

.. note::

  - Your credit card will be verified and you'll be charged immediately.
  - A minimum of ten seats is required.

4. Click **Upgrade** to confirm.

To upgrade to Mattermost Enterprise, `contact sales <https://mattermost.com/contact-sales/>`__.

View subscription information
-----------------------------

When you've purchased a subscription, you can view the details of your Mattermost Cloud account, including the annual cost per user and the number of users currently registered in your workspace. You can also find a summary of your last invoice in the same page.

Billing period
--------------

When you begin your Mattermost Cloud subscription, your credit card is billed immediately. Your subscription automatically renews annually, however you can opt-out of auto-renewal.

If there's a payment failure, your invoice will show **Payment Failed**. Please review the accuracy of your credit card information in **Payment Information**. Unresolved failed payments may result in a delinquency and an interruption to your subscription.

Payment information
~~~~~~~~~~~~~~~~~~~

Mattermost uses a third-party payment processor, Stripe, to safely collect and store your credit card information. 

Credit cards are the only form of payment for customers on a monthly billing cycle. All major credit cards are accepted. You can only store information for one credit card in your account.

We offer pricing and billing only in U.S. Dollars (USD) at this time. Payment will be made in USD converted using the exchange rate at the time of the transaction.

Sales tax and VAT
~~~~~~~~~~~~~~~~~

Mattermost reserves the right to assess applicable taxes as required by local law. Depending on location, you may be charged transaction taxes when purchasing our product. Prices on our website are exclusive of sales tax or VAT.

Failed or late payments
-----------------------

You'll be notified immediately of failed payments both in-product, with a banner, and via email. The notifications provide directions on how to update payment information. Once payment information is updated, you'll be charged right away for the amount owing.

If you have not paid or resolved the failed payment after 90 days, your workspace will be downgraded to Mattermost Free and subject to the data limits of that plan. If there is no activity on your workspace 60 days after the downgrade, your workspace will be deleted.

Add more users to your Cloud Professional subscription
------------------------------------------------------

You can add users to your workspace anytime. You may incur retroactive charges during renewal or at the end of your annual subscription. You can view any upcoming charges in **System Console > Subscriptions**.

- If the number of users is less than 10% of initial number of users when you subscribed to your annual plan, you won't be billed for the cost of additional users retroactively
- If the number of users is greater than 10% of the initial number of users when you subscribed to your annual plan, you will be billed the cost of additional users, pro-rated during renewal or at the end of your annual subcsription.

Example:

- You subscribed to Cloud Professional on January 2023 for 100 users. Throughout your subscription term, you add 8 users. You will not be retroactively billed for the cost of additional users.
- You subscribed to Cloud Professional on January 2023 for 100 users. On March 2023, you add 5 users. On September 2023, you add another 10 users for a total of 15 users during your subscription term. You will be billed pro-rated for the cost of additional users incurred in March and September.

Renew your subscription
-----------------------

Cloud subscriptions renew automatically, unless you opt out of renewal.

Frequently asked questions
---------------------------

How am I billed for my annual Cloud subscription?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you purchase your subscription, your credit card is charged immediately. Thereafter, your subscription auto-renews every year. You can opt-out of auto-renewal in the System Console. You'll still receive reminders when your subscription is due for renewal.

What happens if I want to buy Mattermost Enterprise during my trial?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will have to contact our sales team to upgrade to Mattermost Enterprise. Your plan immediately changes to the plan you've upgraded to. You will be invoiced as per your agreement with our sales team.

How do I cancel my subscription? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have an annual subscription to Mattermost Cloud Professional, or Mattermost Cloud Enterprise and you wish to cancel, please `contact us <https://customers.mattermost.com/cloud/contact-us>`__.

When will support for other regions be available?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud Enterprise will support data residency based on feedback from our customers.

If you require your data to reside in an area outside of the United States, please contact the product team via `feedback-cloud@mattermost.com <feedback-cloud@mattermost.com>`_, or consider `deploying one of our Self-Hosted options <https://mattermost.com/deploy>`_ that provides full control of your data. You may also work with `one of our European partners <https://mattermost.com/partners>`_ for deploying and hosting your Mattermost server.

How is Mattermost Cloud secured?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud has encryption at-rest and in-transit. We're SOC2 Type 1 certified and working towards SOC2 Type 2.

Mattermost Cloud Enterprise is available to be deployed in a secure, private environment within a dedicated cloud offering to a single customer. This architecture provides the isolation and security of an on-premises deployment while ensuring consistent performance and uptime of your Mattermost workspace. `Please contact Mattermost Sales for more information on this option <https://mattermost.com/contact-sales/>`_.

What are the alternatives, and why should I choose Mattermost Cloud?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Other SaaS offerings are closed-source and focus on a very broad use case. Mattermost Cloud is built on our open source core offering, allowing customers to view our source code and have a high degree of transparency into Mattermost development processes. Mattermost provides a DevOps-centric offering and has deep integrations and workflows that help builders and operators be more effective.

Mattermost Cloud Enterprise is available to be deployed in a private environment within an AWS VPC dedicated to a single customer. Other SaaS offerings are multi-tenant, meaning customers share resources. Please contact sales for more inforamtion on this option.

Is Mattermost Cloud Enterprise a dedicated instance run on AWS systems?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud Enterprise can be deployed as a dedicated Mattermost environment running with separate infrastructure for your requirements (e.g., separate database, separate VMs, separate Kubernetes cluster). Please contact Mattermost Sales for more information on this option.

How is customer data in Mattermost Cloud Enterprise encrypted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost uses AWS-provided functionality to enable encryption-at-rest for both databases and file stores. See `Encrypting Amazon RDS resources - Amazon Relational Database Service <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>`__ and `Protecting data using server-side encryption - Amazon Simple Storage Service <https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html>`__ for details.

Whether customer data should be stored in Mattermost Cloud depends heavily on the nature of the data and compliance requirements. We recommend that customers set up their own internal policies or controls around what can and cannot be put into Mattermost.

Are S3-managed keys used for server-side encryption? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Customer-provided keys may be considered for a future release. 

Do you provide cross-region failover in the event of an outage in AWS us-east-1 region?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud is hosted in AWS `us-east-1` region. Cross-region failover is planned, but not yet in the roadmap. If you have feedback or require cross-region failover, please reach out to our product team via feedback-cloud[at]mattermost.com.

What environments and rings are Cloud offerings deployed with?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud provides `three offerings <https://mattermost.com/pricing/>`_: Free, Professional, Enterprise, with a virtual private Cloud add-on available for Enterprise.

These offerings are deployed in the following ways:

 - **Professional**: Single application layer, shared infrastructure, shared network, professional group ring.
 - **Enterprise**: Single application layer, shared infrastructure, shared network, enterprise group ring.
 - **Enterprise plus dedicated add-on**: Single application layer, dedicated network via VPC (Virtual Private Cloud), dedicated infrastructure, enterprise group ring.
