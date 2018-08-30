=====================================
Security Overview
=====================================

Security in Mattermost software is continually reviewed by developers, IT administrators and security researchers accountable for deploying the software in their organizations.

Multiple rounds of penetration testing and security analysis, in addition to internal reviews, have produced a long list of safeguards, processes, policies, and compliance features, please see: 

.. contents::
    :backlinks: top

To expand on each:

Security Features
------------------------------------

Mattermost offers a host of features to help keep your private cloud communications secure.

Private Cloud Deployment with Secure Mobile Apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - Mattermost can run entirely behind your firewall as a single Linux binary with MySQL or PostgreSQL
   - Mattermost mobile apps can be deployed to an `internal Enterprise App Store <https://docs.mattermost.com/deployment/push.html#enterprise-app-store-eas>`_ by using source code available for Mattermost mobile apps and push notification service. Optionally `VPN clients on PC and mobile devices <https://docs.mattermost.com/deployment/deployment.html#vpn-setup>`_ can be used outside your private network.
   - Optionally, Mattermost mobile apps can run without a VPN by opening standard ports on your Mattermost server, such as 80 or 443. In this configuration, you have the option of using compiled `iOS and Android applications in iTunes and Google Play provided by Mattermost, Inc. <https://docs.mattermost.com/deployment/push.html#hosted-push-notifications-service-hpns>`_ (E10, E20), as well as enabling `multi-factor authentication <https://docs.mattermost.com/administration/config-settings.html#enable-multi-factor-authentication-enterprise>`_ (E10, E20).
   - User sessions across web, PC and mobile can be `remotely revoked through account settings <https://docs.mattermost.com/help/settings/account-settings.html#view-and-logout-of-active-sessions>`_, or via the System Console by deactivating accounts.
   - Mattermost apps can be packaged into leading Enterprise Mobility Management solutions including AirWatch and Blackberry through `AppDome <https://www.appdome.com/>`_.

Centralized Security and Administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - Manage users, teams, access control and system settings in a web-based `System Console user interface <https://docs.mattermost.com/administration/config-settings.html>`_.

Transmission Security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - Mattermost supports TLS encryption using AES-256 with 2048-bit RSA on all data transmissions between Mattermost client applications and the Mattermost server across both LAN and internet.
   - Connections to Active Directory/LDAP can be optionally secured with TLS or stunnel (E10).
   - Encryption-at-rest is available for messages via hardware and software disk encryption solutions applied to the Mattermost database, which resides on its own server within your infrastructure. To enable end user search and compliance reporting of message histories, Mattermost does not offer encryption within the database.
   - Encryption-at-rest is available for files stored via hardware and software disk encryption solutions applied to the server used for local storage or storage via Minio.
   - Encryption-at-rest is available for files stored in Amazon's proprietary S3 system using server-side encryption with `Amazon S3-managed keys <https://docs.mattermost.com/administration/config-settings.html#enable-server-side-encryption-for-amazon-s3>`_ (E20) when users choose not to use open source options.
   - Option to `exclude message contents from push notifications <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_ to comply with strict compliance policies, such as US HIPAA standards.
   - Ability to exclude or include the `contents of messages in push notifications <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_ to avoid disclosure on locked mobile screens, and via relay servers from Apple and Google when sending notifications to iOS or Android mobile apps (relevant to compliance standards such as HIPAA)

Integrity & Audit Controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - By default, Mattermost stores a complete history of messages, including edits and deletes, along with all files uploaded. User interface actions for "deleting" messages and channels remove the data only from the user interface; the data is retained within your database. If your compliance guidelines require it, you can turn off users' ability to edit and delete their messages after they are posted.
   - Use an `antivirus plugin <https://github.com/mattermost/mattermost-plugin-antivirus>`_ to scan for viruses before uploading a file to Mattermost. Supports `ClamAV anti-virus software <https://www.clamav.net/>`_ across browser, Desktop App and Mobile Apps.
   - Custom `data retention policies on messages and file uploads <https://docs.mattermost.com/administration/data-retention.html>`_ is available (E20). A daily data deletion job can be scheduled that deletes messages from the database and user interface, and file uploads from local file storage or Amazon S3, which exceed the specified retention period. 
   - The `output and archives of server logs <https://docs.mattermost.com/administration/config-settings.html#file-log-directory>`_ can be saved to a directory of your choice. Mattermost server logs plus logs from your web proxy can provide an end-to-end history of system usage.
   - `Ad hoc compliance reports of messaging by user, date range, and keyword, including edited and deleted messages <https://docs.mattermost.com/administration/compliance.html>`_ are available (E20). To protect against unauthorized use, all ad hoc report requests are logged.
   - Daily compliance reports compatible with 3rd party compliance solutions such as `Global Relay and Actiance <https://docs.mattermost.com/administration/compliance-export.html>`_ are also available (E20).

