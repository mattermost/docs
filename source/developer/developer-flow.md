Developer Flow
-----------------------------

See developers.mattermost.com for the developer flow of the following repositories:
 - [mattermost-server](https://developers.mattermost.com/contribute/server/developer-setup)
 - [mattermost-webapp](https://developers.mattermost.com/contribute/webapp/developer-setup)
 - [mattermost-redux](https://developers.mattermost.com/contribute/redux/developer-setup)
 - [mattermost-mobile](https://developers.mattermost.com/contribute/mobile/developer-setup)
 - [desktop](https://developers.mattermost.com/contribute/desktop/developer-setup)
 
### Testing with GitLab Omnibus ###

To test a locally compiled version of Mattermost with GitLab Omnibus, replace the following GitLab files:
 * The compiled `platform` binary in `/opt/gitlab/embedded/bin/plattermost`
 * The assets (templates, i18n, fonts, webapp) in `/opt/gitlab/embedded/service/mattermost`
