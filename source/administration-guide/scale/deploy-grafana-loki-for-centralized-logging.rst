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

   This guide assumes you have already deployed Prometheus and Grafana by following the `performance monitoring guide </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>`_. Loki and Promtail will be added to that existing infrastructure.

Architecture overview
---------------------

The deployment adds two components to your monitoring stack:

- **Loki** — the log aggregation engine, installed on your existing Grafana/Prometheus monitoring server.
- **Promtail** — a lightweight log-shipping agent, installed on each Mattermost application server.

.. code-block:: text

   ┌──────────────────────┐       ┌──────────────────────┐
   │  Mattermost App 01   │       │  Mattermost App 02   │
   │                      │       │                      │
   │  /opt/mattermost/    │       │  /opt/mattermost/    │
   │   logs/mattermost.log│       │   logs/mattermost.log│
   │         │            │       │         │            │
   │    [ Promtail ]      │       │    [ Promtail ]      │
   └─────────┬────────────┘       └─────────┬────────────┘
             │ push (:3100)                  │
             ▼                               ▼
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

   Optional: Add Promtail on your PostgreSQL server to also
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

2. Create the production configuration file named ``/opt/loki/loki-config.yaml``:

   .. code-block:: yaml

      # Grafana Loki configuration for Mattermost log aggregation
      # This is a production-ready config for a single-instance deployment
      # colocated with an existing Grafana/Prometheus monitoring server.
      
      auth_enabled: false
      
      server:
        http_listen_port: 3100
        grpc_listen_port: 9096
        log_level: warn
      
      common:
        instance_addr: 127.0.0.1
        path_prefix: /opt/loki/data
        storage:
          filesystem:
            chunks_directory: /opt/loki/data/chunks
            rules_directory: /opt/loki/data/rules
        replication_factor: 1
        ring:
          kvstore:
            store: inmemory
      
      # ---------------------------------------------------------------------------
      # Retention settings
      # ---------------------------------------------------------------------------
      # Loki requires retention to be specified in hours (h). The default here
      # is 14 days. To change it, update retention_period below.
      #
      # Common values:
      #   336h   = 14 days  (default)
      #   720h   = 30 days
      #   2160h  = 90 days
      #   8760h  = 365 days
      # ---------------------------------------------------------------------------
      limits_config:
        retention_period: 336h          # 14 days (336 hours) — adjust as needed
        metric_aggregation_enabled: true
      
      compactor:
        working_directory: /opt/loki/data/compactor
        compaction_interval: 10m
        retention_enabled: true         # must be true for retention_period to apply
        retention_delete_delay: 2h
        retention_delete_worker_count: 150
        delete_request_store: filesystem
      
      schema_config:
        configs:
          - from: "2024-01-01"
            store: tsdb
            object_store: filesystem
            schema: v13
            index:
              prefix: index_
              period: 24h
      
      query_range:
        results_cache:
          cache:
            embedded_cache:
              enabled: true
              max_size_mb: 100
      
      ruler:
        alertmanager_url: http://localhost:9093
      
      frontend:
        encoding: protobuf

   .. tip::

      **Log retention** is set to **14 days** by default. To change this, update the ``retention_period`` value under ``limits_config``. Longer retention increases disk usage (roughly 1–3 GB per day for moderately active deployments). The ``compactor.retention_enabled`` setting must remain ``true`` for retention enforcement to work.

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

Step 3: Install Promtail on each Mattermost server
----------------------------------------------------

Promtail runs on each Mattermost application server and pushes logs to Loki. Repeat these steps on **every Mattermost application server**.

.. important::

   Replace ``<LOKI_HOST>`` with the IP address or hostname of your monitoring server, and ``<MM_HOSTNAME>`` with this server's hostname (e.g., ``mm-app-01``).

1. Create the Promtail user, directories, and download the binary:

   .. code-block:: bash

      # Create a dedicated system user
      sudo useradd --system --no-create-home --shell /bin/false promtail

      # Create directories
      sudo mkdir -p /opt/promtail/bin

      # Download and extract Promtail
      cd /tmp
      curl -LO https://github.com/grafana/loki/releases/download/v3.4.2/promtail-linux-amd64.zip
      unzip promtail-linux-amd64.zip
      sudo mv promtail-linux-amd64 /opt/promtail/bin/promtail
      sudo chmod +x /opt/promtail/bin/promtail

