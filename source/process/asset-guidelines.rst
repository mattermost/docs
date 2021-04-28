Mattermost Asset Guidelines
============================================================

.. note::
  This page is largely out-of-date and is stored for record-keeping purposes. For latest marketing processes and guidelines, see the `Mattermost Handbook <https://handbook.mattermost.com/operations/messaging-and-math>`_.

The following guidelines are intended to help queue and prepare marketing assets for community projects by the Mattermost core committers and the Mattermost community.

.. contents::
    :backlinks: top

Queuing Assets for New Community Projects
------------------------------------------

Follow these steps to queue an asset for a new community project:

Integrations and Installers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you find a new integration or installer in the `Mattermost Facebook page <https://www.facebook.com/Mattermost-2300985916642531/>`__, `Mattermost Twitter page <https://twitter.com/mattermost>`__, `GitHub <https://github.com/search?utf8=%E2%9C%93&q=mattermost>`__ or elsewhere you feel Mattermost should promote:

1. Post a request to the `Contributors team "Integrations and Apps" channel <https://community.mattermost.com/core/channels/integrations>`__ with:

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
      
      We'd also like to welcome you to join our public integrations community channel on our nightly build server: https://community.mattermost.com/core/channels/integrations

      Thanks for being a valued member of the Mattermost Community!

      - The Mattermost Team

3. When a contributor submits an integration via the `Wufoo form <https://spinpunch.wufoo.com/forms/mattermost-integrations-and-installers/>`__, a Zapier webhook posts relevant information into the `Integrations and Apps channel <https://community.mattermost.com/core/channels/integrations>`__.

4. Ops replies to each new Wufoo post with a numbered project title and project status. Example:

    .. code-block:: none

      #### 64) Cloud Foundry Integration (work queued)

Media Articles
^^^^^^^^^^^^^^^

When a relevant article on Mattermost is found in the news, add a new entry into `this Google document <https://docs.google.com/document/d/1kwCmn6JYeORdLV0noIk4iaxZx0iqR6OWUuzw5cZl6rA/edit>`__ and follow the process specified there.

Step-by-Step Asset Creation Guide for Artists
----------------------------------------------

Follow these steps to create an asset for integration or feature promotion or for guest blog posts.

You can find sample templates `in this Google drive <https://drive.google.com/open?id=0Bx-9w8QDFlfcbUh2bGdkRElJaWs>`__.

Integration or Feature Promotion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Use this `template (dark background) <https://www.dropbox.com/s/a8tbqxiik1m9i8u/20170717_template_dark.tif?dl=0>`__ or this `template (light background) <https://www.dropbox.com/s/codoct7np20fx3l/20170717_template_light.tif?dl=0>`__ as a starting point.
2. Update the title following the guidelines in `Feature Title`_.
3. Update the footer and the creator name following the guidelines in `Feature Footer`_ and in `Feature Creator`_.
4. Update representative art following the guidelines in `Feature Representative Art`_.
5. Update representative logo(s) following the guidelines in `Mattermost and Representative Logos`_.
6. Add a 1 pixel grey stroke border around the rectangular boundary of the banner.
7. Save the finished asset draft in both .TIF and .png format, and upload to your "Dropbox Share" folder.

Guest Blog Posts
^^^^^^^^^^^^^^^^^

1. Use this `template <https://drive.google.com/file/d/0Bx-9w8QDFlfcQURoRnF1YllZWWc/view?usp=sharing>`__ as a starting point.
2. Update the title following the guidelines in `Feature Title`_.
3. Update representative logo following the guidelines in `Mattermost and Representative Logos`_.
4. Obtain a photo of the guest company member and apply a gray-scale effect. You can also consider applying a `Puppet Module effect <https://mattermost.org/puppet-module-for-mattermost/>`__.
5. Add a 1 pixel grey stroke border around the rectangular boundary of the banner.
6. Save the finished asset draft in both .TIF and .png format, and upload to your "Dropbox Share" folder.

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

Feature Screenshot Development
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When taking a screenshot of a feature, use this checklist to guide your work:

1. **Profiles**: Profile pictures and real people’s names should be filled out throughout the screenshot. For the profile picture, use either normal-looking Avatars or stock photography.
2. **Content**: Show the feature in action. If you are highlighting a specific feature, try to have that screenshot focused on it rather than displaying the whole app. For example, if you are highlighting 1-1 direct message conversations, only include that conversation in your screenshot. Finally, ensure that the contents of the screenshot shows the Mattermost product in the best light - give whoever is viewing it a positive emotion.
3. **Use Cases**: Model a real world interaction. When possible, highlight DevOps use cases since they are familiar to the majority of our users.
4. **Clarity**: Avoid truncating the channel header text, or cutting off messages due to the scroll position in the center pane. All text should be fully visible.
5. **Size**: Provide screenshots that are double in size than needed - this ensures the screenshot does not rasterize on retina displays. The definite size per screenshot can vary - however, a standard will be established per type/category of the screenshot. For example, screenshots of the center pane should be 750px in size (with the shadows).
6. **Spacing**: Add additional spacing to a screenshot if necessary to highlight a feature.
7. **Calibration**: Make sure that the zoom level is at default level, and that the screenshot is not pixelated. Add a box shadow with the screenshot (0 2px 50 0 rgba(black, 0.1)), as well as a grey outline so that it looks good on both dark and light backgrounds.

Screenshot Development of Mattermost User Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Screenshot development guidelines have been moved to the `Mattermost Handbook <https://handbook.mattermost.com/operations/messaging-and-math/how-to-guides-for-m-and-m/how-to-create-screenshots-and-gifs>`_.

Animated GIFs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Animated GIFs with two images that look very similar should not be created since visually it looks like a mistake.

Step-by-Step Asset Review Guide for Ops
----------------------------------------

1. Upload the artists "work in progress" files to the `Archive Dropbox sub-folder <https://www.dropbox.com/home/marketing/Twitter/archive>`__ in `Twitter Marketing <https://www.dropbox.com/sh/13h55hakbvm7iva/AAARooC0rV8JCKBI_8VUj_tga?dl=0>`__
2. In the `Contributors team <https://community.mattermost.com/core/channels/integrations>`__, find the appropriate conversation thread for the queued project, and add a comment mentioning @jason with the following:

  - Link to the image in Dropbox
  - Proposed tweet text with a note to specify whether or not the mention in the text is the Twitter handle of the user. 

    - `@username is the Twitter account of the GitHub user` if the text uses a Twitter username, or
    - `@username is NOT the Twitter account of GitHub user` if the text doesn't use a Twitter username

  - Proposed scheduled tweet date

    - Never schedule a tweet for the 16th or 22nd of any given month as these days are reserved for Mattermost and GitLab release announcements, respectively

  - .png version of the file for a quick preview
