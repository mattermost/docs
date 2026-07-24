Team membership access policies
================================

.. include:: ../../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

From Mattermost v11.10, system admins and team admins can apply attribute-based access control (ABAC) directly to teams — controlling who can join a team based on user profile attributes. This extends the existing ABAC channel membership system to the team boundary, closing the "hallway access" gap where users who fail channel policies could still see the team, its member list, and its channel structure.

Team membership ABAC uses the same policies and attribute rules as channel ABAC, but behaves differently depending on whether the team is public or private:

- **Public teams (advisory mode)**: The policy never blocks access. Anyone can still join freely. Qualifying users who are not yet members see a **Recommended** chip in Browse Teams. Sync can auto-add qualifying users when enabled but never removes anyone.
- **Private teams (strict mode)**: The policy gates directory visibility, join evaluation, and membership at sync. Non-qualifying users cannot find or join the team. Non-qualifying members are removed at the next sync.

.. note::

   **Upgrade notice:** The Access tab in Team Settings has a new UI from Mattermost v11.10 that affects **every team on every deployment** — whether or not ABAC is licensed or enabled. The old "Allow any user to join" checkbox has been replaced by **Public Team / Private Team** selection cards. See `Access tab: Public/Private team cards`_ for details.

.. contents::
   :local:
   :depth: 2

Access tab: Public/Private team cards
---------------------------------------

.. important::

   This change affects **all Mattermost teams on all deployments**, regardless of whether ABAC is enabled or whether your organization has an Enterprise Advanced license. Any team admin who opens **Team Settings > Access** after upgrading will see the new UI.

**What changed:** The "Allow any user to join" checkbox has been permanently replaced by two selection cards:

- **Public Team** — anyone on the server can find and join.
- **Private Team** — only invited members can join.

**Why the change was made:** The cards make a team's public-vs-private state explicit and unambiguous, which is what team ABAC enforcement depends on to decide between advisory and strict mode.

**Behavior without ABAC:** Functionally identical to the old checkbox. Public Team = "Allow any user to join" was ON. Private Team = it was OFF. No other behavior changes for teams that have no membership policy.

**Behavior with ABAC:** The cards drive the enforcement mode — public teams get advisory ABAC, private teams get strict ABAC. Mode changes on policy-governed teams may trigger a confirmation modal (see below).

**Default on new teams:** New teams are Private by default, so any policy assigned before explicitly choosing a mode activates strict enforcement. Teams are always protected by default; advisory mode requires explicitly selecting **Public Team**.

Switching modes
~~~~~~~~~~~~~~~~

**Private → Public:** Always safe — relaxes enforcement. Saves directly with no confirmation modal. If a policy is applied, the team immediately transitions to advisory mode: no existing members are removed.

**Public → Private:** If team ABAC is enabled (both flags on) and the team has a membership policy assigned, clicking **Private Team** opens a confirmation modal before saving:

- Title: **"Switch to Private Team?"**
- Body shows how many current members do not meet the policy criteria and will be removed at the next sync. (If no count is available, a generic warning is shown instead.)
- **Cancel** — closes the modal, no changes made.
- **Switch to Private** — saves the change and immediately creates a team sync job to enforce strict mode.

If no policy is assigned, switching Public → Private saves directly with no modal.

**The cards stay interactive on ABAC-governed teams.** ABAC never disables the Public/Private cards. A public-to-private switch on a governed team is guarded by the mode-flip confirmation modal described above, not by locking the cards.

Other Access tab fields (Invite Code and Allowed Email Domain) are unaffected by this change. On teams managed by LDAP/AD group sync, the Access tab shows a static "Members of this team are added and removed by linked groups" message instead of the cards.

Advisory and strict enforcement
---------------------------------

