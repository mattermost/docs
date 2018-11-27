# Dot Release Process

If a bug fix release is required, run through the below steps.

## Release Timeline

Notes:
- All cut-off dates are based on 10am ([San Francisco Time](http://everytimezone.com/)) on the day stated.
- T-minus counts are measured in "working days" (weekdays other than major holidays concurrent in US and Canada) prior to release day.

### A. (T-minus 4 working days) Code Complete

1. QA Release Manager:
    - Once the list of bugs to be fixed is finalized, post this checklist in Release Checklist channel
    - Make a post in Announcements channel announcing the dot release to the rest of the team with links to approved tickets and include a link to the ticket to submit the GitLab MR
2. Operations:
    - Notify community about upcoming dot release through a Twitter announcement and in changelog with links to approved fixes and a date tagged as "TBD"
3. Dev Ops:
    - Cherry pick bug fixes to the release branch, unless completed by devs
4. PM GitLab Relationship Owner:
    - If appropriate, open an issue in [GitLab Omnibus](https://gitlab.com/gitlab-org/omnibus-gitlab) mentioning a dot release is coming if it affects their build. [See example](https://gitlab.com/gitlab-org/omnibus-gitlab/issues/3099)
      - Open a ticket to [submit Gitlab Omnibus RC install of Mattermost](https://mattermost.atlassian.net/browse/MM-10365)

### B. (T-minus 3 working days) Release Candidate Cut

1. Dev Ops:
    - Cut new RCs after verifying with QA Release Manager (approved fixes should be merged)
    
### C. (T-minus 2 working days) Release Candidate Testing

1. QA Release Manager:
    - If the dot release takes place during a regular release, update ``ci-linux-mysql-prev`` to dot-release RCs for the previous release and keep ``rctesting.reddogsofwar`` on the latest regular release version
    - Test the new RC to verify fixes merged to the release branch work
    - Post in Release Discussion channel after testing

### D. (T-minus 0 working days) Release Build Cut

Once bug fix release is ready to cut:

1. Dev Ops:
    - Tag a new release (e.g. 1.1.1) and run an official build
    - Verify hashes and GPG signatures are correct, once build is cut
2. QA Release Manager:
    - Merge the Changelog PR with notes on patch releases (see [example entry](https://docs.mattermost.com/administration/changelog.html#release-v3-5.1))
    - Update the [version archive](https://docs.mattermost.com/administration/version-archive.html)
    - Update [Mattermost server download page](https://mattermost.org/download) with the links to the EE and TE bits
      - Test the download links before and after updating the page
3. Operations:
    - Contact owners of [community installers](http://www.mattermost.org/installation/) or submit PRs to update install version number
      - For Puppet, Heroku and Ansible Playbook, post to Installers and Images channel announcing the new release. See [example](https://pre-release.mattermost.com/core/pl/5eh8fw3jaiyzzqoc6nfwfaioya).
      - For Chef Cookbook, open a new issue to announce the new release. See [example](https://github.com/verifi-inc/mattermost/issues/2).
      - For Yunohost, open a new pull request to update the version. See [example](https://github.com/kemenaran/mattermost_ynh/pull/11).
      - For OpenShift, open a new pull request to update the version. See [example](https://github.com/goern/mattermost-openshift/pull/13).
4. PM GitLab Relationship Owner:
    - Work with a developer to submit GitLab MR [following this process](https://docs.mattermost.com/process/gitlab-process.html#merge-requests) and [test the upgrade](https://docs.google.com/document/d/1mbeu2XXwCpbz3qz7y_6yDIYBToyY2nW0NFZq9Gdei1E/edit#heading=h.ncq9ltn04isg) once the GitLab MR is merged and included in their RC.
5. Marketing:
    - Prepare [blog post](https://about.mattermost.com/releases/mattermost-4-10/) for mattermost.com and [Twitter announcement](https://twitter.com/mattermosthq/status/827193482578112512), and send for marketing lead to review. Once reviewed, schedule for 08:00 PST on the day after dot release
