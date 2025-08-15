# Mattermost documentation configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os
from sphinx.application import Sphinx


def find_duplicate_redirects(redirects_map: dict[str, str]) -> bool:
    # Track sources that map to the same target
    target_to_sources: dict[str, list[str]] = {}
    # Track duplicate sources
    duplicate_sources: dict[str, str] = {}

    # Open redirect warnings log file in build directory
    with open("build/redirect-warnings.log", "w") as log:
        for source, target in redirects_map.items():
            # Check for duplicate sources
            if source in duplicate_sources:
                warning: str = f"\nDuplicate redirect found:\n"
                warning += f"Source: {source}\n"
                warning += f"Already maps to: {duplicate_sources[source]}\n"
                warning += f"Also maps to: {target}\n"
                log.write(warning)
            else:
                duplicate_sources[source] = target

            # Track sources mapping to same target
            if target in target_to_sources:
                target_to_sources[target].append(source)
            else:
                target_to_sources[target] = [source]

        # Log sources that map to the same target
        for target, sources in target_to_sources.items():
            if len(sources) > 1:
                warning_message: str = (
                    f"Multiple sources map to same target; Target: {target} <- Sources: {sources}\n"
                )
                log.write(warning_message)

    return len(duplicate_sources) == len(redirects_map)


# Import page redirect configuration from redirects.py
sys.path.insert(0, os.path.abspath("."))
import redirects as redirects_py

redirects = redirects_py.redirects_map


def setup(_: Sphinx):
    # Check for duplicate redirects when Sphinx builds
    find_duplicate_redirects(redirects_py.redirects_map)
    return


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath("../extensions"))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = "7.2"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autosectionlabel",
    "myst_parser",
    "sphinxcontrib.mermaid",
    # `reredirects` is a local clone of sphinx_reredirects with parallel
    # read and write support enabled.
    # The original sphinx_reredirects extension can be found at:
    # https://documatt.gitlab.io/sphinx-reredirects/
    "reredirects",
    # `sitemap` is a local clone of sphinx_sitemap with parallel read
    # and write support enabled.
    # The original sphinx_sitemap extension can be found at:
    # https://pypi.org/project/sphinx-sitemap/
    "sitemap",
    "sphinx_copybutton",
    "compass-icons",
    "config-setting-v2",
    "sphinx_inline_tabs",
]

# Mermaid configuration - using minimum required version for sphinxcontrib-mermaid 1.0.0
mermaid_version = "10.3.0"
mermaid_init_js = """
// Wait for Mermaid chart to render
function waitForMermaidChart() {
    const mermaidChart = document.querySelector('.mermaid svg');
    if (mermaidChart) {
        fixMermaidTextColors();
        setupThemeObserver();
    } else {
        setTimeout(waitForMermaidChart, 100);
    }
}

function fixMermaidTextColors() {
    const body = document.body;
    const isLightTheme = body.getAttribute('data-custom-theme') === 'light';
    
    // Apply text colors based on current theme
    const textElements = document.querySelectorAll('.mermaid text');
    textElements.forEach(textElement => {
        if (isLightTheme) {
            // Light mode: remove any forced white text and let CSS handle it
            textElement.style.removeProperty('fill');
            textElement.style.removeProperty('color');
        } else {
            // Dark mode: ensure text is white
            textElement.style.setProperty('fill', '#ffffff', 'important');
            textElement.style.setProperty('color', '#ffffff', 'important');
        }
    });
}

function setupThemeObserver() {
    // Watch for theme changes on the body element
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            if (mutation.type === 'attributes' && mutation.attributeName === 'data-custom-theme') {
                // Theme changed, update text colors
                setTimeout(fixMermaidTextColors, 50);
            }
        });
    });
    
    observer.observe(document.body, {
        attributes: true,
        attributeFilter: ['data-custom-theme']
    });
}

// Start the process
waitForMermaidChart();

// Also fix on page load events
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(fixMermaidTextColors, 100);
});

window.addEventListener('load', () => {
    setTimeout(fixMermaidTextColors, 100);
});
"""

