Deploying Mobile Apps Using an EMM Provider
===========================================

`Enterprise Mobile Management software <https://en.wikipedia.org/wiki/Enterprise_mobility_management>`__ helps enterprise teams manage secure mobile endpoints with managed app configuration. 

You can use an EMM to: 

- Enforce users to download the Mattermost pre-built or custom apps managed by your organization.
- Set default server url address.
- Restrict users from changing servers.
- Enforce security policies.

An EMM provider pushes Mattermost Mobile apps to EMM-enrolled devices. This approach is recommended for organizations that typically use EMM solutions to deploy Mobile apps to meet security and compliance policies. 

Manage App Configuration Using AppConfig
----------------------------------------

AppConfig is our recommended approach for app configuration and management. It was introduced by the `AppConfig Community <https://www.appconfig.org/about/>`__, a group of leading EMM providers and app developers who have come together to make it easier for developers and customers to drive mobility in business. 

AppConfig provides an easy way to configure enterprise mobile apps with any of the EMM providers listed on the `AppConfig website <https://www.appconfig.org/members/>`__. Using AppConfig, you can manage default settings and security controls on both the public app stores, and custom-built mobile clients. For example, you can pre-configure your Mattermost server URL and username.

See our `Mattermost AppConfig Values <https://docs.mattermost.com/mobile/mobile-appconfig.html#mattermost-appconfig-values>`__ documentation for details on the configuration options that can be sent from the EMM provider to Mattermost Mobile apps. 

.. important::
    
    Mattermost only supports the AppConfig standard for securing Mattermost Mobile apps via an EMM provider due to incompatibilities with app wrapping and React Native applications. React Native is the technology used to develop the Mattermost Mobile apps. Different EMM vendors refer to “wrapping” in different ways, but it ultimately comes down to unpacking the mobile client bundle, injecting additional SDKs, and re-packaging/re-signing. 

    Mattermost doesn’t support app wrapping, and Mattermost Mobile apps won't function properly when using app wrapping (e.g., Websockets for real-time messaging will break). Use app wrapping/containerization technology at your own risk.

Enroll Devices
--------------

When building your own custom versions or deploying the pre-built Mattermost Mobile apps, consider your organization’s mobile policy:

- Can users bring their own device (BYOD) If so, what devices will be used?
- Are devices company-owned and company-issued?
- Are both options supported?
- What operating systems do you want to start testing?

Once you know what possible device configurations you’ll be supporting, consider creating a sample configuration, then running validation tests against each configuration item.

Generate and Assign Device Profiles
-----------------------------------

Generate and assign a device profile for device-wide configurations through the EMM provider.