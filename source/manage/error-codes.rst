Mattermost error codes
======================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Mattermost is designed to deploy in private networks which may be disconnected or “air-gapped” from the internet. In these deployments, links to Mattermost’s online documentation may be unavailable. 

Therefore, Mattermost error codes are provided to enable administrators to use internet connected machines to look up error messages and resolutions in online resources, including Mattermost documentation and user forums, as well as providing Mattermost support teams a concise way to identify issues.

Mattermost error codes are used in logs, administrative tools, as well as on-screen messages to concisely identify issues and connect them with additional resources. 

In advanced deployments, error codes can be overwritten by administrators to reference internal documentation and guides.

ERROR_SAFETY_LIMITS_EXCEEDED
----------------------------

This error happens in the free version of Mattermost when more than 10,000 users are registered on the server.

The free version of Mattermost is intended for approximately 50 users, and should a deployment materially exceed this recommended size, administrators should seek to either `purchase a commercial license <https://mattermost.com/pricing/>`__ or apply for a `nonprofit license <https://mattermost.com/nonprofit/>`__.

When usage grossly exceeds the recommended limit for users in a safe deployment, an error message is displayed and certain functionality may be limited.

10,000 users represents a “high upper limit” for deployments that are approximately 200 times the recommended size, which is far beyond the intended design of the product. 

To remove the error message, deactivate users until your user count is below the high upper limit.