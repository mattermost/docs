Desktop App Privacy and Data Handling
======================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

This page provides detailed information about data collection, privacy protections, and compliance considerations for the Mattermost Desktop App. This information is intended for risk assessors, compliance officers, and security teams evaluating the desktop app for organizational use.

Error reporting and crash telemetry (v6.1.0+)
----------------------------------------------

From Mattermost Desktop v6.1.0, the desktop app includes automatic error reporting functionality to help identify and resolve crashes, stability issues, and application errors. This section provides comprehensive details about what data is collected, how it's transmitted, and what controls are available.

Third-party service
~~~~~~~~~~~~~~~~~~~

Error and crash data is transmitted to **Sentry**, a third-party error tracking and monitoring platform. Sentry is used by thousands of organizations worldwide for application performance monitoring and error tracking.

.. important::

  Organizations evaluating Sentry for compliance purposes should:

  - Review Sentry's data processing agreements and subprocessor list
  - Evaluate Sentry's data center locations for data residency requirements
  - Assess Sentry's data retention policies
  - Verify alignment with organizational privacy and security standards

Default behavior and user consent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Opt-out model**: Error reporting is **enabled by default** when users install or upgrade to Mattermost Desktop v6.1.0 or later. Users must take explicit action to disable error reporting if they prefer not to send data.

**User control**:

- Users can disable error reporting at any time through **Settings > Advanced > Send error reports to help improve the app**
- Changes require restarting the desktop app to take effect
- No administrator-level enforcement mechanism is available to force error reporting on or off across an organization

Data collected
~~~~~~~~~~~~~~

When error reporting is enabled, the following types of data are transmitted to Sentry:

**Error and crash information**:

- Stack traces showing the code execution path leading to errors
- Error messages and exception details
- Application state at the time of the error
- JavaScript runtime errors

**Application metadata**:

- Desktop app version number
- Build type (stable vs. prerelease)
- Electron framework version

**Platform and system information**:

- Operating system type (Windows, macOS, Linux)
- Operating system version
- System architecture (x86, x64, ARM)
- Memory statistics (total RAM, available memory)
- CPU information

**Context data**:

The desktop app collects minimal context about the error environment to help developers reproduce and fix issues. This may include:

- Active view or tab information (without content)
- Configuration settings that may be relevant to the error
- Timing information about when the error occurred

Data explicitly excluded
~~~~~~~~~~~~~~~~~~~~~~~~~

The following data is **explicitly excluded** from error reports through technical controls:

**Personally identifiable information (PII)**:

- The desktop app configures Sentry with ``sendDefaultPii: false``, which prevents automatic collection of user identifiers, IP addresses, and other PII
- User display names, usernames, and email addresses are not included
- User profile information is not transmitted

**Message content and communications**:

- Message text, channel content, and direct message content
- File attachments and file names
- Emoji reactions and custom emoji

**Authentication and credentials**:

- Passwords and authentication tokens
- Session cookies and authentication headers
- API keys and integration credentials

.. note::

  **Limitation**: While the desktop app is configured to exclude server URLs and team names from error reports, the scope of all error context data has not been exhaustively documented. Organizations with strict data handling requirements should conduct their own assessment or contact Mattermost for clarification.

Technical implementation details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Build-time configuration**:

- Error reporting requires the ``MM_DESKTOP_BUILD_SENTRYDSN`` environment variable to be set during the build process
- Organizations building the desktop app from source can prevent Sentry initialization entirely by omitting this environment variable
- The Sentry Data Source Name (DSN) determines where error reports are sent

**Runtime behavior**:

- Error reporting only activates in **production builds** (``NODE_ENV === 'production'``)
- Development and test builds do not send error data to Sentry
- The desktop app distinguishes between "stable" release builds and "prerelease" builds for environment tagging

**Network connectivity**:

- Error reports are transmitted over HTTPS to Sentry's endpoints
- Network traffic verification: Organizations can monitor outbound connections to Sentry domains for audit purposes
- Firewall rules: Organizations blocking external telemetry should identify and block Sentry endpoint domains (contact Mattermost Support or Sentry documentation for specific domains)

Compliance and regulatory considerations
-----------------------------------------

Data residency and sovereignty
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Organizations subject to data residency requirements (e.g., GDPR, data localization laws) should:

