Consider mobile VPN options
===========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:


Connect to your private network Mattermost instance
---------------------------------------------------

You need to set up a way to connect to your private network Mattermost instance, using an external proxy with encrypted transport through HTTPS and WSS network connections.

Depending on your security policies, we recommend deploying Mattermost behind a VPN and using a `per-app VPN <#id3>`_ with your EMM provider, or a mobile VPN client.

Also consider deploying a mobile VPN client with multi-factor authentication (MFA) to your preferred login method, such as GitLab SSO with MFA, or run Mattermost Enterprise Edition with :doc:`multi-factor authentication (MFA) </onboard/multi-factor-authentication>` enabled.

Mobile VPN options
------------------

A Virtual Private Network (VPN) allows a device outside a firewall to access content inside the firewall as if it were on the same network.

.. note::
  Some mobile VPN options depend on the requirements of your organization and the demands and/or the needs of your users.

We recommend one of two options: `per-app VPN <#id3>`_ or a `device VPN <#id4>`_ to secure your deployment. Both options are compatible with most EMM providers.

We also recommend you review the following commonly-asked questions about data security on mobile devices:

- :ref:`How data is handled on a device after an account is deleted? <deploy/mobile-faq:how is data handled on mobile devices after a user account is deactivated>`
- :ref:`What post metadata is sent in mobile push notifications? <deploy/mobile-faq:what post metadata is sent in mobile push notifications>`
- :ref:`What are my options for securing the Mobile apps? <deploy/mobile-faq:what are my options for securing the mobile apps>`
- :ref:`What are my options for securing push notifications? <deploy/mobile-faq:what are my options for securing push notifications>`

Per-app VPN
~~~~~~~~~~~

A common approach is to use a per-app VPN. This provides a connection to the VPN when needed (on-demand). If using a per-app VPN with Mattermost, you can configure the following options:

- **useVPN:** Mattermost waits until the connection to the VPN server is established before making any requests (otherwise they will fail). This is only supported on iOS as Android OS cannot support waiting. It still works but the first connection attempt may fail.
- **timeoutVPN (iOS only):** How long to wait for the connection to the VPN server before trying.

Device VPN
~~~~~~~~~~

With this option, all internet traffic routes through the VPN specified in the profile. This could cause issues for personal applications.

Connect via corporate proxy server
----------------------------------

Review the following commonly-asked questions about connecting through a corporate proxy server:

- :ref:`How do I receive mobile push notifications if my IT policy requires the use of a corporate proxy server? <deploy/mobile-faq:how do i receive mobile push notification if my it policy requires the use of a corporate proxy server>`
- :ref:`Deploy Mattermost with connection restricted post-proxy relay in DMZ or a trusted cloud environment <deploy/mobile-faq:deploy mattermost with connection restricted post proxy relay in dmz or a trusted cloud environment>`
- :ref:`Whitelist Mattermost push notification proxy to bypass your corporate proxy server <deploy/mobile-faq:whitelist mattermost push notification proxy to bypass your corporate proxy server>`
- :ref:`Run App Store versions of the Mattermost Mobile apps <deploy/mobile-faq:run app store versions of the mattermost mobile apps>`
