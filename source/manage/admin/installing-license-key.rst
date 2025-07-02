Install a license key
=====================

.. include:: ../../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

You can use the System Console or the mmctl tools to add or change a Mattermost license key.

.. tab:: Use System Console

    1. Go go **System Console > About > Edition and License**.
    2. Upload your license key file.

    Once the key is uploaded and installed, the details of your license are displayed.

.. tab:: Use mmctl

    Use the :ref:`mmctl license upload <manage/mmctl-command-line-tool:mmctl license upload>` command to upload a new license or replace an existing license file with a new one. When complete, restart the Mattermost server. If you're running in a :doc:`High Availability </scale/high-availability-cluster-based-deployment>` environment, the new license file must be updated to every node.

    .. code-block:: sh

        mmctl license upload [license] [flags]

.. note::

    - Enterprise customers with the Premier Support add-on can request a staging license for testing.
    - Removing a Mattermost Enterprise or Professional license key won't remove the configuration for Enterprise settings; however, these features won't function until an Enterprise or Professional license key is applied.
    - When you're using :doc:`High Availability </scale/high-availability-cluster-based-deployment>`, it's critical to ensure that all servers in the cluster have same Enterprise license properly installed to prevent multi-node clusters from failing. An Enterprise license is required for High Availability to work.
    - When you apply an Enterprise license key to a server previously licensed for Professional, Professional features retain their configuration settings in Enterprise. 
    - When you apply a Professional license to a server previously licensed for Enterprise, Enterprise features retain their configuration but will no longer be accessible for use.

Change an existing license key
-------------------------------

You don't need to wait for your current license key to expire before replacing it with a new license from Mattermost. The server only checks for seat count and license end date, not the start date, so you can apply a new license as soon as you receive it. However, ensure your new license is for a seat count that's greater than or equal to your current total number of Mattermost users.

.. tip::
    
    To find the total number of users, go to **System Console > Reporting > Site Statistics**. The total number of users is displayed in the **Total Activated Users** field. The license will be rejected if this value is greater than the value allowed by your license key.

License seat count enforcement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


From Mattermost server v10.10 onward, system administrators can configure active enforcement of licensed seat count limits using the :ref:`IsSeatCountEnforced <configure/environment-configuration-settings:enforce license seat count>` setting. When this feature is enabled:

- **Active enforcement**: New user registration and activation is blocked when the total number of activated users reaches the licensed seat count.
- **System admin notifications**: Administrators receive notifications when approaching license limits.
- **Compliance management**: Organizations can enforce license compliance in real-time rather than relying solely on quarterly true-up processes.

When seat count enforcement is disabled (default), Mattermost continues to use the traditional quarterly true-up reporting model for license compliance.

Follow these steps to change your license key:

1. Go to **System Console > About > Edition and License**.
2. From Mattermost v6.7, simply upload your new license key file. 

.. note::
    
    If you're running a Mattermost release older than v6.7, select **Remove Enterprise License and Downgrade Server** to clear the license from the server and refresh the System Console first before uploading the new key.

License key storage
-------------------

Once you've uploaded your license key to your Mattermost server, it's stored in your SQL database at ``mattermost.Licenses``. You can check what keys are on your server by running ``select * from mattermost.Licenses;``.
