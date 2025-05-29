import itertools
from typing import Optional, List

from docutils import nodes
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util.nodes import NodeMatcher

from .nodes import TabContainer, TabInput, TabLabel, TabSpan


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

        for node in self.document.findall(
            NodeMatcher(TabContainer)
        ):  # type: TabContainer
            self._process_one_node(node)

        while self.stack:
            self.finalize_set(
                self.stack.pop(),
                next(self.counter),
            )

    def _process_one_node(self, node: TabContainer):
        # There is no existing tab set. Let's start a new one.
        if not self.stack:
            self.stack.append([node])
            return

        # There should never be an empty "current" tab set.
        assert self.stack[-1]

        close_till: Optional[list[TabContainer]] = None
        append: bool = False
        for tab_set in reversed(self.stack[:]):
            last_node: TabContainer = tab_set[-1]

            # Is this node a direct child of the last node in this tab-set?
            is_child: bool = node in last_node.children[1]
            if is_child:
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
                close_till = tab_set
                append = True
                break

        # Close all tab sets as required.
        if close_till is not None:
            while self.stack[-1] != close_till:
                self.finalize_set(self.stack.pop(), next(self.counter))
        else:
            while self.stack:
                self.finalize_set(self.stack.pop(), next(self.counter))

        # Start a new tab set, as required or if requested.
        if append and not node["new_set"]:
            assert self.stack
            self.stack[-1].append(node)
        else:
            self.stack.append([node])

    def finalize_set(self, tab_set: List[TabContainer], set_counter: int):
        """Add these TabContainers as a single-set-of-tabs."""
        assert tab_set

        parent: nodes.Element = tab_set[0].parent

        container: nodes.container = nodes.container(
            "", is_div=True, classes=["tab-set"]
        )
        container.parent = parent

        tab_set_name: str = f"tab-set--{set_counter}"
        node_counter: int = 0
        for node in tab_set:
            node_counter += 1
            tab_id: str = tab_set_name + f"-input--{node_counter}"
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
            inline_tab_id: str = (
                node.attributes["inline_tab_id"]
                if "inline_tab_id" in node.attributes
                else ""
            )
            if inline_tab_id:
                label_node += TabSpan(inline_tab_id)

            # Add the tab title to the label
            for title_child in title.children:
                label_node += title_child

            # For error messages
            input_node.source = node.source
            input_node.line = node.line
            label_node.source = node.source
            label_node.line = node.line

            # Populate with the content.
            container += input_node
            container += label_node
            container += content

        container.children[0]["checked"] = True

        # Replace all nodes in tab_set, with the container.
        start_at: int = parent.index(tab_set[0])
        end_at: int = parent.index(tab_set[-1])

        parent.children = (
            parent.children[:start_at] + [container] + parent[end_at + 1 :]
        )
