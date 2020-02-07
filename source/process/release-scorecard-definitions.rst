Release Scorecard Definitions
-----------------------------

For https://docs.google.com/spreadsheets/d/1Aoj4OTaWoyrKIcQNiHH1MVoRG51T20Y_0w2tg5oVw-M/edit#gid=825551144

Release Output
==============

+------------------------------------------+------------------------------------------------+
| Metric                                   | How to Measure                                 |
+==========================================+================================================+
| Ratio of story-to-bug tickets            | Total of feature tickets over total of         |
|                                          | bug tickets. Include current quality           |
|                                          | release and previous feature release.          |
+------------------------------------------+------------------------------------------------+
| Mean time from P1 bug report to delivery | With a new or existing Jira filter, with:      |
|                                          |                                                |
|                                          | 1. Project = Mattermost                        |
|                                          | 2. Fix Versions = Latest released version      |
|                                          | 3. Issue Type = Bug                            |
|                                          | 4. Label = P1                                  |
|                                          | 5. Created Date = 17th of the previous month   |
|                                          | 6. Release Date = 16th of the current month    |
|                                          |                                                |
|                                          | Copy a list of Jira tickets with the above     |
|                                          | information and paste them into a spreadsheet. | 
|                                          | Calculate the average by using a formula       |
|                                          | “=Release Day-Created”.                        |   
+------------------------------------------+------------------------------------------------+
| Mean time from P2 bug report to delivery | With a new or existing Jira filter, with:      |
|                                          |                                                |
|                                          | 1. Project = Mattermost                        |
|                                          | 2. Fix Versions = Latest released version      |
|                                          | 3. Issue Type = Bug                            |
|                                          | 4. Label = P2                                  |
|                                          | 5. Created Date = 17th of the previous month   |
|                                          | 6. Release Date = 16th of the current month    |
|                                          |                                                |
|                                          | Copy a list of Jira tickets with the above     |
|                                          | information and paste them into a spreadsheet. | 
|                                          | Calculate the average by using a formula       |
|                                          | “=Release Day-Created”.                        |
+------------------------------------------+------------------------------------------------+
| Mean time from P3 bug report to delivery | With a new or existing Jira filter, with:      |
|                                          |                                                |
|                                          | 1. Project = Mattermost                        |
|                                          | 2. Fix Versions = Latest released version      |
|                                          | 3. Issue Type = Bug                            |
|                                          | 4. Label = P3                                  |
|                                          | 5. Created Date = 17th of the previous month   |
|                                          | 6. Release Date = 16th of the current month    |
|                                          |                                                |
|                                          | Copy a list of Jira tickets with the above     |
|                                          | information and paste them into a spreadsheet. | 
|                                          | Calculate the average by using a formula       |
|                                          | “=Release Day-Created”.                        |
+------------------------------------------+------------------------------------------------+
| Number of P1 bugs reported in production | *Bug severity guidelines are in progress,*     |
|                                          | *after which a Jira query will be built*       |
+------------------------------------------+------------------------------------------------+
| Number of P2 bugs reported in production | *Bug severity guidelines are in progress,*     |
|                                          | *after which a Jira query will be built*       |
+------------------------------------------+------------------------------------------------+
| Number of P3 bugs reported in production | *Bug severity guidelines are in progress,*     |
|                                          | *after which a Jira query will be built*       |
+------------------------------------------+------------------------------------------------+

Release Management
=================

+----------------------------------------+-----------------------------------------+
| Metric                                 | How to Measure                          |
+========================================+=========================================+
| Number of misses in each release cycle | Same as number of bugs reported in      |
|                                        | production, + count of issues reported  |
|                                        | in documentation or marketing by        |
|                                        | customers, CSMs, Support or Product.    |
|                                        | E.g. dot releases from customer reports,|
|                                        | undocumented breaking changes.          |
+----------------------------------------+-----------------------------------------+
| Number of setbacks to users/staff      | Manual count of negative reactions      |
| resulting in a negative reaction       | reported by CSMs, Support or Product.   |
|                                        | E.g. features that got pushed.          |
+----------------------------------------+-----------------------------------------+
| Number of measurable actions from each | Count of completed and reported items   |
| release retrospective driven from root | from Release Retrospective document.    |
| causes & completed and reported to R&D |                                         |
+----------------------------------------+-----------------------------------------+
| Number of deadlines missed in release  | Manual count of deadlines not met from  |
| checklist                              | items posted to Release Checklist.      |
+----------------------------------------+-----------------------------------------+

Release Heartbeat
=================

