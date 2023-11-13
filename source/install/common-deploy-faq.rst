:orphan:
:nosearch:

Why doesn't Mattermost start at system boot?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To have the Mattermost Server start at system boot, the systemd until file needs to be enabled. Run the following command:

.. code-block:: none
  :class: mm-code-block 

    sudo systemctl enable mattermost.service

Why does Mattermost fail to start at system boot?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your database is on the same system as your Mattermost Server, we recommend editing the default ``/lib/systemd/system/mattermost.service`` systemd unit file to add ``After=postgresql.service`` and ``BindsTo=postgresql.service`` to the ``[Unit]`` section.

Can I run Mattermost without a proxy?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Mattermost binds to 443 instead of 8065. The Mattermost binary requires the correct permissions to do that binding. You must activate the ``CAP_NET_BIND_SERVICE`` capability to allow the new Mattermost binary to bind to ports lower than 1024 by running the following command:

.. code-block:: none
  :class: mm-code-block 

    sudo setcap cap_net_bind_service=+ep ./mattermost/bin/mattermost

.. note::
  
  - We recommend the `Mattermost Omnibus install method </install/installing-mattermost-omnibus.html>`__ over the tarball if you are running the Mattermost Server and database a single system as this greatly reduces setup and ongoing maintenance.
  - We highly recommend using a proxy in front of Mattermost server for up to 200 concurrent users. If you have fewer than 200 concurrent users, you can `set up TLS </install/setup-tls.html>`__. If you're exceeding 200 concurrent users, you'll need `a proxy </install/setup-nginx-proxy.html>`__, such as NGINX, in front of Mattermost to manage the traffic.