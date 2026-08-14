Session attributes
==================

.. include:: ../../../_static/badges/ent-adv.rst
  :start-after: :nosearch:

From Mattermost v11.11, :ref:`permission policies <administration-guide/manage/admin/abac-system-wide-policies:permission policies>` can evaluate **session attributes** in addition to user attributes. Where a user attribute describes *who* someone is, a session attribute describes *how they're connecting right now* (e.g., the network they're on, the client they're using, and the posture of the device in front of them).

This lets you write policies such as "only allow file downloads from a corporate IP range" or "block uploads from jailbroken mobile devices" - conditions that can't be expressed with user attributes alone. 

Session attributes are referenced in policy expressions as ``user.session.<name>``, for example ``user.session.vpn_active == "true"``.

.. note::
  Session attributes can only restrict user actions covered by permission policies; they aren't available for use in membership policies.

.. important::

  Session attributes are collected per session and evaluated at request time. They aren't stored in the database, aren't included in compliance exports, and are discarded when the session is revoked or expires. See `How session attributes are collected <#how-session-attributes-are-collected>`__.

Prerequisites
-------------

- A Mattermost Enterprise Advanced license.
- :doc:`Attribute-based access control </administration-guide/manage/admin/attribute-based-access-control>` must be enabled in **System Console > System Attributes > Attribute-Based Access**.
- Client-reported attributes require Mattermost Desktop App v6.3 or later, or Mattermost mobile app v2.44 or later. Users connecting from a web browser, or an older Desktop or mobile app, can only report a subset of attributes. See `Platform availability <#platform-availability>`__.

Enable and tune session attributes
----------------------------------

**Every session attribute is disabled by default**, to avoid collecting and evaluating attributes that aren't needed. Administrators must explicitly enable each attribute intended for use in a policy.

1. In the System Console, go to **System Attributes > Session Attributes**.
2. Locate the attribute you want to use and select **More** |more-icon| to open its actions menu.
3. Select **Enable**.

The attribute list shows the following for each attribute:

- **Display Name** and **Name**: The label shown in the System Console, and the internal name you reference in policy expressions as ``user.session.<name>``. Attributes marked **Server** are measured by the Mattermost server rather than reported by the client.
- **Type**: ``String``, ``Boolean``, or ``Enum``. Boolean and Enum attributes accept only a fixed set of values; see `Session attribute reference <#session-attribute-reference>`__.
- **Platform**: The clients that can report the attribute, with each platform marked *active* or *inactive*.
- **TTL** and **Grace**: How often clients re-report the attribute, and how long a reported value stays usable after its TTL elapses.
- **Status**: **Enabled** or **Disabled**.

The attribute list itself is fixed - session attributes can't be renamed, deleted, or added, and their types and supported platforms can't be changed.

.. note::

  Disabling an attribute stops it from being collected and evaluated. Policies that reference a disabled attribute will deny access, because the attribute is no longer present on any session. Mattermost blocks you from *saving* a new policy that references a disabled attribute, but disabling an attribute that an existing policy already references does not invalidate that policy.

TTL and grace period
~~~~~~~~~~~~~~~~~~~~

Each attribute has two timers that together control how fresh its value must be:

- **TTL (time-to-live)**: How long a client waits before re-reporting the attribute. A short TTL keeps the value current at the cost of slightly larger requests; a long TTL reduces overhead but lets the value go stale.
- **Grace period**: How long after the TTL elapses Mattermost will still evaluate the last reported value. Once TTL + grace period has passed without a fresh report, the attribute is treated as absent and policies referencing it deny access.

Defaults vary by attribute - see the `session attribute reference <#session-attribute-reference>`__. Presets of 30 seconds, 1 minute, 5 minutes, 1 hour, and 24 hours are available for both timers.

The time-to-live and grace can be adjusted in the System Console, by selecting the attribute in the Session Attributes list and opening the **More** |more-icon| menu.

.. tip::

  Grace periods absorb brief network interruptions. If you set a grace period to a very low value, users on flaky connections may be intermittently denied access while their client catches up on reporting.

How session attributes are collected
------------------------------------

Session attributes come from two sources:

- **Server-derived attributes** are measured by the Mattermost server from the incoming request itself - the connection's IP address and the ``User-Agent`` header.
- **Client-reported attributes** are collected by the Desktop App or mobile app using native operating system APIs and sent to the server in an ``X-MM-Session-Attributes`` request header.

