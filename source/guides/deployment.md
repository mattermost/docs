# Deploy Mattermost

Mattermost is an open source developer collaboration suite offering workplace messaging across web, desktop and mobile, project management, incident management and integration with toolchains and apps.

You can run Mattermost as an MIT-licensed Linux binary working with MySQL or PostgreSQL, available in [open source and commercial editions and offerings](https://docs.mattermost.com/about/deployments-and-editions.html) via cloud and self-hosted environments. 

## Cloud Deployment 

Cloud is the fastest, easiest way to try out the Mattermost suite: 

- [Mattermost Cloud](https://mattermost.com/pricing/) - To use Mattermost as a SaaS service [sign-up online](https://mattermost.com/pricing/).

## Self-Hosted Deployment 

Want 100% control of your deployment and data? Self-host Mattermost for teams of 50 to 50,000 (or more).

### Getting Started 

Here's the two fastest ways to start: 

- [Mattermost Omnibus Quick Install](https://docs.mattermost.com/getting-started/light-install.html) - Fastest, easiest self-host path with an **Ubuntu** server.

- [Local Machine Docker Preview](https://docs.mattermost.com/install/setting-up-local-machine-using-docker.html) - Preview locally on **Mac OS, Windows, Ubuntu or Fedora** using **Docker**.

Once you're deployed, learn about: 

- [Administrator tasks](https://docs.mattermost.com/getting-started/admin-onboarding-tasks.html) - Configure vital settings on your Mattermost server to prepare for end user onboarding. Customize a [Welcome email template](https://docs.mattermost.com/getting-started/welcome-email-to-end-users.html) to bring different groups in sequentially.
- [Architectural Overview](https://docs.mattermost.com/deploy/deployment-overview.html) - Understand user authentication, notifications, data management services, network connectivity, high availability architectures from 5,000 to 50,000+ users. 
- [Software and Hardware Requirements](https://docs.mattermost.com/install/software-hardware-requirements.html) - Size and plan the software and hardware you'll need to deploy in production.
- [Implementation Plan Template](https://docs.mattermost.com/getting-started/implementation-plan.html) - Use this plan template to organize a production rollout to hundreds of users, from project goals, end user groups, technical environment, deployment steps, staffing, training and support. 
- [Enterprise Roll Out Guide](https://docs.mattermost.com/getting-started/enterprise-roll-out-checklist.html) - Extend your implementation plan to a rollout to serveral thousand users with analytics, performance monitoring and performance tuning.

### Install Guides 

Install Mattermost Server and Mattermost Desktop and Mobile Applications in environments meeting [software and hardware requirements](https://docs.mattermost.com/install/software-hardware-requirements.html).

#### Server Installation 

##### Most Popular Self-Hosted Installation Guides: 

- [Mattermost Omnibus (Recommended for up to 1,000 users)](https://docs.mattermost.com/getting-started/light-install.html) - If you have root access on a clean server running **Ubuntu 18.04 or 20.04** this is the fastest, easiest self-hosted deployment option.

- [Local Machine Docker Preview (Recommended for evaluation only)](https://docs.mattermost.com/install/setting-up-local-machine-using-docker.html) - For evaluation only--Preview Mattermost locally on **Mac, Windows, Ubuntu or Fedora** using a single-node Docker image. NOTE: Should only be used for evaluation, not production use. 

- [Kubernetes Operator (Recommended for 500+ users)](https://docs.mattermost.com/install/install-kubernetes.html) - Deploy to self-hosted Kubernetes production environment or services like **Amazon EKS, Azure Kubernetes Service, Google Kubernetes Engine, DigitalOcean Kubernetes** or on self-hosted Kubernetes infrastructure. High availability mode requires [Mattermost Enterprise](https://docs.mattermost.com/about/editions-and-offerings.html#mattermost-enterprise-edition). 

##### Additional Self-Hosted Installation Guides: 

Install single-node (Preview/Evaluation mode) or multi-node (Production mode) deployments on other platforms: 

- [Ubuntu 20.04 LTS](https://docs.mattermost.com/install/installing-ubuntu-2004-LTS.html), [Red Hat Enterprise Linux 8 (RHEL 8)](https://docs.mattermost.com/install/install-rhel-8.html), [Debian Buster](https://docs.mattermost.com/install/install-debian.html), [CentOS](https://docs.mattermost.com/install/install-centos-oracle-scientific.html), [Oracle Linux](https://docs.mattermost.com/install/install-centos-oracle-scientific.html), [Scientific Linux](https://docs.mattermost.com/install/install-centos-oracle-scientific.html) 

#### Desktop and Mobile App Installation 

- [Mattermost Desktop App Setup](https://docs.mattermost.com/install/desktop-app-install.html) - Full install guide for Windows, macOS, and Linux--also see [simple instructions](https://docs.mattermost.com/install/desktop-app-install.html).
- [iOS Setup](https://docs.mattermost.com/install/install-ios-app.html) - Install iOS app on Apple iPhone, iPad, and iPod devices.
- [Android Setup](https://docs.mattermost.com/install/install-android-app.html) - Install Android app on Android phone and tablet devices. 
- [Test Mobile Push Notifications](https://docs.mattermost.com/deploy/mobile-testing-notifications.html) - Verify that push notifications can flow properly from server to mobile devices. 

#### Troubleshooting 

Need help installing on server, desktop or mobile? 
- Check out our [troubleshooting guide](https://docs.mattermost.com/install/troubleshooting.html#review-mattermost-logs) for common errors, fixes and where to find system logs. 
- Free peer-to-peer support is available in our [troubleshooting forum](https://forum.mattermost.com/c/trouble-shoot) and on our [community server](https://community.mattermost.com/core/channels/peer-to-peer-help). 
- If you have a [paid subscription to a Mattermost offering](https://docs.mattermost.com/about/editions-and-offerings.html) you can also [open support tickets online](https://support.mattermost.com/hc/en-us/requests/new). 


