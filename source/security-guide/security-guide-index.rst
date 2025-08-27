Security Guide
==================

Mattermost offers a comprehensive set of security features to protect information in its mobile applications. These features, ranging from encryption and authentication to device management and user education, provide a secure environment for team collaboration and communication. By prioritizing security, Mattermost ensures that customers can trust the mobile application to safeguard their data and privacy.

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   /security-guide/zero-trust.rst
   /security-guide/cmmc-compliance.rst
   /security-guide/mobile-security.rst
   /security-guide/dependency-vulnerability-analysis.rst
   /security-guide/hipaa-compliance.rst
   /security-guide/finra-compliance.rst

Data-in-transit encryption
---------------------------

Mattermost can be configured to use Transport Layer Security (TLS) to encrypt data transmitted over the network. TLS provides a secure channel for data exchange, protecting it from eavesdropping and tampering during transmission. This encryption ensures that only the intended recipients can access the content, preventing unauthorized parties from intercepting or reading the information.

Mattermost administrators who wish to configure access settings for private and public networks can do so with 3rd party infrastructure using a :doc:`reverse proxy </deployment-guide/server/setup-tls>`. This ensures that devices connected to secure networks can safely access the application while restricting access from untrusted networks. Learn more about Mattermost :ref:`data-in-transit encryption <deployment-guide/encryption-options:encryption-in-transit>`.

Data-at-rest encryption
------------------------

Encryption-at-rest ensures that messages, files, and other data stored in the Mattermost database and file storage are protected from unauthorized access by safeguarding data on physical storage media (e.g., disks) by encrypting it, making it inaccessible without the appropriate encryption keys. Learn more about Mattermost :ref:`data-at-rest encryption <deployment-guide/encryption-options:encryption-at-rest>`.

Encryption-at-rest also available for files stored in Amazon's proprietary S3 system using server-side encryption with :ref:`Amazon S3-managed keys <administration-guide/configure/environment-configuration-settings:enable server-side encryption for amazon s3>` (Mattermost Enterprise) when users choose not to use open source options.

We strongly recommend regularly rotating and securely storing encryption keys using tools, enabling logging and monitoring for access to encrypted data, and ensuring that backup data is encrypted.

Authentication and access control
---------------------------------

Single Sign-On (SSO)
~~~~~~~~~~~~~~~~~~~~

The mobile application integrates with Single Sign-On providers, allowing users to authenticate using their existing credentials from other trusted systems. This reduces the risk of password-related security breaches and streamlines the login process. Learn more about Mattermost :doc:`SSO </administration-guide/manage/admin/user-provisioning>`.

