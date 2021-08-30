Licensing and Subscription
--------------------------

Mattermost offers a `secure self-service Customer Portal <https://customers.mattermost.com>`_ where you can easily purchase and manage your Mattermost Enterprise subscriptions.

When you purchase a subscription, a license is generated. This license gives you access to Mattermost's Enterprise features. Subscriptions purchased via the Customer Portal are stored and listed in the portal, with license details including their start and end dates, providing you with an at-a-glance overview of your account. You also have full access to your billing history, making it easier to manage purchases and renewal dates.

You can access your Customer Portal account to view information about your:

- Subscription purchases
- Licenses
- Customer Portal account password
- Organization information
- Payment methods
- Renewals
- Active users (available in a future release)

Purchasing an Enterprise license
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**If you don't have a Customer Portal account**

Open the `Customer Portal page <https://customers.mattermost.com>`__. Enter the required information and check the box to confirm **I have read and agree to the Privacy Policy**. Then select **Next**. When you've completed the process and validated your email address, you can proceed with the steps below.

**If you have an existing Customer Portal account**

1. Log in to your `Customer Portal <https://customers.mattermost.com>`_ account.
2. Choose a subscription type and enter the number of users in the **Order summary** field. This indicates the number of users you can have on this subscription's instance. For more information about how users are defined, see our `FAQ <https://mattermost.com/pricing-self-managed/#faq>`_.
3. (Optional for E20) You can add `Premier Support <https://mattermost.com/support/>`_, the cost of which is automatically added to your order total.
4. Select **Next Step**.
5. Enter your billing and payment information.
6. Accept the **Terms**.
7. Select **Complete**.
8. Choose **Download the license key**.

If you experience any problems with your transaction, please contact our Support Team via the form provided in the Customer Portal. If possible, keep the error message/number that you received on hand as it may assist with their investigation.

Applying the license key
~~~~~~~~~~~~~~~~~~~~~~~~

Your Mattermost Enterprise license is ready to use and be applied via the Mattermost System Console.

.. image:: ../images/mattermost_enterprise_license.png

System Admin access is required in order to apply the license. If you're not a Mattermost System Admin, contact your organization's Mattermost System Admin.

**If you already have Mattermost installed**

On the Customer Portal **Subscriptions** page, select **Download License** to download the license key for your subscription. In Mattermost, follow the steps provided in **System Console > About > Edition and License** to apply your license key.

You can also use the `CLI <https://docs.mattermost.com/install/enterprise-install-upgrade.html>`__ to apply the license.

**If you don't have Mattermost installed**

If you haven't yet installed and deployed a Mattermost instance, visit the `Deployment Guide <https://docs.mattermost.com/deploy/deployment-overview.html>`_ to get started. For information on creating a System Admin account visit the `Administrator Tasks <https://docs.mattermost.com/getting-started/admin-onboarding-tasks.html>`_ documentation.

Viewing license information
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For licenses purchased using the Customer Portal, you can view the license start date, expiry date, number of users, and license type in your account under **Subscription**.

If you have an existing subscription and license, not purchased via the Customer Portal, this information won't be listed.

Adding more users to a purchased license
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add more users to your existing license, `contact us <https://mattermost.com/contact-us/>`_.

You may incur retroactive charges for any unique users added that exceed the licensed total unique users in the current paid subscription. The retroactive charge per user will be the initial subscription cost per user.

Renewing an Enterprise license
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Mattermost Server version 5.32 and later you can renew your self-managed Mattermost Enterprise license with a credit card if you have a standard Mattermost contract. When you renew your license, you can also increase the number of active users.

If you have not upgraded to v5.32 you can contact Support (support@mattermost.com) to renew your license.

If you're a Mattermost Cloud customer, your subscription auto-renews so you don't need to follow this process.

If you are a reseller, have a non-standard contract, or want to adjust the number of active users on your license during the license period, please contact sales@mattermost.com.

