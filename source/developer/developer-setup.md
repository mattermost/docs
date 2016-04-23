Developer Machine Setup
-----------------------------

### Mac OS X ###

1. Download and set up Docker Toolbox
	1. Follow the instructions at http://docs.docker.com/installation/mac/
	2. Start a new docker host  
		`docker-machine create -d virtualbox dev`
	2. Get the IP address of your docker host  
		`docker-machine ip dev`
	3. Add a line to your /etc/hosts that goes `<Docker IP> dockerhost`
	4. Run `docker-machine env dev` and copy the export statements to your ~/.bash_profile
2. Download Go 1.6 and Node.js using Homebrew
	1. Download Homebrew from http://brew.sh/
	2. `brew install go`
	3. `brew install node`
3. Set up your Go workspace
	1. `mkdir ~/go`
	2. Add the following to your ~/.bash_profile  
		- `export GOPATH=$HOME/go`  
		- `export PATH=$PATH:$GOPATH/bin`  
		- `ulimit -n 8096`  
		- If you don't increase the file handle limit you may see some weird build issues with browserify or npm.  
	3. Reload your bash profile  
		`source ~/.bash_profile`
4. Download Mattermost  
	- `cd ~/go`  
	- `mkdir -p src/github.com/mattermost`  
	- `cd src/github.com/mattermost`  
	- `git clone https://github.com/mattermost/platform.git`  
	- `cd platform`

5. Run unit tests on Mattermost using `make test` to make sure the installation was successful
6. If the tests passed, you need to create a team and an admin account. You can choose a team name, email and password:
	- Note: Make sure your team name does not contain any spaces.
	- `godep go run mattermost.go  -create_team -team_name="name" -email="user@example.com"`
	- `godep go run mattermost.go  -create_user -team_name="name" -email="user@example.com" -password="mypassword"`
	- `godep go run mattermost.go  -assign_role -team_name="name" -email="user@example.com" -role="system_admin"`

7. Now you can run Mattermost using `make run`. Log-in as the admin account you created in step 6
8. You can stop Mattermost using `make stop`
9. If you want to setup for cross compilation (required for the `make package` and dependant targets) run:
    - Note: You can skip the platform you are on because you have that target installed by default.
    - `env GOOS=windows GOARCH=amd64 go install std`
    - `env GOOS=darwin GOARCH=amd64 go install std`
    - `env GOOS=linux GOARCH=amd64 go install std`

Any issues? Please let us know on our forums at: http://forum.mattermost.org

### Ubuntu ###

1. Download Docker
	1. Follow the instructions at https://docs.docker.com/installation/ubuntulinux/ or use the summary below:  
		- `sudo apt-get update`  
		- `sudo apt-get install wget`  
		- `wget -qO- https://get.docker.com/ | sh`  
		- `sudo usermod -aG docker <username>`  
		- `sudo service docker start`  
		- `newgrp docker`
2. Set up your dockerhost address
	1. Edit your /etc/hosts file to include the following line  
		- `127.0.0.1 dockerhost`
3. Install build essentials
	1. `apt-get install build-essential`
4. Download Go 1.5.1 from http://golang.org/dl/
5. Set up your Go workspace and add Go to the PATH
	1. `mkdir ~/go`
	2. Add the following to your ~/.bashrc  
		- `export GOPATH=$HOME/go`  
		- `export PATH=$PATH:$GOPATH/bin`  
		- `ulimit -n 8096`  
		- If you don't increase the file handle limit you may see some weird build issues with browserify or npm.  
	3. Reload your bashrc  
		- `source ~/.bashrc`
6. Install Node.js  
	- `curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -`  
	- `sudo apt-get install -y nodejs`
7. Download Mattermost  
	- `cd ~/go`  
	- `mkdir -p src/github.com/mattermost`  
	- `cd src/github.com/mattermost`  
	- `git clone https://github.com/mattermost/platform.git`  
	- `cd platform`
8. Run unit tests on Mattermost using `make test` to make sure the installation was successful
9. If the tests passed, you need to create a team and an admin account. You can choose a team name, email and password:
	- Note: Make sure your team name does not contain any spaces.
	- `godep go run mattermost.go  -create_team -team_name="name" -email="user@example.com"`
	- `godep go run mattermost.go  -create_user -team_name="name" -email="user@example.com" -password="mypassword"`
	- `godep go run mattermost.go  -assign_role -team_name="name" -email="user@example.com" -role="system_admin"`

10. Now you can run Mattermost using `make run`. Log-in as the admin account you created in step 10
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
		1. `export GOPATH=$HOME/go`
		2. `export GOROOT=/usr/lib/go`
		3. `export PATH=$PATH:$GOROOT/bin`
	3. Reload your bashrc
		`source ~/.bashrc`
4. Edit /etc/security/limits.conf and add the following lines (replace *username* with your user):

	```
		username	soft	nofile	8096  
		username	hard	nofile	8096  
	```

	You will need to reboot after changing this. If you don't increase the file handle limit you may see some weird build issues with browserify or npm.
5. Install Node.js
	`pacman -S nodejs npm`
6. Download Mattermost
	`cd ~/go`  
	`mkdir -p src/github.com/mattermost`  
	`cd src/github.com/mattermost`  
	`git clone https://github.com/mattermost/platform.git`  
	`cd platform`  
7. Run unit tests on Mattermost using `make test` to make sure the installation was successful
8. If the tests passed, you need to create a team an admin account. You can choose a team name, email and password:
	- Note: Make sure your team name does not contain any spaces.
	- `godep go run mattermost.go  -create_team -team_name="name" -email="user@example.com"`
	- `godep go run mattermost.go  -create_user -team_name="name" -email="user@example.com" -password="mypassword"`
	- `godep go run mattermost.go  -assign_role -team_name="name" -email="user@example.com" -role="system_admin"`

9. Now you can run Mattermost using `make run`. Log-in as the admin account you created in step 8
10. You can stop Mattermost using `make stop`
11. If you want to setup for cross compilation (required for the `make package` and dependant targets) run:
    - Note: You can skip the platform you are on because you have that target installed by default.
    - `env GOOS=windows GOARCH=amd64 go install std`
    - `env GOOS=darwin GOARCH=amd64 go install std`
    - `env GOOS=linux GOARCH=amd64 go install std`

Any issues? Please let us know on our forums at: http://forum.mattermost.org
