# Mattermost Documentation

This repository generates the documentation available at https://docs.mattermost.com/. All documentation is available under the terms of a [Creative Commons License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

If you have any questions, create an account on the [Mattermost Community server](https://community.mattermost.com/signup_user_complete/?id=f1924a8db44ff3bb41c96424cdc20676), then join the writing team in the [Documentation Working Group](https://community.mattermost.com/core/channels/dwg-documentation-working-group) channel. We look forward to working with you!

# Table of Contents

- [Mattermost Documentation](#mattermost-documentation)
- [Table of Contents](#table-of-contents)
  - [Contribute to Mattermost product documentation](#contribute-to-mattermost-product-documentation)
    - [Get started](#get-started)
    - [Edit content directly on GitHub](#edit-content-directly-on-github)
    - [Create Documentation pull requests](#create-documentation-pull-requests)
    - [Comment on pull requests](#comment-on-pull-requests)
    - [Review pull requests](#review-pull-requests)
  - [Build locally](#build-locally)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Build commands](#build-commands)
    - [Troubleshooting](#troubleshooting)

## Contribute to Mattermost product documentation

### Get started

You can edit or create Mattermost documentation directly in GitHub, or by downloading the `mattermost/docs` repository onto your machine and using an IDE such as VSCode.

If this is your first time contributing to Mattermost, first read and sign the [Mattermost Contributor Agreement](https://mattermost.com/mattermost-contributor-agreement/), so you can be added to the Mattermost [Approved Contributor List](https://docs.google.com/spreadsheets/d/1NTCeG-iL_VS9bFqtmHSfwETo5f-8MQ7oMDE5IUYJi_Y/pubhtml?gid=0&single=true).

### Edit content directly on GitHub

The quickest way to begin is editing directly on GitHub on your fork of the Mattermost docs repo. Select the **Edit** icon on the top right corner of the page you want to edit in the Mattermost documentation.

If this is the first time you're contributing, follow these steps: 
1. Select **Fork** in the top-right corner of the GitHub repository page to fork the current repository.
2. Navigate to file you want to edit, then select the Pencil icon (**Edit the file**) to open the editing interface.

### Create Documentation pull requests

1. When you're ready to submit your changes, add a descriptive title and comments to summarize the changes made.
2. Select **Create a new branch for this commit and start a pull request**.
3. Check the **Propose file change** button.
4. Scroll down to compare changes with the original document.
5. Select **Create pull request**. 

### Comment on pull requests

Once a pull request is submitted, multiple committers may comment on it and provide edits or suggestions which you can commit directly. You can also add line comments. Take a look at [Commenting on pull requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request) for more details.

### Review pull requests

Once a pull request has been submitted and the correct label assigned, the review process begins. This includes aligning the content with the Style Guide, validating processes, and tagging any other relevant committers. Read more about the review process and expectations [in the Mattermost Developer documentation](https://developers.mattermost.com/contribute/getting-started/code-review/). 

Once the review process is complete, and depending on the type of issue it is (e.g., a typo fix vs. a new feature), the change is either merged into master and pushed immediately or merged into the release branch and pushed in alignment with a future release. The branch is then deleted. 

## Build locally

If you've downloaded the `mattermost/docs` repository to edit Mattermost documentation on your local machine, you can generate the HTML files from the `source` directory. You can review your changes as a live or static preview before committing them or creating new pull requests.

> [!NOTE]
> You can generate the docs on Linux, Mac, and Windows (using PowerShell); however, builds on Windows are considerably slower because only a single processing core is used.
> 
> For faster local docs builds on Windows, we strongly recommend [installing WSL](https://learn.microsoft.com/en-us/windows/wsl/install) to create an Ubuntu virtual machine (VM), where you'll configure the following prerequisites. This VM will be using all available processing cores, resulting in faster local builds.

### Prerequisites

- Git [[download]](https://git-scm.com/downloads)
- Python 3.11 or later [[download]](https://www.python.org/downloads)
- Pipenv [[download]](https://pipenv.pypa.io)
- GNU Make 3.82 or later

> [!NOTE]
> Windows users who aren't using WSL require `make` installed. To install via Chocolatey: run `choco install make` in an admin PowerShell terminal after installing [chocolatey](https://chocolatey.org/).

### Setup

1. Clone the repository and navigate to it:
   ```shell
   git clone https://github.com/mattermost/docs.git
   cd docs
   ```

2. Install pipenv:
   ```shell
   # Mac/Ubuntu with Homebrew
   brew install pipenv

   # Other systems
   pip install --user pipenv
   ```

3. Install dependencies (choose one):
   ```shell
   # For local development (recommended for first-time setup)
   pipenv install --dev

   # For exact reproducibility (CI/CD or team environments)
   pipenv sync --dev
   ```

4. Initialize Git submodules:
   ```shell
   git submodule update --init --recursive
   ```

### Build commands

- **`gmake html`** - Build only modified files (fastest for iterative changes)
- **`gmake clean html`** - Clean build directory and rebuild all files
- **`gmake livehtml`** - Start live preview server at `http://127.0.0.1:8000` (auto-updates on save)

Static build output is located in `build/html/index.html`. Build errors are logged to `build/warnings.log` and `build/redirect-warnings.log`.

### Troubleshooting

**What if my local build starts becoming slow?**

Run `make clean` and rebuild the repository from scratch:
```shell
make clean
gmake html
```