1. **Evaluate Sentry's data processing locations**: Verify where Sentry stores and processes error data
2. **Review cross-border data transfer mechanisms**: Ensure appropriate safeguards are in place for international data transfers
3. **Consider geographic restrictions**: Determine if error data transmission aligns with organizational data sovereignty policies

Consent and transparency
~~~~~~~~~~~~~~~~~~~~~~~~

**User notification**: The default-enabled error reporting feature uses an opt-out consent model. Organizations should:

- Inform users about error reporting during desktop app deployment or onboarding
- Provide clear instructions on how to disable error reporting if users prefer to opt out
- Update privacy notices or acceptable use policies to reflect error data collection

**Transparency requirements**: Organizations in jurisdictions requiring explicit consent (e.g., GDPR's requirement for informed consent) should evaluate whether the opt-out model meets regulatory requirements.

Data processing agreements
~~~~~~~~~~~~~~~~~~~~~~~~~~

Organizations requiring Data Processing Agreements (DPAs) or Business Associate Agreements (BAAs) should:

1. Confirm whether Mattermost has a DPA in place with Sentry
2. Determine if additional agreements are needed between your organization and Sentry
3. Verify that Sentry's terms of service and privacy policy meet organizational requirements

Privacy impact assessment
~~~~~~~~~~~~~~~~~~~~~~~~~

For organizations conducting Privacy Impact Assessments (PIAs) or Data Protection Impact Assessments (DPIAs):

**Risk assessment**:

- Error reports include system-level information but are designed to exclude PII and message content
- The opt-out consent model may require justification in privacy assessments
- Third-party data processing (Sentry) introduces additional data flow considerations

**Mitigation measures**:

- User control to disable error reporting
- Technical controls preventing PII transmission (``sendDefaultPii: false``)
- Build-time controls allowing organizations to disable Sentry entirely

Organizational deployment guidance
----------------------------------

For organizations with restrictive data policies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Organizations with policies prohibiting external telemetry or third-party data transmission should:

1. **Communicate with end users**:

   - Inform users that error reporting is enabled by default in Desktop v6.1.0+
   - Provide step-by-step instructions to disable error reporting via **Settings > Advanced**
   - Remind users that a restart is required after changing the setting

2. **Consider custom builds**:

   - Build the desktop app from source without the ``MM_DESKTOP_BUILD_SENTRYDSN`` environment variable
   - Distribute custom-built desktop apps that have Sentry disabled at build time

3. **Implement network controls**:

   - Block outbound connections to Sentry domains at the network or firewall level
   - Monitor network traffic to verify no error data is transmitted

Audit and verification
~~~~~~~~~~~~~~~~~~~~~~

**Confirming error reporting status**:

Organizations can verify whether error reporting is active by:

1. Checking user settings: **Settings > Advanced > Send error reports to help improve the app**
2. Monitoring network traffic for connections to Sentry endpoints
3. Reviewing desktop app logs for Sentry initialization messages (available via **Help > Show logs**)

**Build verification**:

For organizations building from source, verify that the ``MM_DESKTOP_BUILD_SENTRYDSN`` environment variable is not set during the build process to ensure Sentry is not initialized.

Additional resources
--------------------

- :doc:`Desktop app deployment guide </deployment-guide/desktop/desktop-app-deployment>` - System administrator guidance for deploying the desktop app
- :doc:`Desktop app troubleshooting </deployment-guide/desktop/desktop-troubleshooting>` - Instructions for disabling error reporting and accessing logs
- :doc:`Customize desktop app experience </end-user-guide/preferences/customize-desktop-app-experience>` - User-facing documentation for desktop app settings
- `Sentry documentation <https://docs.sentry.io/>`_ - Official Sentry documentation for privacy and security details

Questions or concerns?
----------------------

If you have questions about desktop app privacy, data handling, or compliance:

- **Mattermost customers with support contracts**: Contact `Mattermost Support <https://support.mattermost.com/hc/en-us/requests/new>`_
- **Community deployments**: Post in the `Mattermost community forums <https://forum.mattermost.com/>`_
- **Security-related inquiries**: See the `Mattermost Responsible Disclosure Policy <https://mattermost.com/security-vulnerability-report/>`_
