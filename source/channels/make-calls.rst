Start a call (beta)
===================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:
  
Mattermost introduces beta voice calling and screen sharing functionality in channels, group messages, and direct messages from Mattermost v7.0 for Mattermost Cloud and Mattermost self-hosted deployments.

From 7.0, you can:

- Start or join a call from desktop and mobile apps in addition to web browsers.
- Share screen (not available on mobile), raise hands, chat in a thread, and even switch between products in the Mattermost suite (i.e., Channels, Boards, and Playbooks) while on a call.
- Start a call using the ``/call start`` slash command or **Start call** in the channel header.

Mattermost Cloud users can start calling right out of the box. For Mattermost self-hosted deployments, System Admins need to enable the plugin and adjust configurations `in the System Console </configure/configuration-settings.html#calls-beta>`_.

To start a call, select **Start call** in the channel header. Any active team member in the channel can join a call, whether it's a public or private channel. If someone from outside of the organization wants to join a call, you'll need to provide them with a guest account, and add them to the channel. Users who are archived or not registered won't be able to join a call.

You can share a call's link to use in a meeting request or share with other team mates. The link is unique to each channel, and contains the channel's ID, so it doesn't change between calls. Use the ``/call link`` slash command to generate a shareable link.

The call link is valid for long as the channel is active. When a channel is archived or deleted the link will become invalid.

Frequently asked questions
--------------------------

Is video supported?
~~~~~~~~~~~~~~~~~~~

The integration currently supports only voice calling and screen sharing. We are considering video support as well for the upcoming future.

Can I password-protect a call?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Any member with sufficient permission to access the channel will be able to join the call.

Is there encryption?
~~~~~~~~~~~~~~~~~~~~

Media (audio/video) is encrypted using security standards as part of WebRTC. It's mainly a combination of DTLS and SRTP. It's not e2e encrypted in the sense that in the current design all media needs to go through Mattermost which acts as a media router and has complete access to it. Media is then encrypted back to the clients so it's secured during transit. In short: only the participant clients and the Mattermost server have access to unencrypted call data.

Are there any third-party services involved?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The only external service used is Mattermost official STUN server (``stun.global.calls.mattermost.com``) which is configured as default. This is primarily used to find the public address of the Mattermost instance. The only information sent to this service is the IP addresses of clients connecting as no other traffic goes through it. It can be removed in case the ``ICE Host Override`` setting is provided.

Troubleshooting
---------------

My call is disconnected after a few seconds and I can't transmit voice nor hear anything.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is usually a sign that the underlying UDP channel has not been established and the connection times out after ~10 seconds. When the connection has been established correctly an ``rtc connected`` line should appear in the client-side logs (JS console). There isn't a single solution as it depends on the infrastructure/deployment specifics. However, if you're a System or Network Admin, you may need to open up the UDP port or configure the network accordingly.

Debugging
---------

If you experience issues with calls, collecting information is helpful as you can share it with us for debugging purposes. 

As with any other issue, but more importantly with calls, it’s very useful to provide date and time of when some problem occurred, with as much detail as possible so that information can be cross-checked with server logs as well. Also please include any reproduction steps if applicable. Other important information include:

- Browser/app version
- Operating system type and version

JS console logs
~~~~~~~~~~~~~~~

Web app
^^^^^^^

- **Chrome**: CMD+OPTION+J (macOS)/CTRL+SHIFT+J (Windows, Linux, ChromeOS)
- **Firefox**: CMD+SHIFT+J (macOS)/CTRL+SHIFT+J (Windows, Linux, ChromeOS).
- **Safari**: Enable Developer Menu in **Safari > Preferences > Advanced > Show Develop Menu in Menu Bar**. Then **Develop > Show Javascript Console**. Right-click on the console and select **Save to file** to download the logs.

Desktop app
^^^^^^^^^^^

In the top menu bar of the app, select **View > Developer Tools for Current Tab**. In the logs that are generated, right-click and select **Save as** to download the logs.

Call stats dump
---------------

In cases where there are audio/video issues, difficulty in hearing other participants, and/or stuttering video and/or choppy audio, run the ``/call stats`` slash command in the channel where the call is currently active. This returns a JSON object via an ephemeral message.

You can run this command in an active call or after leaving the call in question. However, we will only save data for the last joined call so joining again will delete the previous call's feedback.

WebRTC internals (Chrome + Firefox only)
----------------------------------------

This is an additional method for Chrome and Firefox users in cases where there are audio/video issues, difficulty in hearing other participants, and/or stuttering video and/or choppy audio.

Chrome browser (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open ``chrome://webrtc-internals/`` in the browser that you're using for the active call.

Firefox browser
~~~~~~~~~~~~~~~

Open ``about://webrtc`` in the browser that you're using for the active call.

Share information
~~~~~~~~~~~~~~~~~

Debug information is helpful to our community as there may be other community members having the same issue as you. We recommend that debug information be shared in either of the two options below:

- Post in `Developers: Calls <https://community.mattermost.com/core/channels/developers-channel-call>`_ channel:  prefer this method when possible but keep in mind the channel is public.
- Post in `Team: Calls <https://community.mattermost.com/private-core/channels/calls-team>`_ channel: use this channel if posting sensitive information.
