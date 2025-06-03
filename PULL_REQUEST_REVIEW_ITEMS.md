# Mattermost Calls Documentation TODOs

This file contains a list of documentation improvements identified for the Mattermost Calls feature.

## Completed Items

- ✅ Update `calls-rtcd-setup.rst` with new version endpoint information
- ✅ Update `calls-troubleshooting.rst` ICE configuration section with correct parameter name
- ✅ Add client and RTCD log examples to ICE configuration issues
- ✅ Remove 'Why Use RTCD' section from calls-rtcd-setup.rst

## High Priority Items

- Re-order RTCD setup recommendations to prioritize "Bare Metal/VM", then "Docker", then "Kubernetes".  I'll share my example systemd unit file and configuration.
- Create documentation for the calls-offloader service used for Calls Recording and Transcription
- Expand CORS documentation or document that `AllowCORSFrom` needs to be set to the SiteURL
- Add call-out/special note that the Calls metrics scraping has issues with `labels` setup in `prometheus.yml` and that the Calls dashboard expects <host>:<port> format, with an example.
- Document a common flow for each piece of the setup: Calls plugin curl/test/telemetry, RTCD curl/test/telemetry, calls-offloader curl/test/telemetry
- Document troubleshooting steps for the error "failed to create recording job: max concurrent jobs reached". 

## Medium Priority Items

- Document the command `curl http://localhost:9090/api/v1/label/__name__/values | jq '.' | grep rtcd` as a troubleshooting tool in `calls-metrics-monitoring.rst`
- Document that Node Exporter service needs to be bound to the right address
- Document how to check Prometheus Scrape targets using the 'Targets' menu option for status
- Document this command for debugging calls-offloader: `docker ps --format "{{.ID}} {{.Image}}" | grep "calls" | awk '{print $1}' | xargs -I {} docker logs -f {}`
- Document the command `docker ps -a --filter "status=exited"` to view completed calls-offloader job containers
- Improve formatting for Network Requirements table to avoid small side-scrolling view
- Document experimental screen sharing audio feature with limitations and how to enable with `/call experimental on` slash command
- Provide documentation on what settings changes require what service/plugin restarts
