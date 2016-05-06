Running Mattermost
-----------------------------

To run Mattermost in development mode locally after setting up your local machine, type: `make run`

To stop Mattermost, type: `make stop`

To restart Mattermost after server code changes, type: `make restart-server`

Client code changes are automatically recompiled on saving.

To clean the database:
  - `make stop`
  - `make clean-docker`
  - `make run`
  
To run a test SMTP server: `sudo python -m smtpd -n -c DebuggingServer localhost:25`
