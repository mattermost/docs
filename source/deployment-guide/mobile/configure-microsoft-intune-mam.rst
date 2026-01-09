Configure Microsoft Intune Mobile Application Management (MAM)
==============================================================

.. include:: ../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

You can configure the Mattermost Mobile App on iOS to enforce Microsoft Intune App Protection Policies (MAM) so organizational data remains protected on Bring Your Own Device (BYOD) and mixed-use devices without requiring device enrollment (MDM).

This guide documents the required configuration to enable Intune MAM successfully on iOS. 

Read This First
----------------

Intune MAM enforcement in Mattermost is identity-based for the enforced sign-in method.

* The enforced authentication provider must resolve users using Azure AD ``objectId`` (``IdAttribute = objectId``).
* MSAL access tokens must include the ``oid`` claim, and it must match the same Azure AD ``objectId`` (confirm identity alignment: ``objectId ↔ oid``).

.. important::

  If Intune MAM enrollment fails due to a technical error, the affected Mattermost server is removed from the mobile app and cached data for that server is wiped from the device.

Unsupported Scenarios
---------------------

This guide doesn't apply when:

* You require Intune MAM on Android devices.
* You want Intune MAM enforcement for a sign-in method not backed by Microsoft Entra ID.
* The enforced authentication provider cannot resolve users to Azure AD ``objectId``.
* You require a rollout model where users can bypass or defer Intune MAM for the enforced sign-in method.

Other authentication methods, such as guest access, may still be enabled separately, but they aren't evaluated by Intune MAM.

Prerequisites
-------------

Confirm the following before continuing:

* Microsoft Entra ID is used for authentication.
* You can commit to Azure AD ``objectId`` as the authoritative identity.
* Mattermost Enterprise Advanced licensing is available for the server.
* Target users are licensed for Microsoft Intune.
* You can register applications and grant tenant-wide admin consent in Microsoft Entra.
* If enforcing Intune MAM on SAML, users already exist in Mattermost (mobile sign-in does not create users for SAML).

.. note::

  In this guide, OpenID Connect (OIDC) refers to the Microsoft Entra sign-in method used by the Mattermost Mobile App via MSAL.

Configuration Overview
----------------------

Successful Intune MAM enforcement requires coordinated configuration across:

* **Microsoft Entra ID** – app registration, scope, API permissions, admin consent
* **Microsoft Intune** – iOS App Protection Policies
* **Mattermost Server** – MAM enablement and provider selection
* **Mattermost Mobile App (iOS)** – enrollment and enforcement

Complete the steps below in order.

Setup Summary
-------------

1. Confirm identity requirements and alignment (``objectId ↔ oid``).
2. Configure Microsoft Entra (server-referenced application).
3. Enable Intune MAM in Mattermost and select the enforced provider.
4. Deploy the official Mattermost iOS app.
5. Configure Intune App Protection Policies.
6. Validate enrollment and enforcement.

Values You’ll Need Later
------------------------

Capture these during setup:

+-------------------------------+-----------------------------------------+---------------------------------------------------------------+
| Value                         | Where to get it                         | Where you use it                                              |
+===============================+=========================================+===============================================================+
| Directory (tenant) ID         | Entra app registration overview         | Mattermost System Console                                     |
+-------------------------------+-----------------------------------------+---------------------------------------------------------------+
| Application (client) ID       | Entra app registration overview         | Mattermost System Console                                     |
+-------------------------------+-----------------------------------------+---------------------------------------------------------------+
| Application ID URI            | Entra app > Expose an API               | Used to form the ``api://<APPLICATION-ID>/login.mattermost``  |
|                               |                                         | scope reference in Authorized client applications             |
+-------------------------------+-----------------------------------------+---------------------------------------------------------------+
| ``login.mattermost`` scope    | Entra app > Expose an API               | Authorized client applications                                |
+-------------------------------+-----------------------------------------+---------------------------------------------------------------+
| Mobile client application ID  | Provided by Mattermost                  | Entra app > Authorized client applications                    |
+-------------------------------+-----------------------------------------+---------------------------------------------------------------+
| iOS bundle IDs (prod/beta)    | This guide                              | Intune App Protection Policies                                |
+-------------------------------+-----------------------------------------+---------------------------------------------------------------+

