# Mattermost Documentation

This repository generates the documentation available at https://docs.mattermost.com/

All documentation is available under the terms of a [Creative Commons License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

If you have any questions, sign up to [community.mattermost.com](https://community.mattermost.com/signup_user_complete/?id=f1924a8db44ff3bb41c96424cdc20676) and join the [Documentation](https://community-daily.mattermost.com/core/channels/documentation) channel. 

## Contributing

**Getting Started**

You can edit or create Mattermost documentation directly in GitHub or by downloading the repo onto your machine and using an editor such as Atom. Consult the [Mattermost Documentation Style Guide](https://docs.mattermost.com/guides/core.html#documentation-style-guide) and [reStructuredText Markup](https://docs.mattermost.com/process/documentation-guidelines.html#restructuredtext-markup) section for stylistic and technical guidance. 

If this is your first time contributing to Mattermost, first read the [Mattermost Contributor Agreement](https://www.mattermost.org/mattermost-contributor-agreement/) and sign it (at the bottom of the page), so you can be added to the Mattermost [Approved Contributor List](https://docs.google.com/spreadsheets/d/1NTCeG-iL_VS9bFqtmHSfwETo5f-8MQ7oMDE5IUYJi_Y/pubhtml?gid=0&single=true).


**Editing** 

The quickest way to begin is editing directly on GitHub, on your fork of the Mattermost docs repo. 

Click the **Edit** icon on the top right corner of the page you want to edit in the Mattermost documentation.

If this the first time you're contributing, click **Edit the file in your fork of this project** (pencil icon) on the top right corner to create a fork. 

## Creating Pull Requests

1. When you're ready to submit your changes, add a descriptive title and comments to summarize the changes made.
2. Select **Create a new branch for this commit and start a pull request**.
3. Check the **Propose file change** button.
4. Scroll down to compare changes with the original document.
5. Select **Create pull request**. 


## Building and Validating

If you're editing Mattermost documentation on a local machine, you can generate the HTML files from markdown in the `/source` directory to review them before you commit changes or create pull requests. 

1. Download the Mattermost docs repo onto a machine with Python installed.
2. Install [pipenv](https://docs.pipenv.org/): `pip install pipenv`. 
3. `cd` into the cloned repository.
4. Install the required packages: `pipenv install`.
5. Build: `make html` - generates files in `/build` directory.


**Additional Process for Core Committers**

These steps are to be followed only in situations of urgency or in situations where it is necessary to check that there aren't any high confidentiality issues. Otherwise the standard approval process should be followed.

1. The **Editor Review** label should be processed after merge.
2. The person conducting editor review needs to have their suggestions **merged by author**. Do this by mentioning the *community.mattermost.com* user name in the GitHub Pull Request.
3. Check weekly or bi-weekly that there are no **Editor Review** labels on closed Pull Requests.

## Installation Issues

If you can't install sphinx on MacOS try `sudo pip install sphinx sphinx-autobuild sphinx_rtd_theme --ignore-installed six`.
