Deploy Grafana Loki for centralized logging
=============================================

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

This guide extends your existing `Prometheus and Grafana performance monitoring deployment </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>`_ by adding `Grafana Loki <https://grafana.com/oss/loki/>`__ for centralized log aggregation. While Prometheus collects **metrics** (CPU, request latency, goroutine counts), Loki collects **logs** — giving your operations team the ability to search, filter, and correlate Mattermost application logs across all servers from a single Grafana interface.

With Loki in place you can:

- Search Mattermost logs across all application servers from Grafana.
- Filter by log level, HTTP status code, or free-text search.
- Identify the top recurring errors and warnings.
- Correlate log events with Prometheus metric spikes on the same timeline.
- Optionally collect PostgreSQL database logs alongside application logs.

.. tip::

   This guide assumes you have already deployed Prometheus and Grafana by following the `performance monitoring guide </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>`_. Loki and the OpenTelemetry Collector will be added to that existing infrastructure.

Architecture overview
---------------------

The deployment adds two components to your monitoring stack:

- **Loki** — the log aggregation engine, installed on your existing Grafana/Prometheus monitoring server.
- **OpenTelemetry Collector** — a versatile, industry-standard agent installed on each Mattermost application server to ship logs.

.. code-block:: text

   ┌──────────────────────┐       ┌──────────────────────┐
   │  Mattermost App 01   │       │  Mattermost App 02   │
   │                      │       │                      │
   │  /opt/mattermost/    │       │  /opt/mattermost/    │
   │   logs/mattermost.log│       │   logs/mattermost.log│
   │         │            │       │         │            │
   │    [ OTel Col ]      │       │    [ OTel Col ]      │
   └─────────┬────────────┘       └─────────┬────────────┘
             │ push (:3100/otlp)            │
             ▼                              ▼
   ┌─────────────────────────────────────────────────────┐
   │           Monitoring Server                         │
   │                                                     │
   │   [ Prometheus :9090 ]    [ Loki :3100 ]            │
   │           │                     │                   │
   │           └──────┬──────────────┘                   │
   │                  ▼                                  │
   │           [ Grafana :3000 ]                         │
   │            Metrics + Logs                           │
   └─────────────────────────────────────────────────────┘

   Optional: Add the OpenTelemetry Collector on your PostgreSQL server to also
   ship database logs to Loki.

Prerequisites
-------------

Before starting, confirm the following:

