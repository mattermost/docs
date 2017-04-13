Running Mattermost
==================

To run changes to server-side code:
  .. code-block:: text

    make stop
    make test
    make run

To run changes to client-side code:
  .. code-block:: text

    make run

  Client side code reloads automatically upon saving.

To clean the database:
  .. code-block:: text

    make stop
    make clean-docker

To clean the database, logs, and workspace:
  .. code-block:: text

    make stop
    make clean

To remove everything:
  .. code-block:: text

    make stop
    make nuke

To check styles of Go and JavaScript:
  .. code-block:: text

    make check-style

To run a test SMTP server using Python:
  .. code-block:: text

    sudo python -m smtpd -n -c DebuggingServer localhost:25

To run a test SMTP server using `Inbucket <http://www.inbucket.org/>`_ in the Mattermost Docker image:
  .. code-block:: text

    make start-docker

  When Docker starts, the SMTP server is available on port 2500. Username and password are not required. You can access Inbucket webmail on port 9000.
