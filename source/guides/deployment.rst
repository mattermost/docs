Install Mattermost Server
=========================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Learn how to install Mattermost Server for teams and organizations of any size.

.. toctree::
    :maxdepth: 1
    :hidden:

    Software requirements </install/software-hardware-requirements>
    Omnibus install </install/omnibus-install>
    Ubuntu install </install/ubuntu-install>
    Red Hat install </install/red-hat-install>
    Kubernetes install </install/kubernetes-install>
    Docker install </install/docker-install>
    AlmaLinux, Rocky Linux, and CentOS install </install/almalinux-rocky-linux-centos-install>

* :doc:`Software requirements </install/software-hardware-requirements>` - 
* :doc:`Omnibus install </install/omnibus-install>` - Install Mattermost Server using Omnibus.
* :doc:`Ubuntu install </install/ubuntu-install>` - Install Mattermost Server on Ubuntu.
* :doc:`Red Hat install </install/red-hat-install>` - Install Mattermost Server on Red Hat.
* :doc:`Kubernetes install </install/kubernetes-install>` - Install Mattermost Server using Kubernetes.
* :doc:`Docker install </install/docker-install>` - Install Mattermost Server using Docker.
* :doc:`AlmaLinux, Rocky Linux, and CentOS install </install/almalinux-rocky-linux-centos-install>` - Install Mattermost Server on AlmaLinux, Rocky Linux, or CentOS.

.. tip::

  * See the `configuration settings </configure/configuration-settings.html>`__ documentation to learn more about customizing your production deployment.
  * Encountering issues with your deployment? See the `Deployment Troubleshooting </install/troubleshooting.html#deployment-troubleshooting>`__ documentation for details.

Server administration
---------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    Deployment overview </deploy/deployment-overview>
    Architecture </getting-started/architecture-overview>
    Install a database </install/install-database>
    Set up a socket-based Mattermost database </install/setting-up-socket-based-mattermost-database>
    Include configuration in the Mattermost database </configure/configuation-in-a-database>
    Configure TLS on Mattermost Server </install/configure-tls>
    Install NGINX proxy server </install/install-nginx-proxy-server>
    SMTP email setup </configure/smtp-email>
    SSL client certificate setup </onboard/ssl-client-certificate>
    Set up an image proxy </deploy/image-proxy>
    Encryption options </deploy/encryption-options>
    Configure transport encryption </install/transport-encryption>
    Set up full-text Bleve search </deploy/bleve-search>
    Backup and disaster recovery </deploy/backup-disaster-recovery>

* :doc:`Deployment overview </deploy/deployment-overview>` - Learn about the Mattermost user experience, communication protocols, network access, data storage, and deployment options.
* :doc:`Architecture </getting-started/architecture-overview>` - Learn about user authentication, notifications, data management services, network connectivity, and high availability.
* :doc:`Install a database </install/install-database>` - Mattermost requires either a MySQL or PostgreSQL database.
* :doc:`Set up a socket-based Mattermost database </install/setting-up-socket-based-mattermost-database>` - Connect your Mattermost server to your database service.
* :doc:`Include configuration in the Mattermost database </configure/configuation-in-a-database>` - Store Mattermost configuration information in your database rather than as a JSON file. Recommended for High Availability environments.
* :doc:`Configure TLS on Mattermost Server </install/configure-tls>`
* :doc:`Install NGINX proxy server </install/install-nginx-proxy-server>`
* :doc:`SMTP email setup </configure/smtp-email>` - Connect to an email server to send emails for password resets and system notifications.
* :doc:`SSL client certificate setup </onboard/ssl-client-certificate>` - Configure SSL client certificates for Mattermost Desktop and Web Apps.
* :doc:`Set up an image proxy </deploy/image-proxy>` - Set up and configure an image proxy to make loading images faster and more reliable and prevent pixel tracking.
* :doc:`Encryption options </deploy/encryption-options>` - Set up encryption for data in transit and at rest.
* :doc:`Configure transport encryption </install/transport-encryption>` - Use transport encryption between Mattermost clusters and your proxy and database.
* :doc:`Set up full-text Bleve search </deploy/bleve-search>` - Use the Bleve search engine to provide Lucene-style full-text search.
* :doc:`Backup and disaster recovery </deploy/backup-disaster-recovery>` - Implement data backups, disaster recovery, and high availability deployment.





IGNORE Desktop and Mobile App installation

These guides will get you up and running with Mattermost desktop and mobile apps in minutes.

.. toctree::
    :maxdepth: 1
    :hidden:

    Desktop app install guides </install/desktop-app-install>
    iOS setup </install/install-ios-app>
    Android setup </install/install-android-app>
    Testing push notifications </deploy/mobile-testing-notifications>

* :doc:`Desktop app install guides </install/desktop-app-install>`
* :doc:`iOS setup </install/install-ios-app>`
* :doc:`Android setup </install/install-android-app>`
* :doc:`Testing push notifications </deploy/mobile-testing-notifications>`

