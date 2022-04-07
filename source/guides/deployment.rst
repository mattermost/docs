Deploy Mattermost
=================

Learn how to install, deploy, and scale Mattermost for teams and organizations of any size.

Preview Mattermost using Docker
-------------------------------

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

You can install Mattermost server in **Preview Mode** using the `Mattermost Docker Preview Image <https://github.com/mattermost/mattermost-docker-preview>`__ image to explore Mattermost product functionality on a single local machine.

.. important::

    **Preview Mode** shouldn't be used in production, as it uses a known password string, contains other non-production configuration settings, has email disabled, keeps no persistent data (all data lives inside the container), and doesn't support upgrades. See the `Configuration Settings <https://docs.mattermost.com/configure/configuration-settings.html>`__ documentation to customize your preview deployment.

1. Install `Docker <https://www.docker.com/get-started/>`__.

2. After you install Docker, run the following command in a terminal window:

  .. code:: bash

    docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

3. When Docker is done fetching the image, navigate to ``http://localhost:8065/`` in your browser to preview Mattermost.

Deploy Mattermost for production use
------------------------------------

Encountering issues with your Docker deployment? See the `Deployment Troubleshooting <https://docs.mattermost.com/install/troubleshooting.html#deployment-troubleshooting>`__ documentation for details.

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

When you're ready to install Mattermost server for production use, you have three options: deploy from a compressed tarball, deploy using Omnibus, or deploy using Docker.

