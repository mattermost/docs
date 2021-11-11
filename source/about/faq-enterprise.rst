Enterprise Edition Questions
============================

What is Mattermost Enterprise Edition?
--------------------------------------

Mattermost Enterprise Edition is a commercial workplace messaging solution for large organizations operating under compliance and security requirements built on top of the open source Mattermost Team Edition.

How can I be assured that my data will not be locked in to commercial software?
-------------------------------------------------------------------------------

Users of Mattermost Enterprise Edition can downgrade to the open source version without losing any data. Moreover, you always have control over your server and database, where the entirety of your Mattermost deployment is stored.

How does Mattermost scale from teams to enterprises?
----------------------------------------------------

Growing your Mattermost installation from supporting a team to supporting an enterprise requires two types of scaling:

1. Technical scaling: Maintaining system responsiveness as large quantities of new users are added.
2. Functional scaling: Adding advanced features to support the increased complexity of large organizations.

**Technical Scaling:** Whether used for teams or enterprises, the Mattermost server is designed to support tens of thousands of users on a single server with appropriate hardware. The server is built using Golang, the language developed by Google to create internet-scale applications, and supports highly scalable databases like MySQL, which is `used extensively by Facebook <https://www.facebook.com/notes/facebook-engineering/mysql-and-database-engineering-mark-callaghan/10150599729938920/>`__. Beyond tens of thousands of users, Mattermost Enterprise Edition can offer high availability/horizontal scaling configurations using multiple servers to support even larger organizations.

**Functional Scaling:** Scaling from a team to an enterprise is like going from a "virtual office" to a "virtual campus". Advanced features like enterprise authentication, granular permissions, compliance and auditing, and advanced reporting become increasingly important as organizations grow beyond teams. Organizations needing this flexibility can easily upgrade from Mattermost Team Edition to Mattermost Enterprise Edition as well as downgrade without data loss, should their needs change.

For more information on how Mattermost scales, technically, and functionally, please `contact the Enterprise team <https://mattermost.com/contact-us/>`__ and `read about scaling for Enterprise <https://docs.mattermost.com/scale/scaling-for-enterprise.html>`__.

What does it take to manage a Mattermost deployment?
----------------------------------------------------

For a small deployment of Mattermost up to a few hundred users, we'd recommend a part-time, mid-level IT admin with a senior IT admin for supervision and as a backup resource. They should have the ability to administer a basic Linux server, a MySQL or PostgreSQL database, and web proxy configuration with web sockets.

For a medium deployment of 500 to 2000 users, we'd recommend a senior IT administrator who has the capability to configure Mattermost in a High Availability cluster with redundant database and application servers. They should also be able to activate performance monitoring and health check features in Prometheus and Grafana.

How do you manage multiple messaging solutions in an enterprise?
----------------------------------------------------------------

Our customers address multiple collaboration solutions in different ways depending on whether the organization is more top down or bottom up.

**For top-down, customers want to simplify and leverage investments in a central, flexible, innovative solution that can scale.** There's generally a lot of pain with different teams and departments running their own messaging tools, creating silos, redundancy, and significant productivity loss. They'll roll out Mattermost as an official solution and centralize communication there. For an example of this, see our `Uber case study <https://mattermost.com/customers/>`__.

**For bottom-up, customers want to supplement for strategic advantage.** We've seen teams flock to Mattermost because of its productivity benefits for DevOps, remote work, rapid response, and scaling large teams where people are overloaded with email. Those organizations, which can have hundreds to thousands of users, will use Mattermost in parallel with general-purpose messaging that doesn't meet their specific needs.

One example is Wargaming, one of the world's largest real-time online video game operators, with over 150 million players on their system. They've moved their DevOps, design, analytics and support teams to Mattermost to supplement Skype for Business. This is their company-wide, general-purpose messenger that isn't optimized for large DevOps organizations and the degree of integration and flexibility they need - specifically for DevOps. People want support for Linux and Mac desktops, lots of APIs and hooks to integrate. They also need help for plugins to embed certain types of reports and interactive controls into messages, friendly keyboard shortcuts, and dozens of other enhancements that provide a distinct advantage to their counterparts at other companies.

What are the options to purchase a subscription to Mattermost Enterprise Edition?
---------------------------------------------------------------------------------

To simplify procurement and to keep prices low, Mattermost offers the following options to purchase:

