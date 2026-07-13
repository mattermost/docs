# Add mattermost_system_server_info metric exposing version and build info

> **Status:** Draft - auto-generated. Requires editorial review.
> **Source:** [mattermost/mattermost#37209](https://github.com/mattermost/mattermost/pull/37209)
> **Dev reviewer:** @lieut-data

---

=== CAPABILITY SUMMARY ===

Capability change (one sentence): Administrators can now query Prometheus for the exact server version and build details (version, build number, build hash, enterprise build hash) running on each Mattermost instance using the new `mattermost_system_server_info` metric.

PARITY or NET-NEW: NET-NEW

Docs scope: Update existing

Target personas: System Admin, IT Service Operations

---

=== DOCUMENTATION DRAFT ===

**Recommended doc location:**
- Mattermost Performance Monitoring / Metrics Reference page (the page documenting available Prometheus metrics)

---

**Proposed content (ready to paste):**

#### Server info metric

From Mattermost v11.9.0, a new Prometheus info metric is available:

```
mattermost_system_server_info
```

This gauge is always set to `1` and exposes the running server's version and build details as labels. It is registered at server startup.

**Labels:**

| Label | Description |
|---|---|
| `version` | Current Mattermost server version |
| `build_number` | Build number |
| `build_hash` | Git commit hash of the server build |
| `build_hash_enterprise` | Git commit hash of the enterprise build |

On cloud deployments, the metric also includes the existing cloud `ConstLabels` (installation ID, group, database cluster).

**Example query:**

To confirm which version is running across all servers in an environment:

```promql
count by (version) (mattermost_system_server_info)
```

This is useful for verifying that a deployment or cherry-pick has fully rolled out.

---

**Notes:**
- This follows the standard [Prometheus info metric pattern](https://www.robustperception.io/how-to-have-labels-for-machine-roles-in-prometheus/) (fixed gauge value of `1`, data carried in labels).
- The metric is registered once at startup; no ongoing collection cost.
- milestone.title: `v11.9.0` — used as version reference per PR metadata.
