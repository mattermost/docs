.. _custom-terms-of-service:

Custom Terms of Service (Beta) (E20)
=====================================

Available in `Enterprise Edition E20 and higher <https://about.mattermost.com/pricing/>`__.

In Mattermost Enterprise Edition E20, you can outline custom Terms of Service for your team members to accept before they can access Mattermost on web, desktop or mobile.

Configuring Terms of Service
--------------------------------

To enable custom terms of service:

1. Go to **System Console > Customization > Custom Terms of Service** in prior versions or **System Console > Compliance > Custom Terms of Service** in versions after 5.12.
2. Set **Enable Custom Terms of Service** to **true**.
3. Set **Custom Terms of Service Text** which contains your terms. Note that Markdown-formatting, including lists, headings and bolding, is supported.
4. Set **Re-Acceptance Period**, which sets the number of days before Terms of Service acceptance expires, and the terms must be re-accepted. Set to 0 if you don't want your terms to expire.
5. Click **Save**.

Once saved, all users must accept the terms of service by clicking **I Agree** next time they log in, or on the next page refresh. If they do not accept, they will be logged out.

.. note::

 If you make an update to your Terms of Service, make sure to update your terms of service link at **System Console > Customization > Legal and Support > Terms of Service link** in prior versions or **System Console > Site Configuration > Customization** in versions after 5.12.
 
 This link is presented to all users on each log in, and is easily accessible to end users after accepting the terms.

Frequently Asked Questions
----------------------------

What happens if I update my terms of service text?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There will be no impact to your end users. Users will simply be required to accept the new terms on next login or page refresh.

How do I know if my users accepted the terms of service?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each time a user agrees to the terms of service, the agreement is recorded in the database:

 - A new field ``AcceptedServiceTermsId`` in the **Users** table indicates the most recent terms of service the user has accepted.
 - Each time a user accepts the terms, the action is recorded in the **Audits** table, containing the username, timestamp of acceptance, and other relevant information.

Why isn't this feature in Team Edition for GDPR compliance?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Terms of service is presented to users on login and account creation, and available to users at all times in the link specified at **System Console > Customization > Legal and Support > Terms of Service link** in prior versions or **System Console > Site Configuration > Customization** in versions after 5.12.

This feature is intended to meet compliance requirements for large Enterprise companies.

Why are custom terms of service beta?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This feature is labelled as beta while we verify the quality of the feature in various scenarios. Known issues include:

- Login fails when custom terms of service is enabled and MFA is enforced.
- Terms of service text disappears in the System Console on save until next refresh.
- Terms of service loads immediately following an update to terms, instead of after login or a page refresh.
