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

## Mattermost Is Not Working / The Server Keeps Dying

Questions to ask when dealing with general complaints along the lines of "Mattermost is not working"
or "the server keeps dying". See the previous section if you have not yet established from the
information provided by the customer that the server is the likely issue.

#### Check the status of the server process

Assuming the customer has followed our Linux setup guide, there will be a systemd service called
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

Many people miss the step in the setup guide that enables the systemd unit file for Mattermost.
Rectify this with the following commands, and ask the customer to reboot to verify it is working.

```
sudo systemctl enable mattermost.service
sudo systemctl start mattermost.service
```

#### Check the Mattermost logs

Ask the customer to share the contents of `mattermost.log` from the `logs` directory of their
Mattermost installation in order to look for any indications why Mattermost has stopped running.

#### Check the system logs

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


## LDAP Issues

#### Attach your LDAP settings from config.json.
The username/password should be removed.

#### What AD/LDAP server and version are you using?
E.g.: Active Directory on Windows Server 2016.

#### Are there any LDAP errors in the logs?

#### Is there a limit on the number of users the LDAP server can return in a single query? If so, have you set the Maximum Page Size in Mattermost?
Many LDAP servers have an upper limit on the number of users returned, so they might be hitting that limit. An error will appear in the logs usually informing of this case, but it's good to try anyway. 

#### Can you send an example user from your system? 
ldapsearch command format is preferred.

#### Is the server properly licensed?
Check the licensing page in the system console.

## TLS/SSL Issues

#### Are you using a proxy or the built in TLS support?

#### Are there any errors in the Mattermost logs?

#### Send us your config.json. For example:
```
grep "TLS" /opt/mattermost/config/config.json 
        "TLSCertFile": "",
        "TLSKeyFile": "",
        "TLSMinVer": "1.2",
        "TLSStrictTransport": false,
        "TLSStrictTransportMaxAge": 63072000,
        "TLSOverwriteCiphers": [],
        "ConnectionSecurity": "STARTTLS",
```

#### Send your proxy configuration if you are using one.

#### Have you followed one of the setup guides?

#### Check the status of the SSL certificate being used on Mattermost. For example:
```
echo | openssl s_client -showcerts -connect <URL>:443 -CApath /etc/ssl/ && echo | openssl s_client -connect <URL>:443 2>/dev/null | openssl x509 -noout -dates -text
```

## GitLab Issues

#### General Questions

1. Have they set up Mattermost on its own, or are they using GitLab Omnibus?
2. If using GitLab Omnibus, what version of it do they have?
3. If using GitLab Omnibus, Can they send us the Mattermost section of their gitlab.rb (found in `/etc/gitlab/gitlab.rb`) and their config.json (found in `/var/opt/gitlab/mattermost/config.json`)?

#### Connection issues

1. If they try to access Mattermost and receive a "took too long to respond" error page, they should check to confirm that their `mattermost_external_url` is set correctly in their gitlab.rb. Then, they should run `gitlab-ctl reconfigure`.
2. If they try to access Mattermost and receive a 502 error, their `mattermost_external_url` is set correctly, but their Mattermost instance does not appear to be running. They should then:
    1. Run `gitlab-ctl status mattermost` to see if Mattermost is running.
    2. Check the logs to see if something is preventing Mattermost from starting. They can do this by running `gitlab-ctl tail mattermost` and using `gitlab-ctl restart mattermost` to attempt to start Mattermost.

#### Login issues

1. Are they seeing any error messages when they try to log in? If so, what error messages are they seeing, and can they send us a screenshot?
2. Does anything appear in the Mattermost logs when they try to log in? They can see these by running `gitlab-ctl tail mattermost`.

#### Other debugging information

Useful commands:
- `sudo gitlab-ctl reconfigure` - Update `config.json` and other configuration files, then restart all services (including Mattermost).
- `sudo gitlab-ctl <stop/start/restart> mattermost` - Stop/start/restart Mattermost.
- `sudo gitlab-ctl status mattermost` - Check if Mattermost is running. The printed output will start with `run` if it's running or `down` if it's not.
- `sudo gitlab-ctl tail mattermost` - Watch all Mattermost log files. Press CTRL+C to exit.
- `sudo gitlab-ctl <stop/start/restart/status/tail> <nginx/postgresql/redis/etc>` - Control, view status, or view logs of a different service.
- `sudo less /var/opt/gitlab/mattermost/config.json` - View the Mattermost `config.json` directly (use the arrow keys to scroll, press Q to exit).
- `sudo gitlab-psql -d mattermost_production` - Access the embedded Mattermost database.
- `sudo gitlab-rails console production` - Access the GitLab admin console (press CTRL+D to exit).
   - You can then carry out commands such as updating a user’s password:

     ```
     user = User.find_by(email: 'admin@local.host')
     user.password = 'secret_pass'
     user.password_confirmation = 'secret_pass'
     user.save!
     ```

File locations:
- Configuration files are located at `/etc/gitlab/gitlab.rb` and `/var/opt/gitlab/mattermost/config.json`.
- Log files are located in `/var/log/gitlab`. Mattermost's current logs in particular are in `/var/log/gitlab/mattermost`. The current log is named `current` with older ones being named `mattermost.log` or `mattermost.logmattermost.log`.
- The default data directory is `/var/opt/gitlab/mattermost/data`.
- Other Mattermost resources (i18n, email templates, webapp code, etc) are located in `/opt/gitlab/embedded/service/mattermost`.
