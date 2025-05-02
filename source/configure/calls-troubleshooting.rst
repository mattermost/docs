Troubleshooting Mattermost Calls
===========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This guide provides comprehensive troubleshooting steps for Mattermost Calls, particularly focusing on the dedicated RTCD deployment model. Follow these steps to identify and resolve common issues.

- `Common issues <#common-issues>`__
- `Connectivity troubleshooting <#connectivity-troubleshooting>`__
- `Log analysis <#log-analysis>`__
- `Performance issues <#performance-issues>`__
- `Debugging tools <#debugging-tools>`__
- `Advanced diagnostics <#advanced-diagnostics>`__

Common Issues
-----------

Calls Not Connecting
^^^^^^^^^^^^^^^^^^^^

**Symptoms**: Users can start calls but cannot connect, or calls connect but drop quickly.

**Possible causes and solutions**:

1. **Network connectivity issues**:
   - Verify that UDP port 8443 (or your configured port) is open between clients and RTCD servers
   - Ensure TCP port 8045 is open between Mattermost and RTCD servers
   - Check that any load balancers are properly configured for UDP traffic

2. **ICE configuration issues**:
   - Verify the ``ice.hostOverride`` setting in RTCD configuration matches the publicly accessible hostname or IP
   - Ensure STUN/TURN servers are properly configured if needed

3. **API connectivity**:
   - Verify that Mattermost servers can reach the RTCD API endpoint
   - Check that the API key is correctly configured in both Mattermost and RTCD

4. **Plugin configuration**:
   - Ensure the Calls plugin is enabled and properly configured
   - Verify the RTCD service URL is correct in the System Console

Audio Issues
^^^^^^^^^^^

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

Call Quality Issues
^^^^^^^^^^^^^^^^^

**Symptoms**: Calls connect but quality is poor, with latency, echo, or distortion.

**Possible causes and solutions**:

1. **Server resources**:
   - Check CPU usage on RTCD servers - high CPU can cause quality issues
   - Refer to the `Performance Monitoring setup guide <../performance-monitoring/setup-guide.rst>`__ for detailed instructions on monitoring and optimizing performance
   - Monitor network bandwidth usage

2. **Network congestion**:
   - Check for packet loss between clients and RTCD
   - Consider network QoS settings to prioritize real-time traffic

3. **Client-side issues**:
   - Browser or app limitations
   - Hardware limitations (CPU, memory)
   - Network congestion at the user's location

Connectivity Troubleshooting
--------------------------

Basic Connectivity Tests
^^^^^^^^^^^^^^^^^^^^^^

1. **HTTP API connectivity test**:

   Test if the RTCD API is reachable:

   .. code-block:: bash

      curl http://YOUR_RTCD_SERVER:8045/api/v1/health
      # Expected response: {"status":"ok"}

2. **UDP connectivity test**:

   On the RTCD server:
   
   .. code-block:: bash

      nc -l -u -p 8443

   On a client machine:
   
   .. code-block:: bash

      nc -v -u YOUR_RTCD_SERVER 8443
      
   Type a message and press Enter. If you see the message on both sides, UDP connectivity is working.

3. **TCP fallback connectivity test**:

   Same as the UDP test, but without the ``-u`` flag:
   
   On the RTCD server:
   
   .. code-block:: bash

      nc -l -p 8443

   On a client machine:
   
   .. code-block:: bash

      nc -v YOUR_RTCD_SERVER 8443

Network Packet Analysis
^^^^^^^^^^^^^^^^^^^^^

To capture and analyze network traffic:

1. **Capture UDP traffic on the RTCD server**:

   .. code-block:: bash

      sudo tcpdump -n 'udp port 8443' -i any

2. **Capture TCP API traffic**:

   .. code-block:: bash

      sudo tcpdump -n 'tcp port 8045' -i any

3. **Analyze traffic patterns**:
   
   - Verify packets are flowing both ways
   - Look for ICMP errors that might indicate firewall issues
   - Check for patterns of packet loss

4. **Use Wireshark for deeper analysis**:
   
   For more detailed packet inspection, capture traffic with tcpdump and analyze with Wireshark:
   
   .. code-block:: bash

      sudo tcpdump -n -w calls_traffic.pcap 'port 8443'
      
   Then analyze the ``calls_traffic.pcap`` file with Wireshark.

Firewall Configuration Checks
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Check iptables rules** (Linux):

   .. code-block:: bash

      sudo iptables -L -n
      
   Ensure there are no rules blocking UDP port 8443 or TCP ports 8045/8443.

2. **Check cloud provider security groups**:
   
   Verify that security groups or network ACLs allow:
   - Inbound UDP on port 8443 from client networks
   - Inbound TCP on port 8045 from Mattermost server networks
   - Inbound TCP on port 8443 (if TCP fallback is enabled)

3. **Check intermediate firewalls**:
   
   - Corporate firewalls might block UDP traffic
   - Some networks might require TURN servers for traversal

Log Analysis
----------

RTCD Logs
^^^^^^^^

The RTCD service logs important events and errors. Set the log level to "debug" for troubleshooting:

1. **In the configuration file**:

   .. code-block:: json

      {
        "log": {
          "level": "debug",
          "json": true
        }
      }

2. **Common log patterns to look for**:

   - **Connection errors**: Look for "failed to connect" or "connection error" messages
   - **ICE negotiation failures**: Look for "ICE failed" or "ICE timeout" messages
   - **API authentication issues**: Look for "unauthorized" or "invalid API key" messages

