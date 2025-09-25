Deploy using an EMM provider
=============================

.. include:: ../../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

You can enhance mobile security by deploying the Mattermost mobile app with `Enterprise Mobility Management (EMM) <https://en.wikipedia.org/wiki/Enterprise_mobility_management>`__ and Mattermost AppConfig compatibility to secure mobile endpoints with management application configuration.

You can use an EMM to:

- Enforce users to download the Mattermost pre-built or custom apps managed by your organization.
- Set default server url address.
- Restrict users from changing servers.
- Enforce security policies.

An EMM provider pushes Mattermost Mobile apps to EMM-enrolled devices. This approach is recommended for organizations that typically use EMM solutions to deploy Mobile apps to meet security and compliance policies.

Manage app configuration using AppConfig
----------------------------------------

AppConfig is our recommended approach for app configuration and management. It was introduced by the `AppConfig Community <https://www.appconfig.org/>`__, a group of leading EMM providers and app developers who have come together to make it easier for developers and customers to drive mobility in business.

AppConfig provides an easy way to configure enterprise mobile apps with any EMM providers listed on the `AppConfig website <https://www.appconfig.org/>`__. Using AppConfig, you can manage default settings and security controls on public app stores and custom-built mobile clients. For example, you can pre-configure your Mattermost server URL and username.

Mattermost AppConfig values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows all the configuration options that can be sent from the EMM provider of your choice to the Mattermost mobile apps. You can also :download:`download an XML template </samples/mattermost-specfile.xml>` of the configuration file for use with your EMM provider. 

.. raw:: html

   <style>
     table.mattermost-plans {
       border-collapse: collapse;
       width: 100%;
       font-size: 0.95em;
     }
     table.mattermost-plans th, table.mattermost-plans td {
       border: 1px solid #888;
       padding: 6px 8px;
       vertical-align: top;
     }
     /* Dark mode border color */
     body:not([data-custom-theme="light"]) table.mattermost-plans th, 
     body:not([data-custom-theme="light"]) table.mattermost-plans td {
       border-color: #666;
     }
     table.mattermost-plans th {
       background: #f2f2f2;
       font-weight: bold;
       text-align: left;
     }
     /* Dark mode support for table headers */
     body:not([data-custom-theme="light"]) table.mattermost-plans th {
       background: #444;
       color: #fff;
     }
   </style>

   <table class="mattermost-plans">
     <thead>
       <tr>
         <th>Key</th>
         <th>Description</th>
         <th>Default/Valid Values</th>
         <th>iOS Support</th>
         <th>Android for Work Support</th>
       </tr>
     </thead>
     <tbody>
       <tr>
         <td><strong><code>inAppPinCode</code></strong><br><em>String</em></td>
         <td>Require users to authenticate as the device owner before using the app. Prompts for fingerprint or passcode when the app first opens and when the app has been in the background for more than five minutes.</td>
         <td>Default: <code>false</code><br>Valid: <code>true | false</code></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
       </tr>
       <tr>
         <td><strong><code>blurApplicationScreen</code></strong><br><em>String</em></td>
         <td>Blur the app when it's set to background to protect any confidential on-screen information. On Android, it also prevents taking screenshots of the app.</td>
         <td>Default: <code>false</code><br>Valid: <code>true | false</code></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
       </tr>
       <tr>
         <td><strong><code>jailbreakDetection</code></strong><br><em>String</em></td>
         <td>Disable app launch on jailbroken or rooted devices.</td>
         <td>Default: <code>false</code><br>Valid: <code>true | false</code></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
       </tr>
       <tr>
         <td><strong><code>copyAndPasteProtection</code></strong><br><em>String</em></td>
         <td>Disable the ability to copy from or paste into any text inputs in the app.</td>
         <td>Default: <code>false</code><br>Valid: <code>true | false</code></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
         <td><img src="../../_static/images/check-circle-green.svg"> (since v1.24.0)</td>
       </tr>
       <tr>
         <td><strong><code>serverUrl</code></strong><br><em>String</em></td>
         <td>Set a default Mattermost server URL. Supports a single server only while v2.0 of the mobile app supports multiple server connections.</td>
         <td>Valid: URL</td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
       </tr>
       <tr>
         <td><strong><code>serverName</code></strong><br><em>String</em></td>
         <td>Automatically populates the server display name for the URL specified in serverURL.</td>
         <td>Valid: alphanumeric or empty</td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
       </tr>
       <tr>
         <td><strong><code>allowOtherServers</code></strong><br><em>String</em></td>
         <td>Allow the user to change the above server URL. If set to <code>true</code>, users can connect to multiple servers that aren't specified in the server URL setting. If set to <code>false</code>, users can only connect to a single defined server.</td>
         <td>Default: <code>true</code><br>Valid: <code>true | false</code></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
       </tr>
       <tr>
         <td><strong><code>username</code></strong><br><em>String</em></td>
         <td>Set the username or email address to use to authenticate against the Mattermost Server.</td>
         <td></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
       </tr>
       <tr>
         <td><strong><code>useVPN</code></strong><br><em>String</em></td>
         <td>Enable connection to the Mattermost Server to use a per-app VPN or VPN on-demand.</td>
         <td>Default: <code>false</code><br>Valid: <code>true | false</code></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
         <td></td>
       </tr>
       <tr>
         <td><strong><code>timeoutVPN</code></strong><br><em>String</em></td>
         <td>Set how long the request waits (in milliseconds) for an initial VPN connection to establish before timeout.</td>
         <td>Default: 30000</td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
         <td></td>
       </tr>
       <tr>
         <td><strong><code>vendor</code></strong><br><em>String</em></td>
         <td>Name of the EMM vendor or company deploying the app. Used in help text when prompting for passcodes so users are aware why the app is being protected.</td>
         <td>Default: Mattermost</td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
       </tr>
       <tr>
         <td><strong><code>inAppSessionAuth</code></strong><br><em>String</em></td>
         <td>Use the app's internal browser for SSO instead of an external browser. From Mattermost v10.2 and mobile v2.2.1, deprecated in favor of the <a href="../../administration-guide/configuration-reference/site-configuration-settings.html#mobile-external-browser">mobile external browser</a> server configuration setting.</td>
         <td>Default: <code>false</code><br>Valid: <code>true | false</code></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
         <td><img src="../../_static/images/check-circle-green.svg"></td>
       </tr>
     </tbody>
   </table>

