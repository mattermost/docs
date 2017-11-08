# Support Handbook

## General Questions For Any Issues

Questions to ask when providing support for any of the following issues.

#### What OS and version is the Mattermost server installed?
E.g.: Ubuntu 16.04, RHEL 7.1

#### What is your Mattermost server version?
E.g.: 4.2, 4.3

#### Are you experiencing the issues with the browser webapp, if so which one?
E.g.: Chrome, Firefox, Edge

#### Are you experiencing the issues with the Mattermost Desktop App, if so what version and OS?
E.g.: App version 3.6 on Mac, App version 3.7.1 on Windows

#### Are you experiencing the issues with the Mattermost Mobile App, if so what version and OS?
E.g.: App version 1.2 on iOS, App version 1.3 on Android

#### Can you send a snippet of the Mattermost server logs around the time of the incident?  
Typically located in `/opt/mattermost/logs`.

#### Are you running Mattermost in a container and/or using container orchestration?
E.g.: Docker and Kubernetes, Docker and Cloud Foundry


## Mattermost Is not Working / The Server Keeps Dying

Questions to ask when dealing with general complaints along the lines of "Mattermost is not working"
or "the server keeps dying". See the previous section if you have not yet established from the
information provided by the customer that the server is the likely issue.

#### Check the status of the server process

Assuming the customer has followed our Linux setup guide, there will be a system service called
`mattermost.service` on their server. You can check the status of this process with:

```
sudo systemctl status mattermost.service
```

If the service is not running, and the status is not `failed`, instruct them to run:

```
sudo systemctl enable mattermost.service
sudo systemctl start mattermost.service
```

#### Mattermost is not running after a reboot

Many people miss the step in the setup guide that enables the system unit file for Mattermost.
Rectify this with the following commands, and ask the customer to reboot to verify it is working.

```
sudo systemctl enable mattermost.service
sudo systemctl start mattermost.service
```

#### Check the Mattermost logs

Ask the customer to share the contents of `mattermost.log` from the `logs` directory of their
Mattermost installation in order to look for any indications why Mattermost has stopped running.

#### Check the System logs

Often, the reason for Mattermost being reported as "randomly dying" is running out of memory. Ask
the customer to send the results of the following command to inspect for evidence of OOM.

```
sudo journalctl -u mattermost.service
```

If the OOM killer is the problem, suggest they use a machine with more RAM. If they already have
plenty of RAM for the load they are experiencing, this may indicate a bug in the Mattermost server.


## Database Issues

Questions to ask when providing support for database issues.

__IMPORTANT: Before asking for any database queries to be run, suggest a back-up is completed to prevent accidental data loss or corruption.__

#### PostgreSQL or MySQL?
Find out which database they are using. We only support PostgreSQL and MySQL currently.

If they're using Amazon Aurora MySQL, and their issue seems like a race condition, it might be due to the multi-region lag that Aurora can have. If this is the case there may be a race in code we need to fix. @christopher will know more.

#### What is the database version?
Make sure it's a [version we support](https://docs.mattermost.com/install/requirements.html#database-software). If we don't support it, ask them to use a version we do support.

#### Read replicas?
Check if they have any read replicas set up. If these are misconfigured, it could be the source of some issues, such as rows not being propagated to the replicas and looking like missing/old data to a user.

If the read replicas are not being used, make sure they have an enterprise license uploaded.

#### Connection errors?
If their Mattermost server is unable to connect to the database, make sure the connection string being used is correct. It could also be a networking issue where the database isn't on the same network or the right ports are not open.

#### Other
If they are receiving a specific error from the database, try using that to troubleshoot the issue.

## WebSocket Issues

#### Can you send us the following Mattermost server configuration settings?
`ServiceSettings.SiteURL`, `ServiceSettings.ListenAddress`, `ServiceSettings.AllowCorsFrom`, `ServiceSettings.WebsocketSecurePort`, `ServiceSettings.WebsocketPort` Typically found in `/opt/mattermost/config/config.json`

#### Can you send us your Nginx configuration files?
Typically found in `/etc/nginx/nginx.conf` and `/etc/nginx/sites-available/mattermost`

#### Can you send us a snippet of your Nginx error logs around the time of the incident?
Typically found in `/var/log/nginx/error.log`