Clients collect only what you've enabled. When a client connects, the server tells it which attributes apply to its platform and how often to refresh each one, and anything not on that list is never collected. The server ignores values it doesn't expect, such as a value for a disabled attribute or for an attribute that platform can't support. Reported values are held in the session's in-memory cache rather than written to the database, are shared across all nodes in a :doc:`high availability cluster </administration-guide/scale/high-availability-cluster-based-deployment>`, and are discarded when the user logs out or the session is revoked or expires.

Platform availability
~~~~~~~~~~~~~~~~~~~~~

Not every client can report every attribute. A user connecting from a **web browser** can't report device or network attributes such as ``os_platform``, ``vpn_active``, or ``client_ip_address``, because a browser has no access to the operating system APIs needed to measure them. Any policy that requires one of those attributes will **always deny browser users**, including users of the Mattermost web app in a browser tab. If your intent is to restrict access to managed desktop and mobile clients, this is the desired behavior. If your intent is to gate on posture *where it can be measured*, you'll need to write the policy so that browser sessions are handled deliberately rather than incidentally.

The **Platform** column in **System Console > System Attributes > Session Attributes** shows the supported clients for each attribute. The `Session attribute reference <#session-attribute-reference>`__ below lists them as well.

For desktop sessions, native device and network collection is implemented only on Windows and macOS. These attributes are absent on desktop sessions for other platforms; mobile clients use the native APIs listed in the reference table.

For mobile users, enabling ``ssid`` prompts mobile users for location access, because both iOS and Android put Wi-Fi network information behind that permission. Mattermost reads only the current network's name and doesn't collect device location, but a user who declines the prompt reports no SSID and is denied by any policy that requires it. See :ref:`Session attribute collection <deployment-guide/mobile/mobile-security-features:session attribute collection>` for what the mobile app declares and why.

Session attribute reference
---------------------------

