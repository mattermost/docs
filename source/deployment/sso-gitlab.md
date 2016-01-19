# Configuring Single-Sign-On
___
Single-Sign-On can be configured with the following services.

## GitLab 

Follow these steps to configure Mattermost to use GitLab as a single-sign-on (SSO) service for team creation, account creation and sign-in.

1. Login to your GitLab account and go to the Applications section either in Profile Settings or Admin Area.
2. Add a new application called "Mattermost" with the following as Redirect URIs:
    * `<your-mattermost-url>/login/gitlab/complete` (example: http://localhost:8065/login/gitlab/complete)
    * `<your-mattermost-url>/signup/gitlab/complete`
  
    (Note: If your GitLab instance is set up to use SSL, your URIs must begin with https://. Otherwise, use http://).

3. Submit the application and copy the given _Id_ and _Secret_ into the appropriate _GitLabSettings_ fields in config/config.json

4. Also in config/config.json, set _Enable_ to `true` for the _gitlab_ section, leave _Scope_ blank and use the following for the endpoints:
    * _AuthEndpoint_: `https://<your-gitlab-url>/oauth/authorize` (example https://example.com/oauth/authorize)  
    * _TokenEndpoint_: `https://<your-gitlab-url>/oauth/token`  
    * _UserApiEndpoint_: `https://<your-gitlab-url>/api/v3/user`  
  
    Note: Make sure your `HTTPS` or `HTTP` prefix for endpoint URLs matches your server configuration. 

5. (Optional) If you would like to force all users to sign-up with GitLab only, in the _ServiceSettings_ section of config/config.json set _DisableEmailSignUp_ to `true`.

6. Restart your Mattermost server to see the changes take effect.

## Unofficial Single-Sign-On

Given the similarities of GitHub and GitHub Enterprise authentication mechanisms to GitLab, Mattermost offers "unofficial" support for GitHub and GitHub Enterprise. Each of the standards should work using the GitLab user interface, but the user interface will visually display GitLab icons and wording rather than GitHub or GitHub Enterprise.  

Instructions for unofficial GitHub and GitHub Enterprise authentication setup are as follows: 

### GitHub (unofficial)

Follow these steps to configure Mattermost to use Github as a single-sign-on (SSO) service for team creation, account creation and sign-in using the GitLab SSO interface.

1. Login to your GitHub account and go to the Applications section in Profile Settings.
2. Add a new application called "Mattermost" with the following as Authorization callback URL:
    * `<your-mattermost-url>` (example: http://localhost:8065)

3. Submit the application and copy the given _Id_ and _Secret_ into the appropriate _GitLabSettings_ fields in config/config.json

4. Also in config/config.json, set _Enable_ to `true` for the _gitlab_ section, leave _Scope_ blank and use the following for the endpoints:
    * _AuthEndpoint_: `https://github.com/login/oauth/authorize`
    * _TokenEndpoint_: `https://github.com/login/oauth/access_token`
    * _UserApiEndpoint_: `https://api.github.com/user`

6. (Optional) If you would like to force all users to sign-up with GitHub only,
in the _ServiceSettings_ section of config/config.json set _DisableEmailSignUp_
to `true`.

6. Restart your Mattermost server to see the changes take effect.

7. Tell the users to set their public email for GitHub at the [Public profile page](https://github.com/settings/profile). Mattermost uses the email to create account.

### GitHub Enterprise (unofficial)

Follow these steps to configure Mattermost to use Github Enterprise as a single-sign-on (SSO) service for team creation, account creation and sign-in using the GitLab SSO interface.

1. Login to your GitHub Enterprise account and go to the Applications section in Profile Settings.
2. Add a new application called "Mattermost" with the following as Authorization callback URL:
    * `<your-mattermost-url>` (example: http://localhost:8065)

3. Submit the application and copy the given _Id_ and _Secret_ into the appropriate _GitLabSettings_ fields in config/config.json

4. Also in config/config.json, set _Enable_ to `true` for the _gitlab_ section, leave _Scope_ blank and use the following for the endpoints:
    * _AuthEndpoint_: `https://<your-github-enterprise-url>/oauth/authorize` (example https://github.com/oauth/authorize)
    * _TokenEndpoint_: `https://<your-github-enterprise-url>/oauth/access_token`
    * _UserApiEndpoint_: `https://<your-github-enterprise-url>/api/v3/user`

5. (Optional) If you would like to force all users to sign-up with GitHub Enterprise only, in the _ServiceSettings_ section of config/config.json set _DisableEmailSignUp_ to `true`.

6. Restart your Mattermost server to see the changes take effect.