Step 1: Identity Configuration for Intune MAM
---------------------------------------------

.. _step-1-identity-configuration-for-intune-mam:

This step defines the required identity model for the authentication provider selected for Intune MAM enforcement.

Required Identity Model
~~~~~~~~~~~~~~~~~~~~~~~~

Microsoft Intune MAM for Mattermost requires Azure AD ``objectId`` as the authoritative user identifier. The following is non-negotiable.

* ``IdAttribute`` must equal ``objectId`` for the enforced provider.
* MSAL access tokens must include the ``oid`` claim.
* Confirm identity alignment (``objectId ↔ oid``) before enabling Intune MAM.

Confirm Identity Alignment (objectId ↔ oid)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _identity-alignment-objectid-oid:

For the same user, the following values must match:

* Azure AD ``objectId``
* MSAL access token ``oid`` claim
* SAML ``objectidentifier`` (if applicable)
* LDAP ``msDS-aadObjectId`` (if applicable)

Any mismatch prevents enrollment.

Identity Enforcement by Authentication Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**OIDC (Mobile sign-in via MSAL)**

* Mattermost uses the MSAL access token for identity and enrollment.
* Confirm identity alignment (``objectId ↔ oid``).

**SAML (Entra-backed)**

* ``SamlSettings.IdAttribute`` must map to ``objectidentifier``.
* Email, UPN, and ``immutableID`` aren't supported.
* Users must already exist in Mattermost before mobile sign-in.

**LDAP (Entra ID Domain Services)**

* Use ``msDS-aadObjectId``.
* Do not use ``objectGUID``.

Runtime Enforcement Behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Intune MAM is enabled for a provider:

* Enforcement occurs during active sessions, not only at login.
* If Intune MAM becomes newly required due to policy, licensing, or configuration changes, enrollment may be triggered immediately.
* Users can’t bypass enforcement for the enforced provider.

Pre-flight Checklist
~~~~~~~~~~~~~~~~~~~~

- Licensed Intune test user available
- Ability to grant tenant-wide admin consent
- Enforced provider identified (OIDC or SAML)
- ``IdAttribute = objectId`` configured
- Identity alignment verified (``objectId ↔ oid``)
- Official Mattermost iOS app deployed
- Target bundle IDs known: ``com.mattermost.rn`` (Production), ``com.mattermost.rnbeta`` (Beta)

Step 2: Microsoft Entra Configuration for Intune MAM
----------------------------------------------------

.. _step-2-microsoft-entra-configuration-for-intune-mam:

You register a single-tenant Microsoft Entra application that is referenced by Mattermost Server. This application validates MSAL access tokens and supports Intune MAM enrollment.

You don't register the Mattermost Mobile app itself. Redirect URI configuration isn't required.

Entra Application Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to **Identity > Applications > App registrations**
2. Select **New registration**
3. Configure:

   * **Name**: Mattermost Mobile (Intune MAM)
   * **Supported account types**: Single tenant

4. Register the app
5. Copy:

   * **Application (client) ID**
   * **Directory (tenant) ID**

