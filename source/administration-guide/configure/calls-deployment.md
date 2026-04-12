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

1. **Are all users and your media server (Mattermost server or RTCD) in the same private network, VPN, or air-gapped environment (no outside clients)?**
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
- `open`: Port is reachable and the service is listeneing. Expected if you've already installed the RTCD or `calls-offloader` services)
- `closed`: Port is reachable but the service has not yet been installed. Expected if you just provisioned the machines in Step 1.4)
**Fail**: 
- `filtered`: Firewall is blocking the port. Revisit your networking configuration in Step 1.5 before continuing.

**All deployments**

Run from a client machine on the same network as your users:

| Check | Command | Replace `TARGET_IP` with | Description |
|---|---|---|---|
| 1.6.2 | `sudo nmap -sU -p 8443 TARGET_IP` | Mattermost server IP | Clients can send UDP media to the Mattermost server |
| 1.6.3 | `nmap -p 8443 TARGET_IP` | Mattermost server IP | Clients can reach the Mattermost server for TCP media fallback |

**RTCD deployments**

Run from a client machine on the same network as your users:

| Check | Command | Replace `TARGET_IP` with | Description |
|---|---|---|---|
| 1.6.4 | `sudo nmap -sU -p 8443 TARGET_IP` | RTCD server IP | Clients can send UDP media to the RTCD server |
| 1.6.5 | `nmap -p 8443 TARGET_IP` | RTCD server IP | Clients can reach the RTCD server for TCP media fallback |

Run from the Mattermost server:

| Check | Command | Replace `TARGET_IP` with | Description |
|---|---|---|---|
| 1.6.6 | `nmap -p 8045 TARGET_IP` | RTCD server IP | Mattermost can reach the RTCD API |

**Recording deployments** — run from the Mattermost server:

| Check | Command | Replace `TARGET_IP` with | Description |
|---|---|---|---|
| 1.6.7 | `nmap -p 4545 TARGET_IP` | calls-offloader server IP | Mattermost can reach the calls-offloader API |

#### 1.6.8 Final checklist

- [ ] Clients can reach the media service on UDP `8443`.
- [ ] Clients can reach the media service on TCP `8443` if you plan to rely on TCP fallback.
- [ ] Mattermost can reach RTCD on TCP `8045` — if using RTCD.
- [ ] Mattermost can reach calls-offloader on TCP `4545` — if using calls-offloader.
- [ ] If using STUN, confirm the media service can reach `stun.global.calls.mattermost.com` on UDP `3478` — validated in Phase 2 when you verify the plugin advertises the correct public IP.

Before you leave Phase 1, plan at least one **real client-side test** in Phase 2 or Phase 5 from the same type of network your users will actually use, such as office LAN, home internet, VPN, or mobile data.

````{dropdown} If nmap is not available
If you cannot install `nmap`, you can use `nc` instead. Unlike `nmap`, `nc` requires a temporary listener running on the target server before the check can work.

Install `nc`:

- Ubuntu or Debian: `sudo apt install netcat-openbsd`
- RHEL or CentOS: `sudo dnf install nmap-ncat`

**For TCP checks** (8443, 8045, 4545): On the target server, start a listener on the port you're testing:

```bash
nc -l -p PORT
```

Then from the source machine:

```bash
nc -zv TARGET_IP PORT
```

Pass: `Connection to ... succeeded`

Fail: `Connection refused` (nothing is listening — the firewall is open, start the listener first) or timeout (firewall is blocking — fix before proceeding).

**For UDP 8443**: On the media server, start a UDP listener:

```bash
nc -lu 8443
```

Then from a client machine:

```bash
nc -u TARGET_IP 8443
```

Type a short message and press Enter. If it appears on the server, the port is open. Stop listeners with `Ctrl+C`.
````

---

## Phase 2: Configure and validate integrated Calls

### 2.1 Overview

Start here even if you know you want RTCD later.

That gives you a clean baseline: if Calls does not work in integrated mode, the problem is usually networking, NAT, firewall rules, or plugin configuration. It is much easier to isolate those problems before you add RTCD or calls-offloader.

### 2.2 Prerequisites

- [ ] Phase 1 passed
- [ ] You have at least two Mattermost test accounts
- [ ] You have System Admin access

### 2.3 Configure the Calls plugin

The Calls plugin is prepackaged with Mattermost self-hosted deployments.

#### 2.3.1 Enable the plugin

Go to **System Console > Plugins > Calls** and confirm the plugin is enabled.

If it is disabled, go to **System Console > Plugins > Plugin Management**, find **Calls**, and enable it.

#### 2.3.2 Put the deployment in test mode

