# Mattermost Documentation

This repository generates the documentation available at https://docs.mattermost.com/. All documentation is available under the terms of a [Creative Commons License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

If you have any questions, sign up to [community.mattermost.com](https://community.mattermost.com/signup_user_complete/?id=f1924a8db44ff3bb41c96424cdc20676) and join the [Documentation](https://community.mattermost.com/core/channels/documentation) channel.

# Table of Contents

 * [Contributing](#contributing)
     * [Getting Started](#getting-started)
     * [Editing](#editing)
     * [Creating Pull Requests](#creating-pull-requests)
     * [Using Labels](#using-labels)
     * [Commenting on Pull Requests](#commenting-on-pull-requests)
     * [Reviewing Pull Requests](#reviewing-pull-requests)
 * [Building and Validating](#building-and-validating)

## Contributing

### Getting Started

You can edit or create Mattermost documentation directly in GitHub or by downloading the repo onto your machine and using an editor such as Atom. Consult the Mattermost [Documentation Style Guide](https://handbook.mattermost.com/operations/operations/company-processes/publishing/publishing-guidelines/voice-tone-and-writing-style-guidelines/documentation-style-guide) and [reStructuredText Markup](https://handbook.mattermost.com/operations/operations/company-processes/publishing/publishing-guidelines/voice-tone-and-writing-style-guidelines/documentation-style-guide#using-restructuredtext-markup-rst) section for stylistic and technical guidance.

If this is your first time contributing to Mattermost, first read the [Mattermost Contributor Agreement](https://www.mattermost.org/mattermost-contributor-agreement/) and sign it (at the bottom of the page), so you can be added to the Mattermost [Approved Contributor List](https://docs.google.com/spreadsheets/d/1NTCeG-iL_VS9bFqtmHSfwETo5f-8MQ7oMDE5IUYJi_Y/pubhtml?gid=0&single=true).

### Editing

The quickest way to begin is editing directly on GitHub on your fork of the Mattermost docs repo. Click the **Edit** icon on the top right corner of the page you want to edit in the Mattermost documentation.

If this is the first time you're contributing, follow these steps: 
1. Select **Fork** in the top-right corner of the GitHub page to fork the repo.
2. Navigate to file you want to edit and select the pencil icon (**Edit the file**) to open the editing interface.

### Creating Pull Requests

1. When you're ready to submit your changes, add a descriptive title and comments to summarize the changes made.
2. Select **Create a new branch for this commit and start a pull request**.
3. Check the **Propose file change** button.
4. Scroll down to compare changes with the original document.
5. Select **Create pull request**. 

### Using Labels

Labels are used to track the lifecycle and status of a pull request. Using the correct labels helps with managing workflows and ensuring that content is edited, merged and released at the correct time. Take a look at the [Labels](https://developers.mattermost.com/contribute/getting-started/labels/) page for information about how and when to use which labels.

### Commenting on Pull Requests

Once a pull request is submitted, multiple committers may comment on it and provide edits or suggestions which you can commit directly. You can also add line comments. Take a look at [Commenting on pull requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request) for more details.

### Reviewing Pull Requests

Once a pull request has been submitted and the correct label assigned, the review process begins. This includes aligning the content with the Style Guide, validating processes, and tagging any other relevant committers. You can read more about the review process and expectations [here](https://developers.mattermost.com/contribute/getting-started/code-review/). 

Once the review process is complete and depending on the type of issue it is (e.g., a typo fix vs. a new feature), the change is either merged into master and pushed immediately or merged into the release branch and pushed in alignment with the release. The branch is then deleted. 

Any merged PRs with an **Editor Review** or **Reviews Complete** label will be processed by the editor reviewer to ensure the documentation is correctly formatted at https://docs.mattermost.com/.

## Building and Validating

If you've downloaded the repo and are editing Mattermost documentation on your local machine, you can generate the HTML files from markdown in the `/source` directory. You can review them before you commit changes or create pull requests.

**Note:** Commands can be executed on Linux, Mac, and Windows (using Powershell)

1. Open a terminal window and clone the forked copy of the docs repo by running:
```sh
$ git clone https://github.com/mattermost/docs.git
```
2. Install [pipenv](https://docs.pipenv.org/) by using:     
-> for Mac users, if you have Homebrew installed
```sh
$ brew install pipenv  
```
-> for other operating systems
```python
$ pip install pipenv 
```
3. Open your terminal and navigate into the cloned repository:
```sh
$ cd docs
```
4. Install the required packages by running
```python
$ pipenv install
```
5. Build the doc set using `make html`. This generates files in `/build` directory.
6. Navigate to the `/build` directory to preview the page/s you've edited, by runnning 
```sh
$ cd /build
```

The build process may generate this error: ``WARNING: toctree contains reference to document u'foo' that doesn't have a title: no link will be generated``. It can be ignored as it does not negatively impact the documentation. 
