Deploy Mattermost Mobile Apps
=============================

This documentation provides foundational information you need when developing a plan for an enterprise mobile application deployment. It’s intended for business leaders, system administrators, and mobile app champions responsible for deploying Mattermost in their organization.

This documentation provides information to help you: 

- Determine the ideal mobile deployment model for your organization.
- Understand what’s required to build your own Mattermost Mobile Apps.
- Deploy Mattermost Mobile Apps.

.. note::

    - Mattermost Cloud customers must use Mattermost pre-built public apps for mobile deployment. 
    - Some features described in this guide are available only in Mattermost Enterprise.

Decision Summary
----------------

When planning for a mobile app deployment, you have two important decisions to make: 

- What app will you deploy?
- How will you deploy it?

Using Mattermost’s pre-built apps is the easiest and fastest approach since your users can download the apps from public app stores, including the `Apple App Store <https://www.apple.com/ca/app-store>`__ and the `Google Play Store <https://play.google.com/store>`__. Alternatively, you can use an EMM provider to enforce or restrict specific security policies. See `Using Mattermost’s Pre-Built Apps <https://docs.mattermost.com/mobile/use-prebuilt-mobile-apps.html>`__ to learn more about using Mattermost pre-built apps.

If you want to control the look, feel, or capabilities of the mobile apps, host your own push proxy server, or to maintain full control over app distribution, you can build your own mobile apps and manage your own app distribution. See `Building and Distributing Your Own Custom Mattermost Mobile Apps <https://docs.mattermost.com/mobile/build-custom-mobile-apps.html>`__ to learn more about working with custom apps.

The following table summarizes the key differences between these two approaches:

+----------------------------------------------------------------+---------------------------------------------------------------------+
| **Use Pre-Built Apps (Highly Recommended)**                    | **Build Custom Apps (Not Easy)**                                    |
+================================================================+=====================================================================+
| **Recommended for:**                                           | **Recommended for:**                                                |
|                                                                |                                                                     |
| Self-supporting teams who need standard features               | Teams that need to customize the app, adhere to corporate           |
| and have minimal corporate compliance rules.                   | compliance rules, or prefer to host their own push proxy server.    |
+----------------------------------------------------------------+---------------------------------------------------------------------+
| **Benefits:**                                                  | **Benefits:**                                                       |
|                                                                |                                                                     |  
| - Easiest way to deploy Mattermost Apps.                       | You maintain full control over the distribution of applications,    |
| - Test push notifications using the Test Push                  | including the look, feel, and capabilities of your mobile app.      |
|   Notification Service (TPNS)                                  |                                                                     |
| - Mattermost Enterprise includes a                             | **Limitations:**                                                    |
|   Hosted Push Notification Service (HPNS).                     |                                                                     |
| - Apps update automatically with the latest                    | - Requires development knowledge and resources to maintain mobile   |
|   features, enhancements, and security updates.                |   app code as Mattermost releases new product updates.              |
|                                                                | - You must deploy your own push proxy server.                       |
| **Limitations:**                                               |                                                                     |
|                                                                |                                                                     |  
| - Can’t control the look, feel, and capabilities               |                                                                     |  
|   of Mattermost Mobile Apps.                                   |                                                                     |
| - Can’t deploy your own push proxy server.                     |                                                                     |  
+----------------------------------------------------------------+---------------------------------------------------------------------+

Technical and Security Requirements
-----------------------------------

See our `Supported Devices/Mobile Device Requirements <https://docs.mattermost.com/install/requirements.html#mobile-apps>`__ documentation for basic mobile device requirements, and our `Supported Mattermost Server Versions <https://docs.mattermost.com/administration/mobile-changelog.html>`__ documentation for details on Mattermost Server minimum requirements. 

We recommend running the latest version of the Mattermost Server as it contains the most recent features and applicable security updates. If this is not possible, we encourage you to be on the most recent Extended Support Release version of Mattermost. This release has critical feature updates that will ensure compatibility in a number of areas, including the Mattermost Push Notification Service (MPNS).

Important
Not all provided updates are compatible with all previous versions of Mattermost. Updating only Mattermost Mobile apps or updating the mobile apps before updating Mattermost Server can result in incompatibility issues.

You should also start thinking about technical and security requirements in parallel with an implementation plan. Feel free to use our `implementation plan template <https://docs.mattermost.com/getting-started/implementation_plan.html>`__ available in the Mattermost documentation. 

Also, start engaging your technical and security teams with the following questions:

- Are there any known security or access requirements?
- Is an `Enterprise Mobile Management (EMM) Provider <https://docs.mattermost.com/mobile/deploy-mobile-apps-using-emm-provider.html>`__ needed?
- Is a `VPN connection required <https://docs.mattermost.com/mobile/deploy-mobile-apps-using-emm-provider.html#consider-mobile-vpn-options>`__?

Asking questions like these requires you to pause before jumping into your Mattermost mobile project. However, it will help ensure you see a return on your investment.

Getting Help
------------

If you need assistance, please reach out using one or more of the following methods.

- **Community** - Join our Mattermost community and post your specific questions in the `Developers: Mobile <https://community-daily.mattermost.com/core/channels/native-mobile-apps>`__ channel to work with one of the best open source communities around. 
- **Documentation** - We link to a lot of mobile-specific documentation within this guide, but we encourage you to visit all of our `product documentation <https://docs.mattermost.com/>`__.
- **Forums** - For more troubleshooting help, `open a new topic in our forums <https://forum.mattermost.org/c/trouble-shoot>`__ with steps to reproduce your issue.
- **GitHub** - `Visit us on GitHub <https://github.com/mattermost/>`__ to create issues in any of our repositories.
- **Enterprise Support** - If you are a Mattermost Enterprise Edition subscriber, you may open a support ticket in the `Enterprise Edition Support portal <https://support.mattermost.com/>`__.
