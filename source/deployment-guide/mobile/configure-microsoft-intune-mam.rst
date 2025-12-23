Configure Microsoft Intune Mobile Application Management (MAM)
==============================================================

.. include:: ../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

You can configure the Mattermost Mobile App to enforce Microsoft Intune App Protection Policies (MAM) on iOS devices so organizational data remains protected on Bring Your Own Device (BYOD) and mixed-use devices. This guide provides the required configuration to activate Intune MAM successfully on iOS.

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

* You require Android Intune MAM support (not yet available).
* Your deployment cannot use Microsoft Entra ID (Azure AD).
* The authentication method you plan to protect with Intune MAM cannot use Azure AD objectId as the authoritative user identifier.
* You need a rollout model where users can defer or bypass Intune enrollment.

Before You Continue
-------------------

Before proceeding, confirm the following are true:

* You use Microsoft Entra ID for authentication.
* You can commit to Azure AD ``objectId`` as the authoritative identity.
* You have (or can obtain) a Mattermost Enterprise Advanced license.
* Target users are licensed for Microsoft Intune.
* You can register applications and grant admin consent in Microsoft Entra.

If any of the above are not true, do not proceed.

Configuration Overview
----------------------

Configuring Intune MAM for Mattermost Mobile requires coordinated setup across the following 4 systems:

* **Microsoft Entra ID (Azure AD)** – identity, app registration, API permissions
* **Microsoft Intune** – app protection policies and user targeting
* **Mattermost Server** – MAM enablement and identity alignment
* **Mattermost Mobile App (iOS)** – enrollment and enforcement

If any system is misconfigured, Intune MAM enrollment will fail.

Before beginning configuration, review the `Identity Configuration <#identity-configuration-for-intune-mam>`__ section to confirm your deployment meets the required identity model.

Setup Order
~~~~~~~~~~~

Follow this setup order exactly to avoid enrollment failures and rework.

Step 1: Finalize Identity Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Azure AD ``objectId`` is the authoritative identity.
* All sign-in paths used by the authentication method selected for Intune MAM must resolve to the same identifier.
* Access tokens issued by Entra include the ``oid`` claim.

These conditions are enforced through Microsoft Entra configuration. If they are not met, Intune MAM enrollment will fail even if all other steps are completed correctly.

Step 2: Configure Microsoft Entra Applications & Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Register the Mattermost mobile app as a public/native Entra application.
* Copy the **Application (Client) ID**.

  To register an application in Microsoft Entra, see: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app

* Configure the iOS platform with the correct bundle ID and redirect URI.

  For Entra portal steps, see: https://learn.microsoft.com/en-us/entra/identity-platform/scenario-mobile-app-configuration

  For redirect URI formatting details, see: https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri

* Grant required Intune MAM API permissions with admin consent.

  To grant tenant-wide admin consent, see: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent

Step 3: Configure Mattermost Server for Intune MAM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Enable Intune MAM in the System Console.
* Set ``IdAttribute = objectId``.
* Verify Enterprise Advanced licensing.

Step 4: Configure Intune App Protection Policies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Create an iOS App Protection Policy.
* Add the Mattermost bundle ID.
* Assign the policy using Azure AD groups.

Step 5: Validate Using the Mobile App
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Ensure test users are assigned in Intune and properly licensed.
* Test enrollment from an iOS device.
* Confirm enforcement behaviors.
* Verify mid-session enforcement behavior.

Identity Configuration for Intune MAM
--------------------------------------

This section defines the identity requirements, constraints, and runtime behavior for the authentication method selected for Microsoft Intune MAM enforcement.

.. important::

  Mattermost can support multiple authentication methods at the same time. Intune MAM enforcement applies only to the authentication method selected in the Intune MAM configuration in the Mattermost System Console. That authentication method must resolve users by Azure AD ``objectId``. Other authentication methods are not evaluated by Intune MAM.

All identity prerequisites for the authentication method selected in the Intune MAM configuration must be met before enabling Intune MAM or enrolling users.

Required Identity Model
~~~~~~~~~~~~~~~~~~~~~~~~

Microsoft Intune MAM for Mattermost requires Azure AD ``objectId`` as the authoritative user identifier.

* No alternative identifiers are supported.
* If identity is misconfigured, Intune MAM enrollment will fail, even if all other configuration steps are correct.
* There is no fallback or partial enforcement mode.
* This requirement applies regardless of authentication method.

