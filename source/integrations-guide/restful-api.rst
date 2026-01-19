RESTful API
============

.. include:: ../_static/badges/all-commercial.rst
  :start-after: :nosearch:

**Technical complexity:** :ref:`Pro-code <pro-code>`

Full developer control for automation, bots, and integrations.

The `Mattermost API <https://developers.mattermost.com/api-documentation/>`_ provides a comprehensive set of endpoints that let you programmatically interact with your Mattermost workspace. With the API, you can manage users, teams, channels, posts, and more, making it possible to automate administrative tasks, integrate external systems, and build custom applications that extend Mattermost functionality. Whether you’re writing lightweight scripts or developing full-scale integrations, the API offers flexible building blocks to tailor Mattermost to your workflows.

Using the API is a pro-code approach meant for developers who want to write scripts to automate specific workflows or build deeply customized integrations using the plugin framework to connect external systems. 

The API is often used in combination with `bot accounts <https://developers.mattermost.com/integrate/reference/bot-accounts/>`_ to authenticate and interact with Mattermost.

Example Use Cases
------------------

Here are some example use cases for API integration in Mattermost:

**User provisioning**  

Write a script to automatically create and manage user accounts in Mattermost, ensuring that new team members are added to the right teams and channels as part of your onboarding process.

**Channel management**  

Use the API to programmatically create, archive, or update channels, making it easy to align collaboration spaces with your project lifecycle or organizational changes.

**Message automation**  

Build a script or integration that posts messages or reminders into specific channels on a schedule, such as daily stand-up prompts, release announcements, or security notifications.

Learn more about using the `API and available endpoints <https://developers.mattermost.com/api-documentation/>`_.

Playbooks API Updates
----------------------

From Mattermost server v2.6.0 and mobile v2.35.0, the Playbooks API includes the following changes:

**Playbook Run API Changes:**

- Added **Type** field to playbook runs API endpoints to support channel checklists
- The **playbook_id** field is now optional in the create run flow, allowing runs to exist without being associated with a specific playbook
- Runs can be typed as "channel checklists" for standalone workflow management within channels

**Mobile API Endpoints:**

From mobile v2.35.0, the following API endpoints are used for mobile checklist functionality:

- ``/runs/{id}/checklists/{n}/rename`` - Rename checklist items
- ``/runs/{id}/checklists/{n}/add`` - Add new checklist items

.. note::

   These API changes support the new channel-based checklist workflow where checklists can be created and managed directly in channels without requiring a playbook template. The Type field and optional playbook_id provide the flexibility needed for both traditional playbook-based workflows and standalone channel checklists.

.. important::

   [NOT PRESENT IN PR — REQUIRES HUMAN JUDGMENT] Some API implementation details may require verification with system administrators or developers familiar with the specific API endpoint documentation, as not all implementation details were explicitly provided in the referenced PRs.