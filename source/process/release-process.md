# Release Process

Mattermost core team works on a bi-monthly release process, with a new version shipping on the 16th of each alternate month in [binary form](http://docs.mattermost.com/administration/upgrade.html#mattermost-team-edition). 

This document outlines the development process for the Mattermost core team, which draws from what we find works best for us from Agile, Scrum and Software Development Lifecycle approaches.

Recommended pre-reading: 

- [Mattermost Software Development Process training materials](https://docs.mattermost.com/process/training.html#software-development-process)
- [Mattermost Security Practices training](https://docs.mattermost.com/process/training.html#system-security) (particularly NIST standards) 

## Release Timeline

Notes: 
- All cut-off dates are based on 10am ([San Francisco Time](http://everytimezone.com/)) on the day stated.
- T-minus counts are measured in "working days" (weekdays other than major holidays concurrent in US and Canada) prior to release day.

### A. (Code complete date of previous release) Beginning of release

Pre-work for the current release begins at the code complete date of the previous release. See "Code Complete" section below for details.

### B. (T-minus 15 working days) Cut-off for submitting major features 

No pull requests for major features should be **submitted** to the current release after this date (except if release manager decides to add "release-exception" label to Jira ticket).

1. Release Manager:
    - Post this checklist in Release channel
2. PM:
    - Prioritize reviewing major features, ensuring any bugs and UX issues get fixed
    - Check that all major features are behind a feature flag
3. Dev:
    - Prioritize reviewing, updating, and merging of pull requests for major features
4. Marketing:
    - Confirm each Enterprise feature is in the correct [pricing SKU](https://about.mattermost.com/pricing/), if not alert the release manager

### C. (T-minus 12 working days) Cut-off for merging major features

No pull requests for major features should be **merged** to the current release after this date (except if release manager decides to add "release-exception" label to Jira ticket).

1. Release Manager:
    - Post this checklist in Release channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Logistics:
    - Confirm the following were posted:
        - Zero Bug Balance query
        - Item queued for UX meeting to discuss worst UX bug
        - Community notified about upcoming release in Reception
3. PM:
    - PM area owners complete draft of Changelog in a WIP PR with updates for highlights, feature additions, known issues, compatibility updates for deprecated features, config.json, [database changes](https://github.com/mattermost/platform/blob/master/store/sql_upgrade.go#L181), [API changes](https://github.com/mattermost/platform/commits/master/model/client.go) (search `#api-proposal` and confirm with Dev) and WebSocket event changes; [see example](http://docs.mattermost.com/administration/changelog.html#compatibility)
    - Review and update [company roadmap](https://about.mattermost.com/direction/) with which major features made it into the release
    - PM feature owners post draft section for the blog post in the Marketing Channel (including screenshots and a hashtag #mattermostXX where XX is the version number, see [example thread](https://pre-release.mattermost.com/core/pl/o611i4wz3pfafb6fpha9ggxxnh)) and [queue a tweet](https://pre-release.mattermost.com/core/pl/f3wsbwkgzfdr9nf9amtcwfpo6h)
    - Backlog is reviewed and tickets that won’t make it are moved to next release
4. Docs:
    - Update [Upgrade Guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide) for any steps needed to upgrade to new version
    - Submit NOTICE.txt PR for any new libraries added from dev, if not added already. The following two files contain a list of dependencies:
        - https://github.com/mattermost/platform/blob/master/webapp/package.json
        - https://github.com/mattermost/platform/blob/master/glide.yaml
5. QA:
    - Coordinate testing:
        - Receive testing sign-off from feature area owners (i.e. PM/Dev either signs-off that their area is well tested, or flags potential quality issues that may exist)  
        - Prioritize updating the RC Testing Spreadsheet to cover any changes or new features, and confirm that known issues are listed in the relevant tests
        - Assign each area of the release testing spreadsheet to a team member and ensure core team has access permissions 
6. **(Team) Major Feature Complete Meeting (10:00am San Francisco time)**:  
    - Discuss worst bug currently on master
    - Discuss release highlights for marketing
    - Review status of last feature PRs to be merged
7. Dev:
    - Prioritize reviewing, updating, and merging of pull requests for current release until there are no more tickets in the [pull request queue](https://github.com/mattermost/platform/pulls) marked for the current release
    - After the cut-off, any PRs that include significant code changes require approval of the release manager before merging.
8. Marketing:
    - Prepare bullet points for release announcement
    - Propose list of key features included in the release GIF and send to marketing lead for review
    - Draft release headline and send to marketing lead for review

### D. (T-minus 10 working days) Judgment Day

Day when leads and PM area owners decide which major features are included in the release, and which are postponed. 

1. Release Manager:
    - Post this checklist in Release channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Logistics:
    - Confirm, in Judgement Day meeting, date of marketing announcement for the release and update release channel header if needed
3. Leads:
    - Finalize roadmap for next release, and identify planned marketing bullet points  
4. **(Team) Judgment Day Meeting (10:00am San Francisco time)**:  
    - Meet to discuss release update and finalize which major features will be in or out for the release
5. PM: 
    - Based on discussion, create tickets for features that need to be turned on or off for the release
    - Update Changelog PR based on what's in/out of the release 
    - Create meta issue for release in GitHub (see [example](https://github.com/mattermost/platform/issues/3702))
    - Review the JIRA tickets remaining in the current release fix version and push those that won't make it to the next fix version.
6. Marketing:
    - Begins to draft blog post, tweet, and email for the release announcement

### E. (T-minus 8 working days) Code Complete and Release Candidate Cut

**Stabilization** period begins when all features for release have been committed. During this period, only **bugs** can be committed to the release branch. Non-bug pull requests are tagged for next version.

Exceptions can be made by the release manager setting priority to "Highest" and adding a "release-exception" label to the Jira ticket. This will add the ticket to the [hotfix list for release candidate](https://mattermost.atlassian.net/issues/?filter=10204).

1. Release Manager:
    - Post this checklist in Release channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Logistics:
    - Mail out mugs to any new contributors
    - Update [Team](http://www.mattermost.org/team/) page with new contributors
    - Add list of contributors to the Changelog draft
    - Confirm all PRs merged into the current release have been tested
3. Dev:
    - Prioritize reviewing, updating, and merging of pull requests for current release until there are no more tickets in the [pull request queue](https://github.com/mattermost/platform/pulls) marked for the current release 
4. PM:
    - Review all [Severity 1 bugs (data loss or security)](https://mattermost.atlassian.net/secure/IssueNavigator.jspa?mode=hide&requestId=10600) to consider for adding to Hotfix list.
    - Update documentation:  
        - Submit Changelog PR
        - Draft [Mattermost Security Updates](http://about.mattermost.com/security-updates/), but do not post until 14 days after official release
5. Docs:
    - Submit all doc PRs for review
    - Confirm changes to config.json in compatibility section of Changelog are written back to [settings documentation](http://docs.mattermost.com/administration/config-settings.html#configuration-settings)
6. **(Team) Code Complete Meeting (10:00am San Francisco time)**:  
    - (PM) Leads team review of Changelog 
    - (Release Manager) Walk through each unfinished item of this checklist  
    - (Dev) Last check of tickets that need to be merged before RC1  
7. Build:  
    - Review all `TODO` notes 
    - Master is tagged and branched and “Release Candidate 1″ is cut (e.g. 3.5.0-RC1) according to the Release Candidate Checklist in ``mattermost/process``
    - After branching, the database version in sql_upgrade.go on master is set to the next scheduled release version (e.g. 3.6.0)
    - CI servers are updated to the release branch
    - Translation server is locked to the release branch
8. PM:  
    - Merge changelog PR after team review is complete, and update the GitHub meta issue to include a link to the changelog on the documentation branch
    - Tweet announcement that RC1 is ready (see [example](https://pre-release.mattermost.com/core/pl/tefx1ijyz7bs8mabuxmpq9f7pw))
 
### F. (T-minus 7 working days) Release Candidate Testing 

1. Release Manager:
    - Post this checklist in Release channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Dev:
    - Test upgrade from previous version to current version, following the [Upgrade Guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide) with database upgrades on both MySQL and Postgres
    - Test upgrade from Team Edition to Enterprise edition based on the [Upgrade Guide](https://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-enterprise-edition)
    - Review any changes made to install guides, and test if necessary
3. QA:
    - Update Release Discussion header with links to RC instances and testing spreadsheet
    - Post release testing instructions to Release Discussion channel ([example](https://pre-release.mattermost.com/core/pl/8z1tazpmm3ycbrehju36brd5nh))
    - Post "Known Issues" to Release Discussion channel
4. Logistics:
    - Confirm community testers are directed to the Release Discussion channel
5. Team:
    - Test assigned areas of the Release Candidate Testing Spreadsheet and file any bugs found in Jira
    - Post a link to any "Blocking" issue that may need a hotfix to the RC in the Release room, with the **#blocking** tag. If the issue is security related or contains confidential information, post the link in the Confidential Bugs private group. Blocking issues are considered to be security issues, data loss issues, and issues that break core functionality or significantly impact aesthetics.
    - Daily triage of hotfix candidates and decide on whether and when to cut next RC or final
6. PM:
    - Queue an item for Release Update meeting to discuss worst bug
    - Update the meta issue:
        - Post comments to the meta issue with approved fixes for the next RCs
        - Download links and testing server links to the RCs
    - Post screenshot and links to final tickets for next RC to the Release Discussion room
    - Update Changelog “Known Issues” section with any significant issues that were found and not fixed for the final release
7. Dev:
    - PRs for hotfixes made to release branch
    - Review PRs made from release branch and merge changes into both the release branch and master
8. QA:
    - Test RC fixes as they come in on CI servers
9. Build: 
    - Verify with Release Manager before cutting any new RCs (approved fixes should be merged)
    - Push next RC to acceptance and announce in Town Square with new RC link
10. PM:
    - Test the new RC to verify fixes merged to the release branch work
    - Post in Release Channel after testing 

### G. (T-minus 5 working days) Release Candidate Testing Finished 

1. Release Manager:
    - Post this checklist in Release channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Team:
    - Finish assigned areas of the Release Candidate Testing Spreadsheet
    - Continue triaging hotfix candidates and decide on whether and when to cut next RC or final
    - If no blocking issues are found, PM, Dev and Ops signs off on the release
3. PM:
    - Check that known issues section of Changelog is updated
    - Check that the contributors section of Changelog is updated (including contributors from all repos)
    - Check that if there is a security fix, the Changelog contains a note mentioning the severity level of the issue, recommending upgrade, and thanking the security researcher (see security process doc for example)
4. Marketing:
    - Finish draft of blog post for mattermost.com and send for marketing lead to review
        - Upgrade should be recommended if there are security fixes in this version, with a note thanking the security researcher
    - Finish drafts of all art work (screenshots, GIFs and twitter banners) used for the blog post and send to marketing lead for review

### H. (T-minus 2 working days) Release Build Cut

The final release is cut. If an urgent and important issue needs to be addressed between major releases, a bug fix release (e.g. 1.1.1) may be created.

1. Release Manager:
    - Post this checklist in Release channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Build:
    - Tags a new release (e.g. 1.1.0) and runs an official build which should be essentially identical to the last RC 
    - Posts SHA key, md5 sum and GPG signatures of the final build to release channel
    - Post in Release Discussion with links to the EE and Team Edition bits
3. PM:
    - Close GitHub meta ticket for the release
    - Submit GitLab MR to take next Mattermost version in the Omnibus (see [example](https://gitlab.com/gitlab-org/omnibus-gitlab/merge_requests/998)):
        - Include changes to Mattermost version number ([`default_version`](https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/config/software/mattermost.rb#L20)) and md5 sum of the final TE build ([`source md5`](https://gitlab.com/jasonblais/omnibus-gitlab/blob/master/config/software/mattermost.rb#L23)) in  [`config/software/mattermost.rb`](https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/config/software/mattermost.rb)
        - Include a summary of updates in Team Edition that are relevant to GitLab
    - Check Security Issues spreadsheet and confirm disclosure text
    - Check the security researcher was added to the [Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/) page
    - Confirm link to security updates appears in blog post if there are security updates in this release, with a note thanking the security researcher 
4. Logistics:
    - Update the [Mattermost server download page](https://www.mattermost.org/download/) with the links to the EE and TE bits
      - Test the download links before and after updating the page
    - Contact owners of [community installers](http://www.mattermost.org/installation/) or submit PRs to update install version number
        - For Puppet, Heroku and Ansible Playbook, post to Installers and Images channel announcing the new release. See [example](https://pre-release.mattermost.com/core/pl/5eh8fw3jaiyzzqoc6nfwfaioya).
        - For Chef Cookbook, open a new issue to announce the new release. See [example](https://github.com/verifi-inc/mattermost/issues/2).
        - For Yunohost, open a new pull request to update the version. See [example](https://github.com/kemenaran/mattermost_ynh/pull/11).
        - For OpenShift, open a new pull request to update the version. See [example](https://github.com/goern/mattermost-openshift/pull/13).
    - Update [MVP page](https://www.mattermost.org/mvp/) with the most valuable contributor of the release
    - Submit PR to update [/mattermost-docker](https://github.com/mattermost/mattermost-docker/commit/782129450e9577a8966e5ddea18a1a4cdecdfd7f) image to latest release
5. Docs:
    - Add the download links, SHA key and md5 sum to [upgrade guide](http://docs.mattermost.com/administration/upgrade.html#version-archive)
    - Finalize docs
      - If reviews are not complete, hold a 30 minute doc review meeting with PMs and anyone else who has changed or reviewed docs this release and wants to join
      - Merge the docs release branch to master and verify all changes on docs.mattermost.com once the build is up
      - Submit a correction PR for any incorrect formatting or other errors missed during the initial review
6. Marketing:
    - Finish draft of animated GIF (for Twitter announcement, MailChimp and blog post) made up of top announcements
    - Finish draft of MailChimp email blast and Twitter announcement and send for marketing lead to review. Once reviewed, schedule for 08:00 PST on the date of marketing announcement
    - **Note:** If the release contains a security update, also draft a Mailchimp email blast for the [Security Bulletin mailing list](http://eepurl.com/cAl5Rv)
    - Finalize blog post for mattermost.com and set timer for 08:00 PST on the day of release
    - Turn on CrazyEgg for blog post page
    - Find [www-gitlab-com merge request](https://gitlab.com/gitlab-com/www-gitlab-com/merge_requests) for latest GitLab release blog post and make request for adding GitLab Mattermost update (see [example request](https://gitlab.com/gitlab-com/www-gitlab-com/merge_requests/2910#note_14096885), [example update](https://about.gitlab.com/2016/07/22/gitlab-8-10-released/#gitlab-mattermost-32)). Post to Release Discussion channel with link to request.
    - Update [feature list](https://about.mattermost.com/pricing/) on mattermost.com with relevant new features

If a bug fix release is required, run through the following steps: 

1. PM:
    - Schedule a team Release Update meeting every day until the dot release is complete
    - Post links to approved tickets for next dot release RC to the Release Discussion channel
    - Make a post in Town Square announcing the dot release. [See example](https://pre-release.mattermost.com/core/pl/4aippek8yp8a3nex9anen5rjoc)
    - Update the GitHub meta issue:
        - Change the title to "Mattermost vx.x.x - RCx", where `vx.x.x` is the version number of the dot release
        - Post a comment to the meta issue with approved fixes for the next RC of the dot release
        - Post download links and testing server links for the next RC when it's cut
    - Update Changelog:
        - Start a WIP PR for the dot release changelog and commit updates as new issues are fixed on the dot release RCs
        - Update “Known Issues” section with any significant issues that were found during RC testing and not fixed for the dot release
2. Dev:
    - PRs for hotfixes are made to release branch
    - Review PRs made from release branch and merge changes into both the release branch and master
3. Build: 
    - Verify with Release Manager before cutting any new dot release RCs (approved fixes should be merged)
    - Push dot release RC's to CI servers, pre-release and GitLab Mattermost.
4. QA:
    - Test the new RC to verify fixes merged to the release branch work. Post in Release Discussion channel after testing 

Once final dot release build is ready to cut:

1. Build:  
    - Tag a new release (e.g. 1.1.1) and run an official build  
    - Update CI servers, pre-release and GitLab Mattermost to the final version    
2. PM:
    - Update [Mattermost pricing page](https://about.mattermost.com/pricing/) if anything has changed
    - Merge the Changelog PR with notes on patch releases (see [example entry](https://docs.mattermost.com/administration/changelog.html#release-v3-5.1))
    - Submit GitLab MR to update the version number and MD5 hash to the dot release version. [See example](https://gitlab.com/gitlab-org/omnibus-gitlab/merge_requests/1127)
      - [Test the upgrade](https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg) once the MR is merged and the package is released to the GitLab package server
3. QA:  
    - Verifies each of the issues in the patch release are fixed
4. Docs:
    - Update the version archive in the [upgrade guide](https://github.com/mattermost/docs/blob/master/source/administration/upgrade.md)
    - Submit an MR to update [GitLab Mattermost documentation](https://docs.gitlab.com/omnibus/gitlab-mattermost/README.html)
5. Logistics:
    - Update [Mattermost server download page](https://mattermost.org/download) with the links to the EE and TE bits
      - Test the download links before and after updating the page
    - Update [mattermost-docker](https://github.com/mattermost/mattermost-docker) version
    - Contact owners of [community installers](http://www.mattermost.org/installation/) or submit PRs to update install version number
      - For Puppet, Heroku and Ansible Playbook, post to Installers and Images channel announcing the new release. See [example](https://pre-release.mattermost.com/core/pl/5eh8fw3jaiyzzqoc6nfwfaioya).
      - For Chef Cookbook, open a new issue to announce the new release. See [example](https://github.com/verifi-inc/mattermost/issues/2).
      - For Yunohost, open a new pull request to update the version. See [example](https://github.com/kemenaran/mattermost_ynh/pull/11).
      - For OpenShift, open a new pull request to update the version. See [example](https://github.com/goern/mattermost-openshift/pull/13).
6. Marketing:
    - Prepare [blog post](https://about.mattermost.com/mattermost-3-6-2/) for mattermost.com, MailChimp email blast, and [Twitter announcement](https://twitter.com/mattermosthq/status/827193482578112512), and send for marketing lead to review. Once reviewed, schedule for 08:00 PST on the day after dot release
      - **Note:** If the release contains a security update, also draft a Mailchimp email blast for the [Security Bulletin mailing list](http://eepurl.com/cAl5Rv)
      - Upgrade should be recommended if there are security fixes in the dot release version

### I. (T-minus 0 working days) Release Day

1. Release Manager:
    - Post this checklist in Release channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Logistics: 
    - Post key dates for the next release in the header of the Release Discussion channel and remove links to RC candidates and testing spreadsheet
    - For the next release, create the following team meetings. If they conflict with existing meetings, check with meeting owner to reschedule or reschedule the release meeting
        - PM Release Update meeting on T-15 at 7:30am San Francisco time
        - Major Feature Complete Meeting on T-12 at 10:00am San Francisco time
        - Judgment Day Meeting on T-10 at 10:00am San Francisco time
        - Code Complete Meeting on T-8 at 10:00am San Francisco time
        - Team-wide Triage each weekday starting at T-8 and ending at T-2 at 9:00am San Francisco time, with optional attendance
        - Release Update each weekday starting at T-7 and ending at T-2 at 10:00am San Francisco time
    - Add “Release Retrospective” item to next team meeting in place of Kaizen/User Issues, asking each core team member to give a letter grade (and brief explanation) for:
        - Release Quality
        - Release Process
        - Testing Process
    - Close the release in Jira
    - Prepare tickets for the next release,  with a corresponding vX.X prefix
        - [Creating final release candidate](https://mattermost.atlassian.net/browse/PLT-2198)
        - [Test Gitlab Omnibus RC install of Mattermost](https://mattermost.atlassian.net/browse/PLT-2197) 
        - [Test upgrade](https://mattermost.atlassian.net/browse/PLT-3940) to latest release based on [upgrade guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide)
        - Test upgrade from Team Edition to Enterprise Edition
        - [RC Build Testing for core team](https://mattermost.atlassian.net/browse/PLT-2208)
        - [Upgrade gitlab.mattermost.com to RC1](https://mattermost.atlassian.net/browse/PLT-3116)
        - [Push final build to gitlab.mattermost.com](https://mattermost.atlassian.net/browse/PLT-3117)
        - [Cut build and set up RC1 servers, including a note to check for all XXX items](https://mattermost.atlassian.net/browse/PLT-3937)
3. Docs:
    - Create a new branch on docs for the next release - `vX.X-documentation`
        - Submit a PR for changelog against the `vX.X-documentation` branch and add a `Work in Progress` label for it
        - Submit a PR to change version number in `docs/source/conf.py` against the `vX.X-documentation` branch
4. Build
    - Put CI servers and translation server back onto master
    - Update [ci-linux-mysql-prev](https://ci-linux-mysql-prev.mattermost.com) to the final release version
5. Dev:
    - Delete RCs after final version is shipped    
    - Check if any libraries need to be updated for the next release, and if so bring up in weekly team meeting
    - Test the GitLab RC containing the Mattermost final bits
    - Confirm gitlab.mattermost.com is updated to final build
6. Marketing:
    - Confirm marketing has been posted (animated GIFs, screenshots, mail announcement, tweets, blog posts)
    - Update @mattermosthq Twitter profile with the next release date
    - Prepare retweet of GitLab release tweet ([see example here](https://pre-release.mattermost.com/core/pl/k7wchwj5mtrhucj6don96yx3sc))

### J. (T-plus 5 working days) Release Updates
1. Release Manager:
    - Post this checklist in Release channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
2. Logistics: 
    - Confirm the Security Researchers list on the [Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/) is up to date
    - Review "Community Installers" and update version numbers if there are any discrepancies https://www.mattermost.org/installation/ (move this to ops eventually)
3. Leads:
    - Update [company roadmap at mattermost.com](https://about.mattermost.com/direction/)
4. Build: 
    - Put pre-release back on master
    
### K. (T-plus 10 working days) Security Updates
1. PM:
    - Post [Mattermost Security Updates](https://about.mattermost.com/security-updates/) after reviewing with security lead
      - If a dot release is shipping with security fixes, do not post new details until T-plus 10 working days from the dot release ship date
    - Update Security Issues spreadsheet with issue number from posted update (e.g. v3.2.0.1)

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

