Environment configuration settings
==================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: common-config-settings-notation.rst
    :start-after: :nosearch:

Both self-hosted and Cloud admins can access the following configuration settings in **System Console > Environment**. Self-hosted admins can also edit the ``config.json`` file as described in the following tables. 

- `Web server <#web-server>`__
- `Database <#database>`__
- `Elasticsearch <#elasticsearch>`__
- `File Storage <#file-storage>`__
- `Image Proxy <#image-proxy>`__
- `SMTP <#smtp>`__
- `Push Notification Server <#push-notification-server>`__
- `High Availability <#high-availability>`__
- `Rate Limiting <#rate-limiting>`__
- `Logging <#logging>`__
- `Session Lengths <#session-lengths>`__
- `Performance Monitoring <#performance-monitoring>`__
- `Developer <#developer>`__
- `config. json-only settings <#config-json-only-settings>`__

----

Web server
----------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: web-server-configuration-settings.rst
    :start-after: :nosearch:

----

Database
--------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: database-configuration-settings.rst
    :start-after: :nosearch:

----

Elasticsearch
-------------

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

.. include:: elasticsearch-configuration-settings.rst
    :start-after: :nosearch:

----

File storage
------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: file-storage-configuration-settings.rst
    :start-after: :nosearch:

----

Image proxy
-----------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: image-proxy-configuration-settings.rst
    :start-after: :nosearch:

----

SMTP
----

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: smtp-configuration-settings.rst
    :start-after: :nosearch:

----

Push notification server
------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: push-notification-server-configuration-settings.rst
    :start-after: :nosearch:

----

High availability
-----------------

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

.. include:: high-availability-configuration-settings.rst
    :start-after: :nosearch:

----

Rate limiting
-------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: rate-limiting-configuration-settings.rst
    :start-after: :nosearch:

----

Logging
--------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: logging-configuration-settings.rst
    :start-after: :nosearch:

----

Session lengths
---------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: session-lengths-configuration-settings.rst
    :start-after: :nosearch:

----

Performance monitoring
----------------------

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

.. include:: performance-monitoring-configuration-settings.rst
    :start-after: :nosearch:

----

Developer
---------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: developer-mode-configuration-settings.rst
    :start-after: :nosearch:

config.json-only settings
-------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. config:setting:: disable-customer-portal-requests
  :displayname: Disable customer portal requests
  :systemconsole: N/A
  :configjson: .CloudSettings.Disable
  :environment: MM_CLOUDSETTINGS_DISABLE
  :description: Enable or disable server requests to the Mattermost Customer Portal.

    - **true**: **(Default)** Server-side requests made to the customer portal are disabled.
    - **false**: Server-side requests made to the customer portal are enabled, but will always fail in air-gapped and restricted environments.

Disable Customer Portal requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+---------------------------------------------------------------------------+
| Enable or disable customer portal requests.   | - System Config path: **N/A**                                             |
|                                               | - ``config.json setting``: ``".CloudSettings.Disable": false",``          |
|                                               | - Environment variable: ``MM_CLOUDSETTINGS_DISABLE``                      |
| - **true**: **(Default)** Server-side         |                                                                           |
|   requests made to the customer portal are    |                                                                           |
|   disabled.                                   |                                                                           |
| - **false**: Server-side requests made to the |                                                                           |
|   Mattermost Customer Portal are enabled,     |                                                                           |
|   but will always fail in air-gapped and      |                                                                           |
|   restricted deployment environments.         |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+
| **Note**: Cloud admins can’t modify this configuration setting.                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+