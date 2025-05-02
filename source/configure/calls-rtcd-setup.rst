RTCD Setup and Configuration
=========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. raw:: html

  <div class="mm-badge mm-badge--note">

Note

|plans-img-yellow| The rtcd service is available only on `Enterprise <https://mattermost.com/pricing/>`__ plans

.. |plans-img-yellow| image:: ../_static/images/badges/flag_icon_yellow.svg
    :class: mm-badge-flag

.. raw:: html

  </div>

This guide provides detailed instructions for setting up, configuring, and validating a Mattermost Calls deployment using the dedicated RTCD service.

- `Why use RTCD <#why-use-rtcd>`__
- `Prerequisites <#prerequisites>`__
- `Installation and deployment <#installation-and-deployment>`__
- `Configuration <#configuration>`__
- `Validation and testing <#validation-and-testing>`__
- `Horizontal scaling <#horizontal-scaling>`__
- `Integration with Mattermost <#integration-with-mattermost>`__

Why use RTCD
-----------

The RTCD service (Real-Time Communication Daemon) is the recommended way to host Mattermost Calls for production environments for the following key reasons:

1. **Performance isolation**: RTCD runs as a standalone service, isolating the resource-intensive calls traffic from the main Mattermost servers. This prevents call traffic spikes from affecting the rest of your Mattermost deployment.

2. **Scalability**: When calls traffic increases, additional RTCD instances can be deployed to handle the load, without affecting your Mattermost servers.

3. **Call stability**: With RTCD, if a Mattermost server needs to be restarted, ongoing calls won't be disrupted. The call audio/video will continue while the Mattermost server restarts (though some features like emoji reactions will be temporarily unavailable).

4. **Kubernetes support**: For Kubernetes deployments, RTCD is the only officially supported way to run Calls.

5. **Real-time optimization**: The RTCD service is specifically optimized for real-time audio/video traffic, with configurations prioritizing low latency over throughput.

Prerequisites
------------

Before deploying RTCD, ensure you have:

- A Mattermost Enterprise license
- A server or VM with sufficient CPU and network capacity (see the `Performance <calls-deployment.html#performance>`__ section for sizing guidance)
- Network configuration that allows:
  - UDP port 8443 (default) open between clients and RTCD servers
  - TCP port 8045 (default) open between Mattermost servers and RTCD servers
  - TCP port 8443 (optional backup) between clients and RTCD servers

Installation and Deployment
--------------------------

There are multiple ways to deploy RTCD, depending on your environment:

Bare Metal or VM Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Download the latest release from the `RTCD GitHub repository <https://github.com/mattermost/rtcd/releases>`__

2. Create a configuration file (``config.toml``) with the following minimal settings:

   .. code-block:: toml

      [api]
      http.listen_address = ":8045"

      [rtc]
      ice_address_udp = ""
      ice_port_udp = 8443
      ice_host_override = "YOUR_RTCD_SERVER_PUBLIC_IP"

3. Run the RTCD service:

   .. code-block:: bash

      ./rtcd --config config.toml

Kubernetes Deployment
^^^^^^^^^^^^^^^^^^^

For Kubernetes deployments, use the official Helm chart:

1. Add the Mattermost Helm repository:

   .. code-block:: bash

      helm repo add mattermost https://helm.mattermost.com
      helm repo update

2. Install the RTCD chart:

   .. code-block:: bash

      helm install mattermost-rtcd mattermost/mattermost-rtcd \
        --set ingress.enabled=true \
        --set ingress.host=rtcd.example.com \
        --set service.annotations."service\\.beta\\.kubernetes\\.io/aws-load-balancer-backend-protocol"=udp \
        --set rtcd.ice.hostOverride=rtcd.example.com

   Refer to the `RTCD Helm chart documentation <https://github.com/mattermost/mattermost-helm/tree/master/charts/mattermost-rtcd>`__ for additional configuration options.

Docker Deployment
^^^^^^^^^^^^^^^

1. Create a configuration file as described in the Bare Metal section

2. Run the RTCD container:

   .. code-block:: bash

      docker run -d --name rtcd \
        -p 8045:8045 \
        -p 8443:8443/udp \
        -p 8443:8443/tcp \
        -v /path/to/config.toml:/rtcd/config/config.toml \
        mattermost/rtcd:latest

Configuration
-----------

RTCD Configuration File
^^^^^^^^^^^^^^^^^^^^^

The RTCD service uses a TOML configuration file. Here's a comprehensive example with commonly used settings:

