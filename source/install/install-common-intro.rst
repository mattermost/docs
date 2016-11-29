A complete Mattermost installation consists of 3 major components: a proxy server, a database server, and the Mattermost server. You can install all components on 1 machine, or you can install each component on its own machine. If you have only 2 machines, then install the proxy and the Mattermost server on one machine, and install the database on the other machine.

The Mattermost server must be installed on a 64-bit machine, but the database and proxy can be on 32-bit machines. For the database, you can install either MySQL or ProstgreSQL. The proxy is NGINX.

After all the components are installed, some configuration is required. You can set up email notifications, SSL, TSL, and HTTP/2. For more information about configuring, see :ref:`config-mattermost`.