Whether a policy is enforced strictly or treated as advisory depends only on whether the team is public or private. The table below summarizes how each combination behaves.

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 20 15 15

   * - Team
     - ABAC policy?
     - Join gate
     - Browse Teams
     - Sync removal
     - Recommended tag
   * - Public
     - No
     - Open
     - Visible to all
     - N/A
     - No
   * - Public
     - Yes — **Advisory**
     - Open (no gate)
     - Visible to all
     - Skipped
     - Yes (qualifying non-members)
   * - Private
     - No
     - Invite-only
     - Members only
     - N/A
     - No
   * - Private
     - Yes — **Strict**
     - Denied for non-qualifying users
     - Hidden from non-qualifying non-members
     - Non-qualifiers removed
     - No

.. note::

   Auto-add is the only behavior that applies to **both** advisory and strict mode. When enabled, sync adds qualifying non-members regardless of whether the team is public or private.

Prerequisites
-------------

Before configuring team membership policies:

1. :doc:`Configure user attributes </administration-guide/manage/admin/user-attributes>` in the System Console.
2. Go to **System Console > System Attributes > Attribute-Based Access** and enable **Enable Attribute-Based Access Control**.
3. Enable the ``TeamMembershipAccessControl`` feature flag. See the Mattermost developer documentation for details on `enabling feature flags in a self-hosted deployment <https://developers.mattermost.com/contribute/more-info/server/feature-flags/#self-hosted-and-local-development>`_. Mattermost Cloud customers can request this feature flag be enabled by contacting their Mattermost Account Manager or by `creating a support ticket <https://support.mattermost.com/hc/en-us/requests/new?ticket_form_id=11184911962004>`_.
4. For Team Admins configuring rules: the ``manage_team_access_rules`` permission is required. This permission is included in the Team Admin role by default.

**What changes when the flags are off:**

.. list-table::
   :header-rows: 1
   :widths: 42 29 29

   * - Surface
     - Both flags ON
     - Either flag OFF
   * - Join gate (private teams)
     - Enforced — non-qualifying users denied
     - Off — anyone can join as before
   * - Browse Teams filter
     - Private+ABAC teams hidden from non-qualifying users
     - All teams visible
   * - Team Membership tab (Team Settings)
     - Visible to Team Admins and System Admins
     - Hidden — tab does not appear
   * - System Console per-team ABAC controls
     - Policy assignment + custom rules panel visible
     - Hidden
   * - Recommended tag
     - Shown to qualifying users on public+ABAC teams
     - Not shown
   * - Sync job — removal pass
     - Removes non-qualifiers from private+ABAC teams
     - No team sync jobs run
   * - Invite modal filtering
     - Filters on private+ABAC teams
     - All users shown, as before
   * - Public/Private cards (Access tab)
     - **Always visible** — not gated by these flags
     - **Still visible** — always rendered (see note above)
   * - Channel ABAC
     - Unaffected by team flag
     - Unaffected by team flag

System Admin configuration
---------------------------

Assign a membership policy to a team
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System Admins assign existing system-wide membership policies to teams via the per-team System Console page.

1. Go to **System Console > User Management > Teams** and open the team you want to configure.
2. Locate the **Membership Policy** section.
3. Select **Link to a policy** and choose an existing policy from the picker.
4. Select **Save**.

Before saving, a confirmation modal shows:

- The number of workspace users who currently qualify for the policy.
- The number of current team members who do not qualify (and will be affected at the next sync on private teams).
- An **empty-team warning** if the team is private and no current member qualifies.

**To remove a policy:** Select the trash icon next to the policy row, then **Save**. The team's enforcement flag is cleared and the team reverts to standard access behavior.

**Policy list team counts:** The **Membership Policies** list page shows the count of channels and teams each policy is applied to — for example, ``2 channels, 1 team``. A zero side is omitted (so ``1 team`` not ``0 channels, 1 team``).

Enable auto-add from the Membership Policy section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a parent policy is linked, the **Membership Policy** section shows an **Auto-add** checkbox per linked policy row. This checkbox is always enabled for any linked policy — it does not require custom rules to exist. Checking it and saving starts the backfill scan immediately.

