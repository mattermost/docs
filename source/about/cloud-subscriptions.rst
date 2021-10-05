Cloud Subscriptions
===================

Purchasing a Cloud subscription
-------------------------------

Mattermost Cloud subscriptions start with a 14-day trial. When you're near the end of your trial, a banner will notify you to upgrade to a subscription plan. 

1. Choose a subscription and enter the number of users in the **Order summary** field. This indicates the number of users you can have on this subscription's instance. For more information about how users are defined, see our `FAQ <https://mattermost.com/pricing-self-managed/#faq>`__.
2. (Optional for Enterprise subscriptions) You can add `Premier Support <https://mattermost.com/support/>`__, the cost of which is automatically added to your order total.
3. Select **Next Step**.
4. Enter your billing and payment information.
5. Accept the **Terms**.
6. Select **Complete**.

View subscription details
----------------------------

You can view your subscription details in **System Console > Billing & Account > Subscription**. 

You can view information about your:

- Subscription invoices
- Billing history
- Organization information
- Credit Card payment methods

Please see the `Cloud Billing <https://docs.mattermost.com/manage/cloud-billing.html>`__ documentation for more detailed information on the Cloud billing process.

Add more users to your subscription
-----------------------------------

If you're on a monthly Cloud subscription, you can just add more users to your instance and you'll be billed on your monthly invoice. If you add new users in the middle of a billing cycle, you’ll only be charged for the days that the user is registered.

If you are on an annual Cloud subscription, you may incur retroactive charges for any unique users added that exceed the total unique users in the current paid subscription. The retroactive charge per user will be the initial subscription cost per user.

Renewing a Subscription
-----------------------

Monthly Cloud subscriptions automatically renew. 

Cloud Subscription Frequently Asked Questions
---------------------------------------------

How am I billed for my Cloud monthly subscription?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After you begin your Mattermost Cloud paid subscription, your first charge will happen at the end of the calendar month. Subsequent billing periods will begin at 12 AM UTC on the first day of each calendar month and end at 11:59 PM UTC on the final day of the same calendar month. Per-user pricing for each billing period will be based on the number of registered users. All monthly charges will be in arrears on the first day of each month, e.g., June billing will be done on 7/1 for the period 6/1 - 6/30.

If you begin your subscription in the middle of a billing period, charges will be prorated. For example, if you signed up 6/15, we will charge you on 7/1 for the period 6/15 - 6/30.

Similarly, if you end your subscription in the middle of a billing period, charges will be prorated. For example, if you cancel your account on 6/15, we will charge you on 7/1 for the period 6/1 - 6/15.

If you upgrade in the middle of a billing period, charges will also be prorated. For example, if  you upgrade from Starter to Professional on 6/15, we will charge you 7/1, with a single charge for Starter for the period 6/1 - 6/14, then Professional for the period 6/15 - 6/30.

Can I purchase an annual subscription to Mattermost Cloud deployments?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. Annual Cloud orders need to be processed by our Sales team, as we don't currently support an annual term using the self-service Customer Portal or Cloud workspace.

If you upgrade during a monthly billing cycle, charges will be prorated. For example, if you upgrade from Starter to an annual term of Mattermost Professional on 6/15, we will charge you on 7/1 for starter for the period 6/1 - 6/14. Separately, an invoice will be provided for an annual period starting 6/15.

How do I cancel my subscription? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To cancel your subscription, please `contact us <https://customers.mattermost.com/cloud/contact-us>`__

How much does Mattermost Cloud cost?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Cloud Professional is $10 USD per user, per month as a pay-as-you-go subscription. If you have over 1000 users, please contact us.

Mattermost Cloud Enterprise is an annual subscription. Please contact us for a quote.    

How can customers trial Mattermost Cloud?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Cloud Professional plan is available to try free for up to 14 days. 

Mattermost Cloud Enterprise offers a discounted proof-of-concept program for a 60-day period. The proof-of-concept program includes a dedicated Customer Engineer.

When will support for other regions be available?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Cloud Enterprise will support data residency based on feedback from our customers. We appreciate feedback from our customers on regional support for both editions.

How is Mattermost Cloud secured?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Cloud has encryption at-rest and in-transit. We are SOC2 Type 1 certified and working towards SOC2 Type 2.

Mattermost Cloud Enterprise is deployed in a private environment within an AWS VPC dedicated to a single customer. This architecture provides the isolation and security of an on-premises deployment while ensuring consistent performance and uptime of your Mattermost workspace.

What are the alternatives, and why should customers choose Mattermost Cloud?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Other SaaS offerings are closed-source and focus on a very broad use case. Mattermost Cloud is built on our open source core offering, allowing customers to view our source code and have a high degree of transparency into Mattermost development processes. Mattermost provides a DevOps-centric offering and has deep integrations and workflows that help builders and operators be more effective.

Mattermost Cloud Enterprise is deployed in a private environment within an AWS VPC dedicated to a single customer. Other SaaS offerings are multi-tenant, meaning customers share resources.

Is Mattermost Cloud Enterprise a dedicated instance run on AWS systems?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, Mattermost Cloud Enterprise is a dedicated Mattermost environment running in a dedicated AWS account with separate infrastructure for that customer specifically, i.e. separate database, separate VMs, separate Kubernetes cluster.

How is customer data in Mattermost Cloud Enterprise encrypted?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost uses AWS-provided functionality to enable encryption-at-rest for both databases and file stores. See `Encrypting Amazon RDS resources - Amazon Relational Database Service <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>`__ and `Protecting data using server-side encryption - Amazon Simple Storage Service <https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html>`__ for details. 

Whether customer data should be stored in Mattermost Cloud depends heavily on the nature of the data and compliance requirements. We recommend that customers set up their own internal policies or controls around what can and cannot be put into Mattermost.

Are S3-managed keys used for server-side encryption? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. Customer-provided keys may be considered for a future release. 
