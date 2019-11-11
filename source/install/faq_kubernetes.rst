.. _faq_kubernetes:

Frequently Asked Questions
=========================================

What is the difference between the Mattermost Operator and Helm Charts?
-----------------------------------------------------------------------

The Mattermost Operater is a self-contained set of application/product-specific instructions that runs inside Kubernetes and facilitates application
management and deployment.

Helm is a tool used to deploy Kubernetes manifests to a cluster, but does not facilitate application management.

Does the Mattermost Operator replace the Helm Chart?
----------------------------------------------------

No. Helm is a good mechanism to deploy operators and other applications but doesn't facilitate application management. But you can use Helm to deploy the
Mattermost operator. 
