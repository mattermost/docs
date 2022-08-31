Calls self-hosted deployment
============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This document provides information on how to successfully make the Calls plugin work on self-hosted deployments. It also outlines some of the most common deployment strategies with example diagrams.

Terminology
-----------

- **WebRTC**: The set of underlying protocols/specifications on top of which calls are implemented. 
- **RTC (Real Time Connection)**: The real-time connection. This is the channel used to send media tracks (audio/video/screen).
- **WS (WebSocket)**: The WebSocket connection. This is the channel used to set up a connection (signaling process).
- **NAT (Network Address Translation)**: A networking technique to map IP addresses. 
- **STUN (Session Traversal Utilities for NAT)**: A protocol/service used by WebRTC clients to help traversing NATs. On the server side it's mainly used to figure out the public IP of the instance. 
- **TURN (Traversal Using Relays around NAT)**: A protocol/service used to help WebRTC clients behind strict firewalls connect to a call through media relay. 

Components
----------

- **Calls plugin**: This is the main entry point and a requirement to enable channel calls.

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

- **RTCD**: This is an optional service that can be deployed to offload all the functionality and data processing involved with the WebRTC connections. This is the preferred solution for a performant and scalable deployment. With RTCD, the Mattermost server will be minimally impacted when hosting a high number of calls.

Requirements
------------

Server
~~~~~~

- Run Mattermost server on a secure (HTTPs) connection. This is a necessary requirement on the client to allow capturing devices (e.g., microphone, screen). See the `config TLS </install/config-tls-mattermost.html>`_ section for more info.
- Open the UDP port configured as ``RTC Server Port`` (default is 8443, incoming direction). This is necessary to allow calls related traffic (e.g., audio, video).
- Open the UDP port used by the configured STUN server (default is 3478, outgoing direction). By default the plugin will attempt to identify the instance's public IP address. To do this the STUN protocol is used. This requirement does not apply when manually setting an IP/hostname through the ``ICE Host Override`` config option.

Client
~~~~~~

- Clients need to be able to connect (send and receive data) to the instance hosting the calls through the UDP port configured as ``RTC Server Port``. If this is not possible a TURN server should be used to achieve connectivity.
- Depending on the platform or operating system, clients may need to grant additional permissions to the application (e.g., browser, desktop app) to  allow them to capture audio inputs or share the screen.

Limitations
-----------

- In Mattermost Cloud, up to 40 participants per channel can join a call. This is a temporary and evolving limitation during public beta.
- In Mattermost self-hosted deployments, the default maximum number of participants is unlimited. The recommended maximum number of participants per call is 200. This setting can be changed in **System Console > Plugin Management > Calls > Max call participants**. There's no limit to the total number of participants across all calls as the supported value greatly depends on instance resources. For more details, refer to the performance section below.

Configuration
-------------

For Mattermost self-hosted customers, the calls plugin is pre-packaged, installed, and enabled. Configuration to allow end-users to use it can be found in the `System Console <https://docs.mattermost.com/configure/configuration-settings.html#calls-beta>`_.

Frequently asked questions
--------------------------

Can I password-protect a call?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Any member with sufficient permission to access the channel will be able to join the call.

Is there encryption?
~~~~~~~~~~~~~~~~~~~~

Media (audio/video) is encrypted using security standards as part of WebRTC. It's mainly a combination of DTLS and SRTP. It's not e2e encrypted in the sense that in the current design all media needs to go through Mattermost which acts as a media router and has complete access to it. Media is then encrypted back to the clients so it's secured during transit. In short: only the participant clients and the Mattermost server have access to unencrypted call data.

What are the potential performance impacts?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Database load should be minimal. Overall instance load however will be affected, especially CPU usage, growing as a function of the number of participants produce the number of active tracks (unmuted participants and users sharing their screen). Screen sharing has the highest impact on both CPU and bandwidth. The latter can be more easily estimated as the audio/video bitrates are constrained and predictable (around 40-60Kbps for each audio track and up to 1Mbps per screen track).

If you wish to host many calls or calls with a large number of participants, take a look at the following platform specific (Linux) tunings (this is the only officially supported target for the plugin right now):

.. code::

  # Setting the maximum buffer size of the receiving UDP buffer to 16MB
  net.core.rmem_max = 16777216

  # Setting the maximum buffer size of the sending UDP buffer to 16MB
  net.core.wmem_max = 16777216

  # Allow to allocate more memory as needed for more control messages that need to be sent for each socket connected
  net.core.optmem_max = 16777216

Are there any third-party services involved?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

STUN servers are configurable on the plugin itself. These are optional and depend on your configuration.

Network requirements
--------------------

+--------------------------+-------------------------+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Service name             | Ports (defaults)        | Protocols                        | Notes                                                                                                                                                                                                                                           |
+==========================+=========================+==================================+=================================================================================================================================================================================================================================================+
| API (plugin)             | 80, 443                 | TCP (incoming)   HTTP(s)/WS(s)   | This API is exposed on the same connection as Mattermost, so there’s no need to change anything.                                                                                                                                                |
+--------------------------+-------------------------+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RTC (plugin or rtcd)     | 8443                    | UDP (incoming)                   | Public/client facing. This should be open on any network component (e.g. NAT, firewalls) in between the instance running the plugin (or rtcd) and the clients joining calls so that UDP traffic is correctly routed both ways (from/to clients).|
+--------------------------+-------------------------+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| API (rtcd)               | 8045                    | TCP (incoming)                   | Internal, private network. Only needs to be reachable by the instances running the Mattermost server.                                                                                                                                           |
+--------------------------+-------------------------+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|STUN/TURN (plugin or rtcd)| 3478                    | UDP (outgoing)                   | Public/client facing. Only needed if configuring STUN/TURN servers.                                                                                                                                                                             |
+--------------------------+-------------------------+----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Modes of operation
------------------

