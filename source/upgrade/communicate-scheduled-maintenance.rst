Communicate scheduled maintenance
==================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Performing scheduled maintenance on a Mattermost server with 1,000 or more users requires advanced planning and a clear communication strategy to ensure minimal disruption and maximum transparency. 

This guide provides best practices for notifying users via email and Mattermost channels, updating the load balancer’s error message, and configuring a dismissable banner to inform users of the upcoming maintenance.

Communication strategy
----------------------

A well-defined communication strategy is essential for informing users before, during, and after maintenance. The key components of this strategy are:

- Define a clear maintenance window in which the self-hosted Mattermost server will be unavailable.

    - Mattermost Cloud deployments have predefined service windows scheduled from 8:00-10:00 UTC on Saturdays only (when applicable) unless an exception has been made and communicated to impacted customers.
- `Email notifications <#email-templates>`__: Send structured and consistent emails to users at intervals of 7 days, 3 days, and 1 day before the scheduled maintenance window.
- `Channel-based reminders <#channel-reminder-templates>`__: :doc:`Send messages </collaborate/send-messages>` similar to the emails in relevant Mattermost channels at the same intervals as the email notifications.
- `Mattermost Banner notification <#banner-notification>`__: Set a :doc:`system-wide notification </manage/system-wide-notifications>` to display at the top of the Mattermost instance ahead of the maintenance window and outage.
- `Display a load balancer message <#display-load-balancer-message>`__: Update the load balancer to show a maintenance message during the scheduled maintenance window of downtime.

Notification templates
----------------------

Email Templates
~~~~~~~~~~~~~~~

7-Day notice email
^^^^^^^^^^^^^^^^^^

**Email subject**: Scheduled Maintenance Notification: [Date and Time]

.. code-block:: none

    Dear Mattermost Users,

    This is a notification that our Mattermost server will undergo scheduled 
    maintenance on [Date] from [Start Time] to [End Time] [Time Zone]. 
    During this time, the Mattermost instance will be unavailable.

    We apologize for any inconvenience this may cause and appreciate your 
    understanding as we work to improve our service.

    If you have any questions or concerns, please contact our 
    support team at [Support Email].

    Thank you for your cooperation.

    Best regards,
    [Your Name]
    [Your Position]

3-Day notice email
^^^^^^^^^^^^^^^^^^

**Email subject**: Reminder: Scheduled Maintenance on [Date and Time]

.. code-block:: none

    Dear Mattermost Users,

    This is a reminder that our Mattermost server will undergo scheduled 
    maintenance on [Date] from [Start Time] to [End Time] [Time Zone]. 
    The Mattermost instance will be unavailable during this period.

    If you have any questions or concerns, please contact our 
    support team at [Support Email].

    Thank you for your cooperation.

    Best regards,
    [Your Name]
    [Your Position]

1-Day notice email
^^^^^^^^^^^^^^^^^^

**Email subject**: Final Reminder: Scheduled Maintenance Tomorrow on [Date and Time]

.. code-block:: none

    Dear Mattermost Users,

    This is a final reminder that our Mattermost server will undergo scheduled
    maintenance tomorrow, [Date], from [Start Time] to [End Time] [Time Zone]. 
    The Mattermost instance will be unavailable during this period.

    If you have any questions or concerns, please contact our
    support team at [Support Email].

    Thank you for your cooperation.

    Best regards,
    [Your Name]
    [Your Position]

Channel reminder templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~

7-Day channel reminder
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

    @all Please be advised that our Mattermost server will 
    undergo scheduled maintenance on [Date],
    from [Start Time] to [End Time] [Time Zone]. 
    The instance will be unavailable during this time. We appreciate your understanding.

3-Day channel reminder
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

    @all This is a reminder that our Mattermost server will 
    undergo scheduled maintenance on [Date],
    from [Start Time] to [End Time] [Time Zone]. 
    Please plan accordingly.

1-Day channel reminder
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: none

    @all Final reminder: Our Mattermost server will 
    undergo scheduled maintenance tomorrow, [Date], 
    from [Start Time] to [End Time] [Time Zone]. 
    Thank you for your cooperation.

Banner notification
~~~~~~~~~~~~~~~~~~~

Sample message:

.. code-block:: text

    Heads up! Scheduled maintenance is planned for [Date],
    between [Start Time] and [End Time] [Time Zone]. 
    The Mattermost instance will be unavailable during this time.

Users can dismiss the banner until they log in again, or until you update the banner.

Display load balancer message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the load balancer to display a notification message during the scheduled maintenance window of downtime.

1. Identify the load balancer you are using (e.g., AWS, HAProxy).
2. Edit configuration. Adjust paths and configurations according to your specific environment.

  - For AWS, navigate to the Load Balancer configurations in the EC2 console.
  - For HAProxy, edit the ``haproxy.cfg`` file.

.. important::

    We strongly recommend adding headers, where needed in your infrastructure, to avoid outdated information being communicated to your users during and following server maintenance.

See the sample message HTML below to use as a starting point:

.. code-block:: html

    HTML Template
    <!DOCTYPE html>
    <html>
    <head>
        <title>Maintenance in Progress</title>
        <style>
            body {
                text-align: center;
                padding: 50px;
                font-family: "Arial", sans-serif;
                background-color: #f2f2f2;
            }
            .container {
                margin: auto;
                width: 50%;
                padding: 20px;
                background-color: #fff;
                border-radius: 8px;
                box-shadow: 0px 0px 10px 0px #0000001a;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Maintenance in Progress</h1>
            <p>Our Mattermost server is currently undergoing scheduled maintenance.</p>
            <p>Estimated downtime: [Start Time] to [End Time] [Time Zone]</p>
            <p>We apologize for any inconvenience and thank you for your understanding.</p>
            <p>If you have any questions, please contact our support team at <a href="mailto:[Support Email]">[Support Email]</a>.</p>
        </div>
    </body>
    </html>