.. list-table::
  :widths: 18 30 14 26 12
  :header-rows: 1

  * - Attribute
    - Description
    - Platforms
    - How it's collected
    - Default TTL / grace
  * - ``ip_address``
    - The IP address the request arrived from, as measured by the server.
    - Desktop, mobile, browser
    - Read from the request connection, or from ``ServiceSettings.TrustedProxyIPHeader`` when that setting is configured. See `Trusted proxy headers and inCIDR rules <#trusted-proxy-headers-and-incidr-rules>`__.
    - 15s / 15s
  * - ``user_agent_platform``
    - Hardware platform. One of ``Windows``, ``Macintosh``, ``Linux``, ``iPad``, ``iPhone``, ``iPod``, ``BlackBerry``, ``Windows Phone``, or ``Unknown``.
    - Desktop, mobile, browser
    - Parsed from the ``User-Agent`` header.
    - 300s / 300s
  * - ``user_agent_os``
    - Operating system. One of ``Windows``, ``Windows 10``, ``Windows 8.1``, ``Windows 8``, ``Windows 7``, ``Windows Vista``, ``Windows XP x64 Edition``, ``Windows XP``, ``Windows 2000``, ``Windows Phone``, ``Mac OS``, ``iOS``, ``Android``, ``Chrome OS``, ``Linux``, ``BlackBerry``, ``Kindle``, ``webOS``, or ``Unknown``.
    - Desktop, mobile, browser
    - Parsed from the ``User-Agent`` header.
    - 300s / 300s
  * - ``user_agent_browser_name``
    - Client name. One of ``Chrome``, ``Firefox``, ``Safari``, ``Edge``, ``Internet Explorer``, ``Opera``, ``Android``, ``BlackBerry``, ``Desktop App``, ``Mobile App``, ``mmctl``, or ``Unknown``.
    - Desktop, mobile, browser
    - Parsed from the ``User-Agent`` header.
    - 300s / 300s
  * - ``user_agent_browser_version``
    - Version of the browser or Mattermost client, such as ``130.0.6723``.
    - Desktop, mobile, browser
    - Parsed from the ``User-Agent`` header.
    - 300s / 300s
  * - ``client_ip_address``
    - The IP address of the device's own primary network interface, as the device sees it. Differs from ``ip_address`` when the user is behind NAT or a proxy.
    - Desktop, mobile
    - Read from the primary network interface using native OS APIs. IPv4 is used when available; the client falls back to IPv6 when no IPv4 address is present.
    - 15s / 15s
  * - ``network_interface_type``
    - Type of the device's primary network interface. One of ``wifi``, ``ethernet``, ``cellular``, ``vpn``, ``bluetooth``, or ``other``.
    - Desktop, mobile
    - macOS: ``SCNetworkInterface`` interface type. Windows: IP Helper adapter type. iOS: ``NWPathMonitor``. Android: ``NetworkCapabilities`` transport type.
    - 15s / 15s
  * - ``vpn_active``
    - Whether a VPN or tunnel interface is active on the device. ``true`` or ``false``.
    - Desktop, mobile
    - Detected by inspecting the device's network interfaces for known VPN and tunnel adapter types. See `VPN detection <#vpn-detection>`__ for accuracy limitations.
    - 15s / 15s
  * - ``ssid``
    - Name of the Wi-Fi network the device is connected to. Empty when the device isn't on Wi-Fi.
    - Desktop, mobile
    - Windows: WLAN API. iOS and Android: platform Wi-Fi APIs, which require the user to grant location access. Not collected on macOS desktop.
    - 15s / 15s
  * - ``mdm_enrolled``
    - Whether the device is enrolled in mobile device management. ``true`` or ``false``.
    - Desktop, mobile
    - Windows: presence of MDM enrollment registry entries. iOS: managed app configuration. Android: managed profile or managed app restrictions. Always reports ``false`` on macOS desktop.
    - 60s / 60s
  * - ``jailbreak_detected``
    - Whether the mobile device appears to be jailbroken or rooted. ``true`` or ``false``.
    - Mobile
    - Root and jailbreak heuristics provided by the mobile OS integration.
    - 60s / 60s
  * - ``os_platform``
    - The device's operating system family. One of ``macos``, ``windows``, ``linux``, ``ios``, or ``android``.
    - Desktop, mobile
    - Reported directly by the client using Electron or React Native APIs.
    - 60s / 60s
  * - ``os_version``
    - The device's operating system version, such as ``15.3.1`` or ``10.0.22631``.
    - Desktop, mobile
    - Reported directly by the client using Electron or React Native APIs.
    - 60s / 60s
  * - ``client_version``
    - The version of the Mattermost Desktop App or mobile app, such as ``6.3.0``.
    - Desktop, mobile
    - Reported directly by the client using Electron or React Native APIs.
    - 60s / 60s
  * - ``hardware_id``
    - A stable hardware identifier for the device.
    - Desktop
    - macOS: ``IOPlatformUUID``. Windows: SMBIOS system UUID.
    - 300s / 300s
  * - ``client_device_id``
    - A per-vendor, per-install device identifier for mobile devices.
    - Mobile
    - iOS: ``identifierForVendor``. Android: ``ANDROID_ID``.
    - 300s / 300s
  * - ``tls_device_id``
    - A device identity asserted by your reverse proxy, typically derived from a client TLS certificate.
    - Desktop, browser
    - Read from the ``X-Mattermost-Session-Attribute-Device-Id`` header, and only when ``TrustProxyDeviceIdentityHeader`` is enabled. Never accepted from a client in the header.
    - 300s / 300s
  * - ``server_fqdn``
    - The hostname of the Mattermost server the client is connected to. Useful when a client connects to multiple servers.
    - Desktop, mobile
    - Derived by the client from the configured server URL.
    - 300s / 300s
  * - ``client_fqdn``
    - The device's own fully qualified domain name.
    - Desktop
    - macOS: local hostname combined with the primary DNS search domain. Windows: ``GetComputerNameExW``.
    - 300s / 300s

.. important::

  **All session attribute values are case-sensitive.** A rule written as ``user.session.ssid == "corp-wifi"`` will never match a device connected to a network named ``Corp-WiFi``. Values are compared exactly as the client reports them. This matters most for free-text attributes such as ``ssid`` and ``client_fqdn``. Attributes with a fixed set of values are offered in a dropdown in the simple policy editor, but you still type them by hand in the CEL editor.

.. note::

  Boolean attributes such as ``vpn_active``, ``mdm_enrolled``, and ``jailbreak_detected`` are reported as the **strings** ``"true"`` and ``"false"``, not as CEL booleans. Compare them as strings: ``user.session.mdm_enrolled == "true"``.

IPv4 and IPv6
~~~~~~~~~~~~~

``client_ip_address`` prefers IPv4. When the device's primary interface has no usable IPv4 address, the client reports its IPv6 address instead. Write CIDR rules to cover both cases if your network is dual-stack, otherwise a user whose interface falls back to IPv6 will be denied by an IPv4-only rule. ``ip_address`` reflects whatever address the connection actually arrived from, which may be IPv4 or IPv6 depending on your network and reverse proxy configuration.

