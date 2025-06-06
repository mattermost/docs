Calls deployment on Kubernetes
===========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This guide provides detailed information for deploying Mattermost Calls on Kubernetes environments.

Overview
--------

Mattermost Calls has been designed to integrate well with Kubernetes to offer improved scalability and control over the deployment. For Kubernetes deployments, the RTCD service is strongly recommended and is the only officially supported approach.

Architecture
-----------

.. image:: ../images/calls-deployment-kubernetes.png
  :alt: Calls deployed in a Kubernetes cluster
  :width: 600px

This diagram shows how the RTCD standalone service can be deployed in a Kubernetes cluster. In this architecture:

1. Calls traffic is handled by dedicated RTCD pods
2. RTCD services are exposed through load balancers
3. Scaling is managed through Kubernetes deployment configurations
4. Call recording and transcription is handled by the calls-offloader service (see `Calls Offloader Setup and Configuration <calls-offloader-setup.html>`__)

If Mattermost isn't already deployed in your Kubernetes cluster and you want to use this deployment type, visit the `Kubernetes operator guide </install/mattermost-kubernetes-operator.html>`__.

Helm Chart Deployment
-------------------

The recommended way to deploy Calls-related components in a Kubernetes environment is to use the officially provided Helm charts:

RTCD Helm Chart
^^^^^^^^^^^^^

The RTCD Helm chart deploys the RTCD service needed for call media handling:

.. code-block:: bash

   helm repo add mattermost https://helm.mattermost.com
   helm repo update
   
   helm install mattermost-rtcd mattermost/mattermost-rtcd \
     --set ingress.enabled=true \
     --set ingress.host=rtcd.example.com \
     --set service.annotations."service\\.beta\\.kubernetes\\.io/aws-load-balancer-backend-protocol"=udp \
     --set rtcd.ice.hostOverride=rtcd.example.com

For complete configuration options, see the `RTCD Helm chart documentation <https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-rtcd>`__.

Calls-Offloader Helm Chart
^^^^^^^^^^^^^^^^^^^^^^^^

If you need call recording and transcription capabilities, deploy the calls-offloader service:

.. code-block:: bash

   helm install mattermost-calls-offloader mattermost/mattermost-calls-offloader \
     --set ingress.enabled=true \
     --set ingress.host=calls-offloader.example.com

For complete configuration options, see the `Calls-Offloader Helm chart documentation <https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-calls-offloader>`__.

Kubernetes-Specific Configuration
-------------------------------

Network Configuration
^^^^^^^^^^^^^^^^^^

For Kubernetes deployments, you need to ensure:

1. UDP traffic is properly routed to RTCD pods (for media)
2. TCP traffic can reach both the Mattermost pods and RTCD pods
3. Load balancers are properly configured to handle UDP traffic
4. Network policies allow the required communications between services

Recommended annotations for AWS environments:

.. code-block:: yaml

   service.beta.kubernetes.io/aws-load-balancer-backend-protocol: udp
   service.beta.kubernetes.io/aws-load-balancer-type: nlb

Resource Requirements
^^^^^^^^^^^^^^^^^^

For optimal performance in Kubernetes environments:

1. **CPU**: At least 2 CPU cores per RTCD pod
2. **Memory**: At least 1GB RAM per RTCD pod
3. **Network**: Sufficient bandwidth for expected call volume (see benchmarks)

We recommend setting resource limits and requests in your deployment:

.. code-block:: yaml

   resources:
     requests:
       cpu: 1000m
       memory: 1Gi
     limits:
       cpu: 2000m
       memory: 2Gi

Scaling Considerations
^^^^^^^^^^^^^^^^^^

Horizontal scaling of RTCD pods is possible, but remember:

1. Each call is hosted entirely on a single RTCD pod
2. DNS-based load balancing should be used to distribute calls among pods
3. Health checks should ensure that only healthy pods receive new calls
4. Calls remain on their assigned pod for their entire duration

Limitations
^^^^^^^^^^

Due to the inherent complexities of hosting a WebRTC service, some limitations apply when deploying Calls in a Kubernetes environment.

One key requirement is that each ``rtcd`` process must live in a dedicated Kubernetes node. This is necessary to forward the data correctly while allowing for horizontal scaling. Data should generally not go through a standard ingress but directly to the pod running the ``rtcd`` process.

The general recommendation is to expose one external IP address per ``rtcd`` instance (Kubernetes node). This makes it simpler to scale as the application is able to detect its own external address (through STUN) and advertise it to clients to achieve connectivity with minimal configuration.

If, for some reason, exposing multiple IP addresses is not possible in your environment, port mapping (NAT) can be used. In this scenario different ports are used to map the respective ``rtcd`` nodes behind the single external IP. Example:

.. code-block:: text

   EXT_IP:8443 -> rtcdA:8443
   EXT_IP:8444 -> rtcdB:8443
   EXT_IP:8445 -> rtcdC:8443

This case requires a couple of extra configurations:

* NAT mappings need to be in place for every ``rtcd`` node. This is usually done at the ingress point (e.g., ELB, NLB, etc).

* The ``RTCD_RTC_ICEHOSTPORTOVERRIDE`` config should be used to pass a full mapping of node IPs and their respective port.

  * Example: ``RTCD_RTC_ICEHOSTPORTOVERRIDE=rtcdA_IP/8443,rtcdB_IP/8444,rtcdC_IP/8445``

* The ``RTCD_RTC_ICEHOSTOVERRIDE`` should be used to set the external IP address.

.. note::
   One option to limit these static mappings is to reduce the size of the local subnet (e.g., to ``/29``).

Monitoring and Metrics
^^^^^^^^^^^^^^^^^^^

We recommend deploying Prometheus and Grafana alongside your Calls deployment:

1. Configure Prometheus to scrape metrics from both Mattermost and RTCD pods
2. Import the official Mattermost Calls dashboard to Grafana
3. Set up alerts for CPU usage, connection failures, and error rates

For detailed information on metrics collection and monitoring, see the `Calls Metrics and Monitoring <calls-metrics-monitoring.html>`__ guide.

Troubleshooting
--------------

For Kubernetes-specific troubleshooting:

1. Check pod logs: `kubectl logs -f deployment/mattermost-rtcd`
2. Verify service connectivity: `kubectl port-forward service/mattermost-rtcd 8045:8045`
3. Ensure UDP traffic is properly routed through your ingress/load balancer
4. Verify network policies allow required communication paths

For detailed troubleshooting steps, see the `Calls Troubleshooting <calls-troubleshooting.html>`__ guide.

Other Calls Documentation
----------------

- `Calls Overview <calls-deployment.html>`__: Overview of deployment options and architecture
- `RTCD Setup and Configuration <calls-rtcd-setup.html>`__: Comprehensive guide for setting up the dedicated RTCD service
- `Calls Offloader Setup and Configuration <calls-offloader-setup.html>`__: Setup guide for call recording and transcription
- `Calls Metrics and Monitoring <calls-metrics-monitoring.html>`__: Guide to monitoring Calls performance using metrics and observability
- `Calls Troubleshooting <calls-troubleshooting.html>`__: Detailed troubleshooting steps and debugging techniques
3. If you encounter issues, see `Calls Troubleshooting <calls-troubleshooting.html>`__