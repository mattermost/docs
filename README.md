# Mattermost Documentation

This repository generates the documentation available at https://docs.mattermost.com/

All documentation is available under the terms of a [Creative Commons License](https://creativecommons.org/licenses/by-nc-sa/3.0/).

## Usage

To generate the HTML files from markdown in the `/source` directory:

1. Download repo onto a machine with Python installed
2. Install [pipenv](https://docs.pipenv.org/): `pip install pipenv`
3. `cd` into the cloned repository
4. Install required packages: `pipenv install`
5. Build: `make html` - generates files in `/build` directory

## Contributing

**How to create Pull Requests to edit or create Mattermost documentation (by community members):**

1. Sign the Contributor License Agreement (see instructions in the next section).
3. On the Mattermost Documentation page that you want to edit, click the GitHub icon on the upper right corner that says "Edit".
4. Click "Edit the file in your fork of this project" (pencil icon) on the upper right corner.
5. After making changes, check the "Propose file change" button.
6. Compare changes with the original document.
7. Click "Create a Pull Request". Make sure that the Pull Request has a descriptive title and add comments to briefly tell others what you have worked on (optional).

**Signing CLA:**

Please read the [Mattermost Contributor Agreement](https://www.mattermost.org/mattermost-contributor-agreement/) and sign it (at the bottom of the page), so you can be added to the Mattermost [Approved Contributor List](https://docs.google.com/spreadsheets/d/1NTCeG-iL_VS9bFqtmHSfwETo5f-8MQ7oMDE5IUYJi_Y/pubhtml?gid=0&single=true).

**Additional process for Core Committers for Doc Repo:**

These steps are to be followed only in situations of urgency or in situations where it is necessary to check that there aren't any high confidentiality issues. Otherwise the standard approval process should be followed.

1. “Needs Editor Review” label should be processed **after merge**.
2. IMPORTANT: Person conducting editor review needs to have their suggestions **merged by author**. Do this by mentioning the pre-release.mattermost.com user name in the GitHub Pull Request.
3. Check weekly or bi-weekly that there are no “Needs Editor Review” labels on closed Pull Requests.

## Installation issues

If you can't install sphinx on MacOS try `sudo pip install sphinx sphinx-autobuild sphinx_rtd_theme --ignore-installed six`.