Authentication Safeguards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - To protect against brute force attacks, you can set `rate limiting on APIs <https://docs.mattermost.com/administration/config-settings.html#id55>`_, varied by query frequency, memory store size, remote address and headers.
   - Session length, session cache and idle timeout can be `configured according to your internal policies <https://docs.mattermost.com/administration/config-settings.html#sessions>`_, automatically forcing a user to re-login after a specified period of time.
   - Remotely `revoke user sessions <https://docs.mattermost.com/help/settings/account-settings.html#view-and-logout-of-active-sessions>`_ across web, mobile devices and native desktop apps.
   - Remotely reset user passwords via the System Console or via the `command line <https://docs.mattermost.com/administration/command-line-tools.html#platform-user-password>`_.
   - Mattermost supports integrated authentication with `Active Directory and LDAP <https://docs.mattermost.com/deployment/sso-ldap.html>`_ (E10) as well as `SAML 2.0 SSO integration <https://docs.mattermost.com/deployment/sso-saml.html>`_ with providers including `Active Directory Federation Services <https://docs.mattermost.com/deployment/sso-saml-adfs.html>`_,  `Okta <https://docs.mattermost.com/deployment/sso-saml-okta.html>`_, among others (E20).
   - The ability to require `multi-factor authentication <https://docs.mattermost.com/deployment/auth.html>`_ is also available (E10).

Access Control Policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - Limit communications to specific users, private channels, or team-wide public channels
   - Increase system security `by restricting email-based account creation to email addresses from a list of specific domains, <https://docs.mattermost.com/administration/config-settings.html#restrict-account-creation-to-specified-email-domains>`_ e.g. "corp.mattermost.com", "mattermost.org", etc."
   - Choose whether to restrict or enable `cross-origin requests. <https://docs.mattermost.com/administration/config-settings.html#enable-cross-origin-requests-from>`_
   - If sharing of public links for account creation or sharing of files and images are enabled, links can be invalidated via the System Console by `regenerating salts <https://docs.mattermost.com/administration/config-settings.html#public-link-salt>`_.
   - Optionally add `advanced passwords requirements <https://docs.mattermost.com/administration/config-settings.html#password-requirements>`_ with minimum numbers of symbols, numbers, and lower and uppercase letters.
   - Optionally restrict `creation, renaming, archiving of channels, private channels and integrations to team admins, system admins or end users <https://docs.mattermost.com/administration/config-settings.html#policy-enterprise>`_ (E10)
   - Optionally restrict `sending team invites to team admins, system admins or end users <https://docs.mattermost.com/administration/config-settings.html#policy-enterprise>`_ (E10)

Security Updates
------------------------------------

Security updates address newly discovered attacks reported to Mattermost, Inc. by the security research community. Disclosures are made confidentially, under the Mattermost responsible disclosure policy, allowing for Mattermost, Inc. to provide security updates to the community prior to public disclosure.

For more information, please see:

- `Mattermost Security Updates Disclosures <http://about.mattermost.com/security-updates/>`_
   - A summary of security updates made based on past and on-going security analysis and penetration testing.

- `Mattermost Responsible Disclosure Policy <https://www.mattermost.org/responsible-disclosure-policy/>`_
   - An overview of how security issues are confidentially reported to and address by Mattermost, Inc.

Security Policies
------------------------------------

