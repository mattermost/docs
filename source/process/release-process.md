# Release Process

Mattermost core team works on a monthly release process, with a new version shipping on the 16th of each month in [binary form](http://docs.mattermost.com/administration/upgrade.html#mattermost-team-edition). 

This document outlines the development process for the Mattermost core team, which draws from what we find works best for us from Agile, Scrum and Software Development Lifecycle approaches.

## Release Timeline

Notes: 
- All cut-off dates are based on 10am PST (UTC-07/08) on the day stated. 
- T-minus counts are measured in "working days" (weekdays other than major holidays concurrent in US and Canada) prior to release day.

### A. (Code complete date of previous release) Beginning of release

Pre-work for the current release begins at the code complete date of the previous release. See "Code Complete" section below for details.

T-15: B. (T-minus 15 working days) Cut-off for submitting major features (to be enforced with Mattermost 3.5)

No pull requests for major features should be **submitted** to the current release after this date (except if release manager decides to add "release-exception" label to Jira ticket).

T-14: C. (T-minus 14 working days) Judgment Day

Day when leads and PM area owners meet to discuss which major features will be cut from the release, if any.

1. Logistics:
    - Post this checklist in Release channel 
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. PM/Dev:
    - Prioritize review of major features submitted for current release
3. Leads:
    - Meet with PM area owners to discuss release update and decide which major features will be in or out for the release
4. Marketing:
    - Confirm each Enterprise feature is in the correct [pricing SKU](https://about.mattermost.com/pricing/), if not alert the release manager

### D. (T-minus 12 working days) Cut-off for merging major features

No pull requests for major features should be **merged** to the current release after this date (except if release manager decides to add "release-exception" label to Jira ticket).

1. Logistics:
    - Post this checklist in Release channel 
    - Begin posting Zero Bug Balance query daily
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. PM:
    - PM area owners complete draft of Changelog in a WIP PR with updates for highlights, feature additions, known issues, compatibility updates for config.json, database and [API changes](https://github.com/mattermost/platform/commits/release-3.3/model/client.go) changes ([see example](http://docs.mattermost.com/administration/changelog.html#compatibility))
    - Confirm changes to config.json in compatibility section of Changelog are written back to [settings documentation](http://docs.mattermost.com/administration/config-settings.html#configuration-settings)
    - Update [Upgrade Guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide) for any steps needed to upgrade to new version
    - Submit NOTICE.txt PR for any new libraries added from dev, if not added already. The following two files contain a list of dependancies:
        - https://github.com/mattermost/platform/blob/master/webapp/package.json
        - https://github.com/mattermost/platform/blob/master/glide.yaml
    - Create meta issue for release in GitHub (see [example](https://github.com/mattermost/platform/issues/3702)).
    - Coordinate testing:  
        - Work with Ops to check the Quality Gate for feature complete.  
        - Receive testing sign-off from feature area owners (i.e. PM/Dev either signs-off that their area is well tested, or flags potential quality issues that may exist)  
        - Check that RC Testing Spreadsheet covers any changes or new features, and that known issues are listed in the relevant tests
        - Assign each area of the release testing spreadsheet to a team member and ensure core team has access permissions 
        - Post in Reception alerting community of upcoming release and to ask about top issues on master ([See example](https://pre-release.mattermost.com/core/pl/pfpzwpi7wj8zzpmeih87cdt77r))  
    - PM owners for each new feature prepare a section highlighting end-user benefits for the blog post and post to the Marketing room, including screenshots. See [example thread](https://pre-release.mattermost.com/core/pl/o611i4wz3pfafb6fpha9ggxxnh) for formatting.
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
    - Communicates checklist of items needed by specific dates to write the blog post announce (e.g. screenshots, GIFs, documentation) and begins to write the blog post, tweet, and email for the release announcement
 
### E. (T-minus 8 working days) Code Complete and Release Candidate Cut

**Stablization** period begins when all features for release have been committed. During this period, only **bugs** can be committed to the release branch. Non-bug pull requests are tagged for next version.

Exceptions can be made by the release manager setting priority to "Highest" and adding a "release-exception" label to the Jira ticket. This will add the ticket to the [hotfix list for release candidate](https://mattermost.atlassian.net/issues/?filter=10204).

1. Logistics:
    - Post this checklist in Release channel
    - Update the channel header to reflect finalized marketing release date
    - Mail out mugs to any new contributors
    - Update [Team](http://www.mattermost.org/team/) page with new contributors
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Dev:
    - Prioritize reviewing, updating, and merging of pull requests for current release until there are no more tickets in the [pull request queue](https://github.com/mattermost/platform/pulls) marked for the current release 
3. PM:
    - Review all [Severity 1 bugs (data loss or security)](https://mattermost.atlassian.net/secure/IssueNavigator.jspa?mode=hide&requestId=10600) to consider for adding to Hotfix list
    - Gather a list of contributors across all [public Mattermost GitHub repos](https://github.com/mattermost/), and add to the Changelog draft
    - Update documentation:  
        - Submit Changelog PR 
        - Submit Changelog PR for [/ios](https://github.com/mattermost/ios) and [/android](https://github.com/mattermost/android) repositories
        - Prioritize any developer documentation tickets  
        - Draft [Mattermost Security Updates](http://about.mattermost.com/security-updates/), but do not post until seven days after official release
4. **(Team) Code Complete Meeting (10:15am PST)**:  
    - (PM) Leads team review of Changelog 
    - (Logistics) Walk through each unfinished item of this checklist  
    - (Dev) Last check of tickets that need to be merged before RC1  
5. Build:  
    - Master is tagged and branched and “Release Candidate 1″ is cut (e.g. 1.1.0-RC1) according to the Release Candidate Checklist in ``mattermost/process``
    - CI servers are updated to the release branch
    - Translation server is locked to the release branch
    - Directory structure is reviewed and large changes posted to the team channel
6. PM:  
    - Merge changelog PR after team review is complete. Post a link to the changelog on the documention branch in the GitHub meta issue.
7. Marketing:
    - Tweet announcement that RC1 is ready (see [example](https://twitter.com/mattermosthq/status/664172166368264192))
 
### F. (T-minus 7 working days) Release Candidate Testing 

1. Logistics:
    - Post this checklist in Release channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Dev:
    - Test upgrade from previous version to current version, following the [Upgrade Guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide) with database upgrades on both MySQL and Postgres
3. PM:
    - Update Release Discussion header with links to RC instances and testing spreadsheet
    - Post release testing instructions to Release Discussion channel ([example](https://pre-release.mattermost.com/core/pl/8z1tazpmm3ycbrehju36brd5nh))
    - Post to Reception directing community testers to the Release Discussion channel for details
    - Post "Known Issues" to Release Discussion channel
4. Team:
    - Test assigned areas of the Release Candidate Testing Spreadsheet and file any bugs found in Jira
    - Post a link to any "Blocking" issue that may need a hotfix to the RC in the Release room, with the **#p1** tag. If the issue is security related or contains confidential information, post the link in the Confidential Bugs private group. Blocking issues are considered to be security issues, data loss issues, issues that break core functionality, or significantly impact aesthetics.
    - Triage hotfix candidates and decide on whether and when to cut next RC or final
5. PM:
    - Update the meta issue:
        - Post comments to the meta issue with approved fixes for the next RCs
        - Download links and testing server links to the RCs
    - Post screenshot and link to final tickets for next RC to the Release Discussion room
    - Update Changelog “Known Issues” section with any significant issues that were found and not fixed for the final release
6. Dev:
    - PRs for hotfixes made to release branch
    - Review PRs made from release branch and merge changes into both the release branch and master
7. Logistics:
    - Test RC fixes as they come in on CI servers
8. Build: 
    - Push next RC to acceptance and announces in Town Square with new RC link after testing is complete and approved fixes are merged. Build manager verifies with release manager before cutting any new RCs.
9. PM:
    - Test tickets on the new RC that were merged to the release branch and post in Release channel after testing
10. Ops:
    - Verifies each of the issues in meta ticket is fixed
 

### G. (T-minus 5 working days) Release Candidate Testing Finished 

1. Logistics:
    - Post this checklist in Release channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Team:
    - Finish assigned areas of the Release Candidate Testing Spreadsheet
    - Continue triaging hotfix candidates and decide on whether and when to cut next RC or final
    - If no blocking issues are found, PM, Dev and Ops signs off on the release
3. PM:
    - Queue an item for UX meeting to discuss worst UX bug
    - Queue an item for Release Update meeting to discuss worst bug
    - Check that known issues section of Changelog is updated
    - Check that the contributors section of Changelog is updated (including contributors from all repos)
    - Submit all doc PRs for review
4. Marketing:
    - Finish draft of blog post for mattermost.org and send for marketing lead to review
        - Upgrade should be recommended if there are security fixed in v3.3
    - Finish drafts of all art work (screenshots, GIFs and twitter banners) used for the blog post and send for marketing lead to review

### H. (T-minus 2 working days) Release Build Cut

The final release is cut. If an urgent and important issue needs to be addressed between major releases, a bug fix release (e.g. 1.1.1) may be created.

1. Logistics:
    - Post this checklist in Release channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager.
2. Build:
    - Tags a new release (e.g. 1.1.0) and runs an official build which should be essentially identical to the last RC. 
3. PM:
    - Post in Release Discussion with links to the EE and Team Edition bits.
    - Update the [Mattermost server download page](mattermost.org/download)
    - Add the download links to [upgrdae guide](http://docs.mattermost.com/administration/upgrade.html#version-archive)
    - Contact owners of [community installers](http://www.mattermost.org/installation/) or submit [PRs](https://github.com/tommyvn/mattermost-heroku/commit/94f7c5c0c5d7d2672fb6d62b6a560b4b5c1b5131) to update install version number.
    - Close GitHub meta ticket for the release.
    - Merge the docs release branch to master and verify all changes on docs.mattermost.com once the build is up. Submit a correction PR for any incorrect formatting or other errors missed during the intitial review.
    - Update [MVP page](https://www.mattermost.org/mvp/) with the most valuable contributor of the release.
    - Submit GitLab MR for `config/software/mattermost.rb` to take next Mattermost version in the Omnibus. The MR should include changes to the `default_version` and `md5` sum (see [example](https://gitlab.com/gitlab-org/omnibus-gitlab/merge_requests/933/diffs)
    - Update [Docker preview image to latest version](https://github.com/mattermost/mattermost-docker-preview/commit/1c34195d70b26bd4c82b5ef4fa0ebaf421096881).
4. Marketing:
    - Finalize Mailchimp email blast
    - Finalize blog post for mattermost.org and set timer for 06:00 PDT on the day of release.
    - Queue Tweet announcement

If a bug fix release is required, run through the following steps again: 

1. Build:  
    - Tag a new release (e.g. 1.1.1) and run an official build  
    - Update testing sites to the final version  
2. PM:  
    - Update [Mattermost server download page](the https://mattermost.org/download)
    - Update [Mattermost pricing page](https://about.mattermost.com/pricing/)
    - Add the download links to http://docs.mattermost.com/administration/upgrade.html#version-archive  
    - Update the Changelog with notes on patch releases (see [example entry](https://docs.mattermost.com/administration/changelog.html#release-v3-0-3))  
3.  Ops:  
    - Verifies each of the issues in the patch release are fixed  

### I. (T-minus 0 working days) Release Day

1. Logistics: 
    - Post this checklist in Release channel 
    - Post key dates for the next release in the header of the Release Discussion channel and remove links to RC candidates and testing spreadsheet
    - Verify all items in the last posted release checklist are complete, if not alert the release manager.
    - For the next release, create the following team meetings:
        - Code Complete Meeting on T-8
        - Team-wide Triage each weekday starting at T-7 and ending at T-2, with optional attendance
        - Release Update each weekday starting at T-7 and ending at T-2
    - For the next release, create PM Release Update meeting on T-14
    - Add “Release Retrospective” item to next team meeting in place of Kaizen/User Issues, asking each core team member to give a letter grade (and brief explanation) for:
        - Release Quality
        - Release Process
        - Testing Process
2. PM:
    - Close the release in Jira
    - Prepare tickets for the next release,  with a corresponding vX.X prefix
        - [Performance improvement ticket](https://mattermost.atlassian.net/browse/PLT-3363)
        - [Update testing spreadsheet](https://mattermost.atlassian.net/browse/PLT-3044)
        - [Creating final release candidate](https://mattermost.atlassian.net/browse/PLT-2198)
        - [Test Gitlab Omnibus RC install of Mattermost](https://mattermost.atlassian.net/browse/PLT-2197) 
        - [Push to private cloud customers](https://mattermost.atlassian.net/browse/PLT-2199)
        - [Push to private long-running feature branches](https://mattermost.atlassian.net/browse/PLT-2199)
        - [Test upgrade](https://mattermost.atlassian.net/browse/PLT-2344) to latest release based on [upgrade guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide)
        - [RC Build Testing for core team](https://mattermost.atlassian.net/browse/PLT-2208)
        - [Upgrade GitLab Mattermost to RC1](https://mattermost.atlassian.net/browse/PLT-3116)
        - [Push final build to GitLab Mattermost](https://mattermost.atlassian.net/browse/PLT-3117)
        - [Cut build and set up RC1 servers](https://mattermost.atlassian.net/browse/PLT-3115)
    - Create [PR tracking spreadsheet](https://docs.google.com/spreadsheets/d/1YkRqyQk0Y4ZouV-SsXbSjbzGOXu2ZSPSd4XC_4LAErI/edit#gid=0) for next release.
        - Populate with any PR's that have already went in for the next release.
        - Zapier manager updates GitHub automation zap to new PR tracking spreadsheet.
    - Create a new branch on docs for the next release - `vX.X-documentation`.
3. Build
    - Put pre-release, CI servers and translation server back onto master.
4. Dev:
    - Delete RCs after final version is shipped    
    - Check if any libraries need to be updated for the next release, and if so bring up in weekly team meeting
    - Test the GitLab RC containing the Mattermost final bits
    - Confirm gitlab.mattermost.com is updated to final build
5. Marketing:
    - Confirm marketing has been posted (animated GIFs, screenshots, mail announcement, tweets, blog posts)

### J. (T-plus 5 working days) Release Updates
1. Logistics: 
    - Post this checklist in Release channel 
    - Verify all items in the last posted release checklist are complete, if not alert the release manager.
2. Leads:
    - Update [company roadmap at mattermost.com](https://about.mattermost.com/direction/)
    - Post and review [Mattermost Security Updates](https://about.mattermost.com/security-updates/)


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

