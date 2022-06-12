Make a call (beta)
==================

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.
  
Mattermost calls introduces voice calling and screen sharing functionality in channels, group messages, and direct messages, and is available as a beta release from Mattermost v7.0 for Mattermost Cloud and Mattermost self-hosted deployments.

From 7.0, you can:

- Use calls on desktop and mobile apps in addition to web browsers.
- Share screen (not available on mobile), raise hands, chat in a thread, and even switch between products in the Mattermost suite (ie. Channels, Boards, and Playbooks) while on a call.
- Start a call using the ``/start call`` slash command.

Mattermost Cloud users can start using calls right away. For Mattermost self-hosted deployments, calls is available as a plugin that can be enabled in the System Console by a System Admin. <link to config doc>.

To start a call, select **Start call** in the channel header. Any active team member in the channel can join a call, whether it's a public or private channel. If someone from outside of the organization wants to join a call, you'll need to provide them with a guest account, and add them to the channel. Users who are archived or not registered won't be able to join a call.

Each call has a unique URL. You can share a call's URL to use in a meeting request or share with other team mates. The link is unique to each channel, and contains the channel's ID, so it doesn't change between calls. To access the link, hover over the call dialog in the channel and open the **More** menu. Select **Copy link**. The call link is valid for long as the channel is active. When a channel is archived or deleted the link will become invalid.

Limitations
-----------

- In Mattermost Cloud, up to eight participants per channel can join a call.
- In Mattermost self-hosted deployments, the default maximum number of participants is unlimited. The recommended maximum number of participants, across all calls in all channels on the server, is 200. This setting can be changed in **System Console > Plugin Management > Calls > Max call participants**.

Configuration
-------------

For Mattermost self-hosted customers, the calls plugin needs to be enabled in the System Console. Additional configuration is also available via the System Console.

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

# Setting the maximum buffer size of the receiving UDP buffer to 16MB
``net.core.rmem_max = 16777216``

# Setting the maximum buffer size of the sending UDP buffer to 16MB
``net.core.wmem_max = 16777216``

# Allow to allocate more memory as needed for more control messages that need to be sent for each socket connected
``net.core.optmem_max = 16777216``

Are there any third-party services involved?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

STUN servers are configurable on the plugin itself. These are optional and depend on your configuration.

Troubleshooting
---------------

My call is disconnected after a few seconds and I can't transmit voice nor hear anything.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is usually a sign that the underlying UDP channel has not been established and the connection timeouts after ~10 seconds. When the connection has been established correctly an `rtc: connected` line should appear in the client-side logs (JS Console). There isn't a single solution as it depends on the infrastructure/deployment specifics. However, if you're a System or Network Admin, you may need to open up the UDP port or configure the network accordingly.
