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

- `Prerequisites <#prerequisites>`__
- `Installation and deployment <#installation-and-deployment>`__
- `Configuration <#configuration>`__
- `Validation and testing <#validation-and-testing>`__
- `Horizontal scaling <#horizontal-scaling>`__
- `Integration with Mattermost <#integration-with-mattermost>`__

Prerequisites
------------

Before deploying RTCD, ensure you have:

- A Mattermost Enterprise license
- A server or VM with sufficient CPU and network capacity (see the `Performance <calls-deployment.html#performance>`__ section for sizing guidance)

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

Installation and Deployment
--------------------------

There are multiple ways to deploy RTCD, depending on your environment. We recommend the following order based on production readiness and operational control:

Bare Metal or VM Deployment (Recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the recommended deployment method for production environments as it provides the best performance and operational control.

1. Download the latest release from the `RTCD GitHub repository <https://github.com/mattermost/rtcd/releases>`__

2. Create a configuration file (``/opt/rtcd/rtcd.toml``) with the following settings:

   .. code-block:: toml

      [api]
      http.listen_address = ":8045"
      security.allow_self_registration = true

      [rtc]
      ice_address_udp = ""
      ice_port_udp = 8443
      ice_address_tcp = ""
      ice_port_tcp = 8443
      ice_host_override = "YOUR_RTCD_SERVER_PUBLIC_IP"

      # UDP port range for WebRTC connections
      ice.port_range.min = 9000
      ice.port_range.max = 10000

      # STUN/TURN server configuration
      ice_servers = [
        { urls = ["stun:stun.global.calls.mattermost.com:3478"] }
      ]

      [store]
      data_source = "/opt/rtcd/data/db"

      [logger]
      enable_console = true
      console_json = true
      console_level = "INFO"
      enable_file = true
      file_json = true
      file_level = "INFO"
      file_location = "/opt/rtcd/rtcd.log"
      enable_color = true

      [mattermost]
      host = "http://YOUR_MATTERMOST_SERVER:8065"

3. Create the data directory:

   .. code-block:: bash

      sudo mkdir -p /opt/rtcd/data/db

4. Create a systemd service file (``/etc/systemd/system/rtcd.service``):

   .. code-block:: ini

      [Unit]
      Description=Mattermost RTCD Server
      After=network.target

      [Service]
      Type=simple
      User=root
      ExecStart=/opt/rtcd/rtcd --config /opt/rtcd/rtcd.toml
      Restart=always
      RestartSec=10
      LimitNOFILE=65536

      [Install]
      WantedBy=multi-user.target

5. Enable and start the service:

   .. code-block:: bash

      sudo systemctl daemon-reload
      sudo systemctl enable rtcd
      sudo systemctl start rtcd

6. Check the service status:

   .. code-block:: bash

      sudo systemctl status rtcd

Docker Deployment
^^^^^^^^^^^^^^^

Docker deployment is suitable for development, testing, or containerized production environments:

1. Run the RTCD container with basic configuration:

   .. code-block:: bash

      docker run -d --name rtcd \
        -e "RTCD_LOGGER_ENABLEFILE=false" \
        -e "RTCD_API_SECURITY_ALLOWSELFREGISTRATION=true" \
        -p 8443:8443/udp \
        -p 8443:8443/tcp \
        -p 8045:8045/tcp \
        mattermost/rtcd:latest

2. For debugging purposes, you can enable more detailed logging:

   .. code-block:: bash

      docker run -d --name rtcd \
        -e "RTCD_LOGGER_ENABLEFILE=false" \
        -e "RTCD_LOGGER_CONSOLELEVEL=DEBUG" \
        -e "RTCD_API_SECURITY_ALLOWSELFREGISTRATION=true" \
        -p 8443:8443/udp \
        -p 8443:8443/tcp \
        -p 8045:8045/tcp \
        mattermost/rtcd:latest

   To view the logs:

   .. code-block:: bash

      docker logs -f rtcd

You can also use a mounted configuration file instead of environment variables:

.. code-block:: bash

   docker run -d --name rtcd \
     -p 8045:8045 \
     -p 8443:8443/udp \
     -p 8443:8443/tcp \
     -v /path/to/config.toml:/rtcd/config/config.toml \
     mattermost/rtcd:latest

For a complete sample configuration file, see the `RTCD config.sample.toml <https://github.com/mattermost/rtcd/blob/master/config/config.sample.toml>`__ in the official repository.

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

We recommend using `coturn <https://github.com/coturn/coturn>`__ for your TURN server implementation. 
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

1. **Check service status and version**:

   .. code-block:: bash

      curl http://YOUR_RTCD_SERVER:8045/version
      # Should return a JSON object with service information
      # Example: {"build_hash":"abc123","build_date":"2023-01-15T12:00:00Z","build_version":"0.11.0","goVersion":"go1.20.4"}

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

Other Calls Documentation
----------------

- `Calls Overview <calls-deployment.html>`__: Overview of deployment options and architecture
- `Calls Offloader Setup and Configuration <calls-offloader-setup.html>`__: Setup guide for call recording and transcription
- `Calls Metrics and Monitoring <calls-metrics-monitoring.html>`__: Guide to monitoring Calls performance using metrics and observability
- `Calls Deployment on Kubernetes <calls-kubernetes.html>`__: Detailed guide for deploying Calls in Kubernetes environments
- `Calls Troubleshooting <calls-troubleshooting.html>`__: Detailed troubleshooting steps and debugging techniques

For detailed Mattermost Calls configuration options, see the `Calls Plugin Configuration Settings <plugins-configuration-settings.html#calls>`__ documentation.