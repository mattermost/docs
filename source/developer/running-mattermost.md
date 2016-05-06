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

### Make Commands ###

Here is a complete listing of all `make` commands:

- `start-docker`: Starts docker daemons
- `stop-docker`: Stops docker daemons
- `clean-docker`: Removes docker daemons
- `check-style`: Runs `gofmt`
- `test`: Runs server tests
- `setup-run-client-tests`: Sets up client tests
- `cleanup-run-client-tests`: Cleans up client tests
- `test-client` Runs client tests
- `.prebuild` Preparation for running go code
- `prepare-enterprise` Preparation for enterprise build
- `build-linux` Builds enterprise for Linux
- `build-osx` Builds enterprise for Mac OSX
- `build-windows` Builds enterprise for Windows
- `build` Builds all enterprise versions
- `package` Packages Mattermost
- `run-server` Runs server
- `run-client` Runs client
- `run-client-fullmap` Runs client with full source map
- `run` Runs server and client
- `run-fullmap` Runs server and full source map client
- `stop-server` Stops server
- `stop-client` Stops client
- `stop` Stops server and client
- `restart-server` Stops and starts server
- `restart-client` Stops and starts client
- `clean` Cleans docker, data, logs, and workspace
- `nuke` Cleans all data
- `setup-mac` Sets up mac