1. **Purchase a subscription online via credit card** (https://mattermost.com/pricing-self-managed/) under standard Mattermost terms (https://mattermost.com/enterprise-edition-terms/) used by hundreds of other Enterprise Edition customers.

2. **Purchasing via a Mattermost reseller** (https://mattermost.com/partners/) under terms agreed between the customer and reseller, and then agreeing to **Mattermost Enterprise Edition Subscription Terms for Purchase by Resale** (https://about.mattermost.com/customer-terms-and-conditions/) prior to being provided a license key for the purchase by Mattermost, Inc.

3. **Purchase via a purchase order referencing a Mattermost quotation number**, and where the quotation is valid, unexpired and references the **Mattermost Enterprise Edition Subscription Terms** (https://mattermost.com/enterprise-edition-terms/):

   If the PO references any special terms and conditions, it cannot be accepted by Mattermost, Inc. without the following special note: ``This Purchase Order is governed solely by the terms and conditions of the Mattermost Enterprise Edition Subscription Terms at https://mattermost.com/enterprise-edition-terms/. Despite anything to the contrary, no other terms and conditions printed on, or incorporated into or referenced by, shall apply.``

4. **Purchase via a purchase order referencing a Master Services Agreement** or similar agreement executed by Mattermost and the customer for subscription purchases over $100,000 USD.

   If the PO references any special terms and conditions, it cannot be accepted by Mattermost, Inc. without the following clause included in the prior signed agreement: ``THE PARTIES AGREE THAT ANY ADDITIONAL OR DIFFERENT TERMS AND CONDITIONS CONTAINED ON OR INCORPORATED INTO YOUR PURCHASE ORDER ARE EXPRESSLY REJECTED AND SHALL NOT BE CONSIDERED AN AMENDMENT TO THIS AGREEMENT.`` If the agreement does not include such a clause the following purchase order note is required: ``This purchase order is governed solely by the terms and conditions of the [AGREEMENT_TITLE] dated [AGREEMENT_DATE] between [CUSTOMER_NAME] and Mattermost, Inc..  All other terms and conditions contained on or referenced by this purchase order shall not apply.``
  
What happens when the Enterprise Edition subscription expires?
--------------------------------------------------------------

Sixty days prior to expiry, System Administrators receive notifications that the Enterprise Edition license key will expire on the anniversary of its purchase. After expiry, there is a 10-day grace period to upload a new license key. After the grace period, Enterprise features will be disabled. At any time, Enterprise Edition can be downgraded to the free Team Edition without data loss by switching off any Enterprise features enabled and then removing the license key.

What are Mattermost's policies around licensing, terms of use, and privacy?
---------------------------------------------------------------------------

The following outlines the licensing, terms of use and privacy policies across Mattermost software and services.

Mattermost Software
~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Software                                           | License                                                                                                                   | Terms and Conditions                                                                                                          | Privacy Policy                                                                                                             |
+====================================================+===========================================================================================================================+===============================================================================================================================+============================================================================================================================+
| Mattermost Team Edition (Open Source)              | Open Source **MIT License**.                                                                                              | `Mattermost Trademark Policy <https://mattermost.org/trademark-standards-of-use/>`__                                          | `Mattermost Server Privacy Policy <https://github.com/mattermost/mattermost-server/blob/master/build/PRIVACY_POLICY.md>`__ |
|                                                    |                                                                                                                           |                                                                                                                               | with `GDPR Data Processing Addendum <https://about.mattermost.com/default-data-processing-addendum/>`__.                   |
|                                                    | Open Source Add-ons available under `Apache v2 and other licenses <https://mattermost.org/licensing/>`__.                 | `Mattermost Terms of Use <https://about.mattermost.com/default-terms/>`__                                                     |                                                                                                                            |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+                                                                                                                            |
| Mattermost Enterprise Edition with no subscription | `Commercial Enterprise Edition License <https://about.mattermost.com/enterprise-edition-license/>`__.                     | No subscription terms apply when operating without a subscription                                                             |                                                                                                                            |
|                                                    |                                                                                                                           |                                                                                                                               |                                                                                                                            |
|                                                    | You are welcome to use the Enterprise Edition of Mattermost free of charge in perpetuity when the subscription feature    |                                                                                                                               |                                                                                                                            |
+----------------------------------------------------+ are not enabled by a license key.                                                                                         +-------------------------------------------------------------------------------------------------------------------------------+                                                                                                                            |
| Mattermost Enterprise Edition with subscription    |                                                                                                                           | `Self Managed Subscription Terms <https://about.mattermost.com/enterprise-edition-terms/>`__                                  |                                                                                                                            |
|                                                    | If you choose to purchase a subscription for paid features, terms and conditions are offered                              |                                                                                                                               |                                                                                                                            |
|                                                    | as part of the subscription purchase (see “Terms”).                                                                       | `Enterprise Edition Subscription Terms for Purchase by Resale <https://about.mattermost.com/customer-terms-and-conditions/>`__|                                                                                                                            |
|                                                    |                                                                                                                           |                                                                                                                               |                                                                                                                            |
|                                                    |                                                                                                                           | `Cloud Subscription Agreement <https://mattermost.com/cloud-subscription-terms/>`__                                           |                                                                                                                            |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+

Mattermost Service Agreements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Service                                                                     | Terms and Conditions                                                                                                                            | Privacy Policy                                                                                                             |
+=============================================================================+=================================================================================================================================================+============================================================================================================================+
| Mattermost Enterprise Edition Support, including Premier Support            | `Mattermost Support Terms <https://mattermost.com/support/>`__                                                                                  | `Mattermost Server Privacy Policy <https://github.com/mattermost/mattermost-server/blob/master/build/PRIVACY_POLICY.md>`__ |
+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+ with `GDPR Data Processing Addendum <https://about.mattermost.com/default-data-processing-addendum/>`__.                   |
| Mattermost Hosted Push Notification Service                                 | `Hosted Push Notifications Service Terms <https://about.mattermost.com/hpns-terms/>`__                                                          |                                                                                                                            |
+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+                                                                                                                            |
| Mattermost Professional Services                                            | To be posted.                                                                                                                                   |                                                                                                                            |
+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+

Mattermost Websites
~~~~~~~~~~~~~~~~~~~

+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Website                    | License                                                                                                                                                          | Terms and Conditions                                                                  | Privacy Policy                                                                                                            |
+============================+==================================================================================================================================================================+=======================================================================================+===========================================================================================================================+
| Mattermost Websites:       | Open source under                                                                                                                                                | `Mattermost Terms of Use <https://mattermost.com/terms-of-service/>`__                | `Mattermost Websites Privacy Policy <https://about.mattermost.com/privacy/>`__                                            |
|                            | `Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License (CC BY-NC-SA 3.0) <https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US>`__. |                                                                                       |                                                                                                                           |
|  - about.mattermost.com    |                                                                                                                                                                  |                                                                                       |                                                                                                                           |
|  - mattermost.com          |                                                                                                                                                                  |                                                                                       |                                                                                                                           |
|  - mattermost.org          |                                                                                                                                                                  |                                                                                       |                                                                                                                           |
|  - forum.mattermost.org    |                                                                                                                                                                  |                                                                                       |                                                                                                                           |
|  - docs.mattermost.com     |                                                                                                                                                                  |                                                                                       |                                                                                                                           |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

Mattermost Partnership Agreements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Partnership Agreement                                                       | Agreement                                                                                                         |
+=============================================================================+===================================================================================================================+
| Mattermost Authorized Reseller Agreement                                    | `Mattermost Authorized Reseller Agreement <https://about.mattermost.com/mattermost-authorized-reseller-terms/>`__ |
+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

Mattermost Confidentiality Agreements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Confidentiality Agreement                                                   | Agreement                                                                                                                             |
+=============================================================================+=======================================================================================================================================+
| Mattermost Mutual Non-Disclosure Agreement                                  | `Mattermost Mutual Non-Disclosure Agreement <https://docs.google.com/document/d/1Ev3VFjiJBKSf1D5Kmf2BScbHBgSQbMzTzOhY3Of28vY/edit>`__ |
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+

Working for Mattermost
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Service                                                                     | Terms and Conditions                                                                                                                             |
+=============================================================================+==================================================================================================================================================+
| Mattermost Professional Consulting Services                                 | `Mattermost Professional Consulting Services Agreement <https://docs.google.com/document/d/1tgEkO5Q-xqAgVEcx5Y-z28OC36HptpltKORpivQGLoY/edit>`__ |
+-----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Mattermost Consulting                                                       | `Mattermost Consulting Terms <https://about.mattermost.com/mattermost-consulting-terms/>`__                                                      |
+-----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

How does the licensing key work?
--------------------------------

See our `frequently asked questions about licensing <https://docs.mattermost.com/about/licensing-and-subscription.html#frequently-asked-questions>`__.

Do you have a program for official non-profits and charities?
-------------------------------------------------------------

See our `frequently asked questions about licensing <https://docs.mattermost.com/about/licensing-and-subscription.html#frequently-asked-questions>`__.

Do you have discounted licenses for academic institutions?
----------------------------------------------------------

See our `frequently asked questions about licensing <https://docs.mattermost.com/about/licensing-and-subscription.html#frequently-asked-questions>`__.