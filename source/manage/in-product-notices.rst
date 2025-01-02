In-product notices
==================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost in-product notices keep users and administrators informed of the newest product improvements, features, and releases.

Administrator notices
---------------------

Administrator notices inform system admins when a new server version is available, when external dependencies are being deprecated, or when server upgrades are recommended due to ending support life cycles. System admins may also receive notices about recommended server configuration options to optimize the user experience of their deployment.

.. image:: ../images/notices_admin.png
   :alt: An example of an in-product administrator notice announcing that a new server version of Mattermost is available. Admin notices can be disabled.
   
System admins can disable end user notices by going to **System Console > Site Configuration > Notices**.

End user notices
----------------

End user notices are used to inform all users when:

- New desktop app versions and feature enhancements are available for users.
- Mattermost is gathering user feedback to improve the product and user experience.

System admins can disable end user notices by going to **System Console > Site Configuration > Notices**.

.. image:: ../images/notices.png
   :alt: An example of an end user in-product notice announcing that a new Mattermost desktop app release is available. End user notices can be disabled.

Frequently asked questions (FAQs)
----------------------------------

Are notices enabled by default?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Notices are enabled by default for all Mattermost users. System admins may choose to disable admin or end user notices in **System Console > Site Configuration > Notices**.

Will I still receive notices if my server is air-gapped?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, the Mattermost server requires a connection to the internet to receive notices.

How often will users receive notices?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notices will be used to raise awareness of new features as part of our monthly release cadence. Users will only receive notices that specifically apply to them. For example, if a user is already running the latest Desktop App version, they will not receive an upgrade notice.