This is separate from the **Auto-add members based on access rules** checkbox in the Custom access rules panel (see below), which requires at least one custom rule before it can be checked.

Configure custom access rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to a system-wide parent policy, System Admins can define team-specific custom rules directly on the per-team System Console page.

1. Go to **System Console > User Management > Teams** and open the team.
2. Enable the **Manage membership with attribute based membership policies** switch.
3. Scroll to the **Custom access rules** panel.
4. Select **Add attribute** to add a condition. For each condition, choose:

   - **Attribute**: The user profile attribute to evaluate.
   - **Operator**: How the attribute must match. Options: **Is**, **Is not**, **In**, **Starts with**, **Ends with**, **Contains**. For ranked attributes: **Is exactly**, **Is at least**, **Is greater than**, **Is at most**, **Is less than**.
   - **Value**: The required attribute value.

   All conditions are combined with a logical AND — users must satisfy all of them.

5. Optionally, check **Auto-add members based on access rules**. This checkbox requires at least one rule to be defined before it can be enabled.
6. Select **Save**. A confirmation modal shows qualifying and non-qualifying counts before changes are applied.

.. important::

   Saving rules always triggers an immediate team sync — **even when auto-add is off**. On private teams, this immediately enforces the rules by removing members who no longer qualify. Confirm the impact in the save modal before proceeding.

.. note::

   Custom rules compose additively with any parent policy assigned to the team. A user must satisfy **both** the parent policy and the custom rules. Custom rules cannot weaken or bypass the parent.

Sync status footer (System Console)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below the Custom access rules panel, a sync status footer appears when membership policy enforcement is enabled. It is rendered inside the white-box Custom access rules panel — scroll down within the panel to find it.

- **"Never synced."** with a **Sync now** link — no sync has run for this team yet.
- **"Last synced N minutes ago."** with a **Sync now** link — after a prior sync.
- Clicking **Sync now** changes the link to **"Syncing…"** with a spinner while the job is in-flight, then updates to **"Last synced just now."** on completion.

Monitor membership sync
~~~~~~~~~~~~~~~~~~~~~~~~

System Admins can review the results of team sync jobs from the System Console.

1. Go to **System Console > Access Control > Membership sync jobs**.
2. Select a job row to open the **Sync Job Details** modal.
3. Select the **Teams** tab.

The Teams tab shows per-team rows with:

- A ``+N added / −N removed`` summary for each governed team.
- A **mass-removal warning indicator** on any team row where more than 50% of members would be removed. This is a warning only — the job is not blocked.
- An expandable per-team user drill-down showing which users were added and removed.

.. note::

   The Teams tab appears only when viewing a team sync job directly, or a channel sync job that was chained from a team sync. The system console section heading was renamed from "Channel access control sync jobs" to **"Membership sync jobs"** to reflect both job types.

.. tip::

   The **Run sync job** button on the Membership Policies list page runs a channel sync only, not a team sync. To trigger a team sync, use the **Sync now** link on the per-team System Console page or in Team Settings > Team Membership tab.

Team Admin configuration
-------------------------

Team Membership tab
~~~~~~~~~~~~~~~~~~~~

From Mattermost v11.10, Team Settings has four tabs: **Info**, **Access**, **Team Membership**, and **Channel Membership**.

.. note::

   The fourth tab was previously labeled **Membership Policies**. It is now labeled **Channel Membership** and covers channel-scope policies only. The new **Team Membership** tab (the third tab) is for policies that control who can join the team itself.

The **Team Membership** tab lets Team Admins view the system policy applied to their team and configure team-specific custom rules — without requiring System Admin involvement for every change.

The tab is visible only when:

- **Enable Attribute-Based Access Control** is on.
- The ``TeamMembershipAccessControl`` feature flag is on.
- The user has the ``manage_team_access_rules`` permission (Team Admin or System Admin).

To open Team Settings: select the team name in the sidebar → **Team Settings** → **Team Membership** tab.

System policy indicator
~~~~~~~~~~~~~~~~~~~~~~~~

