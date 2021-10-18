Mattermost Cloud Billing
========================

|all-plans| |cloud|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

Mattermost Cloud is offered as a pay-as-you-go subscription service.

You will be billed for registered users in your workspace. A registered user is a user who has an account in a workspace and does not show as *Inactive* in **System Console > User Management > Users**. Registered users will count towards your monthly invoice each day as long as they are not deactivated in the billing period.

Customers who signed up for a Mattermost Cloud workspace from our October 2020 launch can continue to use their Cloud instance free of charge for up to ten registered users; however, these customers must upgrade to a per-user pricing model after reaching 11 or more registered users. New Mattermost Cloud workspaces can trial Mattermost Cloud free for 14 days before being required to upgrade to a monthly per-user subscription. 

Billing Period
--------------

After you begin your Mattermost Cloud paid subscription, your first charge will happen at the end of the calendar month. Subsequent billing periods will begin at 12 AM UTC on the first day of each calendar month and end at 11:59 PM UTC on the final day of the same calendar month. Per-user pricing for each billing period will be based on the number of registered users.

Adding and removing users in the middle of a billing period
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you add new users in the middle of a billing cycle, you'll only be charged for the days that the user is registered.

Here's an example:

Your organization has a Mattermost Cloud workspace, and you're on a monthly subscription at the rate of $10 USD per user per month. You add a new user on the 11th day of a 30-day billing period, and that user remains registered for the remainder of the billing period.

The prorated subscription cost for this user is determined by multiplying the monthly amount ($10 USD) by the number of days they are actively registered in the billing period (20) and dividing by the number of days in the month (30).

The prorated subscription cost for the user added on day 11 is $6.67 USD.

Similarly, if you make a registered user inactive in the middle of a billing cycle, we will calculate the prorated amount using the formula above to determine the prorated charge.

Viewing and Managing Billing Details
------------------------------------

You can view your billing details in **System Console > Billing & Account**.

Subscription
~~~~~~~~~~~~

The subscription screen outlines the details of your Mattermost Cloud plan, including the cost per user per month and the number of users currently registered in your workspace. You can also find a summary of your last invoice in the same page.

Billing history
~~~~~~~~~~~~~~~

The Billing History screen contains a list of all your monthly invoices and payments. Invoices appear immediately after the billing period ends.

Billing periods begin at 12 AM UTC on the first day of each calendar month and end at 11:59 PM UTC on the final day of the same calendar month, at which time subscription costs are calculated, and a credit card charge is automatically attempted. It may take up to a day for our billing systems to calculate, charge your credit card, and issue your invoice. Once charges are completed, the invoice will show as *Paid*. The invoice is a downloadable PDF file.

If you have a payment failure, your invoice will show *Payment Failed*. Please review the accuracy of your credit card information in **Payment Information**. Unresolved failed payments may result in a delinquency and an interruption to your subscription.

Company information
~~~~~~~~~~~~~~~~~~~

The **Company Information** screen contains an area to add your company address where you are physically located. The company address will appear on your invoice if specified. Otherwise, the billing address associated with the credit card on file will be used.

Payment information
~~~~~~~~~~~~~~~~~~~

Credit cards are the only form of payment for customers on a monthly billing cycle. All major credit cards are accepted.

Mattermost has engaged third party payments processor Stripe to safely collect and store your credit card information. You may only store information pertaining to one credit card.

We offer pricing and billing only in U.S. Dollars (USD) at this time. Payment will be made in USD converted using the exchange rate from at the time of the transaction.

Sales tax and VAT
~~~~~~~~~~~~~~~~~

Mattermost reserves the right to assess applicable taxes as required by local law. Depending on location, you may be charged transaction taxes when purchasing our product. Prices on our website are exclusive of sales tax or VAT.

Failed or late payments
~~~~~~~~~~~~~~~~~~~~~~~

You will be notified immediately of failed payments both in-product with a banner and via email. The notifications provide directions on how to update payment information. Once payment information is updated, you will be charged right away for the amount owing from the previous billing period. If payment information is not updated and the account remains in arrears, here's what to expect:

.. csv-table::
   :header: "Time in arrears", "Action taken"

   "7 days", "An email is sent to the workspace Administrator with directions to update payment information."
   "14 days", "Another email is sent to the workspace Administrator with directions to update payment information."
   "30 days", "An email is sent to the workspace Administrator indicating that the workspace will be suspended in a further 60 days."
   "90 days", "A final email is sent to the workspace owner. The workspace will be suspended, preventing access by all users and Administrators."
   "97 days", "The workspace and all data is deleted."

Suspended workspaces can be reactivated by contacting Mattermost Customer Support at `https://customers.mattermost.com/cloud/contactus <https://customers.mattermost.com/cloud/contactus>`_.

Once a workspace has been deleted, contents can not be re-instated.  You will need to create a new workspace at that time from https://mattermost.com/get-started/. 
