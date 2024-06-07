# Client compatibility

```{include} ../_static/badges/allplans-cloud-selfhosted.md
```

As an MME admin, what Mattermost server versions (and desktop clients) can I deploy/rollout for our operating system? 
- How long is that version supported? 
- What’s my upgrade path look like from here?

## Desktop app

What Mattermost desktop app version should I install, if my system admin hasn’t already decided that for me?

Caveats to note:
- System admins should advise their end users not to download the latest releases from the App Store (& Android equivalent). These releases may upgrade you to a non-ESR version.
- System admins may also want to consider disabling automatic client updates to avoid users from upgrading to non-ESR releases.

## Mobile app

We strongly recommend using the latest mobile app release that's tested against all supported servers and all supported ESRs. In addition, we recommend the following guidelines:
- Use the latest app versions for the latest security and user experience enhancements.
- Integrate reviews of desktop and mobile app changelog notes into your IT operational procedures. 
- Our product changelogs contain important information about version-specific requirements for features, functionality, and security fixes. 
- Staying informed about these changes helps you avoid potential issues, proactively plan for version-specific requirements, and leverage new capabilities as they become available.

```{Note}
Earlier 4.x versions of Mattermost Desktop App and earlier v1.x versions of the Mobile App are backwards compatible and are supported with our supported Extended Support Releases. However, for an optimal user experience and for latest security fixes, we strongly recommend upgrading both your Mattermost Desktop and Mobile Apps to the latest version.
```
