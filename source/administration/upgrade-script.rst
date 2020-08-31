Upgrading Mattermost Server with a script
=========================================

.. important:: This unofficial guide is maintained by the Mattermost community and this deployment configuration is not yet officially supported by Mattermost, Inc. Community testing, feedback, and improvements are welcome and greatly appreciated.

*Preparing the script*

`Save the script <https://docs.mattermost.com/administration/upgrade_mattermost.sh>`__ to your Mattermost server.

Make it executable.

.. code-block:: sh
   # chmod +x ./update_mattermost.sh
Please adjust the parameters at the beginning of the script according to your environment.

*Start the script*

To start the update process, start the script and add the desired version number as an argument.

.. code-block:: sh
   # ./upgrade_mattermost.sh <VERSION>
Example:

.. code-block:: sh
   # ./upgrade_mattermost.sh 5.26.0
