Secure Command and Control
============================

Mattermost's Secure Command and Control solution is designed to provide fast and secure mobile communications for technical teams. It addresses the pain points of data leakage to unsecured channels, like SMS and WhatsApp, and the lack of control and compliance from vendor-hosted mobile applications that leaves technical teams struggling to collaborate securely.

The solution provides easy-to-use collaboration for technical teams, including team messaging, file sharing, audio and screen-share, and process automation directly from your mobile device on iOS or Android. The solution is specifically designed to address the challenges of enterprise-scale secure mobile communications.

.. tip::

    Download `this guide to out-of-band communications <https://mattermost.com/out-of-band-communications/>`_ to learn more about maintaining business continuity, and `this Mattermost for Security Team Operations datasheet <https://mattermost.com/mattermost-security-team-ops-datasheet/>`_ to learn how Mattermost helps increase cyber resilience with faster detection, response, and remediation workflows with collaboration purpose-built for security team operations.

Features include:

* :doc:`Private mobile communications </deploy/mobile/mobile-app-deployment>` to provide secure mobile apps via encryption keys and certifications with custom mobile applications.
* :ref:`Custom push notification service <configure/environment-configuration-settings:enable push notifications>` to ensure notifications are not intercepted or leaked to unsecured channels by transmitting push notifications within your private network.
* :doc:`Remote user deactivation with data purge </deploy/mobile/mobile-faq>` to mitigate sensitive data from being stored on mobile devices after a user departs the organization.
* (Professional & Enterprise) :ref:`Hosted push notifications service (HPNS) <configure/environment-configuration-settings:hosted push notifications service (hpns)>` for production-level uptime SLAs and encrypted TLS connections between HPNS and Apple Push Notification Services, between HPNS and Google’s Firebase Cloud Messaging Service, and between HPNS and your Mattermost Server.
* (Professional & Enterprise) Mobile single-sign-on with :doc:`SAML </onboard/sso-saml>`, :doc:`AD/LDAP </onboard/ad-ldap>`, :doc:`OpenID Connect </onboard/sso-openidconnect>`, :doc:`Google </onboard/sso-google>`, and :doc:`Office365 </onboard/sso-entraid>` for centralized identity management and automatic account provisioning for fast and secure access to mobile applications.
* (Enterprise) :ref:`ID-only push notifications <configure/environment-configuration-settings:id-only push notifications>` to remove the need to pass clear text notifications through Apple and Google’s mobile notification relays.
* (Enterprise) :doc:`Enterprise Mobility Management (EMM) </deploy/mobile/deploy-mobile-apps-using-emm-provider>` to manage secure mobile endpoints with a managed app configuration (:doc:`via AppConfig </deploy/mobile/deploy-mobile-apps-using-emm-provider>`), such as AirWatch.

For an example case study, learn why `The U.S. Department of Defense relies on Mattermost for Secure Command and Control across devices <https://mattermost.com/customers/us-department-of-defense/>`__, including flight crews who can now securely access documents from mobile devices anywhere in the world. 

Talk to a `Mattermost Expert <https://mattermost.com/contact-sales/>`_ to learn more about this solution and to discuss whether it’s the right one for you.