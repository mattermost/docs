============================================================
Mattermost Asset Guidelines
============================================================

The following guidelines are intended to help queue and prepare marketing assets for community projects by the Mattermost core committers and the Mattermost community.

.. contents::
    :backlinks: top

Queuing Assets for New Community Projects
------------------------------------------

Follow these steps to queue an asset for a new community project:

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

Follow these steps to create an asset for integration or feature promotion or for guest blog posts.

You can find sample templates `in this Google drive <https://drive.google.com/open?id=0Bx-9w8QDFlfcbUh2bGdkRElJaWs>`_.

Integration or Feature Promotion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Use this `template (dark background) <https://www.dropbox.com/s/a8tbqxiik1m9i8u/20170717_template_dark.tif?dl=0>`_ or this `template (light background) <https://www.dropbox.com/s/codoct7np20fx3l/20170717_template_light.tif?dl=0>`_ as a starting point.
2. Update the title following the guidelines in `Feature Title`_.
3. Update the footer and the creator name following the guidelines in `Feature Footer`_ and in `Feature Creator`_.
4. Update representative art following the guidelines in `Feature Representative Art`_.
5. Update representative logo(s) following the guidelines in `Mattermost and Representative Logos`_.
6. Add a 1 pixel grey stroke border around the rectangular boundary of the banner.
7. Save the finished asset draft in both .TIF and .PNG format, and upload to your "Dropbox Share" folder.

Guest Blog Posts
^^^^^^^^^^^^^^^^^

1. Use this `template <https://drive.google.com/file/d/0Bx-9w8QDFlfcQURoRnF1YllZWWc/view?usp=sharing>`_ as a starting point.
2. Update the title following the guidelines in `Feature Title`_.
3. Update representative logo following the guidelines in `Mattermost and Representative Logos`_.
4. Obtain a photo of the guest company member and apply a gray-scale effect. You can also consider applying a `Puppet Module effect <https://www.mattermost.org/puppet-module-for-mattermost/>`_.
5. Add a 1 pixel grey stroke border around the rectangular boundary of the banner.
6. Save the finished asset draft in both .TIF and .PNG format, and upload to your "Dropbox Share" folder.

Asset Elements
---------------

The following include guidelines for specific elements of an asset.

Feature Title
^^^^^^^^^^^^^^

1. Appears in the top left corner of the asset.
2. Title should "communicate the benefit" of the work, while referencing its name.
  
  - Sometimes the title is a straightforward description of an app that can now connect to Mattermost, e.g. "New Update for Desktop App".
  - Sometimes the title needs to be non-standard, e.g. "Gitter integration for Mattermost via Matterbridge".

3. Aim to fit title on two lines. If title is too long, move Feature Representative Art more to the right of the banner to ensure that there is still at least 64px of width between Feature Title and Feature Representative Art.
4. Title should always be in title case.
5. Short titles are better than longer titles.

Feature Footer
^^^^^^^^^^^^^^^^

1. When the background of the banner is blue, the footer should be black. When the background is white, the footer should be blue.
2. Displays who created the integration (Twitter or GitHub account of the creator). See the next section for further instructions.
3. If the text doesn’t blend well with left pane representative art, adjust the outer glow effect.

Feature Creator
^^^^^^^^^^^^^^^^

1. Appears in the bottom right corner of the asset footer.
2. Text in footer should use GitHub username in lowercase, or company/person name in capital case i.e. ``by matterhorn-chat`` or ``by Galois, Inc.``.

