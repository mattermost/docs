===========================
Mobile App Deployment Guide
===========================

################
About this guide
################

********
Audience
********

Leaders, Administrators, and/or Champions responsible for deploying Mattermost mobile apps in their organization.

    **Note:** Some features described in this guide are only available in Enterprise Edition E10 and/or E20.

*******************
Learning objectives
*******************

This guide provides foundational information necessary when developing a plan for a proof of concept and/or enterprise mobile deployment. 

By the end of this guide you will have an understanding of the high-level requirements for a successful Mattermost mobile deployment. 

This includes:

- Choosing how to obtain and distribute the Mattermost mobile applications
- Determining the ideal mobile deployment model for your organization
- Understanding the resource requirements when choosing to build your own Mattermost mobile apps

Technical implementation guides are included as links to keep the information in this guide concise.

.. _support:

*******
Support
*******

If at any point you need additional help, please reach out using the methods below.

**Community**
    Our entire team is active within the `public instance of Mattermost <https://community.mattermost.com>`_, plus you will have the support of one of the best open source communities around.
**Documentation**
    We link to a lot of `mobile-specific documentation <https://docs.mattermost.com/mobile/mobile-overview.html>`_ within this guide, but we encourage you to check `all of our documentation <https://docs.mattermost.com/>`_.
**Forums**
    For more troubleshooting help, `open a new topic in our forums <https://forum.mattermost.org/c/trouble-shoot>`_ with steps to reproduce your issue.
**GitHub**
    Visit us on `GitHub <https://github.com/mattermost/>`_ to create issues in any of our repositories.
**Enterprise Support**
    If you are an Enterprise Edition subscriber, you may open a support ticket in the `Enterprise Edition Support portal <https://support.mattermost.com>`_.

----

################################
Before you begin your deployment
################################

A successful mobile deployment is an important part of your experience with Mattermost.

Our highest priority is making sure you have what you need to be successful, but keep in mind that any change, even beneficial, will have an impact on your users. To ensure your success you need to identify the goals for your mobile deployment.

For example, you can deploy to thousands of users across the world in minutes with the publicly available Mattermost mobile apps on Google Play and Apple App Store.

Of course, large enterprise deployments will take more time, and the overall goals for your deployment will depend on many factors. We recommend taking a moment to write down what a successful deployment looks like. To start, ask yourself and your team what you want to achieve, what are your desired outcomes?

This takes a small amount of time upfront. But, we have seen the difference this makes in successful projects.

Below, we have added some key questions to ask yourself, your team, and any other stakeholders.

- Why have we decided to deploy the Mattermost mobile application?
- Who will, or should, play a key/critical role in this project?
- Who does this project impact?
- How much time do we have for this deployment?
- Should, or could, an initial deployment take a simpler path?
- Can we stagger our deployment, starting with simple requirements first?
- Are you going to run a pilot deployment, if so, with whom?
- What IT or HR policies need to change?

We recommend setting at least one achievable and time-based outcome.

At the same time, you should begin thinking about technical and security requirements. A great place to start is with an implementation plan. So, feel free to `use our template available <https://docs.mattermost.com/getting-started/implementation_plan.html>`_ in the Mattermost documentation. Also, begin by engaging with your technical and security teams with questions like those below.

- Are there any known security or access requirements?
- Is a VPN connection required?
- Do we use an Enterprise Mobile Management (EMM) Provider?

Again, this means pausing before you jump into your Mattermost mobile deployment. But it will make all the difference in ensuring you see a return on your investment.

----

###################################
Mattermost mobile deployment primer
###################################

While Mattermost provides options to make mobile deployment as easy as possible, it will take time and iteration.

This primer serves as an introduction to Mattermost mobile technologies. It is a complement to our technical documentation, and focuses on three main areas:

- Technical Requirements
- Basic Features and Technologies
- Troubleshooting

Regardless of your expertise, we recommend reading this section before starting your deployment. And keep in mind, we are here to support_ you.

**********************
Technical requirements
**********************