2. Create the Promtail configuration file named ``/opt/promtail/promtail-config.yaml``:

   .. code-block:: yaml

      server:
        http_listen_port: 9080
        grpc_listen_port: 0
      
      positions:
        filename: /opt/promtail/positions.yaml
      
      clients:
        - url: http://<LOKI_HOST>:3100/loki/api/v1/push
      
      scrape_configs:
        - job_name: mattermost
          static_configs:
            - targets:
                - localhost
              labels:
                service_name: app
                job: mattermost
                instance: "<MM_HOSTNAME>"
                __path__: /opt/mattermost/logs/mattermost.log
      
          pipeline_stages:
            - json:
                expressions:
                  level: level
                  msg: msg
                  caller: caller
                  status_code: status_code
            - labels:
                level:
            - structured_metadata:
                msg:
                caller:
                worker_name:
                job_id:
                log_file_name:
            - timestamp:
                source: timestamp
                format: "2006-01-02T15:04:05.000Z07:00"
                fallback_formats:
                  - "2006-01-02T15:04:05Z07:00"
                  - "RFC3339"

   Replace the placeholders:
   - Replace ``<LOKI_HOST>`` with your monitoring server's address.
   - Replace ``<MM_HOSTNAME>`` with this server's hostname.

3. Grant Promtail read access to the Mattermost log directory:

   .. code-block:: bash

      sudo usermod -aG mattermost promtail
      sudo chmod 640 /opt/mattermost/logs/mattermost.log
      sudo chmod g+rx /opt/mattermost/logs

   .. note::

      If Mattermost does not run under a ``mattermost`` group, adjust the group name accordingly. The key requirement is that the ``promtail`` user can read the log file.

4. Set ownership:

   .. code-block:: bash

      sudo chown -R promtail:promtail /opt/promtail

5. Create a systemd service file:

   .. code-block:: bash

      sudo tee /etc/systemd/system/promtail.service > /dev/null <<'EOF'
      [Unit]
      Description=Grafana Promtail Log Agent
      Documentation=https://grafana.com/docs/loki/latest/send-data/promtail/
      After=network-online.target
      Wants=network-online.target

      [Service]
      Type=simple
      User=promtail
      Group=promtail
      ExecStart=/opt/promtail/bin/promtail -config.file=/opt/promtail/promtail-config.yaml
      Restart=on-failure
      RestartSec=5
      StandardOutput=journal
      StandardError=journal

      [Install]
      WantedBy=multi-user.target
      EOF

6. Start Promtail:

   .. code-block:: bash

      sudo systemctl daemon-reload
      sudo systemctl enable --now promtail

7. Verify Promtail is running and tailing logs:

   .. code-block:: bash

      sudo systemctl status promtail

      # Check Promtail's targets page (from the Mattermost server itself)
      curl -s http://localhost:9080/targets

   The targets page should show your ``mattermost`` job with the log file path and a ``READY`` state.

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

A pre-built Grafana dashboard is recommended for monitoring your logs. This dashboard serves as a basic example to get started:

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

   {service_name="app"}

**Filter by log level:**

.. code-block:: text

   {service_name="app"} | json | level="error"

**Search for all HTTP 4xx responses:**

.. code-block:: text

   {service_name="app"} | json | status_code >= 400

**Search for all HTTP 5xx responses:**

.. code-block:: text

   {service_name="app"} | json | status_code >= 500

**Top 5 error messages over 5-minute windows:**

.. code-block:: text

   topk(5, sum(count_over_time({service_name="app"} | json | level="error" [5m])) by (msg))

**Count errors by message over 5-minute windows:**

.. code-block:: text

   sum(count_over_time({service_name="app"} | json | level="error" [5m])) by (msg)

**Free-text search (e.g., plugin errors):**

.. code-block:: text

   {service_name="app"} |~ "plugin"

**Authentication-related log lines:**

.. code-block:: text

   {service_name="app"} |~ "(?i)(auth|login|token|session)"

**Logs from a specific server instance:**

.. code-block:: text

   {service_name="app", instance="mm-app-01"}

