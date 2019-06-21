Incident Response and Monitoring Tools
============================================

Our `Integrations Directory <https://integrations.mattermost.com>`_ has several integrations to connect incident response and monitoring tools in Mattermost.

Here are some popular options below, including self-hosted on-prem or self-hosted private cloud solutions, and vendor-hosted SaaS solutions.

AWS CloudWatch SNS
~~~~~~~~~~~~~~~~~~~~~~~~

 - Two-way integration between Mattermost and Amazon AWS SNS, developed by Carlos Tadeu Panato Junior, supported by Mattermost.
 - Receive SNS notifications from Alerts created by Amazon AWS CloudWatch and sent via AWS SNS.
 - Get operational data and actionable insights to monitor Mattermost in order to respond to system-wide performance changes.
 - Source code + docs: https://github.com/mattermost/mattermost-plugin-aws-SNS

PagerDuty
~~~~~~~~~~~~~~~~~~~~~~~~

 - Get automatic information regarding the state of an incident to Mattermost, developed by PagerDuty.
 - Receive all incident updates for any PagerDuty Service in any Mattermost channel to optimize incident resolution time and process.
 - Docs: https://www.pagerduty.com/docs/guides/mattermost-integration-guide/

Splunk
~~~~~~~~~~~~~~~~~~~~~~~~

 - Monitor a Mattermost environment.
 - Receive application performance insights in any Mattermost channel for better troubleshooting and monitoring and to increase uptime.
 - Docs: http://datatomix.com/?p=433, written by Christian Johannsen.

Opsgenie
~~~~~~~~~~~~~~~~~~~~~~~~

 - Two-way integration between Opsgenie and Mattermost, developed by Opsgenie.
 - Send alert notifications from your Opsgenie incident boards to Mattermost channels.
 - Use slash commands to take quick actions such as acknowledging, assigning, creating and closing alerts in the Mattermost user interface.
 - Docs: https://docs.opsgenie.com/docs/mattermost-integration 

Prometheus Alertmanager
~~~~~~~~~~~~~~~~~~~~~~~~

 - Two-way integration between Alertmanager and Mattermost, developed by Carlos Tadeu Panato Junior.
 - Handle alerts sent by client applications such as the Prometheus server and route them to the correct receiver integrations such as email, PagerDuty, or Opsgenie.
 - Source code + docs: https://github.com/cpanato/mattermost-plugin-alertmanager

Have a proposal for an incident response and monitoring integration? `Let us know in the feature proposal forum <https://mattermost.uservoice.com/forums/306457-general?category_id=202591>`_.

Have built an integration? `Let us know <https://integrations.mattermost.com/submit-an-integration/>`_ and we'll share in our `Integrations Directory <https://integrations.mattermost.com>`_.