Trusted proxy headers and inCIDR rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When ``ServiceSettings.TrustedProxyIPHeader`` is configured, Mattermost takes ``ip_address`` from that header instead of the connection. An ``inCIDR`` rule on ``ip_address`` is only trustworthy when clients can't reach the Mattermost server directly **and** your reverse proxy overwrites the header with the real client address on every inbound request. If the proxy appends to a client-supplied value, or a client can bypass the proxy, the address is attacker-controlled and any network rule built on it can be satisfied at will.

VPN detection
~~~~~~~~~~~~~

``vpn_active`` is determined by inspecting the **types of network interfaces present on the device**, not by inspecting network traffic. Mattermost looks for interfaces that the operating system reports as VPN or tunnel adapters - for example ``utun`` and ``ipsec`` interfaces on macOS and iOS, and adapters whose type or name identifies them as VPN or tunnel devices on Windows.

Because detection is based on recognizing interface types, it has real limits:

- **Split-tunnel VPNs** may be reported as active even when traffic to Mattermost isn't going through the tunnel, or not reported at all, depending on how the client provisions its interfaces.
- **Non-standard VPN implementations** that don't present a recognizable tunnel interface aren't detected.
- ``vpn_active`` tells you a tunnel interface exists, not that the Mattermost connection is using it.

.. warning::

  Don't treat ``vpn_active`` as proof that a user's traffic is traversing your corporate VPN. If you need to enforce that requests originate from your network, gate on ``ip_address`` with an ``inCIDR`` check against the address ranges your VPN concentrator or gateway presents. Use ``vpn_active`` as a supporting signal, not as the primary control.

Use session attributes in permission policies
---------------------------------------------

Enabled session attributes appear in the attribute list in the policy editors for permission policies, alongside user attributes. In the simple attribute-and-operator editor, you select a session attribute and an operator the same way you would for a user attribute. Attributes with a fixed set of values, such as ``os_platform``, ``vpn_active``, and ``user_agent_browser_name``, present their values in a dropdown, so you can't mistype them. The `session attribute reference <#session-attribute-reference>`__ lists the valid values for each.

In the Advanced Mode CEL editor, session attributes are referenced as ``user.session.<name>`` and can be combined with user attributes and with each other using the usual CEL operators:

.. code-block:: none

  user.session.mdm_enrolled == "true" || user.session.os_platform in ["macos", "windows"]

Mattermost validates session attribute references when you save a policy. Saving fails if an expression references an attribute that doesn't exist, or one that exists but is currently disabled.

IP range and version conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some conditions can't be expressed by comparing an attribute to a fixed value. Matching an IP address against a subnet, or checking that a client is at or above a minimum version, would otherwise mean listing every acceptable value one by one. Mattermost provides dedicated operators for both cases. In the simple editor they appear in the operator menu, but only after you select an attribute that supports them. In the CEL editor they're written as functions after the attribute they apply to, with the value you're comparing against in parentheses:

.. code-block:: none

  user.session.<name>.<function>("<value>")

.. list-table::
  :header-rows: 1
  :widths: 22 18 34 26

  * - Operator
    - CEL function
    - What it checks
    - Available on
  * - **in IP range**
    - ``inCIDR``
    - The IP address falls inside the given CIDR block, such as ``10.0.0.0/8``.
    - ``ip_address``, ``client_ip_address``
  * - **version is**
    - ``versionEQ``
    - The version is exactly the given version.
    - ``os_version``, ``client_version``, ``user_agent_browser_version``
  * - **version is at least**
    - ``versionGTE``
    - The version is equal to or newer than the given version.
    - ``os_version``, ``client_version``, ``user_agent_browser_version``
  * - **version is greater than**
    - ``versionGT``
    - The version is strictly newer than the given version.
    - ``os_version``, ``client_version``, ``user_agent_browser_version``
  * - **version is at most**
    - ``versionLTE``
    - The version is equal to or older than the given version.
    - ``os_version``, ``client_version``, ``user_agent_browser_version``
  * - **version is less than**
    - ``versionLT``
    - The version is strictly older than the given version.
    - ``os_version``, ``client_version``, ``user_agent_browser_version``

These operators return true or false, so in the CEL editor you can combine them with each other and with ordinary comparisons using ``&&``, ``||``, ``!``, and parentheses. To allow a range of addresses, join several ``inCIDR`` checks with ``||``:

.. code-block:: none

  user.session.ip_address.inCIDR("10.0.0.0/8") || user.session.ip_address.inCIDR("192.168.0.0/16")