For information on internal security policies, development guidelines, business continuity plans and common security-related questions from enterprises, please see our `Security Policies <https://docs.mattermost.com/process/security.html>`_ documentation.

HIPAA compliance
------------------------------------

Deploying Mattermost as part of a HIPAA-compliant IT infrastructure requires a deployment team trained on `HIPAA-compliance requirements and standards <http://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/>`_.

- Mattermost offers HIPAA-relevant **Technical Safeguards** including:

     - `Integrity Controls <https://docs.mattermost.com/overview/security.html#integrity-audit-controls>`_
     - `Access Control <https://docs.mattermost.com/overview/security.html#access-control-policy>`_
     - `Transmission Security <https://docs.mattermost.com/overview/security.html#transmission-security>`_
     - `Audit Controls <https://docs.mattermost.com/overview/security.html#integrity-audit-controls>`_

- HIPAA-compliant deployments commonly consider the following:

     - Omitting the contents of messages from mobile push and email notifications:

        - If your `Push Notifications Contents <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_ option is set to ``Send full message snippet`` there is a chance Personal Health Information (PHI) contained in messages could be displayed on a user's locked phone as a notification. To avoid this, set the option to ``Send generic description with user and channel names`` or ``Send generic description with only sender name``.
        - Similarly, setting `Email Notifications Contents <https://docs.mattermost.com/administration/config-settings.html#email-notification-contents>`_ to ``Send generic description with only sender name`` will only send the team name and name of the person who sent the message, with no information about channel name or message contents included in email notifications.

- Beyond Technical Safeguards, HIPAA compliance deployments also require:

     - Administrative Safeguards
     - Physical Safeguards
     - Organizational requirements and other standards.

To learn more, please review `HIPAA requirements from the US Department of Health and Human Services <http://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/>`_.



FINRA compliance
------------------------------------

Mattermost Enterprise Edition E20 is designed to meet the `cybersecurity requirements of the United States Financial Industry Regulatory Authority (FINRA) <http://www.finra.org/industry/cybersecurity>`_ as part of a customer's existing operational systems, including technology governance, system change management, risk assessments, technical controls, incident response, vendor management, data loss prevention, and staff training.

FINRA reviews a firm’s ability to protect the confidentiality, integrity and availability of sensitive customer information. This includes reviewing each firm’s compliance with SEC regulations, including:

- Regulation `S-P (17 CFR §248.30) <https://www.ecfr.gov/cgi-bin/text-idx?SID=226b4b62d8bf25d29cc88df5039cddde&mc=true&node=se17.4.248_130&rgn=div8>`_, which requires firms to adopt written policies and procedures to protect customer information against cyber-attacks and other forms of unauthorized access

- Regulation `S-ID (17 CFR §248.201-202) <https://www.ecfr.gov/cgi-bin/text-idx?SID=5621786ec1a831400e4b64f3e92198bd&mc=true&node=pt17.4.248&rgn=div5#sp17.4.248.c>`_, which outlines a firm's duties regarding the detection, prevention, and mitigation of identity theft

- The `Securities Exchange Act of 1934 (17 CFR §240.17a-4(f)) <https://www.ecfr.gov/cgi-bin/text-idx?SID=b6b7a79d18d000a733725e88d333ddb5&mc=true&node=pt17.4.240&rgn=div5#se17.4.240_117a_64>`_, which requires firms to preserve electronically stored records in a non-rewriteable, non-erasable format

Mattermost supports FINRA compliance as part of a customer's integrated operations in the following ways: 

- **Continous archiving** - Configuration as a non-rewriteable, non-erasable system of record for all messages and files entered into the system. Moreover, automated compliance exports and integration support for Smarsh/Actiance and Global Relay provide 3rd party eDiscovery options.  
- **Secure deployment** - Deployment within private, public and on-premesis networks with existing FINRA-compliant safeguards and infrastructure to protect customer information from cyber attack.
- **Support for intrusion detection** - Ability to support multi-layered intrusion detection from authentication systems to application servers to database access, including configuration of proxy, application and database logging to deeply audit system interactions.  
- **Multi-layered disaster recovery** - High availability configuration, automated data back up and enterprise information archiving integration to prevent data loss and recover from disaster.
