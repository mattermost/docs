Prepare to deploy Mattermost Server
===================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Mattermost is an open core platform.

This means we develop both `an open source, self-hosted edition <https://docs.mattermost.com/about/editions-and-offerings.html#mattermost-team-edition>`__ of our software provided free to our community, as well as `a commercial edition <https://docs.mattermost.com/about/editions-and-offerings.html#mattermost-enterprise-edition>`__ that extends and enhances our open source software with paid, subscription-based offerings. Our open source edition and our subscription-based plans are available in self-hosted and cloud deployment modes.

On this page, you'll learn how to get started with a Mattermost self-hosted deployment.

Hardware considerations
-----------------------

See the `hardware requirements <https://docs.mattermost.com/install/software-hardware-requirements.html#hardware-requirements>`__ documentation for details on minimum requirements for up to 2000 users, as well as system, scale, and storage requirements for Enterprise deployments.

Deploy Mattermost
-----------------

Getting started with Mattermost is easy. You can `deploy a self-hosted instance of Mattermost <https://docs.mattermost.com/guides/deployment.html>`__ using Kubernetes, from a compressed tarball, using a Ubuntu option called Omnibus, or using Docker.  

Install a license key
---------------------

Mattermost self-hosted deployments require a license to be applied to access features in the Professional or Enterprise plans. Mattermost offers a `secure self-service Customer Portal <https://customers.mattermost.com/>`__ where you can easily purchase and manage your Mattermost self-hosted subscriptions. 

When you purchase a subscription or start a Mattermost Enterprise trial, a license is generated, and you'll receive that license key by email. You can apply that license key using the System Console, using mmctl, or using the CLI.

.. important:: 

    You must be a Mattermost System Admin to apply the license key to your Mattermost instance. If you're not a System Admin, contact your organization's Mattermost System Admin for assistance.

.. tabs::

    .. tab:: System Console

        1. Go go **System Console > About > Edition and License**.
        2. Upload your license key.

        Once the key is uploaded and installed, the details of your license are displayed.

    .. tab:: mmctl

        Use the `mmctl license upload <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-license-upload>`__ command to upload the license key, or to replace an existing license key with a new one. 

        .. code-block:: none

            mmctl license upload [license] [flags]

        When complete, restart the Mattermost server. If you're running in a `High Availability <https://docs.mattermost.com/scale/high-availability-cluster.html>`__ environment, the license key must be updated to every node.

    .. tab:: CLI

        .. note::

          The legacy `CLI <https://docs.mattermost.com/manage/command-line-tools.html>`__ is available for Mattermost v5.39 and earlier.

        Use the `mattermost license upload <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-license-upload>`__ command to to upload a new license key, or to replace an existing license key with a new one. 

        .. code-block:: none

            mattermost license upload {license}

        When complete, restart the Mattermost server. If you're running in a `High Availability <https://docs.mattermost.com/scale/high-availability-cluster.html>`__ environment, the new license key must be updated to every node.

Verify license keys
~~~~~~~~~~~~~~~~~~~

Once your license key is uploaded to your Mattermost server, it's stored in your SQL database at ``mattermost.Licenses``. Verify what keys are on your server by running the following command: 

.. code-block:: none

    select * from mattermost.Licenses;``

.. tip::

    Open the ``mattermost.log`` file which is typically located in the ``mattermost/logs/`` directory. Find the last occurrence of a log entry that starts with the text ``[INFO] License key``. If the license key is valid, the complete line should be similar to the following example:

    .. code-block:: text

        [2017/05/19 16:51:40 UTC] [INFO] License key valid unlocking enterprise features.

What's next?
------------

Now that you've considered your hardware needs, deployed a Mattermost self-hosted workspace, and installed a license key, you'll want to :doc:`review important notes for Mattermost System Admins </getting-started/get-started-system-admin-notes>` before learning how to :doc:`configure your Mattermost deployment </getting-started/get-started-configure>` for production use.