IGNORE Deployment guide

The deployment guide is for administrators who are ready to integrate Mattermost with their organization’s IT infrastructure. 

IGNORE Server deployment

.. toctree::
    :titlesonly:
    :hidden:

    Deployment overview </deploy/deployment-overview>
    Set up a socket-based Mattermost database </install/setting-up-socket-based-mattermost-database>
    Image proxy </deploy/image-proxy>
    Backup and disaster recovery </deploy/backup-disaster-recovery>
    Encryption options </deploy/encryption-options>
    Configure transport encryption </install/transport-encryption>
    Bleve search </deploy/bleve-search>

* :doc:`Deployment overview </deploy/deployment-overview>` - Learn the basics of the Mattermost user experience, communication protocols, network access, data storage, and deployment options.
* :doc:`Set up a socket-based Mattermost database </install/setting-up-socket-based-mattermost-database>` - Connect your Mattermost server to your database service.
* :doc:`Image proxy </deploy/image-proxy>` - Setup and configure an image proxy to make loading images faster and more reliable and prevent pixel tracking.
* :doc:`Backup and disaster recovery </deploy/backup-disaster-recovery>` - Implement data backups, disaster recovery, and high availability deployment.
* :doc:`Encryption options </deploy/encryption-options>` - Setup encryption for data in transit and at rest.
* :doc:`Configure transport encryption </install/transport-encryption>` - Use transport encryption between Mattermost clusters and your proxy and database.
* :doc:`Bleve search </deploy/bleve-search>` - Use the Bleve search engine to provide Lucene-style full-text search.

IGNORE Desktop and Mobile App deployment

.. toctree::
    :maxdepth: 1
    :hidden:

    Desktop app deployment guide </deploy/desktop-app>
    Desktop MSI installer and group policy installation guides (beta) </install/desktop-msi-installer-and-group-policy-install>
    Desktop App custom dictionaries </install/desktop-custom-dictionaries>
    Desktop managed resources </install/desktop-app-managed-resources>
    Using Mattermost’s pre-built mobile apps </deploy/use-prebuilt-mobile-apps>
    Deploy Mattermost mobile apps </deploy/mobile-overview>
    Mobile push notifications </deploy/mobile-hpns>
    Building and distributing your own custom Mattermost mobile apps </deploy/build-custom-mobile-apps>
    Deploying mobile apps using an EMM provider </deploy/deploy-mobile-apps-using-emm-provider>
    AppConfig for EMM solutions with Mattermost Mobile Apps </deploy/mobile-appconfig> 
    Mobile VPN options </deploy/consider-mobile-vpn-options>
    Mobile apps FAQ </deploy/mobile-faq>
    Client-side data storage FAQ </deploy/client-side-data>

Customize the Mattermost desktop and mobile apps to meet any deployment needs.

**Desktop Apps**

* :doc:`Desktop app deployment guide </deploy/desktop-app>` - Customize and distribute the Mattermost desktop app with pre-configured settings.
* :doc:`Desktop MSI installer and group policy installation guides (beta) </install/desktop-msi-installer-and-group-policy-install>` - Use the Mattermost MSI installer and Group Policy definitions for Windows deployment.
* :doc:`Desktop app custom dictionaries </install/desktop-custom-dictionaries>` - Create custom dictionaries for Mattermost spellcheck.
* :doc:`Desktop managed resources </install/desktop-app-managed-resources>` - Configure resource management for services running on the same domain as your Mattermost instance.

**Mobile Apps**

* :doc:`Using Mattermost’s pre-built mobile apps </deploy/use-prebuilt-mobile-apps>` - Connect users to your Mattermost server with our prebuilt apps for Android and iOS.
* :doc:`Deploy Mattermost mobile apps </deploy/mobile-overview>` - Learn the basics of how to customize and deploy Mattermost to the Enterprise.
* :doc:`Mobile push notifications </deploy/mobile-hpns>` - Set up mobile push notifications. 
* :doc:`Building and distributing your own custom Mattermost mobile apps </deploy/build-custom-mobile-apps>` - Build custom mobile Mattermost apps.
* :doc:`Deploying mobile apps using an EMM provider </deploy/deploy-mobile-apps-using-emm-provider>` - Deploy with Enterprise Mobile Management software to enforce security policies and enforce specific versions of the Mattermost mobile apps.
* :doc:`AppConfig for EMM solutions with Mattermost mobile apps </deploy/mobile-appconfig>` - Learn how AppConfig provides an easy way to configure enterprise mobile applications.
* :doc:`Mobile VPN options </deploy/consider-mobile-vpn-options>` - Learn how to use the Mattermost mobile apps with Mobile VPNs.
* :doc:`Mobile apps frequently asked questions </deploy/mobile-faq>`
* :doc:`Client-side data storage frequently asked questions </deploy/client-side-data>`
