:orphan:
:nosearch:

Install the Mattermost Server by extracting the tarball, creating users and groups, and setting file/folder permissions. 

First extract the tarball:

.. code-block:: none
  :class: mm-code-block 

    tar -xvzf mattermost*.gz

Now move the entire folder to the ``/opt`` directory (or whatever path you require):

.. code-block:: none
  :class: mm-code-block 

    sudo mv mattermost /opt

.. note::

	If you choose a custom path, ensure this alternate path is used in all steps that follow.

By default the Mattermost Server uses ``/opt/mattermost/data`` as the folder for files. This can be changed in the System Console during setup (even using alternative storage such as S3). Create the default storage folder:

.. code-block:: none
  :class: mm-code-block 
    
    sudo mkdir /opt/mattermost/data

Now set up a user and group called ``mattermost``:

.. code-block:: none
  :class: mm-code-block 
    
    sudo useradd --system --user-group mattermost

.. note::

	If you choose a custom user and group name, ensure it is used in all the steps that follow.

Set the file and folder permissions for your installation:

.. code-block:: none
  :class: mm-code-block 
    
    sudo chown -R mattermost:mattermost /opt/mattermost

Give the ``mattermost`` group write permissions to the application folder:

.. code-block:: none
  :class: mm-code-block 
        
    sudo chmod -R g+w /opt/mattermost

You will now have the latest Mattermost Server version installed on your system. Starting and stopping the Mattermost Server is done using ``systemd``. Create the systemd unit file:

.. code-block:: none
  :class: mm-code-block 
    
    sudo touch /lib/systemd/system/mattermost.service

As root, edit the systemd unit file to add the following lines:

.. code-block:: none
  :class: mm-code-block 

    [Unit]
    Description=Mattermost
    After=network.target

    [Service]
    Type=notify
    ExecStart=/opt/mattermost/bin/mattermost
    TimeoutStartSec=3600
    KillMode=mixed
    Restart=always
    RestartSec=10
    WorkingDirectory=/opt/mattermost
    User=mattermost
    Group=mattermost
    LimitNOFILE=49152

    [Install]
    WantedBy=multi-user.target

Save the file and reload systemd using ``sudo systemctl daemon-reload``. Mattermost Server is now installed and is ready for setup.

.. note::
	
	If you are installing the Mattermost server on the same system as your database, you may want to add both ``After=postgresql.service`` and ``BindsTo=postgresql.service`` to the ``[Unit]`` section of the systemd unit file.
