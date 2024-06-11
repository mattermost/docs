Manage user surveys
===================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

In your self-hosted Mattermost deployment, use the Mattermost User Survey integration to gather direct feedback from your Mattermost users to identify what's working well and what's not with your Mattermost instance. All user responses are stored in and remain within your self-hosted deployment, and no telemtry data is sent back to Mattermost. You can export a CSV report of NPS scores and user responses for further analysis, or to share your feedback data with Mattermost.

You can schedule when each survey begins, define how long each survey lasts, specify teams excluded from the survey, as well as customize both a welcome message and a user question you want feedback on.

Setup
------

You must be a Mattermost system admin to `upload the plugin <#upload>`__ to your Mattermost self-hosted deployment `enable it <#enable>`__,  `create surveys <#create-surveys>`__, and `export survey responses <#export-survey-responses>`__ using the System Console.

The User Survey integration is compatible with the following :doc:`Mattermost Server versions </deploy/mattermost-changelog>`:

  - v9.6 or later
  - v9.5.2+ (Extended Support Release - ESR)
  - v9.4.4+
  - v9.3.3+
  - v8.1.11+ (Extended Support Release - ESR)

Upload
------

The User Survey integration must be installed using the `latest binary available for download from the plugin repository <https://github.com/mattermost/mattermost-plugin-user-survey/releases>`_

1. Download the binary file from the GitHub repository.
2. Go to **System Console > Plugin Management**.
3. Next to **Upload Plugin**, select **Choose File**.
4. Select the binary file, select **Open**, and then select **Upload**.

Once the binary is uploaded, the **User Survey** integration is added in the navigation pane under **Plugins**.

.. note::

  Mattermost offers an additonal :doc:`User Satisfaction Surveys </manage/user-satisfaction-surveys>` option with limited customization options within the **Plugins** list where surveys are enabled by default. We recommend :ref:`disabling the User Satisfaction Surveys functionality <manage/user-satisfaction-surveys:how can surveys be disabled?>` when using this user survey integration.

Upgrade
~~~~~~~

We recommend updating this integration as new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost.

Visit the `Releases page <https://github.com/mattermost/mattermost-plugin-user-survey/releases>`_ for the latest release, available releases, and compatibiilty considerations.

Enable
------

Go to **System Console > Plugins > User Survey** to enable this integration.

Once the integration is installed and enabled, create surveys by completing configuration in the System Console, as described below.

Create surveys
--------------

Under **Survey setup**, specify the date, time, and details for a new survey:

1. **Send next survey at**: Specify the date and time when the survey will begin rolling out to users.

  .. note::

      A single survey can be active at a time. If you already have an active survey running, you'll need to reschedule your new survey to start on a date after the current survey expires. Alternatively, you can end the active survey early by selecting **End survey**.

2. **Survey expiry**: Specify how long the survey will be open to responses in days.
3. **Exclude specific teams**: Specify teams that shouldn't receive the survey. The survey is sent to all teams if left blank.
4. **Survey message text** Customize the introductory message text users see when prompted to complete the survey.
5. **Textual question**: (Optional) Specify a text-based question for the survey.
6. Select **Save**. Your new survey is scheduled, and displays under **Active and past surveys** when the survey is shared with users.

Active surveys
--------------

When a survey starts, all users recieve a direct message from a feedback bot containing the active survey. The survey includes one mandatory scale-based question, a mandatory text-based question, and 1 optional, customized text-based question. 

Users must answer at least 1 question. When a user selects **Submit**, their responses are recorded.

Export survey responses
-----------------------

Once a survey ends, select **Export responses** to download a CSV file containing NPS scores and user responses gatherered through the survey.