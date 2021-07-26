Desktop Managed Resources
==========================

The Mattermost Desktop App supports managed resources. A managed resource can be any service available on the same hostname using the same protocol as the Mattermost server.

.. note::
    Using this feature requires a `custom build of the Mattermost Desktop App <https://docs.mattermost.com/deployment/desktop-app-deployment.html>`_.

Add the path of a managed resource to your configuration file. When selected, it opens as a pop-up window in the Mattermost Desktop app.

In addition to customizing the Mattermost Desktop App, the `Managed Resource Paths <https://docs.mattermost.com/administration/config-settings.html#managed-resource-paths>`_ setting on the Mattermost server must be configured.

In the below example we add the managed resource ``/video``.

.. code-block:: json

    [...]
    managedResources: ['trusted', 'video'],
    [...]

Here are two example server URLs each with valid and invalid managed resource URLs:

- Mattermost server: ``https://mattermost.my.org``

  - A valid video service: ``https://mattermost.my.org/video``

  - A valid conference service: ``https://mattermost.my.org/conference``

  - An invalid video service using a different protocol: ``http://mattermost.my.org/video``

  - An invalid conference service having a different origin: ``https://conference.my.org``

- Mattermost server: ``https://my.org/mattermost``

  - A valid video service: ``https://my.org/video``

  - A valid conference service: ``https://my.org/conference``

  - An invalid video service using a different protocol: ``http://my.org/video``
  
  - An invalid conference service having a different origin: ``https://conference.my.org``
