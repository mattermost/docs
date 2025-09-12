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

Data-in-Transit Encryption
---------------------------

Mattermost can be configured to use Transport Layer Security (TLS) to encrypt data transmitted over the network. TLS provides a secure channel for data exchange, protecting it from eavesdropping and tampering during transmission. This encryption ensures that only the intended recipients can access the content, preventing unauthorized parties from intercepting or reading the information.

Mattermost administrators who wish to configure access settings for private and public networks can do so with 3rd party infrastructure using a :doc:`reverse proxy </deployment-guide/server/setup-tls>`. This ensures that devices connected to secure networks can safely access the application while restricting access from untrusted networks. Learn more about Mattermost :ref:`data-in-transit encryption <deployment-guide/encryption-options:encryption-in-transit>`.

Data-at-Rest Encryption
------------------------

Encryption-at-rest ensures that messages, files, and other data stored in the Mattermost database and file storage are protected from unauthorized access by safeguarding data on physical storage media (e.g., disks) by encrypting it, making it inaccessible without the appropriate encryption keys. Learn more about Mattermost :ref:`data-at-rest encryption <deployment-guide/encryption-options:encryption-at-rest>`.

Encryption-at-rest also available for files stored in Amazon's proprietary S3 system using server-side encryption with :ref:`Amazon S3-managed keys <administration-guide/configure/environment-configuration-settings:enable server-side encryption for amazon s3>` (Mattermost Enterprise) when users choose not to use open source options.

We strongly recommend regularly rotating and securely storing encryption keys using tools, enabling logging and monitoring for access to encrypted data, and ensuring that backup data is encrypted.

Authentication and Access Control
---------------------------------

Single Sign-On (SSO)
~~~~~~~~~~~~~~~~~~~~

The mobile application integrates with Single Sign-On providers, allowing users to authenticate using their existing credentials from other trusted systems. This reduces the risk of password-related security breaches and streamlines the login process. Learn more about Mattermost :doc:`SSO </administration-guide/manage/admin/user-provisioning>`.

