Redis
=====

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Redis is an open-source, in-memory data structure store used as a database, cache, message broker, and streaming engine. Mattermost uses Redis as an external cache to improve performance at scale. When properly configured, Redis can help support Mattermost installations with more than 100,000 users by providing improved performance through efficient caching.

Deployment guide
----------------

Deploying Redis with Mattermost includes the following 2 steps: `setting up the Redis server <#set-up-a-redis-server>`__, and `configuring Redis in Mattermost <#configure-redis-in-mattermost>`__.

Set up a Redis server
~~~~~~~~~~~~~~~~~~~~~

1. Download and install the latest release of `Redis 7.x <https://redis.io/download/>`_. See the Redis documentation for installation details specific to your operating system.

2. Configure Redis appropriately for your environment. Ensure that Redis is secured and accessible only by trusted systems.

3. For high availability deployments, consider setting up Redis in a cluster configuration for improved reliability and performance.

Configure Redis in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow these steps to configure Mattermost to use your Redis server:

1. Go to **System Console > Environment > Cache**.
2. Set **Cache Type** to ``redis`` to enable the Redis-specific settings.
3. Set the Redis server connection details:

  a. Enter **Redis Address** for the Redis server you set up earlier (e.g., ``redis.example.com:6379``).
  b. (Optional) Enter **Redis Password** if your Redis server requires authentication.
  c. (Optional) Enter **Redis Database** to specify which Redis database to use (-1 by default, which uses Redis's default database).

4. Save your configuration and restart the Mattermost server.

Alternatively, you can configure Redis in the ``config.json`` file:

.. code-block:: json

    "CacheSettings": {
        "CacheType": "redis",
        "RedisAddress": "redis.example.com:6379",
        "RedisPassword": "",
        "RedisCachePrefix": "",
        "RedisDB": -1,
        "DisableClientCache": false
    }

Deploy with AWS ElastiCache
---------------------------

For enterprise-scale deployments, AWS ElastiCache for Redis provides a fully managed Redis service that simplifies deployment, operation, and scaling. 

When deploying Mattermost with AWS ElastiCache:

1. Create an ElastiCache for Redis instance, choosing Redis OSS version 7.1 or later.
2. Based on load testing results, we recommend starting with a ``cache.m7g.2xlarge`` instance for deployments supporting over 100,000 users.
3. Configure your Mattermost server to connect to the ElastiCache endpoint.
4. Monitor CPU utilization closely, as Redis is single-threaded and performance bottlenecks are typically CPU-bound rather than memory-bound.

Performance considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~

When using Redis with Mattermost, consider the following performance insights:

- Current load tests indicate that memory usage of Redis is relatively low, with CPU being the primary bottleneck because Redis is single-threaded.
- When planning your Redis deployment, use CPU utilization as the primary metric for scaling decisions.

Implementation details
----------------------

Mattermost uses the `rueidis <https://github.com/redis/rueidis>`_ library instead of the more popular `go-redis <https://github.com/redis/go-redis>`_, primarily because rueidis offers more performance optimizations out of the box, including:

- Automatic pipelining of concurrent queries
- Client-side caching
- Additional performance tuning options like MaxFlushDelay

The primary implementation files include:

- ``platform/services/cache/provider.go`` - Contains the library initialization code
- ``platform/services/cache/redis.go`` - Contains the cache interface implementation

Frequently asked questions (FAQ)
--------------------------------

Do I need to use Redis?
~~~~~~~~~~~~~~~~~~~~~~~

While Redis is not required for smaller Mattermost deployments, it is highly recommended for large-scale installations.
- If your installation has more than 100K users, Redis is highly recommended. Redis significantly improves performance by reducing database load and optimizing common operations.
- If your installation has less than 100K users, Redis is not recommended.

It is suggested to keep an eye on the ``sum(rate(mattermost_cache_mem_invalidation_total[5m]))`` metric which indicates the rate of cache invalidations happening. A single cache invalidation will send a message across your HA cluster to all nodes, leading to database calls from all of them. So the metric, combined with the number of nodes in your cluster should be used to determine when is the right time to use Redis.

For example, if you have more than 10 nodes in your cluster, and the rate of invalidations goes beyond 10, then you should definitely start considering adding Redis.

Should I install Redis on the same machine as Mattermost Server?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For production deployments, we recommend running Redis on a separate machine from the Mattermost server. This separation allows for better resource allocation and improved system reliability.

What Redis metrics should I monitor?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When running Redis with Mattermost, monitor the following metrics:

- CPU utilization (primary bottleneck)
- Memory usage
- Connected clients
- Cache hit ratio
- Operation latency
- Mattermost's ``mattermost_db_cache_time`` Grafana metric with labels of ``cache_name`` and ``operation``, which can be used to further monitor the performance of Redis
