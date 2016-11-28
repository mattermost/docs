Install Ubuntu Server (x64) 14.04 LTS
=====================================

1. Set up 3 machines with Ubuntu 14.04 with 2GB of RAM or more. The
   servers will be used for the Proxy, Mattermost (must be
   x64), and Database.

   -  **Optional:** You can also use a **1 machine setup** (Proxy, Mattermost and Database on one machine) or a **2 machine setup** (Proxy and Mattermost on one machine, Database on another) depending on your data center standards.

2. Make sure the system is up to date with the most recent security
   patches.

   -  ``sudo apt-get update``
   -  ``sudo apt-get upgrade``
