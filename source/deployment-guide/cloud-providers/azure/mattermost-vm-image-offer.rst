:orphan:
:nosearch:

This Azure Marketplace VM image deploys a Mattermost-ready Linux virtual machine in your own subscription.

What the image includes
~~~~~~~~~~~~~~~~~~~~~~~~

This uses a Linux base image from Canonical Ubuntu Pro 24.04 LTS.

- Mattermost Enterprise Edition
- Common operational dependencies

  - ``jq``: for JSON processing (Mattermost configuration is stored in JSON files)
  - ``nfs-common``: NFS client utilities, for mounting Azure Files when you use the NFS protocol

- High-availability–oriented OS tuning (file descriptor limits and kernel parameters). See :doc:`high-availability-cluster-based-deployment </administration-guide/scale/high-availability-cluster-based-deployment>` for further details.

  - ``/etc/security/limits.conf``: raises open-file limits for the Mattermost process
  - ``/etc/sysctl.conf``: kernel tuning (e.g. increases the maximum number of WebSocket connections).

What you need to provide
~~~~~~~~~~~~~~~~~~~~~~~~~

You still provide and operate the surrounding Azure layers: Network / Proxy, Mattermost Application (will use this VM image), Database, and File Storage.

Please check :doc:`server architecture </administration-guide/scale/server-architecture>` for further details.
