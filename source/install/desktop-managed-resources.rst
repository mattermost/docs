
Desktop - Managed Resources
===========================

This guide provides steps to use managed resources with the Mattermost Desktop App. A managed resource can be any service available on the same hostname using the same protocol as the Mattermost server.

.. note::
    Using this feature requires a `custom build of the Mattermost Desktop App <https://docs.mattermost.com/deployment/desktop-app-deployment.html>`_.

When adding the folder of a managed resource to `src/common/config/buildConfig.js <https://github.com/mattermost/desktop/blob/master/src/common/config/buildConfig.js>`_ it is available from the Mattermost Desktop App as a pop-up window instead of opening in a web-browser. In the below example we add the managed resource `/video`.

.. code-block:: json
    [...]
    managedResources: ['trusted', 'video'],
    [...]

Here are two example server URLs each with valid and invalid managed resource URLs:

- Mattermost server: ``https://mattermost.my.org``

  - A valid video service: ``https://mattermost.my.org/video``

  - A valid conference service: ``https://mattermost.my.org/conference``

  - An invalid video service: ``http://mattermost.my.org/video``

  - An invalid conference service: ``https://conference.my.org``

- Mattermost server: ``https://my.org/mattermost``

  - A valid video service: ``https://my.org/video``

  - A valid conference service: ``https://my.org/conference``

  - An invalid video service: ``http://my.org/video``
  
  - An invalid conference service: ``https://conference.my.org``

