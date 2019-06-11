Net Promoter Score Plugin
=========================

Mattermost is introducing in-product feedback surveys beginning in v5.12. Feedback is collected in the form of a Net Promoter Score survey, and is used to measure user satisfaction and improve product quality by hearing directly from users. 

The Net Promoter Score (NPS) plugin is enabled by default but can be removed in the **System Console > Plugins (Beta) > Plugin Management** section. 

Administration
--------------
When is the survey scheduled?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Users will begin to receive surveys 21 days after the server is upgraded to v5.12 or later, assuming the following conditions are true:

- NPS plugin is enabled in **System Console > Plugins (Beta) > Plugin Management**
- NPS survey is enabled in the plugin configuration in **System Console > Plugins (Beta) > Net Promoter Score**
- User account is >= 21 days old
- User has not completed a survey in the last 90 days
- User has not been sent a survey in the last 90 days
- Current server version is greater than the server version of the last NPS survey, excluding dot releases

The above conditions mean that at maximim frequency, a user will receive a survey every 90 days assuming the server is upgraded in that time period. 

How can I stop the survey?
~~~~~~~~~~~~~~~~~~~~~~~~~~
Removing or disabling the **Net Promoter Score** plugin from **System Console > Plugins (Beta) > Plugin Management** will stop surveys. Alternatively, you can disable surveys from the plugin configuration in **System Console > Plugins (Beta) > Net Promoter Score**. 

Survey Data
-----------

How is feedback collected?
~~~~~~~~~~~~~~~~~~~~~~~~~~

What data is collected?
-----------------------
Data is only collected when a user submits feedback by responding to the survey questions. 





System Console > Plugins (Beta) > Plugin Management





Disabled if Telemetry is disabled

What is NPS
It can be disabled and how to disable it
Who will be surveyed (all users)
When the surveys are taking place with enough notice to disable them
Schedule of surveys (ie every 3 months if admins are upgrading)
Visibility of the admin alerts (ie that only Sys Admins can see them)
Mechanism of the survey (ie bot)
Summary of what is collected (and how it’s GDPR compliant?)
How it will be used to improve the product/benefits to customers



Data collected

How to disable

What we do with the 
