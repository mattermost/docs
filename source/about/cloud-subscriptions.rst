Cloud Subscriptions
===================

Purchase a Cloud subscription
-------------------------------

Mattermost Cloud subscriptions start with a 14-day trial. When you're near the end of your trial, a banner within Mattermost will notify you to upgrade to a subscription plan.

1. Select **Subscribe now** from the banner.
2. Provide your credit card details. 
3. Provide your billing address.
4. (Optional) Select a subscription plan.
5. Select **Subscribe**.

Your credit card will be verified and you'll be charged at the end of the billing period. If you'd prefer an annual Cloud subscription, please contact our Sales team for a quote. 

View subscription details
-------------------------

Access your subscription details in **System Console > Billing & Account > Subscription** to view:

- Subscription invoices
- Billing history
- Organization information
- Credit Card payment methods

Please see the `Cloud Billing <https://docs.mattermost.com/manage/cloud-billing.html>`__ documentation for more detailed information on the Cloud billing process.

Add more users to your subscription
-----------------------------------

If you're on a monthly Cloud subscription, you can add more users to your instance which will be reflected on your monthly invoice. If you add new users in the middle of a billing cycle, you’ll only be charged for the days that the user is registered.

When you subscribe to an annual plan with Mattermost, you may incur retroactive charges on a quarterly basis for the actual number of registered users within your system if you are above the amount you subscribed in your purchase order. A registered user is a user who has an account in a workspace and does not show as *Inactive* in **System Console > User Management > Users**.

If you have more total active users than what you purchased in your annual subscription, we will provide you with an invoice and an amendment to your purchase order for the new users added. The additional invoice will be pro-rated based on the number of months left in your subscription term, including the months for the calendar quarter at the time we review your user counts. We will not provide downward adjustments. Mattermost will invoice based on Mattermost’s `current list prices <www.mattermost.com/pricing>`__ . 

Renew your subscription
-----------------------

Monthly Cloud subscriptions renew automatically.

Frequently Asked Questions
---------------------------

How am I billed for my Cloud monthly subscription?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your first Cloud subscription charge is at the end of the calendar month, and all monthly charges are billed in arrears on the first day of each month, e.g., June billing will be done on 7/1 for the period 6/1 - 6/30. 

After your first month, the billing period begins at 12 AM UTC on the first day of each calendar month and ends at 11:59 PM UTC on the final day of the same calendar month. Per-user pricing for each billing period will be based on the number of registered users.

If you begin your subscription in the middle of a billing period, charges will be prorated. For example, if you signed up 6/15, we'll charge you on 7/1 for the period 6/15 - 6/30.

Similarly, if you end your subscription in the middle of a billing period, charges will be prorated. For example, if you cancel your account on 6/15, we'll charge you on 7/1 for the period 6/1 - 6/15.

If you upgrade in the middle of a billing period, charges will also be prorated. For example, if you upgrade from Starter to Professional on 6/15, we'll charge you 7/1. This will be a single charge for Starter for the period 6/1 - 6/14, then a separate charge for Professional for the period 6/15 - 6/30.

Can I purchase an annual subscription to Mattermost Cloud deployments?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. Contact sales@mattermost.com to learn more about annual Cloud subscription options.

If you upgrade during a monthly billing cycle, charges will be prorated. For example, if you upgrade from monthly Starter to an annual term of Mattermost Professional on 6/15, we'll charge you on 7/1 for Starter for the period 6/1 - 6/14. A separate invoice will be provided for the annual Mattermost Professional subscription period starting 6/15.

How do I cancel my subscription? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To cancel your subscription, please `contact us <https://customers.mattermost.com/cloud/contact-us>`__.

When will support for other regions be available?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Cloud Enterprise will support data residency based on feedback from our customers. We appreciate feedback from our customers on regional support.

How is Mattermost Cloud secured?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Cloud has encryption at-rest and in-transit. We're SOC2 Type 1 certified and working towards SOC2 Type 2.

Mattermost Cloud Enterprise is available to be deployed in a private environment within an AWS VPC (Virtual Private Cloud) dedicated to a single customer. This architecture provides the isolation and security of an on-premises deployment while ensuring consistent performance and uptime of your Mattermost workspace. Please contact Mattermost Sales for more information on this option. 

What are the alternatives, and why should customers choose Mattermost Cloud?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Other SaaS offerings are closed-source and focus on a very broad use case. Mattermost Cloud is built on our open source core offering, allowing customers to view our source code and have a high degree of transparency into Mattermost development processes. Mattermost provides a DevOps-centric offering and has deep integrations and workflows that help builders and operators be more effective.

Mattermost Cloud Enterprise is available to be deployed in a private environment within an AWS VPC dedicated to a single customer. Other SaaS offerings are multi-tenant, meaning customers share resources. Please contact sales for more inforamtion on this option. 

Is Mattermost Cloud Enterprise a dedicated instance run on AWS systems?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Cloud Enterprise can be deployed as a dedicated Mattermost environment running in a dedicated AWS account with separate infrastructure for that customer specifically, i.e. separate database, separate VMs, separate Kubernetes cluster. Please contact Mattermost Sales for more information on this option.

How is customer data in Mattermost Cloud Enterprise encrypted?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost uses AWS-provided functionality to enable encryption-at-rest for both databases and file stores. See `Encrypting Amazon RDS resources - Amazon Relational Database Service <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>`__ and `Protecting data using server-side encryption - Amazon Simple Storage Service <https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html>`__ for details. 

Whether customer data should be stored in Mattermost Cloud depends heavily on the nature of the data and compliance requirements. We recommend that customers set up their own internal policies or controls around what can and cannot be put into Mattermost.

Are S3-managed keys used for server-side encryption? 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. Customer-provided keys may be considered for a future release. 
