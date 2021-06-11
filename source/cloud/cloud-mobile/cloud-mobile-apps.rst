
Mobile Applications Guide
=========================

There are three main options for deploying the Mattermost Mobile Apps.

Install from Apple App Store and Google Play
--------------------------------------------

For quick and easy deployment, you can download the Mattermost mobile apps directly from the Apple App Store and Google Play. Please see our guide on :doc:`installing from the Apple App Store and Google Play Store <mobile-appstore-install>` for more details. 

This option is recommended for:

1. Testing out the mobile applications
2. Team Edition servers using no push notifications, or push notifications from Mattermost's :ref:`TPNS <tpns>` (Test Push Notification Service)
3. Enterprise Edition servers using push notifications from Mattermost's :doc:`HPNS <mobile-hpns>` (Hosted Push Notification Service)

Build the apps yourself
------------------------

To customize the mobile apps, you can fork the open source repository and :doc:`compile your own versions <mobile-compile-yourself>` of the Mattermost mobile applications and Mattermost push proxy server. 

This option is recommended for:

1. Organizations that want to customize the mobile apps
2. Team Edition and Enterprise Edition servers that prefer to host their own push proxy server instead of using one of Mattermost's hosted versions

Use an EMM provider with Managed App Configuration
---------------------------------------------------

To meet other security and compliance policies, you can :doc:`deploy the Mattermost apps with any EMM provider <mobile-appconfig>` that supports `AppConfig <https://www.appconfig.org/members/>`__, such as MobileIron, Blackberry UEM, or Airwatch. You will still need to choose either the App Store/Google Play versions or apps compiled yourself to use in conjunction with the EMM provider.

This option is recommended for organizations that typically use EMM solutions to deploy mobile apps to meet security and compliance policies.

.. note::
    App wrapping via an EMM provider is untested, and not supported by Mattermost. Instead, we recommend using an EMM provider that supports Managed App Configuration.  

    Many app wrapping toolkits, for example `Citrix MDX <https://docs.citrix.com/en-us/mdx-toolkit/about-mdx-toolkit.html>`_, also provide `Managed App Configuration options <https://docs.citrix.com/en-us/xenmobile/server/policies/app-configuration-policy.html>`_. We recommend contacting your provider for more information on what deployment options are available.
