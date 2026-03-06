import itertools
from typing import Optional, List, Any

from docutils import nodes
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging

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

        # Collect all TabContainers in document order first
        all_tab_containers: list[TabContainer] = []
        self._collect_tab_containers(self.document, all_tab_containers)

        # Process TabContainers in the order they appear in the document
        for tab_container in all_tab_containers:
            logger.debug(
                f"{LOG_PREFIX} run ({self.env.docname}) processing TabContainer {tab_container.tab_identifier()}"
            )
            self._process_one_node(tab_container)

        # Finalize any remaining tab sets
        while self.stack:
            TabHtmlTransform.finalize_set(
                self.stack.pop(),
                next(self.counter),
            )

    def _collect_tab_containers(
        self, node: nodes.Node, tab_containers: List[TabContainer]
    ):
        """
        Collect all TabContainer nodes in document order.
        This ensures we process them in the correct sequence for grouping.
        """
        if isinstance(node, TabContainer):
            tab_containers.append(node)
            logger.debug(
                f"{LOG_PREFIX} _collect_tab_containers ({self.env.docname}) found TabContainer: {node.tab_identifier()}"
            )

        # Recursively search children if they exist
        if hasattr(node, "children") and node.children:
            for child in node.children:
                self._collect_tab_containers(child, tab_containers)

    def _process_one_node(self, node: TabContainer):
        """
        Processes a single node, determining how it should be categorized into the current
        tab stack, and handles cases like nested tabs, starting new tab sets, or adding
        to existing ones. This function ensures the correct hierarchical grouping of tabs
        based on their relationships, levels, and identifiers.

        :param node: The tab container node being processed.
        :type node: TabContainer
        :return: None
        """
        # There is no existing tab set. Let's start a new one.
        if not self.stack:
            logger.debug(
                f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) no existing tab set; start a new one"
            )
            self.stack.append([node])
            return

        # There should never be an empty "current" tab set.
        assert self.stack[-1]

        # Get the last tab that was processed
        last_tab_set: list[TabContainer] = self.stack[-1]
        last_tab: TabContainer = last_tab_set[-1]

        logger.debug(
            f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) comparing with last tab: {last_tab.tab_identifier()}"
        )

        # Check if this is a child of the last tab (nested tab)
        if self._is_direct_child(node, last_tab):
            logger.debug(
                f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) is child of {last_tab.tab_identifier()}; start new nested tab set"
            )
            self.stack.append([node])
            return

        # Check if this should be grouped with the current tab set
        # For top-level tabs: same parent and not marked as new-set
        if (
            node.parent == last_tab.parent
            and self._get_tab_level(node) == self._get_tab_level(last_tab)
            and not node["new_set"]
        ):
            logger.debug(
                f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) same level and parent as {last_tab.tab_identifier()}; add to current tab set"
            )
            last_tab_set.append(node)
            return

        # If we're here, this tab should start a new set
        # First, close any deeper nested tab sets but potentially keep the current level
        node_level: int = self._get_tab_level(node)
        last_level: int = self._get_tab_level(last_tab)

        if node_level < last_level:
            # This is at a higher level (less nested), close deeper sets
            logger.debug(
                f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) higher level ({node_level} vs {last_level}); close deeper sets"
            )
            while self.stack and self._get_tab_level(self.stack[-1][-1]) > node_level:
                TabHtmlTransform.finalize_set(self.stack.pop(), next(self.counter))

            # Check if we can add to the now-current tab set
            if (
                self.stack
                and node.parent == self.stack[-1][-1].parent
                and self._get_tab_level(node) == self._get_tab_level(self.stack[-1][-1])
                and not node["new_set"]
            ):
                logger.debug(
                    f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) adding to parent level tab set"
                )
                self.stack[-1].append(node)
                return

        # Start a new tab set
        logger.debug(
            f"{LOG_PREFIX} _process_one_node ({self.env.docname}|{node.tab_identifier()}) starting new tab set"
        )
        self.stack.append([node])

    def _determine_node_relationship(self, node: TabContainer) -> dict[str, Any]:
        """
        Determine the relationship of a node to existing tab sets.
        Returns a dict with 'type' and optional 'tab_set' keys.
        """
        # Check each tab set in the stack, from most recent (deepest) to oldest (shallowest)
        for idx, tab_set in enumerate(reversed(self.stack)):
            stack_index: int = (
                len(self.stack) - 1 - idx
            )  # Convert reversed index to actual stack index
            logger.debug(
                f"{LOG_PREFIX} _determine_node_relationship ({self.env.docname}|{node.tab_identifier()}) checking tab set at stack level {stack_index}"
            )

            # Check if this node is a direct child of any node in this tab set
            for tab_node in tab_set:
                if self._is_direct_child(node, tab_node):
                    logger.debug(
                        f"{LOG_PREFIX} _determine_node_relationship ({self.env.docname}|{node.tab_identifier()}) is child of {tab_node.tab_identifier()}"
                    )
                    return {"type": "child", "parent_node": tab_node}

            # For top-level tabs (level 0), check if this node should be grouped with this tab set
            node_level: int = self._get_tab_level(node)
            if node_level == 0:
                # Check if any node in this tab set is also at level 0 and has the same parent
                for tab_node in tab_set:
                    if (
                        self._get_tab_level(tab_node) == 0
                        and node.parent == tab_node.parent
                        and not node["new_set"]
                    ):
                        logger.debug(
                            f"{LOG_PREFIX} _determine_node_relationship ({self.env.docname}|{node.tab_identifier()}) is top-level sibling of {tab_node.tab_identifier()}"
                        )
                        return {
                            "type": "sibling",
                            "tab_set": tab_set,
                            "sibling_node": tab_node,
                        }

            # Check if this node is a sibling of any node in this tab set (for nested tabs)
            sibling_result: dict[str, Any] = self._check_sibling_relationship(
                node, tab_set
            )
            if sibling_result["is_sibling"]:
                logger.debug(
                    f"{LOG_PREFIX} _determine_node_relationship ({self.env.docname}|{node.tab_identifier()}) is nested sibling at level {stack_index}"
                )
                return {
                    "type": "sibling",
                    "tab_set": tab_set,
                    "sibling_node": sibling_result["sibling_node"],
                }

        # No relationship found
        logger.debug(
            f"{LOG_PREFIX} _determine_node_relationship ({self.env.docname}|{node.tab_identifier()}) no relationship found"
        )
        return {"type": "unrelated"}

    def _check_sibling_relationship(
        self, node: TabContainer, tab_set: List[TabContainer]
    ) -> dict[str, Any]:
        """
        Check if node is a sibling of any node in the tab set.
        Returns dict with 'is_sibling' and optional 'sibling_node' keys.
        """
        for tab_node in tab_set:
            if self._is_sibling_at_same_level(node, tab_node):
                logger.debug(
                    f"{LOG_PREFIX} _check_sibling_relationship ({self.env.docname}|{node.tab_identifier()}) is sibling of {tab_node.tab_identifier()}"
                )
                return {"is_sibling": True, "sibling_node": tab_node}
        return {"is_sibling": False}

    def _is_sibling_at_same_level(
        self, node: TabContainer, potential_sibling: TabContainer
    ) -> bool:
        """
        Check if node is a sibling of potential_sibling at the same hierarchical level.
        """
        # Quick check: same parent and same level
        if node.parent == potential_sibling.parent and self._get_tab_level(
            node
        ) == self._get_tab_level(potential_sibling):
            logger.debug(
                f"{LOG_PREFIX} _is_sibling_at_same_level ({self.env.docname}) {node.tab_identifier()} is sibling of {potential_sibling.tab_identifier()}"
            )
            return True

        return False

    def _get_tab_level(self, node: TabContainer) -> int:
        """
        Calculate the hierarchical level of a TabContainer by counting
        how many TabContainer ancestors it has.
        """
        level: int = 0
        current: Optional[nodes.Element] = node.parent
        while current is not None:
            if isinstance(current, TabContainer):
                level += 1
            current = getattr(current, "parent", None)
        return level

    def _is_direct_child(
        self, node: TabContainer, potential_parent: TabContainer
    ) -> bool:
        """Check if node is a direct child of potential_parent."""
        if len(potential_parent.children) < 2:
            return False

        # The content is in children[1] (children[0] is the label)
        content_container: nodes.Node = potential_parent.children[1]
        if not hasattr(content_container, "children"):
            return False

        # Check if node is directly in the content container's children
        if hasattr(content_container, "children"):
            return node in content_container.children
        return False

    def _is_sibling(self, node: TabContainer, potential_sibling: TabContainer) -> bool:
        """
        Check if node is a sibling of potential_sibling (legacy method).
        Kept for backwards compatibility but now delegates to the more flexible method.
        """
        return self._is_sibling_at_same_level(node, potential_sibling)

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
        logger.debug(
            f"{LOG_PREFIX} finalize_set; tab_set node count={len(tab_set)}, parent={TabHtmlTransform.element_id(parent)}"
        )
        container: nodes.container = nodes.container(
            "", is_div=True, classes=["tab-set"]
        )
        container.parent = parent

        tab_set_name: str = f"tab-set--{set_counter}"
        node_counter: int = 0
        for node in tab_set:
            node_counter += 1
            tab_id: str = tab_set_name + f"-input--{node_counter}"
            logger.debug(
                f"{LOG_PREFIX} finalize_set({tab_set_name}|{node.tab_identifier()}); tab_id={tab_id}, node_counter={node_counter}"
            )
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
                logger.debug(
                    f"{LOG_PREFIX} finalize_set({tab_set_name}|{node.tab_identifier()}); found inline_tab_id from node attributes: {inline_tab_id}"
                )
                inline_tab_id = node.attributes["ids"][0]
            if inline_tab_id:
                tabid: Optional[TabId] = TabId.from_str(inline_tab_id)
                if tabid is not None:
                    logger.debug(
                        f"{LOG_PREFIX} finalize_set({tab_set_name}|{node.tab_identifier()}); inline_tab_id is a valid TabId; add span to label node"
                    )
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

        # Set the first input as checked by default
        if container.children:
            first_input = container.children[0]
            if isinstance(first_input, TabInput):
                first_input.attributes["checked"] = True

        # Replace all nodes in tab_set, with the container.
        start_at: int = parent.index(tab_set[0])
        end_at: int = parent.index(tab_set[-1])

        logger.debug(
            f"{LOG_PREFIX} finalize_set({tab_set_name}); "
            f"set parent.children to: parent.children[:{start_at}] + [container] + parent[{end_at + 1}:]"
        )

        parent.children = (
            parent.children[:start_at] + [container] + parent[end_at + 1 :]
        )
