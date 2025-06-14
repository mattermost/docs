"""
Sphinx directive implementation.
"""
from typing import Final, Optional

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import _make_id

from .nodes import TabContainer
from .tab_id import TabId


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

        tab_id: TabId = TabId(tab_name=self.arguments[0], level=0, tab_count=0, node_id=self.arguments[0])
        container.attributes["tab_name"] = self.arguments[0]
        container.attributes["inline_tab_id"] = str(tab_id)

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

        parse_titles: bool = "parse-titles" in self.options
        parsed_nodes: list[nodes.Node] = self.parse_content_to_nodes(
            allow_section_headings=parse_titles
        )

        """
        Walk the parsed content and add new `id` attributes on section nodes that
        will be used for HTML page navigation.
        """
        self.walk_parsed_nodes(parsed_nodes, tab_name=_make_id(self.arguments[0]), docname=self.env.docname)

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
        self, parsed_nodes: list[nodes.Node], level: int = 0, tab_name: str = "", docname: str = "", tab_counter: int = 0
    ):
        """
        Recursively walk a docutils node tree, adding new `id` attributes to section nodes.
        The new attributes are used for HTML page navigation.

        :param parsed_nodes: A list of nodes to parse, including children.
        :param level: The current level of recursion. It is used to identify subsection hierarchy.
        :param tab_name: The name of the tab, encoded as a Sphinx `id` attribute.
        :param docname: The document name.
        :param tab_counter: The current tab counter.
        :return:
        """
        for parsed_node in parsed_nodes:
            logger.debug(f"{LOG_PREFIX} walk_parsed_nodes({docname}): [{level}/{tab_counter}] parsed_node={type(parsed_node)}")
            parent_node: Optional[nodes.Element] = parsed_node if isinstance(parsed_node, nodes.Element) else None

            if isinstance(parsed_node, TabContainer):
                tab_container_name: str = parsed_node.next_node(nodes.label).astext()
                logger.info(f"{LOG_PREFIX} walk_parsed_nodes({docname}): [{level}/{tab_counter}] node is a TabContainer({tab_container_name}); increment tab_counter to {tab_counter + 1}")
                parsed_node.tab_counter = tab_counter + 1
                # if parsed_node.attributes["ids"]:
                #     tab_container_id: str = parsed_node.attributes["ids"][0]
                #     tab_id = TabId.from_str(tab_container_id)
                #     if tab_id is not None:
                #         tab_id.tab_count = parsed_node.tab_counter
                #         logger.info(f"{LOG_PREFIX} walk_parsed_nodes({docname}): [{level}/{tab_counter}] {tab_container_name}; update ids[0] from {tab_container_id} to {str(tab_id)}")
                #         parsed_node.attributes["ids"][0] = str(tab_id)
                # else:
                sub_tab_name: str = f"{tab_name}-{_make_id(tab_container_name)}"
                tab_id = TabId(tab_name=sub_tab_name, level=level, tab_count=parsed_node.tab_counter, node_id=tab_container_name)
                logger.info(f"{LOG_PREFIX} walk_parsed_nodes({docname}): [{level}/{tab_counter}] {tab_container_name}; set ids[0] to {str(tab_id)}")
                parsed_node.attributes["ids"] = [str(tab_id)]
                parent_node = parsed_node.next_node(nodes.container)
            elif isinstance(parsed_node, nodes.section):
                # If the node has at least one `id` attribute
                if parsed_node.attributes["ids"]:
                    # Get the first `id` for the node
                    node_id: str = parsed_node.attributes["ids"][0]
                    # Create a new `id` value that includes the tab name, subsection level, and first node `id`
                    new_id: TabId = TabId(tab_name=tab_name, level=level, tab_count=tab_counter, node_id=node_id)
                    logger.info(f"{LOG_PREFIX} walk_parsed_nodes({docname}): [{level}/{tab_counter}] section={node_id}, new_id={str(new_id)}")
                    new_ids: list[str] = [str(new_id)]
                    # Create a new list of `id` attribute values with the new value first
                    for existing_id in parsed_node.attributes["ids"]:
                        new_ids.append(existing_id)
                    # Set the node's `id` attribute to the new list of attribute values
                    parsed_node.attributes["ids"] = new_ids

            # Recurse down through this node's children if there are any
            if parent_node is not None and parent_node.children is not None:
                logger.debug(
                    f"{LOG_PREFIX} walk_parsed_nodes({docname}): [{level}/{tab_counter}] parse {len(parent_node.children)} children"
                )
                if isinstance(parsed_node, TabContainer):
                    child_tab_name: str = parsed_node.next_node(nodes.label).astext()
                    self.walk_parsed_nodes(parent_node.children, level + 1, child_tab_name, docname, tab_counter + 1)
                else:
                    self.walk_parsed_nodes(parent_node.children, level + 1, tab_name, docname, tab_counter)