Multi-Factor Authentication (MFA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An additional layer of security beyond username and password. Customers can :doc:`enable and enforce MFA </administration-guide/onboard/multi-factor-authentication>` to protect accounts from unauthorized access, even if login credentials are compromised.

User Password Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~

System administrators can configure user password settings to help safeguard the platform against a range of common attack vectors while maintaining usability and compliance with enterprise security policies:

- Enforcing longer passwords ensures a baseline level of strength for every user's credentials. Learn more about configuring a :ref:`minimum password length <administration-guide/configure/authentication-configuration-settings:minimum password length>`.
- Enforcing character complexity protects against attackers exploiting weak or overly simple passwords by enforcing passwords that resist dictionary attacks and common password vulnerabilities. Learn more about configuring :ref:`password requirements <administration-guide/configure/authentication-configuration-settings:password requirements>`.
- Limiting the number of failed authentication attempts before locking the account temporarily or permanently mitigates brute-force, where attackers attempt to guess passwords by repeatedly entering potential combinations. Learn more about configuring the :ref:`maximum number of login attempts <administration-guide/configure/authentication-configuration-settings:maximum login attempts>`.
- Enabling the forgot password flow adds a layer of convenience by ensuring users can reset their password when needed while preventing users from being locked out due to legitimate loss of credentials. Learn more about :ref:`enabling a password reset workflow <administration-guide/configure/authentication-configuration-settings:enable forgot password link>`.

Session Management
~~~~~~~~~~~~~~~~~~

System administrators can configure session management settings, including session length, session cache, and idle timeout to ensure user sessions are managed effectively and securely. Session fixation attacks are mitigated as Mattermost sets a new session cookie with each login. Learn more about :ref:`session management configuration settings <administration-guide/configure/environment-configuration-settings:session lengths>`.

Protection Against Brute Force Attacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System administrators can :doc:`rate limit Mattermost APIs </administration-guide/configure/environment-configuration-settings>` based on query frequency, memory store size, remote address, and headers.

Remote Session Revocation & Password Reset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System administrators can remotely :doc:`revoke user sessions </end-user-guide/preferences/manage-your-security-preferences>` across web, mobile devices, and desktop apps.
User passwords can be remotely :ref:`reset <administration-guide/configure/user-management-configuration-settings:reset user's password>` to enhance security.

Admins can also enforce re-login after a specified period of time by defining :ref:`session lengths <administration-guide/configure/environment-configuration-settings:session lengths>` and by :ref:`revoking user sessions <administration-guide/configure/user-management-configuration-settings:revoke a user's session>` to force users to log back into the system immediately.

Role-Based Access Control (ABAC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Administrators can set granular permissions to control access to sensitive information within the application. This feature ensures that users only have access to the data necessary for their roles, minimizing the risk of accidental or intentional data exposure. Learn more about Mattermost :doc:`role-based access control </end-user-guide/collaborate/learn-about-roles>`.

Cross-Origin Requests Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose whether to restrict or enable :ref:`cross-origin requests <administration-guide/configure/integrations-configuration-settings:enable cross-origin requests from>` for enhanced control.

Public Link Management
----------------------

Public links for account creation, file, and image shares can be invalidated by :ref:`regenerating salts <administration-guide/configure/site-configuration-settings:public link salt>` to ensure security.

Public links can also be disabled by setting the :ref:`public link salt <administration-guide/configure/site-configuration-settings:public link salt>` to an empty string. This prevents the creation of new public links and invalidates existing ones.

LLM Context Management
-----------------------

Mattermost Agents are designed to ensure that only necessary information is sent to the Large Language Model (LLM) for generating accurate responses in Mattermost. Learn how Mattermost :doc:`Agents manages LLM context </end-user-guide/collaborate/agents-context-management>` and how to ensure data privacy.

Audit Logs and Monitoring
-------------------------

Mattermost writes logs to both the console and to a log file in a machine-readable JSON format. Commercial customers can additionally log directly to syslog and TCP socket destination targets. Learn more about :doc:`Mattermost logging </administration-guide/manage/logging>`.

Activity Monitoring
~~~~~~~~~~~~~~~~~~~~

Mattermost stores a complete history of messages, including edits and deletes, along with all files uploaded. User interface actions for deleting messages and channels only remove the data from the user interface; the data is retained within your database. If your compliance guidelines require it, you can disable users' ability to edit and delete their messages after they are posted. Learn more about :doc:`Mattermost permissions </administration-guide/onboard/advanced-permissions>`.

The Mattermost mobile app generates audit logs that record user activities and system events. These logs enable administrators to monitor access and identify potential security threats, ensuring timely detection and response to suspicious behavior.

Regular Security Updates
------------------------

Patch Management
~~~~~~~~~~~~~~~~~

Mattermost regularly releases security updates to address vulnerabilities and enhance the application's security posture. Users are encouraged to keep their mobile applications up to date to benefit from the latest security improvements. Learn more about Mattermost :doc:`releases and the release life cycle </product-overview/releases-lifecycle>`.

Community and Expert Contributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Being an open-core platform, Mattermost benefits from contributions from the security community and experts. These contributions help identify and mitigate potential security risks, ensuring that the mobile application remains robust and secure. Learn more about `contributing to Mattermost <https://mattermost.com/contribute/>`_.

`Book a live demo <https://mattermost.com/request-demo/>`_  or `talk to a Mattermost expert <https://mattermost.com/contact-sales/>`_ to explore tailored solutions for your organization's secure collaboration needs. Or try Mattermost yourself with a `1-hour preview <https://mattermost.com/sign-up/>`_ for instant access to a live sandbox environment.

Compliance Considerations
--------------------------

Mattermost can be deployed as part of regulated environments where compliance with industry standards is essential.

- HIPAA: Review our guidance on :doc:`deploying Mattermost as part of a HIPAA-compliant IT infrastructure </security-guide/hipaa-compliance>`, with key considerations for protecting electronic protected health information (ePHI).
- FINRA: Learn how :doc:`Mattermost supports organizations in meeting the cybersecurity requirements of FINRA </security-guide/finra-compliance>`.

Frequently Asked Questions
---------------------------

What are the trust benefits of Mattermost compared to third-party SaaS systems that let customers manage their own encryption keys?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Encryption doesn't mean a third-party SaaS vendor can't read your data.** A third-party vendor who provides encryption keys to the database that stores a customer's data at rest may still be able to read a customer's data while its in transit.

For example, performing a search on message histories requires access to unencrypted messages in order to match the search term to words in your unencrypted message history.

As another example, a customer's data encryption key is unlikely to be deployed to the mobile devices of end users; therefore, when a third-party system sends a push notification to an end user's mobile device, the unencrypted text is available to the third party.

In contrast, Mattermost is hosted by the customer. Not only can data be encrypted at rest and in-transit with keys generated by the customer (which no vendors ever touch), unencrypted data for search and mobile notifications is handled by systems under your IT team's control.

If it’s unclear from the vendor’s documentation whether or not your data can be read, ask them directly.

**Moreover, high trust enterprises need more than encryption - they need privacy, total data ownership, auditability, and control of their infrastructure.**

*Privacy* means a third-party service cannot monitor the identity, IP address, location, or access patterns of your employees, nor their activity on your system, nor provide that information either intentionally through a court order (which you may never be informed about) or unintentionally through a data breach.

*Total data ownership* means a third party cannot prevent you from accessing your data at any time. It means no third party can read your data, analyze it or monetize it. It means that should you end your commercial relationship, you maintain your records with any backups. It also means you can delete your data at any time and verify that no additional copies remain.

*Audibility* means being able to fully observe, monitor, and trace the operations of your systems.

*Control of infrastructure* means being able to operate and customize your system to the specific needs of your business, including the ability to run on public and private networks, as well as on-prem, and interoperate with critical legacy systems with full observability and transparency down to reading the source code.

As an open source self-hosted system, Mattermost provides privacy, total data ownership, and control of infrastructure required by high trust teams.

What are the fundamental security challenges with Massive, Multi-Tenant Applications (MMTA)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The key risk of allowing confidential data to enter a Massively Multi-Tenant Applications (MMTA) is having the system breached, never knowing your data has been compromised, and having stolen data used to breach your other systems.

Marketers from MMTA vendors pay highly credentialed security professionals to offer "Death Star Logic" to gain a customer’s trust: "MMTA's SaaS offering is the most secure system in the galaxy because it outspends its customers on security investments, therefore the MMTA is more secure than a customer's self-hosted infrastructure."

The problem with Death Star Logic is that it omits the fact that hosting confidential data from thousands of enterprise customers makes it the prime target for cyber attacks, which increases risk to customers for four key reasons:

**1) Over time, MMTA vendors become Nation State Targets**

The effort behind a cyber attack is proportional to the value of breaching the system. As the value of the data held by an MMTA vendor increases, so does the scale of its cyber threats.

Vendors become "Nation State Targets" when the value of the breaching their system is so high it attracts the attention of the cyberwarfare branches of hostile nations. From there, even the smallest errors in system security can result in a significant breach.

**2) MMTA systems can't protect customers from unknown vulnerabilities**