`Supported Mattermost Server Versions <https://github.com/mattermost/mattermost-mobile/blob/master/CHANGELOG.md>`_ 
    Minimum requirements for the Mattermost Server are maintained in our documentation (link above). 
    **However, we do recommend running the latest version** of the Mattermost Server as it contains the most recent features and any applicable security updates.

    If this is not possible, we encourage you to be on the most recent `Extended Support Release version <https://docs.mattermost.com/administration/extended-support-release.html>`_ of the Mattermost Server. This release has a number of critical feature updates that will ensure compatibility in a number of areas, including the Mattermost Push Notification Service (MPNS).

`Supported Devices/Mobile Device Requirements <https://docs.mattermost.com/install/requirements.html#mobile-apps>`_
    Basic mobile device requirements are provided in the link above.

*******************************************
Public app store vs. custom Mattermost apps
*******************************************

    **Note:** This guide uses the term Public App Store as generic for the two most commonly-used application stores: Apple App Store and Google Play Store.

The most critical decision you will make in your mobile deployment is whether to use the apps provided by Mattermost via Google Play and Apple App Store, or to build and distribute custom versions of the Mattermost apps. Below we provide a very general overview of these options.

Public app store
================

Utilizing the app distributed by Mattermost in Google Play and the Apple App Store greatly reduces the deployment time and is our recommended approach. Key benefits include:

- Easier deployment, driven by user needs.
- Ability to use the Hosted Push Notification Service, or HPNS.
- Apps automatically updated with the latest features, enhancements, and security updates.

Custom Mattermost apps
======================

If you desire to customize the applications, or do not want your users downloading the application from the public app stores, you will need to build the apps yourself. 

As the apps are an open source project, customization will require a fork, and your team will be responsible for maintaining the fork, as well as keeping the fork up to date with any changes made by Mattermost.

This process can be complicated. It will also greatly increase deployment time, not only initially, but whenever the apps need to be updated. 

We recommend having your development team take a look at the documentation to ensure they understand the scale and requirements of this path. In general, this route will present some challenges, including:

- Obtaining/providing certificates for your custom Mattermost application
- Signing your custom Mattermost applications
- Distributing your applications via public or private app stores

*******************************************
Mattermost Push Notification Service (MPNS)
*******************************************

Receiving notifications on a mobile device is a core value of any mobile deployment.

It also represents a return on your deployment investment through better-connected users. 

A push proxy is a key technology behind notification transmission. It enables notifications between the server and the mobile application.

Mattermost provides a self-hosted Push Proxy you can deploy, the Mattermost Push Notification Service (MPNS). This is also available via a hosted-by-Mattermost option, or Hosted Push Notification Service (HPNS).

    **Note:** `Only Mattermost Enterprise Edition E10 <https://mattermost.com/pricing-self-managed/>`_ or higher can be used to receive access to our Hosted Push Notification Service (HPNS)

If you will be using the Mattermost applications via Google Play and Apple App Store, the HPNS is all you need.

Our Hosted Push Notification Service offers:

- Access to a publicly-hosted Hosted Push Notification Service (HPNS).
- An explicit `privacy policy <https://mattermost.com/data-processing-addendum/>`_ for the contents of unencrypted messages.
- Encrypted TLS connections:
    - Between HPNS and Apple Push Notification Services
    - HPNS and Google’s Firebase Cloud Messaging service
    - HPNS and your Mattermost server
- Production-level uptime expectations
- Compatibility with EMM Providers*

\* *When using our publicly-available app store applications and the AppConfig standard.*

Hosting your own version of the MPNS is an option, but requires you to build the Mattermost app yourself. The `Choosing the Right Mobile Deployment Model`_ section of this guide, as well as our `Mobile App Admin Documentation <https://docs.mattermost.com/mobile/mobile-hpns.html>`_ are the best places to start.

********************************************
Enterprise Mobile Management (EMM) Providers
********************************************

EMM Providers develop software that helps enterprise teams manage secure mobile technology deployments. This includes the use of mobile devices and usage-ready applications.

Most large enterprise teams are familiar with `Enterprise Mobile Management <https://en.wikipedia.org/wiki/Enterprise_mobility_management>`_ providers, or EMMs. If this is a new term for you, review `Appendix B: EMM Provider List`_ for a list of providers and relevant information.

For those taking on larger deployments, we assume you are already using an EMM provider.

AppConfig is newer, more modern approach when compared to the previous standard, app wrapping.

AppConfig (supported) vs. app wrapping (not supported)
======================================================

    **Note:** Mattermost only supports the AppConfig standard. It does not support app wrapping. Use app wrapping at your own risk.

