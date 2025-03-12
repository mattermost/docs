Mattermost free user limits
===========================

:ref:`Free deployments <about/editions-and-offerings:mattermost free>` of :ref:`Mattermost Team Edition <about/editions-and-offerings:mattermost team edition>` are designed for small teams of approximately 50 users. When these deployments grow significantly beyond this size, limits help maintain server reliability while encouraging proper scaling.

User thresholds across releases
--------------------------------

From Mattermost v10.6, Team Edition user limits are enforced in 2 ways:

- System admins see a dismissible banner alert when the user count exceeds the user warning threshold.
- System admins see a non-dismissible banner alert and can't create or add new users until the user count falls below the hard limit.
  
The following limits are designed to ensure your self-hosted deployment remains scalable, reliable, and optimized for teams, where 5000 users represents a “high upper limit” for deployments that are approximately 200 times the recommended size, which is far beyond the intended design of the product:

+--------------+--------------+------------+------------+------------+
| **Version**  | **v9.5 ESR** | **v9.9**   | **v10.6**  | **v10.10** |
+--------------+--------------+------------+------------+------------+
| User warning | 10,000       | 5000       | 2500       | 1000       |
+--------------+--------------+------------+------------+------------+
| Hard limit   | None         | 11,000     | 5000       | 2500       |
+--------------+--------------+------------+------------+------------+

Error code: ERROR_SAFETY_LIMITS_EXCEEDED
------------------------------------------

System admins see the ``ERROR_SAFETY_LIMITS_EXCEEDED`` error code in Mattermost logs, administrative tools, and in on-screen alerts when usage grossly exceeds the recommended thresholds for users in a safe deployment. 

This error code is designed to help system admins in private networks that may be disconnected or "air-gapped" from the internet to identify and resolve issues quickly using internet connected machines to look up error codes and resolutions in online resources.

Plan ahead
-----------

If your self-hosted Mattermost free instance is nearing or exceeding these limits, you must plan ahead to ensure uninterrupted collaboration. System admins can:

- Proactively manage user count by regularly reviewing banners and instances of the ``ERROR_SAFETY_LIMITS_EXCEEDED`` error code to manage your deployment size and stay below user thresholds.
- :ref:`Deactivate unused accounts <configure/user-management-configuration-settings:activate or deactivate users>`.
- Plan for scalability by :ref:`upgrading to a commercial license <about/editions-and-offerings:mattermost plans>`. :ref:`Mattermost Enterprise <about/editions-and-offerings:mattermost enterprise>` and :ref:`Mattermost Professional <about/editions-and-offerings:mattermost professional>` licenses are designed for organizations that need performance and reliability at scale.

.. note::

  Nonprofit organizations may qualify for free or discounted licenses via the :ref:`Mattermost Nonprofit License Program <about/subscription:mattermost nonprofit license program>`.