# Release Policy

```{include} ../_static/badges/allplans-selfhosted.md
```

This page describes Mattermost’s release policy, and our recommended practices around releases, including extended support releases, so that you can allocate your IT resources effectively.

To ensure a secure, functional, performant, and efficient Mattermost deployment, system admins managing a self-hosted deployment need to be proactive in:
- monitoring Mattermost release cycles and planning upgrades before life cycles end,
- considering the use of [extended support releases](#extended-support-releases) for longer-term stability, and
- keeping both server and client applications updated.

(release-types)=
## Release Types

Mattermost releases include feature, extended support, and major releases. Each release has a specified life cycle start and end date, and life cycles depend on the release type. 

- **Feature**: Feature releases contain new features and include high severity and high impact security backported to the previous 3 monthly releases. This is to ensure your organization's Mattermost deployment remains secure and stable. It's crucial to apply feature updates to maintain the security of your Mattermost deployment.
- **Extended**: Releases maintained for a longer period of time that receive backports for security fixes and major bug fixes for the length of their life cycle. Learn more about [Mattermost extended support releases](#extended-support-releases) below.
- **Major**: Annual mid-year releases that follow a release theme, and include multiple new features.

With multiple release types, you can plan the upgrade path that best suits your organization's needs and compliance requirements. Align your plan with your organization's IT strategy and risk management policies to ensure continuous operation without exposure to security vulnerabilities.

See the full list of all Mattermost Server and desktop app releases and life cycles.

(extended-support-releases)=
## Extended Support Releases

```{include} ../_static/badges/ent-only.md
```

Mattermost Extended Support Releases (ESRs) are a strategic choice for organizations looking for stability and reduced frequency of updates. Using ESRs can minimize disruptions associated with frequent upgrades, making them an attractive option for environments where stability is paramount.

Starting with the August 2025 Mattermost server and desktop app releases (server v10.11 and desktop app v5.13), Mattermost has adjusted the ESR life cycle as follows: 
 - **Extended Cadence**: The ESR release cycle has changed from every 6 months to every 9 months. 
 - **Prolonged Support**: The support window has increased from 9 months to 12 months. 

We strongly recommend planning ahead for upgrades before the end of an ESR's life cycle to ensure continuity in receiving security updates.

ESRs don’t include changes to product functionality or new features. ESRs are intended for organizations who value stability over having the newest features and improvements, or who have a long internal testing and certification process to undergo when upgrading. Consider using ESRs for more stable and long-term deployments, especially in environments where frequent updates are challenging. If your organization prefers to have the newest features and improvements, Extended Support Releases may not be the best fit for you.

To install extended support releases, follow our [install](/guides/deployment-guide) or [upgrade](/upgrade/upgrading-mattermost-server) documentation. To restore a previous ESR, restore the database and previous version if you need to revert an upgrade. Previous ESR versions continue remain subject to a [life cycle end date](/about/mattermost-server-releases).

```{Important}
- We strongly recommend reviewing [upgrade best practices](https://docs.mattermost.com/upgrade/prepare-to-upgrade-mattermost.html#upgrade-best-practices) for upgrading, and [important upgrade notes](/upgrade/important-upgrade-notes) for all the versions beyond the current ESR version you have currently installed. See the [Mattermost v9 changelog](https://docs.mattermost.com/about/mattermost-v9-changelog.html) for a list of database, API, and `config.json` updates for all v9.x releases.
- Your license key is decoupled from the Mattermost server version, so you can upgrade to the latest ESR using a legacy license.
We highly recommend working with your Mattermost Account Team to plan for a migration to our new plans, and to access the latest features such as persistent notifications, advanced compliance features, call recordings, and more.
```

```{mermaid}

gantt
    dateFormat  YYYY-MM-DD
    axisFormat  %b %y

    section Releases
    v10.4                  :done,  2025-01-16, 2025-04-15
    v10.5 & Desktop App v5.11 Extended Support :crit,    2025-02-16, 2025-11-15
    v10.6                  :done, 2025-03-16, 2025-06-15
    v10.7                  :done, 2025-04-16, 2025-07-15
    v10.8                  :active, 2025-05-16, 2025-08-15
    v10.9                  :active, 2025-06-16, 2025-09-15
    v10.10                 :active, 2025-07-16, 2025-10-15
    v10.11 & Desktop App v5.13 Extended Support :crit,    2025-08-16, 2026-08-15
    v10.12                 :active, 2025-09-16, 2025-12-15
    v11.0                  :active, 2025-10-16, 2026-01-15
```

**Timeline Legend:**
The chart above shows both release dates and end-of-life dates for each version. ESRs provide longer-term stability for organizations preferring less frequent updates.
- 🔵 **Blue bars**: Regular feature releases (monthly releases with standard support lifecycle)
- 🔴 **Red bars**: Extended Support Releases (ESRs) - Released every 6-9 months with extended 9-12 month support

(esr-notifications)=
### ESR Notifications

```{include} ../_static/badges/ent-only.md
```

When an ESR is at the end of its life cycle, there will be announcements ahead of time to provide time for people to test, certify, and deploy a newer ESR version before support ends. After a release reaches its end-of-life, no further updates will be provided for that version. 

To receive updates about Extended Support Releases, sign up for [our mailing list](https://eepurl.com/dCKn2P).

For a new upcoming ESR, an email is sent out 3 months before the end of support for an ESR version. This email includes a note about the new ESR that was just published. A second email is sent out during the month when an ESR version is reaching the end of support.

For deprecated ESRs, an email announcement is sent 3 months in advance. We also add reminders on our release announcements, changelogs, important upgrade notes, and the [Mattermost Discussion Forums](https://forum.mattermost.com/) site.

### Legacy Releases

The following table lists all releases across Mattermost v7.0 and v8.0, including ESRs. See the [unsupported legacy releases](https://docs.mattermost.com/about/unsupported-legacy-releases.html) documentation for comprehensive changelog details for these legacy releases.

```{Important}
- If you're on a legacy Mattermost release prior to v7.1, in order to take advantage of newer Mattermost releases, you must upgrade to [v7.1 ESR](https://docs.mattermost.com/about/unsupported-legacy-releases.html#release-v7-1-extended-support-release) at a minimum.
- Upgrading from ESR-to-ESR (``major`` -> ``major_next``) is fully supported and tested. However, upgrading from ESR-to-ESR (``major`` to ``major+2``) is supported, but not tested. If you plan to upgrade across multiple releases, we strongly recommend upgrading from an ESR to another ESR. For example, if you're upgrading from v7.1 ESR, upgrade to the [v7.8 ESR](https://docs.mattermost.com/about/unsupported-legacy-releases.html#release-v7-8-extended-support-release), or the [v8.1 ESR](https://docs.mattermost.com/about/unsupported-legacy-releases.html#release-v8-1-extended-support-release) before attempting to upgrade to the [v9.5 ESR](https://docs.mattermost.com/about/mattermost-v9-changelog.html#release-v9-5-extended-support-release) or the v9.11 ESR.
```

| **Release** | **Release Type** | **Support ended** | 
|:---|:---|:---|
| v8.1 | Extended | 2024-05-15 |
| v8.0 | Major | 2023-10-15 |
| v7.10 | Feature | 2023-07-15 |
| v7.9 | Feature | 2023-06-15 |
| v7.8 | Extended | 2023-11-15 |
| v7.7 | Feature | 2023-04-15 |
| v7.5 | Feature | 2023-02-15 |
| v7.4 | Feature | 2023-01-15 |
| v7.3 | Feature | 2022-12-15 |
| v7.2 | Feature | 2022-11-15 |
| v7.1 | Extended | 2023-04-15 |
| v7.0 | Major | 2022-09-15 |
