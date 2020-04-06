---------------------------------------------------------
Severity levels for bug tickets
---------------------------------------------------------

Criteria for bugs
---------------------------------------------------------

“Scale” of impact
   - S1 - ``Data loss or crash`` - Prevents app use (e.g. Mattermost crashes when posting a message). These are the only bugs that can be committed after the T-5 Code Freeze deadline.
   - S2 - ``Functionality loss or cosmetic regressions`` - Most users’ functionality affected (e.g. cannot favorite a channel) or includes functional and/or cosmetic/UI regressions. In addition to S1 bugs, these are the only bugs that can be committed after Code Complete deadline until T-5 Code Freeze.
   - S3 - ``Minor issues`` - Half or less than half of users’ functionality affected (e.g. cannot create custom emoji if System Admin). Can be fixed anytime until Code Complete deadline.

Assigning severity levels
---------------------------------------------------------

Severity levels on bug tickets are normally assigned by Release Manager and Triage team during Triage meetings using the "Severity" Jira field, but can also be applied by devs and QA at any time.

Bug tickets are sometimes assessed on a case-by-case basis and further considerations may be applied, such as whether the bug is a recent regression or not, how risky the bug fix is, or whether it’s more effective to revert code that initially caused the bug.

Frequently Asked Questions
---------------------------------------------------------

**Why are we doing this?**

 - This will help with prioritizing release bug fixes, and composing release metrics related to `mean time days from bug report to delivery (MTTD) <https://docs.google.com/spreadsheets/d/1Aoj4OTaWoyrKIcQNiHH1MVoRG51T20Y_0w2tg5oVw-M/edit#gid=825551144>`_. Severity guidelines are important so that we can ensure high quality releases for customers.

**What does this change?**

 - This doesn't change existing processes, but makes it more official. We have prioritized release bug tickets based on severity before, along with other considerations such as whether the bug is a recent regression or not.

**Will this negatively impact quality?**

 - This will not negatively impact quality as this doesn't change existing processes. We have prioritized release bug tickets based on severity before. For example, a fix for an issue where `Mattermost server crashed when running a compliance export <https://mattermost.atlassian.net/browse/MM-23157>`_ was fixed for v5.21.0 at T-3 because it was deemed a high severity issue.

**Will customer/Enterprise bugs be prioritized any differently?**

 - This doesn't change existing processes and customer bugs will continue to be assessed on a case-by-case basis (e.g. how severe and urgent is the issue for the customer). For example, a fix for an issue where `Mattermost server crashed when running a compliance export <https://mattermost.atlassian.net/browse/MM-23157>`_ was fixed for v5.21.0 at T-3 because it was an urgent, high severity customer bug.