.. tabs::

    .. tab:: From Tar

        These instructions outline how to install Mattermost Server on a 64-bit Linux host from a compressed tarball, and assume the IP address of the Mattermost server is 10.10.10.2.

        1. Log in to the server that will host Mattermost Server and open a terminal window.

        2. Download `the latest version of the Mattermost Server <https://mattermost.com/deploy/>`__. In the following command, replace ``X.X.X`` with the version that you want to download:
  
          .. code:: bash

            wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz

        3. Extract the Mattermost Server files.
  
          .. code:: bash
            
            tar -xvzf mattermost*.gz

        4. Move the extracted file to the ``/opt`` directory.
  
          .. code:: bash
            
            sudo mv mattermost /opt

        5. Create the storage directory for files.
        
          .. code:: bash
            
            sudo mkdir /opt/mattermost/data
  
        .. note::
    
            The storage directory will contain all the files and images that your users post to Mattermost, so you need to make sure that the drive is large enough to hold the anticipated number of uploaded files and images.

        6. Set up a system user and group called ``mattermost`` that will run this service, and set the ownership and permissions.
  
          a. Create the Mattermost user and group.
        
            .. code:: bash

                sudo useradd --system --user-group mattermost
  
          b. Set the user and group *mattermost* as the owner of the Mattermost files.
    
            .. code:: bash
            
                sudo chown -R mattermost:mattermost /opt/mattermost
  
          c. Give write permissions to the *mattermost* group.
        
            .. code:: bash
            
                sudo chmod -R g+w /opt/mattermost

        7. Set up the database driver in the file ``/opt/mattermost/config/config.json``. Open the file in a text editor and make the following changes:
  
           **If you are using PostgreSQL:**

            Set ``"DriverName"`` to ``"postgres"``
            Set ``"DataSource"`` to the following value, replacing ``<mmuser-password>``  and ``<host-name-or-IP>`` with the appropriate values: ``"postgres://mmuser:<mmuser-password>@<host-name-or-IP>:5432/mattermost?sslmode=disable&connect_timeout=10",``
  
           **If you are using MySQL:**

            Set ``"DriverName"`` to ``"mysql"``
            Set ``"DataSource"`` to the following value, replacing ``<mmuser-password>``  and ``<host-name-or-IP>`` with the appropriate values. Also make sure that the database name is ``mattermost`` instead of ``mattermost_test``: ``"mmuser:<mmuser-password>@tcp(<host-name-or-IP>:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s"``

        8. Test the Mattermost server to make sure everything works.
    
          a. Change to the Mattermost directory.
            
            .. code:: bash
            
                cd /opt/mattermost
            
          b. Start the Mattermost server as the user mattermost.
            
            .. code:: bash
            
                sudo -u mattermost bin/mattermost
  
        When the server starts, it shows some log information and the text ``Server is listening on :8065``. You can stop the server by pressing CTRL+C in the terminal window.

        9. Set up Mattermost to use *systemd* for starting and stopping.
  
          a. Create a *systemd* unit file.
    
            .. code:: bash
            
                sudo touch /lib/systemd/system/mattermost.service
  
          b. Open the unit file as root in a text editor, and copy the following lines into the file.
  
            .. code-block:: none

                [Unit]
                Description=Mattermost
                After=network.target
                After=postgresql.service
                BindsTo=postgresql.service
                [Service]
                Type=notify
                ExecStart=/opt/mattermost/bin/mattermost
                TimeoutStartSec=3600
                KillMode=mixed
                Restart=always
                RestartSec=10
                WorkingDirectory=/opt/mattermost
                User=mattermost
                Group=mattermost
                LimitNOFILE=49152
                [Install]
                WantedBy=multi-user.target
  
            .. note::
    
                * If you are using MySQL, replace ``postgresql.service`` with ``mysql.service`` in 2 places in the ``[Unit]`` section.
                * If you have installed MySQL or PostgreSQL on a dedicated server, you need to remove the ``After=mysql.service`` and ``BindsTo=mysql.service`` or the ``After=postgresql.service`` and ``BindsTo=postgresql.service`` lines in the ``[Unit]`` section or the Mattermost service won't start.
    
          c. Make systemd load the new unit.
    
            .. code:: bash
            
                sudo systemctl daemon-reload
  
          d. Check to make sure that the unit was loaded.
    
            .. code:: bash
            
                sudo systemctl status mattermost.service
    
          You should see an output similar to the following:
    
          .. code-block:: none
                
            mattermost.service - Mattermost
            Loaded: loaded (/lib/systemd/system/mattermost.service; disabled; vendor preset: enabled)
            Active: inactive (dead)
  
          e. Start the service.
    
            .. code:: bash
            
                sudo systemctl start mattermost.service
  
          f. Verify that Mattermost is running.
    
            .. code:: bash
            
                curl http://localhost:8065
    
            You should see the HTML that's returned by the Mattermost server. Note: in case firewall is used, external requests to port 8065 may be blocked. Use ``sudo ufw allow 8065`` to open port 8065.
  
          g. Set Mattermost to start on machine start up.

            .. code:: bash
            
                sudo systemctl enable mattermost.service

        Once you're Mattermost server is up and running, create your first Mattermost user, `invite more users <https://docs.mattermost.com/channels/manage-channel-members.html>`__, and explore the Mattermost platform. See the `Configuration Settings <https://docs.mattermost.com/configure/configuration-settings.html>`__ documentation to customize your production deployment.
        
    .. tab:: Using Omnibus

        Mattermost Omnibus is a `Debian <https://www.debian.org/>`__ package that bundles the  components of a Mattermost deployment into a single installation. The package leverages the `apt package manager <https://ubuntu.com/server/docs/package-management>`__ to install and update the platform components, and uses a custom CLI and ansible recipes to link the components together and configure them.

        Mattermost Omnibus currently supports Ubuntu's ``bionic`` and ``focal`` distributions. The package bundles the free, unlicensed Mattermost Enterprise version of Mattermost.

        1. In a terminal window, run the following command to configure the repositories needed for a PostgreSQL database, configure an NGINX web server to act as a proxy, configure certbot to issue and renew the SSL certificate, and configure the Mattermost Omnibus repository so that you can run the install command.

          .. code-block:: none

            curl -o- https://deb.packages.mattermost.com/repo-setup.sh | sudo bash

        2. Install the Omnibus package.

          .. code-block:: none

            sudo apt install mattermost-omnibus -y

        To issue the certificate, the installer requests a domain name and an email address from you. These are used to generate the certificate and deliver any related communications. After all the packages are installed, Omnibus runs ansible scripts that configure all the platform components and starts the server. 

        3. Open a browser, navigate to your Mattermost domain by domain name (e.g. ``mymattermostserver.com``), or by the server's IP address if you're not using a domain name. 

        4. Create your first Mattermost user, `invite more users <https://docs.mattermost.com/channels/manage-channel-members.html>`__, and explore the Mattermost platform. 

        .. note:: 

            We recommend installing and configuring Omnibus with SSL enabled; however, you can run the following command to disable SSL: ``sudo MMO_HTTPS=false apt install mattermost-omnibus``.

        **Update Mattermost Omnibus**

        Mattermost Omnibus is integrated with the apt package manager. When a new Mattermost version is released, run: ``sudo apt update && sudo apt upgrade`` to download and update your Mattermost instance.
    
    .. tab:: Using Docker

      You'll need `Docker Engine <https://docs.docker.com/engine/install/>`__ and `Docker Compose <https://docs.docker.com/compose/install/>`__ (release 1.28 or later) Follow the steps in the `Mattermost Docker Setup README <https://github.com/mattermost/docker#mattermost-docker-setup>`__ or follow the steps below.
      
      1. In a terminal window, clone the repository and enter the directory.

        .. code:: bash
        
            git clone https://github.com/mattermost/docker
            cd docker

      2. Create your ``.env`` file by copying and adjusting the ``env.example`` file.

        .. code:: bash
        
            cp env.example .env

        .. important::
    
            At a minimum, you must edit the ``DOMAIN`` value in the ``.env`` file to correspond to the domain for your Mattermost server.

      3. Create the required directories and set their permissions.

        .. code:: bash
        
            mkdir -p ./volumes/app/mattermost/{config,data,logs,plugins,client/plugins,bleve-indexes}
            sudo chown -R 2000:2000 ./volumes/app/mattermost

      4. Configure TLS for NGINX *(optional)*. If you're not using the included NGINX reverse proxy, you can skip this step.

          **If creating a new certificate and key:**

          .. code:: bash
  
                bash scripts/issue-certificate.sh -d <YOUR_MM_DOMAIN> -o ${PWD}/certs

          To include the certificate and key, uncomment the following lines in your ``.env`` file and ensure they point to the appropriate files.

          .. code:: bash
  
                #CERT_PATH=./certs/etc/letsencrypt/live/${DOMAIN}/fullchain.pem
                #KEY_PATH=./certs/etc/letsencrypt/live/${DOMAIN}/privkey.pem

          **If using a pre-existing certificate and key:**

          .. code:: bash
  
                mkdir -p ./volumes/web/cert
                cp <PATH-TO-PRE-EXISTING-CERT>.pem ./volumes/web/cert/cert.pem
                cp <PATH-TO-PRE-EXISTING-KEY>.pem ./volumes/web/cert/key-no-password.pem

          To include the certificate and key, ensure the following lines in your ``.env`` file points to the appropriate files.

          .. code:: bash
  
                CERT_PATH=./volumes/web/cert/cert.pem
                KEY_PATH=./volumes/web/cert/key-no-password.pem

      5. Configure SSO with GitLab *(optional)*. If you want to use SSO with GitLab, and you're using a self-signed certificate, you have to add the PKI chain for your authority. This is required to avoid the ``Token request failed: certificate signed by unknown authority`` error.
      
            To add the PKI chain, uncomment this line in your ``.env`` file, and ensure it points to your ``pki_chain.pem`` file:

            .. code:: bash
  
                S#GITLAB_PKI_CHAIN_PATH=<path_to_your_gitlab_pki>/pki_chain.pem
        
            Then uncomment this line in your ``docker-compose.yml`` file, and ensure it points to the same ``pki_chain.pem`` file:

            .. code:: bash

                # - ${GITLAB_PKI_CHAIN_PATH}:/etc/ssl/certs/pki_chain.pem:ro

      6. Deploy Mattermost.

          **Without using the included NGINX:**

          .. code:: bash
  
                sudo docker-compose -f docker-compose.yml -f docker-compose.without-nginx.yml up -d

          To access your new Mattermost deploy, navigate to ``http://<YOUR_MM_DOMAIN>:8065/`` in your browser.

          To shut down your deployment:

          .. code:: bash
  
                sudo docker-compose -f docker-compose.yml -f docker-compose.without-nginx.yml down

          **Using the included NGINX:**

          .. code:: bash
  
                sudo docker-compose -f docker-compose.yml -f docker-compose.nginx.yml up -d

          To access your new Mattermost deployment via HTTPS, navigate to ``https://<YOUR_MM_DOMAIN>/`` in your browser.

          To shut down your deployment:

          .. code:: bash
  
                sudo docker-compose -f docker-compose.yml -f docker-compose.nginx.yml down
      
      7. Create your first Mattermost System Admin user, `invite more users <https://docs.mattermost.com/channels/manage-channel-members.html>`__, and explore the Mattermost platform. 