A single bug in an MMTA system can put all customers at risk. For example, `Slack reported a bug that exposed message histories and files for nearly four million users <https://www.wired.com/2017/03/hack-brief-slack-bug-everyones-worst-office-nightmare/>`_ (2017), and `a bug left 400 million Microsoft accounts exposed to account takeover <https://hackread.com/critical-bug-in-microsoft-left-400m-accounts-exposed/>`_ (2018).

For multi-tenant systems, bugs in infrastructure can present vulnerabilities as well. For example, in 2018 researchers discovered that chip-level exploits like `Meltdown and Spectre <https://www.wired.com/story/intel-meltdown-spectre-storm/>`__, which had been around for decades, could make it possible for malicious code run by one tenant to affect the operations of another tenant that shared the same CPU.

Keeping MMTA systems secure depends on the ability of internal and external security researches to continually stay ahead of cyber-attackers.

**3) Customers don't know when breaches occur**

When an MMTA is breached, it is most likely from an unknown bug or an unknown vulnerability. Because of this, it may not be clear that a system has been breached, and customers may not be notified. Moreover, following a breach, there's often no way for the customer's security team to audit the MMTA vendor and understand how their confidential data may have been accessed or stolen.

The end result is confidential information passing through an MMTA may be used to exploit other systems the customer operates, with no way to trace the root of the breach to mitigate it in future.