Identity Consistency Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Azure AD ``objectId`` must be resolved consistently across all sign-in paths used by the authentication method selected for Intune MAM, including:

* Mobile (OAuth / MSAL)
* Web (SAML), if the same IdP is used
* LDAP sync, if used to provision those users

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

Attribute Synchronization & Access Enforcement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Intune MAM is enabled, some users may authenticate exclusively through the Mattermost mobile app. If your deployment uses SAML or OpenID Connect, note the following behavior:

* User attributes synchronize only at login.
* Changes made in the identity provider do not apply until the next login.
* Mobile-only users may not trigger attribute synchronization.

As a result, attribute-based access control (ABAC) may not apply immediately.

If proactive enforcement of attribute-based access changes is required, we recommend LDAP (including Entra ID Domain Services). This behavior affects **access enforcement**, not Intune MAM enrollment.

Runtime Enforcement Behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Mobile enforces Intune MAM requirements during active sessions, not only at login.

If Intune MAM becomes newly required due to policy, licensing, or configuration changes:

* Enrollment is triggered immediately.
* Access to sensitive content is restricted until enrollment succeeds.
* Users cannot bypass enforcement.

Plan rollouts assuming enforcement can occur instantly.

Once your identity model and enforcement behavior are understood and aligned, ensure the following prerequisites are in place before beginning configuration.

Detailed Prerequisites
----------------------

Microsoft Requirements
~~~~~~~~~~~~~~~~~~~~~~~

* Microsoft Entra tenant
* Permissions to register and manage enterprise applications
* Microsoft Intune App Protection Policies enabled
* Microsoft Entra–backed sign-in functions for web and mobile
* Targeted users are licensed for Microsoft Intune

Mattermost Requirements
~~~~~~~~~~~~~~~~~~~~~~~

* Mattermost Enterprise Advanced license
* Microsoft Entra (OIDC) SSO configured
* Mattermost mobile app registered as a public/native Entra application
* iOS platform configured with the correct bundle ID and redirect URI
* ``accessTokenAcceptedVersion = 2`` set in the app manifest to ensure access tokens include required claims (such as ``oid``) in the correct format
* Intune enabled

User Requirements
~~~~~~~~~~~~~~~~~

* Users authenticate via Microsoft Entra
* Users exist in Mattermost

With prerequisites in place, the next sections describe how identity requirements are enforced across each authentication method and the Microsoft Entra permissions required for Intune MAM enrollment and validation.

Identity Enforcement by Authentication Method
---------------------------------------------

Apply the same identity rule everywhere.

OAuth / Entra (Mobile)
~~~~~~~~~~~~~~~~~~~~~~

* Only the access token is used.
* The ``oid`` claim is required.

SAML (Web Login)
~~~~~~~~~~~~~~~~~

* ``SamlSettings.IdAttribute`` must map to ``objectidentifier``.
* Email, UPN, and ``immutableID`` are not supported.

LDAP (Entra ID Domain Services)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Use ``msDS-aadObjectId`` as the identity attribute.
* Do not use ``objectGUID``.

Mandatory Microsoft Entra API Permissions
-----------------------------------------

The following Microsoft Entra API permissions are mandatory for Intune MAM enrollment and server-side token validation. Missing permissions will block enrollment.

Grant admin consent for each required permission below:

+-----------------------+--------------------------------------------------------------+
| Component             | Permission                                                   |
+=======================+==============================================================+
| Mattermost Mobile App | Microsoft Mobile Application Management →                    |
|                       | ``user_impersonation`` (Delegated)                           |
+-----------------------+--------------------------------------------------------------+
| Mattermost Server     | ``https://msmamservice.api.application/.default``            |
+-----------------------+--------------------------------------------------------------+

.. note::

    ``user_impersonation`` appears as ``DeviceManagementManagedApps.ReadWrite``.

With prerequisites met and identity requirements understood, proceed to the configuration steps in the next section.

Required Mattermost Server Configuration
----------------------------------------

1. Go to **System Console > Environment > Mobile App Management**.
2. Enable **Microsoft Intune App Protection Policies**.
3. Set ``IdAttribute`` to ``objectId``.
4. Save your changes.

Validation Checklist
--------------------

Before rolling out to production, validate the configuration using a test user account. Confirm the following values match for the same user:

* Azure AD ``objectId``
* MSAL access token ``oid`` claim
* SAML ``objectidentifier`` (if applicable)
* LDAP ``msDS-aadObjectId`` (if applicable)

Any mismatch will cause Intune MAM enrollment to fail.

