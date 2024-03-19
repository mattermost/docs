Configuring transport encryption
=================================

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

The components of the Mattermost setup are shown in the following diagram, including the transport encryption used. Aside from the encryption between the nodes of the Mattermost cluster, all transports rely on TLS encryption.

.. note::

  The transport between the Application servers is not used by default and requires additional setup steps. Enhancing the core product to include automatic encryption between cluster nodes is in progress and planned for a later release.

.. image:: ../images/transport-encryption.png
   :alt: Components of the Mattermost setup where all transports rely on TLS encryption.

The configuration guides are split up into the following documents:

.. toctree::
  :titlesonly:

  proxy-to-mattermost-transport-encryption.rst
  database-transport-encryption.rst
  cluster-transport-encryption.rst
