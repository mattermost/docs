AWS Elastic Beanstalk Docker setup
==================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

The following instructions use Docker to install Mattermost in *Preview Mode* for exploring product functionality. This configuration should not
be used in production.

The Elastic Beanstalk application creation process used here is the easy *Getting Started* approach which combines Application and Environment creation in the same flow. 

1.  From your `AWS console <https://console.aws.amazon.com/console/home>`__ select **Elastic Beanstalk**.
2.  Select the **Create Application** button on the Elastic Beanstalk home page.
3.  Enter an **Application name** for the Elastic Beanstalk application.
4.  (Optional) Specify **Application tags**.
5.  Select **Docker** for the Platform.
6.  Choose **Docker running on 64bit Amazon Linux 2** for the **Platform** branch. Note that multi-container Docker is now deprecated.
7.  Leave the platform version preselected as **3.4.8 (Recommended)**.
8.  For **Application code**, select **Upload your code**.
9.  Download the ``Dockerrun.aws.json`` file from
    https://raw.githubusercontent.com/mattermost/mattermost-docker-preview/master/Dockerrun.aws.json.
10.  Set a unique **Version Label**, choose **Local File**, then select **Choose file** button to browse for the downloaded file in the previous step. You should see a *File successfully uploaded* message.
11. Select **Create Application**. It may take a few minutes for Beanstalk to launch your environment. If the launch is successful, you will see a see a large green checkmark and the **Health status** displayed in green.
12. Test your environment by selecting the domain link next to your application name at the top of the dashboard. Alternatively, enter the domain into your browser in the form of ``http://<your-ebs-application-url>.elasticbeanstalk.com``. You can also map your own domain if you prefer. When everything is working correctly, the domain navigates you to the Mattermost Login page. Enjoy exploring Mattermost!

Configuration Settings
----------------------

See :doc:`Configuration Settings </configure/configuration-settings>` documentation to customize your deployment.

(Recommended) Enable Email
--------------------------

The default Docker instance for Mattermost is designed for product evaluation, and sets ``SendEmailNotifications=false`` so the product can function without enabling email. To see the product's full functionality, enabling SMTP email is recommended.

.. include:: ../configure/smtp-email.rst
	:start-after: How to enable email