Prepare for your Mattermost deployment
--------------------------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    Administrator tasks </getting-started/admin-onboarding-tasks>
    Architecture </getting-started/architecture-overview>
    Implement Mattermost </getting-started/implementation-plan>
    Enterprise roll out checklist </getting-started/enterprise-roll-out-checklist>
    Welcome email template </getting-started/welcome-email-to-end-users>

These guides will help you prepare for your Mattermost deployment.

* :doc:`Administrator tasks </getting-started/admin-onboarding-tasks>` - Learn about the standard configurations and settings you’ll encounter.
* :doc:`Architecture </getting-started/architecture-overview>` - Learn the basics of user authentication, notifications, data management services, network connectivity, and high availability.
* :doc:`Implement Mattermost </getting-started/implementation-plan>` - Get a detailed breakdown of the technical requirements to deploy Mattermost for your team or organization.
* :doc:`Enterprise roll out checklist </getting-started/enterprise-roll-out-checklist>` - Learn how to roll Mattermost out to thousands of users.
* :doc:`Welcome email template </getting-started/welcome-email-to-end-users>` - Use our sample email template when you’re ready to invite users to your server.

Install guides
--------------

The Mattermost server and client apps can run on all of the most popular platforms. Here’s a list of the most popular installation methods.

Server installation
^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Software and hardware requirements </install/software-hardware-requirements>
    Local Docker setup </install/setting-up-local-machine-using-docker>
    Mattermost Omnibus </install/installing-mattermost-omnibus>
    Ubuntu 20.04 LTS </install/installing-ubuntu-2004-LTS>
    Kubernetes </install/install-kubernetes>
    Debian Buster </install/install-debian>
    RHEL 8 </install/install-rhel-8>
    CentOS, Oracle Linux, and Scientific Linux </install/install-centos-oracle-scientific>


