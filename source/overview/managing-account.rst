Account Management
----------------------

Mattermost offers a secure self-service portal where you can manage your Mattermost:

* Subscription purchases
* Licenses
* Account password
* Organization information
* Payment methods

The self-service portal currently only applies to on-premises Mattermost deployments. Cloud deployments will be supported in a future release.

Purchasing an Enterprise license
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log in to your Mattermost customer profile. If you haven't created a profile, follow the steps provided on the landing page, validate your email address, and then log in.
2. Choose a subscription type, enter the number of users in the **Order summary** field.
3. (Optional for E20) You can add Premier Support, the cost of which is automatically added to your order total.
4. Select **Next Step**.
5. Enter your billing and payment information.
6. Accept the **Terms**
7. Select **Complete**.

Choose **Download the license key**, and navigate to the Mattermost System Console to apply it.

If you experience any problems with your transaction, please contact our Support Team. If possible, keep the error message/number
that you received on hand as it may assist with their investigation.

Applying the license key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   If you are not a System Admin, you will not have access to the System Console to apply the license.


Navigate to the **Subscriptions** page of your Mattermost account. Select **Download License** to download the license key for your subscription. Then, in Mattermost,
open **System Console > About > Edition and License**. Follow the steps provided to apply your license key.

Viewing license information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can view your license start date, expiry date, number of users and license type in your account under **Subscription**.

Adding more users to a purchased license
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add more users during your subscription period without requesting a license.

During the annual renewal, a retroactive charge will be placed for any unique users added during the past subscription period that is
above the licensed total unique users in the current paid subscription. The retroactive charge per user will be the initial subscription
cost per user.

Renewing an Enterprise license
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Log in to the Customer Portal and select the Enterprise Edition you want to renew, the user count, and your contact information. To find the user count you want to renew for, log in to Mattermost as a System Admin and go to **System Console > Site Statistics**, where **Total Active Users** displays the user count on your server.

After submitting the renewal form, our renewal team will get in contact with you about your new subscription.

New users added during the subscription period will have a retroactive charge. `Learn more here <https://docs.mattermost.com/overview/faq.html#how-can-i-add-more-users-to-my-subscription>`__.


Managing license renewals
~~~~~~~~~~~~~~~~~~~~~~~~~~

When your subscription is due for renewal, you'll receive a reminder email a month prior to the expiry date. You can then
log into your Mattermost account on the Customer Portal, navigate to **Subscriptions**, and choose **Renew** next to the relevant
subscription. The renewal can be done a month in advance and will be in effect from the previous expiry date. You do not
have to download a new license.
< If a customer renews early, how is that renewal provisioned? Is it possible to renew early or do we just recommend
auto-renewal? What about mid-term renewals if they want to add seats? >


Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Are my credit card details safe?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use Stripe to process credit card transactions. We do not store any credit card details at any stage. Payments made by credit card
are authenticated using 3D Secure.

Should you wish to make payment using another method, please contact our Billing team <>

Can I download the Privacy Policy?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Where are my details stored and can I access them for GDPR requirements?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


How is user defined for Enterprise Edition subscriptions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#faq>`__.


Do I need to pay for deactivated users?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. If you deactivate a user that user is not counted as an active user during your annual renewal process. You can deactivate users manually via System Console and also via Active Directory/LDAP synchronization, the CLI tool, and the server APIs.

If you choose to pull SQL reports from the database to monitor individual activity to make deactivation decisions, and you are running under high user load, we recommend the reports are pulled from a read replica of the database.

Can I use the same license key on multiple Enterprise Edition servers?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Customers who purchase the Premier Support add-on to E20 are licensed to run with the same Mattermost license key in a production deployment and up to 4 non-production deployments of Mattermost (for example: development, staging, user acceptance testing, etc.).

Without the purchase of Premier Support, license keys for unlocking the advanced features in Mattermost Enterprise Edition should only be applied to a single deployment. A deployment consists of either a single Mattermost application server, or multiple linked Mattermost application servers in a high availability configuration.

Is my subscription active immediately?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, once your payment is successfully processed your license is immediately available in your account.

Is there a limit to the subscription value I can purchase?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No, there is no limit to the subscription value or number of users you can purchase per product.

How many users can have access to an account?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

< This should possibly be removed as it may open up a dialog around the fact that multiple people can use the same
account by sharing the username/password >

What happens if my department buys Mattermost Enterprise Edition and then central IT buys a high volume license that also covers my department?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost Enterprise Edition subscriptions and support benefits are licensed per production instance.

When the subscription term for your department's production instance expires, you can either discontinue your department's production instance and move to the instance hosted by central IT (which can optionally provision one or more teams for your department to control), or you can renew your subscription to maintain control of your department's instance (e.g., to configure or customize the system in a manner highly specific to your line-of-business) in addition to using the instance from central IT.


How do I delete my account?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please contact Mattermost Support for assistance with deleting your account.

What happens to my license when I delete my account?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When an account is deleted, the license remains valid. However, auto-renewal is cancelled. When the license
is close to expiring, you will need to create a new profile in order to purchase a new license.
