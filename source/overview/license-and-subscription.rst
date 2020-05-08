Licensing and Subscription
----------------------

Mattermost offers a `secure self-service Customer Portal <https://customers.mattermost.com>`_ where you can easily purchase and manage your Mattermost Enterprise subscriptions.

When you purchase a subscription, a license is generated. This gives you access to Mattermost's Enterprise features. Subscriptions purchased via the Customer Portal are stored and listed in the portal, with license details including their start and end dates, providing you with an at-a-glance overview of your account. You also have full access to your billing history  making it easier to manage purchases and renewal dates.

You can access your Customer Portal account to view information about your:

- Subscription purchases
- Licenses
- Customer Portal account password
- Organization information
- Payment methods
- Renewals (available in a future release)
- Active users (available in a future release)

Purchasing an Enterprise license
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**If you don't have a Customer Portal account**

Open the `Customer Portal page <https://customers.mattermost.com>`__. Enter the required information and check the box to confirm **I have read and agree to the Privacy Policy**. Then select **Next**. When you've completed the process and validated your email address, you can proceed with the steps below. 

**If you have an existing Customer Portal account**

1. Log in to your `Customer Portal <https://customers.mattermost.com>`_ account. 
2. Choose a subscription type and enter the number of users in the **Order summary** field.
   - This indicates the number of users you can have on this subscription's instance. For more information about how users are defined, see our `FAQ <https://about.mattermost.com/pricing/#faq>`_. 
3. (Optional for E20) You can add `Premier Support <https://mattermost.com/support/>`_, the cost of which is automatically added to your order total.
4. Select **Next Step**.
5. Enter your billing and payment information.
6. Accept the **Terms**.
7. Select **Complete**.
8. Choose **Download the license key**.

If you experience any problems with your transaction, please contact our Support Team via the form provided in the Customer Portal. If possible, keep the error message/number that you received on hand as it may assist with their investigation.

Applying the license key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your Mattermost Enterprise license is ready to use and be applied via the Mattermost System Console. 

System Admin access is required in order to apply the license. If you are not a Mattermost System Admin, contact your organization's Mattermost System Admin. 
   
**If you already have Mattermost installed** 

On the Customer Portal **Subscriptions** page, select **Download License** to download the license key for your subscription. In Mattermost, follow the steps provided in **System Console > About > Edition and License** to apply your license key.

You can also use the `CLI <https://docs.mattermost.com/install/ee-install.html#changing-a-license-key>`__ to apply the license.

**For new Mattermost deployments**

If you have not yet installed and deployed a Mattermost instance, visit the `Deployment Guide <https://docs.mattermost.com/deployment/deployment.html>`_ to get started. For information on creating a System Admin account visit the `Administrator Tasks <https://docs.mattermost.com/deployment/on-boarding.html>`_ documentation. 

Viewing license information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For licenses purchased using the Customer Portal, you can view the license start date, expiry date, number of users and license type in your account under **Subscription**.

If you are not able to view this information, please contact your Customer Success Manager. 

Adding more users to a purchased license
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add more users during your subscription period without requesting a license.

You may incur retroactive charges for any unique users added that exceed the licensed total unique users in the current paid subscription. The retroactive charge per user will be the initial subscription cost per user.

Renewing an Enterprise license
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ability to renew your license in the Customer Portal will be available in a future release.
To renew your license in the meantime, contact your CSM to start the renewal process.

Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Are my credit card details safe?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use `Stripe <https://stripe.com/payments>`_ to process credit card transactions. We do not store any credit card details at any stage. Payments made by credit card are authenticated using `3D Secure <https://support.payfast.co.za/article/96-what-is-3d-secure-visa-secure-mastercard-securecode>`__, which is PCI-DSS compliant.

Should you wish to make payment using another method, please contact our `Billing team <mailto:AR@mattermost.com>`_.


How is user defined for Enterprise Edition subscriptions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#faq>`__.


Do I need to pay for deactivated users?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. If you deactivate a user that user is not counted as an active user during your annual renewal process. You can deactivate users manually via System Console and also via Active Directory/LDAP synchronization, the CLI tool, and the server APIs.

If you choose to pull SQL reports from the database to monitor individual activity to make deactivation decisions, and you are running under high user load, we recommend the reports are pulled from a read replica of the database.

Can I use the same license key on multiple Enterprise Edition servers?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

License keys for unlocking the advanced features in Mattermost Enterprise Edition can only be applied to a single deployment. A deployment consists of either a single Mattermost application server, or multiple linked Mattermost application servers in a high availability configuration with access to a single database.

Customers who purchase the Premier Support add-on to E20 are licensed to run with a single deployment of Mattermost license key in production and up to 4 non-production deployments of Mattermost (for example: development, staging, user acceptance testing, etc.).

Is my subscription active immediately?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, once your payment is successfully processed your license is immediately available in your account.

Is there a limit to the subscription value I can purchase?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No, there is no limit to the subscription value or number of users you can purchase per product.

Can other members of my organization use this account to manage our subscription?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We currently support a single account/user per organization. The ability to add multiple users per organization will be available in a future release.


What happens if my department buys Mattermost Enterprise Edition and then central IT buys a high volume license that also covers my department?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Enterprise Edition subscriptions and support benefits are licensed per production instance.

When the subscription term for your department's production instance expires, you can either discontinue your department's production instance and move to the instance hosted by central IT (which can optionally provision one or more teams for your department to control), or you can renew your subscription to maintain control of your department's instance (e.g., to configure or customize the system in a manner highly specific to your line-of-business) in addition to using the instance from central IT.

How do I delete my Customer Portal account?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please contact Mattermost Support for assistance with deleting your Customer Portal account.

What happens to my license when I delete my account?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When an account is deleted, the license remains valid. When the license
is close to expiring, you will need to create a new profile in order to purchase a new license.
