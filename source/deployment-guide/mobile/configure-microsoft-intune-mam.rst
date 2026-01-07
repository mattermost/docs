Configure Microsoft Intune Mobile Application Management (MAM)
==============================================================

.. include:: ../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

You can configure the Mattermost Mobile App to enforce Microsoft Intune App Protection Policies (MAM) on iOS devices so organizational data remains protected on Bring Your Own Device (BYOD) and mixed-use devices without requiring device enrollment (MDM). This guide provides the required configuration to activate Intune MAM successfully on iOS.

Getting Started
---------------

This configuration spans identity, mobile enforcement, and licensing systems. The guide is intentionally explicit to prevent misconfiguration and destructive enrollment failures. It's organized to help you validate fit first, then configure Intune MAM correctly.

* Initial sections help you determine whether Intune MAM is compatible with your deployment.
* `Identity <#identity-configuration-for-intune-mam>`__ sections explain the required identity model and enforcement behavior.
* Configuration sections provide a prescriptive order of operations.
* `Validation <#validation-checklist>`__ and `Troubleshooting <#troubleshooting>`__ describe expected runtime behavior and failure modes.

When Not to Use This Guide
---------------------------

If any of the following apply, stop. This configuration will fail.

* You need Intune MAM support on Android devices (not yet available).
* You want Intune MAM enforcement for a sign-in method that isn’t backed by Microsoft Entra ID (Azure AD).
* The sign-in method you select for Intune MAM enforcement can't resolve users to Azure AD ``objectId`` as the authoritative user identifier.
* You require a rollout model where users can defer, bypass, or opt out of Intune MAM enrollment for the sign-in method you’re protecting.

This guidance applies only to the authentication provider you select for Intune MAM enforcement. Other authentication methods, including guest sign-in, can still be enabled and used separately.

Before You Continue
-------------------

Before proceeding, confirm the following are true:

* You use Microsoft Entra ID for authentication.
* You can commit to Azure AD ``objectId`` as the authoritative identity.
* You have (or can obtain) a Mattermost Enterprise Advanced license.
* Target users are licensed for Microsoft Intune.
* You can register applications and grant admin consent in Microsoft Entra.
* If using SAML for Intune MAM enforcement, users must already exist in Mattermost before they can complete mobile sign-in. Mobile sign-in doesn’t create users for SAML, so unprovisioned users must first sign in on web or desktop (or be provisioned) before using mobile.

If any of the above are not true, Intune MAM enrollment may fail or users may be unable to sign in on mobile until the prerequisite is met.

.. note::

  In this guide, OpenID Connect (OIDC) refers to the Microsoft Entra sign-in method used by the Mattermost Mobile App via MSAL.

Configuration Overview
----------------------

Configuring Intune MAM for the Mattermost Mobile App requires coordinated setup across the following 4 systems:

* **Microsoft Entra ID (Azure AD)** – identity, app registration, API permissions
* **Microsoft Intune** – app protection policies and user targeting
* **Mattermost Server** – MAM enablement and identity alignment
* **Mattermost Mobile App (iOS)** – enrollment and enforcement

If any system is misconfigured, Intune MAM enrollment will fail.

Before beginning configuration, review the `Identity Configuration <#identity-configuration-for-intune-mam>`__ section to confirm your deployment meets the required identity model.

Setup Order
~~~~~~~~~~~

.. important::

  Intune MAM enforcement is evaluated only for the authentication provider selected in **System Console > Environment > Mobile Security**. Before you enable Intune MAM, confirm all of the following for the selected provider:

  * Mattermost resolves user identity to Azure AD objectId (``IdAttribute`` = ``objectId``).
  * MSAL access tokens include the ``oid`` claim.
  * Required Intune MAM API permissions have tenant-wide admin consent.

Follow this setup order exactly to avoid enrollment failures and rework.

Step 1: Confirm Identity Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Step 1 validates that the selected authentication provider can resolve users to Azure AD objectId and that MSAL access tokens include the required oid claim.

* Commit to Azure AD ``objectId`` as the authoritative identity.
* Ensure the authentication provider selected for Intune MAM enforcement (OIDC or SAML) is backed by Microsoft Entra ID and resolves users to Azure AD ``objectId``.
* If LDAP is used to provision those users, LDAP must also resolve the same Azure AD ``objectId``.
* Plan to validate that MSAL access tokens include the ``oid`` claim after completing Step 2 (Microsoft Entra configuration).

These conditions are enforced through Microsoft Entra configuration. If they are not met, Intune MAM enrollment will fail even if all other steps are completed correctly.

Step 2: Configure Microsoft Entra for Mattermost Mobile Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Step 2 creates the Microsoft Entra application Mattermost uses to validate MSAL access tokens and enable Intune MAM enrollment.

