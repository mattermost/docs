# Minimal makefile for Sphinx documentation
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

.PHONY: help Makefile livehtml python-deps

python-deps:
	pip install pipenv
	pipenv install --dev

# Run `make livehtml` to start sphinx-autobuild
livehtml:
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXAUTOBUILD) "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Run `make linkcheck` to check external links
# Overriding `exclude_patterns` configuration to exclude
# directories or files not included in the documentation
linkcheck:
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXBUILD) -M $@ -D exclude_patterns=archive/*,process/* "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) 2>>"$(WARNINGSFILE)"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) 2>>"$(WARNINGSFILE)"
