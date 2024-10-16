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
AUTOBUILDOPTS   ?= -D=html_baseurl=http://127.0.0.1:8000

# If we're not on Windows, check to see if 'mm_url_path_prefix' is included in SPHINXOPTS.
# If it is included, extract the PR ID from the prefix and set the html_baseurl config
# option to the preview environment.
ifneq ($(OS),Windows_NT)
ifeq ($(findstring mm_url_path_prefix,$(SPHINXOPTS)),mm_url_path_prefix)
PATH_PREFIX = $(shell echo "$(SPHINXOPTS)" | grep -Eo 'mm_url_path_prefix=\/([0-9]+)' | cut -d / -f 2)
SPHINXOPTS2 = $(SPHINXOPTS) -D html_baseurl=http://mattermost-docs-preview-pulls.s3-website-us-east-1.amazonaws.com/$(PATH_PREFIX)
else
SPHINXOPTS2 = $(SPHINXOPTS)
endif
endif

# Put it first so that "make" without argument is like "make help".
help:
ifeq ($(OS),Windows_NT)
	@CMD /C $(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
else
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
endif

# Install necessary dependencies for the CI build pipeline.
# NOTE: if the version of Python used to build the docs changes, update the `pipenv` command below accordingly.
python-deps:
	pip install pipenv==2024.1.0
	pipenv install --dev --clear --deploy --python 3.12

test:
	pipenv run pytest

# Run `make livehtml` to start sphinx-autobuild.
livehtml:
ifeq ($(OS),Windows_NT)
	@CMD /C IF NOT EXIST $(BUILDDIR) MD $(BUILDDIR)
	@CMD /C $(SPHINXAUTOBUILD) "$(SOURCEDIR)" "$(BUILDDIR)/html" -d "$(BUILDDIR)/doctrees" $(SPHINXOPTS) $(AUTOBUILDOPTS) $(O)
else
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXAUTOBUILD) "$(SOURCEDIR)" "$(BUILDDIR)/html" -d "$(BUILDDIR)/doctrees" $(SPHINXOPTS) $(AUTOBUILDOPTS) $(O)
endif

# Run `make linkcheck` to check external links
# Overriding `exclude_patterns` configuration to exclude
# directories or files not included in the documentation
linkcheck:
ifeq ($(OS),Windows_NT)
	@CMD /C IF NOT EXIST $(BUILDDIR) MD $(BUILDDIR)
	@CMD /C $(SPHINXBUILD) -M $@ -D exclude_patterns=archive/*,process/* "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -w "$(WARNINGSFILE)" 2>NUL
else
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXBUILD) -M $@ -D exclude_patterns=archive/*,process/* "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) 2>>"$(WARNINGSFILE)"
endif


# Download the latest Compass Icon assets.
compass-icons:
ifeq ($(OS),Windows_NT)
	@CMD /C IF NOT EXIST source/_static/css MD source/_static/css
	@CMD /C IF NOT EXIST source/_static/font MD source/_static/font
else
	@mkdir -p source/_static/css
	@mkdir -p source/_static/font
endif
	curl --no-progress-meter -o source/_static/css/compass-icons.css https://mattermost.github.io/compass-icons/css/compass-icons.css
	curl --no-progress-meter -o "source/_static/font/compass-icons.#1" "https://mattermost.github.io/compass-icons/font/compass-icons.{eot,woff2,woff,ttf,svg}"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
ifeq ($(OS),Windows_NT)
	@CMD /C IF NOT EXIST $(BUILDDIR) MD $(BUILDDIR)
	@CMD /C $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -w "$(WARNINGSFILE)" 2>NUL
else
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS2) $(O) 2>>"$(WARNINGSFILE)"
endif
