# v10 changelog

```{Important}
Support for Mattermost Server v8.1 [Extended Support Release](https://docs.mattermost.com/deploy/about/release-policy.html#extended-support-releases) has come to the end of its life cycle in May 15, 2024. Upgrading to Mattermost Server v9.5 or later is required.
- See the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) documentation for details on upgrading to a newer release.
- See the [changelog in progress](https://bit.ly/2nK3cVf) for details about the upcoming release.
```

(release-v10.0-feature-release)=
## Release v10.0 - Major Release

**Release day: 2024-09-16**

More information on this Mattermost major release coming soon. See the {doc}`Mattermost release policy </about/release-policy>` documentation for details on {ref}`release types <about/release-policy:release types>`.

### Upcoming Breaking Changes in v10.0 Release

Mattermost v10.0 is planned for September, 2024. Below is a list of planned breaking changes for this release:

1. **MySQL Databases** - We will no longer support new installations using MySQL starting in v10. All new customers and/or deployments will only be supported with the minimum supported version of the PostgreSQL database. End of support for MySQL is targeted for Mattermost v11.
2. **Apps Framework** - Apps framework will be deprecated in a future upcoming release. Please extend Mattermost using webhooks, slash commands, oAuth2 apps and plugins.
3. **Playbooks for Enterprise** - An Enterprise license will be required to use v2.0+ Playbooks functionality starting in v10. Team Edition and Professional deployments can continue to use Playbooks v1.x. Security and feature updates will only be added to Playbooks v2.0+.