When a system-level policy is applied to the team by a System Admin, a non-dismissible information banner appears at the top of the Team Membership tab, showing the name of the applied policy. The banner is absent when no parent policy exists.

Configure custom rules
~~~~~~~~~~~~~~~~~~~~~~~

Team Admins can add attribute rules that apply on top of any system policy. These rules use the same Basic Mode editor as channel rules.

1. Select **Add attribute rule**.
2. Choose the attribute, operator, and value for each condition.
3. Add additional rules as needed. All rules are AND-combined.
4. Select **Save** to open the save confirmation modal.

Available operators: **Is**, **Is not**, **In**, **Starts with**, **Ends with**, **Contains**. For ranked attributes: **Is exactly**, **Is at least**, **Is greater than**, **Is at most**, **Is less than**.

.. important::

   Saving rules always triggers an immediate team sync — **even when auto-add is off**. On private teams, this removes members who no longer satisfy the rules. Review the impact counts in the confirmation modal before saving.

.. note::

   Team Settings rules are Basic Mode only. Advanced CEL expressions are not available here. For complex rules with nested logic or mixed operators, a System Admin must create a system-wide parent policy in the System Console.

Auto-add members
~~~~~~~~~~~~~~~~~

The **Auto-add members based on access rules** checkbox controls whether the sync job automatically adds qualifying non-members to the team.

- This checkbox is enabled only when at least one rule exists, **or** when a system-level policy is applied.
- Checking it and saving triggers an immediate backfill scan — qualifying non-members are added right away.
- Subsequent syncs continue to add newly qualifying users.
- Turning auto-add **off** does not remove any members — it is additive only. Toggling auto-add off also does **not** trigger a sync job.

Test matching users
~~~~~~~~~~~~~~~~~~~~

Select **Test matching users** to open a preview modal listing users who would match the current rules, before saving. This lets you verify your intended scope without applying the rules.

.. note::

   If the current rules would exclude the editing Team Admin, the result set is empty. This is intentional — the preview is fail-secure and does not leak information about restricted users.

Save confirmation and safety
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Selecting **Save** opens a confirmation modal before changes are applied. The modal shows:

- The number of workspace users who match the current rules.
- The number of current team members who do not qualify (and will be removed at the next sync on private teams).

**Empty-team warning**: For private teams, if no current member qualifies under the rules, the modal displays a highlighted warning. Save is not blocked, but the team will be empty until sync runs.

**Self-exclusion hard block**: If the rules would exclude the editing Team Admin, a separate error modal appears *before* the confirmation modal and prevents saving. Select **Back to editing** to adjust the rules.

.. note::

   The self-exclusion block only applies to the editing admin's own custom rules. A system-level parent policy that happens to exclude all Team Admins is not blocked here — this is a known limitation.

Sync status footer (Team Settings)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below the auto-add section, a sync status footer appears whenever the team has at least one rule or a parent policy applied:

- **"Never synced."** + **Sync now** link.
- **"Last synced N minutes ago."** + **Sync now** link.
- After clicking **Sync now**: **"Syncing…"** with spinner → **"Last synced just now."** on completion.

The footer is not shown in the empty state (no rules and no parent policy).

Clicking **Sync now** creates a team sync job scoped to this team only.

End-user experience
--------------------

Browse Teams
~~~~~~~~~~~~~

The Browse Teams directory respects team ABAC enforcement:

**Private + ABAC teams (strict mode):**

- Non-qualifying users who are not already members do not see the team in Browse Teams at all. The team is simply absent — not greyed out or locked.
- Qualifying users and existing members see the team normally.

**Public + ABAC teams (advisory mode):**

- All users see the team.
- Qualifying users who are not yet members see a **Recommended** chip (lightbulb outline icon) next to the team name.
- Users who are already members, or who do not qualify for the policy, do not see the chip.

**Teams without a policy:**

- Behave exactly as before — no filtering, no chip.

Invite People modal
~~~~~~~~~~~~~~~~~~~~

