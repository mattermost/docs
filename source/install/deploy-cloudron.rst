:orphan:

.. _deploy-cloudron:

Deploy Mattermost on Cloudron (Unofficial)
==========================================

Unofficial, community-maintained guides for deploying Mattermost on Cloudron.

.. important:: This unofficial guide is maintained by the Mattermost community and this deployment configuration is not yet officially supported by Mattermost, Inc. You can `edit this page on GitHub <https://github.com/mattermost/docs/blob/master/source/install/deploy-cloudron.rst>`__.

Mattermost is available as a 1-click install on `Cloudron <https://cloudron.io>`__. For those unaware,
Cloudron makes it easy to run apps like Mattermost on your server and keep them up-to-date and secure.

.. image:: https://cloudron.io/img/button.svg
   :target: https://cloudron.io/button.html?app=org.mattermost.cloudronapp

Installation
------------

To get started, first `install Cloudron <https://cloudron.io/get.html>`__ on a VPS provider like Digital Ocean
and then install Mattermost from the `Cloudron Store <https://cloudron.io/store/org.mattermost.cloudronapp.html>`__.

The Mattermost app will be configured with MySQL and SMTP email notifications service.

Demo
----

A demo is available `here <https://my.demo.cloudron.io>`__ (username: ``cloudron``, password: ``cloudron``).

Package Source
--------------

The Cloudron package (with automated tests) is developed `here <https://git.cloudron.io/cloudron/mattermost-app>`__.
