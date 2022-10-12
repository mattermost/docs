Deploy Mattermost
=================

.. toctree::
   :maxdepth: 2
   :hidden:

A complete Mattermost installation consists of three major components: a proxy server, a database server, and the Mattermost server. You can install all components on one machine, or you can install each component on its own machine. If you have only two machines, then install the proxy and the Mattermost server on one machine, and install the database on the other machine.

For the database, you can install either MySQL or PostgreSQL. The proxy is NGINX.

To install Mattermost server for production use, you can deploy using an RPM package, deploy using a DEB package, deploy from a compressed tarball, deploy using Kubernetes, or deploy using Docker.

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. tabs::

    .. tab:: RPM package

      .. include:: ../install/common-prod-deploy-omnibus.rst
        :start-after: :nosearch:
        
    .. tab:: DEB package

      Coming soon!
    
    .. tab:: Generic Linux (Tarball)

      .. include:: ../install/common-prod-deploy-tar.rst
        :start-after: :nosearch: 
        
    .. tab:: Kubernetes

      .. include:: ../install/common-prod-deploy-kubernetes.rst
        :start-after: :nosearch:
    
    .. tab:: Docker

      .. include:: ../install/common-prod-deploy-docker.rst
        :start-after: :nosearch:

    .. tab:: GitLab Helm Chart

      .. include:: ../install/installing-team-edition-helm-chart.rst
        :start-after: :nosearch:

.. tip::

  * See the MM Server configuration documentation for details on reqired configuration & setup.
  
  * See the `configuration settings <https://docs.mattermost.com/configure/configuration-settings.html>`__ documentation to learn more about customizing your production deployment.
  
  * Encountering issues with your deployment? See the `deployment troubleshooting <https://docs.mattermost.com/install/troubleshooting.html#deployment-troubleshooting>`__ documentation for details.