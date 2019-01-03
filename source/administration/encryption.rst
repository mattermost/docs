Encryption Options
=======================

Mattermost provides encryption-in-transit and encryption-at-rest capabilities. This page guides you through setting up appropriate encryption security.

Encryption is not required for GDPR, although it can be used as an additional safeguard against data breach.

.. contents::
  :backlinks: top
  :local:

Encryption-in-transit
-----------------------

Mattermost supports TLS encryption including AES-256 with 2048-bit RSA on all data transmissions between Mattermost client applications and the Mattermost server. You may either set up TLS on the Mattermost Server or install a proxy such as NGINX and set up TLS on the proxy. Refer to our `configuration guide for more details <https://docs.mattermost.com/install/config-tls-mattermost.html>`__.

Connections to Active Directory/LDAP can `optionally be secured with TLS or stunnel <https://docs.mattermost.com/administration/config-settings.html#id11>`__.

Encryption-at-rest
-----------------------

Database
~~~~~~~~~~~~~~~~~~~~~~~

Encryption-at-rest is available for messages via hardware and software disk encryption solutions applied to the Mattermost database, which resides on its own server within your infrastructure. Encryption options at the disk level are documented both for `MySQL <https://www.percona.com/blog/2016/04/08/mysql-data-at-rest-encryption/>`__ and `PostgreSQL <https://www.postgresql.org/docs/8.1/static/encryption-options.html>`__.

File Storage
~~~~~~~~~~~~~~~~~~~~~~~

For local storage or storage via Minio, encryption-at-rest is available for files stored via hardware and software disk encryption solutions applied to the server.

For Amazon’s proprietary S3 system, encryption-at-rest is available via `server-side encryption with Amazon S3-managed keys <https://docs.mattermost.com/administration/config-settings.html#enable-server-side-encryption-for-amazon-s3>`__ in Enterprise Edition E20.