1. In the Microsoft Entra admin center, go to **Identity > Applications > App registrations**.
2. Select **New registration**, and enter:

   - **Name**: Mattermost Mobile (Intune MAM)
   - **Supported account types**: Accounts in this organizational directory only (Single tenant)

3. Select **Register**.

4. After registration, copy these values for later use in Mattermost:

   - **Application (client) ID**
   - **Directory (tenant) ID**

5. Configure token version:

   a. In the app registration, go to **Manifest**.
   b. Set ``accessTokenAcceptedVersion`` to ``2``.
   c. Select **Save**.

6. Add required API permissions:

   a. Go to **API permissions**.
   b. Select **Add a permission**.
   c. Add the required Intune MAM permissions for enrollment (including
      ``https://msmamservice.api.application/.default`` and **Microsoft Mobile Application Management**).
   d. Select **Grant admin consent** for the tenant.

7. Confirm access tokens include the ``oid`` claim.

   MSAL v2 access tokens issued by Entra include the ``oid`` claim by default. If your token does not include ``oid``, confirm you are using v2 access tokens and that the Mattermost ``IdAttribute`` is set to ``objectId``.

Step 3: Configure Mattermost Server for Intune MAM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Step 3 configures Mattermost to enable Intune MAM enforcement for the selected authentication provider.

.. image:: ../../images/intune-mam-system-console.png
  :alt: Mattermost System Console > Environment > Mobile Security showing Enable Microsoft Intune MAM, Auth Provider, Tenant ID, and Application (Client) ID fields.

1. Go to **System Console > Environment > Mobile Security**.
2. Set **Enable Microsoft Intune MAM** to **True**.
3. Under **Auth Provider**, select one of the following:

  * **OpenID Connect** (Microsoft Entra-backed)
  * **SAML 2.0** (backed by Microsoft Entra)

4. Enter the following values from your Microsoft Entra application:

  * **Tenant ID** (Directory ID)
  * **Application (Client) ID**

5. Save your changes.

.. important::

  Intune MAM requires Mattermost to resolve users by Azure AD ``objectId`` (``IdAttribute`` = ``objectId``). This value is configured in your authentication provider settings (OIDC or SAML), not in **System Console > Environment > Mobile Security**. If ``IdAttribute`` isn't set correctly, enrollment fails even if the System Console configuration is correct.

Step 4: Configure Intune App Protection Policies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Step 4 creates and assigns an Intune iOS App Protection Policy for the Mattermost app bundle ID so app protection controls are enforced for targeted users.

1. In the **Microsoft Intune admin center**, go to **Apps > App protection policies**.
2. Select **Create policy**, then configure:

   - **Platform**: iOS/iPadOS
   - **Targeted app**: Managed apps

3. Under **Apps**, add the Mattermost iOS app by bundle ID:

   - **Mattermost Mobile (Production)**: ``com.mattermost.rn``
   - **Mattermost Mobile Beta**: ``com.mattermost.rnbeta``

   .. note::

      You must create separate App Protection Policies for Production and Beta. Policies applied to one bundle ID do not apply to the other.

4. Configure the protection settings your organization requires (for example, PIN requirements, data transfer restrictions, and screen capture controls). For a complete list of available App Protection Policy controls and recommended configurations, see Microsoft documentation for Intune app protection policies.
5. Assign the policy to users using Microsoft Entra ID groups.
6. Save the policy.

.. note::

  Intune App Protection Policies are assigned using Microsoft Entra ID groups, not Mattermost teams, channels, or roles.

Step 5: Validate Using the Mobile App
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Step 5 validates end-to-end enrollment and enforcement.

* Ensure test users are assigned in Intune and properly licensed. We recommend performing your first validation login using a Microsoft Entra administrator account that can grant tenant-wide admin consent.
* Test enrollment from an iOS device.
* Confirm enforcement behaviors, including mid-session enforcement behavior.

If enrollment doesn't complete as expected, see the `Troubleshooting <#troubleshooting>`__ section for guidance.

Identity Configuration for Intune MAM
--------------------------------------

This section defines the identity requirements, constraints, and runtime behavior for the authentication method selected for Microsoft Intune MAM enforcement.

.. important::

  - Mattermost can support multiple authentication methods at the same time. Intune MAM enforcement applies only to the authentication method selected in the Intune MAM configuration in the Mattermost System Console. That authentication method must resolve users by Azure AD ``objectId``. Other authentication methods are not evaluated by Intune MAM.
  - Intune MAM enforcement is identity-based and policy-driven. Mattermost roles and permissions don't affect whether Intune MAM is required or which protections apply.

All identity prerequisites for the authentication method selected for Intune MAM enforcement must be met before enabling Intune MAM or enrolling users.

Required Identity Model
~~~~~~~~~~~~~~~~~~~~~~~~

Microsoft Intune MAM for Mattermost requires Azure AD ``objectId`` as the authoritative user identifier.

* No alternative identifiers are supported.
* If identity is misconfigured, Intune MAM enrollment will fail, even if all other configuration steps are correct.
* There is no fallback or partial enforcement mode.
* This requirement applies regardless of authentication method.

Identity Consistency Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Azure AD ``objectId`` must be resolved consistently across all sign-in paths used by the authentication method selected for Intune MAM, including any of the following that apply to that authentication method and user population:

* Mobile (OIDC via MSAL)
* Web (SAML), if the same IdP is used
* LDAP sync (if you use LDAP to provision those users)

``IdAttribute`` is the Mattermost Server configuration that specifies which user attribute contains the Azure AD ``objectId``.

The following rules apply:

* ``IdAttribute`` must equal Azure AD ``objectId``.
* MSAL access tokens must include the ``oid`` claim.
* Any mobile, web, or directory sign-in flows used by the authentication method selected for Intune MAM must resolve to the same Azure AD ``objectId``.

If any authentication path resolves a different identifier, enrollment will fail.

Supported Identity Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only the identity attributes listed below are supported for Intune MAM.

+-------------------+------------------+------------------------------+
| Attribute         | Supported        | Result                       |
+===================+==================+==============================+
| objectId          | Required         | Works                        |
+-------------------+------------------+------------------------------+
| email             | Not supported    | Enrollment fails             |
+-------------------+------------------+------------------------------+
| preferred_username| Not supported    | Identity mismatch            |
+-------------------+------------------+------------------------------+
| objectGUID        | Not supported    | Breaks mobile authentication |
+-------------------+------------------+------------------------------+
| Custom attributes | Not supported    | Unsupported by Intune        |
+-------------------+------------------+------------------------------+

Attribute Synchronization and Access Enforcement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Intune MAM is enabled, some users may authenticate exclusively through the Mattermost Mobile App. If your deployment uses SAML or OIDC, note the following behavior:

* User attributes synchronize only at login.
* Changes made in the identity provider do not apply until the next login.
* Mobile-only users may not trigger attribute synchronization.

As a result, attribute-based access control (ABAC) may not apply immediately.

If proactive enforcement of attribute-based access changes is required, we recommend LDAP (including Entra ID Domain Services). This behavior affects access enforcement, not Intune MAM enrollment.

Runtime Enforcement Behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Mattermost Mobile App enforces Intune MAM requirements during active sessions, not only at login.

If Intune MAM becomes newly required due to policy, licensing, or configuration changes:

* Enrollment is triggered immediately.
* Access to sensitive content is restricted until enrollment succeeds.
* Users can't bypass enforcement.

Plan rollouts assuming enforcement can occur instantly.

Once your identity model and enforcement behavior are understood and aligned, ensure the following prerequisites are in place before beginning configuration.

Microsoft Entra Configuration for Intune MAM
--------------------------------------------

This section provides the detailed Microsoft Entra configuration required to support Mattermost Mobile App authentication and Intune MAM enforcement. Complete this section before 
`configuring the Mattermost server <#configure-mattermost-server>`__ or `Intune App Protection Policies <#configure-intune-app-protection-policies>`__.

The steps below require changes in App registrations (manifest + API permissions) and Enterprise applications (admin consent).

Entra Application Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Register an application in Microsoft Entra that will be used by the Mattermost Mobile App for authentication and Intune MAM enrollment. This Entra application is referenced by the Mattermost server when Intune MAM is enabled to validate the MSAL access token claims issued during mobile sign-in (including the required oid claim). Redirect URI configuration isn’t required for Intune MAM enforcement.

Access Token Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

The Mattermost Mobile App relies on the MSAL access token for identity resolution and Intune MAM enforcement.

The following requirements must be met:

* Access tokens must include the ``oid`` claim.
* The application must issue tokens compatible with MSAL v2.
* ``accessTokenAcceptedVersion`` must be set to ``2`` in the app manifest.

Detailed Prerequisites
----------------------

Microsoft Requirements
~~~~~~~~~~~~~~~~~~~~~~~

* A Microsoft Entra tenant (directory) where you can create an app registration for Mattermost Mobile
* Permissions in that tenant to register applications and grant tenant-wide admin consent
* Microsoft Intune App Protection Policies enabled
* Microsoft Entra–backed sign-in functions for web and mobile
* Targeted users are licensed for Microsoft Intune

.. note::

  Microsoft Entra uses both App registrations and Enterprise Applications to represent the same application. You may need access to both areas to complete registration, permission assignment, and admin consent.

Mattermost Requirements
~~~~~~~~~~~~~~~~~~~~~~~

* Mattermost Enterprise Advanced license
* An authentication method backed by Microsoft Entra is configured: OpenID Connect (OIDC) or SAML
* Intune enabled
* The authentication method selected for Intune MAM enforcement in the System Console must be backed by Microsoft Entra

User Requirements
~~~~~~~~~~~~~~~~~

* Users authenticate via Microsoft Entra
* Users exist in Mattermost

With prerequisites in place, the next sections describe how identity requirements are enforced across each authentication method and the Microsoft Entra permissions required for Intune MAM enrollment and validation.

Identity Enforcement by Authentication Method
---------------------------------------------

Only the authentication method selected for Intune MAM enforcement must meet these requirements. Apply the same identity rule consistently for that selected method.

OIDC (Mobile sign-in via MSAL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Only the access token is used.
* The ``oid`` claim is required.

SAML (Web Login)
~~~~~~~~~~~~~~~~~

* ``SamlSettings.IdAttribute`` must map to ``objectidentifier``.
* Email, UPN, and ``immutableID`` are not supported.

.. important::

  When SAML is selected as the authentication method for Intune MAM enforcement, users must already exist in Mattermost before signing in on mobile. Users who haven't yet been provisioned must first sign in using the Mattermost web or desktop application. Mobile sign-in doesn't create new users for SAML-based authentication. If a user attempts to sign in on mobile before being provisioned, the user will be prompted to sign in using web or desktop.

LDAP (Entra ID Domain Services)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Use ``msDS-aadObjectId`` as the identity attribute.
* Do not use ``objectGUID``.

With prerequisites met and identity requirements understood, proceed to the configuration steps in the next section.

Configure Mattermost Server
----------------------------

1. Go to **System Console > Environment > Mobile Security**.
2. Enable **Microsoft Intune App Protection Policies**.
3. Configure the following fields using values from the Microsoft Entra application created earlier:
   
   * **Application (Client) ID**
   * **Directory (Tenant) ID**
   * **Authentication Provider**:
     * OIDC (Microsoft Entra-backed), or
     * SAML (backed by Microsoft Entra)

4. Set ``IdAttribute`` to ``objectId``.
5. Save your changes.

.. important::

  If you select **SAML** as the authentication provider for Intune MAM enforcement, the SAML identity provider must be backed by Microsoft Entra ID. Mattermost doesn't validate whether a SAML IdP is Entra-backed. Using a non-Entra SAML identity provider with Intune MAM will result in enrollment failures.

Validation Checklist
--------------------

Before rolling out to production, validate the configuration using a test user account. This checklist validates identity alignment, which is the most common cause of Intune MAM enrollment failure. Confirm the following values match for the same user (using Entra, Mattermost logs, or directory sync data as applicable):

* Azure AD ``objectId``
* MSAL access token ``oid`` claim
* SAML ``objectidentifier`` (if applicable)
* LDAP ``msDS-aadObjectId`` (if applicable)

Any mismatch will cause Intune MAM enrollment to fail.

Deploy or Update Mattermost Mobile Apps
---------------------------------------

Install the Mattermost iOS mobile app using one of the following supported methods:

* Apple App Store (production)
* TestFlight (beta)

Other distribution methods, including Intune-wrapped apps, re-signed binaries, or private IPA deployments, aren't supported for Intune MAM enforcement and won't work.

.. note::

  - Mattermost Beta (``com.mattermost.rnbeta``) and Production (``com.mattermost.rn``) apps can share the same Microsoft Entra app registration when using an exposed API configuration. Separate app registrations are optional and only required if you intentionally isolate environments or scopes.
  - MDM device enrollment isn't required. Intune App Protection Policies are enforced at the app level and require the official Mattermost iOS app from the App Store or TestFlight.

Configure Intune App Protection Policies
----------------------------------------

1. Go to the **Microsoft Intune Admin Center**.
2. Create an iOS App Protection Policy.
3. Add the appropriate Mattermost iOS bundle ID:

  * **Mattermost Mobile (Production)**: ``com.mattermost.rn``
  * **Mattermost Mobile Beta**: ``com.mattermost.rnbeta``

4. Assign the policy using Microsoft Entra groups.

.. note::

  - You must create separate Intune App Protection Policies for each Mattermost iOS app you deploy. Policies applied to one bundle ID do not apply to the other.
  - Intune App Protection Policies are assigned using Microsoft Entra groups, not Mattermost teams, channels, or roles.

Expected Mobile Login & Enrollment Flow
---------------------------------------

When Intune MAM is enabled:

1. The mobile app checks:
   * Platform is iOS
   * Intune MAM is enabled
   * Authentication service matches
   * License is **Enterprise Advanced**

2. The user taps **Sign in**.
3. MSAL authenticates the user.
4. Mattermost validates the access token.
5. Intune MAM enrollment is triggered.
6. App protection policies are applied.

Troubleshooting
---------------

Most Intune MAM enrollment failures are caused by:

* Incorrect ``IdAttribute``
* Missing Microsoft Entra API permissions
* Access token missing the ``oid`` claim
* The authentication method selected for Intune MAM resolves a different identifier than expected (not Azure AD ``objectId``)
* Android device usage

Always fix identity alignment first.

Intune MAM Errors
~~~~~~~~~~~~~~~~~~

The errors below may occur during mobile sign-in or when Intune MAM enforcement is triggered mid-session. Some errors are shown in the Mattermost Mobile App, while others are silent and must be diagnosed using the Mattermost server logs.

.. raw:: html

  <style>
    /* Base table layout */
    .mm-intune-errors {
      width: 100%;
      border-collapse: collapse;
      table-layout: fixed;
      margin: 0.75rem 0 1rem 0;
      font-size: 0.95rem;
      line-height: 1.35;
    }

    .mm-intune-errors th,
    .mm-intune-errors td {
      padding: 0.6rem 0.7rem;
      vertical-align: top;
      overflow-wrap: anywhere;
      word-break: break-word;
      white-space: normal;
      border: 1px solid rgba(0, 0, 0, 0.12);
      background: transparent;
      color: inherit;
    }

    .mm-intune-errors th {
      font-weight: 600;
      text-align: left;
      background: rgba(0, 0, 0, 0.04);
    }

    .mm-intune-errors code {
      font-size: 0.9em;
      white-space: normal;
      padding: 0.1em 0.25em;
      border-radius: 4px;
      background: rgba(0, 0, 0, 0.06);
    }

    .mm-intune-errors .meta {
      opacity: 0.85;
      font-size: 0.92em;
      margin-top: 0.35rem;
    }

    .mm-intune-errors ul {
      margin: 0.35rem 0 0 1.1rem;
      padding: 0;
    }

    .mm-intune-errors li {
      margin: 0.2rem 0;
    }

    .mm-intune-errors .label {
      font-weight: 600;
    }

    /* Dark mode overrides */
    @media (prefers-color-scheme: dark) {
      .mm-intune-errors th,
      .mm-intune-errors td {
        border-color: rgba(255, 255, 255, 0.18);
      }

      .mm-intune-errors th {
        background: rgba(255, 255, 255, 0.06);
      }

      .mm-intune-errors code {
        background: rgba(255, 255, 255, 0.10);
      }

      .mm-intune-errors .meta {
        opacity: 0.9;
      }
    }
  </style>

  <table class="mm-intune-errors" aria-label="Microsoft Intune MAM errors and admin remediation steps">
    <thead>
      <tr>
        <th style="width: 26%;">Error</th>
        <th style="width: 20%;">Meaning</th>
        <th style="width: 54%;">Admin cause &amp; next step</th>
      </tr>
    </thead>
    <tbody>

      <!-- Enrollment Failed -->
      <tr>
        <td>
          <strong>Enrollment Failed</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>(varies)</code><br/>
            <span class="label">Retry:</span> No<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          Intune MAM enrollment failed due to a technical error.
        </td>
        <td>
          <span class="label">Cause:</span> Enrollment could not be completed due to a technical failure (MSAL error, Intune enrollment API failure, identity mismatch, or missing Entra permissions).
          <ul>
            <li><span class="label">Behavior:</span> The server is removed immediately and there is no retry option.</li>
            <li><span class="label">Next step:</span> Fix the underlying issue, then have the user re-add the server in the mobile app.</li>
            <li><span class="label">Admin checks:</span> Verify <code>IdAttribute = objectId</code>, token includes <code>oid</code>, tenant-wide admin consent is granted, and Intune App Protection Policy targets the user and app bundle ID.</li>
          </ul>
        </td>
      </tr>

      <!-- Enrollment Declined -->
      <tr>
        <td>
          <strong>Enrollment Declined</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>(varies)</code><br/>
            <span class="label">Retry:</span> Yes<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          User declined Intune MAM enrollment.
        </td>
        <td>
          <span class="label">Cause:</span> The user canceled the enrollment prompt.
          <ul>
            <li><span class="label">Behavior:</span> A <strong>Retry</strong> option is shown.</li>
            <li><span class="label">Next step:</span> Instruct the user to retry enrollment when ready.</li>
            <li><span class="label">Admin note:</span> No server data is removed unless a later technical enrollment failure occurs.</li>
          </ul>
        </td>
      </tr>

      <!-- Enterprise not compiled -->
      <tr>
        <td>
          <strong>(silent)</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>api.user.login_by_intune.not_available.app_error</code><br/>
            <span class="label">HTTP:</span> 501<br/>
            <span class="label">Retry:</span> No<br/>
            <span class="label">Fallback:</span> Web SSO
          </div>
        </td>
        <td>
          Intune MAM login is not available on this server.
        </td>
        <td>
          <span class="label">Cause:</span> The server does not support Intune MAM (feature not available in this build or not enabled for the deployment).
          <ul>
            <li><span class="label">Next step:</span> Confirm the server version/build includes Intune MAM support and that the deployment is licensed for Enterprise Advanced.</li>
            <li><span class="label">User guidance:</span> Have the user sign in via web/desktop while the server is updated or configuration is corrected.</li>
          </ul>
        </td>
      </tr>

      <!-- Intune not configured -->
      <tr>
        <td>
          <strong>(silent)</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>api.user.login_by_intune.not_configured.app_error</code><br/>
            <span class="label">HTTP:</span> 400<br/>
            <span class="label">Retry:</span> No<br/>
            <span class="label">Fallback:</span> Web SSO
          </div>
        </td>
        <td>
          Intune MAM is enabled for the org but not configured on the server.
        </td>
        <td>
          <span class="label">Cause:</span> Intune MAM is not fully configured in <strong>System Console &gt; Environment &gt; Mobile Security</strong>.
          <ul>
            <li><span class="label">Next step:</span> Enable Microsoft Intune MAM and ensure <strong>Tenant ID</strong>, <strong>Application (Client) ID</strong>, and <strong>Auth Provider</strong> are set correctly.</li>
            <li><span class="label">Admin checks:</span> Confirm the selected auth provider is Entra-backed and that required permissions/admin consent have been granted for the Entra app registration.</li>
            <li><span class="label">User guidance:</span> Have the user sign in via web/desktop while configuration is completed.</li>
          </ul>
        </td>
      </tr>

      <!-- Bot login forbidden -->
      <tr>
        <td>
          <strong>Bot accounts cannot sign in using this method.</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>api.user.login_by_intune.bot_login_forbidden.app_error</code><br/>
            <span class="label">HTTP:</span> 403<br/>
            <span class="label">Retry:</span> No<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          The account cannot use Intune MAM sign-in.
        </td>
        <td>
          <span class="label">Cause:</span> Bot accounts are not allowed to authenticate via Intune MAM.
          <ul>
            <li><span class="label">Next step:</span> Use a human user account for Intune MAM enrollment and access.</li>
          </ul>
        </td>
      </tr>

      <!-- Account locked/deactivated -->
      <tr>
        <td>
          <strong>Your account has been deactivated. Please contact your administrator.</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>api.user.login_by_intune.account_locked.app_error</code><br/>
            <span class="label">HTTP:</span> 409<br/>
            <span class="label">Retry:</span> No<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          The account is not permitted to sign in.
        </td>
        <td>
          <span class="label">Cause:</span> The user is deleted, disabled, or locked in Mattermost.
          <ul>
            <li><span class="label">Next step:</span> Re-enable or restore the user account in Mattermost, then retry sign-in and enrollment.</li>
          </ul>
        </td>
      </tr>

      <!-- IsConfigured() false -->
      <tr>
        <td>
          <strong>(silent)</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>ent.intune.login.not_configured.app_error</code><br/>
            <span class="label">HTTP:</span> 403<br/>
            <span class="label">Retry:</span> No<br/>
            <span class="label">Fallback:</span> Web SSO
          </div>
        </td>
        <td>
          Intune MAM is not configured for the current sign-in path.
        </td>
        <td>
          <span class="label">Cause:</span> Intune MAM is not configured for the requested authentication path (configuration incomplete or mismatched provider selection).
          <ul>
            <li><span class="label">Next step:</span> Confirm Intune MAM is enabled and configured, and that the selected <strong>Auth Provider</strong> matches how users authenticate (OIDC vs SAML).</li>
            <li><span class="label">User guidance:</span> Have the user sign in via web/desktop while configuration is corrected.</li>
          </ul>
        </td>
      </tr>

      <!-- IdAttribute mapping failed -->
      <tr>
        <td>
          <strong>We couldn't complete your sign in. Please try again.</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>ent.intune.login.extract_auth_data.app_error</code><br/>
            <span class="label">HTTP:</span> 400<br/>
            <span class="label">Retry:</span> Yes (1x)<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          Identity mapping failed during sign-in.
        </td>
        <td>
          <span class="label">Cause:</span> The server could not extract or map the identity attribute required for Intune MAM (commonly <code>IdAttribute</code> misconfigured or required claim missing).
          <ul>
            <li><span class="label">Next step:</span> Ensure <code>IdAttribute</code> is set to <code>objectId</code> and the access token includes the <code>oid</code> claim.</li>
            <li><span class="label">Admin checks:</span> Verify the Entra app registration is configured to issue v2 tokens and includes <code>accessTokenAcceptedVersion = 2</code>.</li>
          </ul>
        </td>
      </tr>

      <!-- SAML user not found -->
      <tr>
        <td>
          <strong>Your account isn't fully set up yet. Please sign in to Mattermost via the web or desktop app first.</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>ent.intune.login.account_not_found.app_error</code><br/>
            <span class="label">HTTP:</span> 428<br/>
            <span class="label">Retry:</span> No<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          The user does not exist in Mattermost for SAML-based sign-in.
        </td>
        <td>
          <span class="label">Cause:</span> When SAML is the selected provider for Intune MAM enforcement, mobile sign-in cannot create a new user.
          <ul>
            <li><span class="label">Next step:</span> Have the user sign in once via the web or desktop app to create/provision the account, then retry mobile sign-in.</li>
            <li><span class="label">Admin checks:</span> Ensure provisioning is in place (SAML JIT via web/desktop, LDAP sync, or another provisioning method).</li>
          </ul>
        </td>
      </tr>

      <!-- Token validation failed -->
      <tr>
        <td>
          <strong>We couldn't verify your sign in. Please try again.</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>ent.intune.validate_token.invalid_token.app_error</code><br/>
            <span class="label">HTTP:</span> 400<br/>
            <span class="label">Retry:</span> Yes (1x)<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          The access token could not be validated.
        </td>
        <td>
          <span class="label">Cause:</span> Token validation failed (token malformed, wrong issuer/audience, missing permissions, or Entra configuration mismatch).
          <ul>
            <li><span class="label">Next step:</span> Verify the configured <strong>Tenant ID</strong> and <strong>Application (Client) ID</strong> match the Entra app that issued the token.</li>
            <li><span class="label">Admin checks:</span> Confirm required Intune MAM permissions are present and tenant-wide admin consent is granted; confirm token is MSAL v2 and includes <code>oid</code>.</li>
          </ul>
        </td>
      </tr>

      <!-- Token expired -->
      <tr>
        <td>
          <strong>Your sign in session has expired. Please try signing in again.</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>ent.intune.validate_token.token_expired.app_error</code><br/>
            <span class="label">HTTP:</span> 400<br/>
            <span class="label">Retry:</span> Yes (1x)<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          The authentication session expired before enrollment completed.
        </td>
        <td>
          <span class="label">Cause:</span> The access token or interactive session expired during sign-in/enrollment.
          <ul>
            <li><span class="label">Next step:</span> Have the user sign in again and complete enrollment promptly.</li>
            <li><span class="label">Admin checks:</span> If repeated, validate the device has network access to Entra/Intune endpoints and that enrollment prompts are not being blocked.</li>
          </ul>
        </td>
      </tr>

      <!-- Missing claims -->
      <tr>
        <td>
          <strong>We couldn't complete your sign in. Please contact your IT administrator.</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>ent.intune.validate_token.missing_claims.app_error</code><br/>
            <span class="label">HTTP:</span> 400<br/>
            <span class="label">Retry:</span> No<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          The access token is missing required identity claims.
        </td>
        <td>
          <span class="label">Cause:</span> Required claims are missing from the access token (most commonly <code>oid</code>).
          <ul>
            <li><span class="label">Next step:</span> Ensure the Entra app is configured to issue MSAL v2 access tokens and includes the required claims.</li>
            <li><span class="label">Admin checks:</span> Confirm <code>accessTokenAcceptedVersion = 2</code> in the app manifest and that the selected identity model uses <code>objectId</code>.</li>
          </ul>
        </td>
      </tr>

      <!-- Invalid tenant -->
      <tr>
        <td>
          <strong>There was a configuration issue. Please contact your IT administrator.</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>ent.intune.validate_token.invalid_tenant_id.app_error</code><br/>
            <span class="label">HTTP:</span> 400<br/>
            <span class="label">Retry:</span> No<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          The token tenant does not match the configured tenant.
        </td>
        <td>
          <span class="label">Cause:</span> The token was issued by a different tenant than the one configured in Mattermost (tenant mismatch).
          <ul>
            <li><span class="label">Next step:</span> Verify the <strong>Tenant ID</strong> configured in the System Console matches the Entra tenant issuing MSAL tokens for Mattermost Mobile.</li>
            <li><span class="label">Admin checks:</span> Confirm the user is authenticating against the expected tenant and that the mobile configuration points to the correct environment.</li>
          </ul>
        </td>
      </tr>

      <!-- AADSTS650057 -->
      <tr>
        <td>
          <strong>AADSTS650057</strong><br/>
          <span class="meta">(invalid_resource)</span>
          <div class="meta">
            <span class="label">Error ID:</span> <code>(AADSTS650057)</code><br/>
            <span class="label">Retry:</span> No (until fixed)<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          Required Intune MAM API permission is missing.
        </td>
        <td>
          <span class="label">Cause:</span> Required Intune MAM API permissions are missing or do not have tenant-wide admin consent.
          <ul>
            <li><span class="label">Next step:</span> Add and grant admin consent for <code>https://msmamservice.api.application/.default</code> and <code>Microsoft Mobile Application Management → user_impersonation</code> (Delegated), as required.</li>
            <li><span class="label">Admin checks:</span> Confirm admin consent was granted under the Enterprise application (service principal), then have the user retry sign-in.</li>
          </ul>
        </td>
      </tr>

      <!-- NotLicensed -->
      <tr>
        <td>
          <strong>NotLicensed</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>(NotLicensed)</code><br/>
            <span class="label">Retry:</span> No<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          The server is not licensed for Intune MAM enforcement.
        </td>
        <td>
          <span class="label">Cause:</span> Enterprise Advanced licensing is missing or not applied to the server.
          <ul>
            <li><span class="label">Next step:</span> Apply an Enterprise Advanced license to the server and confirm the license is active.</li>
          </ul>
        </td>
      </tr>

      <!-- HTTP 403 Forbidden -->
      <tr>
        <td>
          <strong>HTTP 403 Forbidden</strong>
          <div class="meta">
            <span class="label">Error ID:</span> <code>(HTTP 403)</code><br/>
            <span class="label">Retry:</span> No<br/>
            <span class="label">Fallback:</span> None
          </div>
        </td>
        <td>
          Server-side access is blocked.
        </td>
        <td>
          <span class="label">Cause:</span> A server gating condition is preventing enrollment (not an Intune service failure).
          <ul>
            <li><span class="label">Next step:</span> Verify Enterprise Advanced licensing, Intune MAM is enabled, Tenant ID and Client ID are valid, auth provider is configured, admin consent is granted, and <code>IntuneScope</code> is set.</li>
            <li><span class="label">Admin checks:</span> Confirm the selected auth provider matches the enforcement configuration, and confirm Intune App Protection Policy assignment for the user and app bundle ID.</li>
          </ul>
        </td>
      </tr>

    </tbody>
  </table>

Enrollment Failure Session Behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If Intune MAM enrollment fails due to a **technical error**, the following occurs:

* The user is logged out of the affected Mattermost server.
* The server is removed from the Mattermost Mobile App.
* All cached data for that server is wiped from the device.

If a user has multiple Mattermost servers configured in the app, **only the failing server is removed**. Other servers remain accessible and unaffected.

If the user **declines enrollment**, retry is allowed and no server data is removed unless enrollment later fails due to a technical error.

Consent Required During First Login
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some cases, a user’s first mobile sign-in may succeed, but Intune MAM enrollment doesn't complete. Authentication can succeed even when required Intune MAM permissions are missing, which can make this issue non-obvious during initial rollout or testing.

This issue occurs when required Microsoft Entra permissions for Intune MAM haven't yet been granted with tenant-wide admin consent. This issue is most commonly encountered during initial rollout or testing, before admin consent has been granted for the tenant.

If users are prompted for Microsoft Entra consent during first login, this is expected behavior when tenant-wide admin consent hasn't yet been granted. A Microsoft Entra administrator with permission to grant tenant-wide admin consent must approve the request on behalf of the organization before Intune MAM enrollment can complete. 

Verify that the following permissions have been granted with admin consent in Microsoft Entra:

* Microsoft Mobile Application Management → ``user_impersonation`` (Delegated)
* ``https://msmamservice.api.application/.default``

If admin consent is missing, Intune MAM enrollment can't complete, even if authentication succeeds.

To resolve this:

1. Go to **Microsoft Entra Admin Center > Enterprise applications**.
2. Locate the Mattermost Mobile enterprise application (service principal).
3. Grant **tenant-wide admin consent** for all required Intune MAM permissions.
4. Have the affected user **retry mobile sign-in**.

Once admin consent is granted, enrollment should complete successfully on retry.