* :doc:`Software and hardware requirements </install/software-hardware-requirements>`
* :doc:`Local Docker setup </install/setting-up-local-machine-using-docker>`
* :doc:`Mattermost Omnibus </install/installing-mattermost-omnibus>`
* :doc:`Ubuntu 20.04 LTS </install/installing-ubuntu-2004-LTS>`
* :doc:`Kubernetes </install/install-kubernetes>`
* :doc:`Debian Buster </install/install-debian>`
* :doc:`RHEL 8 </install/install-rhel-8>`
* :doc:`CentOS, Oracle Linux, and Scientific Linux </install/install-centos-oracle-scientific>`
* `More server install guides <https://docs.mattermost.com/guides/deployment.html#other-resources>`__

Desktop and Mobile App installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These guides will get you up and running with Mattermost desktop and mobile apps in minutes.

.. toctree::
    :maxdepth: 1
    :hidden:

    Install the Mattermost Desktop App </install/installing-mattermost-desktop-app>
    Desktop App install guides </install/desktop-app-install>
    iOS setup </install/install-ios-app>
    Android setup </install/install-android-app>
    Testing push notifications </deploy/mobile-testing-notifications>

* :doc:`Install the Mattermost Desktop App </install/installing-mattermost-desktop-app>`
* :doc:`Desktop App install guides </install/desktop-app-install>`
* :doc:`iOS setup </install/install-ios-app>`
* :doc:`Android setup </install/install-android-app>`
* :doc:`Testing push notifications </deploy/mobile-testing-notifications>`

