Security Overview
------

Mattermost keeps your data safe, secure, and private with enterprise-class data security and control.

Mattermost Enterprise Edition E20, E10, and Team Edition offer: 

- Data Center-ready, private cloud deployment 
   - Ability to self-host 100% of your workplace messaging, including mobile applications via an Enterprise App Store.
   - Ability to run behind your firewall as a Linux binary with a MySQL or PostgreSQL database.
   - Ability to use `self-host mobile applications <http://docs.mattermost.com/deployment/push.html#enterprise-app-store-eas>`_ through source code available for Mattermost iOS and Android apps, as an alternative to pre-compiled mobile apps from iTunes and Google Play.

- End-to-end encryption
   - Supports TLS encryption using AES-256 with 2048-bit RSA on all data transmissions across both LAN and internet.
   - Encrypted data at rest through compatibility with disk-level encryption on the Mattermost database server.
   
- Centralized Security and Administration 
   - Manage users, permissions and devices in a web-based UI.
   - Remotely revoke user sessions across mobile devices and native desktop apps.

- Collaboration with the global security research community to continuously improve security
   - A `responsible disclosure policy <http://www.mattermost.org/responsible-disclosure-policy/>`_ for security researchers to report issues and contribute to security improvements. 
   - Mattermost undergoes security reviews and penetration testing at customer sites and `discloses security updates resulting from customer findings on a monthly basis. <https://about.mattermost.com/security-updates/>`_  
   
In addition, Mattermost Enterprise Edition E20 and E10 offer: 

- Enhanced security with multi-factor authentication for user sign-in.
- Encrypted connection to Active Directory/LDAP authentication service using TLS or stunnel.
- Fast setup of encrypted, private cloud push notifications using `a hosted proxy and pre-compiled mobile applications. <http://docs.mattermost.com/deployment/push.html#hosted-push-notifications-service-hpns>`_

**Notes on HIPPA compliance in the United States:**

- Deploying Mattermost as a HIPPA-compliant communication system requires a deployment team trained on HIPPA-compliance requirements and standards. Some items to note include: 

   - If mobile apps from iTunes or Google Play are used with push notifications enabled, it is recommended that `push notification contents <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_ be set to ``generic`` so that confidential data contained in messages does not appear unencrypted to Apple and Google servers relaying notifications to mobile devices.
   - Transport layer TLS encryption and disk-level encryption on the Mattermost database are options to consider for satisfying HIPPA encryption requirements. 

