Cloud Dedicated
===============

.. include:: ../_static/badges/ent-cloud-dedicated.rst
  :start-after: :nosearch:

Mattermost Cloud Dedicated is designed for larger organizations with higher demands for performance, scalability, customizability, and compliance looking to offload operational overhead and focus on more business-critical tasks.

Your own private Mattermost instance running :ref:`Mattermost Enterprise <about/editions-and-offerings:mattermost enterprise>` is a Kubernetes cluster hosted and managed by Mattermost that runs on dedicated cloud infrastructure, where resources are exclusively available for your organization.

Reference architecture
----------------------

.. image:: ../images/mattermost-cloud-dedicated-reference-architecture.png
  :alt: An architecture diagram showing the components of the Mattermost Cloud Dedicated solution.

Available features
------------------

Zero-downtime upgrades
~~~~~~~~~~~~~~~~~~~~~~

Mattermost releases biweekly updates and leverages recurring maintenance windows to keep your instance up-to-date with new stable or beta features behind feature flags, fix security issues, and ensure the overall reliability and performance of your environment. Maintenance windows are announced in advance on https://status.mattermost.com/

Additional support options, including quicker response times, dedicated support personnel, and stronger service level agreements (SLAs), are also available.

Disaster Recovery
~~~~~~~~~~~~~~~~~

Mattermost Cloud Dedicated supports data failover to a secondary region/site should the primary instance experiences an unrecoverable outage with guaranteed recovery times.

Mattermost supports a **multi-AZ (availability zones)** strategy in the same site/region.

Daily backups of the database, object storage, and high availability clusters are captured and retained for 30 days.

In addition, highly available observability tools with automated alerting, long-term metrics, and logs retention are retained for a duration of 1 year, or longer, if requred.

Security
~~~~~~~~

You have access to all the resources required to run the Mattermost application with the highest security standards, including data encryption at rest and in transit.

Your pre-configured cluster is secure by default, based on industry best practices including Data encryption at rest and in transit, TLS certificates life cycle management, and automatic security updates.

Mattermost maintains control over network and security policies, including `encryption <#encryption>`__, database, data, object storage, backup schedules, and compliance certifications. 

Authentication and authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost offers advanced security and authentication options for integrating with corporate directories, including :doc:`Active Directory/LDAP </onboard/ad-ldap>`, Okta, OneLogin, :doc:`SAML </onboard/sso-saml>`, :doc:`Google </onboard/sso-google>`, :doc:`EntraID </onboard/sso-office>`, and :doc:`OpenID </onboard/sso-openidconnect>`.

Secure networking
~~~~~~~~~~~~~~~~~~

Mattermost Cloud Dedicated supports :doc:`IP filtering </manage/cloud-ip-filtering>` through CIDR-based IP ranges, providing flexibility for system administrators to include various authorized IPs or IP ranges for seamless access control. Users attempting to access the workspace from IPs outside defined ranges are restricted from entry. Cloud system admins can :ref:`configure IP filtering <manage/cloud-ip-filtering:configure ip filtering>` through their Mattermost System Console.

Encryption
~~~~~~~~~~~

Mattermost provides encryption-in-transit and encryption-at-rest capabilities. Mattermost supports :doc:`TLS encryption </install/setup-tls>`, including AES-256 with 2048-bit RSA on all data transmissions, between Mattermost client applications and the Mattermost server. You may either set up TLS on the Mattermost Server or :doc:`install a proxy such as NGINX </install/proxy-to-mattermost-transport-encryption>`, and set up TLS on the proxy.

Connections to :doc:`Active Directory/LDAP </onboard/ad-ldap>` can :ref:`optionally be secured with TLS or stunnel <configure/authentication-configuration-settings:ad/ldap port>`.

Connections to calls are secured with a combination of:

- TLS: The existing WebSocket channel is used to secure the signaling path.
- DTLS v1.2 (mandatory): Used for initial key exchange. Supports ``TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`` and ``TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`` algorithms.
- SRTP (mandatory): Used to encrypt all media packets (i.e. those containing voice or screen share). Supports ``AEAD_AES_128_GCM`` and ``AES128_CM_HMAC_SHA1_80`` algorithms.

Gossip encryption (experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost supports encryption of cluster data in-transit when using the gossip protocol. See our :ref:`gossip encryption <deploy/encryption-options:gossip encryption (experimental)>` documentation for details.

The encryption uses AES-256 by default, and it is not configurable. However, it is possible to manually set the value in the ``Systems`` table for the ``ClusterEncryptionKey`` row. A key is a byte array converted to ``base64``. It can be set to a length of 16, 24, or 32 bytes to select ``AES-128``, ``AES-192``, or ``AES-256`` respectively.

SMTP
~~~~

Email sent from Mattermost Cloud Dedicated uses XXX, and the connection to XXX is encrypted. See our :doc:`SMTP </configure/smtp-email>` documentation for setup details.

Audit and observability
~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud Dedicated provides access to :doc:`audit and system logs </manage/logging>` generated by the application. 

Bring your own cloud
~~~~~~~~~~~~~~~~~~~~~

With Bring Your Own Cloud (BYOC), use your own cloud infrastructure instead of using the Mattermost-managed infrastructure to manage your Mattermost instance through Mattermost command and control while keeping your data in your own cloud.

Consider using BYOC if:

- You use Amazon Web Service (AWS) or Azure.
- You're an Enterprise customer with a committed deal with Mattermost.
- You have strict regulatory requirements or special compliance requirements, BYOC may will be the best option for you.
- You require the visibility of all traffic within any VPC you operate in, or need frequent auditing capabilities.
- You're looking for fine-grained network control. BYOC only requires specific network access (non-internet accessible) for Mattermost (for example, service management or troubleshooting) to deploy and manage Mattermost instance. This allows you to customize your network to meet any internal requirements or requirements of your customers.
- Take advantage of cost savings plans, committed use discounts, or other strategies to save on compute and storage infrastructure costs related to your Mattermost instance.

Contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_ to discuss this option in more detail.

Customization
~~~~~~~~~~~~~~

Approved plugins developed and/or tested by Mattermost are supported and available in the `Mattermost Marketplace <https://mattermost.com/marketplace/>`_. Custom plugins and integrations outside of Mattermost Marketplace aren’t currently supported.

Migrate from a self-hosted instance
------------------------------------

See our :ref:`workspace migration <manage/cloud-data-export:migrate from self-hosted to cloud>` documentation to learn more about migrating from a self-hosted to a Mattermost Cloud instance.