Use the **Test mode** setting in **Plugins > Calls** so you can validate Calls before switching to live mode for all users.

When the deployment is in test mode:

- system admins can validate Calls first
- users are prompted to contact a system admin instead of starting calls broadly

#### 2.3.3 Set the participant limit for testing

Set **Max call participants** to `50`.

Why this matters:

- the default is `0`, which means unlimited
- the recommended maximum is `50`
- setting it now prevents accidental oversized tests while you validate the deployment

#### 2.3.4 Configure the advertised media address

If you are using integrated Calls, use the Calls plugin settings below to tell clients how to reach the media service.

**ICE** is the part of WebRTC that helps clients discover which address and port to use for media traffic.

- **ICE Host Override**: Use this when you want to advertise a specific IP address or hostname to clients instead of relying on automatic discovery through STUN.
- **ICE Host Port Override**: Use this if clients must connect on a different external port than the one the service listens on locally.
- **ICE server configurations**: Use this for STUN and TURN configuration.

Use the following rules:

- If your Mattermost server has a stable public IP that clients can reach, set **ICE Host Override** to that IP.
- If your users are all on a private network or VPN, set **ICE Host Override** to the private address they can actually reach.
- If you want the service to discover its own public address, leave **ICE Host Override** empty and use STUN.
- If you use a hostname instead of an IP, verify that DNS resolution on the Mattermost host matches what clients will actually reach. When in doubt, use an IP address directly.

```{note}
`ICE Host Override` only applies when you are hosting media through the plugin itself. Once you move Calls media to RTCD in Phase 3, RTCD handles its own media address configuration.
```

#### 2.3.5 Configure STUN or TURN

The default **ICE server configurations** value is:

```json
[{"urls":["stun:stun.global.calls.mattermost.com:3478"]}]
```

If you need TURN, use a JSON array such as:

```json
[
  {
    "urls": ["turn:turn.example.com:3478"],
    "username": "REPLACE_ME_USERNAME",
    "credential": "REPLACE_ME_PASSWORD"
  }
]
```

Use `credential` (singular) in the JSON. Replace the example values with your real TURN credentials.

If your TURN deployment uses generated short-lived credentials, also configure:

- **TURN Static Auth Secret**
- **TURN Credentials Expiration**

#### 2.3.6 Save and restart the plugin if needed

Some network-facing Calls settings require a plugin restart to take effect. After changing **ICE Host Override**, **ICE Host Port Override**, or similar media settings:

1. Go to **System Console > Plugins > Plugin Management**.
2. Disable **Calls**.
3. Wait a few seconds.
4. Enable **Calls** again.

### 2.4 Create a small test channel

#### 2.4.1 Create the channel

Create a test channel such as `calls-test`.

#### 2.4.2 Enable Calls in that channel

From the channel header:

1. Open the channel menu.
2. Select **Enable calls**.

#### 2.4.3 Add your test users

Add at least two users so you can validate a real call.

### 2.5 Verification gate

Do not continue until all of the following pass.

- [ ] **2.V1** Start a call from the test channel and confirm that a second user can join.
- [ ] **2.V2** Confirm both users can hear each other clearly.
- [ ] **2.V3** Confirm screen sharing works from a desktop app or supported browser.
- [ ] **2.V4** End the call cleanly and confirm the call indicator disappears.
- [ ] **2.V5** Run `/call stats` immediately after the test call and save the output for your deployment notes.

