# Release Process

Mattermost core team works on a monthly release process, with a new version shipping on the 16th of each month in [binary form](http://docs.mattermost.com/administration/upgrade.html#mattermost-team-edition). 

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
    - Complete draft of Changelog with updates for latest feature additions, known issues, and contributors
    - Confirm the documentation checklist is up to date compared to the Changelog 
    - Write compatibility updates for config.json and database changes [See example](http://docs.mattermost.com/administration/changelog.html#compatibility)  
    - Confirm changes to config.json in compatibility section of Changelog are written back to [settings documentation](http://docs.mattermost.com/administration/config-settings.html#configuration-settings)
    - Update [Upgrade Guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide) for any steps needed to upgrade to new version
    - Prepare tickets for:
        - [Cutting RC builds](https://mattermost.atlassian.net/browse/PLT-2200)
        - Upgrade [Gitlab Mattermost](https://gitlab.mattermost.com/community/channels/town-square) to RC1
        - Push final build to [GitLab Mattermost](https://gitlab.mattermost.com/community/channels/town-square)
        - [Creating final release candidate](https://mattermost.atlassian.net/browse/PLT-2198)
        - [Testing GitLab RC with Mattermost](https://mattermost.atlassian.net/browse/PLT-2197) 
        - [Push to private cloud customers](https://mattermost.atlassian.net/browse/PLT-2199)
        - [Test upgrade](https://mattermost.atlassian.net/browse/PLT-2344) to latest release based on [upgrade guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide)
        - [RC Build Testing for core team](https://mattermost.atlassian.net/browse/PLT-2208)
    - Coordinate testing:  
        - Work with Ops to check the [Quality Gate](https://github.com/mattermost/process/blob/master/release/quality-gates.md) for feature complete  
        - Receive testing sign-off from feature area owners (i.e. PM/Dev either signs-off that their area is well tested, or flags potential quality issues that may exist)  
        - Check that RC Testing Spreadsheet covers any changes or new features, and ensure core team has access permissions 
        - Assign each area of the release testing spreadsheet to a team member  
        - Queue an item for UX meeting to discuss worst UX bug  
        - Post in Reception alerting community of upcoming release and to ask about top issues on master ([See example](https://pre-release.mattermost.com/core/pl/pfpzwpi7wj8zzpmeih87cdt77r))  
3. Dev:
    - Prioritize reviewing, updating, and merging of pull requests for current release until there are no more tickets in the [pull request queue](https://github.com/mattermost/platform/pulls) marked for the current release 
4. Leads: 
    - Meet to prioritize the final tickets of the release
    - Backlog is reviewed and tickets that won’t make it are moved to next release
    - Post a link to Release Discussion room for query of [remaining tickets in this release](https://mattermost.atlassian.net/issues/?filter=11102)
    - Finalize roadmap for next release  
    - Draft roadmap for release after next (used to prioritize design tasks)  
5. Marketing:
    - Drafts marketing bullet points for next release based off of roadmap  
    - Notes date of marketing announcement for the release in release channel  
6. Team:
    - In Stand-up, each team member discusses worst bug (10-15s)
 
### C. (T-minus 8 working days) Code Complete and Release Candidate Cut

**Stablization** period begins when all features for release have been committed. During this period, only **bugs** can be committed to the release branch. Non-bug pull requests are tagged for next version.

Exceptions can be made by the release manager setting priority to "Highest" and adding a "release-exception" label to the Jira ticket. This will add the ticket to the [hotfix list for release candidate](https://mattermost.atlassian.net/issues/?filter=10204).

1. Logistics:
    - Post this checklist in Release channel
    - Update the channel header to reflect finalized marketing release date
    - For the next release, create team meetings on Code Complete date
    - Mail out mugs to any new contributors (platform and docs repo)
    - Confirm documentation is complete, read through documentation and confirm all links work
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Dev:
    - Prioritize reviewing, updating, and merging of pull requests for current release until there are no more tickets in the [pull request queue](https://github.com/mattermost/platform/pulls) marked for the current release 
3. PM:
    - Review all [Severity 1 bugs (data loss or security)](https://mattermost.atlassian.net/secure/IssueNavigator.jspa?mode=hide&requestId=10600) to consider for adding to Hotfix list
    - Update documentation:  
        - Submit Changelog PR  
        - Make NOTICE.txt PR for any new libraries added from dev, if not added already   
        - Prioritize any developer documentation tickets  
        - Draft [GitLab ticket](https://gitlab.com/gitlab-org/omnibus-gitlab/issues/942) to take next Mattermost version in the Omnibus, but do not post until RC1 is cut  
4. **(Team) Code Complete Meeting (10:15am PST)**:  
    - (PM) Leads team review of Changelog  
    - (Team) Each team member discusses worst bug (10-15s)  
    - (Logistics) Walk through each unfinished item of this checklist  
    - (Dev) Last check of tickets that need to be merged before RC1  

5. Build:  
    - Master is tagged and branched and “Release Candidate 1″ is cut (e.g. 1.1.0-RC1) according to the [Release Candidate Checklist](https://github.com/mattermost/process/blob/master/release/create-release-candidate.md) 
    - CI servers are updated to the release branch  
6. PM:  
    - Create meta issue for regressions in GitHub (see [example](https://github.com/mattermost/platform/issues/574))  
    - Include link to meta-issue in release notes of RC1  
7. Marketing:
    - Tweet announcement that RC1 is ready (see [example](https://twitter.com/mattermosthq/status/664172166368264192))
    - Submits pull request for "Highlights" section of the Changelog 
    - Communicate checklist of items needed by specific dates to write the blog post announce (e.g. screenshots, GIFs, documentation) and begins to write the blog post, tweet, and email for the release announcement  
 
### E. (T-minus 7 working days) Release Candidate Testing 

1. Logistics:
    - Post this checklist in Release channel
    - Add “Release Retrospective” item to next team meeting in place of Kaizen/User Issues
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Build:
    - Test upgrade from previous version to current version, following the [Upgrade Guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide) 
    - Database upgrade should be tested on both MySQL and Postgres
3. PM:
    - Update Release Discussion header with links to RC instances and testing spreadsheet
    - Post release testing instructions to Release Discussion channel ([example](https://pre-release.mattermost.com/core/pl/8z1tazpmm3ycbrehju36brd5nh))
    - Post to Reception directing community testers to the Release Discussion channel for details
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
    - Check that the contributors section of Changelog is updated (including contributors from all repos)
6. Dev:
    - PRs for hotfixes made to release branch
    - Review PRs made from release branch and merge changes into both the release branch and master
7. Logistics:
    - Test RC fixes as they come in on CI servers
8. Build: 
    - Push next RC to acceptance after testing is complete and approved fixes merged, announces in Town Square on pre-release.mattermost.com/core
9. PM:
    - Closes the meta issue after the next RC is cut, and opens another ticket for new RC
    - Test tickets on the new RC that were merged to the release branch.
10. Ops:
    - Verifies each of the issues in meta ticket is fixed
 
### F. (T-minus 2 working days) Release Build Cut

The final release is cut. If an urgent and important issue needs to be addressed between major releases, a bug fix release (e.g. 1.1.1) may be created

1. Logistics:
    - Post this checklist in Release channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager.
2. Build:
    - Tags a new release (e.g. 1.1.0) and runs an official build which should be essentially identical to the last RC
    - Delete RCs after final version is shipped
3. PM:
    - Submit GitLab ticket to take next Mattermost version in the Omnibus using [template](https://gitlab.com/gitlab-org/omnibus-gitlab/issues/1241)
    - Update the mattermost.org/download page
    - Add the download links to http://docs.mattermost.com/administration/upgrade.html#version-archive
    - Contact owners of [community installers](http://www.mattermost.org/installation/) or submit [PRs](https://github.com/tommyvn/mattermost-heroku/commit/94f7c5c0c5d7d2672fb6d62b6a560b4b5c1b5131) to update install version number.
    - Update the AMI links on mattermost.org/download and mattermost.org/installation  
    - Close final GitHub RC meta ticket  
4. Marketing:
    - Finalize Mailchimp email blast
    - Finalize blog post for mattermost.org set timer for 06:00 PDT on first non-holiday weekday morning after release
    - Queue Tweet announcement
    - Find [GitLab release announcement merge request](https://gitlab.com/gitlab-com/www-gitlab-com/merge_requests) and post proposal for [GitLab Mattermost update text](https://gitlab.com/gitlab-com/www-gitlab-com/merge_requests/1633/diffs#efdba966a222d7071509e0dd4f39de5c9d7c1200_0_185)

### G. (T-minus 0 working days) Release Day

1. Logistics: 
    - Post this checklist in Release channel 
    - Post key dates for the next release in the header of the Release Discussion channel and remove links to RC candidates and testing spreadsheet
    - Verify all items in the last posted release checklist are complete, if not alert the release manager.
2. PM:
    - Close the release in Jira
    - Create [documentation checklist ticket](https://mattermost.atlassian.net/browse/PLT-2373) for next release
    - Create a performance improvement ticket for next release, and move to the sprint before feature complete
3. Dev:
    - Check if any libraries need to be updated for the next release, and if so bring up in weekly team meeting
    - Test the GitLab RC containing the Mattermost final bits
    - Confirm gitlab.mattermost.com is updated to final build
4. Marketing:
    - Confirm marketing has been posted (animated GIFs, screenshots, mail announcement, tweets, blog posts)


## Templates


Templates for GitLab announcement proposal
```
Proposed update for new version of [Mattermost](https://gitlab.com/gitlab-org/omnibus-gitlab/issues/1241). 

## GitLab Mattermost 2.2

[Mattermost 2.2](http://www.mattermost.org/mattermost-2-2-threaded-messages-and-more/) ships in GitLab 8.7 with threaded messages, French translation, new themes, new Trello and IRC support, plus many more new benefits. 

This version also includes security updates and [upgrade from earlier versions]((http://doc.gitlab.com/omnibus/gitlab-mattermost/)) is recommended.
```




## Release Numbering 

Mattermost numbers its stable releases based on the following format:  
  `[Version Number].[Major Build Number].[Minor Build Number]`

Version Number:
- Indicates a major system release (e.g. 1.x.x, 2.x.x)

Major Build Number:
- Indicates significant new functionality, (e.g. 0.5.x, 0.6.x, 0.7.x)

Minor Build Number:
- Indicates a bug fix or security release (e.g. 1.2.5, 1.2.6)

