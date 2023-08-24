Install a License Key
=====================

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

You can use the System Console or the mmctl tools to add or change a Mattermost license key.

.. tabs::

    .. tab:: Use System Console

        1. Go go **System Console > About > Edition and License**.
        2. Upload your license key file.

        Once the key is uploaded and installed, the details of your license are displayed.

    .. tab:: Use mmctl

        Use the `mmctl license upload </manage/mmctl-command-line-tool.html#mmctl-license-upload>`__ command to upload a new license or replace an existing license file with a new one. When complete, restart the Mattermost server. If you're running in a `High Availability </scale/high-availability-cluster.html>`__ environment, the new license file must be updated to every node.

        .. code-block:: none

            mmctl license upload [license] [flags]

.. note::

    - Removing a Professional or Enterprise license key won't remove the configuration for Enterprise settings; however, these features won't function until an Enterprise or Professional license key is applied.
    - When you're using `High Availability </scale/high-availability-cluster.html>`__, it's critical to ensure that all servers in the cluster have same Enterprise license properly installed to prevent multi-node clusters from failing. An Enterprise license is required for High Availability to work.
    - When you apply an Enterprise license key to a server previously licensed for Professional (or legacy Enterprise Edition E10), Professional features retain their configuration settings in Enterprise. 
    - When you apply a Professional license to a server previously licensed for Enterprise, (or legacy Enterprise Edition E20), Enterprise features retain their configuration but will no longer be accessible for use.

Change an existing license key
-------------------------------

Make sure that the new license is for a number of users that is greater than or equal to the current total number of users on your system. To find the total number of users, go to **System Console > Reporting > Site Statistics**. The total number of users is displayed in the **Total Active Users** field. The license is rejected if this value is greater than the value allowed by the license key.

Then, follow these steps to change your license key:
        1. Go go **System Console > About > Edition and License**.
        2. Select **Remove Enterprise License and Downgrade Server**. This clears the license from the server and refreshes the System Console.
        3. Upload your license key file.

License key storage
-------------------

Once you've uploaded your license key to your Mattermost server, it's stored in your SQL database at ``mattermost.Licenses``. You can check what keys are on your server by running ``select * from mattermost.Licenses;``.
