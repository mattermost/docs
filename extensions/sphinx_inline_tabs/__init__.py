"""
Add inline tabbed content to your Sphinx documentation
by: Pradyun Gedam <mail@pradyunsg.me> (https://github.com/pradyunsg/sphinx-inline-tabs)

Support for inline tab subsections in page Table of Contents
by: Alan Lew <alan@ethereal.cc> (https://github.com/neflyte/)
"""

import os
from sphinx.application import Sphinx

__version__: str = "2023.04.21"
__all__: list[str] = ["setup"]


def setup(app: Sphinx):
    """
    Entry point for sphinx theming.

    :param app: Sphinx application.
    """
    app.require_sphinx("8.2")

    # We do imports from Sphinx after validating the Sphinx version
    from .directive import TabDirective
    from .transform import TabHtmlTransform
    from .nodes import TabContainer, TabInput, TabLabel, TabSpan
    from .events import env_purge_doc, env_merge_info, doctree_read, html_page_context

    app.add_directive("tab", TabDirective)
    app.add_post_transform(TabHtmlTransform)
    app.add_node(TabInput, html=(TabInput.visit, TabInput.depart))
    app.add_node(TabLabel, html=(TabLabel.visit, TabLabel.depart))
    app.add_node(TabSpan, html=(TabSpan.visit, TabSpan.depart))
    app.add_node(TabContainer, xml=(lambda _, __: None, lambda _, __: None))

    # Include our static assets
    static_dir: str = os.path.join(os.path.dirname(__file__), "static")
    app.connect(
        "builder-inited", (lambda app: app.config.html_static_path.append(static_dir))
    )
    app.connect("env-purge-doc", env_purge_doc)
    app.connect("env-merge-info", env_merge_info)
    app.connect("doctree-read", doctree_read)
    app.connect("html-page-context", html_page_context)

    app.add_js_file("tabs.js")
    app.add_css_file("tabs.css")

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
