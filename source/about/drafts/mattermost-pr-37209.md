# Add mattermost_system_server_info metric exposing version and build info

> **Status:** Draft - auto-generated. Requires editorial review.
> **Source:** [mattermost/mattermost#37209](https://github.com/mattermost/mattermost/pull/37209)
> **Dev reviewer:** @lieut-data

---

=== CAPABILITY SUMMARY ===

Capability change (one sentence): Admins can now query a new `mattermost_system_server_info` Prometheus metric to determine the exact version and build information of each running Mattermost server instance.

PARITY or NET-NEW: NET-NEW

Docs scope: Update existing

Target personas: System Admin, IT Service Operations

---

=== DOCUMENTATION DRAFT ===

**Recommended doc location:**
- Primary: Mattermost Performance Monitoring / Metrics reference documentation (the page listing available Prometheus metrics)
- Secondary: Any deployment monitoring or observability guide that references Mattermost Prometheus metrics

---

**Proposed content (ready to paste):**

### `mattermost_system_server_info`

From Mattermost v11.9.0, a new info-style gauge metric is available:

```
mattermost_system_server_info{version="...", build_number="...", build_hash="...", build_hash_enterprise="..."} 1
```

**Subsystem:** `system`

**Type:** Gauge (always `1`; version and build data are encoded in labels)

**Labels:**

| Label | Description |
|---|---|
| `version` | The Mattermost server version string (e.g., `11.9.0`) |
| `build_number` | The build number assigned at release |
| `build_hash` | The Git commit hash of the server build |
| `build_hash_enterprise` | The Git commit hash of the enterprise build |

On Cloud deployments, the metric also includes existing `ConstLabels` such as `installationId`, group, and database cluster identifiers.

The metric is registered once at server startup and does not change at runtime.

**Example query:**

Use the following PromQL query to confirm deployment rollout across your fleet:

```promql
count by (version) (mattermost_system_server_info)
```

This returns a count of server instances grouped by version, which is useful for verifying that a deploy or rollout has reached all nodes.

---

**Notes:**

- The metric follows the standard [Prometheus "info metric" pattern](https://www.robustperception.io/exposing-the-software-version-to-prometheus/): the gauge is always `1` and meaningful data is in the labels.
- milestone.title: `v11.9.0` — version reference is confirmed.
- [NOT PRESENT IN PR — REQUIRES HUMAN JUDGMENT]: Confirm whether Cloud-specific `ConstLabels` (installationId, etc.) should be documented in the public-facing metrics reference, or if that section is Cloud-internal only.