Here is `a helpful article  <https://www.computerworld.com/article/3209907/app-wrapping-the-key-to-more-secure-mobile-app-management.html>`_ defining AppConfig and app wrapping. Let us take a look at AppConfig first.

AppConfig
---------

"A community focused on providing tools and best practices around native capabilities in mobile operating systems to enable a more consistent, open and simple way to configure and secure mobile apps in order to increase mobile adoption in business." - AppConfig.org

So that sounds great, but are there any benefits for users?

Again, in the AppConfig Community’s words, "Users benefit with instant mobile productivity and a seamless out-of-the box experience, and businesses benefit with secure work-ready apps with minimal setup required while leveraging existing investments in Enterprise Mobility Management (EMM), VPN, and identity solutions. Put another way, your apps are simpler to configure, secure and deploy."

For now, focus on that last part, "... your apps are simpler to configure, secure and deploy." AppConfig provides the most efficient and scalable path for success. As an admin this means easier deployment and management of mobile applications. And again, when it comes to Mattermost, it is our only supported approach.

Application (App) Wrapping
--------------------------
From the article we `referenced earlier <https://www.computerworld.com/article/3209907/app-wrapping-the-key-to-more-secure-mobile-app-management.html>`_, application (app) wrapping involves "...the use of an SDK from an EMM vendor that allows a developer or admin to deploy an API that enables management policies to be set up." 

When going this route, there are two options:

**Option 1**
    The EMM provider gives you their libraries, and then you go to the source code for the app. Using the libraries you "wrap" the source and repackage the application. This approach will take significant development time and associated frustration. In the end you should have an app that is now wrapped with the EMM libraries. The hope, but not the guarantee, is that you have an app with an additional layer. This allows you to manage and secure the app on a user’s mobile device.

**Option 2**
    The EMM provider gives you a tool used for wrapping the app. In more modern cases, it’s a simple checkbox in your EMM application when configuring the app. These tools then inject all the needed code to wrap it. Then the tool (or EMM provider) builds it back up. This allows you to distribute the new, wrapped app. The wrapped app has a layer allowing you to manage and secure the app on a user’s mobile device. 

Until recently app wrapping has been the common approach. It does not come without risks and challenges to scalability though. 

For example, most modern applications follow continuous development. Each time an application changes it will need to go through the process described above. 

There is also functionality and compatibility risk. This is a known issue for the Mattermost application and app wrapping tools.

This incompatibility is not an issue with the Mattermost application. It results from the proprietary nature of the provider's tools. To make matters worse, there is no course of action to address compatibility issues.

In the end, this sets app wrapping in a negative light. This is the reason the `AppConfig Community <https://www.appconfig.org>`_ came together to create a standard. AppConfig is a modern, efficient, and scalable approach to enterprise mobile management. In that regard, the Mattermost application benefits from being built around this standard.

******************
Mobile VPN options
******************

A Virtual Private Network (VPN) allows a device outside a firewall to access content inside the firewall as if it were on the same network. Most enterprise teams are familiar with VPNs. We will not go into detail here.

There are VPN options which depend on the requirements of your organization. You should also consider the demands/needs of your users. Regardless, this can impact your approach to mobile deployment.

For the Mattermost mobile application, we will discuss two options: a device VPN or per-app VPN.

    **Note:** We suggest `following our recommended steps <https://docs.mattermost.com/mobile/mobile-appstore-install.html>`_ to secure your deployment.

**Device VPN**
    This is not as common, especially in the case of Bring Your Own Device (BYOD) scenarios. In this option, all internet traffic routes through the VPN specified in the profile. This could cause issues for personal applications.

**Per-app VPN**
    In contrast, the more common approach is to use a per-app VPN. This provides a connection to the VPN when needed (on-demand). For example, when using a particular app.

Regardless of the commonness of either option above, Mattermost provides support for both. Because Mattermost supports the AppConfig standard, both options are compatible with EMM providers.

    **Note:** Will you be connecting via a corporate proxy server? If so, `review our FAQ <https://docs.mattermost.com/mobile/mobile-faq.html#how-do-i-receive-mobile-push-notification-if-my-it-policy-requires-the-use-of-a-corporate-proxy-server>`_ covering architecture, troubleshooting, and best practices.