System Admins will be alerted 60 days prior to license expiry via a banner in Mattermost. Select **Renew license now** to start the renewal process in the Customer Portal. You can also dismiss the banner and renew your license at a later date via **System Console > Edition and License**.

Once you select **Renew license now**, you're taken to the renewal page in the Customer Portal, which lists your license information and account details. This is pre-populated based on the email address associated with your existing license subscription.

**To process your license renewal**

1. Enter your **Account Details**, **Additional Contact**, and **Payment Details**.
2. Confirm the `Mattermost Enterprise Edition <https://mattermost.com/pricing-self-managed>`_.

  * You can upgrade from E10 to E20, but it's not possible to downgrade.

3. Confirm the listed number of active users is correct. 

 * You can increase the number of licensed users, but you can't decrease it.

4. Select **Complete purchase**. 

An email with the new license key and information on how to upload the license in the System Console will be sent to the email address provided.

You can watch a video overview of the renewal process on `YouTube <https://www.youtube.com/watch?v=Sz_1nhVufHY>`_.

.. raw:: html
  
   <iframe width="560" height="315" src="https://www.youtube.com/embed/Sz_1nhVufHY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~

Are my credit card details safe?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use `Stripe <https://stripe.com/payments>`_ and `Solupay <https://www.solupay.com/>`_ to process credit card transactions. We do not store any credit card details at any stage. Payments made by credit card are authenticated using `3D Secure <https://www.sc.com/bn/ways-to-bank/3d-secure-faq/>`__, which is PCI-DSS compliant.

Should you wish to make payment using another method, please contact our `Billing team <mailto:AR@mattermost.com>`_.

Why do I need to provide my name and physical address when purchasing a license?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost is a U.S. corporation and therefore all business we do is governed by the laws of the United States, in addition to the local laws wherever we are doing business. 

The United States has a number of export control regulations it has implemented to protect national security interests and to promote its foreign policy objectives. Based on these regulations, U.S. companies are prohibited from doing business with specific countries which have been embargoed by the U.S. government. They are also prohibited from exporting certain items to certain countries that have been sanctioned by the U.S. government. In addition, U.S. companies are prohibited from doing business with specific people and/or companies that have been named and listed by the U.S. government. 

In order to comply with these requirements, Mattermost must collect the name and physical address of all individuals and companies it does business with so that it can comply with the U.S. export controls regulations.

What does Mattermost do with this information?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The information you provide is used for a screening process. There are two different purposes for screening: 

- One screening is to ensure against exports of certain restricted goods to countries that are embargoed. In our case, goods refer to our software that has encryption in it.
- The other screening is against people and companies. There are certain people and companies that the government has put on a list (the Denied Party List) that US companies are prohibited from doing any business with for various reasons. They could be terrorists, be on a terrorist watch list, could be helping finance terrorists, could be participating in human rights violations, etc. If they are on the Denied Party List, we are not able to do any business with them.

Who are the sanctioned people, companies, and entities?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Office of Foreign Assets Control (OFAC) maintains a list of sanctioned entities. Some examples include:

- Terrorists
- Banks or other financial institutions that are involved in financing terrorism
- Companies or people that have been involved in human or drug trafficking
- Organizations that have been sanctioned for human rights violations

This will also include people in violation of government contracts because of our business with the U.S. government. Individuals and Companies do not end up on the Denied Party List based on the country they live in but by their actions and conduct.

What does “physical address” mean for software that will be used in many places?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this case, the "physical address" is the location where the individual, who will be receiving the license key, is physically located and will be able to access the software for installation.

How do I renew my license if I don't have internet access?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you don't have access to the internet, please email support@mattermost.com for assistance.

I'm a Mattermost Cloud customer, how do I renew?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your Mattermost Cloud subscription auto-renews so you don't need to follow this process.

How is user defined for Enterprise Edition subscriptions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See our `frequently asked questions about licensing <https://mattermost.com/pricing-self-managed/#faq>`__.

Do I need to pay for deactivated users?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. If you deactivate a user that user is not counted as an active user during your annual renewal process. You can deactivate users manually via System Console and also via Active Directory/LDAP synchronization, the CLI tool, and the server APIs.

