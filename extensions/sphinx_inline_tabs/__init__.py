"""Add inline tabbed content to your Sphinx documentation."""

import os

__version__ = "2025.05.05"
__all__ = ["setup"]


def setup(app):
    """Entry point for sphinx theming."""
    app.require_sphinx("7.4")

    # We do imports from Sphinx, after validating the Sphinx version
    from ._impl import TabDirective, TabHtmlTransform
    from .nodes import (
        TabContainer, TabInput, TabLabel, TabAnchor,
        visit_anchor_node, depart_anchor_node
    )
    from .sphinx import (
        env_purge_doc, env_merge_info, doctree_read
    )

    app.add_directive("tab", TabDirective)
    app.add_post_transform(TabHtmlTransform)
    app.add_node(TabInput, html=(TabInput.visit, TabInput.depart))
    app.add_node(TabLabel, html=(TabLabel.visit, TabLabel.depart))
    app.add_node(TabAnchor, html=(visit_anchor_node, depart_anchor_node))
    app.add_node(TabContainer, xml=(lambda _, __: None, lambda _, __: None))

    # Include our static assets
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    app.connect(
        "builder-inited", (lambda app: app.config.html_static_path.append(static_dir))
    )
    app.connect("env-purge-doc", env_purge_doc)
    app.connect("env-merge-info", env_merge_info)
    app.connect("doctree-read", doctree_read)

    app.add_js_file("tabs.js")
    app.add_css_file("tabs.css")

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "version": __version__,
    }