Depending on how the Mattermost server is running, there are several modes under which the Calls plugin can operate.

.. image:: ../images/calls-deployment-image1.png
  :alt: A diagram of the calls deployment modes and their dependencies.

Single instance
~~~~~~~~~~~~~~~

Integrated
^^^^^^^^^^

This is the default mode when first installing the plugin on a single Mattermost instance setup. The WebRTC service is integrated in the plugin itself and runs alongside the Mattermost server.

.. image:: ../images/calls-deployment-image3.png
  :alt: A diagram of the integrated configuration model of a single instance.

rtcd
^^^^

An external, dedicated and scalable WebRTC service (RTCD) is used to handle all calls media routing.

.. image:: ../images/calls-deployment-image7.png
  :alt: A diagram of a Web RTC deployment configuration.

High availability cluster
~~~~~~~~~~~~~~~~~~~~~~~~~

Clustered
^^^^^^^^^

This is the default mode when running the plugin in a HA cluster. Every Mattermost node will run an instance of the plugin that includes a WebRTC service. Calls are distributed across all available nodes through the existing load-balancer: a call is hosted on the instance where the initiating websocket connection (first client to join) is made. A single call will be hosted on a single cluster node.

.. image:: ../images/calls-deployment-image5.png
  :alt: A diagram of a clustered calls deployment.

Single handler
^^^^^^^^^^^^^^

This is a fallback mode to only let one node in the cluster to host calls. While the plugin would still run on all nodes, all calls will be routed through the handler node. This mode must be enabled by running the instance with a special environment variable set (MM_CALLS_IS_HANDLER=true).

.. image:: ../images/calls-deployment-image4.png
  :alt: A diagram of a single handler deployment.

rtcd
^^^^

.. image:: ../images/calls-deployment-image2.png
  :alt: A diagram of an rtcd deployment.

Kubernetes deployments
----------------------

.. image:: ../images/calls-deployment-kubernetes.png
  :alt: A diagram of calls deployed in a Kubernetes cluster.
  
If Mattermost is not deployed in a Kubernetes cluster, and you want to use this deployment type, visit the `Kubernetes operator guide <https://docs.mattermost.com/install/mattermost-kubernetes-operator.html>`_.

RTCD is deployed with a Helm chart. To install this Helm chart run:

.. code-block:: none

  helm repo add mattermost https://helm.mattermost.com

More info about the version and the chart itself, please check here. Regarding changing the parameters of the helm chart, please check and copy the default values from here.

An example with sample values:

.. code-block:: none

 image:
   repository: mattermost/rtcd
   pullPolicy: IfNotPresent
   tag: "v0.6.9"

 imagePullSecrets: []
 nameOverride: ""
 fullnameOverride: ""

 serviceAccount:
    create: true
    annotations: {}
    name: ""

 podAnnotations: {}

 podSecurityContext: {}

  securityContext: {}

  daemonset:
    environmentVariables:
      RTCD_API_SECURITY_ALLOWSELFREGISTRATION: "\"true\""
      RTCD_RTC_ICESERVERS: 
    "\'[{\"urls\":[\"stun:stun.global.calls.mattermost.com:3478\"]}]\'"
      RTCD_LOGGER_CONSOLELEVEL: "\"DEBUG\""
      RTCD_LOGGER_ENABLEFILE: "\"false\""
    maxUnavailable: 1 # Only used when updateStrategy is set to 
   "RollingUpdate"
    updateStrategy: RollingUpdate
    terminationGracePeriod: 18000 # 5 hours, used to gracefully draining the instance.

  service:
    # APIport is the port used by rtcd HTTP/WebSocket API.
    APIport: 8045
    # RTCport is the UDP port used to route all the calls related traffic.
    RTCport: 8443

 ingress:
    enabled: false
    classname: nginx-calls
    annotations:
    hosts:
      - host: mattermost-rtcd.local
        paths:
          - "/"
          
 resources:
    limits:
      cpu: 7800m # Values for c5.2xlarge in AWS
      memory: 15Gi # Values for c5.2xlarge in AWS
    requests:
      cpu: 100m
      memory: 32Mi

 nodeSelector:
    kops.k8s.io/instancegroup: rtcd

  tolerations:
    - key: "rtcd"
      operator: "Equal"
      value: "true"
      effect: "NoSchedule"

  dnsConfig:
    options:
    - name: ndots
      value: "1"

  affinity: {}

RTCD will be deployed as DaemonSet, for that reason the sections of nodeSelector and tolerations are used so that RTCD to be deployed in specific nodes.

After having the values above, to deploy the RTCD helm chart run:

.. code-block:: none

  helm upgrade mattermost-rtcd mattermost/mattermost-rtcd -f /Users/myuser/rtcd_values.yaml --namespace mattermost-rtcd --create-namespace --install --debug
  
