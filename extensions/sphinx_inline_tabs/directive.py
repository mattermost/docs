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

INLINE_TAB_DOCNAMES: Final[str] = "inline_tab_docnames"
"""The key in the Sphinx environment to store a list of documents with inline tabs"""
GENERATED_TAB_IDS: Final[str] = "generated_tab_ids"
"""The key in the Sphinx environment to store a list of generated tab IDs"""

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

        # TabContainer ends up being a <div type="tab">
        container: TabContainer = TabContainer(
            "", type="tab", new_set="new-set" in self.options
        )
        self.set_source_info(container)

        # Handle the label (non-plain-text variants allowed)
        textnodes, messages = self.parse_inline(self.arguments[0], lineno=self.lineno)

        # We want to directly populate the children here.
        label: nodes.label = nodes.label("", "", *textnodes)

        # Handle the content
        parse_titles: bool = "parse-titles" in self.options
        parsed_nodes: list[nodes.Node] = self.parse_content_to_nodes(
            allow_section_headings=parse_titles
        )
        content: nodes.container = nodes.container(
            "",
            *parsed_nodes,
            is_div=True,
            classes=["tab-content"],
            tab_name=self.arguments[0],
        )

        # Add the tab label and content to the container
        container += label
        container += content

        """
        Walk the parsed content and add new `id` attributes on section nodes that
        will be used for HTML page navigation.
        """
        if not hasattr(self.env, GENERATED_TAB_IDS):
            setattr(self.env, GENERATED_TAB_IDS, dict())
        all_generated_tab_ids: dict[str, set[str]] = getattr(self.env, GENERATED_TAB_IDS)
        if self.env.docname not in all_generated_tab_ids:
            all_generated_tab_ids[self.env.docname] = set()
        generated_tab_ids: set[str] = all_generated_tab_ids[self.env.docname]
        self.walk_parsed_nodes(
            [container],
            tab_name=_make_id(self.arguments[0]),
            docname=self.env.docname,
            generated_tab_ids=generated_tab_ids,
        )

        """
        Record the name of this document in a list of documents with tabs in the
        Sphinx environment.
        """
        if not hasattr(self.env, INLINE_TAB_DOCNAMES):
            setattr(self.env, INLINE_TAB_DOCNAMES, [])
        tab_docnames: list[str] = getattr(self.env, INLINE_TAB_DOCNAMES)
        if self.env.docname not in tab_docnames:
            tab_docnames.append(self.env.docname)

        return [container]

    def walk_parsed_nodes(
        self,
        parsed_nodes: list[nodes.Node],
        level: int = 0,
        tab_name: str = "",
        docname: str = "",
        tab_counter: int = 0,
        generated_tab_ids: Optional[set[str]] = None,
    ):
        """
        Recursively walk a docutils node tree, adding new `id` attributes to TabContainer and section nodes.
        The new attributes are used for HTML page navigation.

        :param parsed_nodes: A list of nodes to parse, including children.
        :param level: The current level of recursion. It is used to identify subsection hierarchy.
        :param tab_name: The name of the tab, encoded as a Sphinx `id` attribute.
        :param docname: The document name.
        :param tab_counter: The current tab counter.
        :param generated_tab_ids: A set of generated tab IDs to ensure they are unique in the document.
        :return:
        """
        if generated_tab_ids is None:
            generated_tab_ids = set()
        for parsed_node in parsed_nodes:
            node_info: str = (
                f"type(parsed_node)={type(parsed_node)}; "
                f"has_ids={True if hasattr(parsed_node, 'attributes') and parsed_node.attributes["ids"] else False}; "
                f"parent={parsed_node.parent!r}"
            )
            logger.debug(
                f"{LOG_PREFIX} walk_parsed_nodes({docname}|{tab_name}): [{level}/{tab_counter}] {node_info}"
            )

            if isinstance(parsed_node, TabContainer):
                tab_container_name: str = parsed_node.next_node(nodes.label).astext()
                logger.debug(
                    f"{LOG_PREFIX} walk_parsed_nodes({docname}|{tab_name}): [{level}/{tab_counter}] "
                    f"TabContainer({tab_container_name}); node.tab_counter={parsed_node.tab_counter} "
                    f"is_parsed={parsed_node.is_parsed}; has_ids={True if parsed_node.attributes["ids"] else False}; "
                    f"first_id={parsed_node.attributes['ids'][0] if parsed_node.attributes['ids'] else 'None'}; "
                    f"increment tab_counter to {tab_counter + 1}"
                )
                sub_tab_name: str = tab_name
                if tab_counter > 0:
                    sub_tab_name += f"-{_make_id(tab_container_name)}"
                tab_id: TabId = TabId(
                    tab_name=sub_tab_name,
                    level=level,
                    tab_count=tab_counter + 1,
                    node_id=_make_id(tab_container_name),
                )
                tab_id.ensure_unique(generated_tab_ids)
                parsed_node.tab_counter = tab_counter + 1
                parsed_node.is_parsed = True
                parsed_node.tab_id = tab_id
                logger.debug(
                    f"{LOG_PREFIX} walk_parsed_nodes({docname}|{tab_name}): [{level}/{tab_counter}] {tab_container_name}; set ids to [{str(tab_id)}]"
                )
                parsed_node.attributes["ids"] = [str(tab_id)]
                generated_tab_ids.add(str(tab_id))

            elif isinstance(parsed_node, nodes.section):
                section_title: str = parsed_node.next_node(nodes.title).astext()
                logger.debug(
                    f"{LOG_PREFIX} walk_parsed_nodes({docname}|{tab_name}): [{level}/{tab_counter}] section({section_title}); "
                    f"has_ids={True if parsed_node.attributes["ids"] else False}; "
                    f"first_id={parsed_node.attributes['ids'][0] if parsed_node.attributes['ids'] else 'None'}; "
                )
                # If the node has at least one `id` attribute
                if parsed_node.attributes["ids"]:
                    # Get the first `id` for the node
                    node_id: str = parsed_node.attributes["ids"][0]
                    # Create a new `id` value that includes the tab name, subsection level, and first node `id`
                    new_id: TabId = TabId(
                        tab_name=tab_name,
                        level=level,
                        tab_count=tab_counter,
                        node_id=node_id,
                    )
                    new_id.ensure_unique(generated_tab_ids)
                    logger.debug(
                        f"{LOG_PREFIX} walk_parsed_nodes({docname}|{tab_name}): [{level}/{tab_counter}] section={node_id}, new_id={str(new_id)}"
                    )
                    new_ids: list[str] = [str(new_id)]
                    # Create a new list of `id` attribute values with the new value first
                    for existing_id in parsed_node.attributes["ids"]:
                        new_ids.append(existing_id)
                    # Set the node's `id` attribute to the new list of attribute values
                    logger.debug(
                        f"{LOG_PREFIX} walk_parsed_nodes({docname}|{tab_name}): [{level}/{tab_counter}] set attributes['ids'] to {new_ids}"
                    )
                    parsed_node.attributes["ids"] = new_ids
                    generated_tab_ids.add(str(new_id))
                else:
                    logger.warning(
                        f"{LOG_PREFIX} walk_parsed_nodes({docname}|{tab_name}): [{level}/{tab_counter}] section has no IDs; this is unexpected"
                    )

            # Recurse down through this node's children if there are any
            if hasattr(parsed_node, "children") and parsed_node.children:
                if isinstance(parsed_node, TabContainer):
                    child_tab_name: str = _make_id(
                        parsed_node.next_node(nodes.label).astext()
                    )
                    logger.debug(
                        f"{LOG_PREFIX} walk_parsed_nodes({docname}|{tab_name}): [{level}/{tab_counter}] TabContainer({child_tab_name}); parse {len(parsed_node.children)} children"
                    )
                    self.walk_parsed_nodes(
                        parsed_node.children,
                        level + 1,
                        child_tab_name,
                        docname,
                        tab_counter + 1,
                        generated_tab_ids,
                    )
                else:
                    logger.debug(
                        f"{LOG_PREFIX} walk_parsed_nodes({docname}|{tab_name}): [{level}/{tab_counter}] {type(parsed_node)}(); parse {len(parsed_node.children)} children"
                    )
                    self.walk_parsed_nodes(
                        parsed_node.children, level + 1, tab_name, docname, tab_counter, generated_tab_ids
                    )
