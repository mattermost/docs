# Deploy Mattermost Calls

This guide walks an IT administrator through deploying Mattermost Calls in four phases: planning and preparing your infrastructure, deploying in a controlled environment, pilot testing, and rolling out to production. 

| Section | Description |
|---------|-------------|
| [Phase 0: Plan & Prepare](#phase-0-plan--prepare) | Architecture diagram, infrastructure checklist, deployment decisions (SFU mode, recording, network traversal), ports reference, and air-gapped considerations |
| [Phase 1: Deploy](#phase-1-deploy) | Configure Calls for Integrated or RTCD mode, deploy the calls-offloader (optional), enable the plugin, and verify your setup |
| [Phase 2: Pilot Testing](#phase-2-pilot-testing) | Admin-controlled test scenarios for 1:1 calls, group calls, screen sharing, recording, and live captions before widening access |
| [Phase 3: Production Rollout](#phase-3-production-rollout) | Production configuration, incremental channel rollout, user announcement, monitoring, and rollback plan |
| [Appendix A: Troubleshooting by Symptom](#appendix-a-troubleshooting-by-symptom) | Causes and fixes organized by error symptom, plus a diagnostic commands quick reference |
| [Appendix B: Frequently Asked Questions](#appendix-b-reference-information) | Encryption, STUN, UDP vs. TCP, monitoring endpoints, Grafana dashboard, and documentation links |
| [Appendix C: Performance and Sizing](#appendix-c-performance-and-sizing) | RTCD and recording server sizing benchmarks and Linux kernel tuning |
| [Appendix D: Advanced Network Diagnostics](#appendix-d-advanced-network-diagnostics) | MTU path discovery, PMTUD verification, and bandwidth testing — for network teams |
| [Appendix E: Glossary](#appendix-e-glossary) | Definitions for WebRTC, SFU, ICE, STUN, TURN, DTLS, SRTP, and other key terms |

**Quick Links**
- {doc}`RTCD Setup and Configuration <calls-rtcd-setup>` — Full RTCD installation, configuration, and horizontal scaling
- {doc}`Calls Offloader Setup and Configuration <calls-offloader-setup>` — Deploying calls-offloader for recording, transcription, and live captions
- {doc}`Calls Deployment on Kubernetes <calls-kubernetes>` — Helm charts, network policies, and Kubernetes-specific guidance
- {doc}`Calls Metrics and Monitoring <calls-metrics-monitoring>` — Prometheus, Grafana, and performance baselines
- [Calls Log Collection](calls-log-collection.md) — How to gather logs for debugging and support
- [Plugin Configuration Settings](https://docs.mattermost.com/configure/plugins-configuration-settings.html#calls) — Full reference for all System Console settings

---

#### Reaching Mattermost Support

Every step in this guide is numbered hierarchically so you can track exactly where you are and reference precise steps if you need to work with Mattermost Support.

When [filing a support ticket](https://support.mattermost.com), please:
- Attach your Mattermost support packet. For instructions on generating this packet, see {doc}`Generating a support packet <../../administration-guide/manage/admin/generating-support-packet>`. Remember to review and sanitize any confidential information as required.
- The exact step number where the issue occurred (e.g., "Failed at step 1.4 — UDP port unreachable from client network")
- Logs if your security policy permits — see [Calls Log Collection](calls-log-collection.md) for how to gather them.


---

## Phase 0: Plan & Prepare

Before deploying anything, use this phase to understand the full architecture, make key decisions that shape your deployment, and confirm your infrastructure is ready. Do not proceed to Phase 1 until every item in this phase is resolved.

### 0.1 Infrastructure Prerequisites

Confirm every item before proceeding to Section 0.2.

| Requirement | Notes |
|-------------|-------|
| Mattermost server v7.1+ running on HTTPS/TLS | Required by browsers to access microphone and screen sharing. See [Configure TLS](https://docs.mattermost.com/deploy/server/setup-tls.html). |
| System Admin access to System Console | Required to configure the Calls plugin |
| License level confirmed | See table below |
| Network firewall access to open required ports | See Section 0.3 |
| DNS entry or static IP for the Calls service endpoint | Required if configuring ICE Host Override |
| Dedicated dev/staging Mattermost instance available | Strongly recommended — do not configure Calls for the first time on a production instance |

**License requirements:**

| License            | What is included                                           |
|--------------------|------------------------------------------------------------|
| Entry+             | 1:1 audio calls with optional screen sharing               |
| Professional+      | Group calls with up to 50 concurrent users                 |
| Enterprise+        | RTCD service, call recording, live captions, transcription |

---

### 0.2 Deployment Decisions

Make these three decisions before configuring anything. Your answers determine what additional infrastructure to prepare.

#### Decision 0.2.1: SFU Mode

The SFU (Selective Forwarding Unit) is the engine that routes audio and video between call participants. It runs either inside the Calls plugin on your Mattermost server (Integrated mode) or on a separate dedicated service (RTCD mode).

| Feature                          | Integrated Mode                                                             | RTCD Mode                                                        |
|-----------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------------|
| **What it is**                    | WebRTC runs inside the Calls plugin on the Mattermost server               | Dedicated standalone service handles all media routing            |
| **Best for**                      | Evaluation, small teams (under 50 users), single-instance deployments      | Production, 50+ concurrent users, HA clusters, Kubernetes        |
| **License required**              | Entry+                                                                     | Enterprise+                                                      |
| **Impact on Mattermost server**    | Calls traffic shares CPU and memory with Mattermost                        | None — calls fully isolated from Mattermost                      |
| **Scalability**                   | Limited by Mattermost server resources                                     | Horizontal: add RTCD nodes as needed                             |
| **Kubernetes**                    | Not supported                                                              | Required — only officially supported option                      |

**Choose RTCD if any of the following apply:**

- Production deployment expected to host 50 or more calls users
- High availability (HA) cluster-based Mattermost deployment
- Kubernetes Mattermost deployment
- You want to protect Mattermost server responsiveness from calls traffic spikes
- You see the 50-session warning appear in System Console (this is your operational signal to add RTCD)

```{note}
RTCD adds operational complexity, maintenance overhead, and requires an Enterprise license. Start with Integrated mode for evaluation — you can migrate to RTCD later without disrupting existing calls.
```

**If you choose RTCD, prepare:**
- A dedicated server or container for the `rtcd` service
- Port 8443 UDP/TCP open (RTC media — client-facing)
- Port 8045 TCP open (API — internal, Mattermost to RTCD only; never expose publicly)
- Enterprise license

For full RTCD setup, see {doc}`RTCD Setup and Configuration <calls-rtcd-setup>`.

---

#### Decision 0.2.2: Recording & Transcription

Recording calls, generating live captions, and transcribing recordings are resource-intensive operations. They must run on a separate service — `calls-offloader` — to prevent degrading your Mattermost server or RTCD service. All three features require an Enterprise license.

**You need calls-offloader if you want:**
- Call recording
- Post-call transcription
- Live captions during calls

**If you choose calls-offloader, prepare:**
- A dedicated server (recommended: 8 vCPU / 16 GB RAM — see [Appendix C](#appendix-c-performance-and-sizing) for detailed sizing by recording quality)
- Port 4545 TCP open from Mattermost server to calls-offloader (internal only — never expose publicly)
- Enterprise license

For full offloader setup, see {doc}`Calls Offloader Setup and Configuration <calls-offloader-setup>`.

---

#### Decision 0.2.3: Network Traversal

The concepts below determine whether clients outside your local network can reach the Calls service.

**What each option does:**

| Option | What it does | When to use it |
|--------|-------------|----------------|
| **STUN** | Automatically tells the Mattermost server (or `rtcd`) its own public IP address, so clients outside the local network can find it. Mattermost provides a default STUN server (`stun.global.calls.mattermost.com`). | Server is behind NAT and you do not know the public IP in advance |
| **ICE Host Override** | You manually specify the IP or hostname clients use to reach the server — no external discovery needed. | Server is behind NAT and you know the public IP, or air-gapped environment |
| **TURN** | A relay server that forwards all media traffic for clients that cannot connect directly (e.g., behind strict firewalls blocking all UDP). Adds latency and infrastructure cost. | Clients behind firewalls that block UDP entirely |

**Decision path:**

1. Do clients connect from outside the server's local network (your server is behind NAT)?
   - **No** → No STUN, ICE Host Override, or TURN needed. Default settings work.
   - **Yes** → Continue to step 2.

2. Do you know your server's public IP or hostname?
   - **Yes** → Set [ICE Host Override](https://docs.mattermost.com/configure/plugins-configuration-settings.html#ice-host-override) to that IP or hostname. Simpler — no external dependency.
   - **No** → Use STUN (already configured by default). Requires outbound UDP port 3478.

3. Are you in an air-gapped environment?
   - **Yes** → Remove the default STUN server. Set ICE Host Override to the local IP reachable by all clients. See Section 0.4.

4. Do clients connect from networks with strict firewalls that block all UDP?
   - **Yes** → Deploy a TURN server ([coturn](https://github.com/coturn/coturn) is recommended). This is an additional server with infrastructure cost — use only when required.

---

### 0.3 Network Ports Reference

The diagram below shows all Mattermost Calls components and how they connect. Ensure these ports are open on all firewalls, security groups, and network appliances between clients and the Calls service before proceeding to Phase 1.

```{mermaid}
flowchart TB
    clients["Clients
    (Web / Desktop / Mobile)"] -->|"443 TCP - signaling and API"| mmServer["MM Server + Calls Plugin
    (required)"]
    clients -->|"8443 UDP/TCP - media"| mmServer
    clients -.->|"8443 UDP/TCP - media"| rtcdSvc
    mmServer -->|"8045 TCP - internal only"| rtcdSvc
    mmServer -->|"4545 TCP - internal only"| offloaderSvc
    
    rtcdSvc["rtcd Service
    (optional - Enterprise)"]
    offloaderSvc["calls-offloader
    (optional - Enterprise)"]
    
    style rtcdSvc stroke-dasharray: 5 5
    style offloaderSvc stroke-dasharray: 5 5
```
Solid lines indicate required connections. Dashed lines indicate optional or conditional connections.

```{caution}
**Common Pitfall — UDP Port 8443 blocked**: This is the single most common cause of call connection failures. Many firewalls block all UDP by default and must be explicitly configured to allow it. Verify UDP 8443 is open from client networks to the Calls server before any testing.
```

| Service | Port | Protocol | Direction | Source | Target | Purpose |
|---------|------|----------|-----------|--------|--------|---------|
| API (Calls plugin) | 80, 443 | TCP | Incoming | Clients (web/desktop/mobile) | Mattermost server | HTTP and WebSocket from clients to Calls plugin. Shared with Mattermost — no change usually needed. |
| RTC (Calls plugin or `rtcd`) | 8443 | UDP | Incoming | Clients + calls-offloader jobs | Mattermost server or `rtcd` | Primary media port. Must be open for audio and video to flow. |
| RTC (Calls plugin or `rtcd`) | 8443 | TCP | Incoming | Clients + calls-offloader jobs | Mattermost server or `rtcd` | TCP fallback when clients cannot use UDP. Requires Calls plugin ≥ v0.17 and `rtcd` ≥ v0.11. |
| API (`rtcd`) | 8045 | TCP | Incoming | Mattermost server | `rtcd` service | Internal coordination between Calls plugin and RTCD. Keep on private network only. |
| API (`calls-offloader`) | 4545 | TCP | Incoming | Mattermost server | `calls-offloader` | Recording and transcription job coordination. Internal only — never expose publicly. |
| STUN | 3478 | UDP | Outgoing | Mattermost server or `rtcd` | Configured STUN servers | Public IP discovery. Not needed if ICE Host Override is set or in air-gapped deployments. |

```{caution}
**Common Pitfall — NGINX and UDP**: NGINX handles HTTP/WebSocket (TCP) only. It cannot proxy UDP. If Mattermost sits behind NGINX, UDP port 8443 traffic must bypass NGINX and reach the Mattermost server (or `rtcd`) directly. Do not attempt to proxy UDP through NGINX.
```

---

### 0.4 Air-Gapped Considerations

Skip this section if your deployment has internet connectivity.

For air-gapped environments, complete these steps before Phase 1:

**0.4.1:** Remove the default STUN server from Calls plugin settings — `stun.global.calls.mattermost.com` is unreachable in air-gapped networks and causes timeout delays on every call attempt.

**0.4.2:** Set [ICE Host Override](https://docs.mattermost.com/configure/plugins-configuration-settings.html#ice-host-override) to the local IP address reachable by all clients (e.g., `192.168.1.45`).

**0.4.3:** Confirm all clients will connect from within the private network — on-premises, VPN, or virtual machine.

**0.4.4:** If deploying calls-offloader, see the [Air-Gapped Deployments](calls-offloader-setup.md#air-gapped-deployments) section of the Calls Offloader Setup guide for bundle preparation and deployment scripts.


```{caution}
**Common Pitfall — STUN left configured in air-gapped deployments**: Remove the default STUN server entry if your network cannot reach the internet. Leaving it configured causes a timeout delay at the start of every call attempt.
```

---

## Phase 1: Deploy

### 1.0 Prerequisites

Confirm the following before starting Phase 1:

- [ ] All Phase 0 decisions made (SFU mode, offloader, network traversal)
- [ ] Infrastructure checklist from Section 0.1 complete
- [ ] Required ports confirmed open (Section 0.3)
- [ ] At least two test user accounts available on the dev/staging instance
- [ ] System Admin credentials available

---

### 1.1 Configure Calls

Choose your path depending on if you will use Integrated mode or RTCD mode as determined by Decision 0.2.1.

#### Path A: Integrated Mode

Navigate to **System Console > Plugins > Calls** on your dev/staging instance.

Configure the following settings:

| Setting | Recommended Value | Notes |
|---------|------------------|-------|
| **RTC Server Port** | `8443` | UDP/TCP port for call media. Must match what is open in your firewall. Range: 80–49151. |
| **ICE Host Override** | *(blank or public IP)* | Set to the public IP or hostname clients use to reach this server if behind NAT. Set to a local IP for air-gapped. Leave blank only if using STUN for auto-discovery. |
| **ICE Host Port Override** | *(blank unless needed)* | Set only if the external port differs from RTC Server Port — for example, behind a NAT or load balancer that remaps ports. |
| **Max Call Participants** | `50` | Recommended maximum for integrated mode. Actual capacity depends on server hardware. |
| **Enable Test Mode** | `true` | Enables per-channel call control for a controlled rollout. Keep enabled through Phase 3. |
| **STUN Server** | `stun:stun.global.calls.mattermost.com:3478` | Remove for air-gapped deployments. No call content or metadata is sent to this service. |
| **TURN Server** | *(blank unless needed)* | Configure only if clients cannot reach the server via UDP (see Decision 3 in Section 0.2). |
| **Allow Screen Sharing** | `true` | Set to `false` if your organization restricts screen sharing. |
| **Enable Ringing** | *(optional)* | Enables ring notifications for direct message and group message calls. |
| **Enable Simulcast** | *(optional)* | Improves screen sharing quality for participants on varying bandwidth connections. |

```{caution}
**Common Pitfall — ICE Host Override not set behind NAT**: If your server is behind NAT and ICE Host Override is blank with no STUN server configured, clients outside the local network cannot discover the server's real IP and calls will fail to connect.
```

Integrated mode deployment reference:

![A diagram of the integrated configuration model of a single instance.](../../images/calls-deployment-image3.png)

**Advanced settings** (leave at defaults unless you have a specific requirement):

| Setting | Default | Notes |
|---------|---------|-------|
| Enable IPv6 | Off | Enable for dual-stack IPv6 environments. |
| Enable AV1 | Off | Newer video codec for screen sharing. Better quality at lower bitrates but requires modern browsers. Experimental. |
| Enable DC Signaling | Off | Uses data channel for signaling instead of WebSocket. May improve reliability in some network configurations. Experimental. |
| TURN Static Auth Secret | *(blank)* | Shared secret for generating time-limited TURN credentials. |
| TURN Credentials Expiration | 1440 min | How long TURN credentials remain valid. Note: plugin v1.11.3 defaults to 240 minutes (4 hours) — verify your version. |
| Server-Side TURN | Off | Server generates TURN credentials instead of the client. Leave off unless your TURN setup requires it. |

```{caution}
**Common Pitfall — TURN credentials expiring too quickly**: Plugin v1.11.3 defaults TURN Credentials Expiration to 240 minutes (4 hours); later versions default to 1440 minutes (24 hours). If TURN-connected calls disconnect after 4 hours, check this setting against your expected call duration.
```

---

#### Path B: RTCD Mode

```{include} ../../_static/badges/ent-plus.md
```

Use this path if you chose RTCD mode in Decision 0.2.1.

**1.1.1b:** Follow the {doc}`RTCD Setup and Configuration <calls-rtcd-setup>` guide to install and configure the `rtcd` service on a dedicated server or container. Complete through the Validation and Testing section of that guide before continuing here. For Kubernetes deployments, see {doc}`Calls Deployment on Kubernetes <calls-kubernetes>`.

**1.1.2b:** In System Console > Plugins > Calls, set **RTCD Service URL** to the `rtcd` endpoint (e.g., `https://rtcd-host:8045`).

**1.1.3b:** Configure all other settings using the same table as Path A. Settings for RTC Server Port, ICE Host Override, Max Call Participants, Test Mode, and STUN/TURN apply equally in RTCD mode.

Single-node rtcd deployment reference:

![A diagram of a Web RTC deployment configuration.](../../images/calls-deployment-image7.png)

High-availability cluster rtcd deployment reference:

![A diagram of an ha rtcd deployment.](../../images/calls-deployment-image2.png)


---

### 1.2 Deploy Calls Offloader (Optional)

```{include} ../../_static/badges/ent-plus.md
```

Skip this step if you do not need recording, transcription, or live captions.

Follow the {doc}`Calls Offloader Setup and Configuration <calls-offloader-setup>` guide to deploy the `calls-offloader` service on a dedicated server. That guide covers installation, configuration, system requirements, and air-gapped deployment.

Once deployed, configure the following settings in **System Console > Plugins > Calls**. These settings apply to both Integrated and RTCD mode.

| Setting | Notes |
|---------|-------|
| **Enable Recordings** | Enterprise only. Requires calls-offloader deployed and Job Service URL set. |
| **Job Service URL** | URL to calls-offloader service (e.g., `http://offloader-host:4545`). |
| **Recording Quality** | Low (720p/15fps), Medium (720p/20fps), High (1080p/20fps). Higher quality requires more server resources — see [Appendix C](#appendix-c-performance-and-sizing). |
| **Max Recording Duration** | 15–180 minutes. Default: 60 minutes. |
| **Enable Transcriptions** | Requires recordings enabled. Uses Whisper.cpp or Azure Speech. |
| **Transcriber Model Size** | tiny (75 MB / fastest), base (142 MB / recommended), small (466 MB / most accurate). Larger models require more CPU. |
| **Enable Live Captions** | Requires recordings and transcriptions enabled. |

---

### 1.3 Enable Calls Plugin

In **System Console > Plugins > Calls**, set **Enable Plugin** to `true`.

```{caution}
**Common Pitfall — Plugin not appearing**: If Calls is not listed under Plugin Management, your Mattermost version may be below the minimum required (v7.1+). Check your server version at System Console > About.
```

---

### 1.4 Verification Gate

Confirm each item before proceeding to Phase 2. If any check fails, see [Appendix A: Troubleshooting by Symptom](#appendix-a-troubleshooting-by-symptom).

**Functional checks:**
- [ ] Log in as two separate test users on the dev/staging instance
- [ ] User A starts a 1:1 call in a direct message channel with User B
- [ ] User B joins the call
- [ ] Both users confirm audio is audible in both directions
- [ ] Test screen sharing and visibility in both directions
- [ ] Call ends cleanly with no errors

**Infrastructure checks:**
- [ ] Port 8443 UDP is reachable from a client machine on the target network
- [ ] If RTCD: `rtcd` service is running and returns a response at `https://rtcd-host:8045/version`
- [ ] If calls-offloader: service is running and reachable from the Mattermost server on port 4545
- [ ] Check console logs for call related errors or warnings

---

## Phase 2: Pilot Testing

This phase is for controlled testing with a small group of volunteer pilot users. The goal is to confirm every scenario that will be available in production passes before widening access in Phase 3.

### 2.0 Prerequisites

- [ ] Phase 1 Verification Gate complete
- [ ] Calls-offloader deployed and configured for recording, transcription, or live captions (if enabled)
- [ ] RTCD deployed and configured (if enabled)
- [ ] At least 5-10 volunteer pilot users from different locations and using various clients
- [ ] Pilot users have the latest Mattermost desktop and/or mobile app
- [ ] Browser developer tools are accessible for log review if needed

---

### 2.1 Test Scenarios

Run each applicable scenario and record Pass or Fail.

#### 1:1 Call

| Check | Action | Pass criteria |
|-------|--------|---------------|
| 2.1.1 | User A starts a 1:1 call in a direct message channel | Call widget appears for both users |
| 2.1.2 | User B joins the call | Both users show as connected |
| 2.1.3 | Speak in both directions | Both users hear each other clearly |
| 2.1.4 | End the call | Call ends cleanly; no error messages |

#### Group Call

| Check | Action | Pass criteria |
|-------|--------|---------------|
| 2.1.5 | User A starts a call in a channel with 3 or more members | Call widget appears |
| 2.1.6 | Users B and C join | All three show as connected |
| 2.1.7 | All participants speak | All participants hear each other |
| 2.1.8 | End the call | Call ends cleanly |

#### Screen Sharing

| Check | Action | Pass criteria |
|-------|--------|---------------|
| 2.1.9 | During an active call, User A starts screen sharing | Screen share stream appears for all participants |
| 2.1.10 | User B views User A's screen | Screen share is visible and legible |
| 2.1.11 | User A stops screen sharing | Stream ends cleanly; call continues |

#### Recording + Transcription (Optional)

| Check | Action | Pass criteria |
|-------|--------|---------------|
| 2.1.12 | During an active call, the host starts a recording | Recording indicator appears for all participants |
| 2.1.13 | End the call or stop the recording | Recording stops; post-processing begins |
| 2.1.14 | Wait for processing to complete | Recording file appears in the channel and is playable |

#### Live Captions (Optional)

| Check | Action | Pass criteria |
|-------|--------|---------------|
| 2.1.16 | Enable live captions during an active call | Caption overlay appears |
| 2.1.17 | A participant speaks | Captions appear within 2–3 seconds |
| 2.1.18 | Disable captions | Captions stop; call continues normally |

#### Cross-Device Call

| Check | Action | Pass criteria |
|-------|--------|---------------|
| 2.1.19 | User A joins a call from the Mattermost desktop app | User A shows as connected |
| 2.1.20 | User B joins the same call from the Mattermost mobile app | Both users show as connected |
| 2.1.21 | Speak in both directions | Both users hear each other clearly |
| 2.1.22 | End the call | Call ends cleanly on both devices |
| 2.1.23 | Reverse the test: User A on mobile, User B on desktop | Same pass criteria apply |

#### Remote and VPN Call

| Check | Action | Pass criteria |
|-------|--------|---------------|
| 2.1.24 | User A connects from outside the corporate network (e.g., home network or hotspot) | User A can start or join a call |
| 2.1.25 | User B connects from inside the corporate network or VPN | Both users show as connected |
| 2.1.26 | Speak in both directions | Both users hear each other clearly |
| 2.1.27 | If TURN is configured: confirm the call establishes when UDP is blocked (e.g., on a restrictive network) | Call connects via TURN relay |

```{note}
Remote and VPN scenarios are where ICE, STUN, and TURN configuration issues typically surface first. If this test fails but on-network calls pass, revisit Decision 3 in Section 0.2 (Network Traversal).
```

#### Long Duration Call

| Check | Action | Pass criteria |
|-------|--------|---------------|
| 2.1.28 | Start a call with 2 or more participants | Call connects normally |
| 2.1.29 | Leave the call running for at least 30 minutes with periodic voice activity | Call remains stable; no drops or reconnections |
| 2.1.30 | Check server and RTCD logs at the 15-minute and 30-minute marks | No unexpected errors; ICE state remains `succeeded` |
| 2.1.31 | End the call | Call ends cleanly |

```{note}
Long duration tests help catch TURN credential expiry issues. If using TURN and calls drop around the 4-hour mark, check the **TURN Credentials Expiration** setting (see the advanced settings table in Section 1.1).
```

---

### 2.2 Monitor and Optimize

While running test scenarios, monitor server resources and review logs. Use this section to distinguish normal log output from real problems.

**Signs of a healthy call** (check browser or client developer tools logs):
- `rtc connected` appears for all participants
- ICE state shows `succeeded` with `nominated: true`
- Audio and video tracks are flowing — use `/call stats` in Mattermost to verify
- Clean disconnect when the call ends with no unexpected errors

**Expected errors — safe to ignore:**

The following error patterns appear during normal operation:

| Error pattern | Where it appears | Why it is normal |
|---------------|-----------------|-----------------|
| `"Failed to send packet...192.168.254.0"` | RTCD logs | ICE probes all interfaces. 40–60 per call. |
| `"unexpected dc message type: 9"` | Offloader logs | Recorder ignores UI-only messages. 4–8 per call. |
| `"failed to get rtcd system info"` | Server logs | Type mismatch on some operating systems. 1 per call. |
| `"Failed to ping without candidate pairs"` | RTCD logs | Normal ICE startup probe. 2–8 at call start. |
| `"ffmpeg exited with status: 255"` | Offloader logs | FFmpeg stopped intentionally at recording end. 1 per recording. |
| `"failed to send ping...closed pipe"` | Offloader logs | Cleanup timing after call ends. 10–15 occurrences. |
| `"Error reading first packet...EOF"` | RTCD logs | TCP probe resolved by UDP; expected. 2–6 per call. |

If you see errors other than those listed above, see [Appendix A](#appendix-a-troubleshooting-by-symptom) or check [Calls Log Collection](calls-log-collection.md) for how to gather full logs for support.

**Resource monitoring:**
- Monitor Mattermost server CPU and memory during test calls
- If using RTCD: monitor RTCD server CPU — keep below 80% during sustained load (see [Appendix C](#appendix-c-performance-and-sizing) for sizing guidance)
- Review server and RTCD logs for unexpected errors after each test scenario

---

### 2.3 Verification Gate

Before proceeding to Phase 3, confirm:

- [ ] All pilot testing scenarios 2.1.1 - 2.1.31 passed with no errors (as applicable)
- [ ] No unexpected errors in server or RTCD logs
- [ ] Server resource utilization is within acceptable bounds
- [ ] All issues encountered are documented and resolved
- [ ] Pilot users confirm readiness for broader rollout

---

## Phase 3: Production Rollout

### 3.0 Prerequisites

- [ ] Phase 2 Verification Gate complete
- [ ] Administrative access to your production Mattermost instance
- [ ] Production RTCD instance deployed and validated (if applicable)
- [ ] Production calls-offloader deployed and validated (if applicable)
- [ ] Monitoring in place or scheduled for setup during this phase
- [ ] Rollback plan is documented (Section 3.5)

---

### 3.1 Production Configuration

**3.1.1:** In System Console > Plugins > Calls on your production instance, apply the same settings validated in Phase 1. Verify:
- RTC Server Port, ICE Host Override, and STUN/TURN settings match your production network topology
- If using RTCD: RTCD Service URL points to the production `rtcd` endpoint
- Enable Test Mode is set to `true` initially (for incremental rollout in Section 3.2)

**3.1.2:** Click Save and confirm the plugin is enabled.

```{caution}
**Common Pitfall — Different network topology in production**: Production environments often have different firewall rules, NAT configurations, or proxy layers than dev/staging. Re-verify UDP 8443 connectivity from a production client machine before enabling calls for users.
```

---

### 3.2 Incremental Rollout

Use Test Mode to enable Calls in controlled waves, monitoring for issues before expanding to all users.

**How Test Mode works**: When Test Mode is enabled, Calls is disabled by default in all channels. System admins enable it per channel. When Test Mode is disabled, Calls becomes available in every channel.

```{note}
When Test Mode is disabled, users in any Mattermost channel can make a call.
```

**Recommended rollout waves:**

| Wave | Target channels | Duration | Action |
|------|----------------|----------|--------|
| Wave 1 | IT, Engineering, or internal admin channels | Days 1–3 | Monitor stability; resolve any issues before expanding |
| Wave 2 | Broader department channels | Days 4–7 | Expand if Wave 1 is stable; collect feedback |
| Wave 3 | All remaining channels | Day 8+ | Disable Test Mode to enable Calls everywhere |

**To enable calls in a specific channel:**
1. Navigate to the channel
2. Click the channel name at the top of the channel
3. Select **Enable calls** from the dropdown menu

![Channel menu showing Enable/Disable calls options](../../images/calls-channel-enable-disable.png)

---

### 3.3 User Communication

Before enabling calls for each wave, communicate to affected users. Copy the announcement below, customize the placeholders, and post it in your announcement channel.

Customize before posting:
- Replace `[#calls-support]` with your designated support channel
- Replace `[IT contact name]` with the appropriate contact
- Add recording/transcription details if those features are enabled

---

**Draft announcement post:**

```
## Voice Calls are now available in this channel

You can now start a voice call from directly in Mattermost.

**How to start a call:**
Click the phone icon in the channel header to start a call. Anyone in the channel can join.

**What's available:**
- 1:1 and group voice calls
- Screen sharing (desktop app and browser)

**Things to know:**
- We recommend a maximum of 50 participants per call for best performance
- Screen sharing is available on the desktop app and desktop browsers — not available on mobile
- Your browser or desktop app may prompt for microphone and screen sharing permissions the first time you join a call

**Getting help:**
If you run into any issues, post in [#calls-support] or contact [IT contact name].

For end-user guidance on making and joining calls, see the Mattermost documentation:
https://docs.mattermost.com/collaborate/make-calls.html
```

---

### 3.4 Monitor and Optimize

**During the first two weeks after production rollout:**

**3.4.1:** Monitor Mattermost server CPU and memory during peak call hours.

**3.4.2:** Review server and RTCD logs for unexpected errors. Refer to the expected errors table in Section 2.2 — errors outside that list warrant investigation.

**3.4.3:** If using RTCD: monitor RTCD CPU utilization. If it regularly exceeds 70%, add RTCD nodes. See {doc}`RTCD Setup and Configuration <calls-rtcd-setup>` for horizontal scaling guidance.

**3.4.4:** Set up the official Mattermost Calls Grafana dashboard for ongoing observability:

Monitoring Endpoints
| Service | Metrics endpoint | Notes |
|---------|-----------------|-------|
| Calls plugin | `/plugins/com.mattermost.calls/metrics` | Accessed on Mattermost metrics port (8067 by default) |
| `rtcd` service | `/metrics` | On the RTCD API listener (port 8045 by default) |

Mattermost also provides an official Calls monitoring dashboard for Grafana. It visualizes active sessions, connection states, media tracks, CPU, memory, and WebSocket metrics for both the Calls plugin and `rtcd`. You can import it from **Grafana > Dashboards > Import** > enter ID **23225**.

For full Prometheus and Grafana setup, see {doc}`Calls Metrics and Monitoring <calls-metrics-monitoring>`.

**3.4.5:** Track user-reported issues. Common symptoms and fixes are in [Appendix A](#appendix-a-troubleshooting-by-symptom).

**3.4.6:** Adjust Max Call Participants if resource constraints appear during peak usage.

---

### 3.5 Rollback Plan

If issues arise in production, use the appropriate option below.

**Immediate rollback — disable Calls entirely:**
1. Go to System Console > Plugin Management > Calls
2. Set **Enable Plugin** to `false`
3. Click Save

This stops all call functionality instantly across the entire instance.

**Per-channel rollback — disable Calls in affected channels only:**
1. Confirm Test Mode is enabled (System Console > Plugins > Calls > Enable Test Mode = `true`)
2. Navigate to the affected channel
3. Click the channel name > Select **Disable calls**

Use this for targeted issues in specific channels without affecting other channels already on the rollout.

**RTCD fallback — revert to integrated SFU:**
1. Go to System Console > Plugins > Calls
2. Clear the **RTCD Service URL** field
3. Click Save

Calls falls back to the integrated SFU immediately. Active calls may experience a brief interruption during the transition.

---

## Appendix A: Troubleshooting by Symptom

This appendix covers the most common issues encountered during Calls deployment. For guidance on gathering logs to share with Mattermost Support, see [Calls Log Collection](calls-log-collection.md).

### A.1 Timed Out Waiting for Peer Connection

This is the most common error. It means the WebRTC media connection could not be established between the client and the Calls server.

| Cause | Fix |
|-------|-----|
| UDP port 8443 blocked by firewall | Open inbound UDP 8443 on all firewalls between clients and the Calls server. Verify this first — it is the cause in the majority of cases. |
| Server behind NAT without ICE Host Override | Set ICE Host Override to the public IP or hostname clients can reach. See Section 0.2, Decision 3. |
| Docker container port not mapped for UDP | Ensure `8443/udp` is mapped: `-p 8443:8443/udp -p 8443:8443/tcp`. TCP-only mapping is a common oversight. |
| Cloud security group missing UDP rule | AWS, Azure, and GCP security groups often default to TCP only. Add an explicit inbound UDP rule for port 8443. |
| NGINX intercepting port 8443 | NGINX cannot proxy UDP. Ensure UDP 8443 traffic bypasses NGINX and reaches the Mattermost or `rtcd` process directly. |
| Mobile carrier CGNAT | Mobile networks use carrier-grade NAT that blocks or drops UDP. Configure a TURN server (coturn recommended) or confirm TCP fallback is enabled (plugin ≥ v0.17, `rtcd` ≥ v0.11). |

### A.2 Call Connects But No Audio

| Cause | Fix |
|-------|-----|
| Browser microphone permission denied | Grant microphone access in browser settings for the Mattermost URL. |
| OS privacy setting blocking microphone | macOS: System Settings > Privacy & Security > Microphone. Windows: Settings > Privacy > Microphone. Ensure the browser or desktop app is allowed. |
| Wrong input device selected | Verify the correct audio input device is selected in the Calls UI settings panel during the call. |
| Mattermost not on HTTPS | Browsers require a secure context (HTTPS) to access the microphone API. Calls on HTTP will fail to capture audio. |

### A.3 Call Works on LAN But Not Remotely

| Cause | Fix |
|-------|-----|
| ICE Host Override not set | Remote clients need the server's public IP to connect. Set ICE Host Override to the external IP or DNS name. |
| STUN server unreachable | If the default STUN server is blocked by your network, clients cannot discover their public IP. Open outbound UDP 3478 or set ICE Host Override manually. |
| VPN split tunneling | Verify your VPN routes UDP 8443 traffic to the Calls server. Split tunneling that excludes this port causes remote connection failures. |
| Corporate firewall blocking UDP | Enable TCP fallback (plugin ≥ v0.17, `rtcd` ≥ v0.11) or deploy a TURN server configured on TCP port 443. |

### A.4 Calls Drop After a Few Minutes

| Cause | Fix |
|-------|-----|
| Firewall UDP session timeout | Some firewalls drop idle UDP sessions after 30–60 seconds. Increase the UDP session timeout on your firewall to at least 120 seconds. |
| Server resource exhaustion | If CPU or memory is saturated, the server may drop connections. Monitor server resources during calls — see [Appendix C](#appendix-c-performance-and-sizing) for sizing guidance. |
| WebSocket disconnection | If the WebSocket connection to Mattermost drops (e.g., NGINX proxy timeout), call signaling is lost. Audio may continue briefly but participants will disconnect. Check NGINX proxy read timeout and WebSocket upgrade configuration. |
| TURN credentials expired | If using TURN, check TURN Credentials Expiration. Plugin v1.11.3 defaults to 240 minutes — calls longer than this duration will drop. |

### A.5 Screen Sharing Not Working

| Cause | Fix |
|-------|-----|
| Mobile client | Screen sharing is only available on the Mattermost desktop app and desktop browsers. Mobile clients cannot share their screen. |
| Browser permission denied | Grant screen sharing permission when the browser prompts. macOS: System Settings > Privacy & Security > Screen Recording must include the browser or desktop app. |
| Insufficient bandwidth | Screen sharing requires significantly more bandwidth than audio alone. If the network path is constrained, screen sharing may fail while audio continues. |

### A.6 MTU and Packet Fragmentation Issues

**Symptom:** Calls connect and audio is present but quality degrades intermittently, packets are dropped unpredictably, or calls work on some networks but not others despite ports being open.

**Root cause:** When ICMP "Frag Needed" messages are blocked by firewalls or VPN tunnels, Path MTU Discovery (PMTUD) breaks silently. Large packets disappear rather than being fragmented, causing unpredictable quality issues that are difficult to trace. This is common in enterprise environments with strict ICMP filtering.

| Cause | Fix |
|-------|-----|
| ICMP blocked on firewall preventing PMTUD | Allow ICMP Type 3, Code 4 ("Fragmentation Needed") messages through your firewall. |
| VPN tunnel reducing effective MTU | Use MTU path discovery commands (see [Appendix D](#appendix-d-advanced-network-diagnostics)) to find the actual path MTU and adjust server configuration accordingly. |
| Jumbo frames mismatch on network path | Run Appendix D MTU discovery to identify the fragmentation point and align MTU settings. |

### A.7 RTCD-Specific Issues

**`rtcd` service not connecting:**

| Check | Action |
|-------|--------|
| Service running | Verify `rtcd` is running: `systemctl status rtcd` or check container logs. |
| API reachable from Mattermost | From the Mattermost server: `curl -k https://rtcd-host:8045/version` — should return version info. |
| TLS certificate valid | `rtcd` requires a valid TLS certificate. Self-signed certificates must be trusted by the Mattermost server. |
| Firewall between Mattermost and `rtcd` | Port 8045 TCP must be open from Mattermost server to `rtcd`. Verify no firewall blocks this internal path. |

**Calls connect to `rtcd` but no media:**

| Check | Action |
|-------|--------|
| UDP 8443 pointing to `rtcd` host | When RTCD mode is active, clients connect to the `rtcd` host (not the Mattermost server) on UDP 8443. Verify firewalls route media traffic to the `rtcd` host. |
| ICE Host Override on `rtcd` | If `rtcd` is behind NAT, configure `ice_host_override` in the `rtcd` `config.toml` with the public IP or hostname. |

### A.8 RHEL-Specific Issues

| Issue | Fix |
|-------|-----|
| firewalld blocking Calls port | `firewall-cmd --permanent --add-port=8443/udp && firewall-cmd --reload` |
| fapolicyd blocking Mattermost/Calls plugin | The Calls plugin runs as part of the Mattermost process. Ensure Mattermost is allowed in fapolicyd rules. See the [RHEL deployment guide](https://docs.mattermost.com/deployment-guide/server/deploy-linux.html#itab--RHEL-CentOS--0_1-RHEL-CentOS). |
| fapolicyd blocking standalone `rtcd` | Standalone `rtcd` requires its own fapolicyd rule separate from Mattermost rules. |

### A.9 Errors That Indicate Real Problems

| Error pattern | What to do |
|---------------|------------|
| No `rtc connected` in client logs | Connection failed. Check firewall, STUN/TURN configuration, and UDP 8443 access from the client network. |
| ICE state stuck at `checking` or `failed` | Network path blocked. Verify UDP access or configure a TURN server. |
| `failed to upload recording` | Storage issue on calls-offloader. Check disk space, file permissions, and S3 configuration if applicable. |
| `disconnected` during an active call | Network instability. Check packet loss rates, TURN server health, and available bandwidth. |

### A.10 Diagnostic Commands Quick Reference

| Command | Purpose | Run from |
|---------|---------|---------|
| `nc -v -u <server> 8443` | Test UDP connectivity to Calls port | Client machine |
| `nc -v <server> 8443` | Test TCP connectivity to Calls port | Client machine |
| `sudo tcpdump -n port 8443` | Monitor packet flow on Calls port | Server |
| `curl -k https://<rtcd>:8045/version` | Verify `rtcd` API is reachable | Mattermost server |
| `ss -ulnp \| grep 8443` | Verify Calls is listening on UDP | Server |
| `ss -tlnp \| grep 8443` | Verify Calls is listening on TCP | Server |
| `firewall-cmd --list-all` | List firewalld rules (RHEL) | Server |

For gathering full diagnostic logs to share with support, see [Calls Log Collection](calls-log-collection.md).

---

## Appendix B: Frequently Asked Questions

### B.1 Is calls traffic encrypted?

Media (audio/video) is encrypted using DTLS and SRTP as part of the WebRTC standard. It is not end-to-end encrypted — the Mattermost server or `rtcd` service acts as a media router with access to unencrypted media in transit. Media is re-encrypted before delivery to each client, securing it during transit. Only the participant clients and the Mattermost server have access to unencrypted call data.

### B.2 Are there any third-party services involved?

The only external service used by default is a Mattermost-hosted STUN server (`stun.global.calls.mattermost.com`). No user information, call metadata, or media traffic is ever sent to this service. Its sole purpose is public IP address discovery. This dependency can be removed entirely by setting the ICE Host Override configuration option.

### B.3 Is using UDP a requirement?

UDP is the recommended protocol for real-time media because it provides the lowest latency between peers. TCP fallback is supported since Calls plugin v0.17 and `rtcd` v0.11 — the RTC service listens for TCP connections on the same port (8443) in addition to UDP.

If clients cannot use UDP:
- TCP on port 8443 (or a reconfigured commonly allowed port like 80 or 443) allows direct connection without UDP.
- A TURN server relaying traffic over TCP is an option but adds latency and infrastructure cost. Use only when required.

---

## Appendix C: Performance and Sizing

These benchmarks are sourced from official Mattermost performance testing (Mattermost v9.6, Calls v0.28.0, RTCD v0.16.0 on AWS). Use them to right-size your RTCD and recording servers before deployment.

**Key rule: Keep CPU utilization below 80% to leave headroom for traffic spikes. If your expected usage approaches 80%, move to the next server size up.**

### C.1 RTCD Server Sizing

#### 4 vCPU (c7i.xlarge) — Suitable for getting started

| Concurrent calls | Participants/call | Screen share | CPU | Memory |
|-----------------|------------------|--------------|-----|--------|
| 1 | 1,000 | No | 47% | 1.5 GB |
| 1 | 1,000 | Yes | 79% | 1.5 GB |
| 100 | 10 | No | 49% | 1.5 GB |
| 100 | 10 | Yes | 84% | 1.7 GB |

#### 8 vCPU (c7i.2xlarge) — Recommended for production

| Concurrent calls | Participants/call | Screen share | CPU | Memory |
|-----------------|------------------|--------------|-----|--------|
| 1 | 1,000 | No | 20% | 1.4 GB |
| 1 | 1,000 | Yes | 49% | 1.5 GB |
| 2 | 1,000 | Yes | 73% | 2.4 GB |
| 150 | 10 | Yes | 79% | 2.3 GB |
| 250 | 10 | No | 58% | 2.7 GB |
| 1,000 | 2 | No | 78% | 2.3 GB |

#### 16 vCPU (c7i.4xlarge) — For heavy usage

| Concurrent calls | Participants/call | Screen share | CPU | Memory |
|-----------------|------------------|--------------|-----|--------|
| 2 | 1,000 | Yes | 41% | 2.6 GB |
| 4 | 1,000 | Yes | 83% | 4.4 GB |
| 250 | 10 | Yes | 79% | 3.5 GB |
| 500 | 2 | Yes | 71% | 2.5 GB |

For additional performance baselines and Prometheus metrics context, see {doc}`Calls Metrics and Monitoring <calls-metrics-monitoring>`.

### C.2 Recording Server Sizing

Recommended: 8 vCPU / 16 GB RAM dedicated instance (e.g., AWS c6i.2xlarge).

| Quality setting | Resolution | Concurrent jobs | Avg CPU | File size/hr |
|----------------|-----------|----------------|---------|-------------|
| Low | 720p @ 15fps | 8 | 66% | 0.5 GB |
| Medium | 720p @ 20fps | 6 | 66% | 0.7 GB |
| High | 1080p @ 20fps | 4 | 72% | 1.2 GB |

### C.3 Linux Kernel Tuning

For servers (Mattermost or RTCD) hosting many concurrent calls, increase UDP buffer sizes with these kernel parameters:

```bash
# Add to /etc/sysctl.conf or /etc/sysctl.d/calls.conf
net.core.rmem_max = 16777216    # Max receiving UDP buffer (16 MB)
net.core.wmem_max = 16777216    # Max sending UDP buffer (16 MB)
net.core.optmem_max = 16777216  # Additional memory for socket control messages

# Apply without rebooting:
sudo sysctl -p
```

---

## Appendix D: Advanced Network Diagnostics

This appendix is for your network team or sysadmin when standard connectivity checks have not revealed the root cause of an issue.

### D.1 Connectivity Verification

```bash
# On the server — listen for incoming UDP packets:
nc -l -u -p 8443

# From a client — test UDP connectivity:
nc -v -u SERVER_IP 8443

# Monitor packets on the server:
sudo tcpdump -n port 8443
```

### D.2 MTU Path Discovery

Large packets that exceed the path MTU cause silent packet loss. Use these commands to find the actual MTU along the network path:

```bash
# Test path MTU with Don't Fragment flag (Linux/macOS)
# Start at 1360, reduce until packets succeed
ping -M do -s 1360 <server-ip>
ping -M do -s 1300 <server-ip>
ping -M do -s 1200 <server-ip>
# Actual path MTU = largest working size + 28 bytes (IP + ICMP headers)

# Check interface MTU
ip link show         # Linux
ifconfig             # macOS

# Check VPN tunnel MTU
ip link show | grep -E "mtu|tun|ipsec|wg"
```

### D.3 Path MTU Discovery (PMTUD) Verification

If ICMP "Frag Needed" messages are blocked, PMTUD breaks silently — large packets disappear without any error message, causing unpredictable call quality issues.

```bash
# Test whether ICMP fragmentation messages are getting through
ping -M do -s 2000 <rtcd-ip>
# If ICMP works: "Frag needed and DF set" or "Message too long"
# If blocked: timeout or "100% packet loss"

# Discover path MTU along the full route (Linux)
tracepath <rtcd-ip>
# Look for "pmtu XXXX" in output
```

### D.4 Bandwidth Testing

```bash
# Start iperf3 server on the Calls server:
iperf3 -s -p 5201

# UDP test sized to match actual WebRTC traffic (from client):
iperf3 -c <server-ip> -u -b 5M -p 5201 -l 1180
# -l 1180 matches WebRTC video payload size (1208-byte IP packet total)
# Default iperf3 UDP uses 1460-byte payloads — larger than WebRTC. Use -l 1180 for accurate results.
# Look for: packet loss % (should be 0%) and jitter

# TCP baseline for comparison (from client):
iperf3 -c <server-ip> -t 30
```

---

## Appendix E: Glossary

- **[WebRTC](https://bloggeek.me/webrtcglossary/webrtc-2/)**: The set of open protocols on which Mattermost Calls is built
- **RTC**: Real-Time Connection channel used for media (audio/video/screen)
- **WS**: WebSocket connection used for signaling and connection setup
- **SFU**: Selective Forwarding Unit — the component that routes media streams between call participants
- **[NAT](https://bloggeek.me/webrtcglossary/nat/)**: Network Address Translation — maps private IP addresses to public ones
- **[STUN](https://bloggeek.me/webrtcglossary/stun/)**: Session Traversal Utilities for NAT — protocol used by WebRTC clients to discover their public IP
- **[TURN](https://bloggeek.me/webrtcglossary/turn/)**: Traversal Using Relays around NAT — protocol to relay media for clients behind strict firewalls
- **ICE**: Interactive Connectivity Establishment — the process WebRTC uses to find the best network path between peers
- **DTLS**: Datagram Transport Layer Security — encryption protocol used for WebRTC media setup
- **SRTP**: Secure Real-time Transport Protocol — encrypts the audio and video data in transit
- **PMTUD**: Path MTU Discovery — process for determining the maximum packet size that can travel a network path without fragmentation
