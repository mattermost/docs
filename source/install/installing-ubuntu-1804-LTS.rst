:orphan:

Install Mattermost on Ubuntu 18.04 LTS
=======================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Install a production-ready Mattermost system on 1 to 3 machines.

.. include:: install-common-intro.rst
  :start-after: :nosearch:

.. include:: install-ubuntu-1804-server.rst
  :start-after: :nosearch:

.. include:: install-ubuntu-1804-mysql.rst
  :start-after: :nosearch:

.. include:: install-ubuntu-1804-postgresql.rst
  :start-after: :nosearch:

.. include:: install-ubuntu-1804-mattermost.rst
  :start-after: :nosearch:

.. include:: config-mattermost-server.rst
  :start-after: :nosearch:



.. include:: install-nginx.rst
  :start-after: :nosearch:

.. include:: config-proxy-nginx.rst
  :start-after: :nosearch:

.. include:: config-ssl-http2-nginx.rst
  :start-after: :nosearch:
