Deploy Mattermost in Air-Gapped Environments
==============================================

This guide outlines how to deploy Mattermost in a self-hosted air-gapped environment, focusing on setting up the supporting infrastructure required for a successful deployment. An air-gapped environment is one that is isolated from the public internet, requiring all necessary components to be available locally.

Deploying Mattermost in an air-gapped environment involves detailed preparation to ensure uninterrupted availability of critical components within the network. These efforts mitigate risks associated with the lack of internet connectivity by ensuring access to secure, localized resources. Key considerations include:

- Container images required when deploying in Kubernetes or Docker.
- Mattermost server packages and dependencies required when deploying directly on Linux servers.
- Access to a PostgreSQL database.
- Object storage or a shared filesystem service for relaibly accessing files from multiple Mattermost servers.
- Other supporting services such as LDAP for authentication, Elasticsearch for performant post searching, etc. as required for your scale and performance requirements.

Refer to Mattermost deployment documentation for setting up Mattermost as needed. This guide focuses on the supporting infrastructure needed for an air-gapped deployment which is required before deploying Mattermost in these environments.

Set up a self-hosted private container registry
--------------------------------------------------

A private container registry securely stores Docker images for air-gapped deployments, ensuring compliance with data isolation requirements. Use it to enable local deployments in Kubernetes or Docker.

The process for uploading images to the registry will need to be tailored to the security policies of the air-gapped network. For example, perhaps the registry is allowed to pull images from the public internet. If not, images will have to be uploaded to the registry from a machine that has access to the public internet.

Ideally the air-gapped network already has a private registry available. If not, you can set up a private registry using Docker Registry or Harbor.

.. tab:: Docker registry

   1. **Install Docker Registry**:

      .. code-block:: bash

         docker run -d -p 5000:5000 --restart=always --name registry registry:2

   2. **Configure persistent storage**:

      .. code-block:: bash

         docker run -d -p 5000:5000 --restart=always --name registry \
         -v /mnt/registry:/var/lib/registry \
         registry:2

   3. **Add TLS security** (recommended):

      a. Generate self-signed certificates:

         .. code-block:: bash

            mkdir -p certs
            openssl req -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key \
            -x509 -days 365 -out certs/domain.crt

      b. Run the registry with TLS:

         .. code-block:: bash

            docker run -d -p 5000:5000 --restart=always --name registry \
            -v /mnt/registry:/var/lib/registry \
            -v $(pwd)/certs:/certs \
            -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
            -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
            registry:2

.. tab:: Harbor registry

   For more advanced features, consider using `Harbor <https://github.com/goharbor/harbor>`_.

   1. **Download Harbor offline installer** before going air-gapped:
      
      Download from https://github.com/goharbor/harbor/releases

   2. **Extract and configure**:

      .. code-block:: bash

         tar xzvf harbor-offline-installer-v2.x.x.tgz
         cd harbor
         cp harbor.yml.tmpl harbor.yml
         # Edit harbor.yml to configure settings

   3. **Install Harbor**:

      .. code-block:: bash

         ./install.sh --with-trivy

   4. **Access Harbor** at ``https://harbor-hostname`` (based on your configuration)

Populate your private registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the private registry cannot access the public internet, retrieve images on an external machine and securely transfer them using approved data transfer methods.

.. code-block:: bash

   # Pull the required Mattermost images
   docker pull mattermost/mattermost-enterprise-edition:latest
   
   # Tag the images for your private registry
   docker tag mattermost/mattermost-enterprise-edition:latest registry.example.com:5000/mattermost/mattermost-enterprise-edition:latest
   
   # Push to your private registry
   docker push registry.example.com:5000/mattermost/mattermost-enterprise-edition:latest

Configure Kubernetes to use private image registries
-----------------------------------------------------

When using Kubernetes in an air-gapped environment, you need to configure it to use your private registry.

Create registry credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Create a kubernetes secret for registry authentication**:

   .. code-block:: bash

      kubectl create secret docker-registry regcred \
        --docker-server=registry.example.com:5000 \
        --docker-username=your_username \
        --docker-password=your_password \
        --docker-email=your_email@example.com

