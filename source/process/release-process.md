# Release Process

Mattermost core team works on a monthly release process, with a new version shipping on the 16th of each month in [binary form](https://github.com/mattermost/platform/releases). 

This document outlines the development process for the Mattermost core team, which draws from what we find works best for us from Agile, Scrum and Software Development Lifecycle approaches.

## Release Timeline

Notes: 
- All cut-off dates are based on 10am PST (UTC-07/08) on the day stated. 
- T-minus counts are measured in "working days" (weekdays other than major holidays concurrent in US and Canada) prior to release day.

### A. (Code complete date of previous release) Beginning of release

Pre-work for the current release begins at the code complete date of the previous release. See "Code Complete" section below for details.

### B. (T-minus 10 working days) Cut-off for major features

No pull requests for major features should be submitted to the current release after this date (except if release manager decides to add "release-exception" label to Jira ticket).

1. Logistics:
    - Post this checklist in Release channel 
2. PM:
    - Draft Changelog with updates for latest feature additions, known issues, and contributors
    - Write compatibility updates for config.json and database changes [See example](https://github.com/mattermost/platform/blob/master/CHANGELOG.md#compatibility)  
    - Confirm changes to config.json in compatibility section of Changelog are written back to [settings documentation](https://github.com/mattermost/docs/blob/master/source/administration/config-settings.md)
    - Update [Upgrade Guide](https://github.com/mattermost/docs/blob/master/source/administration/upgrade.md) for any steps needed to upgrade to new version
    - Prepare tickets for:
        - [Cutting RC builds](https://mattermost.atlassian.net/browse/PLT-2200)
        - [Creating final release candidate](https://mattermost.atlassian.net/browse/PLT-2198)
        - [Testing GitLab RC with Mattermost](https://mattermost.atlassian.net/browse/PLT-2197) 
        - [Pushing to Battlehouse](https://mattermost.atlassian.net/browse/PLT-2199)
        - [Test upgrade](https://mattermost.atlassian.net/browse/PLT-2344) to latest release based on [upgrade guide](https://github.com/mattermost/docs/blob/master/source/administration/upgrade.md)
        - [RC Build Testing for core team](https://mattermost.atlassian.net/browse/PLT-2208)
        - Updating gitlab.mattermost.com to RC1, and then updating gitlab.mattermost.com to final build
    - Queue an item for UX meeting to discuss worst UX bug  
    - Post in Reception alerting community of upcoming release and to ask about top issues on master ([See example](https://pre-release.mattermost.com/core/pl/pfpzwpi7wj8zzpmeih87cdt77r))  
3. Dev:
    - Prioritize reviewing, updating, and merging of pull requests for current release until there are no more tickets in the [pull request queue](https://github.com/mattermost/platform/pulls) marked for the current release 
4. Leads: 
    - Meet to prioritize the final tickets of the release
    - Backlog is reviewed and major features that won’t make it are moved to next release
    - Post a link to Release Discussion room for query of [remaining tickets in this release](https://mattermost.atlassian.net/issues/?filter=11102)
    - Finalize roadmap for next release  
    - Draft roadmap for release after next (used to prioritize design tasks)  
5. Marketing:
    - Drafts marketing bullet points for next release based off of roadmap  
    - Notes date of marketing announcement for the release in release channel  
6. Team:
    - In Stand-up, each team member discusses worst bug (10-15s)
 
### C. (T-minus 8 working days) Feature Complete and Stabilization

**Stablization** period begins when all features for release have been committed. During this period, only **bugs** can be committed to master. Non-bug pull requests are tagged for next version, and are not committed to master until after a release candidate is cut.

Exceptions can be made by the release manager setting priority to "Highest" and adding a "release-exception" label to the Jira ticket. This will add the ticket to the [hotfix list for release candidate](https://mattermost.atlassian.net/issues/?filter=10204).

1. Logistics:
    - Post this checklist in Release channel
    - Update the channel header to reflect finalized marketing release date
    - Mail out mugs to any new contributors
2. Dev:
    - Prioritize reviewing, updating, and merging of pull requests for current release until there are no more tickets in the [pull request queue](https://github.com/mattermost/platform/pulls) marked for the current release 
3. PM:
    - Review all [Severity 1 bugs (data loss or security)](https://mattermost.atlassian.net/secure/IssueNavigator.jspa?mode=hide&requestId=10600) to consider for adding to Hotfix list
    - Update documentation:  
        - Submit Changelog PR  
        - Make NOTICE.txt PR for any new libraries added from dev, if not added already  
        - Create a checklist of documentation needed based off of Changelog  
        - Prioritize any developer documentation tickets  
        - Draft [GitLab ticket](https://gitlab.com/gitlab-org/omnibus-gitlab/issues/942) to take next Mattermost version in the Omnibus, but do not post until RC1 is cut  
    - Coordinate testing:  
        - Work with Ops to check the [Quality Gate](https://github.com/mattermost/process/blob/master/release/quality-gates.md) for feature complete  
        - Receive testing sign-off from feature area owners (i.e. PM/Dev either signs-off that their area is well tested, or flags potential quality issues that may exist)  
        - Update RC Testing Spreadsheet with any new features and ensure core team has access permissions. 
        - Post in Release Discussion room asking what the current worst bug/issue is  
4. **(Team) Feature Complete Meeting (10:15am PST)**:  
    - (PM) Leads team review of Changelog  
    - (Team) Each team member discusses worst bug (10-15s)  
5. Marketing:
    - Submits pull request for "Highlights" section of the Changelog 
    - Communicate checklist of items needed by specific dates to write the blog post announce (e.g. screenshots, GIFs, documentation) and begins to write the blog post, tweet, and email for the release announcement  

### D. (T-minus 5 working days) Code Complete and Release Candidate Cut 

1. Logistics:  
    - Post this checklist in Release channel  
    - For the next release, create team meetings on Feature Complete and Code Complete dates  
    - Confirms documentation is complete, reads through documentation and confirms all links work  
2. PM:  
    - Remove "Under Development" notice for current release from Changelog on master  
    - Assign each area of the release testing spreadsheet to a team member  
    - Update the release start date for the next release in Jira (setting [here](https://mattermost.atlassian.net/plugins/servlet/project-config/PLT/versions))  
3. **(Team) Code Complete Meeting (10:15am PST meeting)**  
    - (Logistics) Walk through each unfinished item of this checklist  
    - (Dev) Last check of tickets that need to be merged before RC1  
    - (Team) Each team member discusses worst bug (10-15s)  
    - **Code Complete** is declared after meeting  
4. Dev:  
    - Prioritize reviewing, updating, and merging of pull requests for current release until there are no more tickets in the [pull request queue](https://github.com/mattermost/platform/pulls) marked for the current release  
5. Build:  
    - Master is tagged and branched and “Release Candidate 1″ is cut (e.g. 1.1.0-RC1) according to the [Release Candidate Checklist](https://github.com/mattermost/process/blob/master/release/create-release-candidate.md)  
6. PM:  
    - Create meta issue for regressions in GitHub (see [example](https://github.com/mattermost/platform/issues/574))  
    - Include link to meta-issue in release notes of RC1  
7. Marketing:  
    - Tweet announcement that RC1 is ready (see [example](https://twitter.com/mattermosthq/status/664172166368264192))  
 
### E. (T-minus 4 working days) Release Candidate Testing 

1. Logistics:
    - Post this checklist in Release channel
    - Add Release Process Kaizen/Q&A item to next team meeting
2. Build:
    - Test upgrade from previous version to current version, following the [Upgrade Guide](https://github.com/mattermost/docs/blob/master/source/administration/upgrade.md) 
    - Database upgrade should be tested on both MySQL and Postgres
3. PM:
    - Update Release Discussion header with links to RC instances and testing spreadsheet
    - Post release testing instructions to Release Discussion channel ([example](https://pre-release.mattermost.com/core/pl/8z1tazpmm3ycbrehju36brd5nh)). 
    - Post to Reception directing community testers to the Release Discussion channel for details.
    - Post "Known Issues" to Release Discussion channel
4. Team:
    - Test assigned areas of the Release Candidate Testing Spreadsheet and file any bugs found in Jira
    - Post a link to any "Blocking" issue that may need a hotfix to the RC in the Release room, with the **#p1** tag. If the issue is security related or contains confidential information, post the link in the Confidential Bugs private group. Blocking issues are considered to be security issues, data loss issues, issues that break core functionality, or significantly impact aesthetics.
    - Triage hotfix candidates and decide on whether and when to cut next RC or final
    - If no blocking issues are found, PM, Dev and Ops signs off on the release
5. PM:
    - Post links to all issues found in RC as comments on the meta issue
    - Update the meta issue description to include approved fixes
    - Post screenshot and link to final tickets for next RC to the Release room
    - Update Changelog “Known Issues” section with any significant issues that were found and not fixed for the final release
6. Dev:
    - PRs for hotfixes made to release branch, and changes from release branch are merged into master
7. Logistics:
    - For potentially destabilizing changes, test approved fixes on a spinmint private build
8. Build: 
    - Push next RC to acceptance after testing is complete and approved fixes merged, announces in Town Square on pre-release.mattermost.com/core
9. PM:
    - Closes the meta issue after the next RC is cut, and opens another ticket for new RC
10. Ops:
    - Verifies each of the issues in meta ticket is fixed
 
### F. (T-minus 2 working days) Release Build Cut

The final release is cut. If an urgent and important issue needs to be addressed between major releases, a bug fix release (e.g. 1.1.1) may be created

1. Logistics:
    - Post this checklist in Release channel 
2. Build:
    - Tags a new release (e.g. 1.1.0) and runs an official build which should be essentially identical to the last RC
    - Delete RCs after final version is shipped
3. PM:
    - Submit GitLab ticket to take next Mattermost version in the Omnibus  
    - Copy and paste the Release Notes from the Changelog to the Release Description  
    - Update the mattermost.org/download page  
    - Update the AMI links on mattermost.org/download and mattermost.org/installation  
    - Close final GitHub RC meta ticket  
4. Marketing:
    - Finalize mailchimp email blast
    - Finalize blog post and put on timer for release
    - Finalize tweet announcement
    - Finalize announcement on general mailing list
    - Finalize announcement for gitlab.mattermost.com

### G. (T-minus 0 working days) Release Day

1. Logistics: 
    - Post this checklist in Release channel 
    - Post key dates for the next release in the header of the Release channel
2. PM:
    - Close the release in Jira
    - Set header of next release as UNDER DEVELOPMENT in CHANGELOG on master
3. Dev:
    - Check if any libraries need to be updated for the next release, and if so bring up in weekly team meeting
    - Test the GitLab RC containing the Mattermost final bits
4. Marketing:
    - Confirm marketing has been posted (animated GIFs, screenshots, mail announcement, tweets, blog posts)

## Release Numbering 

Mattermost numbers its stable releases based on the following format:  
  `[Version Number].[Major Build Number].[Minor Build Number]`

Version Number:
- Indicates a major system release (e.g. 1.x.x, 2.x.x)

Major Build Number:
- Indicates significant new functionality, (e.g. 0.5.x, 0.6.x, 0.7.x)

Minor Build Number:
- Indicates a bug fix or security release (e.g. 1.2.5, 1.2.6)

