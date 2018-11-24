# Feature Release Process

Mattermost core team works on a monthly release process, with a new version shipping on the 16th of each month in [binary form](http://docs.mattermost.com/administration/upgrade.html). 

This document outlines the development process for the Mattermost core team, which draws from what we find works best for us from Agile, Scrum and Software Development Lifecycle approaches.

## Release Timeline

Notes:
- All cut-off dates are based on 10am ([San Francisco Time](http://everytimezone.com/)) on the day stated.
- T-minus counts are measured in "working days" (weekdays other than major holidays concurrent in US and Canada) prior to release day.

### A. (Code complete date of previous release) Beginning of release

Pre-work for the current release begins at the code complete date of the previous release. See "Code Complete" section below for details.

### B. (T-minus 18 working days) Cut-off for submitting features

No pull requests for major features should be **submitted** to the current release after this date. In special cases, exceptions can be made by the QA Release Manager. 

1. QA Release Manager:
    - Post this checklist in Release Checklist channel
2. Each team (PM and QA own):
    - Follow that major feature PR reviews are prioritized and post a list of outstanding feature PRs in the Release Discussion channel pertaining to your team
    - Check that major features for platform have a corresponding ticket for RN, and are behind a feature flag, where applicable
    - Check that each Enterprise feature is in the correct [pricing SKU](https://about.mattermost.com/pricing/)
    - Review any features that are currently in beta and check if any are promoted
    - Confirm all config settings and new features have diagnostics

### C. (T-minus 15 working days) Cut-off for merging features

No pull requests for major features should be **merged** to the current release after this date. In special cases, exceptions can be made by the QA Release Manager.

1. **(Team) Major Feature Complete Meeting (10:00am San Francisco time)**:  
    - Discuss worst bug currently on master
    - Review status of remaining feature PRs to be merged
2. QA Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Review [contributions](https://github.com/mattermost/mattermost-webapp/graphs/contributors) since last release's Code Complete for Webapp, Server, Docs, Mobile, Redux, Desktop and API Reference repos and queue a list of MVP candidates in alphabetical order to the MVP Discussion channel. [See example](https://community.mattermost.com/core/pl/h3gy69h5ujfpzedtxmsnjfubko).
    - Review [software requirements](https://docs.mattermost.com/install/requirements.html#software-requirements) are up-to-date based on [these guidelines](https://docs.mattermost.com/process/software-requirements.html). If not, update documentation accordingly, and note changes in the Changelog.
    - Review submitted NOTICE.txt PRs for any new libraries added from dev, and ensure they are cherry-picked to feature release branch.
    - Post a reminder in the French Localization channel about the due date for translations, which is T-5 working days. [See example](https://community.mattermost.com/core/pl/7wqx4zehotgu7efhmbz51mxfqa
3. PM - For each team:
    - Draft Changelog in a WIP PR with updates for highlights, feature additions, known issues, compatibility updates for deprecated features, config.json, [database changes](https://github.com/mattermost/mattermost-server/blob/master/store/sqlstore/upgrade.go), [API changes](https://github.com/mattermost/mattermost-server/commits/master/model/client.go), and [WebSocket event changes](https://github.com/mattermost/mattermost-server/blob/master/model/websocket_message.go#L13); [see example](http://docs.mattermost.com/administration/changelog.html#compatibility)
    - Update [Upgrade Guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide) with any special notes for upgrading to the new version, including breaking changes or deprecated features in the release
).
    - Prepare outline for release announcement based on team's work. This includes an outline, benefits, order of major features, and which features have an accompanying screenshot. Review outline with devs and QA in your team
4. Dev Ops:
    - Cut release branch both for server and mobile. Merge database upgrade before cutting the branch
    - Point translation server to release branch after cutting
5. PM Release Manager:
    - Review release outline together with other PMs and decide order of features for release announce. After review, send outline to Marketing who works on release announce draft. [See example](https://oss.mattermost.com/mattermost/pl/5t459hruhfd7bpi46tnf8zq8yo).
    
### D. (T-minus 14 working days) Feature testing

1. QA Release Manager:
    - Prioritize testing merged PRs and resolved tickets for this release
    - Ensure that new features are also properly tested on mobile apps
    - Prioritize updating tests in the Release Testing spreadsheet and in Selenium IDE
    - Identify most-affected areas and queue Selenium tests to be updated and run

### E. (T-minus 13 working days) Judgment Day

Day when Leads and PMs decide which major features are included in the release, and which are postponed.

1. **(Team) Judgment Day Meeting (10:00am San Francisco time)**: 
    - Discuss worst bug on master
    - Finalize which major features will be in or out for the release. Discuss reverting feature(s) if 5 or more bugs found
    - Discuss release highlights for marketing
    - Begin daily triage of tickets, including bug tickets in the backlog
2. QA Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Create meta issue for release in GitHub (see [example](https://github.com/mattermost/mattermost-server/issues/3702))
    - Confirm date of marketing announcement for the release date with Marketing, and update release channel header if needed
       - If release day falls on a Friday, the blog post goes out on the Friday and the emailed newsletter goes out the following Tuesday.
    - Post a reminder to devs in the Release Discussion channel of the code complete date with the ZBB count [see example](https://community.mattermost.com/core/pl/coggyys9atg7fqyam81q3gkmoo)
3. PM - For each team:
    - Based on results of Team Meeting discussion, update Changelog PR and create tickets based on what's in/out of the release
    - Review JIRA tickets remaining in the current release fix version and push those that won't make it to the next fix version
    - Finalize roadmap for next release, and identify planned marketing bullet points
4. Marketing:
    - Start drafting blog post, tweet, and email for the release announcement
    
### F. (T-minus 12 working days) Code Complete

**Stabilization** period begins when all features for release have been committed. During this period, only **bugs** can be committed to the release branch. Non-bug pull requests are tagged for next version. Exceptions can be made by the QA Release Manager during triage.

Review the [Release Features & Bugs Quality Gate Guidelines](https://docs.google.com/document/d/1QxB_A1qkEJBKAvQpRa7JiSQLZhwg6HAEajNRNa7ldGg/edit) for reference.

1. **(Team) Code Complete Meeting (10:00am San Francisco time)**:
    - Team review of Changelog
    - Last check of tickets that need to be merged before RC1
2. QA Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Draft [Mattermost Security Updates](http://about.mattermost.com/security-updates/), but do not post until 30 days after official release. 
       - Add a placeholder text saying "Details on the security update will be posted here on X date, as per our Responsible Disclosure Policy"
    - Identify any new teammates who will be joining release testing, DM them an intro to the testing process and timeframe, send them the [hardware/software survey](https://drive.google.com/open?id=1IUiNO2S5fgWVn-Y_cyouxheukqKyGQC0_2UX64Ejwk8)
3. PM GitLab Relationship Owner:
    - If there are any breaking compatibility changes in the release, open an issue in the [GitLab Omnibus](https://gitlab.com/gitlab-org/omnibus-gitlab) to make sure GitLab is aware. Post a link to the issue in the Release Discussion channel

### G. (T-minus 9 working days) Release Candidate Cut

1. QA Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Update the GitHub meta issue:
       - Include a link to changelog on the documentation branch
       - Post comments to the meta issue with approved fixes for the next RCs
       - Update download links and testing server links to the latest RCs
    - Check that translations are in progress at https://translate.mattermost.com/projects/mattermost/ and reach out to translations if needed
    - Check that a redirect page has been set up in mattermost.com for any new links added to the System Console
2. Logistics:
    - Mail out contributor and security researcher mugs
      - Space out the ordering of mugs over three weeks to prevent mistakes being made by the supplier. For instance, if there are 12 contributors to order mugs for, place an order every 2nd or 3rd day over the next 3 weeks.
    - Update [Team](http://www.mattermost.org/team/) page with new contributors
    - Add list of contributors to Changelog draft
3. QA Release Manager:
    - Confirm up to date with testing merged PRs and resolved tickets
    - Confirm up to date with test updates and known issues in release testing spreadsheet
    - Assign release testing areas to team members
    - After RC1 is cut: Update rctesting and CI server invite links in Release Testing spreadsheet
    - After RC1 is cut: Lock Selenium server to RC1
    - After RC1 is cut: Tweet announcement that RC1 is ready. [See example](https://community.mattermost.com/core/pl/tefx1ijyz7bs8mabuxmpq9f7pw)
4. Dev Ops:
    - Review all `TODO` notes, including one for uncommenting upgrade code
    - Confirm all PRs in [`/enterprise`](https://github.com/mattermost/enterprise/pulls) repo have been merged.
    - Update Redux before each RC and Final build
    - Tag and branch `master`, and cut RC1 (e.g. 3.5.0-RC1) according to the [Dev Release Process](https://developers.mattermost.com/internal/release-process/)
    - After branching, set the database version in ``sql_upgrade.go`` on master to the next scheduled release version (e.g. 3.6.0)
    - Update CI servers and Translation server to the release branch
    - Run daily automated upgrade tests to catch upgrade bugs
5. PM - for each team:
    - Finish changelog PR and queue for QA review
    - Submit documentation PRs for product updates in the release
        - Confirm all new diagnostics are documented in the telemetry docs (https://docs.mattermost.com/administration/telemetry.html)
        - Confirm with devs documentation for [API changes](https://github.com/mattermost/mattermost-server/commits/master/model/client.go) and [WebSocket event changes](https://github.com/mattermost/mattermost-server/blob/master/model/websocket_message.go#L13) is added to API documentation
        - Confirm changes to config.json in compatibility section of Changelog are written back to [settings documentation](http://docs.mattermost.com/administration/config-settings.html#configuration-settings)

### H. (T-minus 8 working days) Release Candidate Testing

1. **(Team) Daily Release Update Meeting**
    - Triage Jira tickets
2. QA Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Post list of tickets to be fixed to the Release Discussion channel ([see example](https://community.mattermost.com/core/pl/65k77x3bnigw5f9ffohfxonnfy))
    - Update Changelog "Known Issues" section with any significant issues that were found and not fixed for the final release
    - Update Release Discussion header with links to RC instances and testing spreadsheet ([template](https://community.mattermost.com/core/pl/db3sur4r53d9tyih1i4wrmi9wy))
    - Post release testing instructions to Release Discussion channel ([template](https://community.mattermost.com/core/pl/uprogtcqzpbk7nkmdkfnhqkcac))
    - DM reminders to team members who are not QA or devs, or who are new to release testing
    - Post "Bug Hunter Coin" message to Reception channel ([see example](https://community.mattermost.com/core/pl/3o15eoq89fdq5m1ac5dyp4nc3e))
    - Begin running all Selenium IDE tests
    - At end of day, post reminders about release testing in Release Discussion and Announcements channels, DM any team members who have zero test cells marked Done
4. Dev Ops:
    - Cherry-pick bug fixes to the release branch, unless completed by devs
    - Run daily automated upgrade tests to catch upgrade bugs
    - Cut new RCs after verifying with QA Release Manager (approved fixes should be merged)
    - Check CI servers are running on the release branch
5. Marketing:
    - Finish draft of blog post for mattermost.com and all art work (screenshots, GIFs and twitter banners) used for the blog post
        - Upgrade should be recommended if there are security fixes in this version, with a note thanking the security researcher
    - Send blog post for PMs and QA to review

### I. (T-minus 7 working days) Release Candidate Testing Finished

1. **(Team) Daily Release Update Meeting**
    - Confirm testing assigned in the release testing spreadsheet is complete 
    - Continue triaging Jira tickets
    - Decide when to cut next RC or final    
2. QA Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
3. Marketing:
    - Send blog post for mattermost.com and all related art work for marketing lead to review
4. PM GitLab Relationship Owner:
    - Find [www-gitlab-com merge request](https://gitlab.com/gitlab-com/www-gitlab-com/merge_requests?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=blog%20post&label_name%5B%5D=release) for latest GitLab release blog post and make request for adding GitLab Mattermost update (see [example request](https://gitlab.com/gitlab-com/www-gitlab-com/merge_requests/2910#note_14096885), [example update](https://about.gitlab.com/2016/07/22/gitlab-8-10-released/#gitlab-mattermost-32)). Post to Release Discussion channel with link to request.
5. QA Release Manager:
    - Midday: Post at-channel reminders about testing, and DM team members whose tests are not marked Done
    - Find QA or other teammates to help finish unfinished tests if needed
    - End of day: Verify all release tests are finished
    - Go through all tabs of testing spreadsheet and verify all comments and questions have been filed in JIRA as needed
    - Verify all JIRA tickets other than newly filed bugs have been tested, verified, and closed
    - As bug fixes are merged and RCs are cut, verify fixes on new RCs and post in Release Channel after testing
    - As RCs are cut, update selenium.mattermost.com to latest RC

### J. (T-minus 2 working days) Release Build Cut

The final release is cut - RC cuts and bug fixes should be completed by this date. Only urgent and critical issues are considered for fixing.

Review the [Release Features & Bugs Quality Gate Guidelines](https://docs.google.com/document/d/1QxB_A1qkEJBKAvQpRa7JiSQLZhwg6HAEajNRNa7ldGg/edit) for reference.

1. **(Team) Daily Release Update Meeting**
    - Continue to triage Jira tickets
    - If no blocking issues are found, PM, Dev and QA sign off on the release and plan to cut final
2. QA Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Verify that the final translations PR for the release is submitted
    - Confirm Changelog reflects any changes since it was merged (including known issues and contributors from all repositories)
      - If there is a security fix, confirm the Changelog recommends upgrade, with a note mentioning the security level and thanking the security researcher
    - Verify all PRs and tickets for the release have been tested / closed
    - Verify Selenium server was put on final RC and build passed
    - Verify smoke tests on platform and RN apps all passed
    - Post QA approval in Release Discussion channel
3. PM GitLab Relationship Owner:
    - Work with a developer to submit GitLab MR [following this process](https://docs.mattermost.com/process/gitlab-process.html#merge-requests) and [test the upgrade](https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg) once the GitLab MR is merged and included in their RC.
5. Dev Ops:
    - Update Redux before each RC and Final build
    - Test upgrade from previous version to current version, following the [Upgrade Guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide) with database upgrades on both MySQL and Postgres
    - Test upgrade from Team Edition to Enterprise edition based on the [Upgrade Guide](https://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-enterprise-edition)
    - Review any changes made to install guides, and test if necessary
    - Tag a new release (e.g. 1.1.0) and run an official build which should essentially be identical to the last RC
    - Verify the hashes (SHA-1, SHA-256 and md5) and GPG signatures are correct for both Team Edition and Enterprise Edition.
    - Ensure [Security Policies](https://docs.mattermost.com/process/security.html) page has been updated
    - Update dependancies after release branch is cut in `mattermost-server`, `mattermost-webapp`, `desktop`, `mattermost-mobile` and `mattermost-redux`
5. Logistics:
    - Update [MVP page](https://www.mattermost.org/mvp/) with the most valued professional of the release and order the contributor's coaster
6. PM Release Manager:
    - Finalize docs
      - If reviews are not complete, hold a 30 minute doc review meeting with PMs and anyone else who has changed or reviewed docs this release and wants to join
      - Merge the docs release branch to master and verify all changes on docs.mattermost.com once the build is up
    - Update feature lists on https://about.mattermost.com/pricing/ and https://about.mattermost.com/features/ with relevant new features
7. QA Release Manager:
    - Submit a correction PR for any incorrect formatting or other errors missed during the initial review
    - Close GitHub meta ticket for the release
    - Add download links, SHA-256 hash and GPG signature to [version archive](http://docs.mattermost.com/administration/upgrade.html#version-archive)
    - Merge changelog PR after review is complete
    - Update [Mattermost server download page](https://www.mattermost.org/download/) with links to EE and TE bits
         - Test the download links before and after updating the page
    - Check Security Issues spreadsheet and confirm disclosure text
    - Check the security researcher was added to the [Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/) page
    - Confirm link to security updates appears in blog post if there are security updates in this release, with a note thanking the security researcher
    - Update [deprecated feature list](https://about.mattermost.com/deprecated-features/) in mattermost.com with new and scheduled deprecations
8. Marketing:
    - Receive sign off on final version of MailChimp email blast and Twitter announcement and schedule for 08:00 PST on the date of marketing announcement
      - **Note:** If the release contains a security update, also draft a Mailchimp email blast for the [Security Bulletin mailing list](http://eepurl.com/cAl5Rv)
    - Finalize blog post for mattermost.com, test on mobile view, and set timer for 08:00 PST on the day of release

### K. (T-minus 0 working days) Release Day

1. QA Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
    - Schedule a release retrospective meeting, to be held within 5 days from the release
    - Prepare and post [release metrics](https://docs.google.com/spreadsheets/d/1Aoj4OTaWoyrKIcQNiHH1MVoRG51T20Y_0w2tg5oVw-M/edit#gid=825551144)
    - Post the MVP winner announcement in the [Contributors channel](https://community.mattermost.com/core/channels/tickets)
    - Post key dates for the next release in the Release Discussion channel and remove links to RC candidates and testing spreadsheet from the header
        - Make sure that statutory holidays for Canada and US are accounted for in the release dates
    - Check for any [UserVoice](https://docs.google.com/spreadsheets/d/1nljd4cFh-9MXF4DxlUnC8b6bdqijkvi8KHquOmK8M6E/edit#gid=0) feature suggestions that were completed in the current release
      - Find the [release tweet](https://twitter.com/mattermosthq/status/854781715914555393) and insert a link to the tweet next to the feature that shipped with the release.
    - Close the release in Jira both for webapp and mobile ([releases page](https://mattermost.atlassian.net/projects/PLT?selectedItem=com.atlassian.jira.jira-projects-plugin%3Arelease-page&status=unreleased))
        - If there are many unresolved tickets in the current release, ask the release manager to review the ticket queue
        - Otherwise, release the fix version (Actions > [...] > Release)
    - Prepare tickets for the next release, with a corresponding vX.X prefix, and put the tickets in the appropriate sprints as follows:
       - The week RC is cut:
            - [RC Build Testing for core team](https://mattermost.atlassian.net/browse/PLT-2208)
       - The week RC is cut:
            - [Loadtest x.x release candidate compared to x.x release](https://mattermost.atlassian.net/browse/MM-12532)
       - Release week (for GitLab dev owner)
            - [Test Gitlab Omnibus RC install of Mattermost](https://mattermost.atlassian.net/browse/PLT-2197)
       - Release week (for dependancies owner)
            - Upgrade dependancies for Webapp, Server and Redux
       - Week after release (for GitLab dev owner)
            - [Submit Gitlab Omnibus RC install of Mattermost](https://mattermost.atlassian.net/browse/MM-9872)
    - Confirm that [mattermost-docker](https://github.com/mattermost/mattermost-docker/releases) has been updated to the latest version (contact the maintainer via direct message on community.mattermost.com if necessary)
2. PM Release Manager:
    - Review and update [company roadmap](https://about.mattermost.com/direction/) with which major features made it into the release
3. Logistics:
    - For the next release, create the following team meetings. If they conflict with existing meetings, check with meeting owner to reschedule or reschedule the release meeting
      - Feature Complete Meeting on T-15 at 10:00am San Francisco time
      - Judgment Day Meeting on T-13 at 10:00am San Francisco time
      - Code Complete Meeting on T-12 at 10:00am San Francisco time
      - Release Triage and Update Meeting each weekday starting at T-13 and ending at T-2 at 9:30am San Francisco time for PM, QA and release dev.
    - Contact owners of [community installers](http://www.mattermost.org/installation/) or submit PRs to update install version number
      - For Puppet, Heroku and Ansible Playbook, post to Installers and Images channel announcing the new release. See [example](https://community.mattermost.com/core/pl/fgjqthmn67nujjtx4fcrn1hd9a).
      - For Chef Cookbook, open a new issue to announce the new release. See [example](https://github.com/ist-dsi/mattermost-cookbook/issues/22).
      - For Yunohost, open a new pull request to update the version. See [example](https://github.com/YunoHost-Apps/mattermost_ynh/pull/103).
      - For OpenShift, open a new issue to update the version. See [example](https://github.com/rhdt/mattermost-openshift/issues/7).
    - Create a new branch on docs for the next release - `vX.X-documentation`
        - Submit a PR for changelog against the `vX.X-documentation` branch and add a `Work in Progress` label for it
        - Submit a PR to change version number in `docs/source/conf.py` against the `vX.X-documentation` branch
4. Dev Ops:
    - Put CI servers and translation server back onto master, and post in Release Discussion channel once done
    - Update [ci-linux-mysql-prev](https://ci-linux-mysql-prev.mattermost.com) to the previous release version
    - Confirm oss.mattermost.com is updated to final build
    - Cut release branch for Bug Fix release
    - Update existing tickets or create new ones for the next release
5. Marketing:
    - Turn on CrazyEgg for blog post page
    - Confirm marketing has been posted (animated GIFs, screenshots, mail announcement, tweets, blog posts)
    - Update @mattermosthq Twitter profile with the next release date
    - Prepare retweet of GitLab release tweet ([see example here](https://community.mattermost.com/core/pl/k7wchwj5mtrhucj6don96yx3sc))

### L. (T-plus 5 working days) Release Updates
1. QA Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Check that dependancies have been upgraded
    - Update Security Research Hall of Fame on the [Responsible Disclosure Policy](https://about.mattermost.com/report-security-issue/) page
    - Update 'latest version of Mattermost' supported in the Airtable Integrations Directory on the [Mattermost Apps and Integrations](https://about.mattermost.com/community-applications) page
2. PM Release Manager:
    - Update [company roadmap at mattermost.com](https://about.mattermost.com/direction/)

### M. (T-plus 30 days) Update Mattermost Security Page
1. QA Release Manager:
    - Post [Mattermost Security Updates](https://about.mattermost.com/security-updates/) after reviewing with security lead
      - If a dot release is shipping with security fixes, do not post new details until T-plus 10 working days from the dot release ship date
    - Update Security Issues spreadsheet with issue number from posted update (e.g. v3.2.0.1)

## Release Numbering

Mattermost numbers its stable releases based on the following format: `[Version Number].[Major Build Number].[Minor Build Number]`

- Version Number indicates a major system release (e.g. 1.x.x, 2.x.x)
- Major Build Number indicates significant new functionality, (e.g. 0.5.x, 0.6.x, 0.7.x)
- Minor Build Number indicates a bug fix or security release (e.g. 1.2.5, 1.2.6)
