=====================================
Security Overview
=====================================

Mattermost offers modern communication behind your firewall to keep your data safe, secure and private. 

Security in Mattermost software is continually reviewed by developers, IT administrators and security researchers accountable for deploying the software in their organizations. 

Multiple rounds of penetration testing and security analysis, in addition to internal reviews, have produced a long list of security improvements, in two forms: 

- **Security Updates**
   - Upgrades addressing newly discovered attacks confidentially disclosed to Mattermost, Inc. by the product community and security researchers
   
- **Security Features**
   - Optional features to enhance security on the Mattermost platform. 

To expand on each type: 

Security Updates 
------

Security updates address newly discovered attacks reported to Mattermost, Inc. by the security research community. Disclosures are made confidentially, under the Mattermost responsible disclosure policy, allowing for Mattermost, Inc. to provide security updates to the community prior to public disclosure.

For more information, please see:

- `Mattermost Security Updates Disclosures <http://about.mattermost.com/security-updates/>`_ 
   - A summary of security updates made based on past and on-going security analysis and penetration testing. 

- `Mattermost Responsible Disclosure Policy <https://www.mattermost.org/responsible-disclosure-policy/>`_ 
   - An overview of how security issues are confidentially reported to and address by Mattermost, Inc. 

Security Features 
------

Mattermost offers a host of features to help keep your private cloud communications secure. 

- Private Cloud Deployment with Secure Mobile Apps 
   - Mattermost can run entirely behind your firewall as a single Linux binary with MySQL or PostgreSQL
   - Mattermost mobile apps can be deployed to an `internal Enterprise App Store <https://docs.mattermost.com/deployment/push.html#enterprise-app-store-eas>`_ by using source code available for Mattermost mobile apps and push notification service. Optionally `VPN clients on PC and mobile devices <https://docs.mattermost.com/deployment/deployment.html#vpn-setup>`_ can be used outside your private network.
   - Optionally, Mattermost mobile apps can run without a VPN by opening standard ports on your Mattermost server, such as 80 or 443. In this configuration, you have the option of using compiled `iOS and Android applications in iTunes and Google Play provided by Mattermost, Inc. <https://docs.mattermost.com/deployment/push.html#hosted-push-notifications-service-hpns>`_ (E10, E20), as well as enabling `multi-factor authentication <https://docs.mattermost.com/administration/config-settings.html#enable-multi-factor-authentication-enterprise>`_ (E10, E20).
   - User sessions across web, PC and mobile can be `remotely revoked through account settings <https://docs.mattermost.com/help/settings/account-settings.html#view-and-logout-of-active-sessions>`_, or via the System Console by deactivating accounts. 

- Centralized Security and Administration 
   - Manage users, teams, access control and system settings in a web-based `System Console user interface <https://docs.mattermost.com/administration/config-settings.html>`_.

- Transmission Security 
   - Mattermost supports TLS encryption using AES-256 with 2048-bit RSA on all data transmissions across both LAN and internet. 
   - Connections to Active Directory/LDAP can be optionally secured with TLS or stunnel (E10).
   - Encryption-at-rest is available through hardware and software disk encryption solutions applied to the Mattermost database, which can reside on its own server within your infrastructure.  
   - Option to `exclude message contents from push notifications <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_ to comply with strict compliance policies, such as US HIPAA standards.
   
- Integrity & Audit Controls
   - By default, Mattermost stores a complete history of messages, including edits and deletes, along with all files uploaded. User interface actions for "deleting" messages, channels and private groups only remove the data from the user interface, the data is retained within your database. 
   - The `output and archives of server logs <https://docs.mattermost.com/administration/config-settings.html#file-log-directory>`_ can be saved to a directory of your choice. Mattermost server logs plus logs from your web proxy can provide an end-to-end history of system usage.
   - `Ad hoc compliance reports of messaging by user, date range, and keyword, including edited and deleted messages <https://docs.mattermost.com/administration/compliance.html>`_ are available (E20). To protect against unauthorized use, all ad hoc report requests are logged. 
   - Daily compliance reports compatible with 3rd compliance solutions such as `Global Relay <https://docs.mattermost.com/administration/compliance.html#global-relay-support>`_ are also available (E20). 