----

##########################################
Choosing the right mobile deployment model
##########################################

At this point you should have read through the deployment primer. It provides a large amount of context for the principles and best practices that follow. This next section aims to help you choose one of two recommended deployment models.

*****************************************
Using the public app stores (recommended)
*****************************************

**Desired Outcomes:**

- Quick rollout of the Mattermost mobile application
- Allow users to install the application on their device
- Ensure a high level of security and controlled access
- Use existing, internal processes and tools

We recommend either of these options if you are:

- Testing out the mobile applications
- Deploying Team Edition servers using no push notifications, or push notifications from Mattermost’s `TPNS <https://docs.mattermost.com/overview/faq.html#tpns>`_ (Test Push Notification Service)
- Deploying Enterprise Edition servers using push notifications from Mattermost’s `HPNS <https://docs.mattermost.com/mobile/mobile-hpns.html>`_ (Hosted Push Notification Service)

The mobile applications provided by Mattermost work with our hosted version of the Mattermost Push Notification Service (MPNS). This represents the easier path. The Mattermost mobile applications can be deployed with or without an EMM provider. These options are explained in more detail below. 

    **Note:** HPNS is compatible with EMM providers.

**Option 1** - Public App Store Installation (Easiest)

- Users download application via Apple App Store or Google Play
- Users enter URL to your hosted Mattermost Server

*Advantages:* Very easy, mobile deployment can be done by each individual user

*Disadvantages:* No additional EMM security features

**Option 2** - Public App Store Installation with EMM Provider (Easy)

- The EMM provider pushes the Mattermost app to the EMM enrolled devices
- Extend your organization’s security best practices/requirements via your EMM provider

*Advantages:* Easy, mobile deployment happens automatically to enrolled devices, app security and configuration can be maintained via your EMM provider

*Disadvantages:* No app customization

*********************************************
Distributing custom builds of the mobile apps
*********************************************

**Desired Outcomes**:

- Maintain full control over the distribution of applications
- Change the look, feel, and capabilities of the Mattermost mobile application
- Deploy your own MPNS to meet specific organizational requirements

This model is more difficult, and is recommended for organizations that can't (or don't desire) to use the HPNS. Often security and access requirements determine this, not the size of your organization.

Both Google and Apple require signatures of the application and push proxy to match. This means if you build the applications, you must host your own instance of MPNS.

Building the apps can be an involved process. This requires that you have the skillset to maintain and deploy packaged apps. Part of this process includes, but is not limited to:

- Obtaining/providing certificates for your custom Mattermost application
- Signing your custom Mattermost applications
- Distributing your applications via public or private app stores

Keeping your custom built apps up to date with features and security updates will be your responsibility.

To understand what’s involved, have your development team `read through our documentation <https://developers.mattermost.com/contribute/mobile/build-your-own/>`_.

    **Note:** As of Mattermost 5.18, E20 customers can limit data sent to the HPNS. With this option a message containing only an ID is transmitted. Once the mobile client receives this ID, the message contents are loaded from the server. Thus, the message contents are never transmitted through APNS/FCM.

----

#####################################################
Mobile deployment via public app stores (recommended)
#####################################################

To proceed you must have a Mattermost Server installed and accessible. This is also true for using the hosted version of the Mattermost push proxy (HPNS).

*********************************
Accessing the mobile applications
*********************************

The Mattermost mobile application is available for both Android and iOS devices. At this point, it is as simple as having your users download the application and `point to your Mattermost Server URL <https://docs.mattermost.com/help/getting-started/signing-in.html#ios-setup>`_.

    **Note:** The Mattermost mobile apps are signed and have certificates associated with Mattermost and the public app stores. This means they will not work if you are privately hosting the Mattermost Push Proxy Service.

`Mattermost for Android Devices <https://play.google.com/store/apps/details?id=com.mattermost.rn&hl=en_US>`_ (via Google Play)
`Mattermost of iOS Devices <https://apps.apple.com/us/app/mattermost/id1257222717>`_ (via Apple App Store)

If you do not desire (or require) additional security provided via an EMM Provider, your deployment is complete. Feel free to point your users to the `available documentation <https://docs.mattermost.com/guides/user.html>`_.

The sub-sections below serve as a high-level guide to understanding this deployment model. When necessary, we point to the documentation for technical instruction.

    **Note:** At a minimum, we recommend you follow our recommended steps to secure your deployment.