Deployment guide
----------------

The deployment guide is for administrators who are ready to integrate Mattermost with their organization’s IT infrastructure. 

Server deployment
^^^^^^^^^^^^^^^^^
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

Desktop and Mobile App deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Desktop App deployment guide </deploy/desktop-app>
    Desktop MSI installer and group policy installation guides (beta) </install/desktop-msi-installer-and-group-policy-install>
    Desktop App custom dictionaries </install/desktop-custom-dictionaries>
    Desktop managed resources </install/desktop-app-managed-resources>
    Using Mattermost’s pre-built Mobile Apps </deploy/use-prebuilt-mobile-apps>
    Deploy Mattermost Mobile Apps </deploy/mobile-overview>
    Mobile push notifications </deploy/mobile-hpns>
    Building and distributing your own custom Mattermost mobile apps </deploy/build-custom-mobile-apps>
    Deploying mobile apps using an EMM provider </deploy/deploy-mobile-apps-using-emm-provider>
    AppConfig for EMM solutions with Mattermost Mobile Apps </deploy/mobile-appconfig> 
    Mobile VPN options </deploy/consider-mobile-vpn-options>
    Mobile Apps FAQ </deploy/mobile-faq>
    Client-side data storage FAQ </deploy/client-side-data>

Customize the Mattermost desktop and mobile apps to meet any deployment needs.

**Desktop Apps**

* :doc:`Desktop App deployment guide </deploy/desktop-app>` - Customize and distribute the Mattermost desktop app with pre-configured settings.
* :doc:`Desktop MSI installer and group policy installation guides (beta) </install/desktop-msi-installer-and-group-policy-install>` - Use the Mattermost MSI installer and Group Policy definitions for Windows deployment.
* :doc:`Desktop App custom dictionaries </install/desktop-custom-dictionaries>` - Create custom dictionaries for Mattermost spellcheck.
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

Upgrade Mattermost
------------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Upgrade Mattermost Server </upgrade/upgrading-mattermost-server>
    Enterprise install and upgrade </install/enterprise-install-upgrade>
    Install a license key </upgrade/installing-license-key>
    Release definitions </upgrade/release-definitions>
    Important upgrade notes </upgrade/important-upgrade-notes>
    Release lifecycle </upgrade/release-lifecycle>
    Extended Support Release </upgrade/extended-support-release>
    Downgrade Mattermost Server </upgrade/downgrading-mattermost-server>
    Version archive </upgrade/version-archive>

Stay up to date with the latest features and improvements.

* :doc:`Upgrade Mattermost Server </upgrade/upgrading-mattermost-server>` - Learn the basics of upgrading your Mattermost server to the latest version.
* :doc:`Enterprise install and upgrade </install/enterprise-install-upgrade>` - Learn how to upgrade your Mattermost server to premium versions.
* :doc:`Install a license key </upgrade/installing-license-key>` - Learn how to add or change a Mattermost license key.
* :doc:`Release definitions </upgrade/release-definitions>` - Get details on the Mattermost release schedule and the types of releases.
* :doc:`Important upgrade notes </upgrade/important-upgrade-notes>` - Find version-specific upgrade considerations.
* :doc:`Release lifecycle </upgrade/release-lifecycle>` - See critical release lifecycle dates.
* :doc:`Extended Support Release </upgrade/extended-support-release>` - Get information about releases that have extended release support.
* :doc:`Downgrade Mattermost Server </upgrade/downgrading-mattermost-server>` - Find out how to roll back to older versions of Mattermost.
* :doc:`Version archive </upgrade/version-archive>` - Download binaries for every release.

