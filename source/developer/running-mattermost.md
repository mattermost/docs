Running Mattermost
-----------------------------

To run changes to server-side code:

```
	make stop
	make test
	make run
```

To run changes to client-side code:

```
	make run
```
Client side code will reload automatically upon saving

To clean the database:

```
	make stop
	make clean-docker
```

To clean the database, logs, and workspace:

```
	make stop
	make clean
```

To remove everything

```
	make stop
	make nuke
```

To check styles of Go and JavaScript:

```
	make check-style
```

To run a test SMTP server:

```
	sudo python -m smtpd -n -c DebuggingServer localhost:25
```

Also you can use the docker image called [inbucket](https://github.com/jhillyerd/inbucket) to test the emails. To access the web interface, open your browser and go to:

```
  http://localhost:9000 or your docker host ip
```

To send emails using the `SMTP` the port is `2500` no user and passwords are required