Expose the API and Create the Scope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to **Expose an API**
2. Confirm **Application ID URI** is set (for example, ``api://<APPLICATION-ID>``)
3. Add a scope named ``login.mattermost``
4. Save your changes.

Authorize the Official Mobile Client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Authorize the official Mattermost Mobile client application ID (provided by Mattermost) to request the ``login.mattermost`` scope.

1. In the Entra app registration, go to **Expose an API**.
2. Under **Authorized client applications**, select **Add a client application**.
3. Add the official Mattermost Mobile client application ID (provided by Mattermost).
4. Authorize the ``api://<APPLICATION-ID>/login.mattermost`` scope.
5. Save your changes.

If the official client application ID isn't yet available, complete the remaining steps and return here once Mattermost provides it.

API Permissions and Admin Consent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _api-permissions-admin-consent:

1. Go to **API permissions**.
2. Add the required Intune MAM permissions for enrollment (minimum required):

   * ``https://msmamservice.api.application/.default``
   * Microsoft Mobile Application Management → ``user_impersonation`` (Delegated)

3. Grant **tenant-wide admin consent**.

If these permissions are missing or lack tenant-wide admin consent, enrollment can fail with an Entra permissions error (for example, ``AADSTS650057``).

Configure MSAL v2 Tokens
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the app **Manifest**.
2. Set the token version to ``2``:

   * If your manifest shows ``api.requestedAccessTokenVersion``, set it to ``2``.
   * Otherwise set ``accessTokenAcceptedVersion`` to ``2``.

3. Save your changes.

Step 3: Configure Mattermost Server for Intune MAM
--------------------------------------------------

.. _step-3-configure-mattermost-server-for-intune-mam:

1. Go to **System Console > Environment > Mobile Security**
2. Set **Enable Microsoft Intune MAM** to **True**
3. Select **Auth Provider**:

   * OpenID Connect (Entra-backed)
   * SAML 2.0 (Entra-backed)

4. Enter:

   * **Tenant ID**
   * **Application (Client) ID**

5. Save your changes.

The enforced provider must resolve identity using ``IdAttribute = objectId``.

Step 4: Deploy the Mattermost iOS App
-------------------------------------

Install the official Mattermost iOS app using:

* Apple App Store (Production)
* TestFlight (Beta)

Wrapped, re-signed, or privately distributed apps aren't supported.

Step 5: Configure Intune App Protection Policies
------------------------------------------------

1. Go to **Intune admin center > Apps > App protection policies**.
2. Create a policy:

   * **Platform**: iOS/iPadOS
   * **Targeted app**: Managed apps

3. Add the Mattermost app by bundle ID:

   * ``com.mattermost.rn`` (Production)
   * ``com.mattermost.rnbeta`` (Beta)

4. Configure protection settings.
5. Assign to Entra ID user groups.
6. Save your changes.

Separate policies are required for Production and Beta apps.

Step 6: Validate Enrollment
---------------------------

Validate with a licensed test user on iOS.

Confirm:

* Enrollment completes successfully
* Enforcement applies at sign-in and mid-session
* Identity alignment is correct (``objectId ↔ oid``)

Expected Behavior During Mobile Sign-In
---------------------------------------

1. User signs in via MSAL.
2. Mattermost validates the access token.
3. Intune MAM enrollment is triggered.
4. App Protection Policies are applied.

If enrollment is required but cannot complete, access is blocked until enrollment succeeds.

Troubleshooting
---------------

.. _troubleshooting:

Most failures are caused by:

* Identity mismatch (``objectId ↔ oid``)
* ``IdAttribute`` not set to ``objectId``
* Missing Entra API permissions or admin consent
* App Protection Policy not targeting the user or app
* Unsupported client or platform

Quick Diagnostics
~~~~~~~~~~~~~~~~~

1. Confirm identity alignment (``objectId ↔ oid``).
2. Confirm ``IdAttribute = objectId``.
3. Confirm Entra permissions and admin consent.
4. Confirm Auth Provider selection.
5. Confirm Intune policy targeting.

If the user declines enrollment, retry is allowed.

Intune MAM Errors
~~~~~~~~~~~~~~~~~

The errors below may occur during mobile sign-in or when Intune MAM enforcement is triggered mid-session. Some errors are shown in the Mattermost Mobile App, while others are silent and must be diagnosed using Mattermost server logs.

.. raw:: html

  <style>
    /* Compact, scannable 3-column table with full inline metadata and strong grid lines */
    .mm-intune-errors {
      width: 100%;
      border-collapse: collapse;
      table-layout: fixed; /* prevents horizontal scrolling */
      margin: 0.75rem 0 1rem 0;
      font-size: 0.95rem;
      line-height: 1.35;
      border: 1px solid #b3b3b3;
    }

    .mm-intune-errors th,
    .mm-intune-errors td {
      padding: 0.6rem 0.7rem;
      vertical-align: top;
      border: 1px solid #b3b3b3;
      overflow-wrap: anywhere;
      word-break: break-word;
      white-space: normal;
      background: transparent;
      color: inherit;
    }

    /* Light mode header: explicit contrast */
    .mm-intune-errors th {
      font-weight: 600;
      text-align: left;
      background-color: #f2f2f2;
      color: #111111;
    }

    /* Strong row separation */
    .mm-intune-errors tbody tr + tr td {
      border-top-width: 2px;
    }

    .mm-intune-errors code {
      font-size: 0.9em;
      white-space: normal;
      padding: 0.1em 0.25em;
      border-radius: 4px;
      background: rgba(0, 0, 0, 0.08);
    }

    .mm-intune-errors .meta {
      opacity: 0.92;
      font-size: 0.92em;
      margin-top: 0.35rem;
    }

    .mm-intune-errors .meta div {
      margin: 0.08rem 0;
    }

    .mm-intune-errors .label {
      font-weight: 600;
    }

    /* Dark mode override */
    @media (prefers-color-scheme: dark) {
      .mm-intune-errors,
      .mm-intune-errors th,
      .mm-intune-errors td {
        border-color: #666;
      }

      .mm-intune-errors th {
        background-color: #2a2a2a;
        color: #ffffff;
      }

      .mm-intune-errors code {
        background: rgba(255, 255, 255, 0.14);
      }

      .mm-intune-errors .meta {
        opacity: 0.9;
      }
    }
  </style>

  <table class="mm-intune-errors" aria-label="Microsoft Intune MAM errors and admin remediation steps">
    <thead>
      <tr>
        <th style="width: 30%;">Error</th>
        <th style="width: 22%;">Meaning</th>
        <th style="width: 48%;">Admin cause &amp; next step</th>
      </tr>
    </thead>
    <tbody>

      <!-- Enrollment Failed -->
      <tr>
        <td>
          <strong>Enrollment Failed</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>(varies)</code></div>
            <div><span class="label">HTTP:</span> <code>(varies)</code></div>
            <div><span class="label">Scenario:</span> Enrollment failed (technical)</div>
            <div><span class="label">User message:</span> "Enrollment Failed"</div>
            <div><span class="label">Retry:</span> No</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          Intune MAM enrollment failed due to a technical error.
        </td>
        <td>
          <span class="label">Cause:</span> Enrollment could not be completed due to a technical failure (MSAL error, Intune enrollment API failure, identity mismatch, or missing Entra permissions).<br/>
          <span class="label">Behavior:</span> The server is removed immediately and there is no retry option; cached data for that server is wiped.<br/>
          <span class="label">Next step:</span> Fix the underlying issue, then have the user re-add the server in the mobile app.<br/>
          <span class="label">Admin checks:</span> Verify <code>IdAttribute = objectId</code>; confirm identity alignment (<code>objectId ↔ oid</code>); confirm tenant-wide admin consent; confirm App Protection Policy targets the user and the correct iOS bundle ID.
        </td>
      </tr>

      <!-- Enrollment Declined -->
      <tr>
        <td>
          <strong>Enrollment Declined</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>(varies)</code></div>
            <div><span class="label">HTTP:</span> <code>(varies)</code></div>
            <div><span class="label">Scenario:</span> User declined enrollment</div>
            <div><span class="label">User message:</span> "Enrollment Declined"</div>
            <div><span class="label">Retry:</span> Yes</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          The user declined Intune MAM enrollment.
        </td>
        <td>
          <span class="label">Cause:</span> The user canceled the enrollment prompt.<br/>
          <span class="label">Behavior:</span> A <strong>Retry</strong> option is shown; no server data is removed unless a later technical enrollment failure occurs.<br/>
          <span class="label">Next step:</span> Instruct the user to retry enrollment when ready.
        </td>
      </tr>
      <!-- Consent Denied (admin consent missing) -->
      <tr>
        <td>
          <strong>Consent Denied</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>(varies)</code></div>
            <div><span class="label">HTTP:</span> <code>(varies)</code></div>
            <div><span class="label">Scenario:</span> Admin consent missing (first login)</div>
            <div><span class="label">User message:</span> "You denied consent for Intune management. The affected accounts have been unenrolled and signed out."</div>
            <div><span class="label">Retry:</span> Yes (after admin consent)</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          Enrollment cannot complete because required Intune MAM permissions don’t have tenant-wide admin consent.
        </td>
        <td>
          <span class="label">Cause:</span> Required Intune MAM API permissions are present or requested, but tenant-wide admin consent has not been granted for the Entra app registration configured in Mattermost.<br/>
          <span class="label">Behavior:</span> The message may appear as if the user denied consent, but the underlying issue is admin consent.<br/>
          <span class="label">Next step:</span> Grant tenant-wide admin consent for the required Intune MAM permissions on the same Entra app registration configured in Mattermost (Step 3), then have the user retry mobile sign-in.
        </td>
      </tr>
      <!-- Enterprise not compiled -->
      <tr>
        <td>
          <strong>(silent)</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>api.user.login_by_intune.not_available.app_error</code></div>
            <div><span class="label">HTTP:</span> 501</div>
            <div><span class="label">Scenario:</span> Enterprise not compiled</div>
            <div><span class="label">User message:</span> (silent)</div>
            <div><span class="label">Retry:</span> No</div>
            <div><span class="label">Fallback:</span> Web SSO</div>
          </div>
        </td>
        <td>
          Intune MAM login is not available on this server.
        </td>
        <td>
          <span class="label">Cause:</span> The server does not support Intune MAM (feature not available in this build or not enabled for the deployment).<br/>
          <span class="label">Next step:</span> Confirm the server build includes Intune MAM support and the deployment is licensed for Enterprise Advanced.<br/>
          <span class="label">User guidance:</span> Have the user sign in via web/desktop while the server is updated or configuration is corrected.
        </td>
      </tr>

      <!-- Intune not configured -->
      <tr>
        <td>
          <strong>(silent)</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>api.user.login_by_intune.not_configured.app_error</code></div>
            <div><span class="label">HTTP:</span> 400</div>
            <div><span class="label">Scenario:</span> Intune not configured</div>
            <div><span class="label">User message:</span> (silent)</div>
            <div><span class="label">Retry:</span> No</div>
            <div><span class="label">Fallback:</span> Web SSO</div>
          </div>
        </td>
        <td>
          Intune MAM is enabled for the org but not configured on the server.
        </td>
        <td>
          <span class="label">Cause:</span> Intune MAM isn't fully configured in <strong>System Console &gt; Environment &gt; Mobile Security</strong>.<br/>
          <span class="label">Next step:</span> Enable Microsoft Intune MAM and ensure <strong>Tenant ID</strong>, <strong>Application (Client) ID</strong>, and <strong>Auth Provider</strong> are set correctly.<br/>
          <span class="label">Admin checks:</span> Confirm the selected auth provider is Entra-backed and required permissions/admin consent have been granted for the Entra app registration.<br/>
          <span class="label">User guidance:</span> Have the user sign in via web/desktop while configuration is completed.
        </td>
      </tr>

      <!-- Bot login forbidden -->
      <tr>
        <td>
          <strong>Bot accounts cannot sign in using this method.</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>api.user.login_by_intune.bot_login_forbidden.app_error</code></div>
            <div><span class="label">HTTP:</span> 403</div>
            <div><span class="label">Scenario:</span> Bot tried to login</div>
            <div><span class="label">User message:</span> "Bot accounts cannot sign in using this method."</div>
            <div><span class="label">Retry:</span> No</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          The account cannot use Intune MAM sign-in.
        </td>
        <td>
          <span class="label">Cause:</span> Bot accounts are not allowed to authenticate via Intune MAM.<br/>
          <span class="label">Next step:</span> Use a human user account for Intune MAM enrollment and access.
        </td>
      </tr>

      <!-- Account locked/deactivated -->
      <tr>
        <td>
          <strong>Your account has been deactivated. Please contact your administrator.</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>api.user.login_by_intune.account_locked.app_error</code></div>
            <div><span class="label">HTTP:</span> 409</div>
            <div><span class="label">Scenario:</span> User deleted/disabled</div>
            <div><span class="label">User message:</span> "Your account has been deactivated. Please contact your administrator."</div>
            <div><span class="label">Retry:</span> No</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          The account is not permitted to sign in.
        </td>
        <td>
          <span class="label">Cause:</span> The user is deleted, disabled, or locked in Mattermost.<br/>
          <span class="label">Next step:</span> Re-enable or restore the user account in Mattermost, then retry sign-in and enrollment.
        </td>
      </tr>

      <!-- IsConfigured() false -->
      <tr>
        <td>
          <strong>(silent)</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>ent.intune.login.not_configured.app_error</code></div>
            <div><span class="label">HTTP:</span> 403</div>
            <div><span class="label">Scenario:</span> IsConfigured() = false</div>
            <div><span class="label">User message:</span> (silent)</div>
            <div><span class="label">Retry:</span> No</div>
            <div><span class="label">Fallback:</span> Web SSO</div>
          </div>
        </td>
        <td>
          Intune MAM is not configured for the current sign-in path.
        </td>
        <td>
          <span class="label">Cause:</span> Intune MAM isn't configured for the requested authentication path (configuration incomplete or mismatched provider selection).<br/>
          <span class="label">Next step:</span> Confirm Intune MAM is enabled and configured, and the selected <strong>Auth Provider</strong> matches how users authenticate (OIDC vs SAML).<br/>
          <span class="label">User guidance:</span> Have the user sign in via web/desktop while configuration is corrected.
        </td>
      </tr>

      <!-- IdAttribute mapping failed -->
      <tr>
        <td>
          <strong>We couldn't complete your sign in. Please try again.</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>ent.intune.login.extract_auth_data.app_error</code></div>
            <div><span class="label">HTTP:</span> 400</div>
            <div><span class="label">Scenario:</span> IdAttribute mapping failed</div>
            <div><span class="label">User message:</span> "We couldn't complete your sign in. Please try again."</div>
            <div><span class="label">Retry:</span> Yes (1x)</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          Identity mapping failed during sign-in.
        </td>
        <td>
          <span class="label">Cause:</span> The server couldn’t extract or map the identity attribute required for Intune MAM (commonly <code>IdAttribute</code> is misconfigured or the token isn't MSAL v2).<br/>
          <span class="label">Next step:</span> Ensure <code>IdAttribute = objectId</code>, then confirm identity alignment (<code>objectId ↔ oid</code>). Verify the Entra app issues v2 tokens (<code>accessTokenAcceptedVersion = 2</code>).
        </td>
      </tr>

      <!-- SAML user not found -->
      <tr>
        <td>
          <strong>Your account isn't fully set up yet. Please sign in to Mattermost via the web or desktop app first.</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>ent.intune.login.account_not_found.app_error</code></div>
            <div><span class="label">HTTP:</span> 428</div>
            <div><span class="label">Scenario:</span> SAML user account not found</div>
            <div><span class="label">User message:</span> "Your account isn't fully set up yet. Please sign in to Mattermost via the web or desktop app first."</div>
            <div><span class="label">Retry:</span> No</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          The user does not exist in Mattermost for SAML-based sign-in.
        </td>
        <td>
          <span class="label">Cause:</span> When SAML is the selected provider for Intune MAM enforcement, mobile sign-in cannot create a new user.<br/>
          <span class="label">Next step:</span> Have the user sign in once via the web or desktop app to provision the account, then retry mobile sign-in.<br/>
          <span class="label">Admin checks:</span> Ensure provisioning is in place (web/desktop first sign-in, LDAP sync, or another provisioning method).
        </td>
      </tr>

      <!-- Token validation failed -->
      <tr>
        <td>
          <strong>We couldn't verify your sign in. Please try again.</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>ent.intune.validate_token.invalid_token.app_error</code></div>
            <div><span class="label">HTTP:</span> 400</div>
            <div><span class="label">Scenario:</span> Token validation failed</div>
            <div><span class="label">User message:</span> "We couldn't verify your sign in. Please try again."</div>
            <div><span class="label">Retry:</span> Yes (1x)</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          The access token could not be validated.
        </td>
        <td>
          <span class="label">Cause:</span> Token validation failed (token malformed, wrong issuer/audience, missing permissions, or Entra configuration mismatch).<br/>
          <span class="label">Next step:</span> Verify configured <strong>Tenant ID</strong> and <strong>Application (Client) ID</strong> match the Entra app used for Intune MAM. Confirm tenant-wide admin consent for required Intune MAM permissions. Then confirm identity alignment (<code>objectId ↔ oid</code>) for the affected user.<br/>
          <span class="label">Admin checks:</span> Confirm v2 tokens (<code>accessTokenAcceptedVersion = 2</code>) and required Intune MAM permissions have admin consent.
        </td>
      </tr>

      <!-- Token expired -->
      <tr>
        <td>
          <strong>Your sign in session has expired. Please try signing in again.</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>ent.intune.validate_token.token_expired.app_error</code></div>
            <div><span class="label">HTTP:</span> 400</div>
            <div><span class="label">Scenario:</span> Token expired</div>
            <div><span class="label">User message:</span> "Your sign in session has expired. Please try signing in again."</div>
            <div><span class="label">Retry:</span> Yes (1x)</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          The authentication session expired before enrollment completed.
        </td>
        <td>
          <span class="label">Cause:</span> The access token or interactive session expired during sign-in/enrollment.<br/>
          <span class="label">Next step:</span> Have the user sign in again and complete enrollment promptly.<br/>
          <span class="label">Admin checks:</span> If repeated, confirm the device can reach Entra/Intune endpoints during enrollment and prompts aren't being blocked.
        </td>
      </tr>

      <!-- Missing claims -->
      <tr>
        <td>
          <strong>We couldn't complete your sign in. Please contact your IT administrator.</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>ent.intune.validate_token.missing_claims.app_error</code></div>
            <div><span class="label">HTTP:</span> 400</div>
            <div><span class="label">Scenario:</span> Required claims missing</div>
            <div><span class="label">User message:</span> "We couldn't complete your sign in. Please contact your IT administrator."</div>
            <div><span class="label">Retry:</span> No</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          The access token is missing required identity claims.
        </td>
        <td>
          <span class="label">Cause:</span> Required claims are missing from the access token (most commonly <code>oid</code>).<br/>
          <span class="label">Next step:</span> Confirm MSAL v2 tokens are issued (<code>accessTokenAcceptedVersion = 2</code>) and the access token includes <code>oid</code>. Confirm the enforced provider uses <code>IdAttribute = objectId</code>. Then confirm identity alignment (<code>objectId ↔ oid</code>).
        </td>
      </tr>

      <!-- Invalid tenant -->
      <tr>
        <td>
          <strong>There was a configuration issue. Please contact your IT administrator.</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>ent.intune.validate_token.invalid_tenant_id.app_error</code></div>
            <div><span class="label">HTTP:</span> 400</div>
            <div><span class="label">Scenario:</span> Token tenant ≠ configured tenant</div>
            <div><span class="label">User message:</span> "There was a configuration issue. Please contact your IT administrator."</div>
            <div><span class="label">Retry:</span> No</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          The token tenant does not match the configured tenant.
        </td>
        <td>
          <span class="label">Cause:</span> The token was issued by a different tenant than the one configured in Mattermost.<br/>
          <span class="label">Next step:</span> Verify the <strong>Tenant ID</strong> configured in <strong>System Console &gt; Environment &gt; Mobile Security</strong> matches the Entra tenant issuing MSAL tokens for the user.
        </td>
      </tr>

      <!-- AADSTS650057 -->
      <tr>
        <td>
          <strong>AADSTS650057</strong><br/>
          <span class="meta">(invalid_resource)</span>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>(AADSTS650057)</code></div>
            <div><span class="label">HTTP:</span> <code>(varies)</code></div>
            <div><span class="label">Scenario:</span> invalid_resource</div>
            <div><span class="label">User message:</span> (MSAL/Entra error)</div>
            <div><span class="label">Retry:</span> No (until fixed)</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          Required Intune MAM API permission is missing.
        </td>
        <td>
          <span class="label">Cause:</span> Required Intune MAM API permissions are missing or do not have tenant-wide admin consent.<br/>
          <span class="label">Next step:</span> Add and grant admin consent for <code>https://msmamservice.api.application/.default</code> and Microsoft Mobile Application Management → <code>user_impersonation</code> (Delegated), then have the user retry sign-in.
        </td>
      </tr>

      <!-- NotLicensed -->
      <tr>
        <td>
          <strong>NotLicensed</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>(NotLicensed)</code></div>
            <div><span class="label">HTTP:</span> <code>(varies)</code></div>
            <div><span class="label">Scenario:</span> License missing or inactive</div>
            <div><span class="label">User message:</span> (varies)</div>
            <div><span class="label">Retry:</span> No</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          The server is not licensed for Intune MAM enforcement.
        </td>
        <td>
          <span class="label">Cause:</span> Enterprise Advanced licensing is missing or not applied to the server.<br/>
          <span class="label">Next step:</span> Apply an Enterprise Advanced license to the server and confirm the license is active, then retry.
        </td>
      </tr>

      <!-- HTTP 403 Forbidden -->
      <tr>
        <td>
          <strong>HTTP 403 Forbidden</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>(HTTP 403)</code></div>
            <div><span class="label">HTTP:</span> 403</div>
            <div><span class="label">Scenario:</span> Server-side access blocked</div>
            <div><span class="label">User message:</span> (varies)</div>
            <div><span class="label">Retry:</span> No</div>
            <div><span class="label">Fallback:</span> None</div>
          </div>
        </td>
        <td>
          Server-side access is blocked by a gating condition.
        </td>
        <td>
          <span class="label">Cause:</span> A server gating condition is preventing enrollment (not an Intune service failure).<br/>
          <span class="label">Next step:</span> Verify Enterprise Advanced licensing, Intune MAM is enabled, <strong>Auth Provider</strong> selection matches how users authenticate, configured <strong>Tenant ID</strong> and <strong>Application (Client) ID</strong> are correct, and tenant-wide admin consent is granted. Then confirm identity alignment (<code>objectId ↔ oid</code>) and Intune App Protection Policy targeting for the correct iOS bundle ID.
        </td>
      </tr>

    </tbody>
  </table>

Consent During First Login
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a user’s first mobile sign-in fails with a message such as **Consent Denied** or: ``You denied consent for Intune management. The affected accounts have been unenrolled and signed out.``

Treat this as a tenant-wide admin consent issue for the Intune MAM permissions on the Entra app registration configured in Mattermost Server (Step 3). The message may appear as if the user denied consent, but the underlying issue is that required admin consent has not been granted for the tenant.

To resolve this:

1. In Microsoft Entra, grant **tenant-wide admin consent** for the required Intune MAM permissions on the same Entra app registration configured in Mattermost.
2. Have the user retry mobile sign-in.

Rollout and Recovery Guidance
-----------------------------

* Pilot with a small group first
* Validate identity alignment before broad rollout
* Expect enforcement to occur mid-session if requirements change
