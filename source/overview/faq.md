# Frequently Asked Questions 

#### Why was Mattermost created? 

To offer an alternative to propreitary SaaS services. For more info, please go to mattermost.org and click "Why we made Mattermost".

#### Can I use Mattermost to create a propretary SaaS service?

We prefer you didn't. For more info, please go to mattermost.org and click "Why we made Mattermost".

## Enterprise Edition

#### What is Mattermost Enterprise Edition? 

Mattermost Enteprise Edition is a commercial workplace messaging solution for enterprises built atop the open source Mattermost platform. It is currently available as a "pre-release" by [contacting the Enterprise team.](https://about.mattermost.com/contact/)

The most recent verson includes LDAP/AD single-sign-on, auditing and advanced reporting for enterprises. It's feature set and roadmap are being determined in collaboration with early customers deploying and sharing feedback on the pre-release version. 

#### How can I be assured that my data will not be locked in to commercial software? 

Users of Mattermost Enterprise Edition can downgrade to the open source version without losing any data. Moreover, you always have control over your server and database, where the entirety of your Mattermost deployment is stored. 

#### How does Mattermost scale from teams to enterprises?

Growing your Mattermost installation from supporting a team to supporting an enterprise requires two types of scaling: 

1. Technical scaling - maintaining system responsiveness as large quantities of new users are added
2. Functional scaling - adding advanced features to support the increased complexity of large organizations

**Technical Scaling** - Whether used for teams or enterprises, the Mattermost platform is designed to support tens of thousands of users on a single server with appropriate hardware. The platform is built using Golang, the language developed by Google to create internet-scale applications, and supports highly scalable databases like MySQL, which is [used extensively by Facebook](https://www.facebook.com/notes/facebook-engineering/mysql-and-database-engineering-mark-callaghan/10150599729938920/). Beyond tens of thousands of users,  Mattermost Enterprise Edition can offer high availability/horizontal scaling configurations using multiple servers to support even larger organizations. 

**Functional Scaling** - Scaling from a team to an enterprise is like going from a "virtual office" to a "virtual campus" (which may include many virtual offices). Features enterprise authentication, granular permissions, compliance and auditing, and advanced reporting become increasingly important as organizations grow beyond teams. Organizations needing this flexibility can easily upgrade from Mattermost Team Edition to Mattermost Enterprise Edition, as well as downgrade without data loss, should their needs change. 

For more information on how Mattermost scales, technically and functionality, please [contact the Enterprise team.](https://about.mattermost.com/contact/)

