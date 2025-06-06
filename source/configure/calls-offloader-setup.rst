Calls Offloader Setup and Configuration
=======================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. raw:: html

  <div class="mm-badge mm-badge--note">

Note

|plans-img-yellow| The calls-offloader service is available only on `Enterprise <https://mattermost.com/pricing/>`__ plans

.. |plans-img-yellow| image:: ../_static/images/badges/flag_icon_yellow.svg
    :class: mm-badge-flag

.. raw:: html

  </div>

This guide provides detailed instructions for setting up, configuring, and validating the Mattermost calls-offloader service used for call recording and transcription features.

- `Overview <#overview>`__
- `Prerequisites <#prerequisites>`__
- `Installation and deployment <#installation-and-deployment>`__
- `Configuration <#configuration>`__
- `Validation and testing <#validation-and-testing>`__
- `Integration with Mattermost <#integration-with-mattermost>`__
- `Troubleshooting <#troubleshooting>`__

Overview
--------

The calls-offloader service is a dedicated microservice that handles resource-intensive tasks for Mattermost Calls, including:

- **Call recording**: Captures audio and screen sharing content from calls
- **Call transcription**: Provides automated transcription of recorded calls
- **Live captions** (Experimental): Real-time transcription during active calls

By offloading these tasks to a dedicated service, the main Mattermost server and RTCD service can focus on core functionality while maintaining optimal performance.

Prerequisites
-------------

Before deploying calls-offloader, ensure you have:

- A Mattermost Enterprise license
- A properly configured Mattermost Calls deployment (either integrated or with RTCD)
- Docker installed and running (for Docker-based job execution)
- Sufficient storage space for recordings (see `Storage Requirements <#storage-requirements>`__)
- A server or container environment with adequate resources

System Requirements
^^^^^^^^^^^^^^^^^

For detailed system requirements and performance recommendations, refer to the `calls-offloader performance documentation <https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md>`__.

Storage Requirements
^^^^^^^^^^^^^^^^^^

Call recordings can consume significant storage space:

- Audio-only recordings: ~1MB per minute per participant
- Screen sharing recordings: ~10-50MB per minute depending on content

Installation and Deployment
---------------------------

Bare Metal or VM Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Download the latest release from the `calls-offloader GitHub repository <https://github.com/mattermost/calls-offloader/releases>`__

2. Create the necessary directories:

   .. code-block:: bash

      sudo mkdir -p /opt/calls-offloader/data/db
      sudo useradd --system --home /opt/calls-offloader calls-offloader
      sudo chown -R calls-offloader:calls-offloader /opt/calls-offloader

3. Create a configuration file (``/opt/calls-offloader/config.toml``):

   .. code-block:: toml

      [api]
      http.listen_address = ":4545"
      http.tls.enable = false
      http.tls.cert_file = ""
      http.tls.cert_key = ""
      security.allow_self_registration = true
      security.enable_admin = true
      security.admin_secret_key = "changeme"
      security.session_cache.expiration_minutes = 1440

      [store]
      data_source = "/opt/calls-offloader/data/db"

      [jobs]
      api_type = "docker"
      max_concurrent_jobs = 2
      failed_jobs_retention_time = "7d"
      image_registry = "mattermost"

      [logger]
      enable_console = true
      console_json = false
      console_level = "INFO"
      enable_file = true
      file_json = true
      file_level = "INFO"
      file_location = "/opt/calls-offloader/calls-offloader.log"
      enable_color = true

4. Create a systemd service file (``/etc/systemd/system/calls-offloader.service``):

   .. code-block:: ini

      [Unit]
      Description=Mattermost Calls Offloader Service
      After=network.target docker.service
      Requires=docker.service

      [Service]
      Type=simple
      User=calls-offloader
      WorkingDirectory=/opt/calls-offloader
      ExecStart=/opt/calls-offloader/calls-offloader --config /opt/calls-offloader/config.toml
      Restart=always
      RestartSec=10
      LimitNOFILE=65536

      [Install]
      WantedBy=multi-user.target

