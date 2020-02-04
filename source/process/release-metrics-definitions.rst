Release Metrics Definitions
------------------

For https://docs.google.com/spreadsheets/d/1Aoj4OTaWoyrKIcQNiHH1MVoRG51T20Y_0w2tg5oVw-M/edit#gid=825551144

Release Output
==============

+------------------------------------------+-------------------------------------------+
| Metric                                   | How to Measure                            |
+==========================================+===========================================+
| Ratio of story-to-bug tickets            | Total of feature tickets over total of    |
|                                          | bug tickets. Include current Quality      |
|                                          | release and previous feature release.     |
+------------------------------------------+-------------------------------------------+
| Mean time from P1 bug report to delivery | Get list of created date and release      |
|                                          | date for tickets with P1 label resolved   |
|                                          | for a release and calculate the average.  |
|                                          | Use formula “=Release Day-Created”.       |
+------------------------------------------+-------------------------------------------+
| Mean time from P2 bug report to delivery | Get list of created date and release      |
|                                          | date for tickets with P2 label resolved   |
|                                          | for a release and calculate the average.  |
|                                          | Use formula “=Release Day-Created”.       |
+------------------------------------------+-------------------------------------------+
| Mean time from P3 bug report to delivery | Get list of created date and release      |
|                                          | date for tickets with P3 label resolved   |
|                                          | for a release and calculate the average.  |
|                                          | Use formula “=Release Day-Created”.       |
+------------------------------------------+-------------------------------------------+
| Number of P1 bugs reported in production | Check "P1" Jira labels.                   |
+------------------------------------------+-------------------------------------------+
| Number of P2 bugs reported in production | Check "P2" Jira labels.                   |
+------------------------------------------+-------------------------------------------+
| Number of P3 bugs reported in production | Check "P3" Jira labels.                   |
+------------------------------------------+-------------------------------------------+

Release Management
=================

+----------------------------------------+-----------------------------------------+
| Metric                                 | How to Measure                          |
+========================================+=========================================+
| Number of misses in each release cycle | Same as number of bugs reported in      |
|                                        | production, + count of issues reported  |
|                                        | in documentation or marketing.          |
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
| Community + customer bugs reported      | Use "Customer-bug" and "Community-bug" label for release month, from           |
| during release timeframe (17th to 16th) | 17th to 16th (from previous release day to current release day).               |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Number of customer bugs fixed           | "Customer-bug" tickets closed and marked for current release.                  |
| during release                          |                                                                                |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Total valid bugs in fix version         | After closing current release:                                                 |
|                                         |                                                                                |
|                                         | project = Mattermost AND issuetype = Bug AND resolution not in (Duplicate,     |                                         
|                                         | "Cannot Reproduce", "Won't Fix") AND fixVersion = latestReleasedVersion()      |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Total valid bugs in fix version found   | Check "Se", "Selenium-found, "Rainforest-found" Jira labels.                   |
| by test automation                      |                                                                                |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Total valid bugs found after RC1 is cut | 1. Check Jira timezone + Pre-release timezone and make sure times match        |
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
| version                                 | 1. Project is set to Mattermost                                                |
|                                         | 2. Fix Versions is set to Latest released version                              |
|                                         | 3. Issue Type is set to Story                                                  |
|                                         | 4. Status is set to Closed or Resolved                                         |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Critical security issues found during   | With a new or existing Jira filter, check for Security Vulnerability tickets:  |
| release timeframe                       | 1. Project is set to Mattermost                                                |
|                                         | 2. Fix Versions = Latest released version                                      |
|                                         | 3. Impact = High                                                               |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Moderate security issues found during   | With a new or existing Jira filter, check for Security Vulnerability tickets:  |
| release timeframe                       | 1. Project is set to Mattermost                                                |
|                                         | 2. Fix Versions = Latest released version                                      |
|                                         | 3. Impact = Medium                                                             |
+-----------------------------------------+--------------------------------------------------------------------------------+
| Minor security issues found during      | With a new or existing Jira filter, check for Security Vulnerability tickets:  |
| release timeframe                       | 1. Project is set to Mattermost                                                |
|                                         | 2. Fix Versions = Latest released version                                      |
|                                         | 3. Impact = Low                                                                |
+-----------------------------------------+--------------------------------------------------------------------------------+
