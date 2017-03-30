.. _dev-compiling:

Compiling Mattermost
====================

Server
Client - desktop client for Windows, Mac, and Linux

make sure you set up your machine according to the instructions for your platform:

note that after you type make run, you won't have a command prompt. To get a command prompt, type CTRL+C

``cd ~/go/src/github.com/mattermost/platform``

Useful Commands
---------------

make run
  Starts the Docker container, compiles the server and client code, and makes Mattermost available at http://localhost:8065 on the machine that you ran this command on.
make test
  Runs the unit tests for server and client.
make test-server
  Runs the unit tests for server only.
make test-client
  Runs the unit tests for client only.
make clean
  Removes all output files, including log files and executable binaries.
make start-docker
  Starts the Docker container.
make stop-docker
  Stops the Docker container.
make clean-docker
  Removes all content from the databases in the Docker container.
make package
  Creates packages for distributing your builds and puts them in the ``~/go/src/github.com/mattermost/platform/dist`` directory. If you want to make packages for targets other than your build machine, you must run the following commands first:

  1. Modify permissions on ``/usr/local/go``. Replace *{user}* and *{group}* with the user and group that you are logged in with.

     ``sudo chown -R {user}.{group} /usr/local/go``

  2. Set up your environment to compile Apple OS X binaries:

     ``env GOOS=darwin GOARCH=amd64 go install std``

  3. Set up your environment to compile Windows binaries:

     a. ``env GOOS=windows GOARCH=amd64 go install std``
     b. ``sudo apt-get install zip``

  4. Set up your environment to compile Linux binaries:

    ``env GOOS=linux GOARCH=amd64 go install std``
