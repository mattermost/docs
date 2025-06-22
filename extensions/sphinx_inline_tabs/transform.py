import itertools
from typing import Optional, List

from docutils import nodes
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging
from sphinx.util.nodes import NodeMatcher

from .directive import LOG_PREFIX
from .nodes import TabContainer, TabInput, TabLabel, TabSpan
from .tab_id import TabId


logger: logging.SphinxLoggerAdapter = logging.getLogger(__name__)
"""The Sphinx logger"""


class TabHtmlTransform(SphinxPostTransform):
    """Transform output of TabDirective into usable chunks."""

    default_priority: int = 200
    formats: list[str] = ["html"]
    stack: list[list[TabContainer]]
    counter: itertools.count

    def run(self):
        """Locate and replace `TabContainer`s."""
        self.stack = []
        self.counter = itertools.count(start=0, step=1)

        # for node in self.document.findall(
        #     NodeMatcher(TabContainer)
        # ):  # type: TabContainer
        #     logger.info(f"{LOG_PREFIX} TabHtmlTransform.run ({self.env.docname}) process TabContainer {node.tab_identifier()})")
        #     self._process_one_node(node)
        self._process_nodes([self.document])

        while self.stack:
            TabHtmlTransform.finalize_set(
                self.stack.pop(),
                next(self.counter),
            )

    def _process_nodes(self, node_list: list[nodes.Node]):
        for node in node_list:
            if isinstance(node, TabContainer):
                logger.info(f"{LOG_PREFIX} _process_nodes ({self.env.docname}) TabContainer: {node.tab_identifier()}")
                self._process_one_node(node)
            #elif isinstance(node, nodes.section):
            #    logger.info(f"{LOG_PREFIX} _process_nodes ({self.env.docname}) section: {TabHtmlTransform.element_id(node)}")
            if hasattr(node, "children") and node.children:
                self._process_nodes(node.children)

    def _process_one_node(self, node: TabContainer):
        # There is no existing tab set. Let's start a new one.
        if not self.stack:
            logger.info(f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) no existing tab set; start a new one")
            self.stack.append([node])
            return

        # There should never be an empty "current" tab set.
        assert self.stack[-1]

        close_till: Optional[list[TabContainer]] = None
        append: bool = False
        logger.info(f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) process {len(self.stack)} stack tab-sets in reverse order")
        for tab_set in reversed(self.stack[:]):
            last_node: TabContainer = tab_set[-1]
            logger.info(f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) last_node={last_node.tab_identifier()}")

            # Is this node a direct child of the last node in this tab-set?
            is_child: bool = node in last_node.children[1]
            if is_child:
                logger.info(f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) node is a child of last_node; close_till=tab_set, append=False")
                close_till = tab_set
                append = False
                break

            # Is this node a sibling of the last node in this tab-set?
            is_sibling: bool = (
                node.parent == last_node.parent  # same parent
                # immediately after the previous node
                and node.parent.index(last_node) + 1 == node.parent.index(node)
            )
            if is_sibling:
                logger.info(f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) node is a sibling of last_node; close_till=tab_set, append=True")
                close_till = tab_set
                append = True
                break

        # Close all tab sets as required.
        if close_till is not None:
            logger.info(f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) close tab sets in reverse until we come to close_till")
            while self.stack[-1] != close_till:
                TabHtmlTransform.finalize_set(self.stack.pop(), next(self.counter))
        else:
            logger.info(f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) close all tab sets in reverse")
            while self.stack:
                TabHtmlTransform.finalize_set(self.stack.pop(), next(self.counter))

        # Start a new tab set, as required or if requested.
        if append and not node["new_set"]:
            logger.info(f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) append node to last tab_set in the stack")
            assert self.stack
            self.stack[-1].append(node)
        else:
            logger.info(f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) start a new tab_set")
            self.stack.append([node])

    @classmethod
    def element_id(cls, el: nodes.Element) -> str:
        if "ids" in el.attributes and el.attributes["ids"]:
            return el.attributes["ids"][0]
        return f"Element-{el.__hash__()}"

    @classmethod
    def finalize_set(cls, tab_set: List[TabContainer], set_counter: int):
        """Add these TabContainers as a single-set-of-tabs."""
        assert tab_set

        parent: nodes.Element = tab_set[0].parent
        logger.info(f"{LOG_PREFIX} finalize_set; tab_set node count={len(tab_set)}, parent={TabHtmlTransform.element_id(parent)}")
        container: nodes.container = nodes.container(
            "", is_div=True, classes=["tab-set"]
        )
        container.parent = parent

        tab_set_name: str = f"tab-set--{set_counter}"
        node_counter: int = 0
        for node in tab_set:
            node_counter += 1
            tab_id: str = tab_set_name + f"-input--{node_counter}"
            logger.info(f"{LOG_PREFIX} finalize_set({tab_set_name}|{node.tab_identifier()}); tab_id={tab_id}, node_counter={node_counter}")
            title, content = node.children

            # <input>, for storing state in radio boxes.
            input_node: TabInput = TabInput(
                type="radio",
                ids=[tab_id],
                name=tab_set_name,
                classes=["tab-input"],
            )

            # <label>
            label_node: TabLabel = TabLabel(
                "", **{"for": tab_id}, classes=["tab-label"]
            )

            # <span>, for storing an anchor that the table of contents links to.
            span_node: Optional[TabSpan] = None
            inline_tab_id: str = ""
            if node.attributes["ids"]:
                logger.info(f"{LOG_PREFIX} finalize_set({tab_set_name}|{node.tab_identifier()}); found inline_tab_id from node attributes: {inline_tab_id}")
                inline_tab_id = node.attributes["ids"][0]
            if inline_tab_id:
                tabid: TabId = TabId.from_str(inline_tab_id)
                if tabid is not None:
                    logger.info(f"{LOG_PREFIX} finalize_set({tab_set_name}|{node.tab_identifier()}); inline_tab_id is a valid TabId; add span to label node")
                    tabid.tab_count = node.tab_counter
                    span_node = TabSpan(str(tabid))
                    label_node += span_node

            # Add the tab title to the label
            if isinstance(title, nodes.Element):
                for title_child in title.children:
                    label_node += title_child

            # For error messages
            input_node.source = node.source
            input_node.line = node.line
            label_node.source = node.source
            label_node.line = node.line
            if span_node is not None:
                span_node.source = node.source
                span_node.line = node.line

            # Populate with the content.
            container += input_node
            container += label_node
            container += content

        container.children[0]["checked"] = True

        # Replace all nodes in tab_set, with the container.
        start_at: int = parent.index(tab_set[0])
        end_at: int = parent.index(tab_set[-1])

        logger.info(
            f"{LOG_PREFIX} finalize_set({tab_set_name}); "
            f"set parent.children to: parent.children[:{start_at}] + [container] + parent[{end_at + 1}:]"
        )

        parent.children = (
            parent.children[:start_at] + [container] + parent[end_at + 1 :]
        )
