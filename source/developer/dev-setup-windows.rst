.. _dev-setup-windows:

Installing Developer Components on Windows
==========================================

1. Install and setup Docker. If you are using Windows 10 Pro or Enterprise, you can use Docker for Windows.
  a. Install `Docker for Windows <https://docs.docker.com/docker-for-windows/>`_.
  b. Add the line ``127.0.0.1 dockerhost`` to ``C:\Windows\System32\drivers\etc\hosts`` using a text editor with administrator privileges.
2. For other Windows versions, or if you prefer to use VirtualBox, use Docker Toolbox:
  a. Install `Docker Toolbox <https://www.docker.com/products/docker-toolbox>`_.
  b. Run the *Docker Quickstart Terminal* and let it configure the ``default`` machine.
  c. Run ``docker-machine ip default`` in the terminal to get the IP address for the next step.
  d. Add the line ``{Docker-IP} dockerhost`` to ``C:\Windows\System32\drivers\etc\hosts`` using a text editor with administrator privileges.
3. Download and install Node.js from https://nodejs.org/.
4. Download and install Go 1.8 from https://golang.org/dl/.
5. Fork Mattermost on GitHub.com from https://github.com/mattermost/platform, then:
  a. ``cd ~/go``
  b. ``mkdir -p src/github.com/mattermost``
  c. ``cd src/github.com/mattermost``
  d. ``git clone https://github.com/{username}/platform.git``
  e. ``cd platform``
  f. ``git config core.eol lf``
  g. ``git config core.autocrlf input``
  h. ``git reset --hard HEAD``
5. Install and setup babun from http://babun.github.io/.
6. Setup the following environment variables (change the path accordingly):

  .. code-block:: batch

    export PATH="/c/Program Files/go/bin":$PATH
    export PATH="/c/Program Files/nodejs":$PATH
    export PATH="/c/Program Files/Git/bin":$PATH
    export GOROOT="c:\\Program Files\\go"
    export GOPATH="c:\\User\\{user-name}\\go"
    export PATH="/c/Program Files/Docker Toolbox":$PATH #change the path accordingly if you are using Docker for Windows
    eval $(docker-machine env default) #skip this line if you are using Docker for Windows

Now that everything is set up, you are ready to compile and run Mattermost. See :doc:`dev-compiling`.
