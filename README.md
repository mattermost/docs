# Mattermost Platform Documentation

This repository generates the documentation available at http://docs.mattermost.com/

All documentation is available under the terms of a [Creative Commons License](http://creativecommons.org/licenses/by-nc-sa/3.0/).

## Usage

To generate the HTML files from markdown in the `/source` directory: 

1. Download repo onto a machine with Python installed
2. `pip install sphinx sphinx-autobuild sphinx_rtd_theme`
3. `pip install recommonmark`
4. Type `make html`

## Contributing

**How to create Pull Requests for documentation (by community members):**

1. Sign the Contributor License Agreement (see instructions in the next section).
3. On the Mattermost Documentation page that you want to edit, click the GitHub icon on the upper right corner that says "Edit".
4. Click "Edit this file" (pencil icon).
5. After making changes, check the "Create a new branch for this commit and start a pull request".
6. Make sure that the Pull Request has a descriptive title. Add comments to briefly tell others what you have worked on (optional).
7. Click "Create a Pull Request".

**Signing CLA:**

Please complete the [Mattermost Contributor Agreement](http://www.mattermost.org/mattermost-contributor-agreement/), so you can be added to the Mattermost [Approved Contributor List](https://docs.google.com/spreadsheets/d/1NTCeG-iL_VS9bFqtmHSfwETo5f-8MQ7oMDE5IUYJi_Y/pubhtml?gid=0&single=true).

**Additional process for Core Committers on Repositions:**

1. “Needs Editorial Review” label should be processed **after merge**.
2. IMPORTANT: Person conducting editoral review needs to have their suggestions **merged by author**. Do this by mentioning the pre-release.mattermost.com user name in the GitHub Pull Request.
3. Check weekly or bi-weekly that there are no “Needs Editoral Review” labels on closed Pull Requests.
