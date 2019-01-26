..  _outbound_proxy:

Using an Outbound Proxy
=======================

To use Mattermost behind a proxy, you need to set the ``HTTP_PROXY`` and ``HTTPS_PROXY`` environment variables to the URL for your proxy server. To set these when running the Mattermost server via ``systemd``, modify the ``mattermost.service`` like this:
  
  .. note::
    Be sure to replace `127.0.0.1:3128` with the correct values for your proxy servers.

  .. code-block:: none

    [Unit]
    Description=Mattermost
    After=network.target
    After=postgresql.service
    Requires=postgresql.service

    [Service]
    Type=notify
    ExecStart=/opt/mattermost/bin/mattermost
    TimeoutStartSec=3600
    Restart=always
    RestartSec=10
    WorkingDirectory=/opt/mattermost
    User=mattermost
    Group=mattermost
    LimitNOFILE=49152
    Environment=HTTP_PROXY=http://127.0.0.1:3128
    Environment=HTTPS_PROXY=http://127.0.0.1:3128

    [Install]
    WantedBy=postgresql.service
    
