..  _outbound_proxy:

Using an Outbound Proxy
=======================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

In some scenarios, you may wish to use Mattermost behind a proxy. This can be used to do things such as monitoring outbound traffic from Mattermost or controlling which websites can appear in link previews and other embedded content. If you only want to use a proxy for images, the `image proxy <https://docs.mattermost.com/deploy/image-proxy.html>`__ is also an option.

Configuration
-------------

Mattermost's use of a proxy is configured using the ``HTTP_PROXY``, ``HTTPS_PROXY`` and ``NO_PROXY`` environment variables.

``HTTP_PROXY`` and ``HTTPS_PROXY``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``HTTP_PROXY`` and ``HTTPS_PROXY`` environment variables store the address of the proxy server for HTTP and HTTPS requests respectively. This value should include the protocol and port of the proxy such as ``http://192.168.4.5:3128``.

If you wish to have Mattermost authenticate with your proxy, it supports HTTP basic authentication by specifying the address of the proxy such as ``http://mattermost:password@192.168.4.5:3128``.

Note that when proxying through a proxy that uses the ``HTTPS`` protocol, you'll need to configure your Mattermost server with the root certificate of the proxy. Otherwise, Mattermost will refuse any response from the proxy as it will detect that its connection has been intercepted.

``NO_PROXY``
~~~~~~~~~~~~

The ``NO_PROXY`` environment variable can be set to prevent certain requests from going through the proxy, such as to an SSO provider (e.g. GitLab or SAML) or intranet sites that should be accessible in link previews. It can be configured as a set of comma-separated IP addresses (e.g. ``1.2.3.4``), IP address ranges specified in CIDR notation (e.g. ``1.2.3.4/8``), or domain names. An IP address or domain name can also include a port number.

When a domain name is specified, the domain and all of its subdomains are matched, however a domain name with a leading ``.`` only matches the subdomains. For example, ``example.com`` matches both ``example.com`` and ``sub.example.com`` while ``.example.com`` only matches the latter.

Sample Configuration
--------------------

To set these environment variables while running the Mattermost server via ``systemd``, modify the ``mattermost.service`` like this:

  .. note::
    Be sure to replace ``127.0.0.1:3128`` with the correct values for your proxy servers.

  .. code-block:: none

    [Unit]
    Description=Mattermost
    After=network.target
    After=postgresql.service
    BindsTo=postgresql.service

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
    Environment=HTTP_PROXY=http://mattermost:password@127.0.0.1:3128
    Environment=HTTPS_PROXY=https://mattermost:password@127.0.0.1:3128
    Environment=NO_PROXY=1.2.3.4:567,.internal.example.com,login.example.com

    [Install]
    WantedBy=postgresql.service
    
For GitLab Mattermost follow the details at https://docs.gitlab.com/omnibus/gitlab-mattermost/#setting-custom-environment-variables instead.
