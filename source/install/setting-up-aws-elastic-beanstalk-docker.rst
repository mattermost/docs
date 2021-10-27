..  _docker-ebs:

AWS Elastic Beanstalk Docker Setup
==================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The following instructions use Docker to install Mattermost in *Preview Mode* for exploring product functionality. This configuration should not
be used in production.

The Elastic Beanstalk application creation process used here is the easy *Getting Started* approach which combines Application and Environment creation in the same flow. 

1.  From your `AWS console <https://console.aws.amazon.com/console/home>`__ select **Compute > Elastic Beanstalk**.
2.  Click the **Create Application** button on the Elastic Beanstalk home page.
3.  Type a name for the Elastic Beanstalk application in the field for **Application name**.
4.  Provide any **Application tags**, this is optional.
5.  Select **Docker** for the Platform.
6.  Choose **Docker running on 64bit Amazon Linux 2** for Platform branch. NOTE: Multi-container Docker is now deprecated.
7.  The platform version is preselected to **3.4.8 (Recommended)**, make no changes here.
7.  For **Application code**, select **Upload your code**.
8.  Download the ``Dockerrun.aws.json`` file from
    https://raw.githubusercontent.com/mattermost/mattermost-docker-preview/master/Dockerrun.aws.json.
9.  Set a unique **Version Label**, choose **Local File** and then click **Choose file** button to browse for the downloaded file in the previous step. You should see a *File successfully uploaded* message.
10. Click **Create Application**.
11. It may take a few minutes for Beanstalk to launch your environment. If the launch is successful, you will see a see a large green checkmark and the **Health status** displays in “Green”.
12. Test your environment by clicking the domain link next to your application name at the top of the dashboard. Alternatively, enter the domain into your browser in the form of ``http://<your-ebs-application-url>.elasticbeanstalk.com``. You can also map your own domain if you wish. If everything is working correctly, the domain should navigate you to the Mattermost signup page. Enjoy exploring Mattermost!

Configuration Settings
----------------------

See `Configuration Settings <https://docs.mattermost.com/administration/config-settings.html>`__ documentation to customize your deployment.

(Recommended) Enable Email
--------------------------

The default Docker instance for Mattermost is designed for product evaluation, and sets ``SendEmailNotifications=false`` so the product can function without enabling email. To see the product's full functionality, enabling SMTP email is recommended.

.. include:: ../configure/smtp-email.rst
	:start-after: How to Enable Email
