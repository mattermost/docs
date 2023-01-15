# Mattermost Documentation

This repository generates the documentation available at https://docs.mattermost.com/. All documentation is available under the terms of a [Creative Commons License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

If you have any questions, create an account on the [Mattermost Community server](https://community.mattermost.com/signup_user_complete/?id=f1924a8db44ff3bb41c96424cdc20676), then join the writing team in the [Documentation Working Group](https://community.mattermost.com/core/channels/dwg-documentation-working-group) channel. We look forward to working with you!

# Table of Contents

 * [Contributing](#contribute-to-mattermost-product-documentation)
     * [Get started](#get-started)
     * [Edit content directly on GitHub](#edit-content-directly-on-github)
     * [Create documentation PRs](#create-documentation-pull-requests)
     * [Use GitHub PR Labels](#use-github-pr-labels)
     * [Comment on Pull Requests](#comment-on-pull-requests)
     * [Review Pull Requests](#review-pull-requests)
 * [Build Mattermost product documentation locally](#build-locally)

## Contribute to Mattermost product documentation

### Get started

You can edit or create Mattermost documentation directly in GitHub, or by downloading the `mattermost/docs` repository onto your machine and using an IDE such as VS Code. Consult the Mattermost [Documentation Style Guide](https://handbook.mattermost.com/operations/research-and-development/product/technical-writing-team-handbook/documentation-style-guide) and [reStructuredText Markup](https://handbook.mattermost.com/operations/research-and-development/product/technical-writing-team-handbook/documentation-style-guide#using-restructuredtext-markup-rst) section for stylistic and technical guidance.

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

### Use GitHub PR labels

GitHub PR labels are used to track the lifecycle and status of a pull request. Using the correct labels helps with managing workflows and ensuring that content is edited, merged and released at the correct time. For example, PRs that include an **Editor Review** label will be processed by an editor on the writing team to ensure the documentation is correctly formatted at https://docs.mattermost.com/ based on guidelines outlined in the style guide.

Take a look at the [Labels](https://developers.mattermost.com/contribute/getting-started/labels/) page for information about how and when to use which labels.

### Comment on pull requests

Once a pull request is submitted, multiple committers may comment on it and provide edits or suggestions which you can commit directly. You can also add line comments. Take a look at [Commenting on pull requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request) for more details.

### Review pull requests

Once a pull request has been submitted and the correct label assigned, the review process begins. This includes aligning the content with the Style Guide, validating processes, and tagging any other relevant committers. Read more about the review process and expectations [in the Mattermost Developer documentation](https://developers.mattermost.com/contribute/getting-started/code-review/). 

Once the review process is complete, and depending on the type of issue it is (e.g., a typo fix vs. a new feature), the change is either merged into master and pushed immediately or merged into the release branch and pushed in alignment with a future release. The branch is then deleted. 

## Build locally

If you've downloaded the `mattermost/docs` repository and are editing Mattermost documentation on your local machine, you can generate the HTML files from markdown in the `source` directory. You can review your changes before you commit them or create pull requests.

**Note:** Terminal commands can be executed on Linux, Mac, and Windows (using PowerShell).

### Build prerequisites

The following software is required to build the documentation:

- Git [[download]](https://git-scm.com/downloads)
- Python 3.9 or later [[download]](https://www.python.org/downloads/)

### Build instructions

1. Open a terminal window, then clone a forked copy of the documentation repository:
    ```shell
    git clone https://github.com/mattermost/docs.git
    ```

2. In the terminal window, navigate into the cloned repository:
    ```shell
    cd docs
    ```

3. Install [pipenv](https://docs.pipenv.org/) by using one of the following commands based on your operating system:

    For Mac users where Homebrew is installed:
    ```shell
    brew install pipenv
    ```

    For other operating systems:
    ```shell
    pip install --user pipenv
    ```

4. Install required Python packages:
    ```shell
    pipenv install --dev
    ```

5. Build the documentation set. You have three build commands available at the terminal:

    - Use `make html` to generate HTML files in the `/build` directory. Only file you've modified are re-built.
    - Use `make clean html` to delete all static HTML output in the `/build` directory and re-build all files. This command is particularly useful when you're making changes to the LHS navigation pane and want to ensure you're not reviewing cached results.
    - Use `make livehtml` to review a live preview published to `http://127.0.0.1:8000` that automatically updates as new changes are saved in your local IDE.

   Windows users will require [GNU Make](https://gnuwin32.sourceforge.net/packages/make.htm) installed for the above commands to work correctly. If GNU Make is not installed, please substitute `CMD /C make.bat` for `make` in the above commands to use the Windows command interpreter. For example `make html` will become `CMD /C make.bat html` on Windows.

   Note: When using the `CMD /C make.bat` substitution, only a single target may be specified. Instead of running `CMD /C make.bat clean html`, each target must be run seperately. For example, `CMD /C make.bat clean` followed by `CMD /C make.bat html`. 

6. When working with static build results, navigate to the `build` directory:
    ```sh
    cd build
    ```
   
7. Then, preview your changes by opening the `source/html/index.html` file.

Build errors are written to the `build/warnings.log` file. 