5. Enable and start the service:

   .. code-block:: bash

      sudo systemctl daemon-reload
      sudo systemctl enable calls-offloader
      sudo systemctl start calls-offloader

6. Check the service status:

   .. code-block:: bash

      sudo systemctl status calls-offloader

7. Verify the service is responding:

   .. code-block:: bash

      curl http://localhost:4545/version
      # Example output:
      # {"buildDate":"2025-03-10 19:13","buildVersion":"v0.9.2","buildHash":"a4bd418","goVersion":"go1.23.6"}


Configuration
-------------

API Configuration
^^^^^^^^^^^^^^^

The API section controls how the service accepts requests:

- **http.listen_address**: The address and port where the service listens (default: ``:4545``)
- **http.tls.enable**: Whether to use TLS encryption for the API
- **security.allow_self_registration**: Allow clients to self-register for job management
- **security.enable_admin**: Enable admin functionality
- **security.admin_secret_key**: Secret key for admin authentication (change from default!)

Store Configuration
^^^^^^^^^^^^^^^^^

Controls persistent data storage:

- **data_source**: Path to directory for storing job metadata and state

Jobs Configuration
^^^^^^^^^^^^^^^^

Controls job processing behavior:

- **api_type**: Job execution backend (``docker`` or ``kubernetes``)
- **max_concurrent_jobs**: Maximum number of simultaneous recording/transcription jobs
- **failed_jobs_retention_time**: How long to keep failed job data before cleanup
- **image_registry**: Docker registry for job runner images (typically ``mattermost``)

Logger Configuration
^^^^^^^^^^^^^^^^^^

Controls logging output:

- **enable_console**: Log to console output
- **console_json**: Use JSON format for console logs
- **console_level**: Log level for console (DEBUG, INFO, WARN, ERROR)
- **enable_file**: Log to file
- **file_location**: Path to log file
- **enable_color**: Use colored output for console logs

Private Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the Mattermost deployment is running in a private network, additional configuration may be necessary for the jobs spawned by the calls-offloader service to reach the Mattermost server.

In such cases, you can override the site URL used by recorder jobs or transcriber jobs to connect to Mattermost by setting the following environment variables on the Mattermost server:

- **MM_CALLS_RECORDER_SITE_URL**: Override the site URL used by recording jobs
- **MM_CALLS_TRANSCRIBER_SITE_URL**: Override the site URL used by transcription jobs

Example configuration:

Create or edit the Mattermost environment file (``/opt/mattermost/config/mattermost.environment``):

.. code-block:: bash

   MM_CALLS_RECORDER_SITE_URL="http://internal-mattermost-server:8065"
   MM_CALLS_TRANSCRIBER_SITE_URL="http://internal-mattermost-server:8065"

Then ensure your Mattermost systemd service references this environment file:

.. code-block:: ini

   [Unit]
   Description=Mattermost
   After=network.target

   [Service]
   Type=notify
   EnvironmentFile=/opt/mattermost/config/mattermost.environment
   ExecStart=/opt/mattermost/bin/mattermost
   TimeoutStartSec=3600
   KillMode=mixed
   Restart=always
   RestartSec=10
   WorkingDirectory=/opt/mattermost
   User=mattermost
   Group=mattermost

   [Install]
   WantedBy=multi-user.target

This is particularly useful when:

- The calls-offloader service runs in a different network segment than clients
- Internal DNS resolution differs from external URLs
- You need to use internal load balancer endpoints for job communication

Validation and Testing
---------------------

After deploying calls-offloader, validate the installation:

1. **Check service status**:

   .. code-block:: bash

      # For systemd
      sudo systemctl status calls-offloader


