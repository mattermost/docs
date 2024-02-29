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

The following reference architectures are available as recommended starting points for your self-hosted Mattermost deployment, where user counts refer to the number of concurrent users for a given deployment. The number of concurrent numbers is commonly lower than the total number of user accounts.

- `Up to 100 users </scale/scale-to-100-users.rst>`__
- `Up to 1000 users </scale/scale-to-1000-users.rst>`__
- `Up to 15000 users </scale/scale-to-15000-users.rst>`__
- `Up to 25000 users </scale/scale-to-25000-users.rst>`__
- `Up to 50000 users </scale/scale-to-50000-users.rst>`__
- `Up to 70000 users </scale/scale-to-70000-users.rst>`__
- `Up to 79000 users </scale/scale-to-79000-users.rst>`__
- `Up to 88000 users </scale/scale-to-88000-users.rst>`__

Testing methodology and updates
--------------------------------

All tests were executed with the custom load test tool built by the Mattermost development teams to determine supported users for each deployment size. Over time, this guide will be updated with new deployment sizes, deployment architectures, and newer versions of the Mattermost Server will be tested using an ESR. 

At a high level, each deployment size was fixed (Mattermost server node count/sizing, database reader/writer count/sizing), and unbounded tests were used to report the maximum numbers of concurrent users the deployment can support. Each test included populated PostgreSQL v14 databases and a post table history of 100 million posts, ~3000 users, 20 teams, and ~720000 channels to provide a test simulation of a production Mattermost deployment. 

Tests were defined by configuration of the actions executed by each simulated user (and the frequency of these actions) where the coordinator metrics define a health system under load. Tests were performed using the Mattermost v8.1 extended support release (ESR). Elasticsearch and job servers weren't used. All tests wtih more than a single app node had an NGINX proxy running in front of them.

Full testing methodology, configuration, and setup is available. Sign up at `Mattermost Community <https://community.mattermost.com/>`__ and join the `Developers: Performance channel <https://community.mattermost.com/core/channels/developers-performance>`__.

Mattermost load testing tools
-----------------------------

Mattermost provides a set of tools written in Go to help profiling Mattermost under heavy load, simulating real-world usage of a server installation at scale. The `Mattermost Load Test Tool <https://github.com/mattermost/mattermost-load-test-ng>`__ estimates the maximum number of concurrently active users the target system supports, and enables you to control the load to generate.

Visit the `Mattermost Load Test Tool <https://github.com/mattermost/mattermost-load-test-ng/tree/master/docs>`__ documentation on GitHub for details on getting started with the tools, and visit `the Go documentation <https://pkg.go.dev/github.com/mattermost/mattermost-load-test-ng>`__ for code-specific documentation details.