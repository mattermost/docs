Software and hardware requirements
==================================

This guide outlines minimum software and hardware requirements for deploying Mattermost. Requirements may vary based on utilization and observing performance of pilot projects is recommended prior to scale out.

Deployment overview
-------------------

Please see the :doc:`Application architecture </deployment-guide/reference-architecture/application-architecture>` documentation for a summary of software systems and components whose requirements are described in this document.

Software requirements
---------------------

Client software
~~~~~~~~~~~~~~~

Desktop apps
^^^^^^^^^^^^

.. csv-table::
    :header: "Operating System", "Self-Hosted Technical Requirement", "Cloud Technical Requirement"

    "Windows", "Windows 11+", "Windows 11+"
    "Mac", "macOS 12+", "macOS 12+"
    "Linux", "Ubuntu LTS releases 22.04 or later", "Ubuntu LTS releases 22.04 or later"

Though not officially supported, the Linux desktop app also runs on RHEL/CentOS 7+.

.. note::

    - `*` Integrated Windows Authentication is not supported by Mattermost desktop apps. If you use ADFS we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.

    - The minimum content size is 800 x 600 pixels.

PC web
^^^^^^

.. csv-table::
    :header: "Browser", "Self-Hosted Technical Requirement", "Cloud Technical Requirement"

    "Chrome", "v144+", "v144+"
    "Firefox", "v140+", "v140+"
    "Safari", "v17.4+", "v17.4+"
    "Edge", "v142+", "v142+"

`*` Internet Explorer (IE11) is no longer supported. We recommend using the `Mattermost desktop app <https://mattermost.com/apps/>`_ or another supported browser. See `this forum post <https://forum.mattermost.com/t/mattermost-is-dropping-support-for-internet-explorer-ie11-in-v5-16/7575>`__ to learn more.

Mobile apps
^^^^^^^^^^^

.. csv-table::
    :header: "Operating System", "Technical Requirement"

    "iOS", "iPhone 8+ devices and later with iOS 16.0+"
    "Android", "Android devices with Android 7+"

.. note::

    - `*` Integrated Windows Authentication is not supported by Mattermost mobile apps. If you use ADFS we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.
    - The minimum and target content size is 320 x 460 pixels, matching the available space when the mobile app is opened in Safari on the minimum supported iOS device.
    - The Mattermost mobile app for Android isn't supported on Chromebooks. Access Mattermost using the Chrome web browser, or install the web app as a Progressive Web App (PWA) directly from the browser for an app-like experience with a desktop icon and windowed view.

Mobile web
^^^^^^^^^^

.. csv-table::
    :header: "Browser", "Technical Requirement"

    "iOS", "iOS 16.0+ with Safari 17.4+ or Chrome 144+"
    "Android", "Android 7+ with Chrome 144+"

Email client
^^^^^^^^^^^^

-  *Desktop clients:* Outlook 2010+, Apple Mail version 7+, Thunderbird 38.2+
-  *Web based clients:* Entra ID, Outlook, Gmail, Yahoo, AOL
-  *Mobile clients:* iOS Mail App (iOS 7+), Gmail Mobile App (Android, iOS)

Server software
~~~~~~~~~~~~~~~

Mattermost server operating system
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Ubuntu, Debian Buster, CentOS 6+, CentOS 7+, RedHat Enterprise Linux 7+, Oracle Linux 6+, Oracle Linux 7+.
- Using the Mattermost `Docker deployment <https://github.com/mattermost/docker>`__ on a Docker-compatible operating system (Linux-based OS) is still recommended.

While community support exists for Fedora, FreeBSD, and Arch Linux, Mattermost does not currently include production support for these platforms.

Database software
^^^^^^^^^^^^^^^^^

-  PostgreSQL 14.0+

Amazon Aurora equivalents of PostgreSQL is also supported. Our `Migration Guide <https://docs.mattermost.com/deployment-guide/postgres-migration.html>`__ outlines the steps, tools and support available for migrating from MySQL to PostgreSQL.

.. important::

    - MariaDB v10+ no longer functions as a MySQL drop-in replacement, and it's not supported for Mattermost due to the requirement of MySQL 5.7.12. Prior versions of MariaDB were not officially supported but may have functioned in older Mattermost releases. If you are running MariaDB now, migrating from MariaDB to the MySQL equivalent is recommended.
    - Deployments requiring searching in Chinese, Japanese, and Korean languages require MySQL 5.7.6+ and the configuration of `ngram Full-Text parser <https://dev.mysql.com/doc/refman/5.7/en/fulltext-search-ngram.html>`__. For searching two characters, you will also need to set ``ft_min_word_len`` and ``innodb_ft_min_token_size`` to ``2`` and restart MySQL. See `CJK discussion <https://github.com/mattermost/mattermost/issues/2033#issuecomment-183872616>`__ for details.

