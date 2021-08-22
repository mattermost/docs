#
# sitemap - A fork of the sphinx_sitemap extension with parallel read and write support enabled.
# Based on a sphinx_sitemap PR: https://github.com/jdillard/sphinx-sitemap/pull/29
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

import os
import xml.etree.ElementTree as ET
import sphinx.builders
from sphinx.application import Sphinx, BuildEnvironment
from sphinx.errors import SphinxError
from sphinx.util import logging
from sphinx.util.console import bold, colorize  # type: ignore
from typing import Dict, List

logger = logging.getLogger(__name__)


def error(message: str):
    logger.error(message)


def warning(message: str):
    logger.warning(message)


def info(message: str):
    logger.info(message)


def debug(message: str):
    logger.debug(message)


def setup(app: Sphinx):
    """Setup connects events to the sitemap builder"""
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

    app.connect('builder-inited', record_builder_type)
    app.connect('env-merge-info', env_merge_info)
    app.connect('env-purge-doc', env_purge_doc)
    app.connect('html-collect-pages', create_sitemap)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }


def env_purge_doc(_: Sphinx, env: BuildEnvironment, docname: str):
    debug('env_purge_doc: docname=%s' % docname)
    if hasattr(env, 'sitemap_links'):
        sitemap_links: Dict[str, str] = env.sitemap_links
        if sitemap_links.get(docname) is not None:
            debug('env_purge_doc: sitemap_links contains %s; removing it' % docname)
            sitemap_links.pop(docname)


def env_merge_info(app: Sphinx, env: BuildEnvironment, docnames: List[str], other: BuildEnvironment):
    if not hasattr(env, 'sitemap_links'):
        env.sitemap_links = dict()
    if hasattr(other, 'sitemap_links'):
        other_links: Dict[str, str] = other.sitemap_links
        for linkKey in other_links.keys():
            env.sitemap_links[linkKey] = other_links[linkKey]
    is_dictionary_builder: bool = False
    if app.env is not None and hasattr(app.env, 'is_dictionary_builder'):
        is_dictionary_builder = app.env.is_dictionary_builder
    for docname in docnames:
        link = calculate_link(is_dictionary_builder, docname)
        debug('env_merge_info: docname=%s, link=%s' % (docname, link))
        env.sitemap_links[docname] = link


def calculate_link(is_dictionary_builder: bool, docname: str) -> str:
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
    # Manually configured list of locales
    builder: sphinx.builders.Builder = app.builder
    sitemap_locales = builder.config.sitemap_locales
    if sitemap_locales:
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
    # builder isn't initialized in the setup so we do it here
    # we rely on the class name, not the actual class, as it was moved 2.0.0
    builder = getattr(app, 'builder', None)
    if builder is None:
        return
    app.env.is_dictionary_builder = \
        type(builder).__name__ == 'DirectoryHTMLBuilder'


def hreflang_formatter(lang: str) -> str:
    """
    sitemap hreflang should follow correct format.
        Use hyphen instead of underscore in language and country value.
    ref: https://en.wikipedia.org/wiki/Hreflang#Common_Mistakes
    source: https://github.com/readthedocs/readthedocs.org/pull/5638
    """
    if '_' in lang:
        return lang.replace("_", "-")
    return lang


def create_sitemap(app: Sphinx):
    """Generates the sitemap.xml from the collected HTML page links"""
    site_url = app.builder.config.site_url or app.builder.config.html_baseurl
    if not site_url:
        error("sphinx-sitemap: Neither html_baseurl nor site_url "
              "are set in conf.py. Sitemap not built.")
        return
    site_url = site_url.rstrip('/') + '/'

    if app.env is None:
        error("sphinx-sitemap: environment is None; this is unexpected")
        return
    sitemap_links: Dict[str, str] = dict()
    if hasattr(app.env, 'sitemap_links'):
        sitemap_links = app.env.sitemap_links

    # if env.sitemap_links.empty():
    if len(sitemap_links) == 0:
        warning("sphinx-sitemap: No pages generated for %s" % app.config.sitemap_filename)
        return

    ET.register_namespace('xhtml', "http://www.w3.org/1999/xhtml")
    root = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    locales = get_locales(app)

    if app.builder.config.version:
        version = app.builder.config.version + '/'
    else:
        version = ""

    for linkKey in sitemap_links.keys():
        link = sitemap_links[linkKey]
        url = ET.SubElement(root, "url")
        scheme = app.config.sitemap_url_scheme
        if app.builder.config.language:
            lang = app.builder.config.language + '/'
        else:
            lang = ""

        ET.SubElement(url, "loc").text = site_url + scheme.format(
            lang=lang, version=version, link=link
        )

        for lang in locales:
            lang = lang + '/'
            ET.SubElement(
                url, "{http://www.w3.org/1999/xhtml}link",
                rel="alternate",
                hreflang=hreflang_formatter(lang.rstrip('/')),
                href=site_url + scheme.format(
                    lang=lang, version=version, link=link
                )
            )

    filename = app.outdir + "/" + app.config.sitemap_filename
    logger.info(bold('writing sitemap... '), nonl=True)
    ET.ElementTree(root).write(filename,
                               xml_declaration=True,
                               encoding='utf-8',
                               method="xml")
    info("done; generated sitemap in %s" % filename)
    return []
