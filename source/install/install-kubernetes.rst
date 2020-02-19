.. _install-kubernetes:

=========================================
Installing Mattermost on Kubernetes
=========================================

This document describes installing and deploying a production-ready Mattermost system on a Kubernetes cluster using the Mattermost Kubernetes operator.

An operator is a set of product- or application-specific instructions packaged into its own program. It tells an application what to run, where to find it,
and how to configure it. An operator can automate complex application deployment and operation
activities, such as installation, configuration changes, software updates, failure recovery, and more. The Mattermost operator does this by interacting with MySQL and MinIO operators.

Deploying the Mattermost Operator on Kubernetes is the recommended installation process. It provides a single common installation and management method
that can be implemented in practically any environment with less IT overhead and more automation.

Tasks such as zero-downtime upgrades, database restore, blue/green deployments, canary builds, and failure recovery are all managed by the Mattermost operator.

.. include:: install-kubernetes-cluster.rst
.. include:: install-kubernetes-operator.rst
.. include:: install-kubernetes-mattermost.rst
.. include:: use-kubernetes-mattermost.rst
.. include:: faq_kubernetes.rst