Minimum PostgreSQL database support policy
::::::::::::::::::::::::::::::::::::::::::

To make planning easier and ensure your Mattermost deployment remains fast and secure, we are introducing a policy for updating the minimum supported version of PostgreSQL. The oldest supported PostgreSQL version Mattermost supports will match the oldest version supported by the PostgreSQL community. This ensures you benefit from the latest features and security updates.

This policy change takes effect from Mattermost v10.6, where the minimum PostgreSQL version required will be PostgreSQL 13. This aligns with the PostgreSQL community's support policy, which provides 5 years of support for each major version.

.. note::

  Mattermost v10.6 is not an :ref:`Extended Support Release (ESR) <product-overview/release-policy:extended support releases>`. Going forward, this database version support policy will only apply to ESR releases.

When a PostgreSQL version reaches its end of life (EOL), Mattermost will require a newer version starting with the next scheduled ESR release. This means the following future PostgreSQL minimum version increases as follows:

+------------------------------------------------------------+------------------+--------------------------------+
| **Mattermost Version**                                     | **Release Date** | **Minimum PostgreSQL Version** |
+============================================================+==================+================================+
| :ref:`v9.11 ESR <release-v9-11-extended-support-release>`  | 2024-8-15        | 11.x                           |
+------------------------------------------------------------+------------------+--------------------------------+
| :ref:`v10.5 ESR <release-v10.5-extended-support-release>`  | 2025-2-15        | 11.x                           |
+------------------------------------------------------------+------------------+--------------------------------+
| :ref:`v10.6 <release-v10.6-feature-release>`               | 2025-3-15        | 13.x                           |
+------------------------------------------------------------+------------------+--------------------------------+
| :ref:`v10.11 ESR <release-v10.11-extended-support-release>`| 2025-8-15        | 13.x                           |
+------------------------------------------------------------+------------------+--------------------------------+
| v11.7 ESR ``*``                                            | 2026-5-15        | 14.x (EOL 2026-11-12)          |
+------------------------------------------------------------+------------------+--------------------------------+

``*`` Forcasted release version and date.

Customers will have 9 months to plan, test, and upgrade their PostgreSQL version before the new requirement takes effect. This policy aims to provide clarity and transparency so you can align database upgrades with the Mattermost release schedule. Contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_. to discuss your options.

Database Search limitations
:::::::::::::::::::::::::::::

Common limitations:

- Only the initial **1 MB** of the file content is available for search, even though much bigger files can be uploaded.

Search limitations on PostgreSQL:

- Email addresses do not return results.
- Hashtags or recent mentions of usernames containing a dash do not return search results.
- Terms containing a dash return incorrect results as dashes are ignored in the search query.
- Limitations set by `PostgreSQL itself <https://www.postgresql.org/docs/current/textsearch-limitations.html>`_:

  - One of them is: ``The length of a tsvector (lexemes + positions) must be less than 1 megabyte``, which means that, based on the file content, even files with content less than 1 MB won't be searchable if they hit the ``tsvector`` limit of 1 MB.

- If any of the above is an issue, you can :doc:`set up and enable enterprise search </administration-guide/scale/enterprise-search>`.

MySQL Support
::::::::::::::::::::
:doc:`MySQL database support </deployment-guide/server/prepare-mattermost-mysql-database>` is being deprecated starting with Mattermost v11. See the :doc:`PostgreSQL migration </deployment-guide/postgres-migration>` documentation for guidance on migrating from MySQL to PostgreSQL.

- Search limitations on MySQL: Hashtags or recent mentions of usernames containing a dot do not return search results.
- The migration system requires the MySQL database user to have additional `EXECUTE`, `CREATE ROUTINE`, `ALTER ROUTINE` and `REFERENCES` privileges to run schema migrations.
- MariaDB v10+ no longer functions as a MySQL drop-in replacement, and it's not supported for Mattermost due to the requirement of MySQL 5.7.12. Prior versions of MariaDB were not officially supported but may have functioned in older Mattermost releases. If you are running MariaDB now, migrating from MariaDB to the MySQL equivalent is recommended.
- Deployments requiring searching in Chinese, Japanese, and Korean languages require MySQL 5.7.6+ and the configuration of `ngram Full-Text parser <https://dev.mysql.com/doc/refman/5.7/en/fulltext-search-ngram.html>`__. For searching two characters, you will also need to set ``ft_min_word_len`` and ``innodb_ft_min_token_size`` to ``2`` and restart MySQL. See `CJK discussion <https://github.com/mattermost/mattermost/issues/2033#issuecomment-183872616>`__ for details.

