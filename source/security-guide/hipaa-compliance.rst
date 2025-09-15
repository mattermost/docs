HIPAA Compliance
=================

Deploying Mattermost as part of a HIPAA-compliant IT infrastructure requires a deployment team trained on `HIPAA-compliance requirements and standards <https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/>`_.

HIPAA-compliant deployments commonly consider the following:

- Omitting the contents of messages from mobile push and email notifications:

  - If your :ref:`Push Notifications Contents <administration-guide/configure/site-configuration-settings:push notification contents>` option is set to ``Send full message snippet`` there is a chance Personal Health Information (PHI) contained in messages could be displayed on a user's locked phone as a notification. To avoid this, set the option to ``Send generic description with user and channel names`` or ``Send generic description with only sender name``.
  - Similarly, setting :ref:`Email Notifications Contents <administration-guide/configure/site-configuration-settings:email notification contents>` to ``Send generic description with only sender name`` will only send the team name and name of the person who sent the message, with no information about channel name or message contents included in email notifications.

- Beyond Technical Safeguards, HIPAA compliance deployments also require:

  - Administrative Safeguards
  - Physical Safeguards
  - Organizational requirements and other standards.

To learn more, please review `HIPAA requirements from the US Department of Health and Human Services <https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/>`_.