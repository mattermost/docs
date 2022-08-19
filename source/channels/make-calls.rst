Start a call (beta)
===================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:
  
Mattermost introduces beta voice calling and screen sharing functionality in channels, group messages, and direct messages from Mattermost v7.0 for Mattermost Cloud and Mattermost self-hosted deployments.

From 7.0, you can:

- Start or join a call from desktop and mobile apps in addition to web browsers.
- Share screen (not available on mobile), raise hands, chat in a thread, and even switch between products in the Mattermost suite (i.e., Channels, Boards, and Playbooks) while on a call.
- Start a call using the ``/call start`` slash command or **Start call** in the channel header.

Mattermost Cloud users can start calling right out of the box. For Mattermost self-hosted deployments, System Admins need to enable the plugin and adjust configurations `in the System Console <https://docs.mattermost.com/configure/configuration-settings.html#calls-beta>`_.

To start a call, select **Start call** in the channel header. Any active team member in the channel can join a call, whether it's a public or private channel. If someone from outside of the organization wants to join a call, you'll need to provide them with a guest account, and add them to the channel. Users who are archived or not registered won't be able to join a call.

You can share a call's link to use in a meeting request or share with other team mates. The link is unique to each channel, and contains the channel's ID, so it doesn't change between calls. Use the ``/call link`` slash command to generate a shareable link.

The call link is valid for long as the channel is active. When a channel is archived or deleted the link will become invalid.

Requirements
-----------

Server
^^^^^^

- Run Mattermost server on a secure (HTTPs) connection. This is a necessary requirement on the client to allow capturing devices (e.g., microphone, screen). See the `config TLS </install/config-tls-mattermost.html>`_ section for more info.
- Open the UDP port configured as ``RTC Server Port`` (default is 8443, incoming direction). This is necessary to allow calls related traffic (e.g., audio, video).
- Open the UDP port used by the configured STUN server (default is 3478, outgoing direction). By default the plugin will attempt to identify the instance's public IP address. To do this the STUN protocol is used. This requirement does not apply when manually setting an IP/hostname through the ``ICE Host Override`` config option.

Client
^^^^^^
- Clients need to be able to connect (send and receive data) to the instance hosting the calls through the UDP port configured as ``RTC Server Port``. If this is not possible a TURN server should be used to achieve connectivity.
- Depending on the platform or operating system, clients may need to grant additional permissions to the application (e.g., browser, desktop app) to  allow them to capture audio inputs or share the screen.

Limitations
-----------

- In Mattermost Cloud, up to eight participants per channel can join a call. This is a temporary and evolving limitation during public beta.
- In Mattermost self-hosted deployments, the default maximum number of participants is unlimited. The recommended maximum number of participants, across all calls in all channels on the server, is 200. This setting can be changed in **System Console > Plugin Management > Calls > Max call participants**.

Configuration
-------------

For Mattermost self-hosted customers, the calls plugin is pre-packaged, installed, and enabled. Configuration to allow end-users to use it can be found in the `System Console <https://docs.mattermost.com/configure/configuration-settings.html#calls-beta>`_.

Frequently asked questions
--------------------------

Can I password-protect a call?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Any member with sufficient permission to access the channel will be able to join the call.

Is there encryption?
~~~~~~~~~~~~~~~~~~~~

Media (audio/video) is encrypted using security standards as part of WebRTC. It's mainly a combination of DTLS and SRTP. It's not e2e encrypted in the sense that in the current design all media needs to go through Mattermost which acts as a media router and has complete access to it. Media is then encrypted back to the clients so it's secured during transit. In short: only the participant clients and the Mattermost server have access to unencrypted call data.

What are the potential performance impacts?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Database load should be minimal. Overall instance load however will be affected, especially CPU usage, growing as a function of the number of participants produce the number of active tracks (unmuted participants and users sharing their screen). Screen sharing has the highest impact on both CPU and bandwidth. The latter can be more easily estimated as the audio/video bitrates are constrained and predictable (around 40-60Kbps for each audio track and up to 1Mbps per screen track).

If you wish to host many calls or calls with a large number of participants, take a look at the following platform specific (Linux) tunings (this is the only officially supported target for the plugin right now):

.. code::

  # Setting the maximum buffer size of the receiving UDP buffer to 16MB
  net.core.rmem_max = 16777216

  # Setting the maximum buffer size of the sending UDP buffer to 16MB
  net.core.wmem_max = 16777216

  # Allow to allocate more memory as needed for more control messages that need to be sent for each socket connected
  net.core.optmem_max = 16777216

Are there any third-party services involved?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

STUN servers are configurable on the plugin itself. These are optional and depend on your configuration.

Troubleshooting
---------------

My call is disconnected after a few seconds and I can't transmit voice nor hear anything.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is usually a sign that the underlying UDP channel has not been established and the connection timeouts after ~10 seconds. When the connection has been established correctly an ``rtc connected`` line should appear in the client-side logs (JS console). There isn't a single solution as it depends on the infrastructure/deployment specifics. However, if you're a System or Network Admin, you may need to open up the UDP port or configure the network accordingly.
