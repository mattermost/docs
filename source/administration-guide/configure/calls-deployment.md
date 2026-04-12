# Mattermost Calls Deployment Guide

```{include} ../../_static/badges/all-commercial.md
```

This guide is designed to walk System Administrators step-by-step through the process of deploying Mattermost Calls, from initial preparation and confirming network readiness, to validating core calling functions with test users, and scaling up to full production deployment. You’ll find detailed instructions, decision points, verification gates, and troubleshooting tips to help ensure a reliable Calls deployment, whether you’re enabling basic audio and screen sharing or advanced features like recording and transcription. 

No prior experience with Mattermost Calls is required — this guide assumes you’re starting fresh and will introduce essential concepts and best practices.


## Calls Overview

Mattermost Calls offers self-hosted audio calling and screen sharing, enabling sovereign real-time collaboration fully contained within your infrastructure. This means no audio, video, or metadata traverses third-party systems.

Calls is uniquely suited for mission-critical operations across defense, intelligence, security and critical infrastructure — where data sovereignty, control, and compliance are non-negotiable. It is designed to function in isolated networks without internet access, supporting deployments that demand full airgap compliance.

Functionality includes:
- **1:1 and Group Calling**: Initiate real-time voice communication between two or more participants.
- **Screen Sharing**:  Share your screen during calls to collaborate visually on tasks, review documents, or troubleshoot live issues. 
- **Call Recording and Transcription**: Record voice sessions for review, compliance, or distribution. *(Enterprise, Enterprise Advanced)*
- **Live Captioning**: Provide real-time subtitles for inclusivity, accessibility, and support in noisy or multilingual environments. *(Enterprise, Enterprise Advanced)*

## Deployment Overview

This guide is organized into sequential deployment phases with heirarchical numbered steps. Each phase begins with prerequisits and ends with verification checks. Before you begin any phase, make sure all the listed prerequisites are fully met, then only proceed to the next phase when you have successfully completed the verification checks for the current phase. This step-by-step approach helps you catch and resolve issues early, ensuring a smooth and reliable Calls deployment.

**Deployment Phases:**

