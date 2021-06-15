..  _docker-ebs:

AWS Elastic Beanstalk Docker Setup
==================================

The following instructions use Docker to install Mattermost in *Preview
Mode* for exploring product functionality. This configuration should not
be used in production.

1.  From your `AWS console <https://console.aws.amazon.com/console/home>`__ select **Compute > Elastic Beanstalk**.
2.  Select **Create New Application** from the top right.
3.  Name your Elastic Beanstalk application and click **Next**.
4.  On the New Environment page, select **Create web server** .
5.  If asked, select **Create an IAM role and instance profile**, then click **Next**.
6.  On the **Environment Type**:

    a. Set Predefined Configuration to **Multi-Container Docker** under the generic heading in the drop-down list.
    b. Set Environment Type to **Single instance** in the drop-down list.
    c. Click **Next**.

7.  For **Application Source**, select **Upload your own** and upload the ``Dockerrun.aws.json`` file from
    https://raw.githubusercontent.com/mattermost/mattermost-docker/master/contrib/aws/Dockerrun.aws.json (select the version you'd like to use), then click **Next**.
8.  Type an Environment Name and URL. Make sure the URL is available by clicking **Check availability**, then click **Next**.
9.  The options on the **Additional Resources** page may be left at default unless you wish to change them. Click **Next**.
10. On the **Configuration Details** page:

    a. Select an Instance Type of **t2.small** or larger.
    b. The remaining options may be left at their default values unless you wish to change them. Click **Next**.

11. **Environment tags** may be left blank. Click **Next**.
12. Review your information, then click **Launch**.
13. It may take a few minutes for Beanstalk to launch your environment. If the launch is successful, you will see a see a large green checkmark and the **Health status** displays in “Green”.
14. Test your environment by clicking the domain link next to your application name at the top of the dashboard. Alternatively, enter the domain into your browser in the form of ``http://<your-ebs-application-url>.elasticbeanstalk.com``. You can also map your own domain if you wish. If everything is working correctly, the domain should navigate you to the Mattermost signup page. Enjoy exploring Mattermost!

Configuration Settings
----------------------

See `Configuration Settings <https://docs.mattermost.com/administration/config-settings.html>`__ documentation to customize your deployment.

(Recommended) Enable Email
--------------------------

The default Docker instance for Mattermost is designed for product evaluation, and sets ``SendEmailNotifications=false`` so the product can function without enabling email. To see the product's full functionality, enabling SMTP email is recommended.

.. include:: smtp-email-setup.rst
	:start-after: How to Enable Email