.. code-block:: toml

   [api]
   # The address and port to which the HTTP API server will listen
   http.listen_address = ":8045"
   # Security settings for authentication
   security.allow_self_registration = false
   security.enable_admin = true
   security.admin_secret_key = "YOUR_API_KEY"
   # Configure allowed origins for CORS
   security.allowed_origins = ["https://mattermost.example.com"]

   [rtc]
   # The UDP address and port for media traffic
   ice_address_udp = ""
   ice_port_udp = 8443
   # The TCP address and port for fallback connections 
   ice_address_tcp = ""
   ice_port_tcp = 8443
   # Public hostname or IP that clients will use to connect
   ice_host_override = "rtcd.example.com"

   [logger]
   # Logging configuration
   enable_console = true
   console_json = false
   console_level = "INFO"
   enable_file = true
   file_json = true
   file_level = "DEBUG"
   file_location = "rtcd.log"

   [metrics]
   # Prometheus metrics configuration
   enable_prom = true
   prom_port = 9090

Key Configuration Options:

- **api.http.listen_address**: The address and port where the RTCD HTTP API service listens
- **rtc.ice_address_udp**: The UDP address for media traffic (empty means listen on all interfaces)
- **rtc.ice_port_udp**: The UDP port for media traffic 
- **rtc.ice_address_tcp**: The TCP address for fallback media traffic
- **rtc.ice_port_tcp**: The TCP port for fallback media traffic
- **rtc.ice_host_override**: The public hostname or IP address clients will use to connect to RTCD
- **api.security.allowed_origins**: List of allowed origins for CORS
- **api.security.admin_secret_key**: API key for Mattermost servers to authenticate with RTCD

STUN/TURN Configuration
^^^^^^^^^^^^^^^^^^^^^

For clients behind strict firewalls, you may need to configure STUN/TURN servers. In the RTCD configuration file, reference your STUN/TURN servers as follows:

.. code-block:: toml

   [rtc]
   # STUN/TURN server configuration
   ice_servers = [
     { urls = ["stun:stun.example.com:3478"] },
     { urls = ["turn:turn.example.com:3478"], username = "turnuser", credential = "turnpassword" }
   ]

We recommend using `coturn <https://github.com/coturn/coturn>`__ for your TURN server implementation. For setting up and configuring coturn:

1. Refer to the `official coturn documentation <https://github.com/coturn/coturn/wiki/turnadmin>`__
2. A basic coturn configuration file might look like this:

   .. code-block:: text

      # Basic coturn configuration - customize for your environment
      # Refer to official documentation for complete options
      
      # Listener interface(s)
      listening-ip=YOUR_SERVER_IP
      listening-port=3478
      
      # Relay interface(s)
      relay-ip=YOUR_SERVER_IP
      min-port=49152
      max-port=65535
      
      # Authentication
      lt-cred-mech
      user=turnuser:turnpassword
      
      # TLS (recommended for production)
      # cert=/path/to/cert.pem
      # pkey=/path/to/privkey.pem
      
      # Logging
      verbose
      fingerprint

3. Always test your TURN server connectivity before deploying to production using a tool like `Trickle ICE <https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice/>`__

For more advanced scenarios or troubleshooting, consult the official coturn documentation and WebRTC resources.

System Tuning
^^^^^^^^^^^

For high-volume deployments, tune your Linux system:

1. Add the following to ``/etc/sysctl.conf``:

   .. code-block:: bash

      # Increase UDP buffer sizes
      net.core.rmem_max = 16777216
      net.core.wmem_max = 16777216
      net.core.optmem_max = 16777216

2. Apply the settings:

   .. code-block:: bash

      sudo sysctl -p

Validation and Testing
--------------------

After deploying RTCD, validate the installation:

1. **Check service status**:

   .. code-block:: bash

      curl http://YOUR_RTCD_SERVER:8045/api/v1/health
      # Should return {"status":"ok"}

2. **Test UDP connectivity**:

   On the RTCD server:
   
   .. code-block:: bash

      nc -l -u -p 8443

   On a client machine:
   
   .. code-block:: bash

      nc -v -u YOUR_RTCD_SERVER 8443
      
   Type a message and hit Enter on either side. If messages are received on both ends, UDP connectivity is working.

3. **Test TCP connectivity** (if enabled):

   Similar to the UDP test, but remove the ``-u`` flag from both commands.

4. **Monitor metrics**:

   If you've enabled Prometheus metrics, access them at:
   
   .. code-block:: bash

      curl http://YOUR_RTCD_SERVER:9090/metrics

Horizontal Scaling
----------------

To scale RTCD horizontally:

1. **Deploy multiple RTCD instances**:
   
   Deploy multiple RTCD servers, each with their own unique IP address.

2. **Configure DNS-based load balancing**:
   
   Set up a DNS record that points to multiple RTCD IP addresses:
   
   .. code-block:: bash

      rtcd.example.com.    IN A    10.0.0.1
      rtcd.example.com.    IN A    10.0.0.2
      rtcd.example.com.    IN A    10.0.0.3

