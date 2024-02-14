Self-hosted subscriptions
=========================

.. contents:: On this page
    :backlinks: top
    :depth: 2

Buy a subscription
------------------

From Mattermost v7.7 you can buy a Mattermost subscription from within Mattermost:

1. In Mattermost, select **View Plans** in the global header or via **System Console > View plans**.
2. Select **Upgrade**. A minimum of ten users is required.
3. Provide payment details.
4. Enter the number of user seats you're purchasing. This number has to be equal to, or greater than, the current number of activated users in your Mattermost deployment.
5. Select **Upgrade**.

When your purchase is complete, a license is automatically applied to instance and your subscription is active immediately.

If your deployment doesn't have internet access, please continue to use the Customer Portal or, contact our sales team for assistance.

Mattermost v7.6 and earlier releases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're using Mattermost v7.6 and below, you can buy a Mattermost subscription via the `Customer Portal page <https://customers.mattermost.com>`__. If you haven't created an account yet, follow the steps provided. Otherwise, you can log in with your existing credentials. When you buy a Mattermost subscription for a self-hosted deployment, you'll receive an activation license.

Once you're logged in:

1. Choose a subscription, and enter the number of users in the **Order summary** field. This indicates the number of users you can have on this subscription's instance. For more information about how users are defined, see our `FAQ <https://mattermost.com/pricing-self-managed/#faq>`__.
2. (Optional for Enterprise subscriptions) You can add `Premier Support <https://mattermost.com/support/>`__. This is an additional cost and is automatically added to your order total.
3. Select **Next Step**.
4. Enter your billing and payment information.
5. Accept the **Terms**.
6. Select **Complete**.
7. Choose **Download the license key**.

.. note::

   If you experience any problems with your transaction, please contact our Support team via the Customer Portal. If possible, keep the error message/number that you received on hand as it may help with their investigation.

Apply your license
------------------

Once downloaded, your Mattermost license is ready to use and is applied via the Mattermost System Console.

.. image:: ../images/mattermost_enterprise_license.png
	:alt: Apply the Mattermost Enterprise license using the System Console.

System admin access is required in order to apply the license. If you're not a Mattermost system admin, contact your organization's Mattermost system admin for assistance.

Mattermost installed
~~~~~~~~~~~~~~~~~~~~

On the Customer Portal **Subscriptions** page, select **Download License** to download the license key for your subscription. In Mattermost, follow the steps provided in **System Console > About > Edition and License** to apply your license key.

You can also use the `mmctl </manage/mmctl-command-line-tool.html#mmctl-license>`__ to apply the license.

Mattermost not yet installed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you haven't yet installed and deployed a Mattermost instance, visit the `Deployment Guide </deploy/deployment-overview.html>`__ to get started. For information on creating a system admin account, visit our `Administrator Tasks </getting-started/admin-onboarding-tasks.html>`__ documentation.

View subscription information
-----------------------------

Self-hosted subscriptions purchased via the `Customer Portal <https://customers.mattermost.com>`__ are stored and listed in the Customer Portal.

Here you can view license details, including their start date, end date and licensed number of users, and have full access to your billing history, making it easier to manage purchases and renewal dates.

You can access your Customer Portal account to view information about your:

- Subscription purchases
- Licenses
- Customer Portal account password
- Organization information
- Payment methods
- Renewals
- Activated users (available in a future release)

Subscription and licenses not purchased via the Customer Portal won't be listed.

Add more users to your subscription
-----------------------------------

If you have a self-hosted license in the Customer Portal, you can add additional users to your subscription via the `Customer Portal page <https://customers.mattermost.com>`__.

1. Select **Purchase additional seats**.
2. Enter your account and billing details.
3. When the transaction is complete, select whether you'd like to download your updated license or having it emailed to you.completes, they will have to either

Once you have your updated license, upload it via **System Console > License and Edition**.

