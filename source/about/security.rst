Security Guide
==================

Mattermost offers a comprehensive set of security features to protect information in its mobile applications. These features, ranging from encryption and authentication to device management and user education, provide a secure environment for team collaboration and communication. By prioritizing security, Mattermost ensures that customers can trust the mobile application to safeguard their data and privacy. 

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   /about/security/zero-trust.rst
   /about/security/mobile-security.rst

Data-in-transit encryption
---------------------------

Mattermost can be configured to use Transport Layer Security (TLS) to encrypt data transmitted over the network. TLS provides a secure channel for data exchange, protecting it from eavesdropping and tampering during transmission. This encryption ensures that only the intended recipients can access the content, preventing unauthorized parties from intercepting or reading the information.

Mattermost administrators who wish to configure access settings for private and public networks can do so with 3rd party infrastructure using a :doc:`reverse proxy </deploy/server/setup-tls>`. This ensures that devices connected to secure networks can safely access the application while restricting access from untrusted networks. Learn more about Mattermost :ref:`data-in-transit encryption <deploy/encryption-options:encryption-in-transit>`.

Data-at-rest encryption
------------------------

Encryption-at-rest ensures that messages, files, and other data stored in the Mattermost database and file storage are protected from unauthorized access by safeguarding data on physical storage media (e.g., disks) by encrypting it, making it inaccessible without the appropriate encryption keys. Learn more about Mattermost :ref:`data-at-rest encryption <deploy/encryption-options:encryption-at-rest>`.

Encryption-at-rest also available for files stored in Amazon's proprietary S3 system using server-side encryption with :ref:`Amazon S3-managed keys <configure/environment-configuration-settings:enable server-side encryption for amazon s3>` (Mattermost Enterprise) when users choose not to use open source options.

We strongly recommend regularly rotating and securely storing encryption keys using tools, enabling logging and monitoring for access to encrypted data, and ensuring that backup data is encrypted.

Authentication and access control
---------------------------------

Single Sign-On (SSO)
~~~~~~~~~~~~~~~~~~~~

The mobile application integrates with Single Sign-On providers, allowing users to authenticate using their existing credentials from other trusted systems. This reduces the risk of password-related security breaches and streamlines the login process. Learn more about Mattermost :doc:`SSO </manage/admin/user-provisioning>`.

Multi-Factor Authentication (MFA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An additional layer of security beyond username and password. Customers can :doc:`enable and enforce MFA </onboard/multi-factor-authentication>` to protect accounts from unauthorized access, even if login credentials are compromised.

User password requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~

System administrators can configure user password settings to help safeguard the platform against a range of common attack vectors while maintaining usability and compliance with enterprise security policies:

- Enforcing longer passwords ensures a baseline level of strength for every user's credentials. Learn more about configuring a :ref:`minimum password length <configure/authentication-configuration-settings:minimum password length>`.
- Enforcing character complexity protects against attackers exploiting weak or overly simple passwords by enforcing passwords that resist dictionary attacks and common password vulnerabilities. Learn more about configuring :ref:`password requirements <configure/authentication-configuration-settings:password requirements>`.
- Limiting the number of failed authentication attempts before locking the account temporarily or permanently mitigates brute-force, where attackers attempt to guess passwords by repeatedly entering potential combinations. Learn more about configuring the :ref:`maximum number of login attempts <configure/authentication-configuration-settings:maximum login attempts>`.
- Enabling the forgot password flow adds a layer of convenience by ensuring users can reset their password when needed while preventing users from being locked out due to legitimate loss of credentials. Learn more about :ref:`enabling a password reset workflow <configure/authentication-configuration-settings:enable forgot password link>`.

Session management
~~~~~~~~~~~~~~~~~~

System administrators can configure session management settings, including session length, session cache, and idle timeout to ensure user sessions are managed effectively and securely. Session fixation attacks are mitigated as Mattermost sets a new session cookie with each login. Learn more about :ref:`session management configuration settings <configure/environment-configuration-settings:session lengths>`.

Protection against brute force attacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System administrators can :doc:`rate limit Mattermost APIs </configure/environment-configuration-settings>` based on query frequency, memory store size, remote address, and headers.

Remote session revocation & password reset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System administrators can remotely :doc:`revoke user sessions </preferences/manage-your-security-preferences>` across web, mobile devices, and desktop apps.
User passwords can be remotely :ref:`reset <configure/user-management-configuration-settings:reset user's password>` to enhance security. 

Admins can also enforce re-login after a specified period of time by defining :ref:`session lengths <configure/environment-configuration-settings:session lengths>` and by :ref:`revoking user sessions <configure/user-management-configuration-settings:revoke a user's session>` to force users to log back into the system immediately.

Role-Based Access Control (ABAC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Administrators can set granular permissions to control access to sensitive information within the application. This feature ensures that users only have access to the data necessary for their roles, minimizing the risk of accidental or intentional data exposure. Learn more about Mattermost :doc:`role-based access control </collaborate/learn-about-roles>`.

Cross-origin requests control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose whether to restrict or enable :ref:`cross-origin requests <configure/integrations-configuration-settings:enable cross-origin requests from>` for enhanced control.

Public link management
----------------------

Public links for account creation, file, and image shares can be invalidated by :ref:`regenerating salts <configure/site-configuration-settings:public link salt>` to ensure security.

Public links can also be disabled by setting the :ref:`public link salt <configure/site-configuration-settings:public link salt>` to an empty string. This prevents the creation of new public links and invalidates existing ones.

LLM context management
-----------------------

Mattermost Agents are designed to ensure that only necessary information is sent to the Large Language Model (LLM) for generating accurate responses in Mattermost. Learn how Mattermost :doc:`Agents manages LLM context </collaborate/agents-context-management>` and how to ensure data privacy.

Audit logs and monitoring
-------------------------

Mattermost writes logs to both the console and to a log file in a machine-readable JSON format. Commercial customers can additionally log directly to syslog and TCP socket destination targets. Learn more about :doc:`Mattermost logging </manage/logging>`.

Activity monitoring
~~~~~~~~~~~~~~~~~~~~

Mattermost stores a complete history of messages, including edits and deletes, along with all files uploaded. User interface actions for deleting messages and channels only remove the data from the user interface; the data is retained within your database. If your compliance guidelines require it, you can disable users' ability to edit and delete their messages after they are posted. Learn more about :doc:`Mattermost permissions </onboard/advanced-permissions>`.

The Mattermost mobile app generates audit logs that record user activities and system events. These logs enable administrators to monitor access and identify potential security threats, ensuring timely detection and response to suspicious behavior.

Regular security updates
------------------------

Patch management
~~~~~~~~~~~~~~~~~

Mattermost regularly releases security updates to address vulnerabilities and enhance the application's security posture. Users are encouraged to keep their mobile applications up to date to benefit from the latest security improvements. Learn more about Mattermost :doc:`releases and the release life cycle </about/releases-lifecycle>`.

Community and expert contributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Being an open-core platform, Mattermost benefits from contributions from the security community and experts. These contributions help identify and mitigate potential security risks, ensuring that the mobile application remains robust and secure. Learn more about `contributing to Mattermost <https://mattermost.com/contribute/>`_.

HIPAA compliance*
-----------------

Deploying Mattermost as part of a HIPAA-compliant IT infrastructure requires a deployment team trained on `HIPAA-compliance requirements and standards <https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/>`_.

HIPAA-compliant deployments commonly consider the following:

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