2. **Reference the secret in pod specifications**:

   .. code-block:: yaml

      apiVersion: v1
      kind: Pod
      metadata:
        name: mattermost-pod
      spec:
        containers:
        - name: mattermost
          image: registry.example.com:5000/mattermost/mattermost-enterprise-edition:latest
        imagePullSecrets:
        - name: regcred

3. **For Helm deployments**, specify the registry in ``values.yaml``:

   .. code-block:: yaml

      image:
        repository: registry.example.com:5000/mattermost/mattermost-enterprise-edition
        tag: latest
        pullPolicy: IfNotPresent
      
      imagePullSecrets:
        - name: regcred

Configure Docker to use private image registries
-------------------------------------------------

Configure Docker on all hosts to trust and use your private registry.

Docker daemon configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Add your registry to Docker's trusted registries**:

   Edit or create ``/etc/docker/daemon.json``:

   .. code-block:: json

      {
        "insecure-registries": ["registry.example.com:5000"]
      }

   For registries using self-signed certificates:

   .. code-block:: bash

      mkdir -p /etc/docker/certs.d/registry.example.com:5000
      cp domain.crt /etc/docker/certs.d/registry.example.com:5000/ca.crt

2. **Restart Docker daemon**:

   .. code-block:: bash

      systemctl restart docker

3. **Test the configuration**:

   .. code-block:: bash

      docker pull registry.example.com:5000/mattermost/mattermost-enterprise-edition:latest

Set up a private Debian package mirror
-----------------------------------------

A local Debian mirror allows you to maintain packages for system updates and dependencies. In this case, the mirror will be used to provide packages for Mattermost server to debian-based hosts.

Ideally the air-gapped network already has a local mirror available. If not, you can set up a local mirror such as Aptly or debmirror.

.. tab:: Use Aptly

   1. **Install Aptly** (on an internet-connected machine):

      .. code-block:: bash

         apt-get update
         apt-get install aptly gnupg

   2. **Create GPG key for signing packages**:

      .. code-block:: bash

         gpg --gen-key

   3. **Create a mirror configuration**:

      .. code-block:: bash

         aptly mirror create -architectures=amd64 debian-bullseye http://deb.debian.org/debian bullseye main contrib non-free

   4. **Update the mirror to download packages**:

      .. code-block:: bash

         aptly mirror update debian-bullseye

   5. **Create and publish a snapshot**:

      .. code-block:: bash

         aptly snapshot create debian-bullseye-$(date +%Y%m%d) from mirror debian-bullseye
         aptly publish snapshot debian-bullseye-$(date +%Y%m%d)

   6. **Serve the repository**:

      .. code-block:: bash

         aptly serve

.. tab:: Use debmirror

   For a simpler approach:

   1. **Install debmirror**:

      .. code-block:: bash

         apt-get install debmirror

   2. **Create a mirror script**:

      .. code-block:: bash

         #!/bin/bash
         debmirror --host=deb.debian.org \
                  --root=/debian \
                  --method=http \
                  --dist=bullseye \
                  --section=main,contrib,non-free \
                  --arch=amd64 \
                  --nosource \
                  --progress \
                  --ignore-release-gpg \
                  /path/to/mirror/debian

   3. **Set up a web server** (like nginx) to serve the mirror:

      .. code-block:: bash

         apt-get install nginx
         
         # Create nginx configuration
         cat > /etc/nginx/sites-available/debian-mirror << EOF
         server {
            listen 80;
            server_name mirror.example.com;
            root /path/to/mirror;
            autoindex on;
         }
         EOF
         
         ln -s /etc/nginx/sites-available/debian-mirror /etc/nginx/sites-enabled/
         systemctl restart nginx

Client configuration
~~~~~~~~~~~~~~~~~~~~~

On air-gapped systems, configure apt to use your local mirror:

.. code-block:: bash

   cat > /etc/apt/sources.list << EOF
   deb http://mirror.example.com/debian bullseye main contrib non-free
   EOF

Set up a private RHEL package mirror
---------------------------------------

For Red Hat Enterprise Linux environments, you'll need a local repository mirror.

Ideally the air-gapped network already has a local mirror available. If not, you can set up a local mirror such as reposync.

Use reposync
~~~~~~~~~~~~~

