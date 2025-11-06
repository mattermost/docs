Multi-View Desktop App
======================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

From desktop app v6.0.0 onward, the Multi-View Desktop App transforms how organizations coordinate across multiple Mattermost environments. This powerful enhancement unifies your operational picture by enabling simultaneous viewing and coordination of multiple workspaces, enhancing cross-system interoperability and command-level situational awareness.

The Multi-View feature is designed for teams operating in distributed or multi-domain environments where coordination across different Mattermost instances is critical for operational success.

Key Benefits
------------

- **Unified Operational View**: Monitor multiple Mattermost workspaces simultaneously from a single desktop interface
- **Enhanced Situational Awareness**: Maintain command-level visibility across distributed systems
- **Cross-System Interoperability**: Seamlessly coordinate activities between different Mattermost environments
- **Streamlined Workflow**: Reduce context switching between different workspace instances
- **Centralized Management**: Administer multiple workspace connections from one location

Multi-View Interface Overview
-----------------------------

The Multi-View interface provides a consolidated dashboard that displays multiple Mattermost workspaces in configurable layouts. Users can:

- View real-time activity across all connected workspaces
- Respond to messages and notifications from any workspace without switching contexts
- Monitor critical channels across different organizational domains
- Coordinate cross-workspace communications and activities

Getting Started with Multi-View
--------------------------------

Prerequisites
~~~~~~~~~~~~~

- Mattermost Desktop App v6.0.0 or later
- Active connections to multiple Mattermost workspaces
- Appropriate permissions on each connected workspace

Enabling Multi-View Mode
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open the Mattermost Desktop App (v6.0+)
2. Navigate to **Settings** > **Advanced** > **Multi-View Options**
3. Enable **Multi-View Mode**
4. Configure your preferred layout and workspace arrangement
5. Select **Apply** to activate Multi-View mode

.. note::
   
   Multi-View mode requires at least two active workspace connections to function. If you have only one workspace configured, you'll need to add additional server connections first.

Workspace Management in Multi-View
-----------------------------------

Adding Workspaces for Multi-View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To take full advantage of Multi-View capabilities:

1. Ensure you have multiple :doc:`workspace connections configured </end-user-guide/preferences/connect-multiple-workspaces>`
2. Verify each workspace connection is active and authenticated
3. Configure workspace-specific settings for optimal Multi-View display

Workspace Layout Options
~~~~~~~~~~~~~~~~~~~~~~~~

Multi-View supports several layout configurations:

**Split View**: Display two workspaces side-by-side for direct comparison and coordination

**Grid View**: Show multiple workspaces in a grid layout for comprehensive monitoring

**Tabbed View with Preview**: Enhanced tabbing with workspace previews and real-time activity indicators

**Custom Layouts**: Configure personalized arrangements based on operational needs

Administrative Configuration
-----------------------------

System administrators can configure Multi-View settings to optimize the experience for their organization's operational requirements.

Multi-View Policy Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Administrators can control Multi-View functionality through policy settings:

- **Enable/Disable Multi-View**: Control whether users can access Multi-View features
- **Maximum Concurrent Workspaces**: Set limits on the number of workspaces displayed simultaneously
- **Layout Restrictions**: Specify allowed layout configurations
- **Cross-Workspace Communication**: Configure permissions for cross-workspace messaging

Configuration Steps
~~~~~~~~~~~~~~~~~~~~

1. Access the System Console as a system administrator
2. Navigate to **Desktop App Settings** > **Multi-View Configuration**
3. Configure the following settings:

   - **Allow Multi-View Mode**: Enable or disable Multi-View capabilities
   - **Default Layout**: Set the default layout for new Multi-View users
   - **Workspace Limit**: Define the maximum number of simultaneous workspace connections
   - **Cross-Workspace Features**: Enable advanced coordination features

4. Apply settings and notify users of Multi-View availability

Advanced Multi-View Features
-----------------------------

Cross-Workspace Notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multi-View provides enhanced notification management across workspaces:

- **Unified Notification Center**: Centralized view of notifications from all connected workspaces
- **Priority-Based Filtering**: Configure notification priorities based on workspace or channel importance
- **Cross-Workspace Mention Handling**: Manage mentions and direct messages across multiple environments

Synchronized Activity Monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Monitor synchronized activities across workspaces:

