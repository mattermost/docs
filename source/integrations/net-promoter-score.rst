Net Promoter Score Plugin
=========================

Mattermost is introducing in-product feedback surveys beginning in v5.12. Feedback is collected in the form of a Net Promoter Score survey, and is used to measure user satisfaction and improve product quality by hearing directly from users. 

Administration
--------------
Is the survey enabled by default?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Net Promoter Score (NPS) plugin and surveys are enabled by default on all servers that have `Error and Diagnostic Reporting <https://docs.mattermost.com/administration/telemetry.html>`_ enabled when upgrading to v5.12 or later. 

How can surveys be disabled?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Removing or disabling the **Net Promoter Score** plugin from **System Console > Plugins (Beta) > Plugin Management** will disable surveys. Alternatively, you can disable surveys from the plugin configuration in **System Console > Plugins (Beta) > Net Promoter Score**. 

If the plugin or surveys are disabled, they will remain disabled for subsequent server upgrades.

When is the survey scheduled?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Users will receive surveys 21 days after the server is upgraded to v5.12 or later, assuming the following conditions are true:

- NPS plugin is enabled in **System Console > Plugins (Beta) > Plugin Management**
- NPS survey is enabled in the plugin configuration in **System Console > Plugins (Beta) > Net Promoter Score**
- User account is greater than 21 days old
- User has not completed a survey in the last 90 days
- User has not been sent a survey in the last 90 days
- Current server version is greater than the server version of the last NPS survey, excluding dot releases

The above conditions mean that at maximim frequency a user will receive a survey every 90 days, assuming the server is upgraded within that time period. 

How will I be notified a survey is scheduled?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System Administrators will receive an email notification and in-product Direct Message from "Surveybot" mentioning the scheduled date the survey will be triggered.

.. image:: ../images/nps-admin.png

Survey Data
-----------

How is the survey received?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the survey is triggered on the server, all users will receive an in-product Direct Messages from "Surveybot" on their next interactation with Mattermost. Surveys are not sent to users who are offline.

Users can optionally select a 0-10 score on how likely they are to recommend Mattermost and then provide written feedback about their expereince. Selecting a score and providing feedback are optional, and the survey can be ignored without interupting usage of Mattermost.

.. image:: ../images/nps-survey.png

What data is collected?
~~~~~~~~~~~~~~~~~~~~~~~
Data is only collected when a user selects a score or provides written feedback in response to survey questions. The following non-personally identifiable data is collected:

- Survey information:
  - `score`: 0-10 score submitted by the user
  - `feedback`: Written feedback submitted by the user (if applicable)
  - `timestamp`: Timestamp of the survey submission
- Basic information about the server: 
  - `server_version`: Server/webapp version the survey was submitted on
  - `server_install_date`: Installation date of the server
  - `server_id`: Diagnostic ID used for error and diagnostics reporting
  - `license_id`: License ID used for error and diagnostics reporting
  - `license_sku`: E10 or E20 (if applicable)
- Basic information about the user:
  - `user_role`: System Admin, Team Admin or member
  - `user_create_at`: Account creation timestamp
  - `user_id`: User ID of the surveyed user
