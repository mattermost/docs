.. _deploy-cloudron:

Deploy Mattermost on Cloudron
=============================

Mattermost is available as a 1-click install on `Cloudron <https://cloudron.io>`_. For those unaware,
Cloudron makes it easy to run apps like Mattermost on your server and keep them up-to-date and secure.

.. image:: https://cloudron.io/img/button.svg
   :target: https://cloudron.io/button.html?app=org.mattermost.cloudronapp

Installation
============

To get started, first `install Cloudron <https://cloudron.io/get.html>`_ on a VPS provider like Digital Ocean
and then install Mattermost from the `Cloudron Store <https://cloudron.io/store/org.mattermost.cloudronapp.html>`_.

The Mattermost app will be already setup to use MySQL. Email sending should also work out of the box.

Demo
====

There is a `demo available <https://my-demo.cloudron.me>`_ (username: cloudron password: cloudron)

Package Source
==============

The Cloudron package (with automated tests) is developed `here <https://git.cloudron.io/cloudron/mattermost-app>`_.

