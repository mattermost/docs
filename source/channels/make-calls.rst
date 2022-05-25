Make calls (beta)
=================

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
  
Mattermost calls is built-in voice calling and screen sharing functionality, available in Channels, and is currently in beta. It’s available and on by default in Mattermost Cloud. For self-hosted deployments it's available as a plugin and needs to be enabled.

You can:

- Start or join a call in any channel, group message, or direct message that you’re a part of.
- Use Calls on desktop and mobile apps in addition to web browsers.
- Share screen (not available on mobile), raise hands, chat in a thread, and even switch between products in the Mattermost suite (ie. Channels, Boards, and Playbooks) while on a call.

Limitations
-----------

- In Mattermost Cloud, up to eight participants in each channel can join a call.
- In Mattermost self-hosted, the recommended maximum number of participants per server is 200.

Configuration
-------------

For Mattermost self-hosted customers, the calls plugin needs to be enabled in the System Console. Additional configuration is also available.

To start a call, select **Start call** in the channel header. Anyone in the channel can join a call. If someone from outside of the organization wants to join a call they are not currently able to, unless they're provided with a guest account and added to the channel.

Each call has a unique URL 
Open the channel, group message, or direct message where you’d like to have a call and then select **Start Call** on the top-right corner.

How do I start a call on the mobile app?
----------------------------------------

Tap the channel header and select **Start Call** from the list menu.

How can I copy the call link to paste in other places such as calendar invite?
------------------------------------------------------------------------------



Call is disconnected after a few seconds and I can't transmit voice nor hear anything.

This is usually a sign that the underlying UDP channel has not been established and the connection timeouts after ~10 seconds. When the connection has been established correctly an `rtc: connected` line should appear in the client-side logs (JS Console).
FAQ



How long is a link valid?
The call link is valid for long as the channel is not archived or deleted.

Does the link change per call?
The link is unique to each channel and does not change between calls. 

Can someone join the call if they’re not a channel member?
No. When someone clicks on that link, Mattermost first checks if that person has permission to access the channel. So if for any reason they aren't allowed to access the channel (non-registered user, private channel but not a member, archived user etc.) then they will not be able to join the call.

Can I password-protect a call?
No. Any member with sufficient permission to access the channel will be able to join the call.

What does call data flow look like?
Client sends data to Mattermost server which then broadcasts to all call participants. There's a back and forth of messaging to initialize a call (it's called signaling in WebRTC jargon) which happens on WebSocket (TLS secured). Data is exchanged between the clients and MM and back. Clients don't connect directly to each other but always go through MM which means addresses are not leaked outside the server.

Is there encryption?
Media (audio/video) is encrypted using security standards as part of WebRTC. It's mainly a combination of DTLS and SRTP. It's not e2e encrypted in the sense that in the current design all media needs to go through MM which acts as a media router and has complete access to it. Media is then encrypted back to the clients so it's secured during transit. In short: only the participant clients and the MM server have access to unencrypted call data.

What are the potential performance impacts?
Database load should be minimal as there's nothing special happening there. Overall instance load however will be affected, especially CPU usage, growing as a function of the number of participants product the number of active tracks (unmuted participants and users sharing their screen). Screen sharing has the highest impact on both CPU and bandwidth. The latter can be more easily estimated as the audio/video bitrates are constrained and predictable (around 40-60Kbps for each audio track and up to 1Mbps per screen track).

Are there any third-party services involved?
STUN servers are configurable on the plugin itself. The default one used is:

- stun:stun.global.calls.mattermost.com:3478

Depending on the setup they may not be necessary (e.g. if running a single instance and providing a ICE Host Override). 

No media goes through STUN servers, the only sensitive information that passes through is the client's (and server's) public IP address.