********************************************
Using an EMM Provider with public store apps
********************************************

EMM providers help extend security parameters to the Mattermost mobile applications. The AppConfig standard makes this possible. `Review the Mattermost AppConfig Values Documentation <https://docs.mattermost.com/mobile/mobile-appconfig.html#mattermost-appconfig-values>`_ for a complete list of available parameters.  

When going this route, you should consider:

- What is the mobile policy, is it company-owned, BYOD or both?
- Do you know what devices will be used if BYOD?
- What OS do you want to start with in testing?
- Creating a sample configuration then run validation tests against each config item

**********************************
Configuring Mattermost to use HPNS
**********************************

Configuring your Mattermost Server to use the Mattermost HPNS is a single configuration item. This is covered in our `Hosted Push Notification Service documentation <https://docs.mattermost.com/mobile/mobile-hpns.html>`_. 

Next your users would need to install the mobile application on their device. If desired, you can further configure security capabilities using an EMM provider.

**********************************
Updating via the public store apps
**********************************

While not part of your initial mobile deployment, you should consider a strategy for updating when new versions of the Mattermost mobile applications are available. Simultaneously, you should check any compatibility requirements for the mobile apps and the Mattermost Server. 

For example we recommend you:

- Check the compatibility requirements
- Validate versions connecting to server
- Update server
- Update apps

It is often easier to upgrade the mobile apps. However, not all provided updates are compatible with all previous versions of the Mattermost server.

Consult the `Mattermost mobile app changelog <https://github.com/mattermost/mattermost-mobile/blob/master/CHANGELOG.md>`_ and `Mattermsot server changelog <https://docs.mattermost.com/administration/changelog.html>`_ for more information.

    **Note:** Only updating the mobile apps, or updating the mobile apps before the Mattermost server, can result in incompatibility.

----

###################################
Mobile deployment via custom builds
###################################

Choosing this model means you have decided not to use the mobile applications Mattermost has made available via the public app stores. 

This also means you will need to maintain these applications. Maintenance includes rebuilding and incorporating feature and/or security updates. Otherwise, your applications will not match the functionality of our publicly available applications, and could be incompatible with future versions of the Mattermost Server.

Finally, this choice also means you cannot use the hosted version of the Mattermost Push Notification Service (MPNS).

A first step for this deployment model is `reviewing the documentation <https://developers.mattermost.com/contribute/mobile/>`_. Your development team should run through the requirements for building the applications. This documentation provides guidance on building, compiling, and signing. It also includes information for customizing the apps.

We’ve provided some recommended sections below.

- Developer Setup
- Build Your Own App
- Push Notifications

*********************************
Distribution through an app store
*********************************

Once you have built your own apps you will need to distribute them. There are two options:

Option 1 - Enterprise App Store via EMM Provider (most common and recommended): 

- This is the most common way for customers to distribute their apps
- Once added to your own Enterprise App Store, users can download from the EMM catalog, or you can use the EMM provider to push the application to the user's device

Option 2 - Apple App Store and Google Play (less common):

- To submit an app to the official app stores, you need to submit the app to Apple/Google for review
- This is the same process Mattermost uses make the apps available for everyone
- This process is more common if you are looking to white label the app to remove Mattermost branding

******************************************************
Using an EMM Provider with your custom Mattermost apps
******************************************************

If you will be using an EMM provider, note that Mattermost does not support app wrapping. Instead we use the AppConfig standard.

In some instances, there is an incompatibility with app wrapping and React Native applications. React Native is the technology used to develop the Mattermost mobile applications. The Mattermost mobile app will not function properly when using app wrapping. In fact, a majority of the app wrappers EMMs provide do not support WebSocket connections.

App wrapping is still often an option during the EMM configuration. Again, AppConfig is the only supported method for securing Mattermost mobile applications via an EMM provider.

AppConfig options will vary by EMM Provider and the associated device. You can review the available options in our `AppConfig Values documentation <https://docs.mattermost.com/mobile/mobile-appconfig.html#mattermost-appconfig-values>`_.

    **Note:** In Appendix B we have provided a list of popular EMM providers as well as example documentation where available.

As part of configuring your EMM solution, you should consider:

