..  _requirements:

Software & Hardware Requirements
================================

This guide outlines minimum software and hardware requirements for deploying Mattermost. Requirements may vary based on utilization and observing performance of pilot projects is recommended prior to scale out. 

.. contents::
    :backlinks: top

Deployment Overview
-------------------

Please see the `Mattermost Deployment Overview <http://docs.mattermost.com/deployment/deployment.html>`__ documentation for a summary of software systems whose requirements are described in this document. 

.. figure:: ../images/network.PNG
   :alt: image
`View Mattermost Network Diagram <https://github.com/mattermost/docs/blob/master/source/images/network.PNG>`__

Software Requirements
---------------------

Client Software
~~~~~~~~~~~~~~~

PC Web Experience
^^^^^^^^^^^^^^^^^

-  PC: Windows 7, Windows 8, Windows 10 with IE 11*, Chrome 43+, Firefox 52+, and Edge 40+ (or EdgeHTML v15+)
-  Mac: OS 10 (Safari 9, Chrome 43+)
-  Linux: Arch 4.0.0 (Chrome 43+)

`*` IE 11 Compatibility View is not supported. 

Mobile App Experience
^^^^^^^^^^^^^^^^^^^^^

-  iPhone 4s and later with iOS 9+
-  Android devices with Android 5+

Mobile Web Experience
^^^^^^^^^^^^^^^^^^^^^

-  iPhone 4s and higher (Safari on iOS 9+, Chrome 43+)
-  Android 5 and higher (Chrome 43+)

Email Client
^^^^^^^^^^^^

-  *Desktop clients:* Outlook 2010+, Apple Mail version 7+, Thunderbird 38.2+
-  *Web based clients:* Office 365, Outlook, Gmail, Yahoo, AOL
-  *Mobile clients:* iOS Mail App (iOS 7+), Gmail Mobile App (Android, iOS)

Server Software
~~~~~~~~~~~~~~~

Mattermost Server Operating System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Ubuntu 14.04, Ubuntu 16.04, Debian Jessie, CentOS 6.6+, CentOS 7.1+, RedHat Enterprise Linux 6.6+, RedHat Enterprise Linux 7.1+, Oracle Linux 6.6+, Oracle Linux 7.1+
- Using Mattermost `Docker image <https://docs.mattermost.com/install/prod-docker.html>`_ on a Docker-compatible operating system (Linux-based OS is still recommended)

While community support exists for Fedora, FreeBSD and Arch Linux, Mattermost does not currently include production support for these platforms.

.. note::
  Please ensure that the directory you place your Mattermost installation in isn't a mounted SAN/NAS volume. This would have a negative performance impact.

Database Software
^^^^^^^^^^^^^^^^^

-  MySQL 5.6, 5.7, 8 (Please see note below on MySQL 8 support)
-  PostgreSQL 9.4+
-  Amazon Aurora MySQL 5.6+

Deployments requiring searching in Chinese, Japanese and Korean languages require MySQL 5.7.6+ and the configuration of `ngram Full-Text parser <https://dev.mysql.com/doc/refman/5.7/en/fulltext-search-ngram.html>`__. For searching two characters, you will also need to set ``ft_min_word_len`` and ``innodb_ft_min_token_size`` to ``2`` and restart MySQL. See `CJK discussion <https://github.com/mattermost/mattermost-server/issues/2033#issuecomment-183872616>`__ for details.

Search limitations on PostgreSQL:

- Email addresses do not return results.
- Hashtags or recent mentions of usernames containing a dash do not return search results.
- Terms containing a dash return incorrect results as dashes are ignored in the search query.
- If any of the above is an issue, you can either enable the `Elasticsearch (E20) feature <https://docs.mattermost.com/deployment/elasticsearch.html>`__ or install MySQL instead.

Search limitations on MySQL:

- Hashtags or recent mentions of usernames containing a dot do not return search results.

**MySql 8 Support**:

