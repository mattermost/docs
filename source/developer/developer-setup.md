Developer Machine Setup
-----------------------------

### Mac OS X ###

1. Download and set up the latest version of VirtualBox. [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)
2. Download and set up Docker Toolbox
	1. Follow the instructions at [http://docs.docker.com/installation/mac/](http://docs.docker.com/installation/mac/)
	2. Start a new docker host  
		`docker-machine create -d virtualbox dev`
	2. Get the IP address of your docker host  
		`docker-machine ip dev`
	3. Add the following line to `/etc/hosts`
		`<Docker IP> dockerhost`
	4. Run `docker-machine env dev` and copy the export statements to `~/.bash_profile`
3. Download Go 1.6 and Node.js using Homebrew
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

6. Run unit tests on Mattermost using `make test` to confirm the installation succeeded
7. If the tests passed, you run `make clean-docker` to clean the database, then `make run` to start Mattermost
8. Browse to `http://localhost:8065` to create an account. The first account created has System Administrator privileges.
9. You can stop Mattermost using `make stop`
10. If you want to setup for cross compilation (required for the `make package` and dependant targets) run:
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
4. Download Go 1.5.1 from [http://golang.org/dl/](http://golang.org/dl/)
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
8. Run unit tests on Mattermost using `make test` to confirm the installation succeeded
9. If the tests passed, you run `make clean-docker` to clean the database, then `make run` to start Mattermost
10. Browse to `http://localhost:8065` to create an account. The first account created has System Administrator privileges.
11. You can stop Mattermost using `make stop`
12. If you want to setup for cross compilation (required for the `make package` and dependant targets) run:
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
7. Run unit tests on Mattermost using `make test` to confirm the installation succeeded
8. If the tests passed, you run `make clean-docker` to clean the database, then `make run` to start Mattermost
9. Browse to `http://localhost:8065` to create an account. The first account created has System Administrator privileges.
10. You can stop Mattermost using `make stop`
11. If you want to setup for cross compilation (required for the `make package` and dependant targets) run:
    - Note: You can skip the platform you are on because you have that target installed by default.
    - `env GOOS=windows GOARCH=amd64 go install std`
    - `env GOOS=darwin GOARCH=amd64 go install std`
    - `env GOOS=linux GOARCH=amd64 go install std`

Any issues? Please let us know on our forums at: http://forum.mattermost.org

## Developing Using PostgreSQL

By default, development is done using a MySQL database. To switch your developement instance to use a PostgreSQL database, update the following settings in the `SqlSettings` section of your `config/config.json`
```
    "DriverName": "mysql",
    "DataSource": "mmuser:mostest@tcp(dockerhost:3306)/mattermost_test?charset=utf8mb4,utf8",
```
to
```
    "DriverName": "postgres",
    "DataSource": "postgres://mmuser:mostest@dockerhost:5432?sslmode=disable&connect_timeout=10",
```

## Development Flow 

A few tips to develop efficiently: 

### Making quick user interface changes 

Use `make run` to run locally. This starts a watcher process and you can change JavaScript files without restarting the server. Just wait a few seconds, refresh the page and you should see changes. 

Connect to your server using `http://localhost:8065`

### Debugging JavaScript 

Use `make run-fullmap` to produce JavaScript that you can look at in a debugger. 

### Restarting the server quickly 

After `make run` you can restart the server while leaving the JavaScript running using `make stop-server` then `make run-server`. This usually takes less than 10 seconds. 
