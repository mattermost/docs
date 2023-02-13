:nosearch:

User satisfaction surveys
==========================

|all-plans| |cloud|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

Mattermost provides in-product feedback surveys. Feedback is used to measure user satisfaction and improve product quality by hearing directly from users. Please refer to our `privacy policy <https://github.com/mattermost/mattermost-server/blob/master/build/PRIVACY_POLICY.md>`_ for more information on the collection and use of information received through our services.

.. contents::
  :depth: 2
  :local:
  :backlinks: entry

Administration
--------------

Is the survey enabled by default?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The user satisfaction survey is a pre-packaged plugin, and surveys are enabled by default. However, the plugin will not be activated on any workspaces that have `Error and Diagnostic Reporting </manage/telemetry.html>`__ disabled, meaning no surveys or data collection occurs.

How can surveys be disabled?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disabling the **User Satisfaction Surveys** plugin from **System Console > Plugins > Plugin Management** will disable surveys and all data collection by the plugin. If surveys have been disabled from the plugin configuration in **System Console > Plugins > User Satisfaction Surveys** but the plugin itself is still enabled, surveys will not be scheduled but users can still send written feedback by messaging Surveybot.

If the plugin or surveys in the plugin configuration are disabled, they will remain disabled.

When is the survey scheduled?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users will receive a survey every 90 days, assuming the following conditions are true:

- User Satisfaction Surveys plugin is enabled in **System Console > Plugins > Plugin Management**
- Surveys are enabled in the plugin configuration in **System Console > Plugins > User Satisfaction Surveys**
- User account is greater than 21 days old
- User has not completed a survey in the last 90 days

How will I be notified a survey is scheduled?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System Admins will receive an email notification and in-product Direct Message from "Surveybot" mentioning the scheduled date the survey will be triggered.

.. image:: ../images/nps-admin.png

Survey Data
-----------

How is the survey received?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the survey is triggered on the workspace, all users will receive an in-product Direct Messages from "Surveybot" on their next login or page refresh in Mattermost.

Users can optionally select a 0-10 score on how likely they are to recommend Mattermost and then provide written feedback about their experience. Selecting a score and providing feedback are optional, and the survey can be ignored without interrupting usage of Mattermost.

.. image:: ../images/nps-survey.png

What data is collected?
~~~~~~~~~~~~~~~~~~~~~~~

Data is only collected when a user selects a score or provides written feedback in response to survey questions. Please refer to our `privacy policy <https://mattermost.com/privacy-policy/>`__ for more information on the collection and use of information received through our services. The following **non-personally identifiable information** is collected:

- Survey information:
   - Score (0-10) submitted by the user
   - Written feedback submitted by the user (if applicable)
   - Timestamp of the survey submission
- User information:
   - User role (System Admin, Team Admin, or member)
   - Account creation timestamp
   - User ID of the surveyed user

