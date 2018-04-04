# Mobile App Release Process

The Mattermost Mobile Apps team works on a monthly release process, with a new version submitted to the iOS App Store and Google Play Store on the 5th of each month. Note: iOS App Store approval may take a few days after the 5th. 

## Release Timeline

Notes:

- All cut-off dates are based on 10am (San Francisco Time) on the day stated.
- T-minus counts are measured in "working days" (weekdays other than major holidays in the US and Canada) prior to release day.

### A. (T-minus 8 working days) Code Complete and Release Candidate Cut 

1. PM:
    - Submit pull request for changelog
    - Check the minimum server version required and submit pull request to update in fastlane files
2. Dev:
    - Finish review of last pull requests for the current release and merge
3. QA:
    - Confirm all pull requests merged into the current release have been tested
4. Build:
    - Create release branch for mattermost-mobile and mattermost-redux
    - Cut release candidate build


### B. (T-minus 7 working days) Release Candidate Testing

1. QA:
    - Post release testing instructions and spreadsheet to Native Mobile Apps channel
2. Team:
    - Test assigned areas of the testing spreadsheet and file any bugs found in Jira 
    - Daily triage of hotfix candidates and decide on whether and when to cut next RC or final
3. Dev:
    - Make pull requests for hotfixes to the release branch
    - Review PRs made to release branch and merge changes into the release branch
4. Build:
    - Verify with Release Manager before cutting any new RCs (approved fixes should be merged)
    - Push next RC to acceptance and announce in Native Mobile Apps channel
5. PM:
    - Check that the release candidate is available to beta testers 
6. QA: 
    - Test the new RC to verify fixes merged to the release branch work

### C. (T-minus 0 working days) Release Build Cut and Submitted to App Stores 

1. Build: 
    - Tag the release and cut the final build
    - Upload the .ipa and .apk files to GitHub
    - Merge the release branch back in to master
    - Review and update project dependencies as needed
2. PM:
    - Final changelog updates to known issues and contributors section
    - Submit final build to iOS App Store and Google Play Store
    - Confirm that minimum server version required is clear in update notes 
    - Create release in GitHub 
    - Close the release in Jira 
    - Schedule a release retrospective meeting, to be held within 5 days from the release
    - Post key dates for the next release in the header of the Release Discussion channel
        - Make sure that statutory holidays for Canada and US are accounted for in the release dates
3. Marketing:
    - Finish draft of blog post and marketing images and send to marketing lead for review
4. Logistics:
    - Make a pinned post in Native Mobile Apps channel with the dates for next release

### D. (T-plus X days) Release Marketing

1. Marketing:
    - After the apps are approved and on the App Store (number of days may vary), send out release marketing
    - Update the app version on the [download page](https://about.mattermost.com/download/#mattermostApps)