If you choose to pull SQL reports from the database to monitor individual activity to make deactivation decisions, and you are running under high user load, we recommend the reports are pulled from a read replica of the database.

Can I use the same license key on multiple self-managed Enterprise Edition servers?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

License keys for unlocking the advanced features in Mattermost Enterprise Edition can only be applied to a single deployment. A deployment consists of either a single Mattermost application server or multiple linked Mattermost application servers in a High Availability configuration with access to a single database.

Customers who purchase the Premier Support add-on to E20 are licensed to run with a single deployment of Mattermost license key in production and up to 4 non-production deployments of Mattermost (for example: development, staging, user acceptance testing, etc.).

Is my license available immediately?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, once your payment is successfully processed your license is immediately available to download.

How will I know when to renew my license?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You will be notified 60 days prior to your license expiry that your license is due for renewal, via a blue banner displayed at the top of your Mattermost window. This banner is only visible to System Admins.

You can select **Renew license now** to begin the renewal process. You can also select the **x** to dismiss the notification. The notification is reactivated when your browser is refreshed or you reload the desktop app.

How long does it take to renew a license?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you’ve started the renewal process, we'll be in contact with you to confirm your order and send you the order form. There may be additional paperwork required. Once we have the signed order form and (if applicable) the necessary paperwork from you, we're able to process the renewal and issue your license key within 24 hours.

What happens to my license if I don't renew in time?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you don't renew within the 60-day renewal period, a 10-day grace period is provided for you to upload a new license key. During this period your Mattermost installation runs as normal, with full access to Enterprise features. During the grace period, the notification banner is not dismissable.

When the grace period expires, your Enterprise version is downgraded to Team Edition. Enterprise features are disabled.
 
What happens when my license expires?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you don't renew your license within the 10-day grace period, your Mattermost version is automatically downgraded to Team Edition so you can still access and use Mattermost. However, Enterprise features will no longer be available and if you are currently using them, the functionality will no longer be accessible.

When you renew, the Enterprise features will become available with the previous configuration (provided no action such as user migration has been taken).

Which features are affected when my Enterprise license expires?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The affected Enterprise features include, but are not limited to, the following:

.. csv-table::
    :header: "Feature", "How it's affected", "What steps do I need to take?"

    "Elasticsearch", "Elasticsearch is automatically disabled and will start using the default database for indexing posts.", "None needed."
    "AD/LDAP, SAML SSO, Office 365 SSO, and Google SSO", "Login options are no longer provided on the sign-in page. Users who previously signed in with one of these methods are no longer able to.
    
    Users who were already signed in can continue to use Mattermost until their session expires or until they log out.", "Users must be migrated to email authentication via **System Console > Users**. Select the drop-down menu for the relevant member, choose **Switch to Email/Password**, enter a new password, and choose **Reset**."
    "AD/LDAP", "Groups in the database are retained but cannot be used. Memberships are frozen in state for group synced teams/channels.
    
    Mentions for AD/LDAP groups are not shown in the autocomplete menu.
    
    Group mentions are no longer highlighted in text and do not trigger new notifications.", "Use the `CLI <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-group>`_ to modify group sync settings for the team/channel."
    "High Availability", "High Availability is disabled. If all nodes in a cluster continue running, the nodes will stop communicating and caches will get out of sync. This is likely to cause delays in messages, notifications, etc.", "None needed."
    "Performance monitoring", "Monitoring is disabled and Grafana will no longer update with new data.", "None needed."
    "Compliance exports", "Jobs are no longer scheduled in the job server. Data is not exported.", "None needed."
    "Data retention", "Jobs are no longer scheduled in the job server. Data is not deleted.", "None needed."
    "Custom terms", "Custom terms no longer displayed to end users on login. Data is retained in the Terms of Service database table.", "None needed."
    "Custom announcement banners", "No longer visible and is replaced by the default announcement banner.", "None needed."
    "Multi-factor authentication (MFA)", "MFA is no longer enforced/required for new accounts but remains enabled for those who configured it.", "None needed."
    "Permissions", "Permissions are retained in the database in a frozen state and cannot be modified in the System Console.", "Use the `CLI https://docs.mattermost.com/manage/command-line-tools.html#mattermost-permissions>`_ to reset permissions to default."
    "Guest accounts", "Guests that are not actively logged in are prevented from logging in. Guests who are actively logged in are able to use Mattermost until their session expires or they log out.", "None needed."
    
