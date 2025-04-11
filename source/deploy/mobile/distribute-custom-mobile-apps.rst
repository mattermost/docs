Distribute a custom mobile app
================================

To control the look and feel of the Mattermost mobile app requires building your own mobile apps, :doc:`hosting your own push proxy service </deploy/mobile/host-your-own-push-proxy-service>`, and managing your own app distribution.

.. note::

   - Mattermost Enterprise customers are eligible for support guidance on distributing their own custom mobile apps.
   - With the release of Mattermost mobile app v2.0, mobile app v1.55 becomes the official :doc:`extended support mobile release </about/mattermost-mobile-releases>`, and v1.55 will continue to be supported for an extended timeframe.

Key considerations
-------------------

The Mattermost Mobile App is an open source project. Customizing Mattermost mobile apps requires a fork of the source code. Your team will be responsible for maintaining that fork, as well as keeping that fork updated with any changes made by Mattermost.

Building your own mobile apps will present some challenges, including:

- Installing the necessary developer tools (such as Nodejs, XCode Developer Tools, Android SDKs, as well as others).
- Obtaining and providing certificates for your custom Mattermost mobile apps*.
- Signing your custom Mattermost mobile apps*.
- Distributing your Mobile app to your users.

This means that you manage the maintenance of your custom Mattermost mobile apps, such as rebuilding and incorporating feature and/or security updates. If this isn't done regularly, your applications won't match the functionality of our publicly-available applications, and could be incompatible with future versions of Mattermost Server.

This process can be complicated and can greatly increase deployment time, not only initially, but whenever the mobile apps need to be updated. We recommend having your development team `review the Mattermost Mobile Apps developer documentation <https://developers.mattermost.com/contribute/mobile/>`__ to ensure they understand the scale and requirements of taking this path. This documentation provides guidance on building, compiling, signing, and white-labeling Mattermost Mobile apps.

URL schema limitations
~~~~~~~~~~~~~~~~~~~~~~

If you are building your own version of Mattermost's mobile client, you need to be aware of the following limitations:

- To allow users to simultaneously run the App Store versions of Mattermost, in addition to the custom company version, you will need to adapt the URL schemes used for the app in the build, as well as configure those schemes on the server using :ref:`App Custom URL Schemes <configure/site-configuration-settings:app custom url schemes>`
- Be aware that the ``bundleid`` for the application should not include ``rnbeta``.
- The same change would be required in a custom build of the Mattermost desktop app.
- The mobile and desktop custom clients would no longer be able to log into other Mattermost servers (unless they had the same custom app schema configuration change applied).

Deployment options
------------------

When you decide to build your own Mattermost mobile apps, you have multiple ways to deploy them to your organization.

Our recommend approach is to submit your app to an Enterprise App Store. Once your custom app is added to your own enterprise App Store, your users can download it from the store directly or from an EMM catalog.

Alternatively, use `an Enterprise Mobile Management (EMM) provider </deploy/mobile/deploy-mobile-apps-using-emm-provider>` to push the mobile app to the user’s device, and use the AppConfig standard to enforce a selection of app-specific controls. Or, you can use `another distribution method <#using-another-distribution-method>`__, such as a file sharing platform.

You can also submit your app to `public app stores <#using-public-app-stores>`__. This is the same process Mattermost uses to make Mattermost mobile apps available for everyone. However, before your app can be listed on the public app stores, you need to submit it to the public app stores for review and approval. 

- As part of the submission process, you need to identify an update strategy that accounts for the release of new versions of Mattermost mobile apps that includes reviewing compatibility requirements, validating mobile app versions connecting to the server, and updating Mattermost server. 
- We highly recommend you update your custom Mattermost mobile apps to incorporate any security or service releases. 
- Prior to distribution, check any compatibility requirements for the mobile apps and the Mattermost server.
- Not all provided updates are compatible with all previous versions of Mattermost server. Updating only Mattermost mobile apps or updating the mobile apps before Mattermost Server can result in incompatibility issues.

Custom whitelabeling
--------------------

Ensure you select a unique app name that helps users distinguish your version from others, such as "<Your Company Name> Collaboration". See our `Brand and Visual Design Guidelines <https://handbook.mattermost.com/operations/operations/company-processes/publishing/publishing-guidelines/brand-and-visual-design-guidelines#name-usage-guidelines.html>`__ in our company Handbook for details.