As an example, when `OneLogin reported a security breach that allowed the attacker to decrypt encrypted data impacting 2000 customers and 70 SaaS apps <https://krebsonsecurity.com/2017/06/onelogin-breach-exposed-ability-to-decrypt-data/>`_ (2017), details were vague and there was little customers could do to analyze their risk or reduce risk in future.

In contrast, an open source, self-hosted collaboration solution remains within the layers of physical security and network security enterprises use to protect their most valuable assets, with full access to logging and system histories to know when, where and how an attack might have occurred.

Moreover, as a single-tenant solution, the strength of cyberattacks is typically limited to the breach value of just your confidential data and not the aggregate breach value of all customer data held by an MMTA. Plus, the sum of security investments your company makes to protect systems in its private networks accrues to your collaboration system - and for banks, this could be hundreds of millions of dollars a year.

**4) MMTA systems risk cross-bleeding your data**

MMTA also runs the risk of bugs or misconfigurations in a vendor’s multi-tenant system bleeding your data into another customer’s space, or vice versa. Bleeds can occur via logging systems, in application logic, middleware, and data layer errors. In 2019, `Facebook admitted to accidentally storing hundreds of millions of user passwords in clear text for years due to a configuration oversight <https://krebsonsecurity.com/2019/03/facebook-stored-hundreds-of-millions-of-user-passwords-in-plain-text-for-years/>`__.

Why does Mattermost disclose whether or not an account exists when a user enters an incorrect password?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost's core design principle is to be "fast, obvious, forgiving" and, telling users that they made a mistake in entering their password, is in service of our principle of prioritizing user interests.

When using username-password authentication, especially with AD/LDAP, there's the possibility of usernames being email addresses, Mattermost username, AD/LDAP username and ID, or other AD/LDAP attributes and our design principle intends to help end users understand whether their login error came from having the wrong password or the wrong email/username.

We believe this design increases productivity, speeds up user adoption, and reduces help desk tickets and support costs - and that these benefits outweigh the trade-offs.

The trade-off with this design is that if physical security is not in effect, network security is not in effect (i.e., no VPN or a malicious user within the private network), and username-password authentication is used, an attacker may be able to enumerate email addresses or usernames by sending HTTP requests to the system, up to the maximum number of requests per second defined in Mattermost's :doc:`API rate limiting settings </administration-guide/configure/environment-configuration-settings>`.

For organizations who choose to deploy in such a configuration, please consider the following mitigations:

1. Instead of username-password, use a Single Sign-On (SSO) provider in Mattermost Enterprise Edition like OneLogin, Okta, or ADFS, or use the GitLab SSO option available with Mattermost Professional and Enterprise editions (deprecated for Team Edition from v11.0.0).
2. Per the recommended install instructions, use a VPN client to apply network security to your deployment.
3. Enable monitoring and alerting from your proxy server to detect and isolate malicious behavior reaching your deployment.

Above all, make sure to subscribe to the `Mattermost Security Bulletin <https://mattermost.com/security-updates/#sign-up>`__ and apply security patches as recommended.