- **Real-time Activity Feeds**: View combined activity streams from multiple workspaces
- **Cross-Workspace Search**: Search for content across all connected environments
- **Coordinated Response Management**: Manage responses to incidents or issues spanning multiple workspaces

Multi-Workspace Communication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enhanced communication capabilities:

- **Cross-Workspace Messaging**: Send messages between different workspace environments (if permitted by administrator policies)
- **Unified Contact Management**: Access contact lists across all connected workspaces
- **Coordinated Team Management**: Manage team activities across distributed environments

User Experience Enhancements
-----------------------------

Keyboard Shortcuts for Multi-View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multi-View introduces specialized keyboard shortcuts:

- **Ctrl/Cmd + Shift + M**: Toggle Multi-View mode
- **Ctrl/Cmd + 1-9**: Switch focus between workspace panels
- **Ctrl/Cmd + Shift + L**: Cycle through layout options
- **Ctrl/Cmd + Shift + N**: Open unified notification center

Visual Indicators
~~~~~~~~~~~~~~~~~

Multi-View provides enhanced visual cues:

- **Workspace Status Indicators**: Real-time connection status for each workspace
- **Activity Badges**: Unread message and notification counts per workspace
- **Priority Highlights**: Visual emphasis for high-priority workspaces or channels

Customization Options
~~~~~~~~~~~~~~~~~~~~~

Users can customize their Multi-View experience:

- **Workspace Ordering**: Arrange workspaces based on priority or frequency of use
- **Panel Sizing**: Adjust the relative size of workspace panels
- **Color Coding**: Assign colors to different workspaces for quick identification
- **Notification Preferences**: Configure notification behavior for each workspace in Multi-View

Troubleshooting Multi-View
---------------------------

Common Issues and Solutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Multi-View option not available**
   - Verify you're using Desktop App v6.0 or later
   - Ensure you have multiple workspace connections configured
   - Check that your system administrator has enabled Multi-View in policy settings

**Performance issues with multiple workspaces**
   - Reduce the number of simultaneously displayed workspaces
   - Close unnecessary applications to free system resources
   - Consider using a less resource-intensive layout option

**Synchronization problems between workspaces**
   - Check network connectivity to all configured workspaces
   - Verify authentication status for each workspace connection
   - Restart the desktop app to refresh all connections

**Cross-workspace features not working**
   - Confirm administrator has enabled cross-workspace communication
   - Verify you have appropriate permissions on all connected workspaces
   - Check firewall and network settings that might block cross-workspace communication

Performance Optimization
~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure optimal Multi-View performance:

- **System Requirements**: Ensure your system meets enhanced requirements for Multi-View operation
- **Network Considerations**: Stable network connections to all workspaces are essential
- **Resource Management**: Monitor system resource usage when running multiple workspace connections
- **Update Management**: Keep the desktop app updated to the latest version for optimal Multi-View functionality

Best Practices
---------------

Operational Efficiency
~~~~~~~~~~~~~~~~~~~~~~~

- **Workspace Organization**: Group related workspaces together in your Multi-View layout
- **Priority Management**: Place high-priority workspaces in prominent positions
- **Notification Strategy**: Configure notifications to avoid information overload
- **Regular Maintenance**: Periodically review and optimize your workspace connections

Security Considerations
~~~~~~~~~~~~~~~~~~~~~~~

- **Access Control**: Ensure appropriate access controls are maintained across all connected workspaces
- **Data Segregation**: Be mindful of data sensitivity when using cross-workspace features
- **Authentication Management**: Regularly review and update authentication credentials for all workspaces
- **Compliance**: Ensure Multi-View usage aligns with your organization's security and compliance requirements

Team Coordination
~~~~~~~~~~~~~~~~~

- **Standardized Layouts**: Consider establishing team-wide layout standards for consistency
- **Communication Protocols**: Develop clear protocols for cross-workspace communication
- **Incident Response**: Establish procedures for managing incidents that span multiple workspaces
- **Training and Adoption**: Provide training to help team members effectively utilize Multi-View capabilities

See Also
---------

- :doc:`Connect to multiple Mattermost workspaces </end-user-guide/preferences/connect-multiple-workspaces>`
- :doc:`Customize your Desktop App experience </end-user-guide/preferences/customize-desktop-app-experience>`
- :doc:`Desktop releases </product-overview/mattermost-desktop-releases>`
- :doc:`Desktop changelog </product-overview/desktop-app-changelog>`