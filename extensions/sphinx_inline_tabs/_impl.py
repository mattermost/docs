"""The actual implementation."""

import itertools
import re
from typing import List, Optional

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import NodeMatcher, _make_id

from .nodes import TabContainer, TabInput, TabLabel


class TabDirective(SphinxDirective):
    """Tabbed content in Sphinx documentation."""

    required_arguments = 1  # directive takes a single argument.
    final_argument_whitespace = True  # this allows that argument to contain spaces.
    has_content = True
    option_spec = {
        "new-set": directives.flag,
        "parse-titles": directives.flag,
    }

    def run(self):
        """Parse a tabs directive."""
        self.assert_has_content()

        container = TabContainer(
            "",
            type="tab",
            new_set="new-set" in self.options,
        )
        self.set_source_info(container)

        # Handle the label (non-plain-text variants allowed)
        textnodes, messages = self.parse_inline(self.arguments[0], lineno=self.lineno)
        # The signature of this object is:
        #     __init__(self, rawsource='', text='', *children, **attributes)
        #
        # We want to directly populate the children here.
        label = nodes.label("", "", *textnodes, id=self.arguments[0])

        # Handle the content
        content = nodes.container("", is_div=True, classes=["tab-content"])

        parse_titles = "parse-titles" in self.options
        parsed_nodes = self.parse_content_to_nodes(allow_section_headings=parse_titles)
        if self.env.docname == "deploy/server/deploy-kubernetes":
            self.walk_parsed_nodes(parsed_nodes, tab_name=_make_id(self.arguments[0]))
        for parsed_node in parsed_nodes:
            content += parsed_node

        container += label
        container += content

        if hasattr(self.env, "sphinx_tabs"):
            if self.env.docname not in self.env.sphinx_tabs:
                self.env.sphinx_tabs[self.env.docname] = []
            self.env.sphinx_tabs[self.env.docname].append(self.arguments[0])

        return [container]

    def walk_parsed_nodes(self, parsed_nodes: list[nodes.Node], level: int = 0, tab_name: str = ""):
        for parsed_node in parsed_nodes:
            #print(f"+++ parsed_node: {parsed_node.astext()}")
            if isinstance(parsed_node, nodes.section):
                node_id: str = parsed_node.attributes["ids"][0]
                print(f"+++ [{level}] section: {node_id}")
                prefixed_id: str = f"inlinetab--{tab_name}--{level}-{node_id}"
                if re.match('id[0-9]+', node_id):
                    print(f"+++ [{level}] replace id with '{prefixed_id}'")
                    parsed_node.attributes["ids"] = [prefixed_id]
                else:
                    print(f"+++ [{level}] add id '{prefixed_id}'")
                    parsed_node.append_attr_list("ids", [prefixed_id])
            if len(parsed_node.children) > 0:
                #print(f"+++ [{level}] parse {len(parsed_node.children)} children")
                self.walk_parsed_nodes(parsed_node.children, level + 1, tab_name)


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

        matcher: NodeMatcher = NodeMatcher(TabContainer)

        for node in self.document.findall(matcher):  # type: TabContainer
            self._process_one_node(node)

        while self.stack:
            tab_set: list[TabContainer] = self.stack.pop()
            self.finalize_set(tab_set, next(self.counter))

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
            last_node = tab_set[-1]

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

        container: nodes.container = nodes.container("", is_div=True, classes=["tab-set"])
        container.parent = parent

        tab_set_name: str = f"tab-set--{set_counter}"
        node_counter: int = 0
        for node in tab_set:
            node_counter += 1
            tab_id: str = tab_set_name + f"-input--{node_counter}"
            title, content = node.children

            # <input>, for storing state in radio boxes.
            input_node: TabInput = TabInput(
                type="radio", ids=[tab_id], name=tab_set_name, classes=["tab-input"]
            )

            # <label>
            label_node: TabLabel = TabLabel(
                "", *title.children, **{"for": tab_id}, classes=["tab-label"]
            )

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
