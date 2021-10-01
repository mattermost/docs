=====================
Subscription Overview
=====================

Mattermost offers features through Starter, Professional, or Enterprise subscription plans. Your subscription to a plan determines what features you have access to. When choosing a subscription, you can choose the deployment type - self-hosted or cloud, and the plan - Starter, Professional, or Enterprise. 

Mattermost self-hosted requires a license to be applied to access features in the Professional or Enterprise plans. Mattermost offers a `secure self-service Customer Portal <https://customers.mattermost.com>`__ where you can easily purchase and manage your Mattermost self-hosted subscriptions. When you purchase a subscription, a license is generated. Please see :ref:`self-hosted-subscriptions` for more details. 

Mattermost Cloud is a software-as-as-service, and you can simply sign up and start using Mattermost in a trial mode and upgrade to the edition you desire within the product. Please see :ref:`cloud-subscriptions` for more details.

For more general information and frequently asked questions on licensing and subscriptions, please see below. 


General Frequently Asked Questions
---------------------------------------------------

Are my credit card details safe?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use `Stripe <https://stripe.com/payments>`__ and `Solupay <https://www.solupay.com/>`__ to process credit card transactions. We do not store any credit card details at any stage. Payments made by credit card are authenticated using `3D Secure <https://www.sc.com/bn/ways-to-bank/3d-secure-faq/>`__, which is PCI-DSS compliant.

Should you wish to make payment using another method, please contact our `Billing team <mailto:AR@mattermost.com>`__.

Why do I need to provide my name and physical address when purchasing a subscription?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Mattermost is a U.S. corporation and, therefore, all business we do is governed by the laws of the United States, in addition to the local laws wherever we are doing business. 

The United States has a number of export control regulations implemented to protect national security interests and to promote its foreign policy objectives. Based on these regulations, U.S. companies are prohibited from doing business with specific countries which have been embargoed by the U.S. government. They are also prohibited from exporting certain items to certain countries that have been sanctioned by the U.S. government. In addition, U.S. companies are prohibited from doing business with specific people and/or companies that have been named and listed by the U.S. government. 

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

How is a user defined for subscriptions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the purpose of billing, a “user” is any account created in Mattermost that has not been deactivated by the System Administrator. You can see your user count for billing purposes from the System Console on the **Site Statistics** page under “Total Active Users”. Guests are also defined as users. 

Do I need to pay for deactivated users?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No. If you deactivate a user, that user is not counted as an active user during your annual renewal process. You can deactivate users manually via System Console, and also via Active Directory/LDAP synchronization, the mmctl tool, and the server APIs.

If you choose to pull SQL reports from the database to monitor individual activity to make deactivation decisions, and you are running under high user load, we recommend the reports are pulled from a read replica of the database.

Which features are affected when my subscription expires?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The affected features include, but are not limited to, the following:

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
    
Do you have a program for official non-profits, open source projects, and charities?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. The Mattermost Nonprofit License enables foundations and other nonprofit organizations that support open source projects or other technology initiatives to apply the benefits of Mattermost Enterprise Edition to advancing their missions with special nonprofit pricing.

To be eligible, an organization needs to be an official nonprofit or charity; as well as non-government, non-academic and non-commercial in nature, with no religious affiliation; and that would otherwise be unable to afford the commercial version of Mattermost software. If your organization doesn’t fit this description, we suggest that you purchase a `commercial license <https://mattermost.com/pricing-self-managed/>`__ instead.

Organizations that receive a Mattermost Nonprofit License must make their server publicly-accessible for anyone to sign up and join. Mattermost will also have the right to place the name and logo of the nonprofit or charitable institution on our website.

To apply for the Mattermost Nonprofit License, `please complete this form <https://docs.google.com/spreadsheets/d/1aEpjFLHcrSpJF3wfi2NItevXtYpZUOSbge9o_pLagXU/edit#gid=446002361>`__, or contact us at community[at]mattermost.com.


Do you have discounted subscriptions for academic institutions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, for academic institutions we offer `Mattermost Enterprise Edition Standard <https://mattermost.com/education/>`_ for no charge to students (staff members pay the regular price). You need to pay for at least 10 staff members in order to qualify for an academic license. Please see `Mattermost Academic Licensing <https://docs.google.com/forms/d/e/1FAIpQLSfdl9fTwahgMQu0hb65A58OWzzR3541VwU-MbT0f3y1ND4QhA/viewform>`_ for more information.

Is there a maximum number of users per subscription?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No, there is no limit to the subscription value or number of users you can purchase per product.


What happens if my department buys a Mattermost subscription and then central IT buys a high volume subscription that also covers my department?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost subscriptions and support benefits are per production instance.

When the subscription term for your department's production instance expires, you can either discontinue your department's production instance and move to the instance hosted by central IT (which can optionally provision one or more teams for your department to control), or you can renew your subscription to maintain control of your department's instance (e.g., to configure or customize the system in a manner highly specific to your line-of-business) in addition to using the instance from central IT.
