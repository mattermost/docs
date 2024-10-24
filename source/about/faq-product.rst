Product questions
=================

What features are available on different Mattermost clients?
------------------------------------------------------------

The following chart highlights the end user features of Mattermost and their support across Web, Desktop, and Mobile applications (iOS and Android).

Messages
~~~~~~~~
+---------------------------------------------------+-----+---------+--------+
| Feature                                           | Web | Desktop | Mobile |
+---------------------------------------------------+-----+---------+--------+
| Threaded messages                                 |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| Markdown                                          |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| Emojis                                            |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| Emoji reactions                                   |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| Viewing emoji reactions                           |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| File sharing                                      |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| @ mentions                                        |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| Hashtags                                          |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| Search (with in:, from:, before:, on: and after:) |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| Search highlighting                               |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| View/marking pinned or saved posts                |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| Image link previews                               |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| Website previews                                  |     |         |        |
+---------------------------------------------------+-----+---------+--------+
| Notifications                                     |     |         |        |
+---------------------------------------------------+-----+---------+--------+

Channels
~~~~~~~~


What feature quality levels does Mattermost have?
--------------------------------------------------

We strive to release viable features. This means that we put in a significant amount of effort to ensure we solve a use case with a high bar for quality. A feature that's viable and meets our criteria for our production quality levels will be released to production.

However, when working on large and complex features or new products, we may need to test them with a high volume of customers and users. For these scenarios, we'll release them as :ref:`Experimental <getting-started/feature-labels:experimental>` or :ref:`Beta <getting-started/feature-labels:beta>`, and implement feature flags and/or A/B testing to validate the effectiveness of features prior to production-level release. Additionally, we `dogfood our features <https://en.wikipedia.org/wiki/Eating_your_own_dog_food>`_ on our community server, and provide many configuration options that ensure customers can opt-in when trying experimental or beta features.

See the :doc:`Mattermost feature labels </getting-started/feature-labels>` documentation for details on the status, maturity, and support level of each feature, and what you can expect at each level.
