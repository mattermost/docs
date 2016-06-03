Custom Branding Tools
=====

Available in `Enterprise Edition E10 and higher <https://about.mattermost.com/pricing/>`_.

Use custom branding tools to present a Mattermost experienced tailored to the branding of your organization. 

.. figure:: images/custom-branding-tools.PNG

Enable Custom Branding
-----

After purchasing and installing a license key for Enterprise Edition E10 or E20:

1. Go to **System Console** > **Customization** > **Custom Branding** and set the value to ``true``.
2. Choose a **Site Name**, upload a **Custom Brand Image** and write **Custom Brand Text**.
3. Click **Save**.

Users should see your new custom branding on the login page of your Mattermost server the next time they sign-in. 

More about settings available in **Customer Branding Tools**:

Site Name
`````
Choose the name of your Mattermost site to be shown in the UI. The site name appears in the header and footer of the site login page, team selection page, team creation page, account creation page, and email invitations. Note that the site name applies to the entire site and not just a specific team on the site. It is recommended to limit your site name to 30 characters or less.

Custom Branding Image
`````
Upload a company logo or custom image representative of your site that is displayed on the left side of the site login page. Supported image formats are JPG, PNG, TIFF and BMP. The recommended image size is 200-500px in width and height, and less than 2 MB since it is loaded for every user who logs in on desktop.


Custom Brand Text
`````
Write custom text to display your company tagline or a welcome prompt. Custom text will be shown below the custom brand image on the left side of site login page on desktop. You can format this text to a maximum of 500 characters using the same `Markdown formatting syntax <http://docs.mattermost.com/help/messaging/formatting-text.html>`_ as used in Mattermost messages.