Deploy or Update Mattermost Mobile Apps
---------------------------------------

Install the latest Mattermost iOS mobile app using one of the following methods:

* Public App Store
* Microsoft Intune deployment
* Private or wrapped builds

.. note::

   Mattermost Beta (``com.mattermost.rnbeta``) and Production (``com.mattermost.rn``) apps require **separate** Microsoft Entra app registrations.

MDM device enrollment is not required.

Configure Intune App Protection Policies
----------------------------------------

1. Go to the **Microsoft Intune Admin Center**.
2. Create an **iOS App Protection Policy**.
3. Add the Mattermost bundle ID.
4. Assign the policy using **Azure AD groups**.

Mattermost roles do not control Intune MAM enforcement.

Expected Mobile Login & Enrollment Flow
---------------------------------------

When Intune MAM is enabled:

1. The mobile app checks:
   * Platform is iOS
   * Intune MAM is enabled
   * Authentication service matches
   * License is **Enterprise Advanced**

2. The user taps **Sign in**. careful with using `Microsoft` explicitly cause we don't enforce it
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

The following errors are displayed in the **Mattermost mobile app** during user login or when enrollment is triggered mid-session. Errors are **not** displayed in the Mattermost System Console.

+-------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Error                         | Meaning                                     | Cause & Next Step                                                                                                                |
+===============================+=============================================+==================================================================================================================================+
| Enrollment Failed             | Intune MAM enrollment failed due to a       | Technical enrollment failure (MSAL error, enrollment API failure, identity mismatch, or missing required Entra permissions).     |
|                               | technical error                             |                                                                                                                                  |
|                               |                                             | The server is removed immediately with **no retry option**. Fix the underlying issue before re-adding the server.                |
+-------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Enrollment Declined           | User declined Intune MAM enrollment         | User canceled the enrollment prompt. A **Retry** option is presented to the user.                                                |
|                               |                                             |                                                                                                                                  |
|                               |                                             | Instruct the user to retry enrollment when ready. No server data is removed unless enrollment later fails technically.           |
+-------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| AADSTS650057                  | Required Intune MAM API permission is       | This error appears during MSAL authentication or token validation.                                                               |
| (invalid_resource)            | missing                                     |                                                                                                                                  |
|                               |                                             | The ``https://msmamservice.api.application/.default`` permission is missing or lacks admin consent.                              |
|                               |                                             |                                                                                                                                  |
|                               |                                             | Add the permission in Microsoft Entra and grant admin consent.                                                                   |
+-------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| MissingAuthAccountError       | Access token does not contain the identity  | MSAL error indicating the access token does not contain the identity claim Mattermost expects.                                   |
|                               | claim Mattermost expects                    |                                                                                                                                  |
|                               |                                             | Unsupported or custom ``IdAttribute`` used, or required claim missing from the access token.                                     |
|                               |                                             |                                                                                                                                  |
|                               |                                             | Use only supported ``IdAttributes`` (``objectId``) and ensure the ``oid`` claim is present.                                      |
+-------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| User mismatch                 | Mobile identity does not match the          | Mutable identifiers (email, ``preferred_username``) used, or user email/UPN changed.                                             |
|                               | server-side user                            |                                                                                                                                  |
|                               |                                             | Reconfigure identity to use Azure AD ``objectId`` exclusively.                                                                   |
+-------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| NotLicensed                   | Server is not licensed for Intune MAM       | Enterprise Advanced license missing or not applied to the server.                                                                |
|                               |                                             |                                                                                                                                  |
|                               |                                             | Verify license tier and server coverage.                                                                                         |
+-------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| HTTP 403 Forbidden            | Server-side access is blocked               | Server gating condition, not an Intune failure.                                                                                  |
|                               |                                             |                                                                                                                                  |
|                               |                                             | Verify Enterprise Advanced license, Intune is enabled in the System Console, valid Tenant ID and Client ID, authentication       |
|                               |                                             | provider is configured, admin consent is granted, and ``IntuneScope`` is set.                                                    |
+-------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

Enrollment Failure Session Behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If Intune MAM enrollment fails due to a **technical error**, the following occurs:

* The user is logged out of the affected Mattermost server.
* The server is removed from the Mattermost mobile app.
* All cached data for that server is wiped from the device.

If a user has multiple Mattermost servers configured in the app, **only the failing server is removed**. Other servers remain accessible and unaffected.

If the user **declines enrollment**, retry is allowed and no server data is removed unless enrollment later fails due to a technical error.
