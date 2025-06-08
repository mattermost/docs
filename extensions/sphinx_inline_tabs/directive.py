"""
Sphinx directive implementation.
"""
from typing import Final

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import _make_id

from .nodes import TabContainer


logger: logging.SphinxLoggerAdapter = logging.getLogger(__name__)
LOG_PREFIX: Final[str] = "[sphinx_inline_tabs]"


class TabDirective(SphinxDirective):
    """Tabbed content in Sphinx documentation."""

    required_arguments = 1  # directive takes a single argument.
    final_argument_whitespace = True  # this allows that argument to contain spaces.
    has_content = True
    option_spec = {
        "new-set": directives.flag,  # Indicates that this tab should start a new tab set
        "parse-titles": directives.flag,  # Indicates that section titles in the content should be parsed
    }

    def run(self) -> list[nodes.Node]:
        """
        Parse a `tabs` directive.

        :return: A list of docutils nodes that will replace the directive.
        """
        self.assert_has_content()

        container: TabContainer = TabContainer(
            "", type="tab", new_set="new-set" in self.options
        )
        self.set_source_info(container)

        tab_id: str = _make_id(self.arguments[0])
        container.attributes["tab_name"] = self.arguments[0]
        container.attributes["inline_tab_id"] = (
            f"inlinetab--{tab_id}--0-{self.arguments[0]}"
        )

        # Handle the label (non-plain-text variants allowed)
        textnodes, messages = self.parse_inline(self.arguments[0], lineno=self.lineno)
        # The signature of this object is:
        #     __init__(self, rawsource='', text='', *children, **attributes)
        #
        # We want to directly populate the children here.
        label: nodes.label = nodes.label("", "", *textnodes)

        # Handle the content
        content: nodes.container = nodes.container(
            "", is_div=True, classes=["tab-content"]
        )

        parse_titles = "parse-titles" in self.options
        parsed_nodes: list[nodes.Node] = self.parse_content_to_nodes(
            allow_section_headings=parse_titles
        )

        """
        Walk the parsed content and add new `id` attributes on section nodes that
        will be used for HTML page navigation.
        """
        self.walk_parsed_nodes(parsed_nodes, tab_name=tab_id)

        # Add the parsed content to the content node
        for parsed_node in parsed_nodes:
            content += parsed_node

        container += label
        container += content

        """
        Record the name of this tab in a list of tabs for this document in the
        Sphinx environment.
        """
        if not hasattr(self.env, "sphinx_tabs"):
            self.env.sphinx_tabs = {}
        if self.env.docname not in self.env.sphinx_tabs:
            self.env.sphinx_tabs[self.env.docname] = []
        self.env.sphinx_tabs[self.env.docname].append(self.arguments[0])

        return [container]

    def walk_parsed_nodes(
        self, parsed_nodes: list[nodes.Node], level: int = 0, tab_name: str = ""
    ):
        """
        Recursively walk a docutils node tree, adding new `id` attributes to section nodes.
        The new attributes are used for HTML page navigation.

        :param parsed_nodes: A list of nodes to parse, including children.
        :param level: The current level of recursion. It is used to identify subsection hierarchy.
        :param tab_name: The name of the tab, encoded as a Sphinx `id` attribute.
        :return:
        """
        for parsed_node in parsed_nodes:
            logger.debug(f"{LOG_PREFIX} walk_parsed_nodes(): parsed_node={parsed_node.astext()}")
            # Only add a new `id` attribute on section nodes
            if isinstance(parsed_node, nodes.section):
                # If the node has at least one `id` attribute
                if parsed_node.attributes["ids"]:
                    # Get the first `id` for the node
                    node_id: str = parsed_node.attributes["ids"][0]
                    logger.debug(f"{LOG_PREFIX} walk_parsed_nodes(): [{level}] section: {node_id}")
                    # Create a new `id` value that includes the tab name, subsection level, and first node `id`
                    new_ids: list[str] = [f"inlinetab--{tab_name}--{level}-{node_id}"]
                    # Create a new list of `id` attribute values with the new value first
                    for existing_id in parsed_node.attributes["ids"]:
                        new_ids.append(existing_id)
                    # Set the node's `id` attribute to the new list of attribute values
                    parsed_node.attributes["ids"] = new_ids
            # Recurse down through this node's children if there are any
            if parsed_node.children is not None:
                logger.debug(
                    f"{LOG_PREFIX} walk_parsed_nodes(): [{level}] parse {len(parsed_node.children)} children"
                )
                self.walk_parsed_nodes(parsed_node.children, level + 1, tab_name)
