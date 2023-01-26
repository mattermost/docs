Start a call 
============

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v7.0, you can make voice calls and share your screen in channels, group messages, and direct messages in both Mattermost Cloud and Mattermost self-hosted deployments.

- `Features <#features>`__
- `Record calls <#record-calls>`__
- `Frequently asked questions <#frequently_asked_questions>`__
- `Troubleshooting <#troubleshooting>`__

   - `My call is disconnected after a few seconds <#my-call-is-disconnected-after-a-few-seconds>`__

   - `I can't screen share using Mattermost desktop on macOS <#i-cant-screen-share-using-mattermost-desktop-on-macos>`__

- `Debugging <#debugging>`__

Features 
--------

Starting from Mattermost v7.0, you can:

- Start or join a call from desktop and mobile apps in addition to web browsers.
- Share screen (not available on mobile), raise hands, chat in a thread, and even switch between products in the Mattermost suite (i.e., Channels, Boards, and Playbooks) while on a call.
- Start a call using the ``/call start`` slash command or **Start call** in the channel header.

Starting from Mattermost v7.7 you can:

- Record calls (Mattermost Enterprise only).
- React using emojis.

Mattermost Cloud users can start calling right out of the box. For Mattermost self-hosted deployments, System Admins need to enable the plugin and adjust configurations `in the System Console </configure/plugins-configuration-settings.html#calls>`_.

To start a call, select **Start call** in the channel header. Any active team member in the channel can join a call, whether it's a public or private channel. If someone from outside of the organization wants to join a call, you'll need to provide them with a guest account, and add them to the channel. Users who are archived or not registered can't join a call.

You can share a call's link to use in a meeting request or share with other team mates. The link is unique to each channel, and contains the channel's ID, so it doesn't change between calls. Use the ``/call link`` slash command to generate a shareable link.

The call link is valid for long as the channel is active. When a channel is archived or deleted the link will become invalid.

Record calls
------------

From Mattermost v7.7 if you're the host of a meeting, you can record the call. 

The recording includes audio as well as any screen sharing during the call. The default setting for a recording is 60 minutes, but your system admin may adjust that as needed. Ten minutes before the time limit is reached, you'll receive a reminder that the recording limit will be reached soon.

If your call is going to continue and you still want to record, once the first recording is complete you can start a new one immediately after.

When you stop recording, the recording is posted in the call thread as a file attachment. It's available to all users in the channel both during the call, and when the call has ended.

To record a call:

1. Select **Start call** in the header of the channel, group message, or direct message.
2. Select the pop-out icon.
3. In the pop-out screen, select the record button.
4. To stop recording, select the record button again.

Frequently asked questions
--------------------------

Is video supported?
~~~~~~~~~~~~~~~~~~~

The integration currently supports only voice calling and screen sharing. We're considering video support in the future.

Can I password-protect a call?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Any member with sufficient permission to access the channel can join the call.

Is there encryption?
~~~~~~~~~~~~~~~~~~~~

Media (audio/video) is encrypted using security standards as part of WebRTC. It's mainly a combination of DTLS and SRTP. It's not e2e encrypted in the sense that in the current design all media needs to go through Mattermost which acts as a media router and has complete access to it. Media is then encrypted back to the clients so it's secured during transit. In short: only the participant clients and the Mattermost server have access to unencrypted call data.

Are there any third-party services involved?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The only external service used is Mattermost official STUN server (``stun.global.calls.mattermost.com``) which is configured as default. This is primarily used to find the public address of the Mattermost server. The only information sent to this service is the IP addresses of clients connecting as no other traffic goes through it. It can be removed in the System Console if you want to provide an ``ICE Host Override`` setting instead.

Troubleshooting
---------------

My audio doesn't work when I join a call
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you can hear the other participants in the call but they can't hear you, select the horizontal dots next to the call end button in the widget. From there, you can check and change your audio output and microphone settings. Select the horizontal dots again to close the menu.

My call is disconnected after a few seconds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is usually a sign that the underlying UDP channel has not been established and the connection times out after ~10 seconds. When the connection has been established correctly an ``rtc connected`` line should appear in the client-side logs (JS console). There isn't a single solution as it depends on your infrastructure/deployment specifics. However, if you're a system or network admin, you may need to open up the UDP port or configure the network accordingly.

I can't screen share using Mattermost desktop on macOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There's a known bug on macOS with some versions of Chrome (which is used by Mattermost desktop). If you've given screen sharing permissions to Mattermost desktop, and are still unable to screen share, do the following:

1. Quit Mattermost.
2. Open Terminal.
3. In terminal, run: ``tccutil reset ScreenCapture Mattermost.Desktop``
4. Restart Mattermost and start a call.
5. Select **Screen share** and give it permissions again.
6. Restart Mattermost again.

If the issue persists please post in the public calls channel.
