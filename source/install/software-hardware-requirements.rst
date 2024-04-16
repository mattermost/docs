Software and hardware requirements
==================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This guide outlines minimum software and hardware requirements for deploying Mattermost. Requirements may vary based on utilization and observing performance of pilot projects is recommended prior to scale out.

Deployment overview
-------------------

Please see the :doc:`Mattermost Deployment Overview </deploy/deployment-overview>` documentation for a summary of software systems whose requirements are described in this document.

.. image:: ../images/network-diagram.svg
   :alt: Mattermost network diagram shows how the components can be deployed. Includes optional configurations for scaling for larger enterprise organizations.
   :class: bg-white

Software requirements
---------------------

Client software
~~~~~~~~~~~~~~~

Desktop apps
^^^^^^^^^^^^

.. csv-table::
    :header: "Operating System", "Self-Hosted Technical Requirement", "Cloud Technical Requirement"

    "Windows", "Windows 10+", "Windows 10+"
    "Mac", "macOS 11+", "macOS 11+"
    "Linux", "Ubuntu LTS releases 18.04 or later", "Ubuntu LTS releases 18.04 or later"

Though not officially supported, the Linux desktop app also runs on RHEL/CentOS 7+.

.. note::

    - `*` Integrated Windows Authentication is not supported by Mattermost desktop apps. If you use ADFS we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.

    - The minimum content size is 769 x 600 pixels. When the width is 768 pixels or less, the desktop app switches to mobile view. When the height is below 600 pixels, screen elements may become misplaced.

PC web
^^^^^^

.. csv-table::
    :header: "Browser", "Self-Hosted Technical Requirement", "Cloud Technical Requirement"

    "Chrome", "v120+", "v120+"
    "Firefox", "v115+", "v115+"
    "Safari", "v16.2+", "v16.2+"
    "Edge", "v120+", "v120+"

`*` Internet Explorer (IE11) is no longer supported. We recommend using the `Mattermost desktop app <https://mattermost.com/apps/>`_ or another supported browser. See `this forum post <https://forum.mattermost.com/t/mattermost-is-dropping-support-for-internet-explorer-ie11-in-v5-16/7575>`__ to learn more.

Mobile apps
^^^^^^^^^^^

.. csv-table::
    :header: "Operating System", "Technical Requirement"

    "iOS", "iPhone 5s devices and later with iOS 12.4+"
    "Android", "Android devices with Android 7+"

.. note::

    - `*` Integrated Windows Authentication is not supported by Mattermost mobile apps. If you use ADFS we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.
    - The minimum and target content size is 320 x 460 pixels, matching the available space when the mobile app is opened in Safari on the minimum supported iOS device.

Mobile web
^^^^^^^^^^

.. csv-table::
    :header: "Browser", "Technical Requirement"

    "iOS", "iOS 12.4+ with Safari 16.2+ or Chrome 112+"
    "Android", "Android 7+ with Chrome 112+"

Email client
^^^^^^^^^^^^

-  *Desktop clients:* Outlook 2010+, Apple Mail version 7+, Thunderbird 38.2+
-  *Web based clients:* Office 365, Outlook, Gmail, Yahoo, AOL
-  *Mobile clients:* iOS Mail App (iOS 7+), Gmail Mobile App (Android, iOS)

Server software
~~~~~~~~~~~~~~~

Mattermost server operating system
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Ubuntu 18.04, Debian Buster, CentOS 6+, CentOS 7+, RedHat Enterprise Linux 7+, Oracle Linux 6+, Oracle Linux 7+.
- Using the Mattermost `Docker deployment <https://github.com/mattermost/docker>`__ on a Docker-compatible operating system (Linux-based OS) is still recommended.

While community support exists for Fedora, FreeBSD, and Arch Linux, Mattermost does not currently include production support for these platforms.

Database software
^^^^^^^^^^^^^^^^^

-  PostgreSQL 11.0+
-  MySQL 5.7.12, 8.0.12+ (see note below on MySQL 8 support)

Amazon Aurora equivalents of both PostgreSQL and MySQL are also supported.

MariaDB v10+ no longer functions as a MySQL drop-in replacement, and it's not supported for Mattermost due to the requirement of MySQL 5.7.12. Prior versions of MariaDB were not officially supported but may have functioned in older Mattermost releases. If you are running MariaDB now, migrating from MariaDB to the MySQL equivalent is recommended.

Deployments requiring searching in Chinese, Japanese, and Korean languages require MySQL 5.7.6+ and the configuration of `ngram Full-Text parser <https://dev.mysql.com/doc/refman/5.7/en/fulltext-search-ngram.html>`__. For searching two characters, you will also need to set ``ft_min_word_len`` and ``innodb_ft_min_token_size`` to ``2`` and restart MySQL. See `CJK discussion <https://github.com/mattermost/mattermost/issues/2033#issuecomment-183872616>`__ for details.

Search limitations on PostgreSQL:

- Email addresses do not return results.
- Hashtags or recent mentions of usernames containing a dash do not return search results.
- Terms containing a dash return incorrect results as dashes are ignored in the search query.
- If any of the above is an issue, you can either enable the :doc:`Elasticsearch feature </scale/elasticsearch>` or install MySQL instead.

Search limitations on MySQL:

- Hashtags or recent mentions of usernames containing a dot do not return search results.
- The migration system requires the MySQL database user to have additional `EXECUTE`, `CREATE ROUTINE`, `ALTER ROUTINE` and `REFERENCES` privileges to run schema migrations.

MySQL 8 Support
^^^^^^^^^^^^^^^^

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

Moreover, memory requirements can be driven by peak file sharing activity. Recommendation is based on default 50 MB maximum file size, which can be :ref:`adjusted from the System Console <configure/environment-configuration-settings:maximum file size>`. Changing this number may change memory requirements.

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

For Enterprise Edition deployments with a multi-server setup, see :doc:`our scaling guide </scale/scaling-for-enterprise>`.

It is highly recommended that pilots are run before enterprise-wide deployments in order to estimate full scale usage based on your specific organizational needs. You can use the Mattermost open source load testing framework to simulate usage of your system: `https://github.com/mattermost/mattermost-load-test-ng <https://github.com/mattermost/mattermost-load-test-ng>`__.

Mattermost's :doc:`performance monitoring </scale/performance-monitoring>` tools can be used for detailed performance measurements and to inspect the running system to ensure sizing and installation is correct.

System requirements
^^^^^^^^^^^^^^^^^^^

For Enterprise Edition deployments with a multi-server setup, we highly recommend the following systems to support your Mattermost deployment:

- Prometheus to track system health of your Mattermost deployment, through :doc:`performance monitoring feature </scale/performance-monitoring>` available in Mattermost Enterprise.
- Grafana to visualize the system health metrics collected by Prometheus with the :doc:`performance monitoring feature </scale/performance-monitoring>`. Grafana 5.0.0 and later is recommended.
- Elasticsearch to support highly efficient database searches in a cluster environment. Elasticsearch 7.x is supported. :doc:`Learn more here </scale/elasticsearch>`.
- MinIO or AWS S3. Mattermost is compatible with object storage systems which implement the S3 API. Other S3-compatible systems may work, but are not officially supported. Learn more about file storage configuration options :ref:`in our documentation <configure/environment-configuration-settings:file storage>`.