.. tip::

   For a full LogQL reference, see the `Grafana Loki LogQL documentation <https://grafana.com/docs/loki/latest/query/>`_.

Optional: Add PostgreSQL log collection
-----------------------------------------

If your PostgreSQL database runs on a dedicated server (not RDS), you can ship its logs to Loki as well. This is useful for correlating slow queries or database errors with Mattermost application events.

1. Install Promtail on the PostgreSQL server using the same steps from **Step 3** (create user, download binary, create systemd unit).
2. Create the Promtail configuration file named ``/opt/promtail/promtail-config.yaml``:

   .. code-block:: yaml

      server:
        http_listen_port: 9080
        grpc_listen_port: 0
      
      positions:
        filename: /opt/promtail/positions-postgres.yaml
      
      clients:
        - url: http://<LOKI_HOST>:3100/loki/api/v1/push
      
      scrape_configs:
        - job_name: postgres
          static_configs:
            - targets:
                - localhost
              labels:
                service_name: postgres
                job: postgres
                instance: "<PG_HOSTNAME>"
                __path__: /var/log/postgresql/*.json
      
          pipeline_stages:
            - json:
                expressions:
                  timestamp: timestamp
                  level: error_severity
                  msg: message
                  pid: pid
                  user_name: user
                  database_name: dbname
                  application_name: application_name
            - labels:
                level:
            - structured_metadata:
                user_name:
                database_name:
                application_name:
            - timestamp:
                source: timestamp
                format: "2006-01-02 15:04:05.000 MST"

   - Replace ``<LOKI_HOST>`` with your monitoring server's address.
   - Replace ``<PG_HOSTNAME>`` with this server's hostname.
   - Adjust the ``__path__`` to match your PostgreSQL log location.

3. Ensure the ``promtail`` user can read the PostgreSQL log directory:

   .. code-block:: bash

      sudo usermod -aG postgres promtail
      sudo chmod g+rx /var/lib/pgsql/15/data/log

4. Start Promtail:

   .. code-block:: bash

      sudo systemctl enable --now promtail

5. Once running, PostgreSQL logs appear in Grafana under the label ``{service_name="postgres"}``:

   .. code-block:: text

      {service_name="postgres"} | level="ERROR"

Verification and troubleshooting
----------------------------------

**End-to-end verification checklist:**

1. Loki is healthy:

   .. code-block:: bash

      curl -s http://<monitoring-server>:3100/ready
      # Expected: "ready"

2. Promtail is shipping logs (run on each Mattermost server):

   .. code-block:: bash

      curl -s http://localhost:9080/targets
      # Look for your mattermost job showing READY

3. Logs are visible in Grafana: Go to **Explore**, select the **Loki** data source, and run ``{service_name="app"}``. You should see recent log lines.

4. The dashboard loads: Open the **Mattermost Log Aggregation** dashboard and confirm panels are populated.

**Common issues:**

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Symptom
     - Resolution
   * - Promtail target shows ``DROPPED``
     - Verify the ``__path__`` in the Promtail config matches the actual log file location. Check file permissions (``promtail`` user must be able to read the file).
   * - ``connection refused`` on port 3100
     - Ensure Loki is running (``systemctl status loki``). Check firewall rules: ``sudo iptables -L -n | grep 3100`` or check your AWS security group allows TCP 3100 from the Mattermost servers.
   * - Logs appear in Loki but fields aren't parsed
     - Confirm Mattermost is writing JSON-formatted logs (see Step 1). Check that the ``pipeline_stages`` in your Promtail config include the ``json`` stage.
   * - ``/ready`` returns an error
     - Check Loki logs: ``sudo journalctl -u loki -f``. Common cause: permissions on ``/opt/loki/data/`` — ensure the ``loki`` user owns the directory.
   * - Old logs are not being deleted
     - Verify ``compactor.retention_enabled: true`` and ``limits_config.retention_period`` are both set in the Loki config. The compactor runs on the ``compaction_interval`` (default: 10 minutes) and applies a ``retention_delete_delay`` (default: 2 hours) before actually removing data.
   * - High disk usage on the monitoring server
     - Review the retention period in the configuration. Consider reducing it or adding more disk. Check ``du -sh /opt/loki/data/`` to see current usage.
