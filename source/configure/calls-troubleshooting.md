# Troubleshooting Mattermost Calls

```{include} ../_static/badges/allplans-cloud-selfhosted.md
```

This guide provides comprehensive troubleshooting steps for Mattermost Calls, particularly focusing on the dedicated RTCD deployment model. Follow these steps to identify and resolve common issues.

- [Common issues](#common-issues)
- [Connectivity troubleshooting](#connectivity-troubleshooting)
- [Log analysis](#log-analysis)
- [Performance issues](#performance-issues)

## Common Issues

### Calls Not Connecting

**Symptoms**: Users can start calls but cannot connect, or calls connect but drop quickly.

**Possible causes and solutions**:

1. **Network connectivity issues**:
   - Verify that UDP port 8443 (or your configured port) is open between clients and RTCD servers
   - Ensure TCP port 8045 is open between Mattermost and RTCD servers
   - Check that any load balancers are properly configured for UDP traffic

2. **ICE configuration issues**:
   - Verify the `rtc.ice_host_override` setting in RTCD configuration matches the publicly accessible hostname or IP of the RTCD server
   - If this setting is incorrect, client browser console may show errors like: `com.mattermost.calls: peer error timed out waiting for rtc connection`
   - Meanwhile, RTCD `trace` level logs might show internal IP addresses in ICE connection logs:
     
     ```json
     {"timestamp":"2025-05-14 10:29:08.935 Z","level":"trace","msg":"Ping STUN from udp4 host 172.31.29.117:8443 (resolved: 172.31.29.117:8443) to udp4 host 192.168.64.1:59737 (resolved: 192.168.64.1:59737)","caller":"rtc/logger.go:54","origin":"ice/v4.(*Agent).sendBindingRequest github.com/pion/ice/v4@v4.0.3/agent.go:921"}
     ```

3. **API connectivity**:
   - Verify that Mattermost servers can reach the RTCD API endpoint
   - Check that the API key is correctly configured in both Mattermost and RTCD

4. **Plugin configuration**:
   - Ensure the Calls plugin is enabled and properly configured
   - Verify the RTCD service URL is correct in the System Console

### Audio Issues

**Symptoms**: Users can connect to calls, but audio is one-way, choppy, or not working.

**Possible causes and solutions**:

1. **Client permissions**:
   - Ensure browser/app has microphone permissions
   - Check if users are using multiple audio devices that might interfere

2. **Network quality**:
   - High latency or packet loss can cause audio issues
   - Try testing with TCP fallback enabled (requires RTCD v0.11+ and Calls v0.17+)

3. **Audio device configuration**:
   - Users should verify their audio input/output settings
   - Try different browsers or the desktop app

### Call Quality Issues

**Symptoms**: Calls connect but quality is poor, with latency, echo, or distortion.

**Possible causes and solutions**:

1. **Server resources**:
   - Check CPU usage on RTCD servers - high CPU can cause quality issues
   - Refer to the [Calls Metrics and Monitoring](calls-metrics-monitoring.md) guide for detailed instructions on monitoring and optimizing performance
   - Monitor network bandwidth usage

2. **Network congestion**:
   - Check for packet loss between clients and RTCD
   - Consider network QoS settings to prioritize real-time traffic

3. **Client-side issues**:
   - Browser or app limitations
   - Hardware limitations (CPU, memory)
   - Network congestion at the user's location

## Connectivity Troubleshooting

### Basic Connectivity Tests

1. **HTTP API connectivity test**:

   Test if the RTCD API is reachable:

   ```bash
   curl http://YOUR_RTCD_SERVER:8045/version
   # Example response: {"buildDate":"2025-04-02 21:33","buildVersion":"v1.1.0","buildHash":"7bc1f7a","goVersion":"go1.23.6","goOS":"linux","goArch":"amd64"}   ```

2. **UDP connectivity test**:

   On the RTCD server:
   
   ```bash
   nc -l -u -p 8443
   ```

   On a client machine:
   
   ```bash
   nc -v -u YOUR_RTCD_SERVER 8443
   ```
      
   Type a message and press Enter. If you see the message on both sides, UDP connectivity is working.

3. **TCP fallback connectivity test**:

   Same as the UDP test, but without the `-u` flag:
   
   On the RTCD server:
   
   ```bash
   nc -l -p 8443
   ```

   On a client machine:
   
   ```bash
   nc -v YOUR_RTCD_SERVER 8443
   ```

### Network Packet Analysis

To capture and analyze network traffic:

1. **Capture UDP traffic on the RTCD server**:

   ```bash
   sudo tcpdump -n 'udp port 8443' -i any
   ```

2. **Capture TCP API traffic**:

   ```bash
   sudo tcpdump -n 'tcp port 8045' -i any
   ```

3. **Analyze traffic patterns**:
   
   - Verify packets are flowing both ways
   - Look for ICMP errors that might indicate firewall issues
   - Check for patterns of packet loss

4. **Use Wireshark for deeper analysis**:
   
   For more detailed packet inspection, capture traffic with tcpdump and analyze with Wireshark:
   
   ```bash
   sudo tcpdump -n -w calls_traffic.pcap 'port 8443'
   ```
      
   Then analyze the `calls_traffic.pcap` file with Wireshark.

### Firewall Configuration Checks

1. **Check iptables rules** (Linux):

   ```bash
   sudo iptables -L -n
   ```
      
   Ensure there are no rules blocking UDP port 8443 or TCP ports 8045/8443.

2. **Check cloud provider security groups**:
   
   Verify that security groups or network ACLs allow:
   - Inbound UDP on port 8443 from client networks
   - Inbound TCP on port 8045 from Mattermost server networks
   - Inbound TCP on port 8443 (if TCP fallback is enabled)

3. **Check intermediate firewalls**:
   
   - Corporate firewalls might block UDP traffic
   - Some networks might require TURN servers for traversal

## Log Analysis

### RTCD Logs

The RTCD service logs important events and errors. Set the log level to "debug" for troubleshooting:

1. **In the configuration file**:

   ```toml
   [logger]
   enable_file = true
   file_level = "DEBUG"
   ```

   Restart the RTCD service after making these changes

2. **Common log patterns to look for**:

   - **Connection errors**: Look for "failed to connect" or "connection error" messages
   - **ICE negotiation failures**: Look for "ICE failed" or "ICE timeout" messages
   - **API authentication issues**: Look for "unauthorized" or "invalid API key" messages

### Mattermost Logs

Check the Mattermost server logs for Calls plugin related issues:

1. **Enable debug logging** in System Console > Environment > Logging > File Log Level

2. **Filter for Calls-related logs**:

   ```bash
   grep -i "calls" /path/to/mattermost.log
   ```
      
3. **Look for common patterns**:
   
   - Connection errors to RTCD
   - Plugin initialization issues
   - WebSocket connection problems

### Browser Console Logs

Instruct users to check their browser console logs:

1. **In Chrome/Edge**:
   - Press F12 to open Developer Tools
   - Go to the Console tab
   - Look for errors related to WebRTC, Calls, or media permissions

2. **Specific patterns to look for**:
   
   - "getUserMedia" errors (microphone permission issues)
   - "ICE connection" failures
   - WebSocket connection errors

## Performance Issues

### Diagnosing High CPU Usage

If RTCD servers show high CPU usage:

1. **Check concurrent calls and participants**:
   
   - Access the Prometheus metrics endpoint to see active sessions
   - Compare with the benchmark data in the {doc}`Calls Metrics and Monitoring <calls-metrics-monitoring>` documentation's Performance Baselines section

2. **Profile CPU usage** (Linux):

   ```bash
   top -p $(pgrep rtcd)
   ```
      
   Or for detailed per-thread usage:
   
   ```bash
   ps -eLo pid,ppid,tid,pcpu,comm | grep rtcd
   ```

3. **Enable pprof profiling** (if needed):

   Add to your RTCD configuration:
   
   ```json
   {
     "debug": {
       "pprof": true,
       "pprofPort": 6060
     }
   }
   ```
      
   Then capture a CPU profile:
   
   ```bash
   curl http://localhost:6060/debug/pprof/profile > cpu.profile
   ```
      
   Analyze with:
   
   ```bash
   go tool pprof -http=:8080 cpu.profile
   ```

### Diagnosing Network Bottlenecks

If you suspect network bandwidth issues:

1. **Monitor network utilization**:

   ```bash
   iftop -n
   ```
      
2. **Check for packet drops**:

   ```bash
   netstat -su | grep -E 'drop|error'
   ```
      
3. **Verify system network buffers**:

   ```bash
   sysctl -a | grep net.core.rmem
   sysctl -a | grep net.core.wmem
   ```
      
   Ensure these match the recommended values:
   
   ```bash
   net.core.rmem_max = 16777216
   net.core.wmem_max = 16777216
   net.core.optmem_max = 16777216
   ```

## Recording and Transcription Issues

For troubleshooting calls-offloader service issues including recording and transcription problems, see the [Calls Offloader Setup and Configuration](calls-offloader-setup.md#troubleshooting) guide.

### Calls-Offloader Docker Debugging

If you're running calls-offloader in Docker, use these commands for debugging:

#### Monitor Live Logs

To view real-time logs from calls-offloader containers:

```bash
# Find and follow logs from all calls-related containers
docker ps --format "{{.ID}} {{.Image}}" | grep "calls" | awk '{print $1}' | xargs -I {} docker logs -f {}
```

This command finds all running containers with "calls" in the image name and follows their logs.

#### View Completed Jobs

To view completed calls-offloader job containers (useful for debugging failed jobs):

```bash
# List all exited containers to see completed jobs
docker ps -a --filter "status=exited"
```

Look for containers with calls-offloader image names that have exited. You can then examine their logs:

```bash
# View logs from a specific completed container
docker logs <container_id>
```

#### Additional Docker Debugging Tips

- **Check container resource usage**: `docker stats` to see if containers are hitting resource limits
- **Inspect container configuration**: `docker inspect <container_id>` for detailed container settings
- **Check container health**: `docker inspect <container_id> | grep Health` if health checks are configured

## Prometheus Metrics Analysis

Use Prometheus metrics for real-time and historical performance data:

For detailed setup instructions on configuring Prometheus and Grafana for Calls monitoring, see the {doc}`Calls Metrics and Monitoring <calls-metrics-monitoring>` guide.

## When to Contact Support

Consider contacting Mattermost Support when:

1. You've tried troubleshooting steps without resolution
2. You're experiencing persistent connection failures across multiple clients
3. You notice unexpected or degraded performance despite proper configuration
4. You need help interpreting diagnostic information
5. You suspect a bug in the Calls plugin or RTCD service

When contacting support, please include:

- RTCD version and configuration (with sensitive information redacted)
- Mattermost server version
- Calls plugin version
- Client environments (browsers, OS versions)
- Relevant logs and diagnostic information
- Detailed description of the issue and steps to reproduce

## Other Calls Documentation

- [Calls Overview](calls-deployment.md): Overview of deployment options and architecture
- [RTCD Setup and Configuration](calls-rtcd-setup.md): Comprehensive guide for setting up the dedicated RTCD service
- [Calls Offloader Setup and Configuration](calls-offloader-setup.md): Setup guide for call recording and transcription
- [Calls Metrics and Monitoring](calls-metrics-monitoring.md): Guide to monitoring Calls performance using metrics and observability
- [Calls Deployment on Kubernetes](calls-kubernetes.md): Detailed guide for deploying Calls in Kubernetes environments