:orphan:
:nosearch:

Rate limiting prevents your Mattermost server from being overloaded with too many requests, and decreases the risk and impact of third-party applications or malicious attacks on your server. Configure rate limiting settings by going to **System Console > Environment > Rate Limiting**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: ratelimit-enableratelimiting
  :displayname: Enable rate limiting (Rate Limiting)
  :systemconsole: Environment > Rate Limiting
  :configjson: .RateLimitSettings.Enable
  :environment: MM_RATELIMITSETTINGS_ENABLE

  - **true**: APIs are throttled at the rate specified by the `Maximum queries per second <#maximum-queries-per-second>`__ configuration setting.
  - **false**: **(Default)** API access isn’t throttled.

Enable rate limiting
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+--------------------------------------------------------------------------+
| Enable or disable rate limiting to throttle APIs to a          | - System Config path: **Environment > Rate Limiting**                    |
| specified number of requests per second.                       | - ``config.json`` setting: ``".RateLimitSettings.Enable: false”,``       |
|                                                                | - Environment variable: ``MM_RATELIMITSETTINGS_ENABLE``                  |
| - **true**: APIs are throttled at the rate specified by the    |                                                                          |
|   `Maximum queries per second <#maximum-queries-per-second>`__ |                                                                          |
|   configuration setting.                                       |                                                                          |
| - **false**: **(Default)** API access isn’t throttled.         |                                                                          |
+----------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: ratelimit-maxpersecond
  :displayname: Maximum queries per second (Rate Limiting)
  :systemconsole: Environment > Rate Limiting
  :configjson: .RateLimitSettings.PerSec
  :environment: MM_RATELIMITSETTINGS_PERSEC
  :description: Throttle the API at this number of requests per second when `rate limiting <#enable-rate-limiting>`__ is enabled. Default is **10** requests per second.

Maximum queries per second
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Throttle the API at this number of requests per second when   | - System Config path: **Environment > Rate Limiting**                    |
| `rate limiting <#enable-rate-limiting>`__ is enabled.         | - ``config.json`` setting: ``".RateLimitSettings.PerSec: 10,``           |
|                                                               | - Environment variable: ``MM_RATELIMITSETTINGS_PERSEC``                  |
| Numerical input. Default is **10**.                           |                                                                          |
|                                                               |                                                                          |
| Increase this value to accept more requests each second, and  |                                                                          |
| decrease this value to allow fewer requests.                  |                                                                          |
|                                                               |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: ratelimit-maxburst
  :displayname: Maximum burst size (Rate Limiting)
  :systemconsole: Environment > Rate Limiting
  :configjson: .RateLimitSettings.MaxBurst
  :environment: MM_RATELIMITSETTINGS_MAXBURST
  :description: The maximum number of requests allowed beyond the per second query limit when `rate limiting <#enable-rate-limiting>`__ is enabled. Default is **100** requests.


Maximum burst size
~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+--------------------------------------------------------------------------+
| The maximum number of requests allowed beyond the per second    | - System Config path: **Environment > Rate Limiting**                    |
| query limit when `rate limiting <#enable-rate-limiting>`__      | - ``config.json`` setting: ``".RateLimitSettings.MaxBurst: 100,``        |
| is enabled.                                                     | - Environment variable: ``MM_RATELIMITSETTINGS_MAXBURST``                |
|                                                                 |                                                                          |
| Numerical input. Default is **100**.                            |                                                                          |
|                                                                 |                                                                          |
| Increase this value to allow for more concurrent requests to be |                                                                          |
| handled, and decrease this value to limit this capacity.        |                                                                          |
|                                                                 |                                                                          |
+-----------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: ratelimit-memorystoresize
  :displayname: Memory store size (Rate Limiting)
  :systemconsole: Environment > Rate Limiting
  :configjson: .RateLimitSettings.MemoryStoreSize
  :environment: MM_RATELIMITSETTINGS_MEMORYSTORESIZE
  :description: The maximum number of user sessions connected to the system as determined by vary rate limit settings when `rate limiting <#enable-rate-limiting>`__ is enabled. Default is **10000** sessions.


Memory store size
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| The maximum number of user sessions connected to the system as  | - System Config path: **Environment > Rate Limiting**                      |
| determined by vary rate limit settings when                     | - ``config.json`` setting: ``".RateLimitSettings.MemoryStoreSize: 10000,`` |
| `rate limiting <#enable-rate-limiting>`__ is enabled.           | - Environment variable: ``MM_RATELIMITSETTINGS_MEMORYSTORESIZE``           |
|                                                                 |                                                                            |
| Numerical input. Default is **10000**. Typically set to the     |                                                                            |
| number of users in the system.                                  |                                                                            |
|                                                                 |                                                                            |
| We recommend setting this value to the expected number of       |                                                                            |
| users. A higher value may result in underutilized resources,    |                                                                            |
| and a lower value may result in user sessions/tokens expiring   |                                                                            |
| too frequently.                                                 |                                                                            |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: ratelimit-varybyremoteaddress
  :displayname: Vary rate limit by remote address (Rate Limiting)
  :systemconsole: Environment > Rate Limiting
  :configjson: .RateLimitSettings.VaryByRemoteAddr
  :environment: MM_RATELIMITSETTINGS_VARYBYREMOTEADDR

  - **true**: **(Default)** Rate limit API access by IP address. Recommended when using a proxy.
  - **false**: Rate limiting does not vary by IP address.


Vary rate limit by remote address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| Configure Mattermost to rate limit API access by IP address     | - System Config path: **Environment > Rate Limiting**                      |
| when `rate limiting <#enable-rate-limiting>`__ is enabled.      | - ``config.json`` setting: ``".RateLimitSettings.VaryByRemoteAddr: true,`` |
|                                                                 | - Environment variable: ``MM_RATELIMITSETTINGS_VARYBYREMOTEADDR``          |
| - **true**: **(Default)** Rate limit API access by IP address.  |                                                                            |
|   Recommended when using a proxy.                               |                                                                            |
| - **false**: Rate limiting does not vary by IP address.         |                                                                            |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: ratelimit-varybyuser
  :displayname: Vary rate limit by user (Rate Limiting)
  :systemconsole: Environment > Rate Limiting
  :configjson: .RateLimitSettings.VaryByUser
  :environment: MM_RATELIMITSETTINGS_VARYBYUSER

  - **true**: Rate limit API access by user authentication token. Recommended when using a proxy.
  - **false**: **(Default)** Rate limiting does not vary by user authentication token.

Vary rate limit by user
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

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

.. config:setting:: ratelimit-varybyhttpheader
  :displayname: Vary rate limit by HTTP header (Rate Limiting)
  :systemconsole: Environment > Rate Limiting
  :configjson: .RateLimitSettings.VaryByHeader
  :environment: MM_RATELIMITSETTINGS_VARYBYHEADER
  :description: Configure Mattermost to vary rate limiting API access by the HTTP header field specified. Recommended when you’re using a proxy.

Vary rate limit by HTTP header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| Configure Mattermost to vary rate limiting API access           | - System Config path: **Environment > Rate Limiting**                      |
| by the HTTP header field specified. Recommended when you’re     | - ``config.json`` setting: ``".RateLimitSettings.VaryByHeader: "",``       |
| using a proxy.                                                  | - Environment variable: ``MM_RATELIMITSETTINGS_VARYBYHEADER``              |
|                                                                 |                                                                            |
| - When configuring NGINX, set this to **X-Real-IP**.            |                                                                            |
| - When configuring AmazonELB, set this to **X-Forwarded-For**.  |                                                                            |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