.. important::

    MySQL 8.0.22 contains an `issue with JSON column types <https://bugs.mysql.com/bug.php?id=101284>`__ changing string values to integers which is preventing Mattermost from working properly. Users are advised to avoid this database version.

In MySQL 8.0.4, the default authentication plugin was changed from ``mysql_native_password`` to ``caching_sha2_password``. Therefore, you will need to enable ``mysql_native_password`` by adding the following entry in your MySQL configuration file:

  .. code-block:: text

   [mysqld]
   default-authentication-plugin=mysql_native_password

In MySQL 8, the default collation changed to ``utf8mb4_0900_ai_ci`` (https://dev.mysql.com/doc/mysqld-version-reference/en/optvar-changes-8-0.html). Therefore, if you update your MySQL installation to version 8, you'll need to convert your database tables to use the new default collation:

.. code-block:: sql

   ALTER TABLE table_name CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

If this change isn't made, tables in the database may end up having different collations which will cause errors when executing queries.

In MySQL versions 8.0.0 - 8.0.11 ``ADMIN`` is a `reserved keyword <https://dev.mysql.com/doc/refman/8.0/en/keywords.html>`_, which is why our requirement for MySQL is version 8.0.12.

MySQL 8.0.22 contains an `issue with JSON column types <https://bugs.mysql.com/bug.php?id=101284>`__ changing string values to integers which is preventing Mattermost from working properly. Users are advised to avoid this database version.

Hardware requirements
---------------------

Usage of CPU, RAM, and storage space can vary significantly based on user behavior. These hardware recommendations are based on traditional deployments and may grow or shrink depending on how active your users are.

Moreover, memory requirements can be driven by peak file sharing activity. Recommendation is based on default 50 MB maximum file size, which can be :ref:`adjusted from the System Console <administration-guide/configure/environment-configuration-settings:maximum file size>`. Changing this number may change memory requirements.

For deployments larger than 2,000 users, it is recommended to use the Mattermost open source load testing framework to simulate usage of your system at full scale: `https://github.com/mattermost/mattermost-load-test-ng <https://github.com/mattermost/mattermost-load-test-ng>`__.

Mattermost supports any 64-bit x86 processor architecture.

Hardware requirements for team deployments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most small to medium Mattermost team deployments can be supported on a single server with the following specifications based on registered users:

-  1 - 1,000 users - 1 vCPU/cores, 2 GB RAM
-  1,000 - 2,000 users - 2 vCPUs/cores, 4 GB RAM

.. _hardware-sizing-for-enterprise:

Hardware requirements for enterprise deployments (multi-server)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Scale requirements
^^^^^^^^^^^^^^^^^^

For Enterprise Edition deployments with a multi-server setup, see :doc:`our scaling guide </administration-guide/scale/scaling-for-enterprise>`.

It is highly recommended that pilots are run before enterprise-wide deployments in order to estimate full scale usage based on your specific organizational needs. You can use the Mattermost open source load testing framework to simulate usage of your system: `https://github.com/mattermost/mattermost-load-test-ng <https://github.com/mattermost/mattermost-load-test-ng>`__.

Mattermost's :doc:`performance monitoring </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>` tools can be used for detailed performance measurements and to inspect the running system to ensure sizing and installation is correct.

System requirements
^^^^^^^^^^^^^^^^^^^

For Enterprise Edition deployments with a multi-server setup, we highly recommend the following systems to support your Mattermost deployment:

- Prometheus to track system health of your Mattermost deployment, through :doc:`performance monitoring feature </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>` available in Mattermost Enterprise.
- Grafana to visualize the system health metrics collected by Prometheus with the :doc:`performance monitoring feature </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>`. Grafana 5.0.0 and later is recommended.
- Elasticsearch to support highly efficient database searches in a cluster environment. Elasticsearch v7.17+ is supported, and Elasticsearch v8.x or AWS OpenSearch is recommended from Mattermost v9.11. :doc:`Learn more </administration-guide/scale/enterprise-search>`.
- AWS S3 or any S3-compatible service. Mattermost is compatible with object storage systems which implement the S3 API. You can also use local storage or a network drive using NFS. Learn more about file storage configuration options :ref:`in our documentation <administration-guide/configure/environment-configuration-settings:file storage>`.