If any of these checks fail, stop here and go to [Appendix A: Troubleshooting](#appendix-a-troubleshooting).

---

## Phase 3: Add RTCD

### 3.1 Overview

RTCD moves media handling off the Mattermost server. That improves isolation and gives you a better path for production scaling.

Skip this phase if you are staying with integrated Calls.

### 3.2 Prerequisites

- [ ] Phase 2 passed
- [ ] Mattermost Enterprise license is active
- [ ] RTCD server is provisioned
- [ ] Mattermost can reach RTCD on TCP `8045`
- [ ] Clients can reach the RTCD media ports on `8443`

### 3.3 Install and configure RTCD

Follow the [RTCD Setup and Configuration](calls-rtcd-setup.md) guide for the actual installation.

That guide covers:

- binary or Docker installation
- `rtcd.toml` configuration
- service setup
- TURN configuration
- validation with `curl http://HOST:8045/version` (or `https://` if you enabled TLS)
- horizontal scaling

If RTCD is behind NAT or a load balancer, configure its advertised media address in `rtcd.toml` before continuing.

When you move media handling to RTCD, configure the **media-plane** address and TURN/STUN settings in `rtcd.toml`. The plugin's client-facing ICE settings still matter for what gets sent to clients, so keep the plugin and RTCD settings aligned.

### 3.4 Connect Mattermost to RTCD

From the Mattermost server, verify the RTCD API first. If you enabled TLS on the RTCD API, use `https://` instead of `http://`:

```bash
curl http://YOUR_RTCD_SERVER:8045/version
```

Pass:

- you receive JSON version information

Then configure Mattermost:

1. Go to **System Console > Plugins > Calls**.
2. Set **RTCD Service URL** to your RTCD address, for example `http://rtcd.internal:8045`.
3. If RTCD credentials were generated during setup, include them in the URL or use `MM_CALLS_RTCD_CLIENT_ID` and `MM_CALLS_RTCD_AUTH_KEY` on the Mattermost server.
4. Save the setting.
5. Restart the Calls plugin so the change takes effect.

```{note}
The `RTCD Service URL` setting supports credentials in the form `http://clientID:authKey@hostname`. The first connection self-registers the client and stores the authentication key in the database.
```

### 3.5 Set up monitoring before the pilot

Before your pilot, set up Calls monitoring so you can see sessions, errors, CPU, and memory while real users are testing.

See [Calls Metrics and Monitoring](calls-metrics-monitoring.md) for:

- Prometheus scrape configuration
- RTCD metrics on `http://RTCD_SERVER:8045/metrics`
- Calls plugin metrics on `http://MATTERMOST_SERVER:8067/plugins/com.mattermost.calls/metrics`
- Grafana dashboard ID `23225`

```{note}
The Calls plugin metrics endpoint depends on Mattermost performance monitoring being enabled. Port `8067` is the default performance listener and may be different in your environment.
```

### 3.6 Verification gate

**3.V0 — Confirm RTCD is listening on TCP 8045**

Run this from the Mattermost server to confirm RTCD started successfully and is accepting connections:

```bash
nc -zv YOUR_RTCD_SERVER 8045
```

Pass: `Connection to ... succeeded`

Fail: `Connection refused` — RTCD is not running or not listening. Check the RTCD service logs before proceeding. If you get a timeout instead of "Connection refused", the firewall path was not properly verified in Step 1.6.4 — go back and fix that first.

- [ ] **3.V1** `curl http://YOUR_RTCD_SERVER:8045/version` returns a version string from the Mattermost server (or `https://` if you enabled TLS).
- [ ] **3.V2** Two users can complete an audio call after `RTCD Service URL` is set.
- [ ] **3.V3** Screen sharing works after `RTCD Service URL` is set.
- [ ] **3.V4** `/call stats` after the test call shows a healthy negotiated connection.
- [ ] **3.V5** RTCD logs or metrics show activity during the test call.

If these checks fail:

- confirm TCP `8045` from Mattermost to RTCD
- confirm UDP and TCP `8443` from clients to RTCD
- confirm the Calls plugin was restarted after the URL change

---

## Phase 4: Add calls-offloader for recording, transcription, and live captions

### 4.1 Overview

`calls-offloader` is the job service used for:

- call recording
- call transcription
- live captions (experimental)

You can add it after Phase 2 on integrated Calls or after Phase 3 on RTCD. For most production environments, pair it with RTCD.

### 4.2 Prerequisites

- [ ] Phase 2 passed
- [ ] If you are using RTCD, Phase 3 also passed
- [ ] Mattermost Enterprise license is active
- [ ] calls-offloader server is provisioned
- [ ] Docker is installed and running on the calls-offloader server
- [ ] The calls-offloader service account can use Docker
- [ ] Mattermost can reach the job service on TCP `4545`
- [ ] You have planned storage for recordings

Storage estimates from the offloader guide:

| Recording quality | Approximate storage per hour | Approximate storage per minute |
|---|---|---|
| Low | 0.5 GB | 8 MB |
| Medium | 0.7 GB | 12 MB |
| High | 1.2 GB | 20 MB |

Audio-only recordings consume approximately `1 MB` per minute per participant.

```{note}
Live captions require both recording and transcription to be enabled.
```

### 4.3 Install and configure calls-offloader

Follow the [Calls Offloader Setup and Configuration](calls-offloader-setup.md) guide for installation.

That guide covers:

- binary installation
- `config.toml`
- systemd service setup
- Docker-backed jobs
- private network overrides
- air-gapped installation

### 4.4 Connect calls-offloader to Mattermost

From the Mattermost server, verify the API first. If you enabled TLS on the offloader API, use `https://` instead of `http://`:

```bash
curl http://YOUR_OFFLOADER_SERVER:4545/version
```

Then configure Mattermost:

1. Go to **System Console > Plugins > Calls**.
2. Set **Job Service URL** to the calls-offloader address, for example `http://calls-offloader.internal:4545`.
3. Enable **Call Recordings** if needed.
4. Enable **Call Transcriptions** if needed. Transcriptions require recordings.
5. Enable **Live Captions** if needed. Live captions require both recordings and transcriptions.
6. Save the settings.
7. Restart the Calls plugin. This is required for `Job Service URL` and recording-related changes to take effect cleanly.

If your recorder or transcriber jobs must reach Mattermost on a different internal address than users do, configure these on the **Mattermost server**:

- `MM_CALLS_RECORDER_SITE_URL`
- `MM_CALLS_TRANSCRIBER_SITE_URL`

See the offloader guide for that private network setup.

### 4.5 AI meeting summaries

If you want AI-generated meeting summaries from call transcripts, configure Mattermost AI separately. See [Enable Copilot](https://docs.mattermost.com/configure/enable-copilot.html).

### 4.6 Verification gate

**4.V0 — Confirm calls-offloader is listening on TCP 4545**

Run this from the Mattermost server to confirm calls-offloader started successfully and is accepting connections:

```bash
nc -zv YOUR_OFFLOADER_SERVER 4545
```

Pass: `Connection to ... succeeded`

Fail: `Connection refused` — calls-offloader is not running or not listening. Check the calls-offloader service logs before proceeding. If you get a timeout instead of "Connection refused", the firewall path was not properly verified in Step 1.6.5 — go back and fix that first.

- [ ] **4.V1** `curl http://YOUR_OFFLOADER_SERVER:4545/version` returns a version string from the Mattermost server (or `https://` if you enabled TLS).
- [ ] **4.V2** A test call still works normally after the job service is configured.
- [ ] **4.V3** A host can start a recording.
- [ ] **4.V4** The MP4 recording appears in the call thread after recording stops.
- [ ] **4.V5** If transcription is enabled, the transcript file appears after the recording finishes.
- [ ] **4.V6** If live captions are enabled, captions appear during a recorded call.

If these checks fail, go to [A.5 Recording, transcription, or captions are failing](#a5-recording-transcription-or-captions-are-failing).

---

## Phase 5: Pilot rollout

### 5.1 Overview

Now that the technical configuration is validated, run a small pilot with real users before broad rollout.

The goal of the pilot is to answer three questions:

1. Does Calls work reliably for real users?
2. Does it work across the clients and locations your organization uses?
3. Do your servers and network stay healthy under normal usage?

### 5.2 Prerequisites

- [ ] Phase 2 passed
- [ ] Phase 3 passed if using RTCD
- [ ] Phase 4 passed if using calls-offloader
- [ ] You have 5 to 10 pilot users from different locations and client types
- [ ] Pilot users have current Mattermost desktop or mobile apps

### 5.3 Prepare the pilot channel and message

Create a pilot channel such as `calls-pilot`, enable Calls in that channel, and post the following message.

If test mode is still enabled, have a **system admin** start each pilot call.

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

### 5.4 What to watch during the pilot

Use your monitoring and logs to watch the following:

- **Active sessions and participants**: The Calls metrics guide exposes session and participant data so you can confirm calls are being counted.
- **RTC errors**: Watch `rtcd_rtc_errors_total` or the equivalent Calls plugin metrics if you are using integrated mode.
- **CPU and memory**: Use RTCD process metrics such as `rtcd_process_cpu_seconds_total` and `rtcd_process_resident_memory_bytes`, or the equivalent plugin metrics in integrated mode.
- **Service logs**: Watch Mattermost, RTCD, and calls-offloader for recurring `ERROR` or `WARN` lines during pilot sessions.

If you do not have Prometheus and Grafana set up yet, monitor Mattermost, RTCD, and calls-offloader logs during the pilot instead.

### 5.5 Verification gate

- [ ] **5.V1** Two users complete a 1:1 audio call successfully.
- [ ] **5.V2** At least one group call with 3 or more users completes successfully.
- [ ] **5.V3** At least one pilot call lasts 15 minutes or longer without unexpected drops.
- [ ] **5.V4** Screen sharing works from a desktop app or browser.
- [ ] **5.V5** At least one user joins from outside the main office network, if that matches your deployment.
- [ ] **5.V6** At least one user joins on mobile.
- [ ] **5.V7** If recording is enabled, recording works during the pilot.
- [ ] **5.V8** If transcription is enabled, transcription works during the pilot.
- [ ] **5.V9** If live captions are enabled, captions work during the pilot.
- [ ] **5.V10** The admin has saved at least one `/call stats` sample from a successful pilot call.

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
