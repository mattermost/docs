WIP: Developer Toolkit 
======================

High Level Overview
-------------------

This document is a work-in-progress document summarizing developer toolkit capabilities currently under development.

The Mattermost Developer Toolkit is meant to give community and in-house customer developers the power to deeply integrate with and extend Mattermost server and clients to better meet their requirements. We are still in the early stages of architecting the toolkit but below is a non-definitive list of what we'd like to offer.

Features of the Developer Toolkit
---------------------------------

1. The ability to build Go 1.8 server plugins to hook directly into server events (think new post events, user update events, etc.), have some sort of database access (possibly access to certain tables, ability to create new tables) and to add custom endpoints to extend the Mattermost REST API
2. The ability to build webapp client plugins to override existing UI components (replace posts with your custom component, use your own video service etc.), modify/extend some client driver to interact with custom server API endpoints, and to add whole new UI views in pre-determined places
3. The ability to build plugins similar to the webapp but for React Native apps for iOS and Android
4. A system or architecture to combine the above plugins into one easy-to-share and easy-to-install package
5. A market or directory to find official and/or certified by Mattermost plugins and a process to get your plugin certified
6. A guide or system to allow the embedding of Mattermost into other apps as a chat service
7. Mattermost HTTP REST APIv4 allowing for much more powerful server interaction
8. Webhooks and slash commands to allow easy, low-effort extension and integration 
9. All the documentation required to support the use and building of all of the above

Example Uses
------------

Some examples of the things we will use the plugin architecture for are: 
1. Building common integrations such as Jira, GitHub, etc and including them as default integrations for Mattermost
2. Redesigning the current video and audio calling to use the plugin architecture, and offering it as one of many video and audio calling solutions
