---------------------------------------------------------
Severity Levels for Bug Tickets
---------------------------------------------------------

Criteria for Bugs
---------------------------------------------------------

“Scale” of impact
   - S1 - ``Data loss or crash`` - Prevents app use (e.g. Mattermost crash when posting a message). These are the only bugs that can be committed after the T-5 Code Freeze deadline.
   - S2 - ``Functionality loss or cosmetic regressions`` - Most users’ functionality affected (e.g. Cannot favorite a channel), functional regressions, or cosmetic/UI regressions. In addition to S1 bugs, these are the only bugs that can be committed after Code Complete deadline until T-5 Code Freeze.
   - S3 - ``Minor issues`` - Half or less than half of users’ functionality affected (e.g. Cannot create custom emoji if System Admin). Can be fixed anytime until Code Complete deadline.

Assigning Severity Levels
---------------------------------------------------------

Severity levels on bug tickets are normally assigned by Release Manager and triage team during triage meetings, but can also be modified afterwards by devs upon further investigation. 

Mattermost Jira project includes an issue field called "Severity" that can be filled in with either ``S1``, ``S2``, or ``S3`` levels.

Bug tickets are sometimes assessed on a case-by-case basis and further considerations may be applied, such as how risky a bug is to fix or whether it’s more effective to revert code that initially caused the bug.
