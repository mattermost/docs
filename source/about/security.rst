Security Guide
==================

Mattermost has implemented a comprehensive set of security features to protect information in its mobile applications. These features, ranging from encryption and authentication to device management and user education, provide a secure environment for team collaboration and communication. By prioritizing security, Mattermost ensures that customers can trust the mobile application to safeguard their data and privacy. 

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   /about/security/zero-trust.rst
   /about/security/mobile-security.rst

Data-in-transit encryption
---------------------------

Mattermost uses Transport Layer Security (TLS) to encrypt data transmitted over the network. TLS provides a secure channel for data exchange, protecting it from eavesdropping and tampering during transmission. This encryption ensures that only the intended recipients can access the content, preventing unauthorized parties from intercepting or reading the information.

Mattermost allows administrators to configure access settings for private and public networks. This feature ensures that mobile devices connected to secure networks can safely access the application while restricting access from untrusted networks. Learn more about Mattermost :ref:`data-in-transit encryption <deploy/encryption-options:encryption in transit>`.

Data-at-rest encryption
------------------------

The Mattermost mobile app for Apple iOS and Android devices uses the native OS security architecture to encrypt data-at-rest on mobile devices, ensuring that stored information remains secure even if the device is lost or stolen. This encryption protects sensitive data, such as messages and files, from unauthorized access. Learn more about Mattermost `data-at-rest encryption <deploy/encryption-options:encryption in transit>`.

Data stored by the Mattermost mobile app only resides within the app’s private storage container. This storage location is isolated by each platform’s rigorous sandboxing model. Learn more about :doc:`secure file storage </about/security/secure-mobile-file-storage>` for Mattermost mobile applications.

Authentication and access control
---------------------------------

Mattermost supports multi-factor authentication, adding an extra layer of security beyond the traditional username and password. Customers can enable MFA to protect their accounts from unauthorized access, even if their login credentials are compromised. 

Single Sign-On (SSO)
~~~~~~~~~~~~~~~~~~~~

The mobile application integrates with Single Sign-On providers, allowing users to authenticate using their existing credentials from other trusted systems. This reduces the risk of password-related security breaches and streamlines the login process. Learn more about Mattermost :doc:`SSO </manage/admin/user-provisioning>`.