1. [**Preparation and Networking**](#phase-1-preparation-and-networking)  
   Plan your deployment architecture, gather prerequisites, provision any required servers, and confirm the required network ports and paths are open before deployment.

2. [**Configure Integrated Calls**](#phase-2-integrated-calls-plugin-configuration)  
   Regardless of the deployment architecture you choose, you'll start with simplest calls deployment (integrated mode) to verify connectivity and core audio and screen sharing functionality.

3. [**Install and Configure RTCD**](#phase-3-add-rtcd) (Optional)  
   RTCD (real-time communication daemon) is a service built to offload media processing tasks from the Mattermost server. This optional phase is where you'll deploy the RTCD service and verify that the Mattermost server and clients can reach it correctly.

4. [**Install and Configure Recording**](#phase-4-add-calls-offloader) (Optional)
   Calls Offloader is a service required to deliver recording, transcription and live captions. This optional phase is where you'll deploy the `calls-offloader` service and confirm that recording, transcription, and live captions work as expected.

5. [**Pilot Rollout**](#phase-5-pilot-rollout)  
   Expand testing to a small group of pilot users to watch for client, network, and environment-specific issues under real usage.

6. [**Production Rollout**](#phase-6-production-rollout)  
   Rollout to all users in controlled waves with appropriate communication and monitoring, and be ready to pause or roll back if needed.


```{note}
If you need expert help deploying Calls, contact your Account Manager or [talk to a Mattermost expert](https://mattermost.com/contact-sales/) to learn about professional service offerings.
```

### Contacting Support

If you encounter issues and need to open a [support case](https://support.mattermost.com), please include the exact **step number** (e.g. 2.2.1) that failed, along with your {doc}`Mattermost support packet <../../administration-guide/manage/admin/generating-support-packet>` and Calls logs (see [Calls Log Collection](calls-log-collection.md) for how to gather them.)

---

## Phase 1: Preparation and Networking

### 1.1 Prerequisites

Before you start, confirm the following:

- [x] You have a running Mattermost server on v10.0+
- [x] Mattermost server is configured to use secure HTTPS.  
      _Browsers will block microphone and screen sharing on unsecure HTTP connections. To enable voice calls and screen sharing, you must run Mattermost over HTTPS. If you need to set up HTTPS, see [Configure TLS](https://docs.mattermost.com/deploy/server/setup-tls.html)._
- [x] You have System Admin access to your Mattermost server.
- [x] You can open inbound and outbound network ports on the servers involved in the deployment. If a network or security team manages your firewalls, you'll need to involve them before continuing.
- [x]You can provision additional servers if your chosen architecture requires RTCD or Calls Offloader services.

### 1.2 Deployment Infrastructure

To determine your deployment instrastructure, answer the following questions:

- **How many users will use Calls?**
  - **Up to 50 users:** You can use the **Integrated** deployment mode.
  - **More than 50 users:** You'll need to deploy an additional component called **RTCD** (Real-Time Communication Daemon) for handling media processing at scale.

- **Do you require call recording, transcription, or live captions?**
  - **Yes:** You'll need to deploy an additional component for the **Recording** service called Calls Offloader.
  - **No:** You do not need the recording service.

Based on your answers, you can explore the associated deployment infrastructure you'll need in the tabs below:

````{tab} Integrated

In Integrated mode, the Calls plugin runs its built-in media service directly on the Mattermost server. This is the simplest deployment model, since you do not need to provision a separate service to handle media processing.

```{mermaid}
flowchart TD
    clients["Clients\nWeb, Desktop, Mobile"]
    mm["Mattermost Server\nCalls plugin + integrated media service"]

    clients -->|TCP 443 signaling| mm
    clients -->|UDP/TCP 8443 media| mm
```

**When to use it**

- You are evaluating Calls for the first time.
- You expect fewer than 50 people to use Calls.
- You want the simplest possible deployment.

**Components**

- **Mattermost server**: Calls plugin is pre-installed.

**License**

- Mattermost Entry: 1:1 Calls + Screen Sharing
- Mattermost Professional, Enterprise, or Enterprise-Advanced: Group Calls + Screen Sharing up to 50 participants
````

````{tab} RTCD

The RTCD can be added as a dedicated media service that processes all call audio and screen sharing media. The Mattermost server is still responsible for signaling (setting up, managing, and ending calls) and channel state (who is joining or leaving, who has muted, and overall call status), but the call media itself flows directly between clients and the RTCD server, completely bypassing the Mattermost server.

Deploying RTCD is **highly recommended in production deployments** for performance, scalability, and stability of Mattermost Calls.

```{mermaid}
flowchart TD
    clients["Clients\nWeb, Desktop, Mobile"]
    mm["Mattermost Server\nCalls plugin"]
    rtcd["RTCD Server"]

    clients -->|TCP 443 signaling| mm
    mm -->|TCP 8045 internal API| rtcd
    clients -->|UDP 8443 media| rtcd
    rtcd -->|UDP 8443 media| clients
    clients -->|TCP 8443 media fallback| rtcd
    rtcd -->|TCP 8443 media fallback| clients
```

**When to use it**

Use RTCD if you need optimized performance, scalability, and the best possible user experience for Mattermost Calls. Specifically:

- You want to keep call media traffic off your main Mattermost server to improve overall server performance and reduce CPU usage spikes.
- You need your deployment to easily scale as call volume increases; additional RTCD servers can be added for load balancing.
- You require ongoing calls to remain active even if the Mattermost server needs to be restarted (some features like reactions and muting may be temporarily unavailable during the restart).
- You want the lowest possible audio/video latency and highest reliability for Calls.
- You are deploying Mattermost on Kubernetes (RTCD is required for all Kubernetes deployments).

**Components**

- **Mattermost server**: Calls plugin is pre-installed.
- **RTCD Server**: Dedicated media service. Clients connect to it directly for media traffic.

**License**

- Mattermost Enterprise or Enterprise-Advanced: Required for RTCD.
````

````{tab} RTCD + Recording

The `calls-offloader` service can be added to a Calls deployment to enable recording, transcription, and live captions.

```{mermaid}
flowchart TD
    clients["Clients\nWeb, Desktop, Mobile"]
    mm["Mattermost Server\nCalls plugin"]
    rtcd["RTCD Server"]
    offloader["calls-offloader Server"]
    jobs["Recorder and transcriber jobs"]

    clients -->|TCP 443 signaling| mm
    mm -->|TCP 8045 internal API| rtcd
    mm -->|TCP 4545 internal API| offloader
    clients -->|UDP or TCP 8443 media| rtcd
    rtcd -->|UDP or TCP 8443 media| clients
    offloader -->|launches| jobs
    jobs -->|UDP or TCP 8443 media| rtcd
    rtcd -->|UDP or TCP 8443 media| jobs
```

**When to use it**

- You need call recording, transcription, or live captions.

**Components**

- **Mattermost server**: Calls plugin is pre-installed.
- **RTCD Server**: Dedicated media service. Clients connect to it directly for media traffic.
- **Calls Offloader**: Job service that manages recording and transcription.

```{note}
`calls-offloader` can also be added to an integrated Calls deployment without RTCD. This guide uses RTCD as the base because it is the recommended production path for most deployments.
```

**License**

- Mattermost Enterprise or Enterprise Advanced: Required for `calls-offloader` service.


````

### 1.3 Networking Decisions

Do this before you install anything new.

#### 1.3.1 STUN for Public IP Discovery

STUN is a protocol used to automatically discover the public IP address of your media server so clients can connect to Calls.  

Mattermost provides a default STUN server (`stun.global.calls.mattermost.com`) for public IP discovery. No user information, call metadata, or media traffic is sent to or shared with this STUN service; its sole purpose is to help media servers discover their public IP address. Use this decision tree to determine if you need to allow outbound access from your media server to the Mattermost global STUN service.

```{note}
Your media server is the Mattermost server in the case of an **Integrated** Calls deployment, or it's the **RTCD server** in the case of an RTCD Calls deployment. 
```

**STUN Decision Tree**

1. **Are all users and your media server (Mattermost server or RTCD) are in the same private network, VPN, or air-gapped environment (no outside clients)?**
   - **Yes**: You do not need STUN. You will use the private address of your media server for configuration in Phase 2.
   - **No**: Continue to the next question. 

2. **Does your media server (Mattermost server or RTCD) have a stable public IP address or DNS name that clients on the public internet can reach?**
   - **Yes**: You do not need STUN. You will use the public address of your media server for configuration in Phase 2.
   - **No**: You will need STUN. You must open outbound UDP 3478 from your media server to `stun.global.calls.mattermost.com`.

If your deployment requires STUN, note this requirement as you work through the exrcise of opening all necessary ports in Step 1.5.


#### 1.3.2 TURN Server

TURN is a protocol that relays media when users cannot reach the Calls media service directly.

Provisioning a TURN server is necessary if both of these conditions are true:

- Clients connect from networks that cannot reliably use UDP on port `8443` for media traffic (preferred path).
- Clients connect from networks that cannot reliably use TCP on port `8443` (fallback).

TURN is typically a last resort as it adds additional networking and infrastructure complexity. Only plan to deploy TURN if your answers indicate that you cannot rely on UDP or TCP for media, and users need an alternative route. 


### 1.4 Provision Infrastructure

Now you will provision the servers or VMs you'll need to support your Calls Deployment. You are only preparing infrastructure here; software installation and service configuration happen in later phases. This step is important because you'll need the IP addresses of these servers in order to configure networking in the next step.

Infrastructure requirements are based on your deployment architecture chosen in Step 1.2. If you need to provision additional hardware, you should note the IP addresses of these servers for networking configuration in the next step:

**Integrated**
Since the Mattermost server is handling all media processing, you can skip this step and proceed to network configuration in Step 1.5.

**RTCD**
You will need to provision a new server for RTCD. Use **Appendix B.1** for benchmark examples of hardware sizing. The RTCD service supports [horizontal scaling](https://docs.mattermost.com/administration-guide/configure/calls-rtcd-setup.html#horizontal-scaling), but we recommend starting with one server, and then scaling out if your pilot or expected workload requires it.

**Recording**
You will need to provision a new server for the `calls-offloader` service. The recommended starting point is **8 vCPU / 16 GB RAM**, or you can use **Appendix B.2** to estimate recording capacity and transcription load.

**TURN Server**
If you've determined in Step 1.3.2 that your users cannot reliably reach the media server over UDP or TCP `8443`, you will need to provision your TURN server now.

Mattermost recommends installing [coturn](https://github.com/coturn/coturn).


Before moving to Step 1.5, confirm the following:

- [ ] Every required server or VM has been created.
- [ ] Every required server has the IP address or DNS name you plan to use later in configuration.
- [ ] You have administrative access to every required server. (test with `ssh <user>@<SERVER_IP>`)

### 1.5 Network Configuration

Here you'll find which network ports need to be opened for each server involved in your Calls deployment. Open the ports in the tables below on each server in your deployment. Work through one server at a time — open every port listed for that server before moving to the next.

**How you open ports depends on your environment:**

- **Cloud deployments (AWS, Azure, GCP):** Configure inbound and outbound rules in your cloud provider's security group or network ACL for each instance. This is done in the cloud console, not on the server itself. The instance must exist before you can configure its rules, which is why provisioning in Step 1.4 comes first.
- **On-premises or self-managed VMs:** Use `firewalld` (RHEL/CentOS) or `ufw` (Ubuntu/Debian) commands directly on each server. Examples:
  - `sudo firewall-cmd --permanent --add-port=8443/udp && sudo firewall-cmd --reload`
  - `sudo ufw allow 8443/udp`
- **Centrally managed firewall:** If a network team manages your firewall, share the tables below with them and request the rules before proceeding.

#### Mattermost server ports

| Port | Protocol | Direction | Source | Destination | Notes |
|---|---|---|---|---|---|
| 443 | TCP | Inbound | Mattermost clients | Mattermost server | HTTPS and WebSocket signaling. |
| 8443 | UDP | Inbound | Mattermost clients | Mattermost server | Media traffic in Integrated mode. |
| 8443 | TCP | Inbound | Mattermost clients | Mattermost server | Media traffic in Integrated mode. |
| 3478 | UDP | Outbound | Mattermost server | `stun.global.calls.mattermost.com` | (Optional - Step 1.3.1) Public IP discovery using STUN. |

#### RTCD server ports

If you deployed an RTCD server in Step 1.4, open these ports:

| Port | Protocol | Direction | Source | Destination | Notes |
|---|---|---|---|---|---|
| 8443 | UDP | Inbound | Mattermost clients and calls-offloader server | RTCD server | Media traffic. |
| 8443 | TCP | Inbound | Mattermost clients and calls-offloader server | RTCD server | Media fallback. |
| 8045 | TCP | Inbound | Mattermost server | RTCD server | RTCD API. Internal only — do not expose publicly. |
| 3478 | UDP | Outbound | RTCD server | `stun.global.calls.mattermost.com` | (Optional - Step 1.3.1) Public IP discovery using STUN. |

```{important}
If you use NGINX as a reverse proxy in front of Mattermost, note that NGINX cannot forward UDP traffic. Port 8443 must be opened directly on the server running the media service — not on NGINX. Port 443 is the only port NGINX handles for Calls.
```

#### Recording server ports

If you deployed a calls-offloader server in Step 1.4, open these ports:

| Port | Protocol | Direction | Source | Destination | Notes |
|---|---|---|---|---|---|
| 4545 | TCP | Inbound | Mattermost server | calls-offloader server | Job service API. Internal only — do not expose publicly. |
| 8443 | UDP | Outbound | calls-offloader server | Mattermost server and RTCD server | Recorder and transcriber jobs connect to the media service as call participants. |
| 8443 | TCP | Outbound | calls-offloader server | Mattermost server and RTCD server | Fallback if UDP is unavailable. |
| 443 | TCP | Outbound | calls-offloader server | Mattermost server | Recorder and transcriber jobs post results back to Mattermost. |

#### TURN server ports

If you deployed a TURN server in Step 1.4, open these ports. If you are using `coturn`, these are the common defaults:

| Port | Protocol | Direction | Source | Destination | Notes |
|---|---|---|---|---|---|
| 3478 | UDP and TCP | Inbound | Mattermost clients | TURN server | STUN and TURN relay. |
| 5349 | UDP and TCP | Inbound | Mattermost clients | TURN server | TURN over TLS. Optional — only if you configure TLS on coturn. |
| 49152–65535 | UDP | Inbound | Mattermost clients | TURN server | TURN relay port range required for coturn to relay media. |

### 1.6 Verification Checks

These checks test firewall and network reachability only — they do not require Calls, RTCD or `calls-offloader` to be installed.

First, you'll have to install `nmap` on each machine you'll run checks from using `sudo apt install nmap` (Ubuntu or Debian) or `sudo dnf install nmap` (RHEL or CentOS)

When you excute each check below, `nmap` will return `open`, `closed` or `filtered`.

**Pass**:
- `open`: Port is reachable and the service is running. Expected if you've already installed the RTCD or `calls-offloader` services (Phase 3-4).
- `closed`: Port is reachable but the service is not running. Expected if you just provisioned the infrastructure in Step 1.4.
**Fail**: 
- `filtered`: Firewall is blocking the port. Revisit your networking configuration in Step 1.5 before continuing.

**All deployments**

Run from a client machine on the same network as your users:

| Check | Command | `TARGET_IP` | Description |
|---|---|---|---|
| 1.6.2 | `sudo nmap -sU -p 8443 TARGET_IP` | Mattermost server IP | Clients can send UDP media to the Mattermost server |
| 1.6.3 | `nmap -p 8443 TARGET_IP` | Mattermost server IP | Clients can reach the Mattermost server for TCP media fallback |

**RTCD deployments**

Run from a client machine on the same network as your users:

| Check | Command | `TARGET_IP` | Description |
|---|---|---|---|
| 1.6.4 | `sudo nmap -sU -p 8443 TARGET_IP` | RTCD server IP | Clients can send UDP media to the RTCD server |
| 1.6.5 | `nmap -p 8443 TARGET_IP` | RTCD server IP | Clients can reach the RTCD server for TCP media fallback |

Run from the Mattermost server:

| Check | Command | `TARGET_IP` | Description |
|---|---|---|---|
| 1.6.6 | `nmap -p 8045 TARGET_IP` | RTCD server IP | Mattermost can reach the RTCD API |

**Recording deployments**

Run from the Mattermost server:

| Check | Command | `TARGET_IP` | Description |
|---|---|---|---|
| 1.6.7 | `nmap -p 4545 TARGET_IP` | calls-offloader server IP | Mattermost can reach the calls-offloader API |

Run from the calls-offloader server:

| Check | Command | `TARGET_IP` | Description |
|---|---|---|---|
| 1.6.8 | `sudo nmap -sU -p 8443 TARGET_IP` | RTCD server IP | `calls-offloader` can send UDP media to the media service to join calls for recording |
| 1.6.9 | `nmap -p 8443 TARGET_IP` | RTCD server IP | `calls-offloader` can reach the media service for TCP media fallback |
| 1.6.10 | `nmap -p 443 TARGET_IP` | Mattermost server IP | `calls-offloader` can post recordings back to Mattermost |

**TURN deployments**

Run from a client machine on the same network as your users:

| Check | Command | `TARGET_IP` | Description |
|---|---|---|---|
| 1.6.11 | `sudo nmap -sU -p 3478 TARGET_IP` | TURN server IP | Clients can reach the TURN server on UDP 3478 |
| 1.6.12 | `nmap -p 3478 TARGET_IP` | TURN server IP | Clients can reach the TURN server on TCP 3478 |
| 1.6.13 | `nmap -p 5349 TARGET_IP` | TURN server IP | Clients can reach the TURN server over TLS (only if you configured TLS on coturn) |
| 1.6.14 | `sudo nmap -sU -p 49152 TARGET_IP` | TURN server IP | Spot check of the TURN relay port range |

```{important}
**Do not proceed to Phase 2 until all checks in this section relevant to your deployment architecture are passing. If any check fails, go to [Appendix A: Troubleshooting](#appendix-a-troubleshooting).**
```

---

## Phase 2: Configure Integrated Calls

You will start by deploying Calls using the Integrated architecture, even if you plan to use RTCD or `calls-offloader` services. This approach gives you a clean baseline: if Calls does not work using the simplest deployment method, the problem is usually networking, firewall rules, or plugin configuration. It is much easier to isolate those problems before you add RTCD or `calls-offloader` in later phases.

### 2.1 Prerequisites

- [ ] Phase 1 networking checks passed (1.6.1-1.6.14)
- [ ] Two test accounts on your Mattermost instance
- [ ] System Admin permissions on your Mattermost instance

### 2.2 Configure the Calls plugin

The Calls plugin is prepackaged with Mattermost self-hosted deployments. Go to **System Console > Plugins > Calls > Settings** and complete the following steps:

**2.2.1: Enable the plugin**

Set **Enable Plugin** to `true`. This enables editing for the rest of the configuration settings on the page.

**2.2.2: Put the deployment in test mode**

Set **Test mode** to `on`. This ensures System Admins must enable Calls in individual channels before end users can access the feature.

**2.2.3: Configure the host media address**

Set **ICE Host Override** to the IP address clients will use to reach the media service. This is based on the STUN decision tree you completed in Step 1.3.1.

- If your users are in an private network, VPN, or air-gapped environment, set it to the private address of the Mattermost server they can reach.
- If your Mattermost server has a stable public IP, set it to that IP.
- Otherwise, leave it empty for automatic public address discovery using STUN.

**2.2.4: Configure TURN Servers**

If TURN is being used, replace or extend the **ICE server configurations** array with your TURN server details:

```json
[
  {
    "urls": ["turn:turn.example.com:3478"],
    "username": "<USERNAME>",
    "credential": "<PASSWORD>"
  }
]
```

If your TURN deployment uses short-lived generated credentials, also set **TURN Static Auth Secret** and **TURN Credentials Expiration**.

**2.3.5: Save configuration**

Click **Save** on the Calls settings page. It is generally also recommended restart the plugin after changing media server settings:

1. Go to **System Console > Plugins > Plugin Management**.
2. Disable **Calls** and wait a few seconds.
3. Enable **Calls** again.

### 2.4 Verification Checks

Now you can move to smoke testing your Calls deployment with your test accounts. Specifically,

- Create a test channel such as `calls-test`. 
- Open the **Channel menu**, then select **Enable calls**.
- Invite your test users into the channel so you can validate a real call.

| Check | Action | Pass criteria |
|---|---|---|
| 2.4.1 | Start a call from the test channel with a second user | Both users are in the call |
| 2.4.2 | Speak during the call | Both users can hear each other clearly |
| 2.4.3 | Share your screen from a desktop app or supported browser | Screen sharing is visible to the other user |
| 2.4.4 | End the call | The call indicator disappears from the channel |

```{important}
**Do not continue until all of the checks pass. If any check fails, go to [Appendix A: Troubleshooting](#appendix-a-troubleshooting).**
```

---

## Phase 3: Install and Configure RTCD

Now that you've verified a basic Integrated Calls deployment, you can add RTCD to move media handling off the Mattermost server.

**You can skip this phase if you are using Integrated Calls only.**

### 3.1 Prerequisites

- [ ] RTCD server is provisioned (1.4) and networking checks passed (1.6.1-1.6.14)
- [ ] Integrated Calls deployment checks passed (2.4.1-2.4.4)
- [ ] Mattermost Enterprise or Enterprise Advanced license is active on your server


### 3.3 Install RTCD

Follow the [RTCD Setup and Configuration](calls-rtcd-setup.md) guide for the actual installation. The guide covers:

- Binary or Docker installation
- `rtcd.toml` configuration
- Service setup
- TURN configuration (if applicable)

Before proceeding, run these checks from the Mattermost server to verify your RTCD service is running and accessible:

| Check | Command | Pass criteria |
|---|---|---|
| 3.3.1 | `nmap -p 8045 YOUR_RTCD_SERVER` | `open` — RTCD is running and accepting connections. |
| 3.3.2 | `curl http://YOUR_RTCD_SERVER:8045/version` | Returns a JSON version string |

### 3.4 Connect Mattermost to RTCD

Once you have completed installation, configuration and validation of your RTCD service, you will update the Calls plugin configuration settings to use it:

1. Go to **System Console > Plugins > Calls**.
2. Set **RTCD Service URL** to your RTCD address. If RTCD credentials were generated during setup, embed them directly in the URL:

   ```
   http://clientID:authKey@rtcd.internal:8045
   ```

   Replace `clientID` and `authKey` with the values generated during RTCD setup. The first connection to RTCD self-registers the client and stores the authentication key in the database.
   
   Alternatively, set credentials via environment variables on the Mattermost server: `MM_CALLS_RTCD_CLIENT_ID` and `MM_CALLS_RTCD_AUTH_KEY`.

3. Click **Save** and restart the Calls plugin so the change takes effect.


### 3.5 Configure Calls Monitoring

Before your pilot, set up Calls monitoring so you can see sessions, errors, CPU, and memory while real users are testing.

See [Calls Metrics and Monitoring](calls-metrics-monitoring.md) for:

- Prometheus configuration
- RTCD metrics on `http://RTCD_SERVER:8045/metrics`
- Calls plugin metrics on `http://MATTERMOST_SERVER:8067/plugins/com.mattermost.calls/metrics`
- Grafana visualization using dashboard ID `23225`

### 3.6 Verification Checks

Now you can move to smoke testing your RTCD Calls deployment with your test accounts. Specifically,

| Check | Action | Pass criteria |
|---|---|---|
| 3.6.1 | Start a call from the test channel with a second user | Both users are in the call |
| 3.6.2 | Speak during the call | Both users can hear each other clearly |
| 3.6.3 | Share your screen from a desktop app or supported browser | Screen sharing is visible to the other user |
| 3.6.4 | End the call | The call indicator disappears from the channel |

```{important}
**Do not continue until all of the checks pass. If any check fails, go to [Appendix A: Troubleshooting](#appendix-a-troubleshooting).**
```

---

## Phase 4: Add calls-offloader for recording, transcription, and live captions

`calls-offloader` is the job service that handles call recording, transcription, and live captions. You can add it after Phase 2 on Integrated Calls or after Phase 3 on RTCD. For most production environments, pair it with RTCD.

**You can skip this phase if you do not need recording, transcription, or live captions.**

### 4.1 Prerequisites

- [ ] `calls-offloader` server is provisioned (1.4) and networking checks passed (1.6.1-1.6.14)
- [ ] RTCD verification checks passed (3.6.1-3.6.4)
- [ ] Mattermost Enterprise or Enterprise Advanced license is active on your server

### 4.2 Install calls-offloader

Follow the [Calls Offloader Setup and Configuration](calls-offloader-setup.md) guide for installation. The guide covers:

- Binary installation
- `config.toml` configuration
- Systemd service setup
- Docker-backed jobs
- Private network overrides
- Air-gapped installation

Before proceeding, run these checks from the Mattermost server to verify calls-offloader is running and accessible:

| Check | Command | Pass criteria |
|---|---|---|
| 4.2.1 | `nmap -p 4545 YOUR_OFFLOADER_SERVER` | `open` — calls-offloader is running and accepting connections. |
| 4.2.2 | `curl http://YOUR_OFFLOADER_SERVER:4545/version` | Returns a JSON version string |

### 4.3 Connect calls-offloader to Mattermost

1. Go to **System Console > Plugins > Calls**.
2. Set **Job Service URL** to the calls-offloader address, for example `http://calls-offloader.internal:4545`.
3. Enable **Call Recordings** if needed.
4. Enable **Call Transcriptions** if needed. Transcriptions require recordings to be enabled.
5. Enable **Live Captions** if needed. Live captions require both recordings and transcriptions to be enabled.
6. Click **Save** and restart the Calls plugin so the change takes effect.

### 4.4 Verification Checks

Now you can move to smoke testing your Calls deployment with recording using your test accounts. Specifically,

| Check | Action | Pass criteria |
|---|---|---|
| 4.5.2 | During a call, start a recording as a call host | Recording starts without error. |
| 4.5.3 | End the call or stop the recording | An MP4 file appears in the call thread after processing is complete. |
| 4.5.4 | With transcription enabled, end a recorded call | A MP4 file and transcript file appear in the call thread after processing is complete. |
| 4.5.5 | With live captions enabled, start a recorded call | Captions appear during the call within 1-3 seconds after participants speak. |

```{important}
**Do not continue until all of the checks pass. If any check fails, go to [Appendix A: Troubleshooting](#appendix-a-troubleshooting).**
```

---

## Phase 5: Pilot rollout

Now that the technical configuration is complete and validated, run a small pilot with real users before broad rollout. The goal is to confirm Calls works reliably across the clients and locations your organization uses, and that your servers stay healthy under normal usage.

### 5.1 Prerequisites

- [ ] Phase 2 passed
- [ ] Phase 3 passed if using RTCD
- [ ] Phase 4 passed if using calls-offloader
- [ ] You have 5 to 10 pilot users from different locations
- [ ] Pilot users have current [Mattermost desktop and mobile apps](https://mattermost.com/apps/)

### 5.2 Prepare the pilot channel

**5.2.1: Create the pilot channel**

Create a channel such as `calls-pilot` and enable Calls in it. If test mode is still enabled, a system admin must start each call.

**5.2.2: Post the pilot message**

Send pilot users the following message so they know what to test and how to report issues.

<details>
<summary>Click to expand the pilot message template</summary>

```markdown
## Mattermost Calls pilot

We are testing Mattermost Calls before wider rollout.

**What you are testing**

- starting and joining an audio call
- hearing other participants clearly
- screen sharing from desktop or browser
- joining from different clients or networks if possible

**How to start**

Select **Start call** in the channel header. Anyone in this channel can join.

**Please try the following**

- [ ] Join a 1:1 test call
- [ ] Join a group call with at least 3 participants
- [ ] Share your screen from desktop or browser
- [ ] Join from a second client if possible
- [ ] Join from home, VPN, or mobile data if possible

**If something fails**

Reply in this channel with:

- what step failed
- what you expected to happen
- what actually happened
- your client type (desktop, browser, or mobile)
```

</details>

### 5.3 What to watch during the pilot

Monitor the following while pilot calls are running:

- **Active sessions and participants**: Confirm calls are being counted in your Calls metrics.
- **RTC errors**: Watch `rtcd_rtc_errors_total` (RTCD) or the equivalent Calls plugin metrics in integrated mode.
- **CPU and memory**: Watch `rtcd_process_cpu_seconds_total` and `rtcd_process_resident_memory_bytes` (RTCD) or the equivalent plugin metrics in integrated mode.
- **Service logs**: Watch Mattermost, RTCD, and calls-offloader logs for recurring `ERROR` or `WARN` lines.

If you do not have Prometheus and Grafana set up yet, tail the service logs directly during pilot sessions.

### 5.4 Verification Checks

Do not continue until all of the following pass. If any check fails, go to [Appendix A: Troubleshooting](#appendix-a-troubleshooting).

| Check | Action | Pass criteria |
|---|---|---|
| 5.4.1 | Two pilot users complete a 1:1 audio call | Both users can hear each other clearly for the duration of the call |
| 5.4.2 | Run a group call with at least 3 pilot users | All participants can hear each other clearly |
| 5.4.3 | Run a call lasting 15 minutes or longer | No unexpected drops or audio degradation |
| 5.4.4 | Share your screen from a desktop app or browser during a pilot call | Screen sharing is visible to other participants |
| 5.4.5 | Have at least one user join from outside the main office network (home, VPN, or mobile data) | Call quality is acceptable from that network |
| 5.4.6 | Have at least one user join on mobile | Call joins and audio works on mobile |
| 5.4.7 | If recording is enabled, start and stop a recording during a pilot call | MP4 file appears in the call thread |
| 5.4.8 | If transcription is enabled, stop a recording | Transcript file appears after processing |
| 5.4.9 | If live captions are enabled, run a recorded pilot call | Captions appear in real time for participants |
| 5.4.10 | Run `/call stats` after a successful pilot call | Output is returned — save it for your deployment notes |

```{important}
**Do not continue until all checks pass.**
```

---

## Phase 6: Production rollout

### 6.1 Overview

Roll Calls out in waves instead of enabling it everywhere at once.

That lets you watch real usage, catch problems early, and stop the rollout cleanly if needed.

### 6.2 Prepare user communication

Create a support channel such as `calls-help` first, then send a short announcement.

<details>
<summary>Click to expand the user announcement template</summary>

```markdown
## Mattermost Calls is available

You can now start audio calls directly from Mattermost and share your screen without leaving the platform.

**How to start a call**

Select **Start call** in the channel header. Anyone in that channel can join.

**What is available**

- audio calls
- screen sharing
- group calls, if enabled for your deployment
- recording, transcription, and live captions, if enabled for your deployment

**Things to know**

- the first time you join, your browser or desktop app may ask for microphone permission
- screen sharing may also require screen capture permission
- if you need help, post in `#calls-help`
```

</details>

### 6.3 Roll out in waves

#### 6.3.1 Wave 1

Enable Calls in IT or admin channels first.

Use this wave to confirm:

- support staff know how Calls works
- internal admins know where to look when users report problems

#### 6.3.2 Wave 2

If the admin-only validation is stable, switch the deployment from **test mode** to **live mode**, then enable Calls in engineering or power-user channels.

Use this wave to gather broader feedback from users who are likely to try more edge cases.

#### 6.3.3 Wave 3

When the earlier waves are stable, expand rollout to the rest of the organization.

### 6.4 Watch the rollout

During each wave, watch:

- call volume
- repeated user complaints about joining or audio quality
- recurring RTC errors
- CPU and memory on the media service
- recording and transcription job failures, if enabled

If you stay on integrated Calls and see sustained media load during rollout, plan a move to RTCD before you expand usage further.

Do not move to the next wave until the current one is stable.

### 6.5 Rollback plan

If something goes wrong, choose the smallest rollback that solves the problem.

**Per-channel rollback**

1. Open the affected channel menu.
2. Select **Disable calls**.

**Return to test mode**

1. Go to **System Console > Plugins > Calls**.
2. Switch the deployment back to test mode.

**Full rollback**

1. Go to **System Console > Plugins > Plugin Management**.
2. Disable the Calls plugin.

Keep your existing conferencing option available until Calls is stable in production for your environment.

---

## Appendix A: Troubleshooting

For log collection details, see [Calls Troubleshooting](calls-troubleshooting.md).

### A.1 Collect the right evidence before asking for help

Before opening a support case, capture as many of these as you can:

- the phase and step where the failure happened
- `/call stats` output from a recent failed or successful test
- `/call logs` output from the most recent call
- `curl` output from `RTCD` or `calls-offloader` version checks
- relevant Mattermost, RTCD, or calls-offloader logs

### A.2 The call button is missing

Common causes:

- the Calls plugin is disabled
- the deployment is still in test mode and the channel is not configured the way you expect
- the user is on an older client

What to check:

1. **System Console > Plugins > Plugin Management** to confirm Calls is enabled.
2. **System Console > Plugins > Calls** to confirm the deployment state.
3. The channel menu to confirm Calls is enabled for that channel.

### A.3 A call starts, but audio does not work

Common causes:

- UDP `8443` is blocked
- clients are falling back poorly because TCP `8443` is also blocked
- the wrong media address is being advertised
- browser or desktop microphone permissions were denied

What to do:

1. Repeat the UDP and TCP connectivity checks from Phase 1.
2. Re-check the integrated media address configuration in Phase 2, or RTCD address configuration in Phase 3.
3. Run `/call stats` after the failed test and compare the negotiated connection details.

### A.4 Remote users cannot join from outside the office

Common causes:

- external firewall rules do not allow media traffic to reach the media service
- the advertised media address is private instead of public
- the deployment needs TURN for restrictive client networks

What to do:

1. Confirm external reachability to UDP `8443`.
2. Confirm the address being advertised to clients is the correct reachable address.
3. If direct connectivity still fails for restrictive networks, add TURN.

### A.5 Recording, transcription, or captions are failing

Common causes:

- calls-offloader is not running
- Mattermost cannot reach `Job Service URL`
- the offloader service account cannot use Docker
- recorder or transcriber jobs cannot reach Mattermost on the expected internal URL

What to do:

1. Run `curl http://YOUR_OFFLOADER_SERVER:4545/version` from the Mattermost server.
2. Confirm the calls-offloader service is running.
3. Confirm the calls-offloader service account can access Docker.
4. If using private network overrides, re-check `MM_CALLS_RECORDER_SITE_URL` and `MM_CALLS_TRANSCRIBER_SITE_URL`.

### A.6 Calls work briefly, then drop

Common causes:

- unstable WebSocket connectivity between clients and Mattermost
- Mattermost restarted during the call
- a load balancer or network device is timing out long-lived connections

What to do:

1. Confirm the Mattermost server is stable and reachable.
2. Review load balancer settings for WebSocket support and idle timeout behavior.
3. Compare Mattermost logs with the call failure time.

### A.7 RHEL deployments using firewalld or fapolicyd

If you deploy on RHEL with `firewalld` or `fapolicyd` enabled, see the [RHEL deployment guide](https://docs.mattermost.com/deployment-guide/server/deploy-linux.html#itab--RHEL-CentOS--0_1-RHEL-CentOS).

Key points:

- the Calls plugin is covered by standard Mattermost `fapolicyd` rules
- standalone `rtcd` requires its own `fapolicyd` configuration
- you still need to open the required Calls and RTCD ports

---

## Appendix B: Server sizing benchmarks

Use this appendix as a starting point, then validate against your own traffic during Phase 5.

### B.1 RTCD benchmark examples

The [Calls Metrics and Monitoring](calls-metrics-monitoring.md) guide includes internal RTCD benchmark data. The examples below are taken directly from that guide and show why screen sharing and total egress bandwidth matter so much for sizing.

| Workload example | RTCD instance | Average CPU | Average memory | Bandwidth in / out |
|---|---|---|---|---|
| 1 call, 1000 participants, 2 unmuted, no screen sharing | `c7i.xlarge` | 47% | 1.46 GB | 1 Mbps / 194 Mbps |
| 1 call, 1000 participants, 1 unmuted, screen sharing enabled | `c7i.xlarge` | 79% | 1.54 GB | 2.9 Mbps / 1.68 Gbps |
| 2 calls, 1000 participants each, screen sharing enabled | `c7i.2xlarge` | 73% | 2.38 GB | 5.7 Mbps / 3.06 Gbps |
| 4 calls, 1000 participants each, screen sharing enabled | `c7i.4xlarge` | 83% | 4.40 GB | 14.5 Mbps / 7.17 Gbps |

How to use this table:

- If you expect large calls with screen sharing, plan around **egress bandwidth** first.
- If you expect many medium-sized calls, use the metrics guide to compare similar benchmark patterns.
- Validate your assumptions during the pilot instead of sizing only from theory.

### B.2 calls-offloader sizing inputs

The published `calls-offloader` performance guide uses an AWS `c6i.2xlarge` host (`8 vCPU / 16 GB RAM`) as the recommended starting point for recordings.

| Recording quality | Recommended `max_concurrent_jobs` | Average CPU | Average memory | Average recording size |
|---|---|---|---|---|
| Low | 8 | 66% | 4 GB | 0.5 GB/hour |
| Medium | 6 | 66% | 4 GB | 0.7 GB/hour |
| High | 4 | 72% | 4 GB | 1.2 GB/hour |

Audio-only recordings consume approximately `1 MB` per minute per participant.

Use those numbers to estimate:

- total storage needed
- how many recordings can run at the same time
- the `max_concurrent_jobs` setting you should start with
- how aggressively you need retention and cleanup policies

If recordings are large or long-lived, also review Mattermost `FileSettings.MaxFileSize` and any proxy upload/body-size limits in front of Mattermost.

### B.3 Transcriptions and live captions

Transcriptions and live captions increase load on the offloader host.

Published offloader guidance highlights these planning points:

- The `small` model is not recommended for live captions.
- `base` live captions need at least `2` threads for real-time performance and work best with `3` or `4`.
- If you expect more than 3 simultaneous live-captioned calls on one host, plan for horizontal scaling.

For additional offloader performance guidance, see the [calls-offloader performance documentation](https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md).

### B.4 TURN server planning

TURN planning is mostly a bandwidth question.

If you must use TURN:

- estimate how many users are likely to need relay traffic
- remember TURN relays all media for those users
- place TURN where it is network-close to the users who need it

---

## Related Documentation

- [RTCD Setup and Configuration](calls-rtcd-setup.md)
- [Calls Offloader Setup and Configuration](calls-offloader-setup.md)
- [Calls Metrics and Monitoring](calls-metrics-monitoring.md)
- [Calls Deployment on Kubernetes](calls-kubernetes.md)
- [Calls Troubleshooting](calls-troubleshooting.md)
- [Calls plugin configuration settings](https://docs.mattermost.com/configure/plugins-configuration-settings.html#calls)
