Install Mattermost Server
=========================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Learn how to install, deploy, and scale Mattermost for teams and organizations of any size.

Deploy Mattermost for production use
------------------------------------

Learn how to install, deploy, and scale Mattermost for teams and organizations of any size using one of four options: deploy using Kubernetes, deploy from a compressed tarball, deploy using a Ubuntu option called Omnibus, or deploy using Docker.

.. tip::

  * See the `configuration settings </configure/configuration-settings.html>`__ documentation to learn more about customizing your production deployment.
  
  * Encountering issues with your deployment? See the `Deployment Troubleshooting </install/troubleshooting.html#deployment-troubleshooting>`__ documentation for details.

.. tabs::

    .. tab:: Ubuntu/Debian

      .. include:: ../install/common-prod-deploy-omnibus.rst
        :start-after: :nosearch:
        
    .. tab:: Generic Linux (Tarball)

      .. include:: ../install/common-prod-deploy-tar.rst
        :start-after: :nosearch: 
        
    .. tab:: Kubernetes

      .. include:: ../install/common-prod-deploy-kubernetes.rst
        :start-after: :nosearch:
    
    .. tab:: Docker

      .. include:: ../install/common-prod-deploy-docker.rst
        :start-after: :nosearch:
    
Prepare for your Mattermost deployment
--------------------------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    Software requirements </install/server-requirements>
    Omnibus install </install/omnibus-install>
    Ubuntu install </install/ubuntu-install>
    Red Hat install </install/red-hat-install>
    Kubernetes install </install/kubernetes-install>
    Docker install </install/docker-install>
    AlmaLinux, Rocky Linux, and CentOS install </install/almalinux-rocky-linux-centos-install>

* :doc:`Software requirements </install/server-requirements>` - Learn what's required to deploy Mattermost Server and clients.
* :doc:`Omnibus install </install/omnibus-install>` - Install Mattermost Server using Omnibus.
* :doc:`Ubuntu install </install/ubuntu-install>` - Install Mattermost Server on Ubuntu.
* :doc:`Red Hat install </install/red-hat-install>` - Install Mattermost Server on Red Hat.
* :doc:`Kubernetes install </install/kubernetes-install>` - Install Mattermost Server using Kubernetes.
* :doc:`Docker install </install/docker-install>` - Install Mattermost Server using Docker.
* :doc:`AlmaLinux, Rocky Linux, and CentOS install </install/almalinux-rocky-linux-centos-install>` - Install Mattermost Server on AlmaLinux, Rocky Linux, or CentOS.

.. tip::

  * GitLab Mattermost deployment is `documented separately <https://docs.gitlab.com/omnibus/gitlab-mattermost/>`__ and not included on this site.
  * See the `configuration settings </configure/configuration-settings.html>`__ documentation to learn more about configuring your Mattermost instance.
  * Encountering issues with your deployment? See the `Deployment Troubleshooting </install/troubleshooting.html#deployment-troubleshooting>`__ documentation for details.