- Prometheus and Grafana are deployed and collecting Mattermost metrics per the `performance monitoring guide </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>`_.
- You have **SSH access** with sudo privileges to the monitoring server and each Mattermost application server.
- Mattermost is installed at ``/opt/mattermost`` (the default location). If your installation path differs, substitute your path wherever ``/opt/mattermost`` appears.
- **Network connectivity**: Each Mattermost server can reach the monitoring server on **TCP port 3100** (Loki's HTTP API).

Step 1: Verify Mattermost JSON logging
----------------------------------------

Mattermost must be writing JSON-formatted file logs for Loki queries to work. This is the default on all plans — verify it on each application server:

.. code-block:: bash

   tail -1 /opt/mattermost/logs/mattermost.log

A JSON-formatted line looks like:

.. code-block:: json

   {"timestamp":"2025-01-15T14:32:01.123Z","level":"info","msg":"Server is listening on [::]:8065","caller":"app/server.go:482"}

If you see plain-text output instead, go to **System Console > Environment > Logging** and set **Output file logs as JSON** to ``true``, then restart Mattermost:

.. code-block:: bash

   sudo systemctl restart mattermost

Step 2: Install Loki on the monitoring server
----------------------------------------------

Install Loki on the same server that runs Grafana and Prometheus. All commands in this section are run **on the monitoring server**.

.. important::

   The commands below use Loki version **3.4.2**. Check the `Loki releases page <https://github.com/grafana/loki/releases>`_ for the latest version and substitute the version number as needed.

1. Create the Loki user, directories, and download the binary:

   .. code-block:: bash

      # Create a dedicated system user
      sudo useradd --system --no-create-home --shell /bin/false loki

      # Create directories
      sudo mkdir -p /opt/loki/data /opt/loki/bin

      # Download and extract Loki
      cd /tmp
      curl -LO https://github.com/grafana/loki/releases/download/v3.4.2/loki-linux-amd64.zip
      unzip loki-linux-amd64.zip
      sudo mv loki-linux-amd64 /opt/loki/bin/loki
      sudo chmod +x /opt/loki/bin/loki

2. Download and install the production configuration file:

   * :download:`Download loki-config.yaml </samples/loki/loki-config.yaml>`

   .. code-block:: bash

      sudo cp loki-config.yaml /opt/loki/loki-config.yaml

   .. tip::

      **Log retention** is set to **14 days** by default. To change this, edit ``/opt/loki/loki-config.yaml`` and update the ``retention_period`` value under ``limits_config``. Loki requires this value in hours — common values:

      - ``336h`` = 14 days (default)
      - ``720h`` = 30 days
      - ``2160h`` = 90 days
      - ``8760h`` = 365 days

      Longer retention increases disk usage. As a rough guide, expect 1–3 GB per day for a moderately active Mattermost deployment (varies with log volume). Monitor ``/opt/loki/data/`` after the first week to project storage needs. The ``compactor.retention_enabled`` setting must remain ``true`` for retention enforcement to work.

3. Set ownership:

   .. code-block:: bash

      sudo chown -R loki:loki /opt/loki

4. Create a systemd service file:

   .. code-block:: bash

      sudo tee /etc/systemd/system/loki.service > /dev/null <<'EOF'
      [Unit]
      Description=Grafana Loki Log Aggregation
      Documentation=https://grafana.com/docs/loki/latest/
      After=network-online.target
      Wants=network-online.target

      [Service]
      Type=simple
      User=loki
      Group=loki
      ExecStart=/opt/loki/bin/loki -config.file=/opt/loki/loki-config.yaml
      Restart=on-failure
      RestartSec=5
      LimitNOFILE=65536
      StandardOutput=journal
      StandardError=journal

      [Install]
      WantedBy=multi-user.target
      EOF

5. Start Loki:

   .. code-block:: bash

      sudo systemctl daemon-reload
      sudo systemctl enable --now loki

6. Verify Loki is running:

   .. code-block:: bash

      sudo systemctl status loki
      curl -s http://localhost:3100/ready

   The ``/ready`` endpoint should return ``ready``.

Step 3: Install OpenTelemetry Collector on each Mattermost server
-----------------------------------------------------------------

The OpenTelemetry (OTel) Collector runs on each Mattermost application server and pushes logs to Loki. Repeat these steps on **every Mattermost application server**.

.. important::

   Replace ``<LOKI_HOST>`` with the IP address or hostname of your monitoring server, ``<HOSTNAME>`` with this server's hostname (e.g., ``mm-app-01``), and ``<SERVICE_NAME>`` with the service type (e.g., ``mattermost`` or ``postgres``).

1. Install the OTel Collector Contrib distribution:

   .. code-block:: bash

      # Add OTel Collector repository and install
      # Commands below are for Ubuntu/Debian
      wget https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.145.0/otelcol-contrib_0.145.0_linux_amd64.deb
      sudo dpkg -i otelcol-contrib_0.145.0_linux_amd64.deb

   .. note::

      The installation process automatically creates a system user and group named ``otelcol-contrib``.

2. Download and edit the OpenTelemetry Collector configuration:

   * :download:`Download otel-collector-config.yaml </samples/loki/otel-collector-config.yaml>`

   .. code-block:: bash

      sudo cp otel-collector-config.yaml /etc/otelcol-contrib/config.yaml

   Edit ``/etc/otelcol-contrib/config.yaml`` and replace the placeholders:

   - Replace ``<LOKI_HOST>`` with your monitoring server's address.
   - Replace ``<HOSTNAME>`` with this server's hostname.
   - Replace ``<SERVICE_NAME>`` with the service type (e.g., ``mattermost``).

   .. code-block:: bash

      sudo vi /etc/otelcol-contrib/config.yaml

3. Grant the collector read access to the Mattermost log directory:

   .. code-block:: bash

      # Grant the collector access to read Mattermost logs.
      # Substitute 'mattermost' for the group that owns your log file.
      sudo usermod -aG mattermost otelcol-contrib

      # Ensure logs are group-readable
      sudo chmod 640 /opt/mattermost/logs/mattermost.log
      sudo chmod g+rx /opt/mattermost/logs

      # Grant access to PostgreSQL logs (if applicable)
      sudo usermod -aG postgres otelcol-contrib

4. Restart the service:

   .. code-block:: bash

      sudo systemctl restart otelcol-contrib
      sudo systemctl enable otelcol-contrib

5. Verify the collector is running and shipping logs:

   .. code-block:: bash

      sudo systemctl status otelcol-contrib
      sudo journalctl -u otelcol-contrib -f

Step 4: Add Loki as a data source in Grafana
----------------------------------------------

1. Log in to Grafana (default: ``http://<monitoring-server>:3000``).
2. Navigate to **Administration > Data Sources > Add data source**.
3. Select **Loki** from the list.
4. Configure the connection:

   - **Name**: ``Loki``
   - **URL**: ``http://localhost:3100`` (since Loki is colocated with Grafana)
5. Select **Save & test**. Grafana should confirm the data source is working.

Step 5: Import the Mattermost Loki dashboard
----------------------------------------------

A pre-built Grafana dashboard is recommended for monitoring your logs. This dashboard is provided as a basic example:

* :download:`Download the Mattermost Loki Logs dashboard JSON </samples/grafana-dashboards/mattermost-loki-logs.json>`

.. note::
   
   While the dashboard provides a useful starting point, users can gain full query flexibility using the **Explore** tab in Grafana to build custom LogQL queries on the fly.

The dashboard provides:

- **Log Volume by Level** — stacked bar chart showing log rates by severity.
- **Error / Warning / Total counters** — stat panels for the selected time range.
- **HTTP 4xx/5xx count** — quick visibility into application-level HTTP errors.
- **Error Rate Over Time** — time series per instance for spotting error spikes.
- **Top Error Messages** — table ranking the most frequent errors.
- **Log Browser** — searchable, filterable log panel with level and free-text variables.

To import the dashboard:

1. In Grafana, go to **Dashboards > New > Import**.
2. Select **Upload JSON file** and choose the downloaded ``mattermost-loki-logs.json`` file.
3. On the import screen, select your **Loki** data source from the dropdown.
4. Select **Import**.

Step 6: Useful LogQL queries
------------------------------

You can run these queries directly in **Grafana Explore** (select the Loki data source) or use them to build additional dashboard panels.

**Search all Mattermost logs:**

.. code-block:: text

   {service_name="mattermost"}

**Filter by log level:**

.. code-block:: text

   {service_name="mattermost"} | json | detected_level="error"

**Search for all HTTP 4xx responses:**

.. code-block:: text

   {service_name="mattermost"} | json | status_code >= 400

**Search for all HTTP 5xx responses:**

.. code-block:: text

   {service_name="mattermost"} | json | status_code >= 500

**Top 5 error messages over 5-minute windows:**

.. code-block:: text

   topk(5, sum(count_over_time({service_name="mattermost"} | json | detected_level="error" [5m])) by (msg))

**Count errors by message over 5-minute windows:**

.. code-block:: text

   sum(count_over_time({service_name="mattermost"} | json | detected_level="error" [5m])) by (msg)

**Free-text search (e.g., plugin errors):**

.. code-block:: text

   {service_name="mattermost"} |~ "plugin"

**Authentication-related log lines:**

.. code-block:: text

   {service_name="mattermost"} |~ "(?i)(auth|login|token|session)"

**Logs from a specific server instance:**

.. code-block:: text

   {service_name="mattermost", service_instance_id="mm-app-01"}

.. tip::

   For a full LogQL reference, see the `Grafana Loki LogQL documentation <https://grafana.com/docs/loki/latest/query/>`_.

Optional: Add PostgreSQL log collection
-----------------------------------------

If your PostgreSQL database runs on a dedicated server (not RDS), you can ship its logs to Loki as well. This is useful for correlating slow queries or database errors with Mattermost application events.

1. Install the OpenTelemetry Collector on the PostgreSQL server using the same steps from **Step 3**.
2. Documentation for PostgreSQL log location varies by installation, but the provided config handles common Ubuntu/Debian JSON log paths.
3. Once running, PostgreSQL logs appear in Grafana under the label ``{service_name="postgres"}``:

   .. code-block:: text

      {service_name="postgres"} | json | detected_level="error"

Verification and troubleshooting
----------------------------------

**End-to-end verification checklist:**

1. Loki is healthy:

   .. code-block:: bash

      curl -s http://<monitoring-server>:3100/ready
      # Expected: "ready"

2. OpenTelemetry Collector is shipping logs (run on each Mattermost server):

   .. code-block:: bash

      sudo journalctl -u otelcol-contrib -n 100
      # Look for export successful messages or lack of errors

3. Logs are visible in Grafana: Go to **Explore**, select the **Loki** data source, and run ``{service_name="mattermost"}``. You should see recent log lines.

4. The dashboard loads: Open the **Mattermost Log Aggregation** dashboard and confirm panels are populated. (Note: You may need to update dashboard queries to use `service_name` and `service_instance_id`).

**Common issues:**

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Symptom
     - Resolution
   * - OTel Col target shows errors
     - Verify the file paths in the config match the actual log file location. Check file permissions (``otelcol-contrib`` user must be able to read the file).
   * - ``connection refused`` on port 3100
     - Ensure Loki is running (``systemctl status loki``). Check firewall rules: ``sudo iptables -L -n | grep 3100`` or check your AWS security group allows TCP 3100 from the Mattermost servers.
   * - Logs appear in Loki but fields aren't parsed
     - Confirm Mattermost is writing JSON-formatted logs (see Step 1). Check that the ``json_parser`` operator (for Postgres) or OTel processors are correctly configured.
   * - ``/ready`` returns an error
     - Check Loki logs: ``sudo journalctl -u loki -f``. Common cause: permissions on ``/opt/loki/data/`` — ensure the ``loki`` user owns the directory.
   * - Old logs are not being deleted
     - Verify ``compactor.retention_enabled: true`` and ``limits_config.retention_period`` are both set in the Loki config. The compactor runs on the ``compaction_interval`` (default: 10 minutes) and applies a ``retention_delete_delay`` (default: 2 hours) before actually removing data.
   * - High disk usage on the monitoring server
     - Review the retention period in the configuration. Consider reducing it or adding more disk. Check ``du -sh /opt/loki/data/`` to see current usage.