To require a managed Windows desktop client on a corporate subnet running a supported version:

.. code-block:: none

  user.session.os_platform == "windows" && user.session.mdm_enrolled == "true" && user.session.ip_address.inCIDR("10.0.0.0/8") && user.session.client_version.versionGTE("6.3.0")

Keep the following in mind:

- **Version comparisons follow semantic versioning**, so ``6.10.0`` is correctly treated as newer than ``6.9.0``. A leading ``v`` and shortened versions such as ``6.3`` are accepted. Pre-release versions such as ``6.3.0-rc1`` sort before the matching release.
- **IP family must match.** An IP range condition only matches when the address and the CIDR block are the same IP version. An IPv4-only rule denies a session that reported an IPv6 address, so cover both families on a dual-stack network. See `IPv4 and IPv6 <#ipv4-and-ipv6>`__.
- **An unparseable value denies access.** If the attribute doesn't hold a valid IP address or version, the condition can't produce a result and the user is denied rather than allowed.
- **Select Validate syntax** before saving in the CEL editor. Validation catches misspelled function names and malformed CIDR blocks or version strings.

A missing attribute denies access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

  **If a policy references a session attribute that isn't present on the session, access is denied.** This applies whether the attribute was never reported, is disabled, isn't supported on the user's platform, or has gone stale past its TTL and grace period.

This is deliberate. Evaluating an absent attribute as "no value" would turn a negative condition into an implicit allow: a rule written as ``user.session.jailbreak_detected != "true"`` would pass for every client that simply never reports the attribute, including one that omits it on purpose. Denying on absence means a posture check can't be bypassed by withholding the data it depends on.

The practical consequence is that **a session attribute rule is also a client requirement**. Consider what a rule implies before saving it:

- ``user.session.os_platform == "windows"`` denies every browser and mobile session, not just non-Windows desktops.
- ``user.session.vpn_active == "false"`` denies browser sessions, because they never report ``vpn_active`` at all.
- ``user.session.hardware_id != ""`` denies every mobile and browser session, and any desktop session on a platform without native collection.

Use **Simulate access** to check the outcome for real users on the clients they actually use before you save. See `Simulate access with session attributes <#simulate-access-with-session-attributes>`__.

Simulate access with session attributes
---------------------------------------

:ref:`Simulate access <administration-guide/manage/admin/abac-system-wide-policies:simulate access>` evaluates draft policies against selected users before you save. When the rules contributing to an action reference ``user.session.*`` and the selected user has no cached session attributes, Mattermost shows a neutral **No recent session** indicator instead of an allow or deny result.

**No recent session** means the simulation had no session data to evaluate, not that the user would be denied. It typically appears when the selected user hasn't connected recently enough for their attributes to still be within TTL and grace period, or has never connected from a client that reports the attributes your rules reference.

To get a meaningful result, have the user connect from the client you're targeting, then re-run the simulation.

Configuration settings
----------------------

Both settings are managed in **System Console > System Attributes > Attribute-Based Access** and are disabled by default.

Trust proxy device identity header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Populates the ``tls_device_id`` session attribute from the ``X-Mattermost-Session-Attribute-Device-Id`` request header, allowing a reverse proxy that performs mutual TLS to assert a device identity that the client itself can't forge.

- ``config.json`` setting: ``".AccessControlSettings.TrustProxyDeviceIdentityHeader: false",`` with options ``true`` and ``false``.
- Environment variable: ``MM_ACCESSCONTROLSETTINGS_TRUSTPROXYDEVICEIDENTITYHEADER``

.. warning::

  Only enable this setting when a reverse proxy you control terminates every connection to Mattermost **and** strips or overwrites ``X-Mattermost-Session-Attribute-Device-Id`` on inbound requests. If clients can reach the Mattermost server directly, or if your proxy passes the header through unmodified, any client can assert an arbitrary device identity and satisfy policies that gate on ``tls_device_id``.

Enforce device ID consistency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Revokes a session when the device identity reported on it changes mid-session. Mattermost compares the ``tls_device_id``, ``client_device_id``, and ``hardware_id`` attributes against the values previously cached for the session; if a value changes, the session is revoked and the user must log in again. Successful revocations are recorded in the audit log.

- ``config.json`` setting: ``".AccessControlSettings.EnforceDeviceIDConsistency: false",`` with options ``true`` and ``false``.
- Environment variable: ``MM_ACCESSCONTROLSETTINGS_ENFORCEDEVICEIDCONSISTENCY``

