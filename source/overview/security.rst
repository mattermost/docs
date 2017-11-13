=====================================
Security Overview
=====================================

Security in Mattermost software is continually reviewed by developers, 
IT administrators,
and security analysts who deploy Mattermost Editions in their organizations.

Our software undergoes multiple rounds of penetration testing and security analysis as well as constant internal review.
This diligence and the efficacy of the open source community alongside our Enterprise Edition user feedback has produced a long list of safeguards, processes, 
policies, 
and compliance features.
The features following represent an overview of Mattermost's exceedingly robust security features and safeguards.


Private Cloud Deployment with Secure Mobile applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost can run entirely behind your firewall as a single Linux binary with MySQL or PostgreSQL.
Mobile applications can be deployed to an `internal Enterprise App Store <https://docs.mattermost.com/deployment/push.html#enterprise-app-store-eas>`_ by using source code available for Mattermost mobile applications and push notification service. 
Optionally `VPN clients on PC and mobile devices <https://docs.mattermost.com/deployment/deployment.html#vpn-setup>`_ can be used outside your private network.

Mattermost mobile applications can run without a VPN by opening standard ports on your Mattermost server, 
such as 80 or 443. 
In this configuration you have the option of using compiled `iOS and Android applications in iTunes and Google Play provided by Mattermost, Inc. <https://docs.mattermost.com/deployment/push.html#hosted-push-notifications-service-hpns>`_ for Mattermost Enterprise Editions E10 and E20. 
Both Enterprise Editions provide for `multi-factor authentication <https://docs.mattermost.com/administration/config-settings.html#enable-multi-factor-authentication-enterprise>`_.

User sessions across web, 
PC,
and mobile can be `remotely revoked through account settings <https://docs.mattermost.com/help/settings/account-settings.html#view-and-logout-of-active-sessions>`_, or through the System Console by deactivating accounts.

Mattermost applications can be packaged into leading Enterprise Mobility Management solutions including AirWatch and Blackberry through `AppDome <https://www.appdome.com/>`_.

Centralized Security and Administration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Administrators can manage users, 
teams, 
access control,
and system settings in a web-based `System Console user interface <https://docs.mattermost.com/administration/config-settings.html>`_.

Transmission Security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost supports TLS encryption using AES-256 with 2048-bit RSA on all data transmissions between Mattermost client applications and the Mattermost server across both LAN and internet.

Connections to Active Directory/LDAP can be optionally secured with TLS or stunnel on Mattermost Enterprise Edition E10.
Encryption-at-rest is available for messages through hardware and software disk encryption solutions applied to the Mattermost database on its own server in the client's infrastructure. 

Mattermost does not offer encryption within the database so end user search and compliance reporting of message histories can be enabled. 

Encryption-at-rest is available for files stored through hardware and software disk encryption solutions applied to the server used for local storage or storage through Minio.
Encryption-at-rest is also available for files stored in Amazon's proprietary S3 system using server-side encryption with `Amazon S3-managed keys <https://docs.mattermost.com/administration/config-settings.html#enable-server-side-encryption-for-amazon-s3>`_ on Mattermost Enterprise Edition E20 when users choose not to use open source options.

There is an option to `exclude message contents from push notifications <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_ to comply with strict compliance policies like US HIPAA standards.

Users have the ability to exclude or include the `contents of messages in push notifications <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_ to avoid disclosure on locked mobile screens, 
and through relay servers from Apple and Google when sending notifications to iOS or Android mobile applications. This is relevant to compliance standards such as HIPAA.

Integrity and Audit Controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost stores a complete history of messages by default.
This includes edits and deletes and all uploaded files. 
User interface actions for *deleting* messages and channels remove the data only from the user interface but not from your database. 
If compliance guidelines demand more then administrators can turn off users' ability to edit and delete their messages after posting.

Custom `data retention policies on messages and file uploads <https://docs.mattermost.com/administration/data-retention.html>`_ is available in Mattermost Enterprise Edition E20. 
A daily data deletion job can be scheduled to purge messages from the database and user interfaces and purge file uploads from local file storage or Amazon S3 that have exceeded the specified retention period. 

The `output and archives of server logs <https://docs.mattermost.com/administration/config-settings.html#file-log-directory>`_ can be saved to a directory of an organization's choice. 

Mattermost server logs and logs from a web proxy can provide an end-to-end history of system usage.
`Ad hoc compliance reports of messaging by user, 
date range, 
and keyword, 
including edited and deleted messages <https://docs.mattermost.com/administration/compliance.html>`_,
are available on Mattermost Enterprise Edition E20. 

All ad hoc report requests are logged to protect against unauthorized use. 
Daily compliance reports compatible with third party compliance solutions like `Global Relay <https://docs.mattermost.com/administration/compliance.html#global-relay-support>`_ are also available on Mattermost Enterprise Edition E20.

Authentication Safeguards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users can set `rate limiting on APIs <https://docs.mattermost.com/administration/config-settings.html#id55>`_ to protect against brute force attacks varied by query frequency, 
memory store size, 
remote address,
and headers.

