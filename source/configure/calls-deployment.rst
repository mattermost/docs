Calls self-hosted deployment
============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This document provides an overview of Mattermost Calls deployment options for self-hosted environments, including deployment architectures, key requirements, and important considerations.

Quick Links
----------

For detailed information on specific topics, please refer to these specialized guides:

- `RTCD Setup and Configuration <calls-rtcd-setup.html>`__: Comprehensive guide for setting up the dedicated RTCD service
- `Calls Troubleshooting <calls-troubleshooting.html>`__: Detailed troubleshooting steps and debugging techniques
- `Calls Metrics and Monitoring <calls-metrics-monitoring.html>`__: Guide to monitoring Calls performance using metrics and observability

About Mattermost Calls
---------------------

Mattermost Calls provides integrated audio calling and screen sharing capabilities within Mattermost channels. It's built on WebRTC technology and can be deployed either:

1. **Integrated mode**: Built into the Calls plugin (simpler, suitable for smaller deployments)
2. **RTCD mode**: Using a dedicated service for improved performance and scalability (recommended for production environments)

Terminology
-----------

- `WebRTC <https://bloggeek.me/webrtcglossary/webrtc-2/>`__: The set of protocols on which calls are built
- **RTC**: Real-Time Connection channel used for media (audio/video/screen)
- **WS**: WebSocket connection used for signaling and connection setup
- **SFU**: Selective Forwarding Unit, routes media between participants
- `NAT <https://bloggeek.me/webrtcglossary/nat/>`__: Network Address Translation for mapping IP addresses
- `STUN <https://bloggeek.me/webrtcglossary/stun/>`__: Protocol used by WebRTC clients to help traverse NATs
- `TURN <https://bloggeek.me/webrtcglossary/turn/>`__: Protocol to relay media for clients behind strict firewalls

Key Components
-------------

- **Calls plugin**: The main plugin that enables calls functionality
- **RTCD service**: Optional dedicated service for offloading media processing (Enterprise feature)
- **calls-offloader**: Service for call recording and transcription (if enabled)

Network Requirements
------------------

The following network connectivity is required:

+-------------------+--------+-----------------+-------------------------+------------------------+
| Service           | Ports  | Protocols       | Source                  | Target                 |
+===================+========+=================+=========================+========================+
| Calls plugin API  | 80,443 | TCP (incoming)  | Mattermost clients      | Mattermost server      |
+-------------------+--------+-----------------+-------------------------+------------------------+
| RTC media         | 8443   | UDP (incoming)  | Mattermost clients      | Mattermost or RTCD     |
+-------------------+--------+-----------------+-------------------------+------------------------+
| RTC media         | 8443   | TCP (incoming)  | Mattermost clients      | Mattermost or RTCD     |
+-------------------+--------+-----------------+-------------------------+------------------------+
| RTCD API          | 8045   | TCP (incoming)  | Mattermost server       | RTCD service           |
+-------------------+--------+-----------------+-------------------------+------------------------+
| STUN              | 3478   | UDP (outgoing)  | Mattermost or RTCD      | STUN servers           |
+-------------------+--------+-----------------+-------------------------+------------------------+

For complete network requirements, see the `RTCD Setup and Configuration <calls-rtcd-setup.html>`__ guide.

Limitations
-----------

- In Mattermost Cloud, up to 200 participants per channel can join a call.
- In Mattermost self-hosted deployments, the default maximum number of participants is unlimited. The recommended maximum number of participants per call is 200. 
- You can configure the maximum participants in **System Console > Plugin Management > Calls > Max call participants**.

Configuration
-------------

For Mattermost self-hosted customers, the calls plugin is pre-packaged, installed, and enabled. Configuration to allow end-users to use it can be found in the `System Console </configure/plugins-configuration-settings.html#calls>`__.

Deployment Architecture Options
-----------------------------

Mattermost Calls can be deployed in several configurations:

