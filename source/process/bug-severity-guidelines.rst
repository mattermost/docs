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

Severity levels on bug tickets are normally assigned by Release Manager and Triage team during Triage meetings, but can also be applied by devs and QA at any time. 

Mattermost Jira project includes an issue field called "Severity" that can be filled in with either ``S1``, ``S2``, or ``S3`` levels.

Bug tickets are sometimes assessed on a case-by-case basis and further considerations may be applied, such as how risky a bug is to fix or whether it’s more effective to revert code that initially caused the bug.

Frequently Asked Questions
---------------------------------------------------------

**Why are we doing this?**
 - This will help with prioritizing release bug fixes, and composing release metrics related to `mean time days from bug report to delivery (MTTD) <https://docs.google.com/spreadsheets/d/1Aoj4OTaWoyrKIcQNiHH1MVoRG51T20Y_0w2tg5oVw-M/edit#gid=825551144>`_. Severity guidelines are important so that we can ensure high quality releases.

**What does this change?**
 - This doesn't change existing processes, but makes it official. We have prioritized release bug tickets based on severity before, but this helps make the process more visible.

**Will this negatively impact quality?**
 - This doesn't change existing processes, but makes it official. We have prioritized release bug tickets based on severity before. For example, a fix for an issue where _`Mattermost server crashed when running a compliance export <https://mattermost.atlassian.net/browse/MM-23157> was fixed for v5.21 at T-3 because it was a high severity issue.

**Will customer/Enterprise bugs be prioritized any differently?**
 - This doesn't change existing processes and customer bugs will continue to be assessed on a case-by-case basis (how urgent is the fix, how big is the customer, etc.). For example, a fix for an issue where _`Mattermost server crashed when running a compliance export <https://mattermost.atlassian.net/browse/MM-23157> was fixed for v5.21 at T-3 because it was an urgent customer bug.
 
