Deploy Mattermost using Containers
================================

Mattermost can be deployed using container technologies, providing flexibility and portability for your deployment. This guide covers deployment options using Docker and AWS Elastic Beanstalk.

.. important::

   Container deployments are recommended for professional deployments only, as they don't support High Availability (HA) configurations out of the box. For production environments requiring HA, consider using :doc:`Kubernetes </deploy/deploy-kubernetes>` or a :doc:`traditional Linux installation </deploy/deploy-linux>`.

Choose your preferred container platform below for specific deployment instructions:

.. tab:: Docker

  .. include:: containers/install-docker.rst

.. tab:: AWS Elastic Beanstalk

  .. include:: containers/install-aws-beanstalk.rst