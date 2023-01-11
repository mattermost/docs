# Minimal makefile for Sphinx documentation
#
.PHONY: Makefile help python-deps linkcheck livehtml python-deps test compass-icons
#
# You can set these variables from the command line, and also
# from the environment for the last three.
SOURCEDIR       = source
BUILDDIR        = build
WARNINGSFILE    = $(BUILDDIR)/warnings.log
SPHINXOPTS      ?= -j auto
SPHINXBUILD     ?= pipenv run sphinx-build
SPHINXAUTOBUILD ?= pipenv run sphinx-autobuild

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Install necessary dependencies for the CI build pipeline.
# NOTE: if the version of Python used to build the docs changes, update the `pipenv` command below accordingly.
python-deps:
	pip install pipenv==2022.12.19
	pipenv install --dev --clear --deploy --python 3.9

test:
	pipenv run pytest

# Run `make livehtml` to start sphinx-autobuild.
livehtml:
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXAUTOBUILD) "$(SOURCEDIR)" "$(BUILDDIR)/html" -d "$(BUILDDIR)/doctrees" $(SPHINXOPTS) $(O)

# Run `make linkcheck` to check external links
# Overriding `exclude_patterns` configuration to exclude
# directories or files not included in the documentation
linkcheck:
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXBUILD) -M $@ -D exclude_patterns=archive/*,process/* "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) 2>>"$(WARNINGSFILE)"

# Download the latest Compass Icon assets.
compass-icons:
	mkdir -p source/_static/css
	mkdir -p source/_static/font
	curl --no-progress-meter -o source/_static/css/compass-icons.css https://mattermost.github.io/compass-icons/css/compass-icons.css
	curl --no-progress-meter -o "source/_static/font/compass-icons.#1" "https://mattermost.github.io/compass-icons/font/compass-icons.{eot,woff2,woff,ttf,svg}"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) 2>>"$(WARNINGSFILE)"
