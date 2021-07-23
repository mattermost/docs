Shared Channels (Experimental) (E20)
====================================

Shared Channels bring people together from multiple Mattermost installations, such as teams collaborating with external partners, and customers using multiple Mattermost instances in a federated architecture. 

Mattermost System Admins use slash commands to establish secure connections between Mattermost instances, then invite secured connections to shared channels.

Shared Channels behave like regular channels, offering the same user experience and functionality as Public and Private channels. All members using secure connections, including local members and remote members, can `send and receive messages <https://docs.mattermost.com/help/messaging/sending-messages.html#sending-and-receiving-messages>`__, `use emojis <https://docs.mattermost.com/help/messaging/emoji.html>`__ to react to messages, `share files <https://docs.mattermost.com/help/messaging/attaching-files.html>`__, and `search message history <https://docs.mattermost.com/help/getting-started/searching.html#searching-for-message-contents>`__. Content is synchronized in real-time across all participating Mattermost instances. 

A channel’s permissions and access continues to be governed by each server separately. Channel moderation permissions can be applied to a shared channel, and be in effect on the local Mattermost server, while not being in effect on a remote Mattermost server.

Setting Up Shared Channels
--------------------------

The process of sharing channels involves the following three steps:

1. System Admins must enable Shared Channels functionality for their Mattermost instance. See our `Configuration Settings <https://docs.mattermost.com/configure/configuration-settings.html#enable-shared-channels-experimental>`__ documentation for details.

2. System Admins `use a slash command <https://docs.mattermost.com/help/messaging/executing-commands.html>`__ to establish a secure and trusted relationship between other Mattermost Enterprise Edition E20 instances. This process involves creating a password-protected, encrypted invitation, creating a strong decryption password, then sending the invitation and password to the System Admin of a remote Mattermost instance. We strongly recommend that you share an invitation separately from its password to ensure that, if the message were compromised, someone doesn't have all of the data necessary to take action.

3. The remote System Admin receiving the invitation uses a slash command to `accept the invitation <#accepting-a-secure-connection-invitation>`_. 

Once a trusted relationship is established between Mattermost servers, System Admins can `share specific Public or Private channels <#sharing-channels-with-secure-connections>`_ with secure connections.

.. note:: 

    - System Admins can only create secure connections with other Mattermost Enterprise Edition E20 instances, and can only share channels with secured connections by typing slash commands into the Message box of any channel.
    - System Admins must use Mattermost to generate a password-protected encrypted invitation code. However, sending secure connection invitations is not completed using Mattermost. System Admins must have an independent way to extend the secure connection invitation, such as by email.
    - A channel shared by a host organization cannot be shared from the receiving organization to another organization. Organizations are prevented from sharing a channel originating from another organization. 

Creating a Secure Connection Invitation
---------------------------------------

System Admins can use the following slash command to create a secure connection invitation:

``/secure-connection create --name <--displayname> --password``

For example:

``/secure-connection create --name “AcmeUS” --displayname “AcmeUSA” --password examplepassword``

This slash command creates an invitation consisting of a password-protected AES 256-bit encrypted code blob for a remote Mattermost entity known locally as ``AcmeUS`` with a password of ``examplepassword``. Within Mattermost, this shared connection displays to the local System Admin based on the ``name`` and ``displayname`` provided. 

Extending the Invitation
~~~~~~~~~~~~~~~~~~~~~~~~

1. Copy the invitation code blob in the System message, then send the code blob and the decryption password to the remote Mattermost System Admin you want to securely connect with.

2. Ensure that the remote Mattermost instance can access your workspace URL listed in the System message.

Removing a Secure Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following slash command to remove a secure connection from your Mattermost instance:

``/secure-connection remove --connectionID``

For example:

``/secure-connection remove --connectionID``

This slash command severs the trust relationship between the local Mattermost server and a remote Mattermost server based on its ``connectionID``, and removes the secure connection from all shared Mattermost channels.

Reviewing Secure Connection Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following slash command to review the current status of all secure connections established for your Mattermost instance:

``/secure-connection status``

Status details include:

- Connection ID
- Connection URL
- Description
- Invite accepted (Yes/No)
- Online (Yes/No)
- Last ping timestamp (UTC)

Accepting a Secure Connection Invitation
----------------------------------------

Use the following slash command to accept a secure connection invitation from a remote Mattermost instance:

``/secure-connection accept --name --displayname --password --invite [code blob]``

For example:

``/secure-connection accept --name AcmeUS --displayname “AcmeUSA” --password examplepassword --invite [code-blob]``

This slash command accepts a secure connection invitation from AcmeUS.

Sharing Channels with Secure Connections
----------------------------------------

Within a specific Public or Private channel, use the following slash command to invite secure connections:

``/share-channel invite --connectionID <--readonly>``

You can extend an invitation that permits remote members to participate in the channel based on their channel and member permissions. 

Alternatively, you can extend a read-only invitation to a secure connection by appending the optional ``--readonly`` parameter to this command. Remote members can’t post or reply to messages within shared read-only channels.

.. tip:: 

    To convert a read-only shared channel to an participation channel, remove the original secured connection from the channel, then re-extend an invitation to that secure connection while omitting the optional ``--readonly`` parameter.

For example:

``/share-channel invite --connectionID``
 
This slash command invites the shared connection to the current channel based on its connection ID.

.. tip:: 
    See `Reviewing Secure Connection Status <#reviewing-secure-connection-status>`_ to find the connectionID for a shared connection.

Uninviting Shared Channel Connection from a Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Within a specific channel, use the following slash command to uninvite a secure connection:

``/share-channel uninvite --connectionID``

This slash command removes a secure connection from the current channel based on its connection ID. The channel continues to function for local users as expected, and the secure connection may continue to be invited to other shared channels. 

Removing All Secure Connections from a Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Within a specific channel, use the following slash command to remove all secure connections: 

``/share-channel unshare``

This slash command removes all secure connections from the current channel. Secure connections may continue to be invited to other shared channels. 

While unsharing a shared channel stops synchronizing the channel with the other Mattermost server, the channel continues to function for local users as expected. 

.. note:: 
    A System message notifies System Admins that the channel is no longer shared.

Reviewing Secure Connections in Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following slash command to review the status of all secure connections within the current shared channel:

``/share-channel status``

Status details include:
- Connection ID
- Connection URL
- Description
- Read only channel (True/False)
- Invite accepted (Yes/No)
- Online (Yes/No)
- Last ping timestamp (UTC)

Frequently Asked Questions
---------------------------

Why is this feature in beta?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature is in beta while we recruit customer testing partners. This feature has been tested by Mattermost QA, but as we build the interface for managing shared channels, we want to work with System Admins to build the most optimal experience.

Are special characters supported in secure connection names?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. ``--name`` can include periods, hyphens, and/or underscores. You must surround ``--name`` using quotation marks (“ “) when the value contains spaces.

What happens if two Mattermost instances contain different emojis?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In cases where one Mattermost instance has different emojis than another instance, emoji text displays in place of a missing emoji image. 

Is a Display Name required for all secure connections?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. ``--displayname`` is optional. When omitted, ``--name`` is displayed and used instead.

Do connection interruptions affect message synchronization?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. A System message is posted in the channel visible to all channel members when message synchronization is interrupted for more than five minutes. 

What happens if two secure connections share the same usernames?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In cases where members share the same usernames across Mattermost secure connections, usernames on the local server instance are appended with the secure connection name of the remote server.

For example, if multiple members named John Smith exist after two Mattermost instances establish a secure connection with one another, all remote John Smith members include their Secure Connection ID following their username to help differentiate members across multiple Mattermost instances.
