Calls self-hosted deployment
============================

This document provides information on how to successfully make the Calls plugin work on self-hosted deployments. It also outlines some of the most common deployment strategies with example diagrams.

Components
----------

- Calls plugin: This is the main entry point and a requirement to enable channel calls. 
- RTCD: This is an optional service that can be deployed to offload all the functionality and data processing involved with the WebRTC connections. This is the preferred solution for a performant and scalable deployment. With RTCD, the Mattermost server will be minimally impacted when hosting a high number of calls.

Terminology
-----------

- WebRTC: The set of underlying protocols/specifications on top of which calls are implemented. 
- RTC (Real Time Connection): The real-time connection. This is the channel used to send media tracks (audio/video/screen).
- WS (WebSocket): The WebSocket connection. This is the channel used to set up a connection (signaling process).
- NAT (Network Address Translation): A networking technique to map IP addresses. 
- STUN (Session Traversal Utilities for NAT): A protocol/service used by WebRTC clients to help traversing NATs. On the server side it's mainly used to figure out the public IP of the instance. 
- TURN (Traversal Using Relays around NAT): A protocol/service used to help WebRTC clients behind strict firewalls connect to a call through media relay. 

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

Single instance
~~~~~~~~~~~~~~~

Integrated
^^^^^^^^^^

This is the default mode when first installing the plugin on a single Mattermost instance setup. The WebRTC service is integrated in the plugin itself and runs alongside the Mattermost server.


rtcd
^^^^

An external, dedicated and scalable WebRTC service (RTCD) is used to handle all calls media routing.

High availability cluster
~~~~~~~~~~~~~~~~~~~~~~~~~

Clustered
^^^^^^^^^

This is the default mode when running the plugin in a HA cluster. Every Mattermost node will run an instance of the plugin that includes a WebRTC service. Calls are distributed across all available nodes through the existing load-balancer: a call is hosted on the instance where the initiating websocket connection (first client to join) is made. A single call will be hosted on a single cluster node.

Single handler
^^^^^^^^^^^^^^

This is a fallback mode to only let one node in the cluster to host calls. While the plugin would still run on all nodes, all calls will be routed through the handler node. This mode must be enabled by running the instance with a special environment variable set (MM_CALLS_IS_HANDLER=true).

rtcd
^^^^

Kubernetes deployments
----------------------

If Mattermost is not deployed in a Kubernetes cluster, there is a guide that describes how to deploy a Mattermost operator. https://docs.mattermost.com/install/mattermost-kubernetes-operator.html

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
      RTCD_RTC_ICESERVERS: "\'[{\"urls\":[\"stun:stun.global.calls.mattermost.com:3478\"]}]\'"
      RTCD_LOGGER_CONSOLELEVEL: "\"DEBUG\""
      RTCD_LOGGER_ENABLEFILE: "\"false\""
    maxUnavailable: 1 # Only used when updateStrategy is set to "RollingUpdate"
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
  