Session length, 
session cache,
and idle timeout can be `configured according to your internal policies <https://docs.mattermost.com/administration/config-settings.html#sessions>`_. This forces users to login again after a specified period of time.

Remotely `revoke user sessions <https://docs.mattermost.com/help/settings/account-settings.html#view-and-logout-of-active-sessions>`_ across web, 
mobile devices,
and native desktop applications
and remotely reset user passwords through the System Console or through the `command line <https://docs.mattermost.com/administration/command-line-tools.html#platform-user-password>`_.

Mattermost supports integrated authentication with `Active Directory and LDAP <https://docs.mattermost.com/deployment/sso-ldap.html>`_ on Mattermost Enterprise Editions E10 and E20,
and `SAML 2.0 SSO integration <https://docs.mattermost.com/deployment/sso-saml.html>`_ with providers including `Active Directory Federation Services <https://docs.mattermost.com/deployment/sso-saml-adfs.html>`_,  `Okta <https://docs.mattermost.com/deployment/sso-saml-okta.html>`_, among others on Mattermost Enterprise Edition E20.

Users can mandate `multi-factor authentication <https://docs.mattermost.com/deployment/auth.html>`_ on Mattermost Enterprise Editions E10 and E20.

Access Control Policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All of Mattermost's editions can limit communications to specific users, 
private channels, 
or team-wide public channels.
System security can be increased `by restricting email-based account creation to email addresses from a list of specific domains, <https://docs.mattermost.com/administration/config-settings.html#restrict-account-creation-to-specified-email-domains>`_ , 
for example, *corp.mattermost.com*.

Users can choose whether to restrict or enable `cross-origin requests. <https://docs.mattermost.com/administration/config-settings.html#enable-cross-origin-requests-from>`_

Links can be invalidated through the System Console by `regenerating salts <https://docs.mattermost.com/administration/config-settings.html#public-link-salt>`_ if sharing of public links for account creation or sharing of files and images is enabled.

Administrators can:
- restrict `creation, 
renaming, 
archiving of channels, 
private channels and integrations to team admins, 
system admins,
or end users <https://docs.mattermost.com/administration/config-settings.html#policy-enterprise>`_ on Mattermost Enterprise Edition E10.

- restrict `sending team invites to team admins, 
system admins or end users <https://docs.mattermost.com/administration/config-settings.html#policy-enterprise>`_ on Mattermost Enterprise Edition E10.

- add `advanced passwords requirements <https://docs.mattermost.com/administration/config-settings.html#password-requirements-enterprise>`_ with minimum numbers of symbols, 
numbers, 
and lower and uppercase letters on Mattermost Enterprise Edition E10.

Security Updates
------------------------------------

Security updates address newly discovered attacks reported to Mattermost, Inc. by the security research community. Disclosures are made confidentially, under the Mattermost responsible disclosure policy, allowing for Mattermost, Inc. to provide security updates to the community prior to public disclosure.

For more information, please see:

- `Mattermost Security Updates Disclosures <http://about.mattermost.com/security-updates/>`_
A summary of security updates made based on past and on-going security analysis and penetration testing.

- `Mattermost Responsible Disclosure Policy <https://www.mattermost.org/responsible-disclosure-policy/>`_
An overview of how security issues are confidentially reported to and address by Mattermost, Inc.

Security Policies
------------------------------------

For information on internal security policies, 
development guidelines, 
business continuity plans,
and common security-related questions from enterprises, 
please see our `Security Policies <https://docs.mattermost.com/process/security.html>`_ documentation.


HIPAA compliance
------------------------------------

Deploying Mattermost as part of a HIPAA-compliant IT infrastructure requires a deployment team trained on `HIPAA-compliance requirements and standards <http://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/>`_.

Mattermost offers HIPAA-relevant *Technincal Safeguards* including:

- Integrity Controls <https://docs.mattermost.com/overview/security.html#integrity-audit-controls>`_
- Access Control <https://docs.mattermost.com/overview/security.html#access-control-policy>`_
- Transmission Security <https://docs.mattermost.com/overview/security.html#transmission-security>`_
- Audit Controls <https://docs.mattermost.com/overview/security.html#integrity-audit-controls>`_.

HIPAA-compliant deployments commonly omit the contents of messages from mobile push and email notifications:

- If your `Push Notifications Contents <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_ option is set to ``Send full message snippet`` there is a chance Personal Health Information (PHI) contained in messages could be displayed on a user's locked phone as a notification. 
To avoid this, 
set the option to ``Send generic description with user and channel names`` or ``Send generic description with only sender name``.

- Setting `Email Notifications Contents <https://docs.mattermost.com/administration/config-settings.html#email-notification-contents>`_ to ``Send generic description with only sender name`` will send the team name and name of the person who sent the message absent information about channel name or message contents included in email notifications.

Beyond Technical Safeguards, HIPAA compliance deployments also require:

- Administrative Safeguards
- Physical Safeguards
- Organizational requirements and other standards.

To learn more, please review `HIPAA requirements from the US Department of Health and Human Services <http://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/>`_.
