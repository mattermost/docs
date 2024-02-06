Deployment overview
===================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

The following Mattermost network diagram illustrates a private cloud deployment of Mattermost with optional configurations for scaling to performance from teams to large organizations.

.. image:: ../images/network_diagram.png
   :alt: Mattermost network diagram shows how the components of a private cloud deployment could be deployed. Includes optional configurations for scaling for larger enterprise organizations.

.. note::

  GitLab Mattermost deployment is `documented separately <https://docs.gitlab.com/omnibus/gitlab-mattermost/>`__ and not included below.

Requirements and installation guides
-------------------------------------

Mattermost supports workplace messaging for teams using one to three servers with instructions available in the Install Guides section of this documentation. See the `Software and Hardware Requirements </install/software-hardware-requirements.html>`__ documentation for server sizing estimates.

User experience
----------------

PC web experience
^^^^^^^^^^^^^^^^^

End users can securely share messages and files using a web-based Mattermost experience in Chrome, Firefox, Safari, and Edge. Please see `Software and Hardware Requirements </install/software-hardware-requirements.html>`__ documentation for full details.

Mobile App experience
^^^^^^^^^^^^^^^^^^^^^^

Native applications for iOS and Android are available for interacting with the Mattermost server and receiving encrypted push notifications from your private cloud. Organizations can use `a Hosted Push Notification Service </deploy/mobile-hpns.html#hosted-push-notifications-service-hpns>`__ with encrypted communications to mobile apps on the App Store and Google Play, or deploy to an `Enterprise App Store </deploy/mobile-hpns.html#mobile-push-notifications>`__ on your organization's private network. A `Test Push Notification Service </deploy/mobile-hpns.html#hosted-push-notifications-service-hpns>`__ is available for use while evaluating options.

Mobile web experience
^^^^^^^^^^^^^^^^^^^^^

End users can securely share messages and files using a mobile web-based Mattermost experience on iOS and Android devices. Please see `Software and Hardware Requirements </install/software-hardware-requirements.html>`__ documentation for full details.

Email client
^^^^^^^^^^^^

Receive emails on desktop and mobile from the Mattermost server.

Communication protocols
-----------------------

HTTPS connection (secure hypertext transfer protocol)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The HTTPS connection to the Mattermost server renders pages and provides core functionality. It doesn't include real-time interactivity, which is enabled by the WSS connection.

If the HTTPS connection isn't available, the Mattermost service won't work. HTTPS is a secure, encrypted protocol and is highly recommended for production. An unencrypted HTTP connection may be used in initial testing and configuration but it is not recommended for production.

WSS connection (secure WebSocket protocol)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

WSS is a secure, encrypted connection and is highly recommended. An unencrypted WSS connection may be used in initial testing and configuration but it is not recommended for production.

The WSS connection to the Mattermost server enables real-time updates and notifications. If the WSS connection is not available, but HTTPS is available, the system will appear to work, but real-time updates and notifications will not work. Updates will only appear on a page refresh. WSS will be a persistent connection to the Mattermost server while you are connected, while HTTPS will be intermittent depending on when you load a page or a file.

Typically a "Mattermost unreachable" error message will be displayed warning users that the Mattermost server is either unreachable or the WebSocket connection is not properly configured.

Network access and multi-Factor authentication
----------------------------------------------

Behind a VPN
^^^^^^^^^^^^

Mattermost is intended to be installed within a private network which can offer multiple factors of authentication, including secure access to computing devices and physical locations.

If outside access is required, a virtual private network client (VPN), such as `OpenVPN <https://openvpn.net/>`__, with additional authentication used to connect to Mattermost for web, desktop, and mobile experiences, is recommended.

Non-VPN setup
^^^^^^^^^^^^^^^

If Mattermost is accessible from the open internet, the following is recommended:

1. An IT admin should be assigned to set up appropriate network security, subscribe to `the Mattermost security bulletin <https://mattermost.com/security-updates/#sign-up>`__, and `apply new security updates </upgrade/upgrading-mattermost-server.html>`__.
2. The organization enables `SAML Single Sign-on </onboard/sso-saml.html>`__ or enable `MFA </onboard/multi-factor-authentication.html>`__ using Google Authenticator.

If Mattermost is accessible from the open internet with no VPN or MFA set up, we recommended using it only for non-confidential, unimportant conversations where impact of a compromised system is not essential.

Data center infrastructure
---------------------------

Push notification service
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

The `Mattermost Push Notification Service (MPNS) </deploy/mobile-hpns.html#enable-mpns>`__ routes push notifications to:

1. Apple Push Notification Service to send notifications to the Mattermost iOS app.
2. Google Push Notification Service to send notifications to the Mattermost Android app.

If you're deploying mobile applications to an Enterprise App Store, your MPNS should be behind your firewall on your private network. If you're using mobile apps in the App Store and Google Play, you can relay notifications to mobile apps using the `Hosted Push Notification Service (HPNS) </deploy/mobile-hpns.html#hosted-push-notifications-service-hpns>`__.

HPNS does not connect to your mobile apps directly. It sends messages over an encrypted channel to Apple or Google which are relayed to the app users downloaded from the App Store or Google Play.

Proxy
^^^^^^

The proxy manages Secure Socket Layer (SSL) encryption and sets the policy on how network traffic will be routed to the Mattermost server.

Mattermost install guides include setup instructions for the NGNIX software proxy by default. For large scale deployments, a hardware proxy with dedicated devices for processing SSL encryption and decryption could potentially increase efficiencies.

In a High Availability configuration (Enterprise subscription plans only) the proxy would also balance network load across multiple Mattermost servers.

Microsoft Active Directory Single Sign-On 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

