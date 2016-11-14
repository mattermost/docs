Developer Machine Setup
-----------------------------

If you run into any issues getting your environment set up, please check the Troubleshooting section at the bottom for common solutions.

### Mac OS X ###

1. Install [Docker for Mac](https://docs.docker.com/docker-for-mac/)
2. Add the following line to `/etc/hosts` 
  - `127.0.0.1 dockerhost`
3. [Download Go 1.6](http://golang.org/dl/) (Go 1.5 and earlier is not supported) and Node.js using Homebrew.
	1. Download Homebrew from [http://brew.sh/](http://brew.sh/)
	2. `brew install go`
	3. `brew install node`
4. Set up your Go workspace
	1. `mkdir ~/go`
	2. Add the following to your `~/.bash_profile`  
		- `export GOPATH=$HOME/go`  
		- `export PATH=$PATH:$GOPATH/bin`  
		- `ulimit -n 8096`  
		- If you don't increase the file handle limit you may see some weird build issues with browserify or npm.  
	3. Reload your bash profile  
		`source ~/.bash_profile`
	4. Set GOROOT (optional) in your `~/.bash_profile`
		- `export GOROOT=/usr/local/go/`
5. Fork Mattermost on GitHub.com from [https://github.com/mattermost/platform](https://github.com/mattermost/platform), then:
	1. `cd ~/go`  
	2. `mkdir -p src/github.com/mattermost`  
	3. `cd src/github.com/mattermost`  
	4. `git clone https://github.com/<username>/platform.git`  
	5. `cd platform`
6. Run `make run` to start Mattermost
7. Browse to `http://localhost:8065` to create an account. The first account created has System Administrator privileges.
8. You can stop Mattermost using `make stop`
9. If you want to setup for cross compilation (required for the `make package` and dependant targets) run:
    - Note: You can skip the platform you are on because you have that target installed by default.
    - `env GOOS=windows GOARCH=amd64 go install std`
    - `env GOOS=darwin GOARCH=amd64 go install std`
    - `env GOOS=linux GOARCH=amd64 go install std`

Any issues? Please let us know on our forums at: https://forum.mattermost.org/

### Ubuntu ###

1. Download Docker, follow the instructions at [https://docs.docker.com/engine/installation/linux/ubuntulinux/](https://docs.docker.com/engine/installation/linux/ubuntulinux/)
2. Set up your dockerhost address
	1. Edit your `/etc/hosts` file to include the following line  
		- `127.0.0.1 dockerhost`
3. Install build essentials
	1. `apt-get install build-essential`
4.  [Download Go 1.6](http://golang.org/dl/) (Go 1.5 and earlier is not supported).
5. Set up your Go workspace and add Go to the PATH
	1. `mkdir ~/go`
	2. Add the following to your `~/.bashrc`
		- `export GOPATH=$HOME/go`  
		- `export PATH=$PATH:$GOPATH/bin`  
		- `ulimit -n 8096`  
		- If you don't increase the file handle limit you may see some weird build issues with browserify or npm.  
	3. Reload your bashrc  
		- `source ~/.bashrc`
	4. Set GOROOT (optional) in your `~/.bash_profile`
		- `export GOROOT=/usr/local/go/`
6. Install Node.js  
	- `curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -`  
	- `sudo apt-get install -y nodejs`
7. Fork Mattermost on GitHub.com from [https://github.com/mattermost/platform](https://github.com/mattermost/platform), then:
	1. `cd ~/go`  
	2. `mkdir -p src/github.com/mattermost`  
	3. `cd src/github.com/mattermost`  
	4. `git clone https://github.com/<username>/platform.git`  
	5. `cd platform`
8. Run `make run` to start Mattermost
9. Browse to `http://localhost:8065` to create an account. The first account created has System Administrator privileges.
10. You can stop Mattermost using `make stop`
11. If you want to setup for cross compilation (required for the `make package` and dependant targets) run:
    - Note: You can skip the platform you are on because you have that target installed by default.
    - `env GOOS=windows GOARCH=amd64 go install std`
    - `env GOOS=darwin GOARCH=amd64 go install std`
    - `env GOOS=linux GOARCH=amd64 go install std`

Any issues? Please let us know on our forums at: http://forum.mattermost.org

### Archlinux ###

1. Install Docker
	1. `pacman -S docker`
	2. `gpasswd -a user docker`
	3. `systemctl enable docker.service`
	4. `systemctl start docker.service`
	5. `newgrp docker`
2. Set up your dockerhost address
	1. Edit your /etc/hosts file to include the following line
		`127.0.0.1 dockerhost`
3. Install Go
	1. `pacman -S go`
4. Set up your Go workspace and add Go to the PATH
	1. `mkdir ~/go`
	2. Add the following to your ~/.bashrc
		- `export GOPATH=$HOME/go`
		- `export GOROOT=/usr/lib/go`
		- `export PATH=$PATH:$GOROOT/bin`
	3. Reload your bashrc
		- `source ~/.bashrc`
	4. Set GOROOT (optional) in your `~/.bash_profile`
		- `export GOROOT=/usr/local/go/`
4. Edit /etc/security/limits.conf and add the following lines (replace *username* with your user):

	```
		username	soft	nofile	8096  
		username	hard	nofile	8096  
	```

	You will need to reboot after changing this. If you don't increase the file handle limit you may see some weird build issues with browserify or npm.
5. Install Node.js
	`pacman -S nodejs npm`
6. Fork Mattermost on GitHub.com from [https://github.com/mattermost/platform](https://github.com/mattermost/platform), then:
	1. `cd ~/go`  
	2. `mkdir -p src/github.com/mattermost`  
	3. `cd src/github.com/mattermost`  
	4. `git clone https://github.com/<username>/platform.git`  
	5. `cd platform`
7. Run `make run` to start Mattermost
8. Browse to `http://localhost:8065` to create an account. The first account created has System Administrator privileges.
9. You can stop Mattermost using `make stop`
10. If you want to setup for cross compilation (required for the `make package` and dependant targets) run:
    - Note: You can skip the platform you are on because you have that target installed by default.
    - `env GOOS=windows GOARCH=amd64 go install std`
    - `env GOOS=darwin GOARCH=amd64 go install std`
    - `env GOOS=linux GOARCH=amd64 go install std`

Any issues? Please let us know on our forums at: http://forum.mattermost.org

### Windows ###

1. Install and setup Docker
    1. If you are using Windows 10 Pro or Enterprise, you may use Docker for Windows
        1. Install [Docker for Windows](https://docs.docker.com/docker-for-windows/)
        2. Add the line `127.0.0.1 dockerhost` to `C:\Windows\System32\drivers\etc\hosts` using a text editor with administrator privileges
    2. For other Windows versions, or if you prefer to use [VirtualBox](https://www.virtualbox.org/wiki/Downloads), use Docker Toolbox
        1. Install [Docker Toolbox](https://www.docker.com/products/docker-toolbox)
        2. Run the `Docker Quickstart Terminal` and let it configure the `default` machine
        3. Run `docker-machine ip default` in the terminal to get `default` IP
        4. Add the line `<Docker-IP> dockerhost` to `C:\Windows\System32\drivers\etc\hosts` using a text editor with administrator privileges
2. Download and install Node.js from [https://nodejs.org/](https://nodejs.org/)
3. Download and install Go from [https://golang.org/dl/](https://golang.org/dl/) 
4. Fork Mattermost on GitHub.com from [https://github.com/mattermost/platform](https://github.com/mattermost/platform), then:
    1. `cd ~/go`  
    2. `mkdir -p src/github.com/mattermost`  
    3. `cd src/github.com/mattermost`  
    4. `git clone https://github.com/<username>/platform.git`  
    5. `cd platform`
    6. `git config core.eol lf`
    7. `git config core.autocrlf input`
    8. `git reset --hard HEAD`
5. Install and setup babun from [http://babun.github.io/](http://babun.github.io/)
6. Setup the following environment variables (change the path accordingly):
      
    ```
    export PATH="/c/Program Files/go/bin":$PATH
    export PATH="/c/Program Files/nodejs":$PATH
    export PATH="/c/Program Files/Git/bin":$PATH    
    export GOROOT='c:\\Program Files\\go'
    export GOPATH='c:\\User\\<user-name\\go'
    export PATH="/c/Program Files/Docker Toolbox":$PATH #change the path accordingly if you are using Docker for Windows
    eval $(docker-machine env default) #skip this line if you are using Docker for Windows
    ```

7. Run `make run` to start Mattermost
8. You can now log in to Mattermost as the user you created in step 9
9. If you want to setup for cross compilation (required for the `make package` and dependant targets) run:
    - Note: You can skip the platform you are on because you have that target installed by default.
    - `env GOOS=windows GOARCH=amd64 go install std`
    - `env GOOS=darwin GOARCH=amd64 go install std`
    - `env GOOS=linux GOARCH=amd64 go install std`

Any issues? Please let us know on our forums at: http://forum.mattermost.org

## Troubleshooting

#### I get the following error when running `make run` on Mac OS X: "Cannot connect ot the Docker daemon"

If you have Docker Tools installed (as opposed to Docker for Mac), you need make sure `docker-machine` is running with the following:
```
docker-machine start dev
```

#### I get the following error when running `make run`: "Failed to ping db err:dial tcp 192.168.99.100:3306: getsockopt: connection refused"

It appears that your MySQL database isn't running. If you run `docker ps`, you should see a line like
```
ecb17c10973d    mysql:5.7  "/entrypoint.sh mysql"   2 weeks ago    Up 24 hours  0.0.0.0:3306->3306/tcp     mattermost-mysql
```
If not, running `make clean-docker` will remove all existing docker containers so that they'll be recreated next time you call `make run`.

#### I get the following error when running `make run`: "Error starting server, err:listen tcp :8065: bind: address already in use"

There's likely another Mattermost instance already running. You can use `make stop` to stop it before running `make run` again.

If there isn't another copy of Mattermost running and you need to change the port that Mattermost is running on, you can do so by changing the `ListenAddress` setting in the `ServiceSettings` section of `config/config.json`.

#### I don't see any error messages, but I can't access `http://localhost:8065`

It's possible that the server reported an error, but it was missed because of all of the output from the Javascript compiler. Try running `make run-server` by itself to see its output. If you still don't see any error messages, continue to the next section.

#### I don't see anything logged to the console when Mattermost is running

You can enable console logging in the `LogSettings` section of your `config/config.json` by setting `EnableConsole` to `true`.

#### I can't log into Mattermost because I don't have an account

You can create an account using the following command:
```
go run mattermost.go -create_user -email="user@example.com" -password="mypassword"
```
Optionally, you can make that account a System Admin with the following command:
```
go run mattermost.go -assign_role -email="user@example.com" -role="system_admin system_user"
```

## Development Flow

Here's a general workflow a Mattermost developer working on our [platform repository](https://github.com/mattermost/platform) will follow:

1. Take a look at the `Repository structure` to find out where to look for what you're working on.
2. On your fork, create a branch `PLT-####` where #### is the ticket number if it is a [Jira](https://mattermost.atlassian.net) ticket, or `GH-####` if it is a GitHub Issue without a Jira ticket.
3. Make the code changes required to complete your ticket, making sure to write or modify unit tests where appropriate.
4. To test your changes, run `make run` from the root directory of the respository. This will start up the server and a watcher process that will build any changes to the client as you make them. To get changes to the server it must be restarted with `make restart-server`. Your server will be running at `http://localhost:8065`.
5. Once everything works to meet the ticket requirements, stop the server with `make stop` and then run both `make check-style` and `make test` to make sure there are no errors with your syntax or tests.
6. Commit your changes, push your branch and [create a pull request](https://docs.mattermost.com/developer/contribution-guide.html#preparing-a-pull-request).
7. Respond to feedback on your pull request and make changes as necessary by commiting to your branch and pushing it. You might need to [rebase your changes](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) if another pull request creates conflicts.
8. That's it! Rejoice that you've helped make Mattermost better.

### Useful Makefile commands

Some other `make` commands that might be useful in addition to the ones mentioned above:

* `make run-server` will run only the server and not the client
* `make clean-docker` stops and removes your docker images and is a good way to wipe your database
* `make run-fullmap` will run the server and build the client with the full source map for easier debugging
* `make clean` cleans your local environment of temporary files
* `make nuke` wipes your local envrionment back to a completely fresh start

### Running only specific unit tests

Since running every single unit test takes a lot of time while making changes, you can run a subset of the serverside unit tests by using the following:
```
go test -v -run='<test name or regex>' ./<package containing test>
```
For example, if you wanted to run `TestPostUpdate` in `api/post_test.go`, you would run the following:
```
go test -v -run='TestPostUpdate' ./api
```

Alternatively, if you're writing client-side code, you can run only the client-side unit tests by using `make test-client`.

### Repository structure

For server work, all the directories you'll need are at the root of the repository.
 * [./api/](https://github.com/mattermost/platform/tree/master/api) holds all API and application related code
 * [./model/](https://github.com/mattermost/platform/tree/master/model) holds all data model definitions and the Go driver
 * [./store/](https://github.com/mattermost/platform/tree/master/store) holds all database querying code
 * [./utils/](https://github.com/mattermost/platform/tree/master/utils) holds all utilities, such as the mail utility
 * [./i18n/](https://github.com/mattermost/platform/tree/master/i18n) holds all localization files for the server

For client work, you'll mostly be working in [./webapp/](https://github.com/mattermost/platform/tree/master/webapp).
 * [./webapp/components/](https://github.com/mattermost/platform/tree/master/webapp/components) holds all the [React](https://facebook.github.io/react/) UI components and views
 * [./webapp/actions/](https://github.com/mattermost/platform/tree/master/webapp/actions) holds all [Flux actions](https://facebook.github.io/flux/docs/actions-and-the-dispatcher.html#content) where the majority of the logic of the webapp takes place
 * [./webapp/stores/](https://github.com/mattermost/platform/tree/master/webapp/stores) holds the stores responsible for storing and providing the views with data
 * [./webapp/routes](https://github.com/mattermost/platform/tree/master/webapp/routes) holds the definitions for all the [React-Router](https://github.com/ReactTraining/react-router) routes
 * [./webapp/i18n/](https://github.com/mattermost/platform/tree/master/webapp/i18n) holds the localization files for the client
 * [./webapp/utils](https://github.com/mattermost/platform/tree/master/webapp/utils) holds all widely-used utilities
 * [./webapp/tests](https://github.com/mattermost/platform/tree/master/webapp/tests) holds all the client unit tests