Role-Based Access Control (ABAC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Administrators can set granular permissions to control access to sensitive information within the application. This feature ensures that users only have access to the data necessary for their roles, minimizing the risk of accidental or intentional data exposure. Learn more about Mattermost :doc:`role-based access control </collaborate/learn-about-roles>`.

Mobile Device Management (MDM)
------------------------------

Mattermost supports the ability for an EMM provider to push Mattermost Mobile apps to EMM-enrolled devices. This approach is recommended for organizations that typically use EMM solutions to deploy Mobile apps to meet security and compliance policies. Learn more about :doc:`deploying Mattermost mobile using an EMM provider </deploy/mobile/deploy-mobile-apps-using-emm-provider``>.

Remote Wipe Capability
~~~~~~~~~~~~~~~~~~~~~~~

Administrators can remotely wipe Mattermost data from mobile devices in case of loss or theft. This capability prevents unauthorized access to sensitive information by ensuring that data is erased from compromised devices. 

Compliance Policies
~~~~~~~~~~~~~~~~~~~~

Mattermost can be integrated with mobile device management solutions to enforce compliance policies. These policies ensure that mobile devices accessing the application adhere to security standards, such as encryption, password complexity, and device integrity. Learm more about `compliance with Mattermost </guides/compliance-with-mattermost>`.

Mobile Access Platforms
~~~~~~~~~~~~~~~~~~~~~~~

Mattermost mobile applications can be operated under the protection of mobile access platforms like Hypori.

Audit Logs and Monitoring
-------------------------

Mattermost write logs to both the console and to a log file in a machine-readable JSON format. Commercial customers can additional log directly to syslog and TCP socket destination targets. Learn more about Mattermost :doc:`logging </manage/logging>`.

Activity Monitoring
~~~~~~~~~~~~~~~~~~~~

The Mattermost mobile app generates audit logs that record user activities and system events. These logs enable administrators to monitor access and identify potential security threats, ensuring timely detection and response to suspicious behavior. 

Alerts and Notifications
~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost can send alerts and notifications to administrators when security-related events occur. This feature ensures that potential issues are promptly addressed, minimizing the impact of security incidents on the organization. Learn about :doc:`managing Mattermost notifications </preferences/manage-your-notifications>`.

Regular Security Updates
------------------------

Patch Management
~~~~~~~~~~~~~~~~~

Mattermost regularly releases security updates to address vulnerabilities and enhance the application's security posture. Users are encouraged to keep their mobile applications up to date to benefit from the latest security improvements. Learn more about Mattermost :doc:`releases and the release life cycle </about/releases-lifecycle>`.

Community and Expert Contributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Being an open-core platform, Mattermost benefits from contributions from the security community and experts. These contributions help identify and mitigate potential security risks, ensuring that the mobile application remains robust and secure. Learn more about `contributing to Mattermost <https://mattermost.com/contribute/>`_.

User Education and Training
---------------------------

Security Awareness
~~~~~~~~~~~~~~~~~~~

Mattermost provides resources and training materials to educate users about security best practices. These resources help users understand the importance of security measures and how to implement them effectively within the mobile application. Visit `Mattermost Academy <https://academy.mattermost.com/>`_ to learn more. 

Incident Response
~~~~~~~~~~~~~~~~~~

Mattermost offers guidance on how to respond to security incidents, including steps to take in case of a data breach or compromise. This training ensures that users are prepared to handle security challenges and protect sensitive information proactively. 



















Security features
------------------

Mattermost offers a host of features to help keep your private cloud communications secure. Learn more about :doc:`Zero Trust with Mattermost </about/security/zero-trust>` and :doc:`mobile security </about/security/mobile-security>`.

Private Cloud deployment with secure mobile apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Mattermost can run entirely behind your firewall as a single Linux binary, as a Docker container, or on your Kubernetes cluster with a PostgreSQL database. Remote access can be enabled through the use of :ref:`VPN clients on PC and mobile devices <deploy/application-architecture:communication protocols>` so that Mattermost can be used outside your private network.
- Mattermost mobile apps can be deployed to an :doc:`internal Enterprise App Store </deploy/mobile/deploy-mobile-apps-using-emm-provider>` by using source code available for Mattermost mobile apps and push notification service. 
- Optionally, the provided Mattermost Mobile Apps can be used when the Mattermost server is reachable through the internet on port 443. In this configuration, you have the option of using compiled iOS and Android applications in iTunes and Google Play provided by Mattermost, Inc. (Mattermost Enterprise and Mattermost Professional).
- User sessions across web, PC, and mobile can be :doc:`remotely revoked through profile settings </preferences/manage-your-security-preferences>`, or via the System Console by deactivating accounts.
- Mattermost apps can be packaged into leading Enterprise Mobility Management solutions including AirWatch and Blackberry through `AppDome <https://www.appdome.com/>`__.

Centralized security and administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Manage users, teams, access control, and system settings in a web-based :doc:`System Console user interface </configure/configuration-settings>`.
- Centralized authentication through AD/LDAP and SAML (Mattermost Enterprise and Mattermost Professional).
- Synchronize users and groups through the built-in :doc:`AD/LDAP integration </onboard/ad-ldap>` (Mattermost Enterprise).

Transmission security
~~~~~~~~~~~~~~~~~~~~~~

- Mattermost supports TLS encryption using AES-256 with 2048-bit RSA between Mattermost client applications and the Mattermost server across both LAN and internet.
- Connections to calls are secured with a combination of:

  - TLS: the existing WebSocket channel is used to secure the signaling path.
  - DTLS v1.2 (mandatory): used for initial key exchange. Supports ``TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`` and ``TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`` algorithms.
  - SRTP (mandatory): used to encrypt all media packets (i.e. those containing voice or screen share). Supports ``AEAD_AES_128_GCM`` and ``AES128_CM_HMAC_SHA1_80`` algorithms. 

- Connections to Active Directory/LDAP can be optionally secured with TLS or stunnel (Mattermost Enterprise and Mattermost Professional).
- Encryption-at-rest is available for messages via hardware and software disk encryption solutions applied to the Mattermost database, which resides on its own server within your infrastructure. To enable end user search and compliance reporting of message histories, Mattermost does not offer encryption within the database.
- Encryption-at-rest is available for files stored via hardware and software disk encryption solutions applied to the server used for local storage or storage via MinIO.
- Encryption-at-rest is available for files stored in Amazon's proprietary S3 system using server-side encryption with :ref:`Amazon S3-managed keys <configure/environment-configuration-settings:enable server-side encryption for amazon s3>` (Mattermost Enterprise) when users choose not to use open source options.
- Option to :ref:`exclude message contents from push notifications <configure/site-configuration-settings:push notification contents>` to comply with strict compliance policies, such as US HIPAA standards.
- Ability to exclude or include the :ref:`contents of messages in push notifications <configure/site-configuration-settings:push notification contents>` to avoid disclosure on locked mobile screens, and via relay servers from Apple and Google when sending notifications to iOS or Android mobile apps (relevant to compliance standards such as HIPAA).

Integrity and audit controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- By default, Mattermost stores a complete history of messages, including edits and deletes, along with all files uploaded. User interface actions for "deleting" messages and channels remove the data only from the user interface; the data is retained within your database. If your compliance guidelines require it, you can turn off users' ability to edit and delete their messages after they are posted.
- Use an `antivirus plugin <https://github.com/mattermost/mattermost-plugin-antivirus>`__ to scan for viruses before uploading a file to Mattermost. Supports `ClamAV anti-virus software <https://www.clamav.net/>`__ across browser, Desktop App, and Mobile Apps.
- Custom :doc:`data retention policies on messages and file uploads </comply/data-retention-policy>` is available (Mattermost Enterprise). A daily data deletion job can be scheduled that deletes messages from the database and user interface, and file uploads from local file storage or Amazon S3, which exceed the specified retention period.
- The :ref:`output and archives of server logs <configure/environment-configuration-settings:file log directory>` can be saved to a directory of your choice. Mattermost server logs plus logs from your web proxy can provide an end-to-end history of system usage.
- :doc:`Ad hoc compliance reports of messaging by user, date range, and keyword, including edited and deleted messages </comply/compliance-monitoring>` are available (Mattermost Enterprise). To protect against unauthorized use, all ad hoc report requests are logged.
- Daily compliance reports compatible with third-party compliance solutions such as :doc:`Global Relay and Actiance </comply/compliance-export>` are also available (Mattermost Enterprise).

Authentication safeguards
~~~~~~~~~~~~~~~~~~~~~~~~~~

- To protect against brute force attacks, you can set :doc:`rate limiting on APIs </configure/environment-configuration-settings>`, varied by query frequency, memory store size, remote address, and headers.
- Session length, session cache, and idle timeout can be :ref:`configured according to your internal policies <configure/environment-configuration-settings:session lengths>`, automatically forcing a user to re-login after a specified period of time.
- Remotely :doc:`revoke user sessions </preferences/manage-your-security-preferences>` across web, mobile devices, and native desktop apps. User sessions can also be revoked remotely by a system admin in **System Console > Users**.
- Session fixation, where an attacker can trick the user to authenticate with a known session cookie, does not affect Mattermost users as a new session cookie is set at each login.
- Remotely reset user passwords via the System Console or via the :ref:`mmctl user reset-password <manage/mmctl-command-line-tool:mmctl user reset-password>` command.
- Mattermost supports integrated authentication with :doc:`Active Directory and LDAP </onboard/ad-ldap>` (Mattermost Enterprise and Mattermost Professional) as well as :doc:`SAML 2.0 SSO integration </onboard/sso-saml>` with providers including :ref:`Active Directory Federation Services <onboard/ad-ldap:configure AD/LDAP deployments with multiple domains>`,  :doc:`Okta </onboard/sso-saml-okta>`, among others (Mattermost Enterprise and Mattermost Professional).
- The ability to require :doc:`multi-factor authentication </onboard/multi-factor-authentication>` is also available (Mattermost Enterprise and Mattermost Professional).

Access control policy
~~~~~~~~~~~~~~~~~~~~~~

To prevent account enumeration, if a user logs in and enters incorrect login details a generic error is presented.

Security is a top concern for organizations who deploy Mattermost in a private network. While running under existing policies and auth protocols of the private network, we prioritize a better user experience (telling a user what went wrong on login) ahead of preventing users on the private network from enumerating accounts.

Mattermost is optimized to be deployed in a highly secure environment. However, admins are given a choice as to the deployment environment.

When Mattermost is deployed outside a firewall, Admins must be aware that their system is exposed to issues inherent in public cloud deployments. In this case, we generally follow the standards of leading online services. For example, Gmail offers APIs that not only confirm whether an email account exists, but also displays the user's profile picture by default.

Mattermost undergoes extensive penetration testing, security reviews, and `security updates <https://mattermost.com/security-updates/>`__. You can find further details and previous discussion `in our GitHub thread <https://github.com/mattermost/platform/issues/4321#issuecomment-258832013>`__. In addition, the following policies are provided:

- Limit communications to specific users, private channels, or team-wide public channels.
- Increase system security :ref:`by restricting email-based account creation to email addresses from a list of specific domains, <configure/authentication-configuration-settings:restrict account creation to specified email domains>` e.g. "corp.mattermost.com", "mattermost.com", etc."
- Choose whether to restrict or enable :ref:`cross-origin requests <configure/integrations-configuration-settings:enable cross-origin requests from>`.
- If sharing of public links for account creation or sharing of files and images are enabled, links can be invalidated via the System Console by :ref:`regenerating salts <configure/site-configuration-settings:public link salt>`.
- Optionally add :ref:`advanced passwords requirements <configure/authentication-configuration-settings:password requirements>` with minimum numbers of symbols, numbers, lower, and uppercase letters.
- Optionally restrict :doc:`creation, renaming, archiving of channels, Private channels, and integrations to team admins, system admins, or end users </onboard/advanced-permissions>` (Mattermost Enterprise and Mattermost Professional).

Copilot context management
~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the :doc:`Copilot context management </collaborate/copilot-context-management>` documentation to learn how Copilot manages LLM context and how to ensure data privacy.

Security updates
-----------------

Security updates address newly discovered attacks reported to Mattermost, Inc. by the security research community. Disclosures are made confidentially, under the Mattermost responsible disclosure policy, allowing for Mattermost, Inc. to provide security updates to the community prior to public disclosure.

For more information, please see:

- `Mattermost Security Updates Disclosures <https://mattermost.com/security-updates/>`_

  - A summary of security updates made based on past and on-going security analysis and penetration testing.

- `Mattermost Responsible Disclosure Policy <https://mattermost.com/security-vulnerability-report/>`_
 
  - An overview of how security issues are confidentially reported to and addressed by Mattermost, Inc.

Security policies
-----------------

For information on internal security policies, development guidelines, business continuity plans, and common security-related questions from enterprises, please see our `Security Policies <https://handbook.mattermost.com/operations/operations/company-policies/security-policies>`__ documentation.

Moreover, Mattermost performs a penetration test on the software no less than once per twelve (12) month period. Customers may request a copy of any penetration test results upon five (5) days' written notice at any time, but no more than once per twelve (12) month period.

HIPAA compliance*
-----------------

Deploying Mattermost as part of a HIPAA-compliant IT infrastructure requires a deployment team trained on `HIPAA-compliance requirements and standards <https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/>`_.

- Mattermost offers HIPAA-relevant **Technical Safeguards** including:

  - :ref:`Integrity Controls <about/security:integrity and audit controls>`
  - :ref:`Access Control <about/security:access control policy>`
  - :ref:`Transmission Security <about/security:transmission security>`
  - :ref:`Audit Controls <about/security:integrity and audit controls>`

- HIPAA-compliant deployments commonly consider the following:

  - Omitting the contents of messages from mobile push and email notifications:

   - If your :ref:`Push Notifications Contents <configure/site-configuration-settings:push notification contents>` option is set to ``Send full message snippet`` there is a chance Personal Health Information (PHI) contained in messages could be displayed on a user's locked phone as a notification. To avoid this, set the option to ``Send generic description with user and channel names`` or ``Send generic description with only sender name``.
   - Similarly, setting :ref:`Email Notifications Contents <configure/site-configuration-settings:email notification contents>` to ``Send generic description with only sender name`` will only send the team name and name of the person who sent the message, with no information about channel name or message contents included in email notifications.

- Beyond Technical Safeguards, HIPAA compliance deployments also require:

  - Administrative Safeguards
  - Physical Safeguards
  - Organizational requirements and other standards.

To learn more, please review `HIPAA requirements from the US Department of Health and Human Services <https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/>`_.

FINRA compliance*
------------------

Mattermost Enterprise features help users to meet the `cybersecurity requirements of the United States Financial Industry Regulatory Authority (FINRA) <https://www.finra.org/rules-guidance/key-topics/cybersecurity>`_ as part of a customer's existing operational systems, including technology governance, system change management, risk assessments, technical controls, incident response, vendor management, data loss prevention, and staff training.

FINRA reviews a firm’s ability to protect the confidentiality, integrity, and availability of sensitive customer information. This includes reviewing each firm’s compliance with SEC regulations, including:

- Regulation `S-P (17 CFR §248.30) <https://www.ecfr.gov/current/title-17/chapter-II/part-248/subpart-A/subject-group-ECFR83262a0bce5ffaa/section-248.30>`_, which requires firms to adopt written policies and procedures to protect customer information against cyber-attacks and other forms of unauthorized access.

- Regulation `S-ID (17 CFR §248.201-202) <https://www.ecfr.gov/current/title-17/chapter-II/part-248>`_, which outlines a firm's duties regarding the detection, prevention, and mitigation of identity theft.

- The `Securities Exchange Act of 1934 (17 CFR §240.17a-4(f)) <https://www.ecfr.gov/current/title-17/chapter-II/part-240>`_, which requires firms to preserve electronically stored records in a non-rewriteable, non-erasable format.

Mattermost supports FINRA compliance as part of a customer's integrated operations in the following ways:

- **Continuous archiving:** Configuration as a non-rewriteable, non-erasable system of record for all messages and files entered into the system. Moreover, automated compliance exports and integration support for Smarsh/Actiance and Global Relay provide third-party eDiscovery options.
- **Secure deployment:** Deployment within private, public, and on-premises networks with existing FINRA-compliant safeguards and infrastructure to protect customer information from cyber attack.
- **Support for intrusion detection:** Ability to support multi-layered intrusion detection from authentication systems to application servers to database access, including configuration of proxy, application, and database logging to deeply audit system interactions.
- **Multi-layered disaster recovery:** High Availability configuration, automated data back up, and enterprise information archiving integration to prevent data loss and recover from disaster.

***DISCLAIMER:** MATTERMOST DOES NOT POSITION ITS PRODUCTS AS “GUARANTEED COMPLIANCE SOLUTIONS”. WE MAKE NO GUARANTEE THAT YOU WILL ACHIEVE REGULATORY COMPLIANCE USING MATTERMOST PRODUCTS. YOUR LEVEL OF SUCCESS IN ACHIEVING REGULATORY COMPLIANCE DEPENDS ON YOUR INTERPRETATION OF THE APPLICABLE REGULATION, AND THE ACTIONS YOU TAKE TO COMPLY WITH THEIR REQUIREMENTS. SINCE THESE FACTORS DIFFER ACCORDING TO INDIVIDUALS AND BUSINESSES, WE CANNOT GUARANTEE YOUR SUCCESS, NOR ARE WE RESPONSIBLE FOR ANY OF YOUR ACTIONS. NO GUARANTEES ARE MADE THAT YOU WILL ACHIEVE ANY SPECIFIC COMPLIANCE RESULTS FROM THE USE OF MATTERMOST OR FROM ANY RECOMMENDATIONS CONTAINED ON OUR WEBSITES, AND AS SUCH, THIS SHOULD NOT BE A SUBSTITUTE TO CONSULTING WITH YOUR OWN LEGAL AND COMPLIANCE REPRESENTATIVES ON THESE MATTERS.
