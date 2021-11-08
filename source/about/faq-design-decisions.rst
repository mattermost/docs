Design Decision Questions
=========================

Why does Mattermost disclose whether or not an account exists when a user enters an incorrect password?
-------------------------------------------------------------------------------------------------------

Mattermost's core design principle is to be "fast, obvious, forgiving" and, telling users that they made a mistake in entering their password, is in service of our principle of prioritizing user interests.

When using username-password authentication, especially with AD/LDAP, there's the possibility of usernames being email addresses, Mattermost username, AD/LDAP username, AD/LDAP ID, or other AD/LDAP attributes and our design principle intends to help end users understand whether their login error came from having the wrong password or the wrong email/username.

We believe this design increases productivity, speeds up user adoption, and reduces help desk tickets and support costs - and that these benefits outweigh the trade-offs.

The trade-off with this design is that if physical security is not in effect, network security is not in effect (i.e., no VPN or a malicious user within the private network), and username-password authentication is used, an attacker may be able to enumerate email addresses or usernames by sending HTTP requests to the system, up to the maximum number of requests per second defined in Mattermost's `API rate limiting settings <https://docs.mattermost.com/configure/configuration-settings.html#rate-limiting>`__.

For organizations who choose to deploy in such a configuration, please consider the following mitigations:

1. Instead of username-password, use a Single Sign-On (SSO) provider in Mattermost Enterprise Edition like OneLogin, Okta, or ADFS, or use the open source GitLab SSO option available with Mattermost Team Edition.
2. Per the recommended install instructions, use a VPN client to apply network security to your deployment.
3. Enable monitoring and alerting from your proxy server to detect and isolate malicious behavior reaching your deployment.

Above all, make sure to subscribe to the `Mattermost Security Bulletin <https://mattermost.com/security-updates/#sign-up>`__ and apply security patches as recommended.