Feature Representative Art
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Representative art appears in the right side of the asset.
2. Screenshot of a feature in action is most preferred (see guidelines for `Feature Screenshot`_ and `Screenshot Development of Mattermost User Interface`_.
3. If no feature screenshot is available, take a screenshot of a well-formatted "README" file or of feature code with the word "Mattermost". If using a "README" file, ensure the screenshot doesn't highlight spelling or capitalization errors.
4. Change the color of the background based on the color of the screenshot. If the screenshot is light, use a dark background. If the screenshot is dark, use a light background.
5. Screenshot should not take up more than 40% of the banner width.
6. Follow these guidelines on spacing:

  - Ensure there is around 31px of “white space” between the contents of the screenshot and the edge of the screengrab. (This can be adjusted by resizing the rectangle layer below the screengrab in Photoshop).
  - Ensure there is at least 64px of width between the copy title and the edge of the screengrab.
  - There should be around 60px of space between the top edge of the screengrab and top edge of the banner. (Give or take 10px considering the diagonal of the screengrab).

6. Leave equal whitespace between all like objects.
7. Avoid wavy lines when rotating an image. To avoid them, increase the size of the original layer, rotate it, then reduce the size of the image.
8. Adjacent areas of light and dark should always have a separator, or have a shading so that the areas don't bleed into the background.
9. Add a 1px grey border and a drop shadow around the screenshot.

Mattermost and Representative Logos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Mattermost logo appears in the bottom left corner of the asset.
2. Use white Mattermost logo on dark backgrounds and black Mattermost logo on light backgrounds.
3. Representative logo appears on the left side of the asset below the feature title.
4. For representative logos, always confirm you are using the official version of the company’s logo. If you’re unsure, ask.
5. The space between the feature title and the representative logo should be 35px.
6. When the background color is dark, use the white/inverted version of representative logo. When the background color is light, use the dark/primary version of representative logo.
7. If the color of the representative logo is the same as the color of the title, make sure to make them distinctive from each other by slightly reducing the size of the logo.

Feature Screenshot
^^^^^^^^^^^^^^^^^^^

When taking a screenshot of a feature, follow these guidelines:

1. **Complete**: Profile pictures and real people names should be filled out. Use either in-house art, free, or purchased clip art. If you're modifying the image such as changing username and profile picture, make sure to do it throughout the image. Don't show any bugs or UX defects in the product and use the "Mattermost" theme when appropriate.
2. **Authentic**: Try to model a real world interaction. When possible, highlight DevOps use cases since they are familiar to the majority of our users.
3. **Oversized**: Provide screenshots that are at least 20-30% larger than needed, so that there is room to rotate and crop the image as needed.
4. **Illustrative**: Try to find screenshots that are representative of the feature.
5. **Easy to follow**: The screenshot should be easy to understand at a glance. Avoid using short forms or acronyms in conversations, and choose images that are clear.

Screenshot Development of Mattermost User Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The purpose is to highlight and illustrate the best features of Mattermost user interface.

To choose the best screenshot image, follow this order: an end-user screenshot that best illustrates the feature > screenshot of System Console or other settings help text > screenshot of documentation > screenshot of a code mentioning the feature and/or Mattermost.

Setup
~~~~~~~~~~~~~

- Use the Mattermost Desktop app, which has a nicer border.
- Create a secondary account with [first.last]+blah@mattermost.com email address. This makes triggering notifications for yourself easier (for the screenshot). You can also use a second browser to login to the second account while taking the screenshot.

Checklist
~~~~~~~~~~~~~

- Screen size: Provide screenshots that are 20-30% larger than needed - this will make it easier for the screenshot to be included in blog posts, documentation, and others. To do this, close the right-hand sidebar and shrink your screen horizontally to make it narrower, leaving the screen wide enough until the "mobile send button" no longer appears in the bottom-right corner. Make sure not to cut off any sides of the page in the screenshot.
- Left-hand side: Include Favorite, Public, and Private channels on the left-hand side. Make sure that you scroll all the way to the top in the channel list on the left-hand side for the screenshot.
- Favorites channel list: Include one Public channel, a Direct Message channel with someone who is online, as well as a Group Direct Message channel using people with short names to avoid truncation.
- Center pane: Make the center pane one of the Favorited channels. Make sure that the heading of the center pane is fully visible to avoid truncation. Also, make the first message in the center pane fully visible right below the channel header.
- Profiles: Profile pictures and real people's names should be filled out throughout the screenshot. For the profile picture, use either normal-looking Avatars or stock photography.
- Clarity: Do not include an "unread posts" indicator in the left-hand side, but you can have a few mentions. Also, avoid showing any text with acronyms and abbreviations. Do not show any bugs or defects. Make sure that the area of focus is big enough to read in blog posts, documentation, and others.
- Outline: Ensure that the screenshot has a grey outline so that it looks good on both dark and light backgrounds.
- Outstanding look: Ensure that the contents of the screenshot shows the Mattermost product in the best light.
   
   - Show the feature in action.
   - Make sure that the screenshot is positive - give whoever is viewing it a positive emotion.
   - Show how the feature can be extended and customized. For instance, use custom slash commands instead of the default commands.

Animated GIFs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Animated GIFs with two images that look very similar should not be created since visually it looks like a mistake.

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
