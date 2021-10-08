'''
sitemap - The sphinx_sitemap extension with parallel read and write support enabled

Parallel read/write support by Alan Lew <alan@ethereal.cc> (https://github.com/neflyte/)

Copyright (c) 2013 Michael Dowling <mtdowling@gmail.com>
Copyright (c) 2017 Jared Dillard <jared.dillard@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
'''
import os
import sphinx.builders
from typing import Dict, List, Optional, Tuple, Any
from xml.etree import ElementTree
from sphinx.application import Sphinx, BuildEnvironment
from sphinx.errors import SphinxError
from sphinx.util import logging
from sphinx.util.console import bold, colorize  # type: ignore

# Sphinx logger
logger = logging.getLogger(__name__)


def setup(app: Sphinx) -> Dict[str, Any]:
    """
    Sphinx extension setup function.
    It adds config values and connects Sphinx events to the sitemap builder.

    :param app: The Sphinx Application instance
    :return: A dict of Sphinx extension options
    """
    app.add_config_value(
        'site_url',
        default=None,
        rebuild=''
    )
    app.add_config_value(
        'sitemap_url_scheme',
        default="{lang}{link}",
        rebuild=''
    )
    app.add_config_value(
        'sitemap_locales',
        default=None,
        rebuild=''
    )
    app.add_config_value(
        'sitemap_filename',
        default="sitemap.xml",
        rebuild=''
    )

    try:
        app.add_config_value(
            'html_baseurl',
            default=None,
            rebuild=''
        )
    except SphinxError:
        pass

    """
    Determine the type of Builder used when the `builder-inited` event fires.
    https://www.sphinx-doc.org/en/master/extdev/appapi.html#event-builder-inited
    """
    app.connect('builder-inited', record_builder_type)
    """
    Merge collected document information from parallel readers (workers) when the `env-merge-info` event fires.
    https://www.sphinx-doc.org/en/master/extdev/appapi.html#event-env-merge-info
    """
    app.connect('env-merge-info', env_merge_info)
    """
    Remove references to documents that no longer exist when the `env-purge-doc` event fires.
    https://www.sphinx-doc.org/en/master/extdev/appapi.html#event-env-purge-doc
    """
    app.connect('env-purge-doc', env_purge_doc)
    """
    Write the sitemap when the `html-collect-pages` event fires.
    https://www.sphinx-doc.org/en/master/extdev/appapi.html#event-html-collect-pages
    """
    app.connect('html-collect-pages', create_sitemap)

    return {
        # Enable parallel reading and writing
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }


def env_purge_doc(app: Sphinx, env: BuildEnvironment, docname: str):
    """
    Purge an existing document from the pickled document list.
    This function is called when the Sphinx `env-purge-doc` event is fired.

    :param app: The Sphinx instance; unused
    :param env: The Sphinx BuildEnvironment
    :param docname: The name of the document to purge
    """
    logger.debug('env_purge_doc: docname=%s' % docname)
    if hasattr(env, 'sitemap_links'):
        sitemap_links: Dict[str, str] = env.sitemap_links
        if sitemap_links.get(docname) is not None:
            logger.debug('env_purge_doc: sitemap_links contains %s; removing it' % docname)
            env.sitemap_links.pop(docname)


def env_merge_info(app: Sphinx, env: BuildEnvironment, docnames: List[str], other: BuildEnvironment):
    """
    Merge collected document names from parallel readers (workers) into the master Sphinx environment.
    This function is called when the Sphinx `env-merge-info` event is fired.

    :param app: The Sphinx Application instance
    :param env: The master Sphinx BuildEnvironment
    :param docnames: A list of the document names to merge
    :param other: The Sphinx BuildEnvironment from the reader worker
    """
    # Create a `sitemap_links` attribute in the environment if it doesn't already exist
    if not hasattr(env, 'sitemap_links'):
        env.sitemap_links = dict()
    # Add any links that were present in the reader worker's environment
    if hasattr(other, 'sitemap_links'):
        other_links: Dict[str, str] = other.sitemap_links
        for linkKey in other_links.keys():
            env.sitemap_links[linkKey] = other_links[linkKey]
    # Determine if we're using a DirectoryHTMLBuilder or not
    is_dictionary_builder: bool = False
    if app.env is not None and hasattr(app.env, 'is_dictionary_builder'):
        is_dictionary_builder = app.env.is_dictionary_builder
    # Calculate the document link for each docname and add it to the `sitemap_links` attribute in the environment
    for docname in docnames:
        link = calculate_link(is_dictionary_builder, docname)
        logger.debug('env_merge_info: docname=%s, link=%s' % (docname, link))
        env.sitemap_links[docname] = link


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
    return docname + ".html"


