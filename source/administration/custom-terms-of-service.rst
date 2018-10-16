.. _custom-terms-of-service:

Custom Terms of Service (Beta) (E20)
=====================================

Available in `Enterprise Edition E20 and higher <https://about.mattermost.com/pricing/>`_.

In Mattermost Enterprise Edition E20, you can outline custom Terms of Service for your team members to accept before they can access Mattermost on web or desktop.

.. note::

 Users on mobile will not be presented with the custom Terms of Services. Mobile support is scheduled for an upcoming release.

Configuring Terms of Service
--------------------------------

To enable custom terms of service:

1. Go to **System Console > Customization > Legal and Support**.
2. Set **Enable Custom Terms of Service** to **true**.
3. Set **Custom Terms of Service Text** which contains your terms. Note that Markdown-formatting, including lists, headings and bolding, is supported.
4. Click **Save**.

Once saved, all users must accept the terms of service by clicking **I Agree** next time they log in, or on the next page refresh. If they do not accept, they will be logged out.

.. note::

 If you make an update to your terms of service, make sure to update your terms of service link at **System Console > Customization > Legal and Support > Terms of Service link**.
 
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

Terms of service is presented to users on login and account creation, and available to users at all times in the link specified at **System Console > Customization > Legal and Support > Terms of Service link**.

This feature is intended to meet compliance requirements for large Enterprise companies.
