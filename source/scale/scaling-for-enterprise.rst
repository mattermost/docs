Scaling for Enterprise 
======================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Mattermost is designed to scale from small teams hosted on a single server to large enterprises running in cluster-based, highly available deployment configurations.

- Mattermost supports any 64-bit x86 processor architecture
- **Databases supported**: PostgreSQL, Amazon RDS for PostgreSQL
- **Storage supported**: Amazon S3 or a local filestore

Server requirements vary based on usage and we highly recommend that you run a pilot before an enterprise-wide deployment in order to estimate full scale usage based on your specific organizational needs. 

Available reference architectures
---------------------------------

The following reference architectures are available as recommended starting points for your self-hosted Mattermost deployment.

[Neil] Expand on this to explain what the user count means (i.e. are we stating concurrent or supported)

- `Up to 100 users </scale/scale-to-100-users.rst>`__
- `Up to 1000 users </scale/scale-to-1000-users.rst>`__
- `Up to 15000 users </scale/scale-to-15000-users.rst>`__
- `Up to 25000 users </scale/scale-to-25000-users.rst>`__
- `Up to 50000 users </scale/scale-to-50000-users.rst>`__
- `Up to 70000 users </scale/scale-to-70000-users.rst>`__
- `Up to 79000 users </scale/scale-to-79000-users.rst>`__
- `Up to 88000 users </scale/scale-to-88000-users.rst>`__

Testing methodology and updates
------------

[Neil] Lay out what we did in testing these archs (specifically which version of MM was used in the tests, when we plan to publish updated lists etc). 

Share the data profile (e.g. DB size in users, posts). Share the “action” profile (login, channel switch, posts created etc).

Mattermost load testing tools
-----------------------------

Mattermost provides a set of tools written in Go to help profiling Mattermost under heavy load, simulating real-world usage of a server installation at scale. The `Mattermost Load Test Tools <https://github.com/mattermost/mattermost-load-test-ng>`__ estimates the maximum number of concurrently active users the target system supports, and enables you to control the load to generate.

Visit the `Mattermost Load Test Tools <https://github.com/mattermost/mattermost-load-test-ng/tree/master/docs>`__ documentation on GitHub for details on getting started with the tools, and visit `GDoc <https://godoc.org/github.com/mattermost/mattermost-load-test-ng>`__ for code-specific documentation.