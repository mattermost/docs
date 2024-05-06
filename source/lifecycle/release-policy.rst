Mattermost release policy
=========================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This page describes Mattermost’s release policy, and our recommended practices around deployment updates and ESRs, so that you can allocate your IT resources effectively.

To ensure a secure, functional, performant, and efficient Mattermost deployment, system admins managing a self-hosted deployment need to be proactive in:
- monitoring release cycles and planning upgrades before life cycles end,
- considering the use of ESRs for longer-term stability, and
- keeping both server and client applications updated (compatibility)

Release life cycles
-------------------

Mattermost releases include feature, extended support, and major releases. Each release has a specified life cycle start and end date, and life cycles depend on the release type. 

- **Feature release**: Feature releases contain new features and include high severity and high impact security backported to the previous 3 monthly releases. This is to ensure your organization's Mattermost deployment remains secure and stable. It's crucial to apply feature updates to maintain the security of your Mattermost deployment.
- **Extended Support Release (ESR)**: Releases maintained for a longer period of time that receive backports for security fixes and major bug fixes for the length of their life cycle. Learn more about `Mattermost <#extended-support-releases>` below.
- **Major release**: Annual mid-year releases that follow a release theme, and include multiple new features.

With multiple release types, you can plan the upgrade path that best suits your organization's needs and compliance requirements. Align your plan with your organization's IT strategy and risk management policies to ensure continuous operation without exposure to security vulnerabilities.

See the full list of all Mattermost Server and desktop app releases and life cycles.

Extended support releases
-------------------------

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

Mattermost Extended Support Releases (ESR) are a strategic choice for organizations looking for stability and reduced frequency of updates. Using ESRs can minimize disruptions associated with frequent upgrades, making them an attractive option for environments where stability is paramount. New ESRs are released twice a year, every February and August release. An ESR is supported for nine months to provide customers with enough time to test and upgrade to the next ESR. 

ESRs don’t include changes to product functionality or new features. ESRs are intended for organizations who value stability over having the newest features and improvements, or who have a long internal testing and certification process to undergo when upgrading. Consider using ESRs for more stable and long-term deployments, especially in environments where frequent updates are challenging. If your organization prefers to have the newest features and improvements, Extended Support Releases may not be the best fit for you.

We strongly recommend planning ahead for upgrades before the end of an ESR's life cycle to ensure continuity in receiving security updates.

[image here]

.. important::

    High severity and high impact security fixes are backported to ESRs for the duration of their life cycle to ensure your organization's Mattermost deployment remains secure and stable. It's crucial to apply these updates to maintain the security of your Mattermost deployment.

ESR Notifications
~~~~~~~~~~~~~~~~~~

When an ESR is at the end of its life cycle, there will be announcements ahead of time to provide time for people to test, certify, and deploy a newer ESR version before support ends. After a release reaches its end-of-life, no further updates will be provided for that version. 

To receive updates about Extended Support Releases, sign up for `our mailing list <https://eepurl.com/dCKn2P>`_.

For a new upcoming ESR, an email is sent out 3 months before the end of support for an ESR version. This email includes a note about the new ESR that was just published. A second email is sent out during the month when an ESR version is reaching the end of support.

For deprecated ESRs, an email announcement is sent 3 months in advance. We also add reminders on our release announcements, changelogs, :doc:`important upgrade notes </upgrade/important-upgrade-notes>`, and the `Mattermost Discussion Forums <https://forum.mattermost.com/>`_ site.