- What is the mobile policy, is it company-owned, BYOD or both?
- Do you know what devices will be used if BYOD?
- What OS do you want to start with in testing?
- Creating a sample configuration then run validation tests against each config item

****************************************************
Configuring the MPNS for your custom Mattermost apps
****************************************************

Building and distributing the Mattermost mobile apps requires you to deploy an instance of the MPNS.

As part of the process of building the applications you will need to sign the applications. You must also obtain the appropriate certificate for both Android and iOS. If this is not done, the applications will not be able to interact with your instance of the MPNS.

Once that is complete you can proceed with deployment of your MPNS instance.

The documentation topics listed below guide installation and configuration for your MPNS.

- `Push Notification Service Installation <https://developers.mattermost.com/contribute/mobile/push-notifications/service/>`_
- `Admin Configuration for Push Notifications <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_
- `Additional FAQs <https://docs.mattermost.com/mobile/mobile-faq.html#>`_

************************************
Updating your custom Mattermost apps
************************************

While not part of your initial mobile deployment, you should consider a strategy for updating when new versions of the Mattermost mobile applications are available. We highly recommend you update your custom Mattermost apps for any security or service releases. At the same time, if you have updated the apps, prior to distribution, check any compatibility requirements for the mobile apps and the Mattermost Server. 

    **Note:** Only updating the mobile apps, or updating the mobile apps before the Mattermost server, can result in incompatibility.

----

####################################
Appendix A: Troubleshooting and FAQs
####################################

We highly recommend you check out our `Mobile FAQ <https://docs.mattermost.com/mobile/mobile-faq.html>`_ and `Mobile Troubleshooting documentation <https://docs.mattermost.com/mobile/mobile-troubleshoot.html>`_. The most common questions we've received have been answered there. However, it’s important to call out a few common items customers run into.

*******************************
Data Security on Mobile Devices
*******************************

- `How is data handled on a device after an account is deleted? <https://docs.mattermost.com/mobile/mobile-faq.html#how-is-data-handled-on-mobile-devices-after-a-user-account-is-deactivated>`_
- `What post metadata is sent in mobile push notifications? <https://docs.mattermost.com/mobile/mobile-faq.html#what-post-metadata-is-sent-in-mobile-push-notifications>`_
- `What are my options for securing the mobile apps? <https://docs.mattermost.com/mobile/mobile-faq.html#what-are-my-options-for-securing-the-mobile-apps>`_
- `What are my options for securing push notifications? <https://docs.mattermost.com/mobile/mobile-faq.html#what-are-my-options-for-securing-push-notifications>`_

***********************
Corporate Proxy Servers
***********************

`How do I receive mobile push notifications if my IT policy requires the use of a corporate proxy server? <https://docs.mattermost.com/mobile/mobile-faq.html#how-do-i-receive-mobile-push-notification-if-my-it-policy-requires-the-use-of-a-corporate-proxy-server>`_

- `Deploy Mattermost with connection restricted post-proxy relay in DMZ or a trusted cloud environment <https://docs.mattermost.com/mobile/mobile-faq.html#deploy-mattermost-with-connection-restricted-post-proxy-relay-in-dmz-or-a-trusted-cloud-environment>`_
- `Whitelist Mattermost push notification proxy to bypass your corporate proxy server <https://docs.mattermost.com/mobile/mobile-faq.html#whitelist-mattermost-push-notification-proxy-to-bypass-your-corporate-proxy-server>`_
- `Run App Store versions of the Mattermost mobile apps <https://docs.mattermost.com/mobile/mobile-faq.html#run-app-store-versions-of-the-mattermost-mobile-apps>`_

----

#############################
Appendix B: EMM Provider List
#############################

We’ve compiled a list of the most popular EMM providers and the associated Unified Endpoint Management tools they employ. In two cases (Blackberry Dynamics and MobileIron) we’ve also provided corresponding documentation developed by the Mattermost team.

************************************
Blackberry Dynamics (Blackberry UEM)
************************************

"BlackBerry UEM is a multiplatform EMM solution that provides comprehensive device, app, and content management with integrated security and connectivity, and helps you manage iOS, macOS, Android, Windows 10, and BlackBerry 10 devices for your organization. BlackBerry UEM is included in the `BlackBerry Secure UEM & Productivity Suites <https://www.blackberry.com/us/en/products/blackberry-secure-uem-suites.html>`_ - Choice Suite, Freedom Suite, and Limitless Suite."

