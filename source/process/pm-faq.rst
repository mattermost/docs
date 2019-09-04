Product Manager FAQ
===================

Can we take this feature out of beta?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To officially release a feature, it should meet the following criteria: 

1. Scalable: Works for 60k concurrent connections, 60M rows in the database, and in High Availability
2. Cross Platform: Works on all web view sizes, mobile apps, desktop apps
3. Measurable: Telemetry added where appropriate 
4. Documented: Complete documentation is available
5. Secure: Reviewed internally for security, and included in future security reviews 
6. Accessible: Accessibility has been added for user interface components
7. Logged: Audit log entries have been added to allow system admins to troubleshoot issues
8. Compliant: Anything needed for compliance is tracked in logs


How to create redirects for in-product documentation? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentation that is linked in-product should always use a redirect from www.mattermost.com instead of the docs.mattermost.com site, to ensure links are not broken in the event that they are moved on the docs site. 

To set up a redirect, you must have admin access to www.mattermost.com.  Marketing can assist with this access or @jason.blais or @katie.wiersgalla can add a redirect for you. 

If you have access, follow these steps: 

1. Log in to the administration panel for www.mattermost.com.
2. From the left-hand sidebar, go to **SEO > Redirects**.
3. On the top of the screen, ensure you are on the **Redirects - Yoast SEO** page header on the **Redirects** tab.
4. Under **Type**, choose ``301 Moved Permanently`` option (this is the default option).
5. In the **Old url** field, enter in the new direct you want to use in-product in the format of ``/pl/default-page-description``. Update the page description with your page information. 
6. In the **Url** field, enter in the full URL to the page on docs.mattermost.com. 
7. Click the **Add Redirect** botton and verify your entry is added to the list. You may need to page through to find your entry.
8. Test your redirect URL.  This will be the URL in the format of ``https://www.mattermost.com/pl/default-page-description.html``.
