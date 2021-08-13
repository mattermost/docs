# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the last three.
SOURCEDIR       = source
BUILDDIR        = build
WARNINGSFILE    = $(BUILDDIR)/warnings.log
ERRORSFILE      = $(BUILDDIR)/errors.log
SPHINXOPTS      ?= -j auto -w $(WARNINGSFILE)
SPHINXBUILD     ?= pipenv run sphinx-build
SPHINXAUTOBUILD ?= pipenv run sphinx-autobuild

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile livehtml clean

# Run `make livehtml` to start sphinx-autobuild
livehtml:
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXAUTOBUILD) "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@mkdir -p "$(BUILDDIR)"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) 2>>"$(ERRORSFILE)"

clean: # clean the build directory
	rm -rf build/