- `BlackBerry Website <https://www.blackberry.com/us/en/products/blackberry-uem>`_
- `BlackBerry Mattermost Documentation <https://docs.mattermost.com/mobile/mobile-blackberry.html>`_
- `Blackberry Documentation and Help Materials <https://docs.blackberry.com/en/endpoint-management/blackberry-uem/12_11>`_

**********
MobileIron
**********

"MobileIron Unified Endpoint Management (UEM) provides the foundation for the industry’s first mobile-centric, zero trust enterprise security framework. Unlike other UEM solutions, MobileIron UEM puts enterprise mobile security at the center of your enterprise and allows you to build upon it with enabling technologies such as `zero sign-on (ZSO) <https://www.mobileiron.com/en/products/access>`_ user and device authentication, multi-factor authentication (MFA), and `mobile threat detection (MTD) <https://www.mobileiron.com/en/products/mobile-threat-defense>`_."

- `MobileIron Website <https://www.mobileiron.com/en/products/uem>`_
- `MobileIron Mattermost Documentation <https://docs.mattermost.com/mobile/mobile-mobileiron.html>`_ 
- `MobileIron Support (requires login) <https://help.mobileiron.com/s/login/?startURL=%2Fs%2F&ec=302>`_

****
Fyde
****

"Securely access Mattermost’s messaging platform to enable productive team collaboration. Our connectionless, modern alternative to VPN helps mitigate breach risk by securing private cloud network from direct access by unmanaged devices."

- `Fyde for Mattermost Use Case <https://www.fyde.com/use-cases/fyde-for-mattermost>`_
- `Fyde Documentation <https://fyde.github.io/docs/>`_

****************************************
Workspace One (formerly VMware AirWatch)
****************************************

"Empower employees with a personalized “any app, any device” experience and engage them from Day One with a virtual assistant that speeds common tasks. With modern management and Zero Trust security, along with data-driven insights and automation, IT can unify siloed teams, protect corporate apps and data, and confidently provide the engaging experiences that modern workforces demand."

- `Workspace One Website <https://www.air-watch.com/why-workspace-one-airwatch/>`_
- `Workspace One Help Portal <https://my.workspaceone.com/>`_

***********************************************
Citrix Endpoint Management (formerly XenMobile)
***********************************************

"If you're still relying on multiple platforms to oversee endpoints, it's time for a change. Now more than ever, IT needs a way to manage and monitor mobile, traditional and IoT endpoints without having to consult dozens of different dashboards and reports. With the majority of employees working away from desks 50-60% of the time,1 the devices and apps they access are as varied as the tools available to manage them. As the diversity of end user options reaches an all-time high—`BYOD <https://www.citrix.com/digital-workspace/byod.html>`_, `Office 365 <https://www.citrix.com/digital-workspace/optimize-microsoft-ems-intune.html>`_ and frequent `Windows 10 updates <https://www.citrix.com/digital-workspace/windows-10.html>`_ all play a role—you need a consolidated console. Get a single view of multidevice users with UEM to unify device configurations, data protection and usage policies… all in one central location."

`Citrix Endpoint Website <https://www.citrix.com/products/citrix-endpoint-management/>`_
`Citrix Endpoint Management Documentation <https://docs.citrix.com/en-us/citrix-endpoint-management.html>`_

****************
Microsoft InTune
****************

"Microsoft Intune is a cloud-based service that focuses on mobile device management (MDM) and mobile application management (MAM). Intune is included in Microsoft's `Enterprise Mobility + Security (EMS) suite <https://www.microsoft.com/microsoft-365/enterprise-mobility-security>`_, and enables users to be productive while keeping your organization data protected. It integrates with other services, including Microsoft 365 and Azure Active Directory (Azure AD) to control who has access, and what they have access to, and Azure Information Protection for data protection. When you use it with Microsoft 365, you can enable your workforce to be productive on all their devices, while keeping your organization's information protected."

- `InTune Website <https://docs.microsoft.com/en-us/intune/fundamentals/what-is-intune>`_
- `Microsoft InTune Documentation <https://docs.microsoft.com/en-us/intune-user-help/use-managed-devices-to-get-work-done>`_
