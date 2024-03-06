Encryption options
==================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Mattermost provides encryption-in-transit and encryption-at-rest capabilities. This page guides you through setting up appropriate encryption security.

Encryption is not required for GDPR, although it can be used as an additional safeguard against data breach.

.. contents:: On this page
  :backlinks: top
  :local:

Encryption-in-transit
---------------------

Mattermost supports TLS encryption including AES-256 with 2048-bit RSA on all data transmissions between Mattermost client applications and the Mattermost server. You may either set up TLS on the Mattermost Server or install a proxy such as NGINX and set up TLS on the proxy. Refer to our `configuration guide for more details </install/config-tls-mattermost.html>`__.

Connections to Active Directory/LDAP can `optionally be secured with TLS or stunnel </configure/configuration-settings.html#ad-ldap-port>`__.

Connections to calls are secured with a combination of:

  - TLS: The existing WebSocket channel is used to secure the signaling path.
  - DTLS v1.2 (mandatory): Used for initial key exchange. Supports ``TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`` and ``TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`` algorithms.
  - SRTP (mandatory): Used to encrypt all media packets (i.e. those containing voice or screen share). Supports ``AEAD_AES_128_GCM`` and ``AES128_CM_HMAC_SHA1_80`` algorithms.

Gossip encryption (experimental)
--------------------------------

In a High Availability mode, Mattermost supports encryption of cluster data in-transit when using the gossip protocol.  

The encryption uses AES-256 by default, and it is not configurable. However, it is possible to manually set the value in the ``Systems`` table for the ``ClusterEncryptionKey`` row. A key is a byte array converted to base64. It can be set to a length of 16, 24, or 32 bytes to select AES-128, AES-192, or AES-256 respectively.

Encryption-at-rest
------------------

Database
~~~~~~~~

Encryption-at-rest is available for messages via hardware and software disk encryption solutions applied to the Mattermost database, which resides on its own server within your infrastructure. See the `PostgreSQL <https://www.postgresql.org/docs/10/encryption-options.html>`__ database documentation for details on encryption options at the disk level.

File storage
~~~~~~~~~~~~~

For local storage or storage via Minio, encryption-at-rest is available for files stored via hardware and software disk encryption solutions applied to the server.

For Amazon’s proprietary S3 system, encryption-at-rest is available via `server-side encryption with Amazon S3-managed keys </configure/configuration-settings.html#enable-server-side-encryption-for-amazon-s3>`__ in Mattermost enterprise-badge.
