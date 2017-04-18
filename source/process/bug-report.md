# Bug Reports

A bug for Mattermost is defined as "any obvious error". Errors on unsupported platforms are not considered bugs.

Sample bugs:
   - [The front page is blank.](https://mattermost.atlassian.net/browse/PLT-3030)
   - [/msg does not work for users outside of the current team.](https://mattermost.atlassian.net/browse/PLT-2911)
   - [Whitespace is removed beside emoticons.](https://mattermost.atlassian.net/browse/PLT-3034)

Sample non-bugs:
   - Sort channels based on custom ordering.
   - Mattermost does not have a native app for Windows Phone.
   - @all does not work.

## Bug Report Format

A well-written bug report consists of several components:
   1. **Summary**, the bug in one sentence.
   2. **Reproduction Steps**, how to reproduce the bug.
   3. **Expected Behavior**, describe the bug in detail.
   4. **Observed Behavior**, what exactly happened.
   5. **Possible Fixes** (optional), linking code/settings that may have caused the bug.
   6. **Screenshots** (optional), any relevant screenshots

## How to File A Good Bug Report

The most important part of a bug report is the text, if a developer cannot tell what you meant, then the bug report was useless. Well written bug reports are:
   - **Absolute**, if something can be done in two different ways, state exactly which one you used.
   - **Verbose**, giving more information is almost always more useful than less.
   - **Explicit**, avoid the use of pronouns. Words such as "it", or references such as "the box" are often unclear.

### The Summary

Be as clear as you can in the summary, a good summary tells the reader:
   - **What** happened? Be as exact as you can (e.g. The app crashes)
   - **How** did it happen? Give a brief description of the process used (e.g. when switching channels from Town Square to any other channel)
   - **Where** does it happen? Include the version number/platform. (e.g. on Android v5.1 running Mattermost v3.0.2.)
   
### Reproduction Steps

State exactly which actions you took before encountering the bug. A good list of reproduction steps is:
   - **Clear**, anyone should be able to reproduce the bug using just your instructions
   - **Accurate**, no vague descriptions should be used. (e.g. "Switch channel to Off-Topic" vs. "Switch channel to Off-Topic by clicking on the channel in the LHS")
   - **Inclusive**, included all relevant information for the developer. (e.g. screen resolution for UI issues, hardware/internet specifications for performance issues)

Consider including the following (depending upon relevance):
   - Recent software/hardware changes (e.g upgrading Mattermost, migrating to a new server)
   - Reproducibility (always, intermittent, or single occurence)
   
### Behavior

#### Expected

Clearly describe the intended behavior upon executing your reproduction steps. Expectations can be based upon common sense/help text (e.g. "Save" should save, app should not crash), or feature specifications (e.g. /join should join any channel open to the current user). Include modified screenshots/diagrams as necessary.

#### Observed

What you have actually seen upon executing your reproduction steps. Be sure to include:
   - A detailed description of what you see
   - Screenshots (if applicable)
   - Exact error messages (if applicable)
   - JavaScript errors (if applicable)
   - Server logs (if applicable)

### Possible Fixes

Including any potential fixes, or areas to look into, for developers reading your bug report. Consider including section(s) of code. This section is completely optional.

## Sample Bug Reports

```
Summary: Preview mode is persistent when switching channels on Chrome, Mattermost v3.0.3
Reproduction Steps:
   1. Type "test" in center channel of [channel_1]
   2. Click 'Preview'
   3. Switch to [channel_2]
Expected Behavior: Message box is no longer in preview mode
Observed Behavior: Message box remains in preview mode (and is locked)
```

```
Summary: Unabled to log in with LDAP account if an existing account shares its username, Mattermost v3.0.3
Reproduction Steps:
   1. Create an account using email with the username "test.one"
   2. Log out and return to the login page
   3. Attempt to log in with LDAP account using the username "test.one"
Expected Behavior: An error message is displayed that explains the situation and tells the user to log in using email/password, or to contact their system administrator.
Observed Behavior: "We received an unexpected status code from the server. (500)"
```

```
Summary: CTRL+UP does nothing if user has not made a post to a channel
Reproduction Steps:
   1. Join a new channel
   2. Press 'CTRL'+'UP'
Expected Behavior: The message box should contain the latest message posted.
Observed Behavior: The message box contains nothing
```