The Invite People modal adapts to the team's enforcement mode:

**Private + ABAC team (strict mode):**

- Only users who qualify for the team's membership policy appear in search results. Non-qualifying users are filtered out before any results are shown.
- A section notice informs admins: *"Only users who meet the membership requirements can be added to this team."*
- Qualifying users in the results show attribute value tags (for example, "Department: Engineering").

**Public + ABAC team (advisory mode):**

- All users appear in search results — there is no filtering because advisory mode never blocks access.
- A section notice is still shown informing admins that the team has membership requirements.
- A warning is shown when generating an invite link, noting that the link recipients will be subject to membership requirements.

**Team without a policy:**

- No change from previous behavior — all users appear, no notice shown.

Add Members flow (admin)
~~~~~~~~~~~~~~~~~~~~~~~~~

When a System Admin or Team Admin uses the **Add Members** admin flow on a private + ABAC team and selects multiple users, ABAC denials are reported per user without aborting the batch:

- Qualifying users in the selection are added successfully.
- Non-qualifying users show an inline **"Does not meet membership requirements"** indicator on their row.
- The batch continues — qualifying users are not affected by a co-selected user's denial.

On a public + ABAC team (advisory mode), all users can be added without restriction.

Team Members modal
~~~~~~~~~~~~~~~~~~~

When a team has an active membership policy:

- A requirements notice banner appears at the top of the Team Members modal explaining that membership is controlled by access rules.
- Qualifying members see attribute value tags on their own user entry (for example, "Department: Engineering").
- Members without the matching attributes see only the generic notice — attribute values are never shown to non-holders.

Membership notifications
~~~~~~~~~~~~~~~~~~~~~~~~~

**Removal notification:** When the sync job removes a non-qualifying member from a private team, that user receives a direct message from the System Bot identifying the team they were removed from. The message does not include policy names, attribute values, or CEL expressions.

**Auto-add notification:** When the sync job auto-adds a qualifying user to a team, that user receives a direct message from the System Bot identifying the team they were added to. Removal and auto-add notifications use different icons so users can distinguish them at a glance.

Policy inheritance and composition
------------------------------------

When a parent (system-level) policy and custom team rules both apply:

- The parent policy is shown in a non-dismissible info banner at the top of the Team Membership tab (read-only).
- The user must satisfy **both** the parent policy and the custom team rules to be admitted.
- Custom rules can only add restrictions — they cannot weaken or bypass the parent policy.
- If a parent policy is deleted, the deletion cascades to unlink it from the team. Child (team-scoped) policies are not cascade-deleted.

Sync behavior
--------------

A team sync batch runs in the following order:

1. **Evaluate team membership rules** for all teams that have a policy assigned.
2. **Removal pass** (private + ABAC teams only): remove members who no longer qualify. Each removal triggers a channel cascade — the user is removed from all channels within the team. Each removal notifies the user by system-bot DM and is recorded in the audit log. Ordinary, non-ABAC team leaves are not recorded as policy-driven cascades.
3. **Auto-add pass** (any mode, when auto-add is enabled): add qualifying non-members to the team. Each addition emits a system-bot DM.
4. **Channel membership sync** (chained): evaluate and apply channel policy changes. Deduped against any already-pending or in-progress channel sync job.

**Mass-removal guardrail**: If a sync pass would remove more than 50% of a team's current members, the job sets a warning flag visible in the Sync Job Details > Teams tab. The job is not blocked — all removals proceed — but the warning is surfaced for admin review.

Team sync also runs automatically every 30 minutes to handle attribute changes propagated from LDAP or SAML.

Mutual exclusivity with group sync
------------------------------------

A team managed by LDAP/AD group synchronization cannot have an ABAC membership policy assigned. Attempting to assign a policy to a group-synced team returns an error.

You must choose one membership control mechanism per team: group sync or ABAC.

Troubleshooting and FAQs
--------------------------

