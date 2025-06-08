# Makefile for Sphinx documentation
#
.PHONY: Makefile help python-deps linkcheck livehtml python-deps test compass-icons

# Check Make version (we need at least GNU Make 3.82). Fortunately,
# 'undefine' directive has been introduced exactly in GNU Make 3.82.
#
# Platform notes:
#
#    macOS has shipped with v3.81 of GNU Make pre-installed and may
#    cause this error. A modern version of GNU Make can be installed
#    using Homebrew.
#
#    Windows users can install a modern version of GNU Make using
#    the Scoop (https://scoop.sh/) or Chocolatey (https://chocolatey.org)
#    package managers.
#
ifeq ($(filter undefine,$(.FEATURES)),)
$(error Unsupported Make version. \
    The build system does not work properly with GNU Make $(MAKE_VERSION), \
    please use GNU Make 3.82 or above.)
endif

#
# You can set these variables from the command line, and also
# from the environment for the last three.
SOURCEDIR       = source
BUILDDIR        = build
SPHINXOPTS      ?= -j auto
SPHINXBUILD     ?= pipenv run sphinx-build
SPHINXAUTOBUILD ?= pipenv run sphinx-autobuild
AUTOBUILDOPTS   ?= -D=html_baseurl=http://127.0.0.1:8000

# If we're using Windows, use CMD to run commands in the Makefile.
ifeq ($(OS),Windows_NT)
SHELL=C:\Windows\system32\cmd.exe
.SHELLFLAGS=/C
WARNINGSFILE=$(BUILDDIR)\warnings.log
else
WARNINGSFILE=$(BUILDDIR)/warnings.log
endif

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

# Put the help target first so that "make" without arguments runs like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Install necessary dependencies for the Mattermost docs CI build pipeline.
# NOTE: if the version of Python used to build the docs changes, update the `pipenv` command below accordingly.
python-deps:
	pip install pipenv==2025.0.2
	pipenv install --dev --clear --deploy --python 3.12

# Run `make test` to start Sphinx extension unit tests.
test:
	pipenv run pytest

# Run `make livehtml` to start sphinx-autobuild.
# Note: sphinx-autobuild seems to want a build directory
#       setting of $(BUILDDIR)/html instead of $(BUILDDIR)
#       to use the output of a previous `make html` build.
livehtml:
ifeq ($(OS),Windows_NT)
	@IF NOT EXIST $(BUILDDIR) MD $(BUILDDIR)
	@$(SPHINXAUTOBUILD) "$(SOURCEDIR)" "$(BUILDDIR)\html" -d "$(BUILDDIR)\doctrees" $(SPHINXOPTS) $(AUTOBUILDOPTS) $(O)
else
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXAUTOBUILD) "$(SOURCEDIR)" "$(BUILDDIR)/html" -d "$(BUILDDIR)/doctrees" $(SPHINXOPTS) $(AUTOBUILDOPTS) $(O)
endif

# Run `make linkcheck` to check external links.
# Overriding `exclude_patterns` configuration to exclude
# directories or files not included in the documentation.
linkcheck:
ifeq ($(OS),Windows_NT)
	@IF NOT EXIST $(BUILDDIR) MD $(BUILDDIR)
	@$(SPHINXBUILD) -M $@ -D exclude_patterns=archive\*,process\* "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -w "$(WARNINGSFILE)"
else
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXBUILD) -M $@ -D exclude_patterns=archive/*,process/* "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -w "$(WARNINGSFILE)"
endif

# Run `make compass-icons` to download the latest Compass Icons assets.
# This target requires the cURL utility. See https://curl.se/ for download instructions.
compass-icons:
ifeq ($(OS),Windows_NT)
	@IF NOT EXIST source/_static/css MD source/_static/css
	@IF NOT EXIST source/_static/font MD source/_static/font
else
	@mkdir -p source/_static/css
	@mkdir -p source/_static/font
endif
	curl --no-progress-meter -o source/_static/css/compass-icons.css https://mattermost.github.io/compass-icons/css/compass-icons.css
	curl --no-progress-meter -o "source/_static/font/compass-icons.#1" "https://mattermost.github.io/compass-icons/font/compass-icons.{eot,woff2,woff,ttf,svg}"

# Catch-all target: route all unknown targets to Sphinx using the
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
# Note: Instead of $(SPHINXOPTS), non-Windows (i.e. Linux) systems use $(SPHINXOPTS2)
#       to account for Mattermost docs preview builds.
%: Makefile
ifeq ($(OS),Windows_NT)
	@IF NOT EXIST $(BUILDDIR) MD $(BUILDDIR)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -w "$(WARNINGSFILE)"
else
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS2) $(O) -w "$(WARNINGSFILE)"
endif