This process adds additional users to your existing subscription and is not a new license. Your license renewal date doesn't change when you add additional users and receive an updated license. Billing is pro-rated based on the time left in your billing cycle.

If you don't have a self-hosted license in the Customer Portal and want to add users, `contact us <https://mattermost.com/contact-us/>`__.

Quarterly true-up reports
-------------------------

When you buy an annual Mattermost subscription, you agree to provide Mattermost with quarterly reports of the actual number of activated users within your system. An activated user is a user who has a Mattermost account and doesn't show as **Deactivated** in **System Console > User Management > Users**.

We'll send you an email notice around the end of the quarter reminding you to send us your report.

.. image:: ../images/true-up-schedule.png
   :alt: The timeframes followed for the true-up notifications.

If you have more total active users than you purchased in your annual subscription, your Customer Success Manager will provide you with a true-up quote for the new users added. The additional invoice will be pro-rated based on the number of months left in your subscription term, including the months for the calendar quarter for the time you pull the report. Mattermost won't provide downward adjustments. Mattermost will invoice based on Mattermost’s `current list prices <https://mattermost.com/pricing/>`__.

From Mattermost v7.9
~~~~~~~~~~~~~~~~~~~~

From Mattermost v7.9, we've introduced a process that no longer requires you to take screenshots. To send Mattermost the report, a system admin must go to the **System Console** and open either the **Site Statistics** or **Team Statistics** pages.

When the current date is within the true-up reporting period, a panel will be visible at the top of the page with a button to share your system's statistics with Mattermost directly.