Why can't I dismiss the expiry notification banner?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If there's a red expiry announcement banner stating: "Enterprise license is expired and some features may be disabled. Please contact your System Administrator for details." it means your grace period has expired. This announcement banner persists until the license is renewed, and is visible to users.

Once a new license is applied, the banner will no longer be visible.

If you don't plan to renew your Enterprise Edition subscription, revoke the expired license in **System Console > Edition and License**.

Do you have a program for official non-profits, open-source projects, and charities?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. The Mattermost Nonprofit License enables eligible charities, open-source projects and non-profit organizations to apply the benefits of Mattermost E10 to advancing their missions with special non-profit pricing. 

The Mattermost Nonprofit License includes a three-year Mattermost E10 Enterprise Edition subscription for up to 1,000 users with a subscription fee of $250 USD. Upon acceptance of these terms, Mattermost has the right to place the name and logo of the nonprofit or charitable institution on our website. Following the three-year free license, the institution can renew the license every three years for an additional $250 USD subscription fee.

For greater than 1,000 users, please contact us at community[at]mattermost.com to learn more about your options.

An eligible organization needs to be an official nonprofit or charity, and also non-government, non-academic and non-commercial in nature, with no religious affiliation and that would otherwise be unable to afford the commercial version of Mattermost software. If your organization doesn’t fit this description, we suggest that you purchase a `commercial license <https://mattermost.com/pricing-self-managed/>`_ instead.

There is currently no official program for Mattermost Cloud. Please contact us at community[at]mattermost.com for inquiries on using Mattermost Cloud for your non-profit, open-source porject or charity.

Do you have discounted licenses for academic institutions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, for academic institutions we offer `Mattermost Enterprise Edition Standard <https://mattermost.com/education/>`_ for no charge to students (staff members pay the regular price). You need to pay for at least 10 staff members in order to qualify for an academic license. Please see `Mattermost Academic Licensing <https://docs.google.com/forms/d/e/1FAIpQLSfdl9fTwahgMQu0hb65A58OWzzR3541VwU-MbT0f3y1ND4QhA/viewform>`_ for more information.

Is there a maximum number of users per subscription?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No, there is no limit to the subscription value or number of users you can purchase per product.

Can other members of my organization use this account to manage our subscription?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We currently support a single account/user per organization. The ability to add multiple users per organization will be available in a future release.

What happens if my department buys Mattermost Enterprise Edition and then central IT buys a high volume license that also covers my department?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Enterprise Edition subscriptions and support benefits are licensed per production instance.

When the subscription term for your department's production instance expires, you can either discontinue your department's production instance and move to the instance hosted by central IT (which can optionally provision one or more teams for your department to control), or you can renew your subscription to maintain control of your department's instance (e.g., to configure or customize the system in a manner highly specific to your line-of-business) in addition to using the instance from central IT.

Where can I find the license agreement for Mattermost Enterprise Edition?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Enterprise Edition can be used for free without a license key as commercial software functionally equivalent to the open source Mattermost Team Edition licensed under MIT. When a license key is purchased and applied to Mattermost Enterprise Edition, additional enterprise features unlock. The license agreement for Mattermost Enterprise Edition is included in the software and also available `here <https://mattermost.com/enterprise-edition-license/>`_.

How do I delete my Customer Portal account?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please contact Mattermost Support for assistance with deleting your Customer Portal account.

What happens to my license when I delete my account?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When an account is deleted, the license remains valid. When the license is close to expiring, you'll need to create a new profile in order to purchase a new license.
