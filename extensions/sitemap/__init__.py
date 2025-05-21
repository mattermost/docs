#
# sitemap - The sphinx_sitemap extension with parallel read and write support enabled
#
# Parallel read/write support by Alan Lew <alan@ethereal.cc> (https://github.com/neflyte/)
#
# Copyright (c) 2013 Michael Dowling <mtdowling@gmail.com>
# Copyright (c) 2017 Jared Dillard <jared.dillard@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

from pathlib import Path
from typing import Any, Final
from xml.etree import ElementTree

from docutils import nodes
from sphinx.application import Sphinx, BuildEnvironment
from sphinx.errors import SphinxError
from sphinx.util import logging
from sphinx.util.console import bold, colorize  # type: ignore
from sphinx.util.logging import SphinxLoggerAdapter

# Sphinx logger
logger: SphinxLoggerAdapter = logging.getLogger(__name__)
LOG_PREFIX: Final[str] = "[sitemap]"


def setup(app: Sphinx) -> dict[str, Any]:
    """
    Sphinx extension setup function.
    It adds config values and connects Sphinx events to the sitemap builder.

    :param app: The Sphinx Application instance
    :return: A dict of Sphinx extension options
    """
    app.add_config_value("site_url", default=None, rebuild="")
    app.add_config_value("sitemap_url_scheme", default="{link}", rebuild="")
    app.add_config_value("sitemap_locales", default=None, rebuild="")
    app.add_config_value("sitemap_filename", default="sitemap.xml", rebuild="")

    try:
        app.add_config_value("html_baseurl", default=None, rebuild="")
    except SphinxError:
        pass

    """
    Determine the type of Builder used when the `builder-inited` event fires.
    https://www.sphinx-doc.org/en/master/extdev/appapi.html#event-builder-inited
    """
    app.connect("builder-inited", record_builder_type)
    """
    Merge collected document information from parallel readers (workers) when the `env-merge-info` event fires.
    https://www.sphinx-doc.org/en/master/extdev/appapi.html#event-env-merge-info
    """
    app.connect("env-merge-info", env_merge_info)
    """
    Remove references to documents that no longer exist when the `env-purge-doc` event fires.
    https://www.sphinx-doc.org/en/master/extdev/appapi.html#event-env-purge-doc
    """
    app.connect("env-purge-doc", env_purge_doc)
    """
    Write the sitemap when the `html-collect-pages` event fires.
    https://www.sphinx-doc.org/en/master/extdev/appapi.html#event-html-collect-pages
    """
    app.connect("html-collect-pages", create_sitemap)
    """
    Create the sitemap link for a document when the `doctree-read` event fires.
    https://www.sphinx-doc.org/en/master/extdev/event_callbacks.html#event-doctree-read
    """
    app.connect("doctree-read", doctree_read)

    return {
        # Enable parallel reading and writing
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def env_purge_doc(app: Sphinx, _: BuildEnvironment, docname: str):
    """
    Purge an existing document from the pickled document list.
    This function is called when the Sphinx `env-purge-doc` event is fired.

    :param app: The Sphinx instance
    :param _: The Sphinx BuildEnvironment object; unused
    :param docname: The name of the document to purge
    """
    logger.debug(f"{LOG_PREFIX} env_purge_doc: docname={docname}")
    if hasattr(app.env, "sitemap_links"):
        if docname in app.env.sitemap_links:
            logger.debug(
                f"{LOG_PREFIX} env_purge_doc: sitemap_links contains {docname}; removing it"
            )
            app.env.sitemap_links.pop(docname)


def env_merge_info(
    app: Sphinx, _: BuildEnvironment, docnames: list[str], other: BuildEnvironment
):
    """
    Merge collected document names from parallel readers (workers) into the master Sphinx environment.
    This function is called when the Sphinx `env-merge-info` event is fired.

    :param app: The Sphinx Application instance
    :param _: The master Sphinx BuildEnvironment object; unused
    :param docnames: A list of the document names to merge
    :param other: The Sphinx BuildEnvironment from the reader worker
    """
    # Create a `sitemap_links` attribute in the environment if it doesn't already exist
    if not hasattr(app.env, "sitemap_links"):
        app.env.sitemap_links = {}
    # Add any links that were present in the reader worker's environment
    if hasattr(other, "sitemap_links"):
        for docname in docnames:
            if docname in other.sitemap_links:
                app.env.sitemap_links[docname] = f"{other.sitemap_links[docname]}"


def doctree_read(app: Sphinx, doctree: nodes.document):
    """
    Create the sitemap link for a document after it has been read

    :param app: The Sphinx Application instance
    :param doctree: The parsed document tree; unused
    """
    # Create a `sitemap_links` attribute in the environment if it doesn't already exist
    if not hasattr(app.env, "sitemap_links"):
        logger.debug(f"{LOG_PREFIX} doctree_read: create app.env.sitemap_links")
        app.env.sitemap_links = {}
    # Determine if we're using a DirectoryHTMLBuilder or not
    is_dictionary_builder: bool = False
    if hasattr(app.env, "is_dictionary_builder"):
        is_dictionary_builder = app.env.is_dictionary_builder
    # Calculate the document link for this document and add it to the `sitemap_links` attribute in the environment
    app.env.sitemap_links[app.env.docname] = calculate_link(is_dictionary_builder, app.env.docname)


def calculate_link(is_dictionary_builder: bool, docname: str) -> str:
    """
    Calculate the resulting file name or directory page name from the supplied document name.
    Both StandaloneHTMLBuilder and DirectoryHTMLBuilder builders are handled.

    :param is_dictionary_builder: Whether or not this builder is an instance of DirectoryHTMLBuilder
    :param docname: The name of the document to calculate the file name of
    :return: The calculated file name or directory page name
    """
    if is_dictionary_builder:
        if docname == "index":
            # root of the entire website, a special case
            directory_pagename = ""
        elif docname.endswith("/index"):
            # checking until / to avoid false positives like /funds-index
            directory_pagename = docname[:-6] + "/"
        else:
            directory_pagename = docname + "/"
        return directory_pagename
    return f"{docname}.html"


def get_locales(app: Sphinx) -> list[str]:
    """
    Get a list of locales from the extension config or automatically detect based on Sphinx Application config.

    :param app: The Sphinx Application instance
    :return: A list of locales
    """
    # Manually configured list of locales
    if app.builder.config.sitemap_locales is not None:
        # special value to add nothing -> use primary language only
        if app.builder.config.sitemap_locales == [None]:
            return []

        return [
            locale
            for locale in app.builder.config.sitemap_locales
            # skip primary language
            if locale != app.builder.config.language
        ]
    # Or autodetect
    locales: list[str] = []
    for locale_dir in app.builder.config.locale_dirs:
        locale_path: Path = Path(app.confdir) / locale_dir
        if locale_path.is_dir():
            for locale_subpath in locale_path.iterdir():
                if not locale_subpath.is_dir():
                    continue
                locale_dir_locale: Path = Path(locale_dir) / locale_subpath.name
                if locale_dir_locale.is_dir():
                    locales.append(locale_dir_locale.name)
    return locales


def record_builder_type(app: Sphinx):
    """
    Determine if the Sphinx Builder is an instance of DirectoryHTMLBuilder and store that in the
    application environment.

    :param app: The Sphinx Application instance
    """
    # builder isn't initialized in the setup so we do it here
    # we rely on the class name, not the actual class, as it was moved 2.0.0
    builder = getattr(app, "builder", None)
    if builder is None:
        return
    app.env.is_dictionary_builder = type(builder).__name__ == "DirectoryHTMLBuilder"


def hreflang_formatter(lang: str) -> str:
    """
    Format the supplied locale code into a string that is compatible with `hreflang`.

    See also:

    https://en.wikipedia.org/wiki/Hreflang#Common_Mistakes

    https://github.com/readthedocs/readthedocs.org/pull/5638

    :param lang: The locale string to format
    :return: The formatted locale string
    """
    if "_" in lang:
        return lang.replace("_", "-")
    return lang


def create_sitemap(app: Sphinx) -> list[tuple[str, dict[str, Any], str]]:
    """
    Generates the sitemap.xml from the collected HTML page links.
    This function is called when the Sphinx `html-collect-pages` event is fired.

    :param app: The Sphinx Application instance
    :return: An empty list
    """
    # Initialize the empty return list
    return_list: list[tuple[str, dict[str, Any], str]] = []
    # Retrieve the `site_url` config property
    site_url: str = app.builder.config.site_url or app.builder.config.html_baseurl
    if not site_url:
        logger.error(
            f"{LOG_PREFIX} create_sitemap: Neither html_baseurl nor site_url "
            "are set in conf.py. Sitemap not built."
        )
        return return_list
    site_url = site_url.rstrip("/") + "/"
    # Retrieve the collected document links
    if not hasattr(app.env, "sitemap_links") or app.env.sitemap_links == []:
        logger.warning(
            f"{LOG_PREFIX} create_sitemap: No pages generated for {app.config.sitemap_filename}"
        )
        return return_list
    # Create a new XML root element
    ElementTree.register_namespace("xhtml", "http://www.w3.org/1999/xhtml")
    root: ElementTree.Element = ElementTree.Element(
        "urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    )
    # Get the list of locales to include
    locales: list[str] = get_locales(app)
    # Retrieve the `version` config property
    version: str = ""
    if app.builder.config.version:
        version = f"{app.builder.config.version}/"
    # Retrieve the `sitemap_url_scheme` config property
    scheme: str = app.config.sitemap_url_scheme
    # Retrieve the `language` config property
    lang: str = ""
    if app.builder.config.language:
        lang = "{app.builder.config.language}/"
    # Add each document link as a child of the root XML element
    for link_key, link in app.env.sitemap_links.items():
        # Create a new XML child element of the root element for this link
        url: ElementTree.Element = ElementTree.SubElement(root, "url")
        ElementTree.SubElement(url, "loc").text = (
            f"{site_url}{scheme.format(lang=lang, version=version, link=link)}"
        )
        # Add a sub-element for each locale
        for locale in locales:
            locale_name = f"{locale}/"
            ElementTree.SubElement(
                url,
                "{http://www.w3.org/1999/xhtml}link",
                rel="alternate",
                hreflang=hreflang_formatter(lang.rstrip("/")),
                href=f"{site_url}{scheme.format(lang=locale_name, version=version, link=link)}",
            )
    # Determine the output filename of the sitemap and write the XML document to it
    filename: Path = Path(app.outdir) / app.config.sitemap_filename
    logger.info(bold("writing sitemap... "), nonl=True)
    ElementTree.ElementTree(root).write(
        str(filename), xml_declaration=True, encoding="utf-8", method="xml"
    )
    logger.info(f"done; generated sitemap in {str(filename)}")
    # Return the empty list
    return return_list
