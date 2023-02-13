:orphan:
:nosearch:

.. tip:: 

    Each configuration value below includes a JSON path to access the value programmatically in the ``config.json`` file using a JSON-aware tool. For example, the ``SiteURL`` value is under ``ServiceSettings``.
    
    - If using a tool such as `jq <https://stedolan.github.io/jq/>`__, you'd enter: ``cat config/config.json | jq '.ServiceSettings.SiteURL'``
    - When working with the ``config.json`` file manually, look for the key ``ServiceSettings``, then within that object, find the key ``SiteURL``.