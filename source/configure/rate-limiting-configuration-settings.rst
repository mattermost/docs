:orphan:
:nosearch:

Rate limiting prevents your Mattermost server from being overloaded with too many requests, and decreases the risk and impact of third-party applications or malicious attacks on your server. Configure rate limiting settings by going to **System Console > Environment > Rate Limiting**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

Enable rate limiting
~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+----------------------------------------------------------------+--------------------------------------------------------------------------+
| Enable or disable rate limiting to throttle APIs to a          | - System Config path: **Environment > Rate Limiting**                    |
| specified number of requests per second.                       | - ``config.json`` setting: ``".RateLimitSettings.Eanble: false”,``       |
|                                                                | - Environment variable: ``MM_RATELIMITSETTINGS_ENABLE``                  |
| - **true**: APIs are throttled at the rate specified by the    |                                                                          |
|   `Maximum queries per second <#maximum-queries-per-second>`__ |                                                                          |
|   configuration setting.                                       |                                                                          |
| - **false**: **(Default)** API access isn’t throttled.         |                                                                          |
+----------------------------------------------------------------+--------------------------------------------------------------------------+

Maximum queries per second
~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Throttle the API at this number of requests per second when   | - System Config path: **Environment > Rate Limiting**                    |
| `rate limiting <#enable-rate-limiting>`__ is enabled.         | - ``config.json`` setting: ``".RateLimitSettings.PerSec: 10,``           |
|                                                               | - Environment variable: ``MM_RATELIMITSETTINGS_PERSEC``                  |
| Numerical input. Default is **10**.                           |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Maximum burst size
~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+--------------------------------------------------------------------------+
| The maximum number of requests allowed beyond the per second    | - System Config path: **Environment > Rate Limiting**                    |
| query limit when `rate limiting <#enable-rate-limiting>`__      | - ``config.json`` setting: ``".RateLimitSettings.MaxBurst: 100,``        |
| is enabled.                                                     | - Environment variable: ``MM_RATELIMITSETTINGS_MAXBURST``                | 
|                                                                 |                                                                          |
| Numerical input. Default is **100**.                            |                                                                          |
+-----------------------------------------------------------------+--------------------------------------------------------------------------+

Memory store size
~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| The maximum number of user sessions connected to the system as  | - System Config path: **Environment > Rate Limiting**                      |
| determined by vary rate limit settings when                     | - ``config.json`` setting: ``".RateLimitSettings.MemoryStoreSize: 10000,`` |
| `rate limiting <#enable-rate-limiting>`__ is enabled.           | - Environment variable: ``MM_RATELIMITSETTINGS_MEMORYSTORESIZE``           |
|                                                                 |                                                                            |
| Numerical input. Default is **10000**. Typically set to the     |                                                                            |
| number of users in the system.                                  |                                                                            |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+

Vary rate limit by remote address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| Configure Mattermost to rate limit API access by IP address     | - System Config path: **Environment > Rate Limiting**                      |
| when `rate limiting <#enable-rate-limiting>`__ is enabled.      | - ``config.json`` setting: ``".RateLimitSettings.VaryByRemoteAddr: true,`` |
|                                                                 | - Environment variable: ``MM_RATELIMITSETTINGS_VARYBYREMOTEADDR``          |
| - **true**: **(Default)** Rate limit API access by IP address.  |                                                                            |
|   Recommended when using a proxy.                               |                                                                            |
| - **false**: Rate limiting does not vary by IP address.         |                                                                            |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+

Vary rate limit by user
~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| Configure Mattermost to rate limit API access by authentication | - System Config path: **Environment > Rate Limiting**                      |
| token or not when `rate limiting <#enable-rate-limiting>`__     | - ``config.json`` setting: ``".RateLimitSettings.VaryByUser: false,``      |
| is enabled.                                                     | - Environment variable: ``MM_RATELIMITSETTINGS_VARYBYUSER``                |   
|                                                                 |                                                                            |
| - **true**: Rate limit API access by user authentication token. |                                                                            |
|   Recommended when using a proxy.                               |                                                                            |
| - **false**: **(Default)** Rate limiting does not vary by user  |                                                                            |
|   authentication token.                                         |                                                                            |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+

Vary rate limit by HTTP header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| Configure Mattermost to vary rate limiting API access           | - System Config path: **Environment > Rate Limiting**                      |
| by the HTTP header field specified. Recommended when you’re     | - ``config.json`` setting: ``".RateLimitSettings.VaryByHeader: "",``       |
| using a proxy.                                                  | - Environment variable: ``MM_RATELIMITSETTINGS_VARYBYHEADER``              |  
|                                                                 |                                                                            |
| - When configuring NGINX, set this to **X-Real-IP**.            |                                                                            | 
| - When configuring AmazonELB, set this to **X-Forwarded-For**.  |                                                                            |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+