# Release Process

Mattermost core team works on a monthly release process, with a new version shipping on the 16th of each month in [binary form](http://docs.mattermost.com/administration/upgrade.html#mattermost-team-edition). 

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

No pull requests for major features should be **submitted** to the current release after this date. In special cases, exceptions can be made by the Release Manager. 

1. Release Manager:
    - Post this checklist in Release Checklist channel
2. PM:
    - Prioritize reviewing major features, ensuring any bugs and UX issues get fixed
    - Check that all major features are behind a feature flag
    - Confirm with Leads that each Enterprise feature is in the correct [pricing SKU](https://about.mattermost.com/pricing/). If not, alert the release manager
    - Review any features that are currently in beta and confirm with Leads if there are any to be promoted
    - Confirm all config settings and new features have diagnostics
3. Dev:
    - Prioritize reviewing, updating, and merging of pull requests for major features

### C. (T-minus 12 working days) Cut-off for merging major features

No pull requests for major features should be **merged** to the current release after this date. In special cases, exceptions can be made by the Release Manager.

1. **(Team) Major Feature Complete Meeting (10:00am San Francisco time)**:  
    - Discuss worst bug currently on master
    - Discuss release highlights for marketing
    - Review status of remaining feature PRs to be merged
2. Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Review and update [company roadmap](https://about.mattermost.com/direction/) with which major features made it into the release
    - Queue a list of MVP candidates in alphabetical order to the Platform Meeting channel. [See example](https://pre-release.mattermost.com/private-core/pl/q9jdbzw7c7ribjsp78857xbomh)
    - Draft Changelog in a WIP PR with updates for highlights, feature additions, known issues, compatibility updates for deprecated features, config.json, [database changes](https://github.com/mattermost/mattermost-server/blob/master/store/sql_upgrade.go#L181), [API changes](https://github.com/mattermost/mattermost-server/commits/master/model/client.go) (search `#api-proposal` and confirm with Dev) and WebSocket event changes; [see example](http://docs.mattermost.com/administration/changelog.html#compatibility)
    - Update [Upgrade Guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide) with any special notes for upgrading to the new version
    - Submit NOTICE.txt PR for any new libraries added from dev, if not added already. The following two files contain a list of dependencies:
        - https://github.com/mattermost/mattermost-webapp/blob/master/package.json
        - https://github.com/mattermost/mattermost-server/blob/master/Gopkg.lock
    - Start posting a daily Zero Bug Balance query (posted until zero bugs or day of release)
3. PM:
    - Review Jira Backlog and move any tickets that will not be merged to the next release
4. Dev:
    - Prioritize reviewing, updating, and merging of pull requests for current release until there are no more tickets in the [pull request queue](https://github.com/mattermost/mattermost-server/pulls) marked for the current release
      - After the cut-off, any PRs that include significant code changes, require approval of the release manager before merging
5. Logistics:
    - Notify community about upcoming release in Reception [see example](https://pre-release.mattermost.com/core/pl/aq434e5dt3ntmfdowhekxjzi4r)
6. Marketing:
    - Prepare bullet points and release headline for release announcement. Release manager to review the outline (benefits and order of major features) with PMs before sending to Justin to work on
    - Decide which sections of the release announcement will have an accompanying screenshot / photo
    
### D. (T-minus 11 working days) Major feature testing

1. QA:
    - Prioritize testing merged PRs and resolved tickets
    - Ensure that new features designed for mobile are also properly tested on mobile
    - Write and update tests in the Release Testing spreadsheet and in Selenium IDE
    - Run Selenium IDE tests for updated areas, note Pass/Fail and date tested in the Release Testing spreadsheet

### E. (T-minus 10 working days) Judgment Day

Day when Leads and PMs decide which major features are included in the release, and which are postponed.

1. **(Team) Judgment Day Meeting (10:00am San Francisco time)**: 
    - Discuss worst bug on master
    - Finalize which major features will be in or out for the release
    - Begin daily triage of tickets
2. Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Update Changelog PR based on what's in/out of the release
    - Create meta issue for release in GitHub (see [example](https://github.com/mattermost/mattermost-server/issues/3702))
    - Confirm date of marketing announcement for the release date with Marketing, and update release channel header if needed
      - If release day falls on a Friday, the blog post goes out on the Friday and the emailed newsletter goes out the following Tuesday.
    - Post a reminder to devs in the Release Discussion channel of the the code complete date with the ZBB count [see example](https://pre-release.mattermost.com/core/pl/coggyys9atg7fqyam81q3gkmoo)
3. Leads:
    - Finalize roadmap for next release, and identify planned marketing bullet points
4. PM:
    - Based on results of Team Meeting discussion, create tickets for features that need to be turned on or off for the release
    - Review the JIRA tickets remaining in the current release fix version and push those that won't make it to the next fix version
5. Marketing:
    - Start drafting blog post, tweet, and email for the release announcement
    
### F. (T-minus 9 working days) Code complete

**Stabilization** period begins when all features for release have been committed. During this period, only **bugs** can be committed to the release branch. Non-bug pull requests are tagged for next version. Exceptions can be made by the Release Manager during triage.

1. **(Team) Code Complete Meeting (10:00am San Francisco time)**:
    - Team review of Changelog
    - Walk through each unfinished item of this checklist
    - Last check of tickets that need to be merged before RC1
2. Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Review all [Severity 1 bugs (data loss or security)](https://mattermost.atlassian.net/secure/IssueNavigator.jspa?mode=hide&requestId=10600) to consider adding to Hotfix list
    - Draft [Mattermost Security Updates](http://about.mattermost.com/security-updates/), but do not post until 14 days after official release
3. Dev:
    - Prioritize reviewing, updating, and merging of pull requests for current release until there are no more tickets in the [pull request queue](https://github.com/mattermost/mattermost-server/pulls) marked for the current release
4. PM:
    - If there are any breaking compatibility changes in the release, open an issue in the [GitLab Omnibus](https://gitlab.com/gitlab-org/omnibus-gitlab) to make sure GitLab is aware. Post a link to the issue in the Release Discussion channel
    - PM owner of System Admin features reviews changes to `config.json` to confirm they're included in the correct Mattermost Edition

### G. (T-minus 8 working days) Release Candidate Cut

1. Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Update the GitHub meta issue to include a link to the changelog on the documentation branch
    - After build is cut, tweet announcement that RC1 is ready (see [example](https://pre-release.mattermost.com/core/pl/tefx1ijyz7bs8mabuxmpq9f7pw))
2. Logistics:
    - Mail out contributor and security researcher mugs
    - Update [Team](http://www.mattermost.org/team/) page with new contributors
    - Provide release manager with a list of contributors for Changelog draft
3. QA:
    - Confirm all PRs merged into the current release have been tested
    - Ensure the release testing spreadsheet covers any changes and new features, and confirm known issues are listed in the relevant tests
    - Assign each area of the spreadsheet to a team member and give the core team access permissions
    - Update rctesting and CI server invite links in Release Testing spreadsheet after they've been updated to release branch
    - Test remaining merged PRs and resolved tickets for the release
    - Write and update tests in the Release Testing spreadsheet and in Selenium IDE
    - Run Selenium IDE tests for updated areas, note Pass/Fail and date tested in the Release Testing spreadsheet
4. Build:
    - Review all `TODO` notes, including one for uncommenting upgrade code
    - Confirm all PRs in [`/enterprise`](https://github.com/mattermost/enterprise/pulls) repo have been merged.
    - Master is tagged and branched and “Release Candidate 1″ is cut (e.g. 3.5.0-RC1) according to the Release Candidate Checklist in ``mattermost/process``
    - After branching, the database version in sql_upgrade.go on master is set to the next scheduled release version (e.g. 3.6.0)
    - CI servers are updated to the release branch
    - Translation server is locked to the release branch
    - Run daily automated upgrade tests to avoid catching upgrade bugs late
5. Docs:
    - Submit Changelog PR for team review
    - Submit any remaining documentation PRs for product updates in the release
    - Confirm changes to config.json in compatibility section of Changelog are written back to [settings documentation](http://docs.mattermost.com/administration/config-settings.html#configuration-settings)
    - Confirm all new diagnostics are documented in the telemetry docs (https://docs.mattermost.com/administration/telemetry.html)

### H. (T-minus 7 working days) Release Candidate Testing

1. **(Team) Daily Release Update Meeting**
    - Triage Jira tickets
    - Decide when to cut next RC or final
2. Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Update the GitHub meta issue:
        - Post comments to the meta issue with approved fixes for the next RCs
        - Update download links and testing server links to the latest RCs
    - Post list of tickets to be fixed to the Release Discussion channel ([see example](https://pre-release.mattermost.com/core/pl/65k77x3bnigw5f9ffohfxonnfy))
    - Update Changelog “Known Issues” section with any significant issues that were found and not fixed for the final release
3. QA:
    - Update Release Discussion header with links to RC instances and testing spreadsheet ([template](https://pre-release.mattermost.com/core/pl/db3sur4r53d9tyih1i4wrmi9wy))
    - Post release testing instructions to Release Discussion channel ([template](https://pre-release.mattermost.com/core/pl/uprogtcqzpbk7nkmdkfnhqkcac))
    - Update Selenium and manual smoke tests as needed, to prepare to run on each RC after it is cut
    - As bug fixes are merged, verify fixes on new RCs and post in Release Channel after testing
    - Update selenium.mattermost.com to latest RC
4. Dev:
    - Run load tests against the release candidate to find potential performance issues
    - Make PRs for bug fixes to the release branch
    - Review PRs made from release branch and merge changes into the release branch as required and merge the release branch back into master once per day
    - Run daily automated upgrade tests to avoid catching upgrade bugs late
5. Build:
    - Verify with Release Manager before cutting any new RCs (approved fixes should be merged)
    - Push next RC to acceptance and announce in Town Square with new RC link
    - Check CI servers running on release branch

### I. (T-minus 5 working days) Release Candidate Testing Finished

1. **(Team) Daily Release Update Meeting**
    - Confirm testing assigned in the release testing spreadsheet is complete 
    - Continue to triage Jira tickets
    - If no blocking issues are found, PM, Dev and QA sign off on the release and plan to cut final
2. Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Verify that the final translations PR for the release is submitted
    - Confirm Changelog reflects any changes since it was merged (including known issues and contributors from all repositories)
      - If there is a security fix, confirm the Changelog recommends upgrade, with a note mentioning the security level and thanking the security researcher (security process doc for example)
3. Marketing:
    - Finish draft of blog post for mattermost.com and send for release manager and PMs to review before sending for marketing lead to review
        - Upgrade should be recommended if there are security fixes in this version, with a note thanking the security researcher
    - Finish drafts of all art work (screenshots, GIFs and twitter banners) used for the blog post and review with PMs before sending to marketing lead for review
    - Find [www-gitlab-com merge request](https://gitlab.com/gitlab-com/www-gitlab-com/merge_requests?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=blog%20post&label_name%5B%5D=release) for latest GitLab release blog post and make request for adding GitLab Mattermost update (see [example request](https://gitlab.com/gitlab-com/www-gitlab-com/merge_requests/2910#note_14096885), [example update](https://about.gitlab.com/2016/07/22/gitlab-8-10-released/#gitlab-mattermost-32)). Post to Release Discussion channel with link to request.

### J. (T-minus 2 working days) Release Build Cut

The final release is cut. If an urgent and important issue needs to be addressed between major releases, a bug fix release (e.g. 1.1.1) may be created.

1. Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Work with a developer to submit GitLab MR [following this process](https://docs.mattermost.com/process/gitlab-process.html#merge-requests) and [test the upgrade](https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg) once the GitLab MR is merged and included in their RC.
      - Open a ticket to [submit Gitlab Omnibus RC install of Mattermost](https://mattermost.atlassian.net/browse/MM-10365)
    - Close GitHub meta ticket for the release
    - Add the download links and SHA-256 hash [upgrade guide](http://docs.mattermost.com/administration/upgrade.html#version-archive)
    - Merge changelog PR after review is complete
    - Update the [Mattermost server download page](https://www.mattermost.org/download/) with the links to the EE and TE bits
      - Test the download links before and after updating the page
2. Build:
    - Tags a new release (e.g. 1.1.0) and runs an official build which should be essentially identical to the last RC
    - Posts SHA key, md5 sum and GPG signatures of the final build to release channel
    - Post in Release Discussion with links to the EE and Team Edition bits
3. PM:
    - Check Security Issues spreadsheet and confirm disclosure text
    - Check the security researcher was added to the [Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/) page
    - Confirm link to security updates appears in blog post if there are security updates in this release, with a note thanking the security researcher
    - Update [deprecated feature list](https://about.mattermost.com/deprecated-features/) in mattermost.com with new and scheduled deprecations
4. Dev:
    - Verify the hashes (SHA-1, SHA-256 and md5) and GPG signatures are correct for both Team Edition and Enterprise Edition.
    - Test upgrade from previous version to current version, following the [Upgrade Guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide) with database upgrades on both MySQL and Postgres
    - Test upgrade from Team Edition to Enterprise edition based on the [Upgrade Guide](https://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-enterprise-edition)
    - Review any changes made to install guides, and test if necessary
    - Run loadtests against the final release build to confirm there are no performance issues
    - Ensure [Security Policies](https://docs.mattermost.com/process/security.html) page has been updated
    - Update dependancies after release branch is cut in `mattermost-server`, `mattermost-webapp`, `desktop`, `mattermost-mobile` and `mattermost-redux`
5. Logistics:
    - Update [MVP page](https://www.mattermost.org/mvp/) with the most valuable contributor of the release
6. Docs:
    - Finalize docs
      - If reviews are not complete, hold a 30 minute doc review meeting with PMs and anyone else who has changed or reviewed docs this release and wants to join
      - Merge the docs release branch to master and verify all changes on docs.mattermost.com once the build is up
      - Submit a correction PR for any incorrect formatting or other errors missed during the initial review
7. Marketing:
    - Receive sign off on final version of MailChimp email blast and Twitter announcement and schedule for 08:00 PST on the date of marketing announcement
    - **Note:** If the release contains a security update, also draft a Mailchimp email blast for the [Security Bulletin mailing list](http://eepurl.com/cAl5Rv)
    - Finalize blog post for mattermost.com, test on mobile view, and set timer for 08:00 PST on the day of release
    - Update feature lists on https://about.mattermost.com/pricing/ and https://about.mattermost.com/features/ with relevant new features
    - Add links to [Admin guide](https://docs.mattermost.com/guides/administrator.html) in the release blog post where needed
 
If a security fix release is required, run through the following steps:

1. PM:
    - Verify all patch fixes are backported
    - Verify all patch fixes are tested (either via unit tests or RCs)
2. Release Manager:
    - Work with a developer to submit GitLab MR [following this process](https://docs.mattermost.com/process/gitlab-process.html#merge-requests) and [test the upgrade](https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg) once the GitLab MR is merged and included in their RC.
      - Open a ticket to [submit Gitlab Omnibus RC install of Mattermost](https://mattermost.atlassian.net/browse/MM-10365)
    - Make a post in Announcements channel announcing the dot release to the rest of the team with links to approved tickets and include a link to the ticket to submit the GitLab MR
    - Update the changelog
    - Update the [version archive](https://docs.mattermost.com/administration/version-archive.html)
    - Update [Mattermost server download page](https://mattermost.org/download) with the links to the EE and TE bits
      - Test the download links before and after updating the page
    - Contact owners of [community installers](http://www.mattermost.org/installation/) or submit PRs to update install version number
      - For Puppet, Heroku and Ansible Playbook, post to Installers and Images channel announcing the new release. See [example](https://pre-release.mattermost.com/core/pl/5eh8fw3jaiyzzqoc6nfwfaioya).
      - For Chef Cookbook, open a new issue to announce the new release. See [example](https://github.com/verifi-inc/mattermost/issues/2).
      - For Yunohost, open a new pull request to update the version. See [example](https://github.com/kemenaran/mattermost_ynh/pull/11).
      - For OpenShift, open a new pull request to update the version. See [example](https://github.com/goern/mattermost-openshift/pull/13).
    - Update Security Research Hall of Fame on the [Responsible Disclosure Policy](https://about.mattermost.com/report-security-issue/) page
    - Post [Mattermost Security Updates](https://about.mattermost.com/security-updates/) 10 working days after the dot release has shipped
      - Update Security Issues spreadsheet with issue number from posted update (e.g. v3.2.0.1)
3. Marketing:
    - Prepare [blog post](https://about.mattermost.com/mattermost-3-6-2/) for mattermost.com, MailChimp email blast, and [Twitter announcement](https://twitter.com/mattermosthq/status/827193482578112512), and send to marketing lead for review. Once reviewed, schedule for 08:00 PST on the day after dot release
    
If a bug fix release is required, run through the following steps:

1. PM:
    - Schedule a Daily Release Update meeting every day until the dot release is complete
    - Open an issue in the [GitLab Omnibus](https://gitlab.com/gitlab-org/omnibus-gitlab) mentioning a dot release is coming 
2. Release Manager:
    - Work with a developer to submit GitLab MR [following this process](https://docs.mattermost.com/process/gitlab-process.html#merge-requests) and [test the upgrade](https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg) once the GitLab MR is merged and included in their RC.
      - Open a ticket to [submit Gitlab Omnibus RC install of Mattermost](https://mattermost.atlassian.net/browse/MM-10365)
    - Make a post in Announcements channel announcing the dot release to the rest of the team with links to approved tickets and include a link to the ticket to submit the GitLab MR
    - Update the GitHub meta issue:
        - Change the title to "Mattermost vx.x.x - RCx", where `vx.x.x` is the version number of the dot release
        - Post a comment to the meta issue with approved fixes for the next RC of the dot release
        - Post download links and testing server links for the next RC when it's cut
    - Update Changelog:
        - Start a WIP PR for the dot release changelog and commit updates as new issues are fixed on the dot release RCs
3. Dev:
    - PRs for hotfixes are made to release branch
    - Review PRs made from release branch and merge changes into the release branch as required and merge the release branch back into master once per day
4. Build:
    - Verify with Release Manager before cutting any new dot release RCs (approved fixes should be merged)
5. QA:
    - Test the new RC to verify fixes merged to the release branch work
    - Post in Release Discussion channel after testing

Once bug fix release is ready to cut:

1. Dev:
    - Tag a new release (e.g. 1.1.1) and run an official build
    - Verify hashes and GPG signatures are correct, once build is cut
    - Delete RCs after final version is shipped
    - Merge changes made to release branch into master 
2. PM:
    - Update [Mattermost pricing page](https://about.mattermost.com/pricing/) if anything has changed
3. Release Manager:
    - Merge the Changelog PR with notes on patch releases (see [example entry](https://docs.mattermost.com/administration/changelog.html#release-v3-5.1))
    - Update the [version archive](https://docs.mattermost.com/administration/version-archive.html)
    - Update [Mattermost server download page](https://mattermost.org/download) with the links to the EE and TE bits
      - Test the download links before and after updating the page
    - Contact owners of [community installers](http://www.mattermost.org/installation/) or submit PRs to update install version number
      - For Puppet, Heroku and Ansible Playbook, post to Installers and Images channel announcing the new release. See [example](https://pre-release.mattermost.com/core/pl/5eh8fw3jaiyzzqoc6nfwfaioya).
      - For Chef Cookbook, open a new issue to announce the new release. See [example](https://github.com/verifi-inc/mattermost/issues/2).
      - For Yunohost, open a new pull request to update the version. See [example](https://github.com/kemenaran/mattermost_ynh/pull/11).
      - For OpenShift, open a new pull request to update the version. See [example](https://github.com/goern/mattermost-openshift/pull/13).
4. QA:  
    - Verifies each of the issues in the patch release are fixed
5. Marketing:
    - Prepare [blog post](https://about.mattermost.com/mattermost-3-6-2/) for mattermost.com and [Twitter announcement](https://twitter.com/mattermosthq/status/827193482578112512), and send for marketing lead to review. Once reviewed, schedule for 08:00 PST on the day after dot release

### K. (T-minus 0 working days) Release Day

1. Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete, if not alert the release manager
    - Schedule a release retrospective meeting, to be held within 5 days from the release
    - Post key dates for the next release in the header of the Release Discussion channel and remove links to RC candidates and testing spreadsheet
        - Make sure that statutory holidays for Canada and US are accounted for in the release dates
    - Check for any [UserVoice](https://docs.google.com/spreadsheets/d/1nljd4cFh-9MXF4DxlUnC8b6bdqijkvi8KHquOmK8M6E/edit#gid=0) feature suggestions that were completed in the current release
      - Find the [release tweet](https://twitter.com/mattermosthq/status/854781715914555393) and insert a link to the tweet next to the feature that shipped with the release.
    - For the next release, create the following team meetings. If they conflict with existing meetings, check with meeting owner to reschedule or reschedule the release meeting
      - PM Release Update meeting on T-15 at 7:30am San Francisco time
      - Major Feature Complete Meeting on T-12 at 10:00am San Francisco time
      - Judgment Day Meeting on T-10 at 10:00am San Francisco time
      - Code Complete Meeting on T-9 at 10:00am San Francisco time
      - Release Triage and Update Meeting each weekday starting at T-10 and ending at T-2 at 9:30am San Francisco time for PM, QA and release dev.
    - Prepare tickets for the next release, with a corresponding vX.X prefix, and put the tickets in the appropriate sprints as follows:
        - The week RC is cut:
            - [RC Build Testing for core team](https://mattermost.atlassian.net/browse/PLT-2208)
         - Release week (for GitLab dev owner)
             - [Test Gitlab Omnibus RC install of Mattermost](https://mattermost.atlassian.net/browse/PLT-2197)
         - Release week (for dependancies owner)
             - Upgrade dependancies for Webapp and Server
         - Week after release (for GitLab dev owner)
             - [Submit Gitlab Omnibus RC install of Mattermost](https://mattermost.atlassian.net/browse/MM-9872)
    - Confirm that [mattermost-docker](https://github.com/mattermost/mattermost-docker/releases) has been updated to the latest version (contact the maintainer via direct message on pre-release if necessary)
    - Contact owners of [community installers](http://www.mattermost.org/installation/) or submit PRs to update install version number
      - For Puppet, Heroku and Ansible Playbook, post to Installers and Images channel announcing the new release. See [example](https://pre-release.mattermost.com/core/pl/fgjqthmn67nujjtx4fcrn1hd9a).
      - For Chef Cookbook, open a new issue to announce the new release. See [example](https://github.com/ist-dsi/mattermost-cookbook/issues/22).
      - For Yunohost, open a new pull request to update the version. See [example](https://github.com/YunoHost-Apps/mattermost_ynh/pull/103).
      - For OpenShift, open a new issue to update the version. See [example](https://github.com/rhdt/mattermost-openshift/issues/7).
2. Docs:
    - Create a new branch on docs for the next release - `vX.X-documentation`
        - Submit a PR for changelog against the `vX.X-documentation` branch and add a `Work in Progress` label for it
        - Submit a PR to change version number in `docs/source/conf.py` against the `vX.X-documentation` branch
3. Logistics:
    - Close the release in Jira ([releases page](https://mattermost.atlassian.net/projects/PLT?selectedItem=com.atlassian.jira.jira-projects-plugin%3Arelease-page&status=unreleased))
        - If there are many unresolved tickets in the current release, ask the release manager to review the ticket queue
        - Otherwise, release the fix version (Actions > [...] > Release)
4. Build:
    - Put pre-release back on master
    - Put CI servers and translation server back onto master, and post in Release Discussion channel once done
    - Update [ci-linux-mysql-prev](https://ci-linux-mysql-prev.mattermost.com) to the previous release version
5. Dev:
    - Delete RCs after final version is shipped
    - Confirm gitlab.mattermost.com is updated to final build
    - Merge changes made to release branch into `master`
    - Update existing tickets or create new ones for the next release
6. Marketing:
    - Turn on CrazyEgg for blog post page
    - Confirm marketing has been posted (animated GIFs, screenshots, mail announcement, tweets, blog posts)
    - Update @mattermosthq Twitter profile with the next release date
    - Prepare retweet of GitLab release tweet ([see example here](https://pre-release.mattermost.com/core/pl/k7wchwj5mtrhucj6don96yx3sc))

### L. (T-plus 5 working days) Release Updates
1. Release Manager:
    - Post this checklist in Release Checklist channel
    - Verify all items in the last posted release checklist are complete
    - Check that dependancies have been upgraded
    - Update Security Research Hall of Fame on the [Responsible Disclosure Policy](https://about.mattermost.com/report-security-issue/) page
    - Update 'latest version of Mattermost' supported in the Airtable Integrations Directory on the [Mattermost Apps and Integrations](https://about.mattermost.com/community-applications) page
2. Leads:
    - Update [company roadmap at mattermost.com](https://about.mattermost.com/direction/)

### M. (T-plus 10 working days) Update Mattermost Security Page
1. Release Manager:
    - Post [Mattermost Security Updates](https://about.mattermost.com/security-updates/) after reviewing with security lead
      - If a dot release is shipping with security fixes, do not post new details until T-plus 10 working days from the dot release ship date
    - Update Security Issues spreadsheet with issue number from posted update (e.g. v3.2.0.1)

## Release Numbering

Mattermost numbers its stable releases based on the following format:  
  `[Version Number].[Major Build Number].[Minor Build Number]`

Version Number:
- Indicates a major system release (e.g. 1.x.x, 2.x.x)

Major Build Number:
- Indicates significant new functionality, (e.g. 0.5.x, 0.6.x, 0.7.x)

Minor Build Number:
- Indicates a bug fix or security release (e.g. 1.2.5, 1.2.6)
