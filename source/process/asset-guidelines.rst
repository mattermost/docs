============================================================
Mattermost Asset Guidelines
============================================================

The following guidelines are intended to help queue and prepare marketing assets for community projects by the Mattermost core committers and the Mattermost community.

.. contents::
    :backlinks: top

Queuing Assets for New Community Projects
------------------------------------------

Follow these steps to queue an asset for a new community project.

Integrations and Installers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you find a new integration or installer in the `Mattermost Facebook page <https://www.facebook.com/MattermostHQ/?fref=ts>`_, `Mattermost Twitter page <https://twitter.com/mattermosthq>`_, `GitHub <https://github.com/search?utf8=%E2%9C%93&q=mattermost>`_ or elsewhere you feel Mattermost should promote:

1. Post a request to the `Contributors team "Integrations and Apps" channel <https://pre-release.mattermost.com/core/channels/integrations>`_ with:

  - mention to @jason
  - link to suggested integration
  - link to creator's GitHub profile, if applicable

    Example:

    .. code-block:: none

      @jason Here is [Matterbridge](https://github.com/42wim/matterbridge) from [42wim](https://github.com/42wim), which is a sample bridge between Mattermost, IRC, XMPP, Gitter and Slack.
      
      Is this something Mattermost would like to promote?

2. If the proposal is accepted, Ops reaches out to the integration creator by opening a GitHub issue with the following text:

    .. code-block:: none

      Title: 

      Share your work with Mattermost community?

      Body: 

      Hi @{GitHub_username}, 

      We came across your work and we'd love to help share it with the Mattermost community.

      If this interests you, we wondered if you'd help complete a form to tell us more about your work so we can promote it? 
      
      Here's the form: https://spinpunch.wufoo.com/forms/mattermost-integrations-and-installers/
      
      We'd also like to welcome you to join our public integrations community channel on our nightly build server: https://pre-release.mattermost.com/core/channels/integrations

      Thanks for being a valued member of the Mattermost Community!

      - The Mattermost Team

3. When a contributor submits an integration via the `Wufoo form <https://spinpunch.wufoo.com/forms/mattermost-integrations-and-installers/>`_, a Zapier webhook posts relevant information into the `Integrations and Apps channel <https://pre-release.mattermost.com/core/channels/integrations>`_.

4. Ops replies to each new Wufoo post with a numbered project title and project status. Example:

    .. code-block:: none

      #### 64) Cloud Foundry Integration (work queued)

Media Articles
^^^^^^^^^^^^^^^

When a relevant article on Mattermost is found in the news, add a new entry into `this Google document <https://docs.google.com/document/d/1kwCmn6JYeORdLV0noIk4iaxZx0iqR6OWUuzw5cZl6rA/edit>`_ and follow the process specified there.

Step-by-Step Asset Creation Guide for Artists
----------------------------------------------

Follow these steps to create an asset for integration or feature promotion, integration blog tweet, or user award tweet.

Integration or Feature Promotion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Use this `template <https://www.dropbox.com/s/9o6c331u815mflp/20160118_spanish.tif?dl=0>`_ as a starting point
2. Change text in the "title" layer following the guidelines in `Feature Title`_
3. Change text in the "by cburns" layer to replace the name with appropriate creator name following the guidelines in `Feature Creator`_
4. Change the contents of the "Left Image" layer to update representative art following the guidelines in `Feature Representative Art`_
5. Change the contents in the "right image" layer to update representative logo(s) following the guidelines in `Mattermost and Representative Logos`_
6. Save the finished asset draft in both .TIF and .PNG format, and upload to your "Dropbox Share" folder

Integration Blog
^^^^^^^^^^^^^^^^^

Occasionally a blog post will be written to further promote an integration. Follow these steps to create a marketing asset promoting said blog entry:

1. Use this `template <https://www.dropbox.com/s/w832mo3tgxjreb5/20160207_blog_puppet.tif?dl=0>`_ as a starting point
2. Change text in the "title" layer to read “Meet the Creator:”, followed by the proper integration name
3. Change text in the "by liger1978" layer to the integration creator's name
4. Change the contents in the "right image" layer to include proper representative logo, followed by a split with the blue Mattermost logo. This helps create the message that it’s the representative and Mattermost together
5. Obtain a photo of the integration creator, apply a Wall Street Journal “Hedcut” effect, and update the "Left Image" layer. A helpful tutorial for how to achieve the "Hedcut" effect can be found `here <http://www.alleba.com/blog/2006/12/20/photoshop-tutorial-the-hedcut-effect/>`_
6. Save the finished asset draft in both .TIF and .PNG format, and upload to your "Dropbox Share" folder

User Award
^^^^^^^^^^^

Occasionally a blog post will be written to recognize a member for their contributions to Mattermost. Follow these steps to create a marketing asset promoting said blog entry:

1. Use this `template <https://www.dropbox.com/s/311qq6d17zvyhtj/20161118_minio_hackertoberfest.tif?dl=0>`_ as a starting point
2. Change text in the "title" layer to update the user being recognized, the event, and contribution or integration made
3. Change the contents in the "right image" layer to include proper representative logo and/or a picture of the user being recognized
4. Change the contents of the "Left Image" layer to update text with proper event name and match color to logo in the right pane
5. Save the finished asset draft in both .TIF and .PNG format, and upload to your "Dropbox Share" folder

Asset Elements
---------------

The following include guidelines for specific elements of an asset.

Feature Title
^^^^^^^^^^^^^^

1. Appears in the bottom right corner of the asset
2. Title should "communicate the benefit" of the work, while referencing its name, followed by "for Mattermost"
  
  - Sometimes the title is a straightforward description of an app that can now connect to Mattermost, like "Jira integration for Mattermost"
  - Sometimes the title needs to be non-standard, like "Gitter integration for Mattermost via Matterbridge"

3. Title should be sentence case
4. Short titles are better than longer titles

Feature Creator
^^^^^^^^^^^^^^^^

1. Appears in the bottom left corner of the left "representative art" pane
2. Displays who created the integration (Twitter or GitHub account of the creator)
3. If text doesn’t blend well with left pane representative art, adjust the outer glow effect

Feature Representative Art
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Representative art appears in the left pane of the asset
2. Screenshot of a feature in action is most preferred (see guidelines for `Feature Screenshot`_ here)
3. If no feature screenshot is available, take a screenshot of a well-formatted "README" file or of feature code with the word "Mattermost"

  - If using a "README" file, ensure the screenshot doesn't highlight spelling or capitalization errors

4. If necessary, consider using a two-image, half-and-half combination of the README and feature code to provide a visually appealing color inversion. See `example <https://www.dropbox.com/s/bqh564rpkshf08n/20160122_github_integration.png?dl=0>`_

  - When creating a two-image representative art piece, ensure that the top section is continuous and flat to avoid a triangular blank space

5. Place and size representative art in a way that it doesn’t clash with the `Feature Creator`_ layer
6. Leave a 17px border of white space in between representative art and banner edge
7. Have equal margins on the left side and above the image
8. Leave equal whitespace between all like objects
9. Avoid wavy lines when rotating an image as shown in the sample below

  .. image:: ../images/asset-guidelines-wavy-lines.png

  - To avoid them, increase the size of the original layer, rotate it, then reduce the size of the image

10. If you use a rotated image, avoid visible gaps between the edge of the banner and the image as shown in the sample below

  .. image:: ../images/asset-guidelines-visible-gaps.png

11. Colored shading on the left pane should match the primary colors of the logo in the right pane
12. Adjacent areas of light and dark should always have a separator, or have a shading so that the areas don't bleed into the background
13. If a logo is used, ensure it follows the same guidelines from `Mattermost and Representative Logos`_ section

Feature Screenshot
^^^^^^^^^^^^^^^^^^^

When taking a screenshot of a feature, follow these guidelines:

1. **Complete**: Profile pictures and real people names should be filled out. Use either in-house art, free or purchased clip art
2. **Authentic**: Try to model a real world interaction. If you're modifying the image such as changing username and profile picture, make sure to do it throughout the image
3. **Oversized**: Provide screenshots that are at least 20-30% larger than needed, so that there's room to rotate and crop the image as needed
4. **Illustrative**: Try to find screenshots that are representative of the feature

Mattermost and Representative Logos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Mattermost logo appears in the bottom left corner of the asset
2. Representative logo appears in the right pane

  - If we're promoting a Mattermost feature, not an integration, use Mattermost white logo on blue background
  - If representative logo is from a product, find a logo with the product name, not just the image when possible. Example:

  Correct: 
  
  .. image:: ../images/asset-guidelines-gitter-correct.png

  Incorrect: 
  
  .. image:: ../images/asset-guidelines-gitter-incorrect.png

  - Ensure representative logo is similar in size to other logos shown in `Twitter ad examples <https://www.dropbox.com/sh/13h55hakbvm7iva/AAARooC0rV8JCKBI_8VUj_tga?dl=0>`_

3. If no representative logo exists, use `this template <https://www.dropbox.com/s/9ck2ldoaizb8hvr/20170118_trax.tif?dl=0>`_ as a starting point to create a new custom one:

  - Change the size of font so the name fits within the guides shown in reference screenshot below

  .. image:: ../images/asset-guidelines-no-logo.png

  - Text of name should be at least as wide as "for Mattermost"
  - The space between the bottom of the integration name and "for Mattermost" should be the same distance as in the reference screenshot above
  - Vertically center the combined image of the integration name and the text "for Mattermost"

Step-by-Step Asset Review Guide for Ops
----------------------------------------

1. Upload the artists "work in progress" files to the `Archive Dropbox sub-folder <https://www.dropbox.com/home/marketing/Twitter/archive>`_ in `Twitter Marketing <https://www.dropbox.com/sh/13h55hakbvm7iva/AAARooC0rV8JCKBI_8VUj_tga?dl=0>`_
2. In the `Contributors team <https://pre-release.mattermost.com/core/channels/integrations>`_, find the appropriate conversation thread for the queued project, and add a comment mentioning @jason with the following:

  - Link to the image in Dropbox
  - Proposed tweet text with a note to specify whether or not the mention in the text is the Twitter handle of the user. 

    - `@username is the Twitter account of the GitHub user` if the text uses a Twitter username, or
    - `@username is NOT the Twitter account of GitHub user` if the text doesn't use a Twitter username

  - Proposed scheduled tweet date

    - Never schedule a tweet for the 16th or 22nd of any given month as these days are reserved for Mattermost and GitLab release announcements, respectively

  - .png version of the file for a quick preview