sphinx_tabs_disable_tab_closing = True
sphinx_tabs_disable_css_loading = False
myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 3

# Suppress particular classes of warnings
suppress_warnings = ["myst.xref_missing", "myst.header", "autosectionlabel"]

# Prefix document path to section labels, otherwise autogenerated labels would look like 'heading'
# rather than 'path/to/file:heading'
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames and what type of document they map to.
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# Sitemap configuration
sitemap_excludes = [
    # Original excludes
    "agents/.config/notice-file/README.html",
    
    # GitHub directory files
    "agents/.github/CONTRIBUTING.html",
    "agents/.github/ISSUE_TEMPLATE/BUG_REPORT.html",
    "agents/.github/ISSUE_TEMPLATE/FEATURE_REQUEST.html",
    "agents/.github/PULL_REQUEST_TEMPLATE.html",
    "agents/.github/SECURITY.html",
    
    # Common ESR support files
    "about/common-esr-support.html",
    "about/common-esr-support-rst.html",
    "about/common-esr-support-upgrade.html",
    
    # Deploy server files
    "deploy/server/linux/deploy-tar.html",
    "deploy/server/linux/deploy-omnibus.html",
    "deploy/server/linux/deploy-ubuntu.html",
    "deploy/server/linux/deploy-rhel.html",
    "deploy/server/kubernetes/deploy-k8s-aks.html",
    "deploy/server/kubernetes/deploy-k8s.html",
    "deploy/server/containers/install-aws-beanstalk.html",
    "deploy/server/containers/install-docker.html",
    
    # About and configure files
    "about/cloud-supported-integrations.html",
    "configure/push-notification-server-configuration-settings.html",
    "configure/rate-limiting-configuration-settings.html",
    
    # Onboard files
    "onboard/common-converting-oauth-to-openidconnect.html",
    "onboard/sso-saml-before-you-begin.html",
    "onboard/sso-saml-faq.html",
    "onboard/sso-saml-ldapsync.html",
    
    # Scale files
    "scale/estimated-storage-per-user-per-month.html",
    "scale/lifetime-storage.html",
    
    # Agents files
    "agents/readme.html",
    "agents/notice.html",
    "agents/license.html",
    "agents/claude.html",
    "agents/CLAUDE.html",
    "agents/README.html",
    "agents/interpluginclient/README.html",
]

# -- Page redirects -------------------------------------------------

# If `redirects_baseurl` is non-empty and the target of a redirect begins
# with that value, the value of `html_baseurl` will replace that of
# `redirects_baseurl`. The target will not be affected if `redirects_baseurl`
# and `html_baseurl` have the same value.
redirects_baseurl = "https://docs.mattermost.com/"

# A redirect option which, when True, will write one extensionless page (i.e. without the .html extension)
# for each redirect page that was written. This enables redirects for pages where the .html extension was not
# specified in the URL and the underlying web server doesn't attempt to add .html when resolving the location
# of the resource to send.
redirects_write_extensionless_pages = False

