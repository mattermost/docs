Deploy Mattermost using Containers
==================================

You can deploy Mattermost Server using container technologies for exploring functionality, testing, and development purposes, as it allows you to quickly set up a Mattermost instance without needing to manage the underlying infrastructure. This deployment method shouldn't be used in production environments as it doesn't support clustered deployments or High Availability (HA) configurations out-of-the-box.

Choose your preferred container platform below for specific deployment instructions:

.. tab:: Docker

  .. include:: containers/install-docker.rst

.. tab:: AWS Elastic Beanstalk

  .. include:: containers/install-aws-beanstalk.rst