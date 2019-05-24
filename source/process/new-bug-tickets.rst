---------------------------------------------------------
Creating New Jira Bug Tickets
---------------------------------------------------------

A bug is any “obvious error” on how the product or feature is functioning and any UI issues. If you’re not reporting an obvious error,
please file a Story ticket instead. Bugs on `unsupported platforms <https://docs.mattermost.com/install/requirements.html>`_ are not considered bugs.

1. Confirm you’re filing a new issue
---------------------------------------------------------

 - Search existing tickets in Jira in the Mattermost project to confirm your issue isn’t already filed by someone else.

2. Confirm the bug is not a security issue
---------------------------------------------------------

 - If your issue involves security, or includes confidential information or customer information, please mark the bug ticket as internal.

3. Information needed on Mattermost bug tickets
---------------------------------------------------------

 - **Labels:** Add a ``customer-bug`` label if the ticket is based on a customer or a community bug report.
 - **Environment:** Mattermost server and version, OS and version, Mattermost mobile app version, Mattermost desktop app version (include the ones that are relevant),
 and any notable Mattermost configurations (such as HA, Elasticsearch, image proxy, SSO).
 - **Steps to reproduce:** How can we reproduce the issue.
 - **Expected behavior:** Describe what you’re expecting to see.
 - **Observed behavior:** Describe your issue in detail. What did you see happen? Please include relevant error messages and/or screenshots.
 - **Regression:** Please re-test your issue (if possible) on the previous Mattermost version at https://prev.test.mattermost.com to see if the bug is a recent regression.

4. Additional helpful information
------------------------------------

 - **Summary:** Add a summary and any additional relevant details of the issue if it helps make the bug more clear.
 - **Attachments:** Please include screenshots and/or videos of any helpful error messages and snippets of what you are seeing.
 - **Possible fixes:** If you can, link to the line of code that might be responsible for the problem.
 
