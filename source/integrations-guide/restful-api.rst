RESTful API
============

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