.. _dev-setup-troubleshooting:

Troubleshooting Setup and Build
===============================

Build Errors
------------

macOS: I get the following error when running ``make run``: "Cannot connect to the Docker daemon"
  If you have Docker Tools installed (as opposed to Docker for Mac), make sure docker-machine is running.

  ``docker-machine start dev``

macOS: I get the following error or something similar when running ``make run``: "Module build failed: Error: dyld: Library not loaded: /usr/local/opt/libpng/lib/libpng16.16.dylib"
  libpng needs to be updated because it is used by one of our dependencies. If you do not have libpng installed through Homebrew, run

  ``brew install libpng``

  If you already have libpng installed through Homebrew, you can update it using the following command:

  ``brew update && brew upgrade libpng``

I get the following error when running ``make run``: "Failed to ping db err:dial tcp 192.168.99.100:3306: getsockopt: connection refused"
  It appears that your MySQL database isn't running. If you run ``docker ps``, you should see a line like

  .. code-block:: text

    ecb17c10973d    mysql:5.7  "/entrypoint.sh mysql"   2 weeks ago    Up 24 hours  0.0.0.0:3306->3306/tcp     mattermost-mysql

  If not, running ``make clean-docker`` will remove all existing Docker containers so that they'll be recreated next time you call ``make run``.

I get the following error when running ``make run``: "Error starting server, err:listen tcp :8065: bind: address already in use"
  There's likely another Mattermost instance already running. You can use ``make stop`` to stop it before running ``make run`` again.

  If there isn't another copy of Mattermost running and you need to change the port that Mattermost is running on, you can do so by changing the ``ListenAddress`` setting in the *ServiceSettings* section of ``config/config.json``.

macOS: I get the following error or something similar when running ``make run``: [ERROR] Failed to ping DB retrying in 10 seconds err=Error 1045: Access denied for user ‘mmuser’@’localhost’ (using password: YES)
  It appears that 'mmuser' is not created as a user in your MySQL database. Hence create the new user by using the following command:
  ``CREATE USER 'mmuser'@'localhost' IDENTIFIED BY 'mostest';``

  Grant all the permissions to the user using the command:

  ``GRANT ALL PRIVILEGES ON * . * TO '
  mmuser
  '@'localhost';``

  Reload the privileges, so that the changes can be reflected: 
  ``FLUSH PRIVILEGES;``

Testing Errors
--------------

I get the following error when running ``make test``: t.Run undefined (type \*testing.T has no field or method Run)
  You need to upgrade to Go 1.9. We don't support earlier versions than that.

Other Errors
------------

I don't see any error messages, but I can't access http://localhost:8065
  It's possible that the server reported an error, but it was missed because of all of the output from the JavaScript compiler. Try running ``make run-server`` by itself to see its output. If you still don't see any error messages, continue to the next section.

I don't see anything logged to the console when Mattermost is running
  You can enable console logging in the *LogSettings* section of your ``config/config.json`` by setting *EnableConsole* to ``true``.

I can't log into Mattermost because I don't have an account
  You can create an account using the following command:

  ``go build -o mattermost && ./mattermost user create --email user@example.com --username test1 --password mypassword``

  Optionally, you can make that account a System Admin with the following command:

  ``go build -o mattermost && ./mattermost user create --email user@example.com --username test1 --password mypassword --system_admin``
