:orphan:
:nosearch:

Configure the following properties in this file:

* Under ``SqlSettings``, set ``DriverName`` to ``"postgres"``. This is the default and recommended database for all Mattermost installations.
* Under ``SqlSettings``, set ``DataSource`` to ``"postgres://mmuser:<mmuser-password>@<host-name-or-IP>:5432/mattermost?sslmode=disable&connect_timeout=10"`` replacing ``mmuser``, ``<mmuser-password>``, ``<host-name-or-IP>`` and ``mattermost`` with your database name.
* Under ``ServiceSettings``, set ``"SiteURL"``: The domain name for the Mattermost application (e.g. ``https://mattermost.example.com``).