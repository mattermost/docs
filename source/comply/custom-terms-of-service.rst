.. _custom-terms-of-service:

Custom terms of service
=======================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Mattermost Enterprise Edition E20*

System Admins can outline custom Terms of Service for their team members to accept before they can access Mattermost on web, desktop, or mobile.

Configuring terms of service
----------------------------

To enable custom terms of service:

1. Go to **System Console > Compliance > Custom Terms of Service**.
2. Set **Enable Custom Terms of Service** to **true**.
3. Set **Custom Terms of Service Text** which contains your terms. Markdown formatting is supported, including lists, headings, and bolding.
4. Set **Re-Acceptance Period** to configure the number of days before Terms of Service acceptance expires, and when the terms must be re-accepted. Set to 0 if you don't want your terms to expire.
5. Select **Save**.

Once saved, all users must accept the terms of service by clicking **I Agree** next time they log in, or on the next page refresh. If they do not accept, they will be logged out.

.. note::
 
 If you make an update to your Terms of Service, make sure to update your terms of service link at **System Console > Site Configuration > Customization > Terms of Service link**. This link is presented to all users when they log in, and it's easily accessible to end users after accepting the terms.

Frequently asked questions
--------------------------

What happens if I update my terms of service text?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There will be no impact to your end users. Users will simply be required to accept the new terms on next login or page refresh.

What happens if a user doesn't accept the terms of service?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users won't be able to log in if they don't accept the Terms of Service.

How do I know if my users accepted the terms of service?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each time a user agrees to the terms of service, the agreement is recorded in the database:

- A new field ``AcceptedServiceTermsId`` in the **Users** table indicates the most recent terms of service the user has accepted.
- Each time a user accepts the terms, the action is recorded in the **Audits** table, containing the username, timestamp of acceptance, and other relevant information.

Why isn't this feature in Team Edition for GDPR compliance?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Terms of service is presented to users on login and account creation, and available to users at all times in the link available by going to **System Console > Site Configuration > Customization**.

This feature is intended to meet compliance requirements for large Enterprise companies.
