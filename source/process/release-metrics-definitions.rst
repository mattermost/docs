Release Metrics Definitions
------------------

Release Output
==============

+------------------------------------------+----------------------------------------+
| Metric                                   | How to Measure                         |
+==========================================+========================================+
| Ratio of story-to-bug tickets            |                                        |
+------------------------------------------+----------------------------------------+
| Mean time from P1 bug report to delivery |                                        |
+------------------------------------------+----------------------------------------+
| Mean time from P2 bug report to delivery |                                        |
+------------------------------------------+----------------------------------------+
| Mean time from P3 bug report to delivery |                                        |
+------------------------------------------+----------------------------------------+
| Number of P1 bugs reported in production |                                        |
+------------------------------------------+----------------------------------------+
| Number of P2 bugs reported in production |                                        |
+------------------------------------------+----------------------------------------+
| Number of P3 bugs reported in production |                                        |
+------------------------------------------+----------------------------------------+

Release Management
=================

+----------------------------------------+-----------------------------------------+
| Metric                                 | How to Measure                          |
+========================================+=========================================+
| Number of misses in each release cycle | E.g. dot releases from customer reports,|
|                                        | undocumented breaking changes           |
+----------------------------------------+-----------------------------------------+
| Number of setbacks to users/staff      | Manual count of negative reactions      |
| resulting in a negative reaction       | reported by CSMs, Support or Product.   |
|                                        | E.g. features that got pushed.          |
+----------------------------------------+-----------------------------------------+
| Number of measurable actions from each | Action items driven from root causes.   |
| release retrospective completed        |                                         |
| and reported to R&D                    |                                         |
+----------------------------------------+-----------------------------------------+
| Number of deadlines missed in release  |                                         |
| checklist                              |                                         |
+----------------------------------------+-----------------------------------------+

Release Heartbeat
=================

+-----------------------------------------+------------------------------------------------------------------------------+
| Metric                                  | How to Measure                                                               |
+=========================================+==============================================================================+
| Time updated to RC1 (PST)               | Check Release Discussion channel history                                     |
|                                         | for date/time RC1 was cut.                                                   |
+-----------------------------------------+------------------------------------------------------------------------------+
| How many RCs cut                        | Check Release Discussion channel history                                     |
|                                         | for how many RCs were cut for that release.                                  |
+-----------------------------------------+------------------------------------------------------------------------------+
| Number of days between when final RC    | Check Release Discussion channel for post with official release build.       |
| is cut and the release date             | Oxygen = 16th - Day Final RC is cut                                          |
+-----------------------------------------+------------------------------------------------------------------------------+
| Community + customer bugs reported      | Use "Customer-bug" and "Community-bug" label for release month, from         |
| during release timeframe (17th to 16th) | 17th to 16th (from previous release day to current release day).             |
+-----------------------------------------+------------------------------------------------------------------------------+
| Number of customer bugs fixed           | "Customer-bug" tickets closed and marked for current release.                |
| during release                          |                                                                              |
+-----------------------------------------+------------------------------------------------------------------------------+
| Total valid bugs in fix version         | After closing current release:                                               |
|                                         |                                                                              |
|                                         | project = Mattermost AND issuetype = Bug AND resolution not in (Duplicate,   |                                         
|                                         | "Cannot Reproduce", "Won't Fix") AND fixVersion = latestReleasedVersion()    |
+-----------------------------------------+------------------------------------------------------------------------------+
| Total valid bugs in fix version found   | Check "Se", "Selenium-found, "Rainforest-found" Jira labels                  |
| by test automation                      |                                                                              |
+-----------------------------------------+------------------------------------------------------------------------------+
| Total valid bugs found after RC1 is cut | 1. Check Jira timezone + Pre-release timezone and make sure times match      |
|                                         | 2. Replace START with date (yyyy-MM-dd HH:mm) RC1 was cut                    |
|                                         | 3. Replace END with date (yyyy-MM-dd HH:mm) test servers returned to master  |
|                                         |                                                                              |
|                                         | project = Mattermost AND issuetype = Bug AND resolution not in (Duplicate,   |
|                                         | "Cannot Reproduce", "Won't fix") AND created > "START" AND created < "END"   |
+-----------------------------------------+------------------------------------------------------------------------------+
| Valid bugs found after RC1 fixed in     | After closing current release, & adjust dates as per above:                  |
| release                                 |                                                                              |
|                                         | project = Mattermost AND issuetype = Bug AND resolution not in (Duplicate,   |
|                                         | "Cannot Reproduce", "Won't Fix")  AND created > "START" AND created < "END"  |
|                                         | AND fixVersion = latestReleasedVersion()                                     |
+-----------------------------------------+------------------------------------------------------------------------------+
| Valid bugs found after RC1 pushed to    | After closing current release, & adjust dates as per above:                  |
| next release                            |                                                                              |
|                                         | project = Mattermost AND issuetype = Bug AND resolution not in (Duplicate,   |                                      
|                                         | "Cannot Reproduce", "Won't Fix") AND created > "START" AND created < "END"   |
|                                         | AND fixVersion = earliestUnreleasedVersion()                                 |
+-----------------------------------------+------------------------------------------------------------------------------+
| Valid bugs found after RC1 fix version  | project = Mattermost AND issuetype = Bug AND created > "START" AND created < |  
| = other (eg unscheduled, not set)       | "END" AND resolution not in (Duplicate, "Cannot Reproduce", "Won't Fix") AND |
|                                         | (fixVersion not in (latestReleasedVersion(), earliestUnreleasedVersion()) OR |
|                                         | fixVersion is EMPTY)                                                         |
+-----------------------------------------+------------------------------------------------------------------------------+
| (Non-security) Bugs requiring patch     | After any patch release goes out (after the normal release date):            |
| release                                 | Check Changelog for total number of non-security patch releases.             |
+-----------------------------------------+------------------------------------------------------------------------------+
| Total features/improvements in fix      | Check number of Story tickets completed for the release.                     |
| version                                 |                                                                              |
+-----------------------------------------+------------------------------------------------------------------------------+
| Critical security issues found during   | Check Jira security board for issues where:                                  |
| release timeframe                       | 1. Date reported is between the 16th of last month and the 16th of the       |
|                                         | release month.                                                               |
|                                         | 2. Impact = High                                                             |
+-----------------------------------------+------------------------------------------------------------------------------+
| Moderate security issues found during   | Check Jira security board for issues where:                                  |
| release timeframe                       | 1. Date reported is between the 16th of last month, and the 16th of the      |
|                                         | release month.                                                               |
|                                         | 2. Impact = Medium                                                           |
+-----------------------------------------+------------------------------------------------------------------------------+
| Minor security issues found during      | Check Jira security board for issues where:                                  |
| release timeframe                       | 1. Date reported is between the 16th of last month, and the 16th of the      |
|                                         | release month.                                                               |
|                                         | 2. Impact = Low                                                              |
+-----------------------------------------+------------------------------------------------------------------------------+

