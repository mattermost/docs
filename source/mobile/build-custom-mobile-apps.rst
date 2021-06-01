Building and Distributing Your Own Custom Mattermost Mobile Apps
================================================================

You can build and distribute custom versions of the Mattermost Mobile App. Choosing this approach means `you've decided not to use the mobile app Mattermost has made available <https://docs.mattermost.com/mobile/use-prebuilt-mobile-apps.html>`__ through public app stores.

This approach is recommended for:

- Organizations that want to customize their Mattermost Mobile Apps.
- Customers using self-hosted Mattermost Team Edition or Enterprise Editions that prefer to host their own push proxy server instead of using one of Mattermost’s hosted versions.
  
Deployment Options
------------------

When you decide to build your own Mattermost Mobile apps, you have multiple ways to deploy it: 

- Submitting your app to `an Enterprise App Store <#using-an-enterprise-app-store>`_
- Using `an Enterprise Mobile Management (EMM) provider <https://docs.mattermost.com/mobile/deploy-mobile-apps-using-emm-provider.html>`__.
- Submitting your app to `public app stores <#using-public-app-stores>`_
- Using `another distribution method <#using-another-distribution-method>`_.

Developing and Maintaining Your Custom App
------------------------------------------

The Mattermost Mobile App is an open source project. Customizing Mattermost Mobile apps requires a fork of the source code. Your team will be responsible for maintaining that fork, as well as keeping that fork updated with any changes made by Mattermost.

This means that you must maintain your custom Mattermost Mobile apps. Maintenance includes rebuilding and incorporating feature and/or security updates. Otherwise, your applications will not match the functionality of our publicly available applications, and could be incompatible with future versions of Mattermost server.

This process can be complicated and can greatly increase deployment time, not only initially, but whenever the apps need to be updated. We recommend having your development team `review the Mattermost Mobile Apps developer documentation <https://developers.mattermost.com/contribute/mobile/>`__ to ensure they understand the scale and requirements of taking this path. This documentation provides guidance on building, compiling, signing, and customizing Mattermost Mobile apps.

In general, building your own Mobile apps will present some challenges, including:

- Installing the necessary developer tools (such as Nodejs, XCode Developer Tools, Android SDKs, as well as others).
- Obtaining and providing certificates for your custom Mattermost Mobile apps. *****
- Signing your custom Mattermost Mobile apps. *****
- Distributing your Mobile app to your users.

***** Mattermost Mobile apps are signed and have certificates associated with Mattermost and public app stores. This means Mattermost’s Mobile App won’t work if you choose to privately host the Mattermost Push Proxy Service (MPNS). You'll need to build your own custom mobile app.

Custom Mobile App Branding
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure you select a unique app name that helps users distinguish your version from others, such as "<Your Company Name> Chat". See our `Brand and Visual Design Guidelines <https://handbook.mattermost.com/operations/operations/company-processes/publishing/publishing-guidelines/brand-and-visual-design-guidelines#name-usage-guidelines>`__ in our Company Handbook for branding details.

Deploying Your Custom App
-------------------------

You have a number of ways to deploy your custom app for your users to download to their mobile devices.

Using an Enterprise App Store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the most common way for customers to distribute their apps, and it’s our recommended approach. Once your custom app is added to your own Enterprise App Store, your users can download it from the store directly or from an EMM catalog. 

Alternatively, you can use an EMM provider to push the application to the user’s device, then use the AppConfig standard to enforce a selection of app-specific controls. See our `Manage App Configuration Using AppConfig <https://docs.mattermost.com/mobile/deploy-mobile-apps-using-emm-provider.html#manage-app-configuration-using-appconfig>`__ documentation for details.

Using an EMM Provider
~~~~~~~~~~~~~~~~~~~~~

See our `Deployment Using an EMM Provider <https://docs.mattermost.com/mobile/deploy-mobile-apps-using-emm-provider.html>`__ documentation to learn more about deploying your custom Mattermost Mobile apps through an EMM provider.

Using Public App Stores
~~~~~~~~~~~~~~~~~~~~~~~

This is the same process Mattermost uses to make Mattermost Mobile apps available for everyone. It’s a good choice if you're looking to white-label your own Mobile apps to remove Mattermost branding. To submit an app to the public app stores, you need to submit the app to public app stores for review and approval.

As part of the submission process, you need to identify an update strategy that accounts for the release of new versions of Mattermost Mobile apps. 

This update strategy should include:

- Reviewing compatibility requirements
- Validating mobile app versions connecting to the server
- Updating Mattermost Server
- Updating Mattermost Mobile apps

We highly recommend you update your custom Mattermost Mobile apps to incorporate any security or service releases. Prior to distribution, check any compatibility requirements for the Mobile apps and the Mattermost Server. Consult the `Mattermost Mobile App Changelog <https://github.com/mattermost/mattermost-mobile/blob/master/CHANGELOG.md>`__ and the `Mattermost Server Changelog <https://docs.mattermost.com/administration/changelog.html>`__ for details.

.. important::

    Not all provided updates are compatible with all previous versions of Mattermost Server. Updating only Mattermost Mobile apps or updating the mobile apps before Mattermost server can result in incompatibility issues.

Using Another Distribution Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can set up an alternate distribution method to deploy your custom app, such as a file sharing platform.