When disabled, a changed device identity simply overwrites the cached value without revoking the session.

This setting mitigates session token theft: a stolen token replayed from a different device reports a different device identifier and the session is terminated. Enable it once you've confirmed that the device identity attributes you rely on report stable values across your fleet, since an identifier that legitimately changes will log users out.

Privacy considerations
----------------------

Session attribute collection is opt-in on the server, and default-on on the client. No attribute is collected unless a System Admin enables it, and clients only report the attributes the server asks for in the manifest.

Desktop App users can stop their client from reporting attributes entirely by clearing **Settings > Advanced > Enable session attributes**. When disabled, the Desktop App stops sending the ``X-MM-Session-Attributes`` header, which means any policy that depends on a client-reported attribute will deny that user. While the setting is enabled, the Desktop App shows users a table of every attribute it can collect and the value it currently reports, so they can see exactly what's being sent. See :ref:`Session attribute collection <deployment-guide/desktop/desktop-app-deployment:session attribute collection>` for what the Desktop App collects and how to communicate this to your users.

On mobile, enabling ``ssid`` may prompt users for location access. See :ref:`Session attribute collection <deployment-guide/mobile/mobile-security-features:session attribute collection>` for the permissions the mobile app declares.

Reported values live only in the server's per-session cache. They aren't written to the database, aren't included in compliance exports, and are discarded when the session ends.

Troubleshooting and FAQs
------------------------

Why is a user denied access when their attributes look correct?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Work through these in order:

1. **Check the client.** Confirm the user is on a client that can report the attribute, using the **Platforms** column in the `session attribute reference <#session-attribute-reference>`__. Server-derived attributes such as ``ip_address`` and the ``user_agent_*`` values are available on every client, including browsers; client-reported attributes need a Desktop or mobile app on a supported platform.
2. **Check the attribute is enabled.** A disabled attribute is never collected, so any rule referencing it denies. Go to **System Console > System Attributes > Session Attributes** to confirm the status.
3. **Check value casing.** Values are case-sensitive, so a free-text value such as ``ssid`` must match exactly what the client reports.
4. **Check freshness.** If the attribute's TTL plus grace period has elapsed without a fresh report, it's treated as absent. Very short grace periods make this more likely on unstable connections.
5. **Check the user's Desktop App setting.** If the user has cleared **Settings > Advanced > Enable session attributes**, their client reports nothing. When the setting is enabled, the table beneath it shows the value the app currently reports for each attribute, which tells you whether the problem is on the client or the server.
6. **Check location permission for** ``ssid``. Mobile devices only report the Wi-Fi network name when the user has granted location access.

Why does Simulate access show "No recent session"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The selected user has no cached session attributes for the simulator to evaluate. Have them connect from the client you're targeting and re-run the simulation. This is a neutral result, not a denial.

Can users spoof session attributes?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Client-reported attributes are self-attested by the client, so treat them as posture signals rather than as cryptographic proof. Mattermost limits the exposure in several ways: server-derived attributes are measured from the request rather than accepted from the client; ``tls_device_id`` is only ever accepted from a trusted proxy, never from a client; incoming values are validated against the schema and dropped when they're unknown, disabled, or not valid for the requesting platform; and `Enforce device ID consistency <#enforce-device-id-consistency>`__ terminates sessions whose device identity changes.

For controls that must not be self-attested, prefer ``ip_address`` with ``inCIDR`` or ``tls_device_id`` backed by mutual TLS at your proxy. Both depend on your proxy being correctly configured - see `Trusted proxy headers and inCIDR rules <#trusted-proxy-headers-and-incidr-rules>`__ and `Trust proxy device identity header <#trust-proxy-device-identity-header>`__.

Are session attributes collected for bots, personal access tokens, or integrations?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Collection is limited to interactive end-user sessions. Personal access token sessions, OAuth app sessions, local mode sessions, and remote cluster tokens don't correspond to a physical device with a security posture, so they can't report session attributes. Policies that reference session attributes will deny these callers.

Do session attributes work in a high availability cluster?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Attribute updates are broadcast to all nodes so every node evaluates policies against the same view of a session, regardless of which node handled the request that reported the value.

Can I add my own session attributes?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. The set of session attributes is fixed and defined by Mattermost. You can enable, disable, and tune the TTL and grace period of the built-in attributes, but you can't add, rename, or remove attributes, or change their types or supported platforms. For organization-specific values, use :doc:`user attributes </administration-guide/manage/admin/user-attributes>` instead.
