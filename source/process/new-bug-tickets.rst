---------------------------------------------------------
Creating New Jira Bug Tickets
---------------------------------------------------------

Bugs are any “obvious errors” on how the product or a feature is functioning as well as any UI issues. If you’re not reporting an obvious error, please file a Story ticket instead. Errors on `unsupported platforms <https://docs.mattermost.com/install/requirements.html>`_ are not considered bugs.

1. Initial steps to access the "Mattermost" Jira project
---------------------------------------------------------

 - Create a Jira account with your mattermost email address at https://mattermost.atlassian.net.
 - Ask to give your account permission to create Jira tickets in our `Jira Configuration channel <https://community.mattermost.com/core/channels/jira-configuration>`_.
 - Create a ticket in Jira's "Mattermost" project following the next steps below with a note on its priority level.

2. Confirm you’re filing a new issue
---------------------------------------------------------

 - Search existing tickets in Jira's "Mattermost" project to confirm your issue isn’t already filed by someone else.

3. Confirm the bug is not a confidential issue
---------------------------------------------------------

 - If your issue involves security or if it involves confidential information or customer information, please mark the bug ticket as internal.

4. Information needed on Mattermost bug tickets
---------------------------------------------------------

 - **Labels:** Add a ``customer-bug`` label if the ticket is based on a customer bug report. Add a ``community-bug`` label if the ticket is based on a community bug report.
 - **Environment:** Mattermost server and version, OS and version, Mattermost mobile app version, Mattermost desktop app version, any notable Mattermost configurations (such as HA, Elasticsearch, image proxy, SSO).
 - **Steps to reproduce:** How can we reproduce the issue.
 - **Expected behavior:** Describe what you’re expecting to see.
 - **Observed behavior:** Describe your issue in detail. What did you see happen? Please include relevant error messages and/or screenshots.
 - **Regression:** Please re-test your issue (if possible) on the previous Mattermost version at https://prev.test.mattermost.com to see if the bug is a recent regression.

5. Additional helpful information
------------------------------------

 - **Summary:** Add a summary and any additional relevant details of the issue if it helps make the bug more clear.
 - **Attachments:** Please include screenshots and/or videos of any helpful error messages and snippets of what you are seeing.
 - **Possible fixes:** If you can, link to the line of code that might be responsible for the problem.
 