Scale Mattermost
----------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Scale for Enterprise </scale/scaling-for-enterprise>
    High Availability cluster </scale/high-availability-cluster>
    Elasticsearch </scale/elasticsearch>
    Performance monitoring </scale/performance-monitoring>
    Mattermost performance alerting guide </scale/performance-alerting>

Scale and monitor your Mattermost deployment.

* :doc:`Scale for Enterprise </scale/scaling-for-enterprise>` - Scale Mattermost to tens of thousands of users and beyond.
* :doc:`High Availability cluster </scale/high-availability-cluster>` - Maintain Mattermost service during outages and hardware failures with redundant infrastructure.
* :doc:`Elasticsearch </scale/elasticsearch>` - Enhance search performance with Elasticsearch.
* :doc:`Performance monitoring </scale/performance-monitoring>` - Use Prometheus and Grafana to monitor the health and performance of your Mattermost cluster.
* :doc:`Mattermost performance alerting guide </scale/performance-alerting>` - Learn strategies and best practices for monitoring your Mattermost cluster. 

Troubleshooting guides
----------------------
.. toctree::
    :maxdepth: 1
    :hidden:

    General troubleshooting </install/troubleshooting>
    Troubleshooting mobile applications </deploy/mobile-troubleshoot>
    MySQL installation troubleshooting </install/trouble_mysql>

* :doc:`General troubleshooting </install/troubleshooting>`
* :doc:`Troubleshooting mobile applications </deploy/mobile-troubleshoot>`
* :doc:`MySQL installation troubleshooting </install/trouble_mysql>`

Changelogs
----------
.. toctree::
    :maxdepth: 1
    :hidden:

    Mattermost self-hosted </install/self-managed-changelog>
    Mattermost legacy self-hosted </install/legacy-self-hosted-changelog>
    Mattermost Cloud </install/cloud-changelog>
    Mobile Apps </deploy/mobile-app-changelog>
    Desktop Apps </install/desktop-app-changelog>
    Deprecated features </install/deprecated-features>

* :doc:`Mattermost self-hosted </install/self-managed-changelog>`
* :doc:`Mattermost legacy self-hosted </install/legacy-self-hosted-changelog>`
* :doc:`Mattermost Cloud </install/cloud-changelog>`
* :doc:`Mobile Apps </deploy/mobile-app-changelog>`
* :doc:`Desktop Apps </install/desktop-app-changelog>`
* :doc:`Deprecated features </install/deprecated-features>`

Additional server install guides
--------------------------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Install on Ubuntu 18.04 LTS </install/installing-ubuntu-1804-LTS>
    Install on RHEL 7 </install/install-rhel-7>
    Deploy Mattermost on Bitnami </install/deploying-team-edition-on-bitnami>
    AWS Elastic Beanstalk Docker setup </install/setting-up-aws-elastic-beanstalk-docker>
    Install Mattermost Team Edition in GitLab Helm Chart </install/installing-team-edition-helm-chart>
    Open source components </upgrade/open-source-components>

* :doc:`Install on Ubuntu 18.04 LTS </install/installing-ubuntu-1804-LTS>`
* :doc:`Install on RHEL 7 </install/install-rhel-7>`
* :doc:`Deploy Mattermost on Bitnami </install/deploying-team-edition-on-bitnami>`
* :doc:`AWS Elastic Beanstalk Docker setup </install/setting-up-aws-elastic-beanstalk-docker>`
* :doc:`Install on GitLab Helm Chart </install/installing-team-edition-helm-chart>`
* :doc:`Open source components </upgrade/open-source-components>`