Other AppConfig settings
~~~~~~~~~~~~~~~~~~~~~~~~~

As part of AppConfig, EMM administrators can set the following additional configuration options for the Mattermost mobile apps:

1. **App Tunnel:** Leverage the "Per-app VPN" capabilities in most commercial VPN solutions.
2. **Prevent App Backup:** Prevent users from backing up app data.
3. **Enforce App Encryption:** Set security policies such as requiring encryption.
4. **Remotely Wipe App:** Use the EMM tool to distribute the app to devices as a managed application so it can be remotely wiped. If the app was previously installed, mark it so the EMM converts the app to a managed app.

Other configurations may be available depending on your EMM provider.

.. important::
    - Mattermost only supports the AppConfig standard for securing Mattermost mobile apps via an EMM provider due to incompatibilities with app wrapping and React Native applications. Different EMM vendors refer to “wrapping” in different ways, but it ultimately comes down to unpacking the mobile client bundle, injecting additional SDKs, and re-packaging/re-signing. React Native is the technology used to develop the Mattermost mobile apps.
    - Mattermost doesn’t support app wrapping, and Mattermost mobile apps won't function properly when using app wrapping (e.g., Websockets for real-time messaging will break). Use app wrapping/containerization technology at your own risk.
    - A Mattermost Enterprise subscription plan (or a legacy Enterprise Edition license) is required to request assistance or troubleshooting help from `Mattermost Customer Support <https://mattermost.com/support/>`__ when building and deploying custom mobile apps. Customers on other Mattermost subscription plans can develop and deploy custom mobile apps, but can't request technical support assistance through Mattermost Customer Support.
    - With the release of Mattermost mobile app v2.0, mobile app v1.55 becomes the official :doc:`extended support mobile release </product-overview/mattermost-mobile-releases>`, and will be supported for an extended timeframe.

Enroll devices
--------------

When building your own custom versions or deploying the pre-built Mattermost Mobile apps, consider your organization’s mobile policy:

- Can users bring their own device (BYOD) If so, what devices will be used?
- Are devices company-owned and company-issued?
- Are both options supported?
- What operating systems do you want to start testing?

Once you know what possible device configurations you’ll be supporting, consider creating a sample configuration, then running validation tests against each configuration item.

Generate and assign device profiles
-----------------------------------

Generate and assign a device profile for device-wide configurations through the EMM provider.