def get_locales(app: Sphinx) -> List[str]:
    """
    Get a list of locales from the extension config or automatically detect based on Sphinx Application config.

    :param app: The Sphinx Application instance
    :return: A list of locales
    """
    # Manually configured list of locales
    builder: sphinx.builders.Builder = app.builder
    sitemap_locales: Optional[List[str]] = builder.config.sitemap_locales
    if sitemap_locales is not None:
        # special value to add nothing -> use primary language only
        if sitemap_locales == [None]:
            return []

        return [
            locale for locale in sitemap_locales
            # skip primary language
            if locale != app.builder.config.language
        ]

    # Or autodetect
    locales: List = list()
    for locale_dir in app.builder.config.locale_dirs:
        locale_dir = os.path.join(app.confdir, locale_dir)
        if os.path.isdir(locale_dir):
            for locale in os.listdir(locale_dir):
                if os.path.isdir(os.path.join(locale_dir, locale)):
                    locales.append(locale)
    return locales


def record_builder_type(app: Sphinx):
    """
    Determine if the Sphinx Builder is an instance of DirectoryHTMLBuilder and store that in the
    application environment.

    :param app: The Sphinx Application instance
    """
    # builder isn't initialized in the setup so we do it here
    # we rely on the class name, not the actual class, as it was moved 2.0.0
    builder = getattr(app, 'builder', None)
    if builder is None:
        return
    app.env.is_dictionary_builder = \
        type(builder).__name__ == 'DirectoryHTMLBuilder'


def hreflang_formatter(lang: str) -> str:
    """
    Format the supplied locale code into a string that is compatible with `hreflang`.

    See also:

    https://en.wikipedia.org/wiki/Hreflang#Common_Mistakes

    https://github.com/readthedocs/readthedocs.org/pull/5638

    :param lang: The locale string to format
    :return: The formatted locale string
    """
    if '_' in lang:
        return lang.replace("_", "-")
    return lang


def create_sitemap(app: Sphinx) -> List[Tuple[str, Dict[str, Any], str]]:
    """
    Generates the sitemap.xml from the collected HTML page links.
    This function is called when the Sphinx `html-collect-pages` event is fired.

    :param app: The Sphinx Application instance
    :return: An empty list
    """
    # Initialize the empty return list
    return_list = list()
    # Retrieve the `site_url` config property
    site_url = app.builder.config.site_url or app.builder.config.html_baseurl
    if not site_url:
        logger.error("sphinx-sitemap: Neither html_baseurl nor site_url "
                     "are set in conf.py. Sitemap not built.")
        return return_list
    site_url = site_url.rstrip('/') + '/'
    # Retrieve the collected document links
    if app.env is None:
        logger.error("sphinx-sitemap: environment is None; this is unexpected")
        return return_list
    sitemap_links: Dict[str, str] = dict()
    if hasattr(app.env, 'sitemap_links'):
        sitemap_links = app.env.sitemap_links
    if len(sitemap_links) == 0:
        logger.warning("sphinx-sitemap: No pages generated for %s" % app.config.sitemap_filename)
        return return_list
    # Create a new XML root element
    ElementTree.register_namespace('xhtml', "http://www.w3.org/1999/xhtml")
    root = ElementTree.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    # Get the list of locales to include
    locales = get_locales(app)
    # Retrieve the `version` config property
    if app.builder.config.version:
        version = app.builder.config.version + '/'
    else:
        version = ""
    # Retrieve the `sitemap_url_scheme` config property
    scheme = app.config.sitemap_url_scheme
    # Retrieve the `language` config property
    if app.builder.config.language:
        lang = app.builder.config.language + '/'
    else:
        lang = ""
    # Add each document link as a child of the root XML element
    for linkKey in sitemap_links.keys():
        # Retrieve the linked document filename including extension
        link = sitemap_links[linkKey]
        # Create a new XML child element of the root element for this link
        url = ElementTree.SubElement(root, "url")
        ElementTree.SubElement(url, "loc").text = site_url + scheme.format(
            lang=lang, version=version, link=link
        )
        # Add a sub-element for each locale
        for lang in locales:
            lang = lang + '/'
            ElementTree.SubElement(
                url, "{http://www.w3.org/1999/xhtml}link",
                rel="alternate",
                hreflang=hreflang_formatter(lang.rstrip('/')),
                href=site_url + scheme.format(
                    lang=lang, version=version, link=link
                )
            )
    # Determine the output filename of the sitemap and write the XML document to it
    filename = app.outdir + "/" + app.config.sitemap_filename
    logger.info(bold('writing sitemap... '), nonl=True)
    ElementTree.ElementTree(root).write(filename,
                                        xml_declaration=True,
                                        encoding='utf-8',
                                        method="xml")
    logger.info("done; generated sitemap in %s" % filename)
    # Return the empty list
    return return_list
