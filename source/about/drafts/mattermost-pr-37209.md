# Add mattermost_system_server_info metric exposing version and build info

> **Status:** Draft - auto-generated. Requires editorial review.
> **Source:** [mattermost/mattermost#37209](https://github.com/mattermost/mattermost/pull/37209)
> **Dev reviewer:** @lieut-data

---

=== CAPABILITY SUMMARY ===

**Capability change (one sentence):** Admins can now query Prometheus for `mattermost_system_server_info` to determine exactly which version and build each Mattermost server instance is running.

**PARITY or NET-NEW:** NET-NEW

**Docs scope:** Update existing

**Target personas:** System Admin, IT Service Operations

---

=== DOCUMENTATION DRAFT ===

**Recommended doc location:**
- Mattermost Prometheus metrics reference page (likely: "Performance monitoring" or "Metrics reference" in the administration docs)

---

**Proposed content (ready to paste):**

### `mattermost_system_server_info`

From Mattermost v11.9.0, a new info-style Prometheus gauge is available:

```
mattermost_system_server_info{version="...", build_number="...", build_hash="...", build_hash_enterprise="..."} 1
```

**Subsystem:** `system`

**Type:** Gauge (always `1`; version and build data are exposed as labels)

**Labels:**

| Label | Description |
|---|---|
| `version` | The running server version (e.g., `11.9.0`) |
| `build_number` | The CI build number |
| `build_hash` | The Git commit hash of the server build |
| `build_hash_enterprise` | The Git commit hash of the enterprise build |

On cloud deployments, this metric also includes the standard cloud `ConstLabels` (installation ID, group, database cluster).

**Set:** Once at server startup; value does not change at runtime.

**Example query:** To confirm which version is running across all instances in an environment:

```promql
count by (version) (mattermost_system_server_info)
```

---

**Notes:**

- This metric follows the standard [Prometheus info metric pattern](https://www.robustperception.io/exposing-the-software-version-to-prometheus/): the gauge value is always `1`; meaningful data is in the labels.
- If the product's metrics reference docs organize metrics by subsystem, add this entry under the `system` subsystem alongside `mattermost_system_server_start_time`.
- Verify the exact page name and existing table/list structure before inserting — the draft above is formatted to match a typical tabular metrics reference section. [NOT PRESENT IN PR — REQUIRES HUMAN JUDGMENT]
