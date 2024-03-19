Secure command and control
============================

Mattermost's Secure Command and Control solution is designed to provide fast and secure mobile communications for technical teams. It addresses the pain points of data leakage to unsecured channels, like SMS and WhatsApp, and the lack of control and compliance from vendor-hosted mobile applications that leaves technical teams struggling to collaborate securely.

The solution provides easy-to-use collaboration for technical teams, including team messaging, file sharing, audio and screen-share, and process automation directly from your mobile device on iOS or Android. The solution is specifically designed to address the challenges of enterprise-scale secure mobile communications.

Features include:

* :doc:`Private mobile communications </deploy/mobile-overview>` to provide secure mobile apps via encryption keys and certifications with custom mobile applications.
* :doc:`Custom push notification service </deploy/mobile-hpns>` to ensure notifications are not intercepted or leaked to unsecured channels by transmitting push notifications within your private network.
* :ref:`Remote user deactivation with data purge <deploy/client-side-data:mobile app experience>` to mitigate sensitive data from being stored on mobile devices after a user departs the organization.
* (Professional & Enterprise) :ref:`Hosted push notifications service (HPNS) <deploy/mobile-hpns:hosted push notifications service (hpns)>` for production-level uptime SLAs and encrypted TLS connections between HPNS and Apple Push Notification Services, between HPNS and Google’s Firebase Cloud Messaging Service, and between HPNS and your Mattermost Server.
* (Professional & Enterprise) Mobile single-sign-on with :doc:`SAML </onboard/sso-saml>`, :doc:`AD/LDAP </onboard/ad-ldap>`, :doc:`OpenID Connect </onboard/sso-openidconnect>`, :doc:`Google </onboard/sso-google>`, and :doc:`Office365 </onboard/sso-office>` for centralized identity management and automatic account provisioning for fast and secure access to mobile applications.
* (Enterprise) :ref:`ID-only push notifications <deploy/mobile-hpns:id-only push notifications>` to remove the need to pass clear text notifications through Apple and Google’s mobile notification relays.
* (Enterprise) :doc:`Enterprise Mobility Management (EMM) </deploy/deploy-mobile-apps-using-emm-provider>` to manage secure mobile endpoints with a managed app configuration (:doc:`via AppConfig </deploy/mobile-appconfig>`), such as AirWatch.

For an example case study, learn why `The U.S. Department of Defense relies on Mattermost for Secure Command and Control across devices <https://mattermost.com/customers/us-department-of-defense/>`__, including flight crews who can now securely access documents from mobile devices anywhere in the world. 

`Contact us <https://mattermost.com/contact-sales/>`__ to learn more about this solution and to discuss whether it’s the right one for you.