Single Instance Deployments
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/calls-deployment-image3.png
  :alt: A diagram of the integrated configuration model of a single instance.
  :width: 600px

**Integrated mode**: The WebRTC service runs within the Calls plugin on the Mattermost server.

.. image:: ../images/calls-deployment-image7.png
  :alt: A diagram of a Web RTC deployment configuration.
  :width: 600px

**RTCD mode**: A dedicated RTCD service handles media routing, reducing load on the Mattermost server.

High Availability Deployments
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/calls-deployment-image4.png
  :alt: A diagram of a clustered calls deployment.
  :width: 600px

**Clustered mode**: Each Mattermost node runs an instance of the plugin with its own WebRTC service.

.. image:: ../images/calls-deployment-image2.png
  :alt: A diagram of an rtcd deployment.
  :width: 600px

**RTCD with HA**: Dedicated RTCD services handle media routing for high availability.

Kubernetes Deployments
~~~~~~~~~~~~~~~~~~~~

.. image:: ../images/calls-deployment-kubernetes.png
  :alt: A diagram of calls deployed in a Kubernetes cluster.
  :width: 600px

For Kubernetes deployments, the RTCD service is strongly recommended and is the only officially supported approach.

For Kubernetes deployments, the recommended approach is to use the officially provided Helm charts:

- `rtcd Helm chart <https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-rtcd>`__
- `calls-offloader Helm chart <https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-calls-offloader>`__

When to Use RTCD
--------------

The dedicated RTCD service (available with Enterprise license) is recommended for:

- **Production environments**: Isolates call traffic from other Mattermost services
- **Performance optimization**: Dedicated service tuned for real-time media
- **Scalability**: Add RTCD instances as call volume grows
- **Call stability**: Calls continue even if Mattermost server needs to restart
- **Kubernetes deployments**: Required for officially supported Kubernetes deployments

For detailed RTCD setup instructions, see the `RTCD Setup and Configuration <calls-rtcd-setup.html>`__ guide.

Call Recording and Transcription
------------------------------

For call recording and transcription, you need to:

1. Deploy the ``calls-offloader`` service
2. Configure the service URL in the System Console
3. Enable call recordings and/or transcriptions in the plugin settings

Performance Considerations
------------------------

Calls performance primarily depends on:

- **CPU resources**: More participants require more processing power
- **Network bandwidth**: Both incoming and outgoing traffic increases with participant count
- **Active speakers**: Unmuted participants require significantly more resources 

For detailed performance metrics, benchmarks, and monitoring guidance, see the `Calls Metrics and Monitoring <calls-metrics-monitoring.html>`__ guide.

Frequently Asked Questions
------------------------

**Is calls traffic encrypted?**  
Yes, using WebRTC security standards (DTLS/SRTP). Traffic is encrypted in transit.

**Are there any third-party services involved?**  
Only a Mattermost STUN server (``stun.global.calls.mattermost.com``) is used by default. This can be removed if you set the ICE Host Override configuration.

**Is using UDP a requirement?**  
UDP is recommended for best performance, but TCP fallback is supported since plugin version 0.17 and RTCD version 0.11.

**Do I need a TURN server?**  
Only if clients are behind restrictive firewalls that block UDP. We recommend `coturn <https://github.com/coturn/coturn>`__ if needed.

**Can RTCD traffic be kept internal?**  
Yes, and it's recommended. Only the media ports need to be accessible to end-users.

Troubleshooting
---------------

For comprehensive troubleshooting steps and debugging techniques, please refer to the `Calls Troubleshooting <calls-troubleshooting.html>`__ guide.

Next Steps
---------

1. For detailed setup instructions, see `RTCD Setup and Configuration <calls-rtcd-setup.html>`__
2. For monitoring guidance, see `Calls Metrics and Monitoring <calls-metrics-monitoring.html>`__
3. If you encounter issues, see `Calls Troubleshooting <calls-troubleshooting.html>`__