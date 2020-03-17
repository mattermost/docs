---------------------------------------------------------
Severity levels for bug tickets
---------------------------------------------------------

Criteria for bugs
---------------------------------------------------------

Scale of impact
   - S1 - Prevents app use (e.g. Mattermost crashes when posting a message) or results in functional regressions. These are the only bugs that can be committed after the T-5 Code Freeze deadline.
   - S2 - Most users’ functionality affected (e.g. cannot favorite a channel) or includes cosmetic/UI regressions. In addition to S1 bugs, these are the only bugs that can be committed after Code Complete deadline until T-5 Code Freeze.
   - S3 - Half or less than half of users’ functionality affected (e.g. cannot create custom emoji if System Admin). Can be fixed anytime until Code Complete deadline.
   - S4 - Other minor (e.g. channel ID is too small in View Info modal). Can be fixed anytime until Code Complete deadline.

Assigning severity levels
---------------------------------------------------------

Severity levels on bug tickets are normally assigned by the Release Manager and Triage team during Triage meetings, but can also be modified afterwards by devs upon further investigation. 

Bug tickets are sometimes assessed on a case-by-case basis and further considerations may be applied, such as how risky a bug is to fix or whether it’s more effective to revert code that initially caused the bug.