Mattermost Enterprise and Professional supports Microsoft Active Directory and LDAP Single Sign-on with secure transport over TLS or stunnel.

Private Cloud integrations
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost offers complete access to its Web Service APIs, along with incoming and outgoing webhooks, and slash command options for integrating with your self-managed systems.

`Visit our app directory <https://mattermost.com/marketplace/#privateApps>`__ for dozens of open source integrations to common tools like Jira, Jenkins, GitLab, Trac, Redmine, and SVN, along with interactive bot applications (Hubot, mattermost-bot), and other communication tools (Email, IRC, XMPP, Threema) that are freely available for use and customization.

Email service
^^^^^^^^^^^^^

For notifications and account verification, Mattermost connects to your existing email service over SMTP, including Microsoft Exchange, Amazon SES, SendGrid, and self-hosted email solutions.

Mattermost Server
-----------------

Mattermost Server installs as a single compiled binary file. All server settings are stored in a configuration file, ``config/config.json``, which can be updated directly or via the web-based System Console user interface.

RESTful JSON web service
^^^^^^^^^^^^^^^^^^^^^^^^

The entirety of the Mattermost server is accessible through a RESTful web service API. The API can be completely accessed by developers creating custom applications for Mattermost either directly or via Javascript and Golang drivers.

Authentication client
^^^^^^^^^^^^^^^^^^^^^

Authenticates users by email or username plus password.

Authentication provider
^^^^^^^^^^^^^^^^^^^^^^^^

Enables authentication of Mattermost server to other services with authentication client interface using OAuth2.

Notification service
^^^^^^^^^^^^^^^^^^^^

Sends notifications via SMTP email and mobile push notifications via Mattermost Push Notification Service.

Data management service
^^^^^^^^^^^^^^^^^^^^^^^

Connects to and manages supported databases.

High Availability
^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Also available in legacy Mattermost Enterprise Edition E20*

Large organizations needing sophisticated, large scale, High Availability configurations can set up a `highly available, horizontally scalable </scale/high-availability-cluster.html>`__ deployment. `Contact us  <https://mattermost.com/contact-us/>`__ for guidance on configuring and sizing Mattermost to support your specific needs.

Data stores
------------

Databases
^^^^^^^^^^

Mattermost uses a Postgres database to store and retrieve system data and to execute full text search. Solid State Drives (SSDs) can be used for faster read times to increase performance.

See `Database requirements </install/software-hardware-requirements.html#database-software>`__ for full details.

Multiple read replicas 
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Also available in legacy Mattermost Enterprise Edition E20*

For enterprise deployments, the Mattermost database can be configured with a master and multiple read replicas. The read replicas can be configured as a redundant backup to the active server, so that during hardware failures operation can be diverted to the read replica server without interrupting service. 

The safest configuration is to size the disk space on the read replica used for failover two to three times larger than storage available on master, so that if the master fails because it runs out of disk space it will fail over to a read replica with enough extra space to run smoothly until the master is corrected.

Search replicas
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Also available in legacy Mattermost Enterprise Edition E20*

You can configure one or more search replicas to isolate search queries. A search replica is similar to a read replica, but is used only for handling search queries.

Global deployments 
~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Also available in legacy Mattermost Enterprise Edition E20*

Enterprise customers with deployments spanning many time zones can `contact us <https://mattermost.com/contact-us/>`__ for advanced configurations to minimize latency by:

1. Storing static assets over a global CDN.
2. Deploying multiple Mattermost servers to host API communication closer to the location of end users.
3. Deploying multiple database read replicas closer to the location of end users.

File store
^^^^^^^^^^^

Images and files shared by users are stored and retrieved in one of three options.

1. For teams sharing only modest amounts of file data, local storage on the same physical machine as the Mattermost server may be sufficient.
2. For enterprises sharing very large amounts of data, a Network Attached Storage (NAS) server may be used, which can scale to petabytes if necessary.
3. Alternatively, for both ease-of-use and scale, a third option is to use Amazon's S3 file storage service.

Deployment options
-------------------

Mattermost Enterprise Edition customers can contact Mattermost, Inc. for advice on deployment options for their specific environments. The following section describes common deployment configurations.

Mobile devices with VPN clients (recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost can be deployed behind your company firewall on a private network with access from the outside via a Virtual Private Network (VPN). This means running a VPN client on the mobile devices and desktop computers that need to access Mattermost.

The `Mattermost Push Notification Service </deploy/deployment-overview.html#push-notification-service>`__ (MPNS) should be behind your firewall on your private network. MPNS does not connect with mobile apps directly, it forwards push notifications from the Mattermost server to a relay service for the App Store or Google Play, or to mobile apps within an Enterprise App Store.

Mobile devices without VPN clients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If Mattermost is available on the internet, we recommend using `SAML Single Sign-on </onboard/sso-saml.html>`__ or enable `MFA </onboard/multi-factor-authentication.html>`__ using Google Authenticator. 

The `Mattermost Push Notification Service </deploy/deployment-overview.html#push-notification-service>`__ (MPNS) should be behind your firewall inside your private network. MPNS does not connect with mobile apps directly, it forwards push notifications from the Mattermost server to a relay service for App Store or Google Play, or directly to mobile apps within an Enterprise App Store behind your firewall.

For support for certificate-based authentication for mobile devices, `contact us <https://mattermost.com/contact-us/>`__ for more information.

Mobile devices with an EMM provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost mobile applications can also be deployed via `EMM providers who support AppConfig </deploy/mobile-appconfig.html>`__. EMM solutions typically offer per-app VPN capabilities that can be used to connect to mobile apps behind a VPN.