If your system is air-gapped (meaning it doesn't have access to the internet), the system admin can download the system statistcs which can then be shared with your Mattermost Customer Success Manager from a device that's not air-gapped.

.. tip::
   
   Not sure where to find the site statistics or team statistics? Please reach out to your account executive, Customer Success Manager, orders@mattermost.com, or support@mattermost.com for help.

Prior to Mattermost v7.9
~~~~~~~~~~~~~~~~~~~~~~~~~

If you have a Mattermost deployment prior to v7.9, a system admin needs to take a screenshot of the **System Console > Site Statistics** page and send it to Mattermost in an email.

- Please ensure your screenshot is taken from the top of the page and includes both **Total Active Users** and the **Monthly Active Users** metrics. 
- Please include the date of the screenshot in the file name.
- We don't need your server address, so if it appears on your screenshot, you can redact it from the image.

.. tip:: 

   Not sure where to take the screenshot? Please reach out to your account executive, Customer Success Manager, orders@mattermost.com, or support@mattermost.com for help.
   
Renew your subscription
-----------------------

From Mattermost Server v5.32, you can renew your self-hosted Mattermost subscription with a credit card if you have a standard Mattermost contract. When you renew your license, you can also increase the number of activated users.

If you haven't upgraded to v5.32, contact Mattermost Support at support@mattermost.com to renew your license.

If you're a reseller, have a non-standard contract, or want to adjust the number of activated users on your license during the license period, please contact Mattermost Sales at sales@mattermost.com.

System admins will be alerted 60 days prior to license expiry via a banner in Mattermost. Select **Renew license now** to start the renewal process in the Customer Portal. You can also dismiss the banner and renew your license at a later date via **System Console > Edition and License**.

When you select **Renew license now**, you're taken to the renewal page in the Customer Portal, which lists your license information and account details. This is pre-populated based on the email address associated with your existing license subscription.

Process your license renewal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Enter your **Account Details**, **Additional Contact**, and **Payment Details**.
2. Confirm the `Mattermost Edition <https://mattermost.com/pricing-self-managed>`_.

  * You can upgrade within the Customer Portal, but it's not possible to downgrade.

3. Confirm the listed number of activated users is correct. 

 * You can increase the number of licensed users, but you can't decrease it.

4. Select **Complete purchase**. 

An email with the new license key and information on how to upload the license in the System Console will be sent to the email address provided.

You can watch a video overview of the renewal process on YouTube:

.. raw:: html
  
   <iframe width="560" height="315" src="https://www.youtube.com/embed/Sz_1nhVufHY" alt="Video on self hosted subscription" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Frequently asked questions
--------------------------

What is a true-up report and why is the true-up notice necessary? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A true-up report is our quarterly request for you to provide us with the actual number of activated users within your system to determine if you have more active users now than when you bought your subscription.

As your organization grows, you may need to add additional users during your subscription period. Mattermost needs to have insight into changes in your active user count so that we can charge you appropriately for your self-hosted license usage. Additionally, we don’t want to over estimate/charge activated users at your renewal time. 

When you receive the quarterly true-up notice from Mattermost, please share your active user count with us.

How do I renew my subscription if I don't have internet access?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you don't have access to the internet, please email support@mattermost.com for assistance.

Can I use the same license key on multiple self-hosted servers?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

License keys for unlocking the advanced features in Mattermost can only be applied to a single deployment. A deployment consists of either a single Mattermost server or multiple linked Mattermost servers in a High Availability configuration with access to a single database.

Customers who are eligible to purchase the `Premier Support add-on <https://mattermost.com/support/>`__ are licensed to run with a single deployment of Mattermost license key in production and up to four non-production deployments of Mattermost (for example: development, staging, user acceptance testing, etc.)

Is my license key available immediately?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, once your payment is successfully processed your license is available to download immediately.

How will I know when to renew my subscription?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You'll be notified 60 days prior to your subscription expiry, via a blue banner displayed at the top of your Mattermost window. This banner is only visible to system admins.

You can select **Renew license now** to begin the renewal process. You can also select the **x** to dismiss the notification. The notification is reactivated when your browser is refreshed or you reload the Mattermost Desktop App.

How long does it take to renew a subscription?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you’ve started the renewal process, we'll be in contact with you to confirm your order and send you the order form. There may be additional paperwork required. Once we have the signed order form and (if applicable) the necessary paperwork from you, we're able to process the renewal and issue your license key within 24 hours.

What happens to my subscription if I don't renew in time?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you don't renew within the 60-day renewal period, a 10-day grace period is provided. During this period your Mattermost installation runs as normal, with full access to commercial features. During the grace period, the notification banner is not dismissable.

When the grace period expires, your Professional or Enterprise plan is downgraded to the Free plan and other plan features are disabled.
 
What happens when my subscription expires?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you don't renew within the 10-day grace period, your Mattermost version is automatically downgraded to Free plan so you can still access and use Mattermost. However, subscription features will no longer be available, and if you are currently using them, the functionality will no longer be accessible.

When you renew, the subscription features will become available with the previous configuration (provided no action such as user migration has been taken).

Why can't I dismiss the expiry notification banner?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If there's a red expiry announcement banner stating: "Enterprise license is expired and some features may be disabled. Please contact your system admin for details." it means your grace period has expired. This announcement banner persists until the license is renewed, and is visible to all users.

Once a new license is applied, the banner will no longer be visible.

If you don't plan to renew your subscription, revoke the expired license in **System Console > Edition and License**.

Can other members of my organization use the Customer Portal account to manage our subscription?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We currently support a single account/user per organization. The ability to add multiple users per organization will be available in a future release.

Where can I find the license agreement for Mattermost Enterprise Edition?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Enterprise Edition is the name for the binary of the Mattermost self-hosted Professional and Enterprise editions. This edition can be used for free without a license key as commercial software functionally equivalent to the open source Mattermost Team Edition licensed under MIT. When a license key is purchased and applied to Mattermost Enterprise Edition, additional features unlock. The license agreement for Mattermost Enterprise Edition is included in the software and also available `here <https://mattermost.com/enterprise-edition-license/>`__.

How do I delete my Customer Portal account?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please contact Mattermost Support for assistance with deleting your Customer Portal account.

What happens to my subscription when I delete my account?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When an account is deleted, the license key remains valid. When the subscription is close to expiring, you'll need to create a new profile in order to renew it.