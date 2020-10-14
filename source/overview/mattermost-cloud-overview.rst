=========================
Mattermost Cloud Overview
=========================

Mattermost Cloud is offered as a monthly subscription service. It is available free, indefinitely, for all workspaces that have 10 or fewer active users. Your subscription is upgraded to pay-as-you-go once you reach 11 or more active users.

How Billing Works
-----------------

You are billed for active users in your workspace.  An active user: 

- Has created an account and joined a workspace and shows as **Active** in **System Console > Users**.
- Counts towards your monthly invoice for each day they are active in the billing period.

Users deactivated by a System Administrator are no longer counted toward future monthly invoices.

Billing periods
~~~~~~~~~~~~~~~

When you begin your Mattermost Cloud subscription, after upgrading from the free tier, your first charge is at the end of the calendar month.

Billing periods end at 11:59 P.M. UTC on the final day of the month. We calculate usage for the billing period based on the number of users who were active at that time and charge the credit card stored in your profile.

Adding and removing users in the middle of a billing period
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you add new users in the middle of a billing cycle, we’ll only charge for the days that the user was active. We’ll keep track of this for you, and bill you at the end of the cycle.

Here’s an example:

Your organization has a Mattermost Cloud workspace and you're paying monthly by credit card at rate of $10 USD per user per month. You add a new user 11 days into your billing period and that user remains active for the subsequent 19 days remaining in the month - for a total of 20 days.

The prorated subscription cost for this user is determined by multiplying the monthly amount ($10 USD) by the number of days they were active in the billing cycle (20) and dividing by the number of days in the month (30). 

The prorated subscription cost for the user added on day 11 is $6.67 USD.

Similarly, if you deactivate users in the middle of a billing cycle, we will calculate the prorated amount using the formula above to determine the prorated charge.

Viewing and Managing Billing Details
------------------------------------

Billing details are presented in **System Console > Billing & Account**.

Subscription
~~~~~~~~~~~~

The subscription screen outlines the details of the Mattermost Cloud plan, including the cost per user per month and the number of users currently registered in your workspace. Also on this screen is a summary of your last invoice.

Billing history
~~~~~~~~~~~~~~~

The Billing History screen contains a list of all your monthly invoices and payments. Invoices appear in your billing history immediately after the billing period ends.

Billing periods end at 11:59 P.M. UTC on the last day of the month, at which time subscription costs are calculated and a credit card charge is automatically attempted. It may take up to a day for our billing systems to calculate, charge your credit card, and issue your invoice. Once charges are completed, the invoice will show as *Paid*. The invoice is a downloadable PDF file.

If you have a payment failure, your invoice will show *Payment Failed*. Please review the accuracy of your credit card information in **Payment Information**. Unresolved failed payments may result in a delinquency and an interruption to your subscription.

Company information
~~~~~~~~~~~~~~~~~~~

The **Company Information** screen contains an area to add your company address where you are physically located. The company address will appear on your invoice if specified. Otherwise the billing address associated with the credit card on file will be used.

Payment information
~~~~~~~~~~~~~~~~~~~

Credit cards are the only form of payment for customers on a monthly billing cycle. All major credit cards are accepted.
To add a new credit card first delete the saved card, then select **Add a Credit Card** in the top right of the subsequent screen. Mattermost has engaged third party payments processor Stripe to safely collect and store your credit card information. You may only store information pertaining to one credit card.
To add a new credit card first delete the saved card, then select **Add a Credit Card** in the top right of the subsequent screen. Mattermost only stores information pertaining to one credit card.

We offer pricing and billing only in U.S. Dollars at this time. Payment will be made in USD converted using the exchange rate from at the time of the transaction.

Sales tax and VAT
~~~~~~~~~~~~~~~~~

Mattermost reserves the right to assess applicable taxes as required by local law. Depending on location, customers may be charged transaction taxes when purchasing our product. Prices on our website are exclusive of sales tax or VAT.

Failed or late payments
~~~~~~~~~~~~~~~~~~~~~~~

Administrators are notified immediately of failed payments both in-product with a banner and via email. The notifications provide directions on how to update payment information. Once payment information is updated you are charged right away for the amount owing from the previous billing period. If payment information is not updated and the account remains in arrears, here’s what to expect:

.. csv-table::
   :header: "Time in arrears", "Action taken"

   "7 days", "An email is sent to the workspace Administrator with directions to update payment information."
   "14 days", "Another email is sent to the workspace Administrator with directions to update payment information."
   "30 days", "An email is sent to the workspace Administrator indicating that the workspace will be suspended in a further 90 days."
   "120 days", "The workspace will be suspended, preventing access by all users and Administrators."

Suspended workspaces can be reactivated by contacting Mattermost Customer Support at `https://customers.mattermost.com/cloud/contactus <https://customers.mattermost.com/cloud/contactus>`_.