Why did the Access tab change and where did the "Allow any user to join" checkbox go?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v11.10, the "Allow any user to join" checkbox has been permanently replaced by **Public Team** and **Private Team** selection cards on the Access tab. This change applies to all teams on all deployments regardless of ABAC. The cards are functionally equivalent to the old checkbox — Public Team is the same as having the checkbox enabled, Private Team is the same as having it disabled.

Why is the Team Membership tab not visible in Team Settings?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tab requires all of the following:

- **Enable Attribute-Based Access Control** is ON in System Console > System Attributes > Attribute-Based Access.
- The ``TeamMembershipAccessControl`` feature flag is ON.
- The user has the ``manage_team_access_rules`` permission (Team Admin or System Admin).

If all three conditions are met but the tab is still missing, confirm the feature flag is actually enabled by checking **System Console > Environment > Feature Flags** or the server configuration.

Why are private ABAC teams not appearing in Browse Teams for some users?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is intended behavior. When a private team has an ABAC policy and a user does not satisfy that policy, the team is completely hidden from them in Browse Teams and search results. They will not see an error or a locked entry — the team simply does not appear. Qualifying users see the team normally.

Can I use advanced CEL expressions in Team Settings?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. The Team Membership tab uses Basic Mode only — the same simple attribute editor available in Channel Settings. For rules that require nested logic, mixed ``&&`` / ``||`` operators, or grouping, a System Admin must create a system-wide parent policy using the CEL editor in the System Console.

Can a group-synced team use ABAC?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Group sync and ABAC are mutually exclusive on a per-team basis. If a team is group-constrained, assigning an ABAC policy returns an error. You must remove the group sync configuration before applying an ABAC policy, or vice versa.

How quickly are membership changes applied?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Saving rules in Team Settings or the System Console triggers an immediate team sync — **including when auto-add is off**, because enforcement (removal on private teams) runs regardless of the auto-add setting. Changes are applied as soon as the sync completes. An automatic sync also runs every 30 minutes to process attribute changes from LDAP or SAML.

Does System Admin role bypass team ABAC enforcement?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. All roles — including System Admin — are subject to team ABAC policy evaluation. A System Admin who does not satisfy a private team's policy cannot join that team as a member through the standard UI, though they can still access the team's configuration in the System Console and make changes.

What happens when I switch a team from public to private while a policy is assigned?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If team ABAC is enabled (both flags on) and a policy is assigned to the team, clicking **Private Team** opens a confirmation modal — **"Switch to Private Team?"** — showing how many current members do not meet the policy criteria. Confirming the switch saves the change and triggers an immediate sync to enforce strict mode. Members who don't qualify are removed at that sync.

If no policy is assigned, the switch saves directly with no confirmation.

What happens when I switch a team from private to public while a policy is assigned?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Switching from Private to Public always saves directly with no confirmation modal. The team immediately transitions to advisory mode: existing members (including non-qualifying ones) are retained, and no removals occur. The policy continues to drive the Recommended tag and optional auto-add for qualifying users.

Can I add a non-qualifying user to a private ABAC team?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. The enforcement gate applies to all add paths: the Invite People modal (non-qualifying users are filtered from search results entirely), the Add Members admin flow (inline denial per user), and direct API calls. The error message is generic and does not expose policy names or attribute details. Qualifying users in the same batch request are still added — a denial for one user does not abort the rest.

How does ABAC interact with email-domain restrictions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Email-domain restrictions (configured on the Access tab) and ABAC rules (Team Membership tab) apply independently. A user must satisfy both to join the team. If both are configured and they conflict — for example, an email-domain rule and an attribute rule that together make the team unreachable — no warning is shown at configuration time. Review both settings together when debugging unexpected access denials.

Why does saving rules trigger a sync even when auto-add is off?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Auto-add controls only the **add pass** (whether sync adds qualifying non-members). The **enforcement pass** (removing non-qualifying members from private teams) runs whenever rules exist, regardless of auto-add. This ensures that newly saved or changed rules take effect immediately rather than waiting up to 30 minutes for the next scheduled sync.