+-----------------------------------------+--------------------------------------------------------------------------------+
| Metric                                  | How to Measure                                                                 |
+=========================================+================================================================================+
| Time updated to RC1 (PST)               | Check Release Discussion channel history                                       |
|                                         | for date/time RC1 was cut.                                                     |
+-----------------------------------------+--------------------------------------------------------------------------------+
| How many RCs cut                        | Check Release Discussion channel history                                       |
|                                         | for how many RCs were cut for that release.                                    |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Number of days between when final RC    | Check Release Discussion channel for post with official release build.         |
| is cut and the release date             | Oxygen = 16th - Day Final RC is cut                                            |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Community + customer bugs reported      | With a new or existing Jira filter, with:                                      |
| during release timeframe (17th to 16th) |                                                                                |
|                                         | 1. Project = Mattermost                                                        |
|                                         | 2. Fix Versions = Latest released version                                      |
|                                         | 3. Issue Type = Bug                                                            |
|                                         | 4. Label = Customer-bug and Community-bug                                      |
|                                         | 5. Created Date = 17th of the previous month                                   |
|                                         | 6. Release Date = 16th of the current month                                    |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Number of customer bugs fixed           | With a new or existing Jira filter, with:                                      |
| during release                          |                                                                                |
|                                         | 1. Project = Mattermost                                                        |
|                                         | 2. Fix Versions = Latest released version                                      |
|                                         | 3. Issue Type = Bug                                                            |
|                                         | 4. Status = Closed and Resolved                                                |
|                                         | 5. Label = Customer-bug                                                        |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Total valid bugs in fix version         | After closing current release:                                                 |
|                                         |                                                                                |
|                                         | project = Mattermost AND issuetype = Bug AND resolution not in (Duplicate,     |                                         
|                                         | "Cannot Reproduce", "Won't Fix") AND fixVersion = latestReleasedVersion()      |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Total valid bugs in fix version found   | Check "Se", "Selenium-found, "Rainforest-found" Jira labels.                   |
| by test automation                      |                                                                                |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Total valid bugs found after RC1 is cut | After closing current release, adjust dates as per above, and use this Jira    |
|                                         | query:                                                                         |
|                                         |                                                                                |
|                                         | 1. Check Jira timezone + Pre-release timezone and make sure times match        |
|                                         | 2. Replace START with date (yyyy-MM-dd HH:mm) RC1 was cut                      |
|                                         | 3. Replace END with date (yyyy-MM-dd HH:mm) test servers returned to master    |
|                                         |                                                                                |
|                                         | project = Mattermost AND issuetype = Bug AND resolution not in (Duplicate,     |
|                                         | "Cannot Reproduce", "Won't fix") AND created > "START" AND created < "END"     |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Valid bugs found after RC1 fixed in     | After closing current release, adjust dates as per above, and use this Jira    |
| release                                 | query:                                                                         |
|                                         |                                                                                |
|                                         | project = Mattermost AND issuetype = Bug AND resolution not in (Duplicate,     |
|                                         | "Cannot Reproduce", "Won't Fix")  AND created > "START" AND created < "END"    |
|                                         | AND fixVersion = latestReleasedVersion()                                       |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Valid bugs found after RC1 pushed to    | After closing current release, adjust dates as per above, and use this Jira    |
| next release                            | query:                                                                         |
|                                         |                                                                                |
|                                         | project = Mattermost AND issuetype = Bug AND resolution not in (Duplicate,     |                                      
|                                         | "Cannot Reproduce", "Won't Fix") AND created > "START" AND created < "END"     |
|                                         | AND fixVersion = earliestUnreleasedVersion()                                   |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Valid bugs found after RC1 fix version  | After closing current release, adjust dates as per above, and use this Jira    |
| = other (eg unscheduled, not set)       | query:                                                                         |
|                                         |                                                                                |
|                                         | project = Mattermost AND issuetype = Bug AND created > "START" AND created <   |  
|                                         | "END" AND resolution not in (Duplicate, "Cannot Reproduce", "Won't Fix") AND   |
|                                         | (fixVersion not in (latestReleasedVersion(), earliestUnreleasedVersion()) OR   |
|                                         | fixVersion is EMPTY)                                                           |
+-----------------------------------------+--------------------------------------------------------------------------------+
| (Non-security) Bugs requiring patch     | After any patch release goes out (after the normal release date):              |
| release                                 | Check Changelog for total number of non-security patch releases.               |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Total features/improvements in fix      | With a new or existing Jira filter, with:                                      |
| version                                 |                                                                                |
|                                         | 1. Project = Mattermost                                                        |
|                                         | 2. Fix Versions = Latest released version                                      |
|                                         | 3. Issue Type = Story                                                          |
|                                         | 4. Status = Closed and Resolved                                                |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Critical security issues found during   | With a new or existing Jira filter, check for Security Vulnerability tickets:  |
| release timeframe                       |                                                                                |
|                                         | 1. Project = Mattermost                                                        |
|                                         | 2. Fix Versions = Latest released version                                      |
|                                         | 3. Impact = High                                                               |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Moderate security issues found during   | With a new or existing Jira filter, check for Security Vulnerability tickets:  |
| release timeframe                       |                                                                                |
|                                         | 1. Project = Mattermost                                                        |
|                                         | 2. Fix Versions = Latest released version                                      |
|                                         | 3. Impact = Medium                                                             |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Minor security issues found during      | With a new or existing Jira filter, check for Security Vulnerability tickets:  |
| release timeframe                       |                                                                                |
|                                         | 1. Project = Mattermost                                                        |
|                                         | 2. Fix Versions = Latest released version                                      |
|                                         | 3. Impact = Low                                                                |
+-----------------------------------------+--------------------------------------------------------------------------------+
