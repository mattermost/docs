# Mattermost Platform Documentation

This repository generates the documentation available at http://docs.mattermost.com/

## Usage

To generate the HTML files from markdown in the `/source` directory: 

1. Download repo onto a machine with Python installed
2. `pip install sphinx sphinx-autobuild sphinx_rtd_theme`
3. `pip install recommonmark`
4. Type `make html`

## Contributing

How to create Pull Requests (by community members):

1. Sign the Contributor License Agreement (see instructions in the next section)
2. To contribute to the documentation please fork this repository and create a pull request.
3.
4.

Signing CLA:

Please complete the [Mattermost Contributor Agreement](http://www.mattermost.org/mattermost-contributor-agreement/), so you can be added to the Mattermost [Approved Contributor List](https://docs.google.com/spreadsheets/d/1NTCeG-iL_VS9bFqtmHSfwETo5f-8MQ7oMDE5IUYJi_Y/pubhtml?gid=0&single=true).

Additional process for Core Committers on Repositions:

1. “Needs Editorial Review” label should be processed AFTER MERGE.
2. IMPORTANT: Person conducting editoral review needs to have their suggestions MERGED BY AUTHOR. Do this by mentioning the pre-release.mattermost.com user name in the GitHub Pull Request.
3. Check weekly or bi-weekly that there are no “Needs Editoral Review” labels on closed Pull Requests.

All documentation is available under the terms of a [Creative Commons License](http://creativecommons.org/licenses/by-nc-sa/3.0/)