Mattermost Logs
^^^^^^^^^^^^^

Check the Mattermost server logs for Calls plugin related issues:

1. **Enable debug logging** in System Console > Environment > Logging > File Log Level

2. **Filter for Calls-related logs**:

   .. code-block:: bash

      grep -i "calls" /path/to/mattermost.log
      
3. **Look for common patterns**:
   
   - Connection errors to RTCD
   - Plugin initialization issues
   - WebSocket connection problems

Browser Console Logs
^^^^^^^^^^^^^^^^^

Instruct users to check their browser console logs:

1. **In Chrome/Edge**:
   - Press F12 to open Developer Tools
   - Go to the Console tab
   - Look for errors related to WebRTC, Calls, or media permissions

2. **Specific patterns to look for**:
   
   - "getUserMedia" errors (microphone permission issues)
   - "ICE connection" failures
   - WebSocket connection errors

Performance Issues
---------------

Diagnosing High CPU Usage
^^^^^^^^^^^^^^^^^^^^^^^

If RTCD servers show high CPU usage:

1. **Check concurrent calls and participants**:
   
   - Access the Prometheus metrics endpoint to see active sessions
   - Compare with the benchmark data in the documentation

2. **Profile CPU usage** (Linux):

   .. code-block:: bash

      top -p $(pgrep rtcd)
      
   Or for detailed per-thread usage:
   
   .. code-block:: bash

      ps -eLo pid,ppid,tid,pcpu,comm | grep rtcd

3. **Enable pprof profiling** (if needed):

   Add to your RTCD configuration:
   
   .. code-block:: json

      {
        "debug": {
          "pprof": true,
          "pprofPort": 6060
        }
      }
      
   Then capture a CPU profile:
   
   .. code-block:: bash

      curl http://localhost:6060/debug/pprof/profile > cpu.profile
      
   Analyze with:
   
   .. code-block:: bash

      go tool pprof -http=:8080 cpu.profile

Diagnosing Network Bottlenecks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you suspect network bandwidth issues:

1. **Monitor network utilization**:

   .. code-block:: bash

      iftop -n
      
2. **Check for packet drops**:

   .. code-block:: bash

      netstat -su | grep -E 'drop|error'
      
3. **Verify system network buffers**:

   .. code-block:: bash

      sysctl -a | grep net.core.rmem
      sysctl -a | grep net.core.wmem
      
   Ensure these match the recommended values:
   
   .. code-block:: bash

      net.core.rmem_max = 16777216
      net.core.wmem_max = 16777216
      net.core.optmem_max = 16777216

Debugging Tools
------------

WebRTC Internals (Chrome)
^^^^^^^^^^^^^^^^^^^^^^^^

For in-depth WebRTC diagnostics in Chrome:

1. **Access chrome://webrtc-internals** in a new browser tab while on a call

2. **Examine the connection details**:
   
   - ICE connection state
   - Selected candidate pairs
   - DTLS/SRTP setup
   - Bandwidth estimation

3. **Look for specific issues**:
   
   - Candidate gathering delays
   - Failed ICE connections
   - Bandwidth limitations

Prometheus Metrics Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^

Use Prometheus metrics for real-time and historical performance data:

1. **Key metrics to monitor**:

   - ``rtcd_rtc_sessions_total``: Number of active RTC sessions
   - ``rtcd_rtc_conn_states_total``: Connection state transitions 
   - ``rtcd_rtc_errors_total``: Error counts
   - ``rtcd_rtc_rtp_tracks_total``: Media track count
   - ``rtcd_process_cpu_seconds_total``: CPU usage

2. **Set up Grafana dashboards**:
   
   Import the official [Mattermost Calls dashboard](https://github.com/mattermost/mattermost-performance-assets/blob/master/grafana/mattermost-calls-performance-monitoring.json) into Grafana for visualization.

Advanced Diagnostics
-----------------

WebRTC Diagnostic Commands
^^^^^^^^^^^^^^^^^^^^^^^^

For detailed WebRTC diagnostics:

1. **Test STUN server connectivity**:

   .. code-block:: bash

      # Using stun-client (you may need to install it)
      stun-client stun.global.calls.mattermost.com
      
   This should return your public IP address if STUN is working correctly.

2. **Verify TURN server**:

   .. code-block:: bash

      # Using turnutils_uclient (part of coturn)
      turnutils_uclient -v -s your-turn-server -u username -p password
      
   This tests if your TURN server is correctly configured.

3. **Test end-to-end latency**:

   Between client locations and RTCD server:
   
   .. code-block:: bash

      ping -c 10 your-rtcd-server
      
   Look for consistent, low latency (<100ms ideally for voice calls).

Client-Side Testing Tools
^^^^^^^^^^^^^^^^^^^^^^^

Tools to help diagnose client-side issues:

1. **WebRTC Troubleshooter**:
   
   Direct users to [WebRTC Troubleshooter](https://test.webrtc.org/) for browser capability testing.

2. **Network Quality Tests**:
   
   Use [Speedtest](https://www.speedtest.net/) or similar to check internet connection quality.

3. **Browser-Specific WebRTC Info**:
   
   - Chrome: chrome://webrtc-internals
   - Firefox: about:webrtc

When to Contact Support
^^^^^^^^^^^^^^^^^^^^

Consider contacting Mattermost Support when:

1. You've tried basic troubleshooting steps without resolution
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