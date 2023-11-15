Cloud IP Filtering
========================

.. include:: ../_static/badges/ent-cloud-only.rst
   :start-after: :nosearch:


IP Filtering is a powerful security feature that allows system administrators to control access to their workspace by defining approved IP ranges. Only users within these specified IP ranges can access the workspace, ensuring enhanced security for your workspace. IP Filtering requires a subscription to Mattermost Cloud Enterprise.  

Accessing the IP Filtering Configuration:
------------------------

1. **Login as System Administrator:** Access the system console of your workspace, ensuring your user is a system administrator.

2. **Navigate to Site Configuration:** Once logged in, navigate to the "Site Configuration" section within the admin console.

3. **Access IP Filtering Settings:** Under "Site Configuration," select "IP Filtering" to access the IP Filtering settings.

Understanding CIDR Notation:
----------------------------


CIDR (Classless Inter-Domain Routing) notation is used to specify a range of IP addresses. It consists of an IP address followed by a forward slash and a number indicating the network's prefix length. For example:

   - `192.168.0.0/24` represents the IP range from `192.168.0.0` to `192.168.0.255`.
   - The `/24` signifies that the first 24 bits are the network address, leaving 8 bits for host addresses.

For a more in-depth explanation of CIDR notation, refer to `this article </https://aws.amazon.com/what-is/cidr/>`__.

Configuring IP Filters:
------------------------

Adding an IP Range:
~~~~~~~~~~~~~~~~~~~~~~~
To add an IP range to the whitelist, follow these steps:

1. Click on the "Add Filter" button within the IP Filtering settings page in the System Console.
2. Enter the IP range using CIDR notation. For example, `192.168.1.0/24`.
3. Provide a descriptive name or label for the IP range to ease identification in the future.
4. Save the changes.

.. note::

   The system console will restrict you from saving changes if the IP address you are accessing your workspace on is not within the ranges you have specified at the time of clicking save

Editing or Removing an Existing IP Range:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To edit or remove an existing IP range from the whitelist:

1. Locate the IP range you wish to modify within the IP Filtering settings.
2. Hover over the rule you'd like to edit or delete, and click on the respective edit or delete option beside the IP range.
3. Make necessary changes or confirm the removal of the IP range.
4. Save changes by clicking the "Save" button

Enabling/Disabling IP Filtering:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
System administrators have the option to enable or disable IP Filtering:

- **Enable:** To activate IP Filtering, ensure at least one IP range is added to the whitelist.
- **Disable:** Temporarily disable IP Filtering by removing all IP ranges from the whitelist, or by flipping the global IP Filtering toggle in the System Console.

Unable to Access Your Workspace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If  you are unable to access your workspace due to previously set IP filters, and you need to regain access to your workspace, your workspace owner can:

1. Navigate to the `Mattermost Customer Portal </https://customers.mattermost.com/>`__.
2. Click on the "IP Filtering" menu item in the left hand side bar.
3. Click on the button to "Disable IP Filtering"

.. note::

   Going through this process will disable **all** existing rules applied to your workspace. This means that any IP address will now be able to access it.

Conclusion:
--------------

By configuring IP filters using CIDR notation, system administrators can effectively manage access to the workspace, enhancing security by allowing access only from specified IP ranges.

For any further assistance or queries, `contact our support team </https://mattermost.com/support/>`__.