1. **Install required tools** (on an internet-connected RHEL system):

   .. code-block:: bash

      yum install yum-utils createrepo

2. **Download packages**:

   .. code-block:: bash

      mkdir -p /var/www/html/repos/rhel8
      reposync -p /var/www/html/repos/rhel8 --download-metadata --repo=rhel-8-for-x86_64-baseos-rpms
      reposync -p /var/www/html/repos/rhel8 --download-metadata --repo=rhel-8-for-x86_64-appstream-rpms

3. **Create repository metadata**:

   .. code-block:: bash

      createrepo /var/www/html/repos/rhel8/rhel-8-for-x86_64-baseos-rpms
      createrepo /var/www/html/repos/rhel8/rhel-8-for-x86_64-appstream-rpms

4. **Set up a web server**:

   .. code-block:: bash

      yum install httpd
      systemctl enable httpd
      systemctl start httpd

Client configuration
~~~~~~~~~~~~~~~~~~~~~~

On air-gapped RHEL systems:

1. **Disable existing repositories**:

   .. code-block:: bash

      cd /etc/yum.repos.d/
      mkdir backup
      mv *.repo backup/

2. **Create new repository files**:

   .. code-block:: bash

      cat > /etc/yum.repos.d/local-baseos.repo << EOF
      [local-baseos]
      name=Red Hat Enterprise Linux 8 BaseOS
      baseurl=http://mirror.example.com/repos/rhel8/rhel-8-for-x86_64-baseos-rpms
      enabled=1
      gpgcheck=0
      EOF
      
      cat > /etc/yum.repos.d/local-appstream.repo << EOF
      [local-appstream]
      name=Red Hat Enterprise Linux 8 AppStream
      baseurl=http://mirror.example.com/repos/rhel8/rhel-8-for-x86_64-appstream-rpms
      enabled=1
      gpgcheck=0
      EOF

3. **Clear cache and test**:

   .. code-block:: bash

      yum clean all
      yum repolist

Mattermost server configuration for air-gapped deployments
-----------------------------------------------------------

When deploying Mattermost in an air-gapped environment, there are configuration options available to accommodate the lack of internet access. The following covers these configuration options and offers recommendations for settings.

Mobile push notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost can use mobile push notifications to notify users of new messages and activity. These notifications require a server component to be deployed to send the notifications to the mobile devices. By default, Mattermost will use the public push notification service which is not available in an air-gapped environment. We recommend :ref:`disabling push notifications <configure/environment-configuration-settings:enable push notifications>` in **System Console > Environment > Push Notification Server**.

Website link previews
~~~~~~~~~~~~~~~~~~~~~~~

Website link previews require a connection to the internet to fetch the content of the links. We recommend :ref:`disabling website link previews <configure/site-configuration-settings:enable website link previews>` in **System Console > Site Configuration > Posts**.

Additional considerations
---------------------------

Remember that air-gapped environments require ongoing maintenance to stay secure and up-to-date. Regular updates to the Mattermost server and other components are required to ensure the environment remains secure and up-to-date.

Network security
~~~~~~~~~~~~~~~~~

In air-gapped environments, network security is critical:

1. **Implement strict firewall rules** to control traffic between network segments.
2. **Use network segmentation** to isolate critical infrastructure components.
3. **Regularly audit network access** to ensure the environment remains properly isolated.

Transfer data to air-gapped networks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For initial setup and updates:

1. **Use approved data diodes** or one-way transfer devices.
2. **Implement strict media control** for any physical media entering the air-gapped environment.
3. **Scan all incoming data** for malware before allowing it into the environment.

Keep systems updated
~~~~~~~~~~~~~~~~~~~~~~

Develop a process for regular updates:

1. **Schedule periodic updates** to your local mirrors.
2. **Maintain a consistent testing process** for all updates before deployment.
3. **Keep comprehensive documentation** of all packages and versions in use.

Monitoring and logging
~~~~~~~~~~~~~~~~~~~~~~~

Ensure robust monitoring within the air-gapped environment:

1. **Deploy local monitoring solutions** that don't require internet access.
2. **Establish baselines** for normal system behavior.
3. **Implement centralized logging** for security analysis and troubleshooting.