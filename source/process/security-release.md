# Security Release Process

If a security fix release is required, run through the below steps.

## Release Timeline

Notes:
- All cut-off dates are based on 10am ([San Francisco Time](http://everytimezone.com/)) on the day stated.
- T-minus counts are measured in "working days" (weekdays other than major holidays concurrent in US and Canada) prior to release day.

### A. (T-minus 4 working days) Code complete

1. Release Manager:
    - Once the list of security issues to be fixed is finalized, post this checklist in Release Checklist channel
    - Notify community about upcoming security release through a Twitter announcement and in changelog with links to approved fixes and a date tagged as "TBD"
    - Email GitLab release team about upcoming security release.
    - Work with a developer to submit GitLab MR [following this process](https://docs.mattermost.com/process/gitlab-process.html#merge-requests) and [test the upgrade](https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg) once the GitLab MR is merged and included in their RC.
     - Open a ticket to [submit Gitlab Omnibus RC install of Mattermost](https://mattermost.atlassian.net/browse/MM-10365)
    - Make a post in Announcements channel announcing the security release to the rest of the team with links to approved tickets and include a link to the ticket to submit the GitLab MR
2. Dev:
    - PRs for hotfixes are made to release branch
    - Review PRs made from release branch and merge changes into the release branch as required and merge the release branch back into master once per day

### B. (T-minus 3 working days) Release Candidate Cut

1. Build:
    - Verify with Release Manager before cutting any new dot release RCs (approved fixes should be merged)
    
### C. (T-minus 2 working days) Release Candidate Testing

1. QA:
    - If the dot release takes place during a regular release, update ``prev.test.mattermost.com`` to dot-release RCs for the previous release and keep ``rc.test.mattermost.com`` on the latest regular release version
    - Test the new RC to verify fixes merged to the release branch work
    - Post in Release Discussion channel after testing
2. Logistics:
    - If the security researcher has not previously received a security researcher mug, order one for them 

### D. (T-minus 0 working days) Release Build Cut

Once security fix release is ready to cut:

1. Dev:
    - Tag a new release (e.g. 1.1.1) and run an official build
    - Verify hashes and GPG signatures are correct, once build is cut
    - Delete RCs after final version is shipped
2. Release Manager:
     - Update the changelog
     - Update the [version archive](https://docs.mattermost.com/administration/version-archive.html)
     - Update the [ESR documentation](https://docs.mattermost.com/administration/extended-support-release.html#what-are-the-current-supported-esr-versions)
     - Update [Mattermost server download page](https://mattermost.org/download) with the links to the EE and TE bits
      - Test the download links before and after updating the page
    - Confirm that [mattermost-docker](https://github.com/mattermost/mattermost-docker/releases) has been updated to the latest version (contact the maintainer via direct message on community server if necessary)
    - Contact owners of [community installers](http://www.mattermost.org/installation/) or submit PRs to update install version number
      - For Puppet, Heroku and Ansible Playbook, post to Installers and Images channel announcing the new release. See [example](https://community.mattermost.com/core/pl/5eh8fw3jaiyzzqoc6nfwfaioya).
      - For Chef Cookbook, open a new issue to announce the new release. See [example](https://github.com/verifi-inc/mattermost/issues/2).
      - For Yunohost, open a new pull request to update the version. See [example](https://github.com/kemenaran/mattermost_ynh/pull/11).
      - For OpenShift, open a new pull request to update the version. See [example](https://github.com/goern/mattermost-openshift/pull/13).
    - Update Security Research Hall of Fame on the [Responsible Disclosure Policy](https://about.mattermost.com/report-security-issue/) page
    - Post [Mattermost Security Updates](https://about.mattermost.com/security-updates/) 30 days after the dot release has shipped
      - Update Security Issues spreadsheet with issue number from posted update (e.g. v3.2.0.1)
3. Marketing:
    - Prepare [blog post](https://about.mattermost.com/releases/mattermost-4-10/) for mattermost.com, MailChimp email blast, and [Twitter announcement](https://twitter.com/mattermosthq/status/827193482578112512), and send to marketing lead for review. Once reviewed, schedule for 08:00 PST on the day after dot release
    
