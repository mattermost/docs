Configure Microsoft Intune Mobile Application Management (MAM)
==============================================================

.. include:: ../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

You can configure the Mattermost Mobile App on iOS to enforce Microsoft Intune App Protection Policies (MAM) so organizational data remains protected on Bring Your Own Device (BYOD) and mixed-use devices without requiring device enrollment (MDM).

This guide documents the required configuration to enable Intune MAM successfully on iOS. 

Read This First
----------------

Intune MAM enforcement in Mattermost is provider-scoped and identity-based.

Before you begin:

* Intune MAM is enforced only for the authentication provider selected in **System Console > Environment > Mobile Security**.
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

Other authentication methods, such as guest access, may still be enabled separately, but they are not evaluated by Intune MAM.

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

+-------------------------------+-----------------------------------------+----------------------------------------------+
| Value                         | Where to get it                         | Where you use it                             |
+===============================+=========================================+==============================================+
| Directory (tenant) ID         | Entra app registration overview         | Mattermost System Console                    |
+-------------------------------+-----------------------------------------+----------------------------------------------+
| Application (client) ID       | Entra app registration overview         | Mattermost System Console                    |
+-------------------------------+-----------------------------------------+----------------------------------------------+
| Application ID URI            | Entra app > Expose an API               | Used when authorizing the scope              |
+-------------------------------+-----------------------------------------+----------------------------------------------+
| ``login.mattermost`` scope    | Entra app > Expose an API               | Authorized client applications               |
+-------------------------------+-----------------------------------------+----------------------------------------------+
| Mobile client application ID  | Provided by Mattermost                  | Entra app > Authorized client applications   |
+-------------------------------+-----------------------------------------+----------------------------------------------+
| iOS bundle IDs (prod/beta)    | This guide                              | Intune App Protection Policies               |
+-------------------------------+-----------------------------------------+----------------------------------------------+

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
* Email, UPN, and ``immutableID`` are not supported.
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

Authorize the official Mattermost Mobile client application ID (provided by Mattermost) to request the ``login.mattermost`` scope. If the client application ID is not yet available, complete the remaining steps and return here once Mattermost provides it.

API Permissions and Admin Consent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _api-permissions-admin-consent:

1. Go to **API permissions**.
2. Add required Intune MAM permissions:

   * ``https://msmamservice.api.application/.default``
   * Microsoft Mobile Application Management → ``user_impersonation`` (Delegated)

3. Grant **tenant-wide admin consent**.

Configure MSAL v2 Tokens
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the app **Manifest**
2. Set ``accessTokenAcceptedVersion`` to ``2``
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

If enrollment fails due to a technical error:

* The server is removed from the mobile app
* Cached data for that server is wiped

If the user declines enrollment, retry is allowed.

Intune MAM Errors
~~~~~~~~~~~~~~~~~

The errors below may occur during mobile sign-in or when Intune MAM enforcement is triggered mid-session. Some errors are shown in the Mattermost Mobile App, while others are silent and must be diagnosed using Mattermost server logs.

.. raw:: html

  <style>
    .mm-intune-errors {
      width: 100%;
      border-collapse: collapse;
      table-layout: fixed;
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
      background-color: #f2f2f2; /* light gray */
      color: #111111;            /* explicit dark text */
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
      margin-top: 0.4rem;
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
        background-color: #2a2a2a; /* dark header */
        color: #ffffff;            /* explicit light text */
      }

      .mm-intune-errors code {
        background: rgba(255, 255, 255, 0.14);
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
          <span class="label">Next step:</span> Confirm the deployment includes Intune MAM support and the server is licensed for Enterprise Advanced.
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
          Intune MAM is enabled but not fully configured on the server.
        </td>
        <td>
          <span class="label">Cause:</span> Intune MAM configuration in Mattermost is incomplete.<br/>
          <span class="label">Next step:</span> In <strong>System Console &gt; Environment &gt; Mobile Security</strong>, enable Microsoft Intune MAM and ensure <strong>Tenant ID</strong>, <strong>Application (Client) ID</strong>, and <strong>Auth Provider</strong> are set correctly.
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
          <span class="label">Cause:</span> Intune MAM is not configured for the requested authentication path (configuration incomplete or mismatched provider selection).<br/>
          <span class="label">Next step:</span> Confirm Intune MAM is enabled and configured, and that the selected <strong>Auth Provider</strong> matches how users authenticate (OIDC vs SAML).
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
          <span class="label">Cause:</span> The server couldn’t extract or map the identity attribute required for Intune MAM (commonly <code>IdAttribute</code> is misconfigured or the token is not MSAL v2).<br/>
          <span class="label">Next step:</span> Ensure the enforced provider uses <code>IdAttribute = objectId</code>, then confirm identity alignment (<code>objectId ↔ oid</code>). Verify the Entra app issues v2 tokens (<code>accessTokenAcceptedVersion = 2</code>).
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
          <span class="label">Cause:</span> When SAML is the enforced provider, mobile sign-in cannot create a new user.<br/>
          <span class="label">Next step:</span> Have the user sign in once via web/desktop to create/provision the account, then retry mobile sign-in.
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
          <span class="label">Cause:</span> Token validation failed (tenant/client mismatch or configuration/consent issue).<br/>
          <span class="label">Next step:</span> Verify the configured <strong>Tenant ID</strong> and <strong>Application (Client) ID</strong> match the Entra app used for Intune MAM. Confirm tenant-wide admin consent for required Intune MAM permissions.
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
          <span class="label">Next step:</span> Have the user sign in again and complete enrollment promptly. If repeated, confirm the device can reach Entra/Intune endpoints during enrollment.
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
          <span class="label">Next step:</span> Confirm the Entra app issues MSAL v2 tokens (<code>accessTokenAcceptedVersion = 2</code>) and that the access token includes <code>oid</code>. Confirm the enforced provider uses <code>IdAttribute = objectId</code>. Then confirm identity alignment (<code>objectId ↔ oid</code>).
        </td>
      </tr>

      <!-- Invalid tenant -->
      <tr>
        <td>
          <strong>There was a configuration issue. Please contact your IT administrator.</strong>
          <div class="meta">
            <div><span class="label">Error ID:</span> <code>ent.intune.validate_token.invalid_tenant_id.app_error</code></div>
            <div><span class="label">HTTP:</span> 400</div>
            <div><span class="label">Scenario:</span> Token tenant ≠ config tenant</div>
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
          <span class="label">Next step:</span> Verify the <strong>Tenant ID</strong> configured in **System Console > Environment > Mobile Security** matches the Entra tenant issuing MSAL tokens for the user.
        </td>
      </tr>

    </tbody>
  </table>

Consent During First Login
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If authentication succeeds but enrollment stalls:

1. Grant tenant-wide admin consent for required Intune MAM permissions.
2. Have the user retry mobile sign-in.

Rollout and Recovery Guidance
-----------------------------

* Pilot with a small group first
* Validate identity alignment before broad rollout
* Expect enforcement to occur mid-session if requirements change