Multi-Factor Authentication (MFA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An additional layer of security beyond username and password. Customers can :doc:`enable and enforce MFA </administration-guide/onboard/multi-factor-authentication>` to protect accounts from unauthorized access, even if login credentials are compromised.

User password requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~

System administrators can configure user password settings to help safeguard the platform against a range of common attack vectors while maintaining usability and compliance with enterprise security policies:

- Enforcing longer passwords ensures a baseline level of strength for every user's credentials. Learn more about configuring a :ref:`minimum password length <administration-guide/configure/authentication-configuration-settings:minimum password length>`.
- Enforcing character complexity protects against attackers exploiting weak or overly simple passwords by enforcing passwords that resist dictionary attacks and common password vulnerabilities. Learn more about configuring :ref:`password requirements <administration-guide/configure/authentication-configuration-settings:password requirements>`.
- Limiting the number of failed authentication attempts before locking the account temporarily or permanently mitigates brute-force, where attackers attempt to guess passwords by repeatedly entering potential combinations. Learn more about configuring the :ref:`maximum number of login attempts <administration-guide/configure/authentication-configuration-settings:maximum login attempts>`.
- Enabling the forgot password flow adds a layer of convenience by ensuring users can reset their password when needed while preventing users from being locked out due to legitimate loss of credentials. Learn more about :ref:`enabling a password reset workflow <administration-guide/configure/authentication-configuration-settings:enable forgot password link>`.

Session management
~~~~~~~~~~~~~~~~~~

System administrators can configure session management settings, including session length, session cache, and idle timeout to ensure user sessions are managed effectively and securely. Session fixation attacks are mitigated as Mattermost sets a new session cookie with each login. Learn more about :ref:`session management configuration settings <administration-guide/configure/environment-configuration-settings:session lengths>`.

Protection against brute force attacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System administrators can :doc:`rate limit Mattermost APIs </administration-guide/configure/environment-configuration-settings>` based on query frequency, memory store size, remote address, and headers.

Remote session revocation & password reset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System administrators can remotely :doc:`revoke user sessions </end-user-guide/preferences/manage-your-security-preferences>` across web, mobile devices, and desktop apps.
User passwords can be remotely :ref:`reset <administration-guide/configure/user-management-configuration-settings:reset user's password>` to enhance security.

Admins can also enforce re-login after a specified period of time by defining :ref:`session lengths <administration-guide/configure/environment-configuration-settings:session lengths>` and by :ref:`revoking user sessions <administration-guide/configure/user-management-configuration-settings:revoke a user's session>` to force users to log back into the system immediately.

Role-Based Access Control (ABAC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Administrators can set granular permissions to control access to sensitive information within the application. This feature ensures that users only have access to the data necessary for their roles, minimizing the risk of accidental or intentional data exposure. Learn more about Mattermost :doc:`role-based access control </end-user-guide/collaborate/learn-about-roles>`.

Cross-origin requests control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose whether to restrict or enable :ref:`cross-origin requests <administration-guide/configure/integrations-configuration-settings:enable cross-origin requests from>` for enhanced control.

Public link management
----------------------

Public links for account creation, file, and image shares can be invalidated by :ref:`regenerating salts <administration-guide/configure/site-configuration-settings:public link salt>` to ensure security.

Public links can also be disabled by setting the :ref:`public link salt <administration-guide/configure/site-configuration-settings:public link salt>` to an empty string. This prevents the creation of new public links and invalidates existing ones.

LLM context management
-----------------------

Mattermost Agents are designed to ensure that only necessary information is sent to the Large Language Model (LLM) for generating accurate responses in Mattermost. Learn how Mattermost :doc:`Agents manages LLM context </end-user-guide/collaborate/agents-context-management>` and how to ensure data privacy.

Audit logs and monitoring
-------------------------

Mattermost writes logs to both the console and to a log file in a machine-readable JSON format. Commercial customers can additionally log directly to syslog and TCP socket destination targets. Learn more about :doc:`Mattermost logging </administration-guide/manage/logging>`.

Activity monitoring
~~~~~~~~~~~~~~~~~~~~

Mattermost stores a complete history of messages, including edits and deletes, along with all files uploaded. User interface actions for deleting messages and channels only remove the data from the user interface; the data is retained within your database. If your compliance guidelines require it, you can disable users' ability to edit and delete their messages after they are posted. Learn more about :doc:`Mattermost permissions </administration-guide/onboard/advanced-permissions>`.

The Mattermost mobile app generates audit logs that record user activities and system events. These logs enable administrators to monitor access and identify potential security threats, ensuring timely detection and response to suspicious behavior.

Regular security updates
------------------------

Patch management
~~~~~~~~~~~~~~~~~

Mattermost regularly releases security updates to address vulnerabilities and enhance the application's security posture. Users are encouraged to keep their mobile applications up to date to benefit from the latest security improvements. Learn more about Mattermost :doc:`releases and the release life cycle </product-overview/releases-lifecycle>`.

Community and expert contributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Being an open-core platform, Mattermost benefits from contributions from the security community and experts. These contributions help identify and mitigate potential security risks, ensuring that the mobile application remains robust and secure. Learn more about `contributing to Mattermost <https://mattermost.com/contribute/>`_.

`Book a live demo <https://mattermost.com/request-demo/>`_  or `talk to a Mattermost expert <https://mattermost.com/contact-sales/>`_ to explore tailored solutions for your organization's secure collaboration needs. Or try Mattermost yourself with a `1-hour preview <https://mattermost.com/sign-up/>`_ for instant access to a live sandbox environment.

Compliance Considerations
--------------------------

Mattermost can be deployed as part of regulated environments where compliance with industry standards is essential.

- HIPAA: Review our guidance on :doc:`deploying Mattermost as part of a HIPAA-compliant IT infrastructure </security-guide/hipaa-compliance>`, with key considerations for protecting electronic protected health information (ePHI).
- FINRA: Learn how :doc:`Mattermost supports organizations in meeting the cybersecurity requirements of FINRA </security-guide/finra-compliance>`.