# General information about the project.
project = "Mattermost"
copyright = "2015-2025 Mattermost"
author = "Mattermost"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '10.11'
# The full version, including alpha/beta/rc tags.
# release = '10.11'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = "en"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories and files to ignore when looking for source files. Include all child pages that are includes of another page as well as any submodule
# files from external repositories you don't want to be returned in search results.
exclude_patterns = [
    # Reusable included child pages that shouldn't be available outside of the context of their parent pages
    "about/common-esr-support.md", 
    "about/common-esr-support-rst.rst", 
    "about/common-esr-support-upgrade.md", 
    "deploy/server/linux/deploy-tar.rst", 
    "deploy/server/linux/deploy-omnibus.rst", 
    "deploy/server/linux/deploy-ubuntu.rst", 
    "deploy/server/linux/deploy-rhel.rst", 
    "deploy/server/kubernetes/deploy-k8s-aks.rst", 
    "deploy/server/kubernetes/deploy-k8s.rst", 
    "deploy/server/containers/install-aws-beanstalk.rst", 
    "deploy/server/containers/install-docker.rst", 
    "about/cloud-supported-integrations.rst", 
    "configure/push-notification-server-configuration-settings.rst", 
    "configure/rate-limiting-configuration-settings.rst", 
    "onboard/common-converting-oauth-to-openidconnect.rst", 
    "onboard/sso-saml-before-you-begin.rst", 
    "onboard/sso-saml-faq.rst", 
    "onboard/sso-saml-ldapsync.rst", 
    "scale/estimated-storage-per-user-per-month.rst", 
    "scale/lifetime-storage.rst", 
    # Agents directory files - development and repository files that shouldn't be in documentation
    "agents/.config/notice-file/README.md",
    "agents/.github/CONTRIBUTING.md",
    "agents/.github/ISSUE_TEMPLATE/BUG_REPORT.md",
    "agents/.github/ISSUE_TEMPLATE/FEATURE_REQUEST.md",
    "agents/.github/PULL_REQUEST_TEMPLATE.md",
    "agents/.github/SECURITY.md",
    "agents/CLAUDE.md",
    "agents/README.md",
    "agents/interpluginclient/README.md",
    "agents/notice.txt", 
    "agents/license.txt"
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
pygments_dark_style = "monokai"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# -- Options for HTML output ----------------------------------------------

html_baseurl = "https://docs.mattermost.com/"

# Global variables available to all templates
html_context = {
    # Enable Google Analytics
    "googleanalytics_id": "UA-67846571-2",
    "googleanalytics_enabled": True,
}

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "furo"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "light_css_variables": {
        "font-stack": "'Noto Sans', 'Helvetica Neue', Arial, sans-serif",
        "font-stack--monospace": "'Fira Mono', 'Courier New', Courier, monospace",
    },
    # Edit in GitHub settings
    "source_repository": "https://github.com/mattermost/docs/",
    "source_branch": "master",
    "source_directory": "source/",
    # Only show the 'Edit in GitHub' button at the top of the page; don't show the 'View in GitHub' button
    "top_of_page_buttons": ["edit"],
}

# html_permalinks_icon = " "

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Mattermost documentation"

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# A list of CSS files. The entry must be a filename string or a tuple containing the filename string and the attributes
# dictionary. The filename must be relative to the html_static_path, or a full URI with scheme like
# https://example.org/style.css. The attributes is used for attributes of <link> tag. It defaults to an empty list.
html_css_files = [
    "css/mattermost-global.css",
    "css/homepage-v1.css",
    "css/compass-icons.css",
    "css/version-filter.css",
    "css/changelog-filter.css",
]

# A list of JavaScript filenames. The entry must be a filename string or a tuple containing the filename string and the
# attributes dictionary. The filename must be relative to the html_static_path, or a full URI with scheme like
# https://example.org/script.js. The attributes is used for attributes of <script> tag. It defaults to an empty list.
html_js_files = [
    "js/jquery.js",
    "js/thermometer.js",
    "js/myscript-v1.js",
    "js/version-filter.js",
    "js/changelog-filter.js",
]