2. **Test API connectivity**:

   **From the calls-offloader server (localhost test)**:

   .. code-block:: bash

      curl http://localhost:4545/version
      # Should return version information
      # Example: {"buildDate":"2025-03-10 19:13","buildVersion":"v0.9.2","buildHash":"a4bd418","goVersion":"go1.23.6"}

   **From the Mattermost server**:

   .. code-block:: bash

      curl http://YOUR_CALLS_OFFLOADER_SERVER:4545/version
      # Should return the same version information
      # This confirms network connectivity from Mattermost to calls-offloader

   If the localhost test works but the Mattermost server test fails, check:
   
   - Firewall rules or SELinux policies on the calls-offloader server (port 4545 must be accessible)
   - Network connectivity between Mattermost and calls-offloader servers
   - calls-offloader service binding configuration (ensure it's not bound to localhost only)

3. **Verify Docker integration** (if using docker api_type):

   .. code-block:: bash

      # Check that system user running calls-offloader can access Docker
      sudo -u calls-offloader docker ps

Integration with Mattermost
---------------------------

Once calls-offloader is properly set up and validated, configure Mattermost to use it:

1. Go to **System Console > Plugins > Calls**

2. In the **Job Service** section:

   - Set **Job Service URL** to your calls-offloader service (e.g., ``http://calls-offloader-server:4545``)

3. Enable recording and transcription features as needed:

   - **Enable Call Recordings**: Toggle to allow call recordings
   - **Enable Call Transcriptions**: Toggle to allow call transcriptions  
   - **Enable Live Captions** (Experimental): Toggle to allow real-time transcription

4. Save the configuration

5. Restart the Calls plugin to re-establish state:

   - Go to **System Console > Plugins > Plugin Management**
   - Find the **Calls** plugin and click **Disable**
   - Wait a few seconds, then click **Enable**

6. Test by starting a call and enabling recording or live captions

Troubleshooting
---------------

Common Issues
^^^^^^^^^^^

**"failed to create recording job: max concurrent jobs reached"**

This error occurs when the calls-offloader service has reached its configured job limit.

Solutions:

- Increase ``max_concurrent_jobs`` in the configuration
- Check if jobs are hanging and restart the service
- Monitor system resources and scale up if needed

**Jobs not processing**

Check the following:

- Verify the calls-offloader service is running: ``sudo systemctl status calls-offloader``
- Ensure network connectivity between Mattermost and calls-offloader
- Check Docker daemon is running and accessible by the user running `calls-offloader`: ``docker ps``
- Verify authentication configuration matches between services
- Review service logs for specific error messages

**Docker permission issues**

If using Docker API and seeing permission errors:

.. code-block:: bash

   # Add calls-offloader user to docker group
   sudo usermod -a -G docker calls-offloader
   sudo systemctl restart calls-offloader

Debugging Commands
^^^^^^^^^^^^^^^^

Monitor calls-offloader job containers:

.. code-block:: bash

   # View running job containers
   docker ps --format "{{.ID}} {{.Image}}" | grep "calls"

   # Follow logs for debugging
   docker ps --format "{{.ID}} {{.Image}}" | grep "calls" | awk '{print $1}' | xargs -I {} docker logs -f {}

   # View completed job containers
   docker ps -a --filter "status=exited"

Monitor service health:

.. code-block:: bash

   # Check service version and health
   curl http://localhost:4545/version

Check service logs:

.. code-block:: bash

   # View recent logs
   sudo journalctl -u calls-offloader -f

   # View log file (if file logging enabled)
   tail -f /opt/calls-offloader/calls-offloader.log

Performance Monitoring
^^^^^^^^^^^^^^^^^^^^

Monitor calls-offloader performance and resource usage to ensure optimal operation. Set up alerts for high CPU/memory usage, failed jobs, or extended processing times.

Other Calls Documentation
----------------

- `Calls Overview <calls-deployment.html>`__: Overview of deployment options and architecture
- `RTCD Setup and Configuration <calls-rtcd-setup.html>`__: Comprehensive guide for setting up the dedicated RTCD service
- `Calls Metrics and Monitoring <calls-metrics-monitoring.html>`__: Guide to monitoring Calls performance using metrics and observability
- `Calls Deployment on Kubernetes <calls-kubernetes.html>`__: Detailed guide for deploying Calls in Kubernetes environments
- `Calls Troubleshooting <calls-troubleshooting.html>`__: Detailed troubleshooting steps and debugging techniques

For detailed performance tuning and monitoring recommendations, refer to the `calls-offloader performance documentation <https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md>`__.