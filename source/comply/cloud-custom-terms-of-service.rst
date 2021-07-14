Custom Terms of Service (Beta)
==============================

You can outline custom Terms of Service for your team members to accept before they can access Mattermost on web, desktop, or mobile.

Configuring Terms of Service
----------------------------

To enable custom terms of service:

1. Go to **System Console > Compliance > Custom Terms of Service**.
2. Set **Enable Custom Terms of Service** to **true**.
3. Set **Custom Terms of Service Text** which contains your terms. Note that Markdown-formatting, including lists, headings and bolding, is supported.
4. Set **Re-Acceptance Period**, which sets the number of days before Terms of Service acceptance expires, and the terms must be re-accepted. Set to 0 if you don't want your terms to expire.
5. Select **Save**.

Once saved, all users must accept the terms of service by selecting **I Agree** next time they log in, or on the next page refresh. If they do not accept, they will be logged out.

.. note::

 If you make an update to your Terms of Service, make sure to update your terms of service link at **System Console > Site Configuration > Customization**.
 
 This link is presented to all users on each log in, and is easily accessible to end users after accepting the terms.

Frequently Asked Questions
----------------------------

What happens if I update my terms of service text?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There will be no impact to your end users. Users will simply be required to accept the new terms on next login or page refresh.

What happens if a user does not accept the terms of service?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A user will not be able to log in if they do not accept the terms of service. 

Why are custom terms of service beta?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature is labeled as beta while we verify the quality of the feature in various scenarios. Known issues include:

- Login fails when custom terms of service is enabled and MFA is enforced.
- Terms of service text disappears in the System Console on save until next refresh.
- Terms of service loads immediately following an update to terms, instead of after login or a page refresh.
