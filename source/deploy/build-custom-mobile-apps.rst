Building and distributing your own custom Mattermost mobile apps
================================================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

You can build and distribute custom versions of the Mattermost mobile app. Choosing this approach means :doc:`you've decided not to use the mobile app Mattermost has made available </deploy/use-prebuilt-mobile-apps>` through public app stores. This also means that you've decided to :ref:`host your own push proxy service <deploy/mobile-hpns:host your own push proxy service>`.

This approach is recommended for:

- Organizations that want to customize their Mattermost mobile Apps.
- Customers using self-hosted Mattermost Team Edition, Professional or Enterprise Edition that prefer to host their own push proxy server instead of using one of Mattermost’s hosted versions.

.. note::
   
   - A Mattermost Enterprise subscription plan (or a legacy Enterprise Edition license) is required to request assistance or troubleshooting help from `Mattermost Customer Support <https://mattermost.com/support/>`__ when building and deploying custom mobile apps. Customers on other Mattermost subscription plans can develop and deploy custom mobile apps, but can't request technical support assistance through Mattermost Customer Support.
   - With the release of Mattermost mobile app v2.0, :ref:`mobile app v1.55 becomes the official extended support mobile release <upgrade/extended-support-release:mobile app v1 55 1 extended support release esr>`, and will be supported for an extended timeframe.

Deployment options
------------------

When you decide to build your own Mattermost mobile apps, you have multiple ways to deploy:

- Submitting your app to `an Enterprise App Store <#using-an-enterprise-app-store>`_.
- Using `an Enterprise Mobile Management (EMM) provider <#using-an-emm-provider>`_.
- Submitting your app to `public app stores <#using-public-app-stores>`_.
- Using `another distribution method <#using-another-distribution-method>`_.

Setting up push notifications
-----------------------------

See our :doc:`Mobile Push Notifications </deploy/mobile-hpns>` documentation to learn about setting up push notifications for custom-built mobile apps.

Developing and maintaining your custom app
------------------------------------------

The Mattermost Mobile App is an open source project. Customizing Mattermost mobile apps requires a fork of the source code. Your team will be responsible for maintaining that fork, as well as keeping that fork updated with any changes made by Mattermost.

This means that you manage the maintenance of your custom Mattermost mobile apps, such as rebuilding and incorporating feature and/or security updates. If this isn't done regularly, your applications won't match the functionality of our publicly-available applications, and could be incompatible with future versions of Mattermost Server.

This process can be complicated and can greatly increase deployment time, not only initially, but whenever the mobile apps need to be updated. We recommend having your development team `review the Mattermost Mobile Apps developer documentation <https://developers.mattermost.com/contribute/mobile/>`__ to ensure they understand the scale and requirements of taking this path. This documentation provides guidance on building, compiling, signing, and white-labeling Mattermost Mobile apps.

In general, building your own mobile apps will present some challenges, including:

- Installing the necessary developer tools (such as Nodejs, XCode Developer Tools, Android SDKs, as well as others).
- Obtaining and providing certificates for your custom Mattermost mobile apps*.
- Signing your custom Mattermost mobile apps*.
- Distributing your Mobile app to your users.

***** Mattermost mobile apps are signed, and they have certificates and keys associated with Mattermost and public app stores. This means Mattermost’s Mobile App won’t work if you choose to privately host the Mattermost Push Proxy Service (MPNS). You'll need to build your own custom mobile app.

Custom mobile app branding
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure you select a unique app name that helps users distinguish your version from others, such as "<Your Company Name> Collaboration". See our `Brand and Visual Design Guidelines <https://handbook.mattermost.com/operations/operations/company-processes/publishing/publishing-guidelines/brand-and-visual-design-guidelines#name-usage-guidelines.html>`__ in our company Handbook for details.

Deploying your custom app
-------------------------

You have a number of ways to deploy your custom app for your users to download to their mobile devices.

Using an enterprise app store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the most common way for customers to distribute their apps, and it’s our recommended approach. Once your custom app is added to your own enterprise App Store, your users can download it from the store directly or from an EMM catalog.

Using an EMM provider
~~~~~~~~~~~~~~~~~~~~~

Alternatively, you can use an EMM provider to push the application to the user’s device, then use the AppConfig standard to enforce a selection of app-specific controls.

For additional details, see the following documentation:

- :doc:`Deployment Using an EMM provider </deploy/deploy-mobile-apps-using-emm-provider>` to learn more about deploying your custom Mattermost Mobile apps through an EMM provider.
- :doc:`Manage app configuration using AppConfig </deploy/mobile-appconfig>`  to learn more about managing your app configuration using App Config, and the configuration options that can be sent from the EMM provider to Mattermost mobile apps.

Using public app stores
~~~~~~~~~~~~~~~~~~~~~~~

This is the same process Mattermost uses to make Mattermost mobile apps available for everyone. Before your app can be listed on the public app stores, you need to submit it to the public app stores for review and approval.

As part of the submission process, you need to identify an update strategy that accounts for the release of new versions of Mattermost mobile apps.

This update strategy should include:

- Reviewing compatibility requirements.
- Validating mobile app versions connecting to the server.
- Updating Mattermost Server.
- Updating Mattermost mobile apps.

We highly recommend you update your custom Mattermost mobile apps to incorporate any security or service releases. Prior to distribution, check any compatibility requirements for the mobile apps and the Mattermost server. Consult the :doc:`Mattermost mobile app changelog </deploy/mobile-app-changelog>` and the :doc:`Mattermost server changelog </deploy/legacy-self-hosted-changelog>` for details.

.. important::

   Not all provided updates are compatible with all previous versions of Mattermost Server. Updating only Mattermost mobile apps or updating the mobile apps before Mattermost Server can result in incompatibility issues.

Using another distribution method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can set up an alternate distribution method to deploy your custom app, such as a file sharing platform.