# The name of an image file, relative to the configuration directory, to use as favicon of the docs.  This file should
# be a Windows icon file (.ico) being 16x16 or 32x32 pixels in size.
html_favicon = "_static/favicon.ico"

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ["_static/robots.txt"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {"404": "404.html"}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
html_search_language = "en"

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# linkcheck settings
linkcheck_ignore = [
    # Ignore localhost
    "http://localhost",
    "http://127.0.0.1",
    # Ignore anchors on github.com and Weblate because linkcheck fails on them
    "https://github.com",
    "https://translate.mattermost.com/",
    # Ignore azuremarketplace because of no server response
    "https://azuremarketplace.microsoft.com/.*",
    # Ignore Mattermost Support Portal
    "https://support.mattermost.com",
    # Ignore BizGov & HIPPA
    "www.bis.doc.gov",
    "https://www.hhs.gov/",
]
linkcheck_timeout = 10
linkcheck_rate_limit_timeout = 10.0
linkcheck_anchors = False

rst_prolog = """
.. |plans-img| image:: /_static/images/badges/flag_icon.svg
    :class: mm-badge-flag
.. |deployment-img| image:: /_static/images/badges/deployment_icon.svg
    :class: mm-badge-flag
.. |plans-img-yellow| image:: /_static/images/badges/flag_icon_yellow.svg
    :class: mm-badge-flag
.. |deployment-img-yellow| image:: /_static/images/badges/deployment_icon_yellow.svg
    :class: mm-badge-deployment
.. |copy-link-icon| image:: /images/link-variant_F0339.svg
    :alt: Use the Copy Link icon to copy the public URL link for an image in a message.
    :class: theme-icon
.. |channel-info| image:: /images/information-outline_F02FD.svg
    :alt: Use the Channel Info icon to access additional channel management options.
    :class: theme-icon
.. |more-icon| image:: /images/dots-horizontal_F01D8.svg
    :alt: Use the More icon to access additional message options.
    :class: theme-icon
.. |favorite-icon| image:: /images/star-outline_F04D2.svg
    :alt: Use the Star icon to mark a channel as a favorite.
    :class: theme-icon
.. |globe| image:: /images/globe_E805.svg
    :alt: Public channels are identified with a Globe icon.
    :class: theme-icon
.. |lock| image:: /images/lock-outline_F0341.svg
    :alt: Private channels are identified with a Lock icon.
    :class: theme-icon
.. |file-box| image:: /images/archive-outline_F120E.svg
    :alt: Archived channels are identified with a File Box icon.
    :class: theme-icon
.. |plus| image:: /images/plus_F0415.svg
    :alt: The Plus icon provides access to channel and direct message functionality.
    :class: theme-icon
.. |save-icon| image:: /images/bookmark-outline_F00C3.svg
    :alt: Save icon.
    :class: theme-icon
.. |send-icon| image:: /images/send_F048A.svg
    :alt: Select the Send icon to post your message.
    :class: theme-icon
.. |restore-edit| image:: /images/restore_F099B.svg
    :alt: Use the Restore icon to restore a previous version of an edited message.
    :class: theme-icon
    :width: 25
.. |smile-icon| image:: /images/emoticon-plus-outline_E80F.svg
    :alt: Use the Smile icon to add emojis to your message.
    :class: theme-icon
.. |gear| image:: /images/settings-outline_F08BB.svg
    :alt: Use the Settings icon to customize your Mattermost user experience.
    :class: theme-icon
.. |more-icon-vertical| image:: /images/dots-vertical_F01D9.svg
    :alt: Use the More icon in the top left corner to access Mattermost desktop apps customization settings.
    :class: theme-icon
.. |ai-actions-icon| image:: /images/creation-outline_F1C2B.svg
    :alt: Select the AI Actions icon to access AI options.
    :class: theme-icon
.. |bold-icon| image:: /images/format-bold_F0264.svg
    :alt: Bold message text using the Bold icon in the message formatting toolbar.
    :class: theme-icon
.. |italics-icon| image:: /images/format-italic_F0277.svg
    :alt: Italicize message text using the Italic icon in the message formatting toolbar.
    :class: theme-icon
.. |strikeout-icon| image:: /images/format-strikethrough-variant_F0281.svg
    :alt: Strike out message text using the Strikethrough icon in the message formatting toolbar.
    :class: theme-icon
.. |headings-icon| image:: /images/format-header_E81D.svg
    :alt: Format message text as a heading using the Heading icon in the message formatting toolbar. Headings 1 through 6 are supported.
    :class: theme-icon
.. |attachments-icon| image:: /images/paperclip_F03E2.svg
    :alt: Add a message attachment using the Upload files icon in the message formatting toolbar.
    :class: theme-icon
.. |numbered-icon| image:: /images/format-list-numbered_F027B.svg
    :alt: Format message text as a numbered list using the Numbered list icon in the message formatting toolbar.
    :class: theme-icon
.. |bullets-icon| image:: /images/format-list-bulleted_F0279.svg
    :alt: Format message text as a bulleted list using the Bulleted list icon in the message formatting toolbar.
    :class: theme-icon
.. |quotes-icon| image:: /images/format-quote-open_F0757.svg
    :alt: Format message text as a quotation using the Quote icon in the message formatting toolbar.
    :class: theme-icon
.. |code-icon| image:: /images/code-tags_F0174.svg
    :alt: Format message text as code using the Code icon in the message formatting toolbar.
    :class: theme-icon
.. |emoji-icon| image:: /images/emoticon-outline_F01F2.svg
    :alt: Add emojis or GIFs to message text using the Emoji/Gif picker icon in the message formatting toolbar.
    :class: theme-icon
.. |hide-formatting-icon| image:: /images/format-letter-case_F0B34.svg
    :alt: Hide formatting options in the message formatting toolbar using the Show/Hide Formatting icon.
    :class: theme-icon
.. |preview-icon| image:: /images/eye-outline_F06D0.svg
    :alt: Review your message text formatting using the Show/Hide preview icon in the message formatting toolbar.
    :class: theme-icon
.. |message-priority-icon| image:: /images/alert-circle-outline_F05D6.svg
    :alt: Mark a message as important or urgent using the Priority Message icon.
    :class: theme-icon
.. |acknowledge-button| image:: /images/Ack-Button-Default.svg
    :alt: Select the Acknowledge button to indicate that you've read it and taken necessary action.
.. |reply-arrow| image:: /images/reply-outline_F0F20.svg
    :alt: Reply icon.
    :class: theme-icon
.. |product-list| image:: /images/products_E82F.svg
    :alt: Navigate between Channels, collaborative playbooks, and boards using the product menu icon.
    :class: theme-icon
.. |search-icon| image:: /images/magnify_F0349.svg
    :alt: Search for messages and files in Mattermost.
    :class: theme-icon
.. |channel-files-icon| image:: /images/file-text-outline_F09EE.svg
    :alt: Use the Channel Files icon to search for files attached to messages in a given channel.
    :class: theme-icon
.. |download-icon| image:: /images/download-outline_F0B8F.svg
    :alt: Use the Download icon to download an attached file to your local system.
    :class: theme-icon
.. |desktop-download-icon| image:: /images/arrow-down-bold-circle-outline_F0048.svg
    :alt: Use the desktop app download icon to review download status, as well as access and clear the list of downloaded files.
    :class: theme-icon
.. |edit-on-github| image:: /images/edit-on-github.png
    :alt: Contribute to Mattermost documentation by selecting the Edit option located in the top right corner of any documentation page.
    :class: theme-icon
.. |servers-icon| image:: /images/server-variant_E81F.svg
    :alt: Access server connection options using the Servers icon.
    :class: theme-icon
.. |online| image:: /images/online.png
    :alt: Online availability status icon in Mattermost.
.. |away| image:: /images/away.png
    :alt: Away availability status icon in Mattermost.
.. |dnd| image:: /images/dnd.png
    :alt: Do Not Disturb availability status icon in Mattermost.
.. |offline| image:: /images/offline.png
    :alt: Offline availability status icon in Mattermost.
.. |checkmark| image:: /_static/images/check-circle-green.svg
    :alt: Green checkmark icon used to indicate that a given feature is included in a specific package, deployment, or plan.
.. |pinned-messages| image:: /images/pin-outline_F0931.svg
    :alt: Pin icon used to indicate when there are pinned messages in a given channel.
.. |add-user-icon| image:: /images/account-plus-outline_F0801.svg
    :alt: Account plus outline icon used to add user to a channel.
    :class: theme-icon
.. |shared| image:: /images/circle-multiple-outline_F0695.svg
    :alt: Shared icon indicates channels and their members that are shared across connected Mattermost servers.
.. |saved-icon| image:: /images/bookmark_F00C0.svg
    :alt: Saved icon.
    :class: theme-icon
.. |edit-icon| image:: /images/pencil-outline_F0CB6.svg
    :alt: Edit icon.
    :class: theme-icon
.. |scheduled-message-total| image:: /images/schedule-count-red-badge.png
    :alt: Total count of scheduled messages.
"""
# rst_epilog = """
# .. |mm_badge_version| replace:: 7.2
# .. _mm_badge_version: https://mattermost.com/blog/mattermost-v7-2-is-now-available/
# """