In MySQL 8.0.4, the deafult authentication plugin was changed from ``mysql_native_password`` to ``caching_sha2_password`` (https://mysqlserverteam.com/mysql-8-0-4-new-default-authentication-plugin-caching_sha2_password/). If you are using MySQL 8.0.4+, you will need to enable ``mysql_native_password`` by adding the following entry in your MySQL configuration file:

  .. code-block:: text
   
   [mysqld]
   default-authentication-plugin=mysql_native_password

Hardware Requirements
---------------------

Usage of CPU, RAM and storage space can vary significantly based on user behavior. For deployments larger than 500 users, it's highly recommended usage patterns in a small pilot deployment representative of your large organization are observed before rolling out the full scale service.

Hardware Sizing for Team Deployments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most small to medium Mattermost team deployments can be supported on a single server with the following specifications based on registered users:

-  250-500 users - 2 vCPUs/cores, 4 GB RAM, and 45-90 GB storage
-  500-1,000 users - 4 vCPUs/cores, 8 GB RAM, and 90-180 GB storage
-  1,000-2,000 users - 4-8 vCPUs/cores, 16-32 GB RAM, and 180-360 GB storage

Notes:

1. Memory requirements are largely driven by peak file sharing activity. Recommendation is based on default 50 MB max file size, which can be adjusted from the System Console. Changing this number may change memory requirements. 
2. Larger deployments should estimate utilization based on pilots representative of full scale usage. 
3. Storage recommendation is based on storing 3 years of archives with moderate file sharing.
4. Solid state drives (SSD) can be used in place of disk storage for higher concurrency.

.. _hardware-sizing-for-enterprise:

Mattermost Load Test Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Mattermost Enterprise Edition deployments, an open source load testing framework is available to simulate usage: https://github.com/mattermost/mattermost-load-test

The system can be used to place a deployment under estimated user activity load and to log in and inspect the running system to ensure sizing and installation is correct. 

Mattermost's `performance monitoring <https://docs.mattermost.com/deployment/metrics.html>`_ tools can be used to look into detailed behavior. 

Hardware Sizing for Enterprise Deployments (Multi-Server)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost can also be configured with a redundant, highly available, highly scalable mode to support large organizations. The following is an example that can be scaled up or down in size:

For enterprise deployments of 10,000-20,000 registered users with moderate usage and a peak of 2,000-4,000 concurrent users, the following hardware deployment configurations are recommended:

**Proxy Server** 

- One server with 4-8 vCPUs/cores, 16-32 GB RAM.
- Minimum 4 GB SSD (solid state drive) storage for the binary and related files.
- (Optional) Add one additional identical server for high availability mode, where one Mattermost server can be disabled or upgraded without interrupting service quality. Second server should be sized to carry the full load of the first server so performance does not degrade when the first server is taken offline.

**Mattermost Server** (1 to 2 depending on level of redundancy and high availability required) 

- One server with 4-8 vCPUs/cores, 16-32 GB RAM.
- Minimum 4 GB SSD (solid state drive) storage for the binary and related files.
- (Optional) Add one additional identical server for high availability mode, where one Mattermost server can be disabled or upgraded without interrupting service quality. Second server should be sized to carry the full load of the first server so performance does not degrade when the first server is taken offline. Note: The high availability option is available only by `contacting the Enterprise Edition team <https://about.mattermost.com/contact/>`_.

**Network Attached Storage** 

- One NAS server with 4-8 TB of storage (based on moderate storage of 10 MB per user per month times 20,000 users times 3 years of history, times 2x safety factor) or sized appropriately for your desired usage requirements. For high availability it is recommended you select a NAS server offering redundancy.

**Database Server** (2 recommended for redundancy) 

- One database server with 8-16 vCPUs/cores, 16-32 GB memory.
- Minimum 100 GB SSD (solid state drive) storage for the binary and related files.
- (Recommended) Add one identical database server to setup a Master-Slave configuration where the master can failover to slave with minimal disruption to service.

**Notes:**

- Regular hard drives can be used in place of solid-state hard drives if having top performance is not a priority. If using a mix of HDD and SSD drives, the greatest performance gain would come from using SSD in the database server.

Alternate Storage Calculations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As an alternative to recommended storage sizing above, you can forecast your own storage usage. Begin with a Mattermost server approximately 600 MB to 800 MB in size including operating system and database, then add the multiplied product of:

-  Estimated storage per user per month (see below), multipled by 12 months in a year
-  Estimated mean average number of users in a year
-  A 1-2x safety factor

**Estimated storage per user per month**

File usage per user varies significantly across industries. The below benchmarks are recommended:

-  **Low usage teams** (1-5 MB/user/month) 
	- Primarily use text-messages and links to communicate. Examples would include software development teams that heavily use web-based document creation and management tools, and therefore rarely upload files to the server.

-  **Medium usage teams** (5-25 MB/user/month) 
	- Use a mix of text-messages as well as shared documents and images to communicate. Examples might include business teams that may commonly drag and drop screenshots, PDFs and Microsoft Office documents into Mattermost for sharing and review.

-  **High usage teams** - (25-100 MB/user/month) 
	- Heaviest utlization comes from teams uploading a high number of large files into Mattermost on a regular basis. Examples include creative teams who share and store artwork and media with tags and commentary in a pipeline production process.

*Example:* A 30-person team with medium usage (5-25 MB/user/month) with a safety factor of 2x would require between 300 MB (30 users \* 5 MB \* 2x safety factor) and 1500 MB (30 users \* 25 MB \* 2x safety factor) of free space in the next year.

It's recommended to review storage utilization at least quarterly to ensure adequate free space is available.
