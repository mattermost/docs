Collaborate with audio and video
================================

Mattermost offers native real-time chat, self-hosted audio calls, and screen sharing within your own network, enabling secure, effective team communication and collaboration.

For video conferencing, Mattermost integrates seamlessly with leading providers, giving users the flexibility to easily transition from chat to video:

- **Pexip**: An enterprise-grade video conferencing solution with advanced security features, tailored for secure and scalable video collaboration.
- :doc:`Zoom </integrate/zoom-interoperability>`: A widely used, cloud-based video conferencing platform known for its ease of use and wide range of collaboration tools, including screen sharing and breakout rooms.
- `Webex <https://mattermost.com/marketplace/webex-cloud/>`_: A comprehensive video conferencing solution designed for enterprise-grade security, offering features like file sharing, virtual backgrounds, and meeting recordings.
- :doc:`Microsoft Teams </integrate/microsoft-teams-interoperability>`: A cloud-based collaboration platform that integrates with Microsoft 365, with text, voice, video, and file-sharing features.

With always-online calls and screen sharing, Mattermost ensures that communications remain uninterrupted, even during maintenance or outages, and scales effortlessly to meet your team’s growing needs, safeguarding the integrity of mission-critical operations.

Conference call plan comparison
-------------------------------

The following chart outlines the various conferencing features supported across Mattermost plans, including on mobile devices:

+---------------------------------+----------+------------------+----------------+
| **Mattermost Calls**            | **Free** | **Professional** | **Enterprise** |
+=================================+==========+==================+================+
| 1:1 audio call                  | X        | X                | X              |
+---------------------------------+----------+------------------+----------------+
| Audio conference call           |          | X                | X              |
+---------------------------------+----------+------------------+----------------+
| Screen share                    | X        | X                | X              |
+---------------------------------+----------+------------------+----------------+
| Chat/messaging during calls     | X        | X                | X              |
+---------------------------------+----------+------------------+----------------+
| Search chat history post-call   | X        | X                | X              |
+---------------------------------+----------+------------------+----------------+
| Host controls                   |          | X                | X              |
+---------------------------------+----------+------------------+----------------+
| Call recording                  |          |                  | X              |
+---------------------------------+----------+------------------+----------------+
| Call transcription              |          |                  | X              |
+---------------------------------+----------+------------------+----------------+
| Live captioning                 |          |                  | X              |
+---------------------------------+----------+------------------+----------------+
| AI call summarization           |          |                  | X              |
+---------------------------------+----------+------------------+----------------+
| Advanced security controls      |          |                  | X              |
+---------------------------------+----------+------------------+----------------+
| Redundancy                      |          |                  | X              |
+---------------------------------+----------+------------------+----------------+
| Scaleable calls and screenshare |          |                  | X              |
+---------------------------------+----------+------------------+----------------+

Conference call provider comparison
-----------------------------------

Here’s a breakdown of the conference call features supported across the available call providers on Mattermost:

+--------------------------------+-----------+----------+--------------+-----------+
| **Feature**                    | **Pexip** | **Zoom** | **Microsoft  | **Webex** |
|                                |           |          | Teams**      |           |
+================================+===========+==========+==============+===========+
| Video conferencing             | X         | X        | X            | X         |
+--------------------------------+-----------+----------+--------------+-----------+
| Audio conferencing             | X         | X        | X            | X         |
+--------------------------------+-----------+----------+--------------+-----------+
| Screen share                   | X         | X        | X            | X         |
+--------------------------------+-----------+----------+--------------+-----------+
| Chat/messaging during calls    | X         | X        | X            | X         |
+--------------------------------+-----------+----------+--------------+-----------+
| Cloud recording calls          | X         | X        | X            | X         |
+--------------------------------+-----------+----------+--------------+-----------+
| Self-hosted video meetings     | X         |          |              | X         |
+--------------------------------+-----------+----------+--------------+-----------+
| On-premise recording calls     | X         |          |              | X         |
+--------------------------------+-----------+----------+--------------+-----------+
| Virtual backgrounds            | X         | X        | X            | X         |
+--------------------------------+-----------+----------+--------------+-----------+
| Custom layouts for video calls | X         | X        | X            | X         |
+--------------------------------+-----------+----------+--------------+-----------+
| End-to-end encryption          | X         | X        | X            | X         |
+--------------------------------+-----------+----------+--------------+-----------+
| SIP support                    | X         | X        | X            | X         |
+--------------------------------+-----------+----------+--------------+-----------+

.. note::

    - Webex is community supported and not maintained by Mattermost. Please see the `GitHub repository <https://github.com/mattermost-community/mattermost-plugin-webex#readme>`_ for the latest releases and documentation. 
    - Community supported integrations are not available to Cloud deployments of Mattermost.