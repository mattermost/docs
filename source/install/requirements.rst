..  _requirements:

Software & Hardware Requirements
================================

--------------

Deployment Overview
-------------------

Please see `Mattermost Deployment
Overview <http://docs.mattermost.com/deployment/deployment.html>`__ for
a summary of components listed here.

.. figure:: ../images/network.PNG
   :alt: image
`View Mattermost Network Diagram <../images/network.PNG>`__

Software Requirements
---------------------

Client Software
~~~~~~~~~~~~~~~

PC Web Experience
^^^^^^^^^^^^^^^^^

-  PC: Windows 7, Windows 8, Windows 10 with (IE 11*, Chrome 43+, Firefox 38+, and Edge)
-  Mac: OS 10 (Safari 9, Chrome 43+)
-  Linux: Arch 4.0.0 (Chrome 43+)

* IE 11 Compatiblity View is not supported. 

Mobile App Experience
^^^^^^^^^^^^^^^^^^^^^

-  iPhone 4s and later with iOS 9+
-  Android devices with Android 4.40+

Mobile Web Experience
^^^^^^^^^^^^^^^^^^^^^

-  iPhone 4s and higher (Safari on iOS 9+, Chrome 43+)
-  Android 5 and higher (Chrome 43+)

Email Client
^^^^^^^^^^^^

-  *Desktop clients:* Outlook 2010+, Apple Mail version 7+, Thunderbird
   38.2+
-  *Web based clients:* Office 365, Outlook, Gmail, Yahoo, AOL
-  *Mobile clients:* iOS Mail App (iOS 7+), Gmail Mobile App (Android,
   iOS)

Server Software
~~~~~~~~~~~~~~~

Mattermost Server Operating System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Ubuntu 14.04, Debian Jessie, CentOS 6.6+, CentOS 7.1+, RedHat
   Enterprise Linux 6.6+, RedHat Enterprise Linux 7.1+, Oracle Linux
   6.6+, Oracle Linux 7.1+

The Mattermost roadmap does not currently include production support for
Fedora, FreeBSD or Arch Linux.

Database Software
^^^^^^^^^^^^^^^^^

-  MySQL 5.6+
-  PostgreSQL 9.4+

Deployments requiring searching in Chinese, Japanese and Korean
languages require MySQL 5.7.6+ and the configuration of `ngram Full-Text
parser <https://dev.mysql.com/doc/refman/5.7/en/fulltext-search-ngram.html>`__.
See `CJK
discussion <https://github.com/mattermost/platform/issues/2033#issuecomment-183872616>`__
for details.

Hardware Requirements
---------------------

Usage of CPU, RAM and storage space can vary significantly based on user
behavior. For deployments larger than 500 users, it's highly recommended
usage patterns in a small pilot deployment representative of your large
organization is observed before rolling out the full scale service.

Hardware Sizing for Team Deployments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most small to medium Mattermost team deployments can be supported on a
single server with the following specifications based on registered
users:

-  250-500 users - 2 CPUs (2GHz or higher) with Hyper-Threading, 4GB
   RAM, and 45-90GB HDD storage
-  500-1,000 users - 4 CPUs (2.8GHz or higher) with Hyper-Threading, 8GB
   RAM, and 90-180GB HDD storage
-  1,000-2,000 users - 4-8 CPUs (2.8GHz or higher) with Hyper-Threading,
   16-32GB RAM, and 180-360GB HDD storage

Notes:

1. Larger deployments should estimate utilization based on pilots
   represenative of full scale usage.
2. Storage recommendation is based on storing 3 years of archives with
   moderate file sharing.
3. Solid-state storage drives (SDD) can be used in place of disk storage
   for higher concurrency.
4. Team deployments assume registered users are divided into teams of
   10-100.

Hardware Sizing for Enterprise Deployments (Multi-Server)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost can also be configured with a redundant, highly available,
highly scalable mode to support large organizations. The following is an
example that can be scaled up or down in size:

For enterprise deployments of 10,000-20,000 registered users with
moderate usage and a peak of 2,000-4,000 concurrent users, the following
hardware deployment configurations are recommended:

**Proxy Server** 

- One server with 4-8 CPU cores supporting Hyper-Threading, 16-32 GB, SSD drive with at least 4GB of storage 
- (Optional) Add one additional identical server for high availability mode, where one Mattermost server can be disabled or upgraded without interrupting service quality). Second server should be sized to carry the full load of the first server so performance does not degrade when the first server is taken offline.

**Mattermost Server** (1 to 2 depending on level of redundancy and high
availability required) 

- One server with 4-8 CPU cores supporting Hyper-Threading, 16-32GB memory, SSD drive with at least 4GB storage. 
- (Optional) Add one additional identical server for high availability mode, where one Mattermost server can be disabled or upgraded without interrupting service quality). Second server should be sized to carry the full load of the first server so performance does not degrade when the first server is taken offline. Note: The high availability option is available only by `contacting the Enterprise Edition team <https://about.mattermost.com/contact/>`_.

**Network Attached Storage** 

- One NAS server with 3.6-7.2TB of storage (based on moderate storage of 10MB per user per month times 20,000 users times 3 years of history, times 2x safety factor) or sized appropriately for your desired usage requirements. For high availability it is recommended you select a NAS server offering redundancy.

**Database Server** (2 recommended for redundancy) 

- One database server with 8-16 CPU cores supporting Hyper-Threading, 16-32GB memory, SSD drive with at least 100GB of storage.
- (Recommended) Add one identical database server to setup a Master-Slave configuration where the master can failover to slave with minimal disruption to service.

**Notes:**

- Regular hard drives can be used in place of solid-state hard drives if having top performance is not a priority. If using a mix of HDD and SSD drives, the greatest performance gain would come from using SDD in the database server.

Alternate Storage Calculations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As an alternative to recommended storage sizing above, you can forecast
your own storage usuage. Begin with a Mattermost server approximately
600 MB to 800 MB in size including operating system and database, then
add the multiplied product of:

-  Estimated storage per user per month (see below), multipled by 12
   months in a year
-  Estimated mean average number of users in a year
-  A 1-2x safety factor

**Estimated storage per user per month**

File usage per user varies significantly across industries. The below
benchmarks are recommended:

-  **Low usage teams** (1-5 MB/user/month) 
	- Primarily use text-messages and links to communicate. Examples would include software development teams that heavily use web-based document creation and management tools, and therefore rarely upload files to the server.

-  **Medium usage teams** (5-25 MB/user/month) 
	- Use a mix of text-messages as well as shared documents and images to communicate. Examples might include business teams that may commonly drag and drop screenshots, PDFs and Microsoft Office documents into Mattermost for sharing and review.

-  **High usage teams** - (25-100 MB/user/month) 
	- Heaviest utlization comes from teams uploading a high number of large files into Mattermost on a regular basis. Examples include creative teams who share and store artwork and media with tags and commentary in a pipeline production process.

*Example:* A 30-person team with medium usage (5-25 MB/user/month) with
a safety factor of 2x would require between 300 MB (30 users \* 5 MB \*
2x safety factor) and 1500 MB (30 users \* 25 MB \* 2x safety factor) of
free space in the next year.

It's recommended to review storage utilization at least quarterly to
ensure adequate free space is available.
