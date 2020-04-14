Enterprise Edition
------------------

What is Mattermost Enterprise Edition?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Enterprise Edition is a commercial workplace messaging solution for large organizations operating under compliance and security requirements that is built on top of the open source Mattermost Team Edition.

What are the options to purchase a subscription to Mattermost Enterprise Edition? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To simplify procurement and to keep prices low, Mattermost offers the following options to purchase: 

1. **Create a self-service account and purchase a license** (https://about.mattermost.com/pricing/) under standard Mattermost terms (https://about.mattermost.com/enterprise-edition-terms/) used by hundreds of other Enterprise Edition customers. 

2. **Purchasing via a Mattermost reseller** (https://about.mattermost.com/partners/) under terms agreed between the customer and reseller, and then agreeing to **Mattermost Enterprise Edition Subscription Terms for Purchase by Resale** (https://about.mattermost.com/customer-terms-and-conditions/) prior to being provided a license key for the purchase by Mattermost, Inc. 

3. **Purchase via a purchase order referencing a Mattermost quotation number**, and where the quotation is valid, unexpired and references the **Mattermost Enterprise Edition Subscription Terms** (https://about.mattermost.com/enterprise-edition-terms/): 

   i. If the PO references any special terms and conditions, it cannot be accepted by Mattermost, Inc. without the following special note: ``This Purchase Order is governed solely by the terms and conditions of the Mattermost Enterprise Edition Subscription Terms at https://about.mattermost.com/enterprise-edition-terms/. Despite anything to the contrary, no other terms and conditions printed on, or incorporated into or referenced by, shall apply.``

4. **Purchase via a purchase order referencing a Master Services Agreement** or similar agreement executed by Mattermost and the customer for subscription purchases over $100,000 USD. 

   i. If the PO references any special terms and conditions, it cannot be accepted by Mattermost, Inc. without the following clause included in the prior signed agreement: ``THE PARTIES AGREE THAT ANY ADDITIONAL OR DIFFERENT TERMS AND CONDITIONS CONTAINED ON OR INCORPORATED INTO YOUR PURCHASE ORDER ARE EXPRESSLY REJECTED AND SHALL NOT BE CONSIDERED AN AMENDMENT TO THIS AGREEMENT.`` If the agreement does not include such a clause the following purchase order note is required: ``This purchase order is governed solely by the terms and conditions of the [AGREEMENT_TITLE] dated [AGREEMENT_DATE] between [CUSTOMER_NAME] and Mattermost, Inc..  All other terms and conditions contained on or referenced by this purchase order shall not apply.``

How does the licensing key work?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#faq>`__.

How do I renew the Enterprise Edition subscription?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to `https://licensing.mattermost.com/renew <https://licensing.mattermost.com/renew>`__ and specify the Enterprise Edition you want to renew, the user count, and your contact information. To find the user count you want to renew for, log in to Mattermost as a System Admin and go to **System Console > Site Statistics**, where **Total Active Users** displays the user count on your server.

After submitting the renewal form, our renewal team will get in contact with you about your new subscription.

New users added during the subscription period will have a retroactive charge. `Learn more here <https://docs.mattermost.com/overview/faq.html#how-can-i-add-more-users-to-my-subscription>`__.

For information on what happens when the Enterprise Edition subscription expires, see our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#faq>`__.

What happens when the Enterprise Edition subscription expires?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#faq>`__.

How is user defined for Enterprise Edition subscriptions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#faq>`__.

How can I add more users to my subscription?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add more users during your subscription period without requesting a license.

During the annual renewal, a retroactive charge will be placed for any unique users added during the past subscription period that is above the licensed total unique users in the current paid subscription. The retroactive charge per user will be the initial subscription cost per user.

Do I need to pay for deactivated users?  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. If you deactivate a user that user is not counted as an active user during your annual renewal process. You can deactivate users manually via System Console and also via Active Directory/LDAP synchronization, the CLI tool, and the server APIs. 

If you choose to pull SQL reports from the database to monitor individual activity to make deactivation decisions, and you are running under high user load, we recommend the reports are pulled from a read replica of the database.

Can I use the same license key on multiple Enterprise Edition servers?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Customers who purchase the Premier Support add-on to E20 are licensed to run with the same Mattermost license key in a production deployment and up to 4 non-production deployments of Mattermost (for example: development, staging, user acceptance testing, etc.).

Without the purchase of Premier Support, license keys for unlocking the advanced features in Mattermost Enterprise Edition should only be applied to a single deployment. A deployment consists of either a single Mattermost application server, or multiple linked Mattermost application servers in a high availability configuration.


What happens if my department buys Mattermost Enterprise Edition and then central IT buys a high volume license that also covers my department?   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Enterprise Edition subscriptions and support benefits are licensed per production instance. 

When the subscription term for your department's production instance expires, you can either discontinue your department's production instance and move to the instance hosted by central IT (which can optionally provision one or more teams for your department to control), or you can renew your subscription to maintain control of your department's instance (e.g., to configure or customize the system in a manner highly specific to your line-of-business) in addition to using the instance from central IT. 
