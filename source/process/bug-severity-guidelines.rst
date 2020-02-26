---------------------------------------------------------
Assigning Severity Levels for Bug Tickets
---------------------------------------------------------

Criteria for Bugs:
---------------------------------------------------------

1. % of customers affected
2. “scale” of impact
   - S1 - Prevents app use (e.g. Mattermost crash when posting a message) OR functional regressions. Only bugs that can be committed after Code Freeze deadline
   - S2 - 50%-100% of users’ functionality affected (e.g. Cannot favorite a channel) OR cosmetic/UI regressions. In addition to S1, only bugs that can be committed after Code Complete.
   - S3 - 20%-50% of users’ functionality affected (e.g. Cannot create custom emoji if System Admin)
   - S4 - Other minor (e.g. channel ID is too small in View Info modal)