- Authentication Safeguards 
   - To protect against brute force attacks, you can set `rate limiting on APIs <https://docs.mattermost.com/administration/config-settings.html#id55>`_, varied by query frequency, memory store size, remote address and headers.    
   - Session length and session cache can be `configured according to your internal policies <https://docs.mattermost.com/administration/config-settings.html#id33>`_.
   - Remotely `revoke user sessions <https://docs.mattermost.com/help/settings/account-settings.html#view-and-logout-of-active-sessions>`_ across web, mobile devices and native desktop apps.
   - Mattermost supports integrated authentication with `Active Directory and LDAP <https://docs.mattermost.com/deployment/sso-ldap.html>`_ (E10) as well as `Active Directory Federation Services <https://docs.mattermost.com/deployment/sso-saml-adfs.html>`_ and `Okta <https://docs.mattermost.com/deployment/sso-saml-okta.html>`_ via SAML 2.0 (E20)
   - The ability to require `multi-factor authentication <https://docs.mattermost.com/deployment/auth.html>`_ is also available (E10) 

- Access Control Policy 
   - Limit communications to specific users, private groups, or team-wide public channels
   - Increase system security `by restricting email-based account creation to email addresses from a list of specific domains, <https://docs.mattermost.com/administration/config-settings.html#restrict-account-creation-to-specified-email-domains>`_ e.g. "corp.mattermost.com", "mattermost.org", etc." 
   - Choose whether to restrict or enable `cross-origin requests. <https://docs.mattermost.com/administration/config-settings.html#enable-cross-origin-requests-from>`_
   - If sharing of public links for account creation or sharing of files and images are enabled, links can be invalidated via the System Console by `regenerating salts <https://docs.mattermost.com/administration/config-settings.html#public-link-salt>`_. 
   - Optionally restrict `creation, renaming, archiving of channels, private groups and integrations to team admins, system admins or end users <https://docs.mattermost.com/administration/config-settings.html#policy-enterprise>`_ (E10)
   - Optionally restrict `sending team invites to team admins, system admins or end users <https://docs.mattermost.com/administration/config-settings.html#policy-enterprise>`_ (E10)
   - Optionally add `advanced passwords requirements <https://docs.mattermost.com/administration/config-settings.html#password-requirements-enterprise>`_ with minimum numbers of symbols, numbers, and lower and uppercase letters (E10).
   
Special notes on encryption requirements in highly regulated industries: 
^^^^^^^ 

- Mobile apps from iTunes or Google Play require special configuration for advanced transmission security
   - Any mobile app hosted in iTunes or Google Play using push notifications has a moment where the contents of push notifications is decrypted on Apple or Google servers in order to relay the notification to a mobile app. For highly regulated industries that do not allow any moment where confidential data may appear decrypted to a 3rd party, Mattermost offers the ability to prevent the contents from messages from being included in push notifications, by setting `push notification contents <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_ to ``generic``. 
   - Alternatively, you can deploy Mattermost mobile applications and a private push notification service to an `internal Enterprise App Store <https://docs.mattermost.com/deployment/push.html#enterprise-app-store-eas>`_  to avoid passing any information through Apple or Google servers.
   
- Disk encryption is recommended for meeting encryption-at-rest requirements 
   - The Mattermost database can be deployed on its own server and hard drive to make use of both software and hardware disk encryption solutions based on your data center standards. 
   - Encryption of Mattermost messages prior to storage is not available since such functionality would make search unusable.
 
HIPAA compliance 
^^^^^^^ 

- Deploying Mattermost as part of a HIPAA-compliant IT infrastructure requires a deployment team trained on `HIPAA-compliance requirements and standards <http://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/>`_, including administrative safeguards, physical safeguards, organizational requirements and other standards. 
- Technincal safeguards relevant to HIPAA-compliance deployments are described above (Access Control, Audit Controls, Integrity Controls, Transmission Security), please take special note of the deployment notes for "highly regulated industries".