3. **Configure health checks**:
   
   Set up health checks to automatically remove unhealthy RTCD instances from DNS.

4. **Configure Mattermost**:
   
   In the Mattermost System Console, set the **RTCD Service URL** to your DNS name (e.g., ``rtcd.example.com``).

The Mattermost Calls plugin will distribute calls among the available RTCD hosts. Remember that a single call will always be hosted on one RTCD instance; sessions belonging to the same call are not spread across different instances.

RTCD Connectivity Diagrams
-----------------------

Understanding the network connectivity between clients, Mattermost servers, and RTCD services is crucial for proper deployment. The following diagrams illustrate the key communication paths in different deployment scenarios.

Basic RTCD Deployment
^^^^^^^^^^^^^^^^^^^

In this basic deployment model, RTCD handles all media traffic while the Mattermost server manages signaling:

::

    +----------------+       +----------------+       +----------------+
    |                |  1    |                |  2    |                |
    |   Client A     |<----->|   Mattermost  |<----->|     RTCD       |
    |                |  WS   |     Server    |  API  |    Service     |
    |                |       |                |       |                |
    +----------------+       +----------------+       +----------------+
            ^                                                 ^
            |                                                 |
            |                 Media (RTP)                     |
            |                    3                            |
            +-------------------------------------------------+

1. **WebSocket Connection (WS)**: Clients connect to Mattermost server using WebSockets for signaling and call control
2. **API Connection**: Mattermost server communicates with RTCD service for call setup and management
3. **Media (RTP) Connection**: Clients send/receive audio and screen sharing directly with RTCD service  

High Availability RTCD Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For high availability, multiple RTCD instances can be deployed with DNS-based load balancing:

::

    +----------------+       +----------------+       +----------------+
    |                |       |                |       |    RTCD #1     |
    |   Client A     |       |   Mattermost  |<----->|                |
    |                |       |     Server    |       +----------------+
    +----------------+       |      HA       |
            ^                |                |       +----------------+
            |                |                |       |    RTCD #2     |
    +----------------+       |                |<----->|                |
    |                |       |                |       +----------------+
    |   Client B     |<----->|                |
    |                |       |                |       +----------------+
    +----------------+       |                |       |    RTCD #3     |
            ^                |                |<----->|                |
            |                +----------------+       +----------------+
            |                         ^
            |                         |
            +-------------------------------------------------+
                              Media flows to appropriate
                                RTCD instance

In this model:
- Each client connects to Mattermost through the load balancer
- Mattermost distributes calls among available RTCD instances
- A single call is always hosted on one RTCD instance
- If an RTCD instance fails, only calls on that instance are affected

RTCD with TURN Server
^^^^^^^^^^^^^^^^^^

For environments with restrictive firewalls, a TURN server can relay media:

::

    +----------------+       +----------------+       +----------------+
    |                |       |                |       |                |
    |   Client A     |<----->|   Mattermost  |<----->|     RTCD       |
    |   (Firewall)   |       |     Server    |       |    Service     |
    |                |       |                |       |                |
    +----------------+       +----------------+       +----------------+
            ^                                                 ^
            |                                                 |
            |                                                 |
            v                                                 |
    +----------------+                                        |
    |                |                                        |
    |  TURN Server   |<---------------------------------------+
    |                |              Media Relay
    +----------------+

- Clients behind restrictive firewalls connect to the TURN server
- TURN server relays media between clients and RTCD
- Adds some latency but enables connectivity in challenging network environments

Detailed Network Protocol Diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This diagram shows the specific protocols and ports used in a typical RTCD deployment:

::

                        WebSockets HTTP(S)           RTCD API
                        TCP 80/443                   TCP 8045
    +--------------+   +--------------+   +------------------------+
    |              |   |              |   |                        |
    |   Clients    |<--|  Mattermost  |<--|        RTCD            |
    |              |   |   Server     |   |                        |
    +--------------+   +--------------+   +------------------------+
          ^                                          ^
          |                                          |
          |                                          |
          |       Media (RTP/RTCP)                   |
          +------------------------------------------+
                   UDP 8443 (preferred)
                   TCP 8443 (fallback)

Integration with Mattermost
-------------------------

Once RTCD is properly set up and validated, configure Mattermost to use it:

1. Go to **System Console > Plugins > Calls**

2. Enable the **Enable RTCD Service** option

3. Set the **RTCD Service URL** to your RTCD service address (either a single server or DNS load-balanced hostname)

4. If configured, enter the **RTCD API Key** that matches the one in your RTCD configuration

5. Save the configuration

6. Test by creating a new call in any Mattermost channel

7. Verify that the call is being routed through RTCD by checking the RTCD logs and metrics

For detailed Mattermost Calls configuration options, see the `Calls Plugin Configuration Settings <plugins-configuration-settings.html#calls>`__ documentation.