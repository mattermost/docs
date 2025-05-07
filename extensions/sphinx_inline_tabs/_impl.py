"""The actual implementation."""

import itertools
from dataclasses import dataclass
from typing import List

from docutils import nodes
from docutils.nodes import NodeVisitor
from docutils.parsers.rst import directives
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import NodeMatcher


def env_purge_doc(_: Sphinx, env: BuildEnvironment, docname: str) -> None:
    if hasattr(env, "sphinx_tabs"):
        if docname in env.sphinx_tabs:
            env.sphinx_tabs.pop(docname)


def env_merge_info(
        _: Sphinx, env: BuildEnvironment, docnames: List[str], other: BuildEnvironment
) -> None:
    if not hasattr(env, "sphinx_tabs"):
        env.sphinx_tabs = {}
    if hasattr(other, "sphinx_tabs"):
        for docname in docnames:
            if docname in other.sphinx_tabs:
                if len(other.sphinx_tabs[docname]) > 0:
                    env.sphinx_tabs[docname] = other.sphinx_tabs[docname]


@dataclass(repr=True)
class SectionData:
    name: str
    level: int
    is_doc_root: bool
    is_section_root: bool
    is_tab: bool
    children: list["SectionData"]


def collect_sections(docname: str, node: nodes.Element, level = 0) -> SectionData:
    #print(f">>> ({docname}) [{level}] node={type(node)}")
    localsecdata = SectionData(
        name=docname if level == 0 else "",
        level=level,
        is_doc_root=True if level == 0 else False,
        is_section_root=True if level == 1 else False,
        is_tab=True if isinstance(node, TabContainer) else False,
        children=[],
    )
    if isinstance(node, nodes.section):
        localsecdata.name = node.next_node(nodes.title).astext()
        #print(f">>> ({docname}) [{level}] Section: {localsecdata.name}")
    elif isinstance(node, TabContainer):
        localsecdata.name = node.next_node(nodes.label).astext()
        #print(f">>> ({docname}) [{level}] Tab: {localsecdata.name}")

    parent_node = node.next_node(nodes.container) if isinstance(node, TabContainer) else node

    for child in parent_node.children:
        #print(f"   >>> ({docname}) [{level}] child={type(child)}")
        if isinstance(child, nodes.section) or isinstance(child, TabContainer):
            localsecdata.children.append(collect_sections(docname, child, level + 1))

    return localsecdata


def dump_sections(docname: str, secdata: SectionData):
    section_type: str = "section"
    if secdata.is_doc_root:
        section_type = "doc root"
    elif secdata.is_section_root:
        section_type = "section root"
    elif secdata.is_tab:
        section_type = "tab"
    print(f"!!! ({docname}) [{secdata.level}] {secdata.name}: {section_type}, {len(secdata.children)} children")
    for child in secdata.children:
        dump_sections(docname, child)


def walk_sections(docname: str, node: nodes.Element, level = 0):
    #print(f">>> ({docname}) [{level}] node={type(node)}")
    if isinstance(node, nodes.section):
        section_title = node.next_node(nodes.title).astext()
        print(f">>> ({docname}) [{level}] Section: {section_title}")
    elif isinstance(node, TabContainer):
        node_label = node.next_node(nodes.label).astext()
        print(f">>> ({docname}) [{level}] Tab: {node_label}")
    for node_child in node.children:
        #print(f"   >>> ({docname}) [{level}] node_child={type(node_child)}")
        if (
            isinstance(node_child, nodes.section)
            or isinstance(node_child, TabContainer)
        ):
            walk_sections(docname, node_child, level + 1)
        elif (
            isinstance(node_child, nodes.container)
        ):
            walk_sections(docname, node_child, level)


def doctree_read(app: Sphinx, doctree: nodes.document):
    if not hasattr(app.env, "sphinx_tabs"):
        app.env.sphinx_tabs = {}
    if app.env.docname in app.env.sphinx_tabs:
        if app.env.docname == "deploy/server/deploy-kubernetes":
            print(f"+++ doctree_read({app.env.docname}): walk sections")
            sd: SectionData = collect_sections(app.env.docname, doctree)
            dump_sections(app.env.docname, sd)
        for tab_name in app.env.sphinx_tabs[app.env.docname]:
            anchor_name = tab_name.replace(" ", "_").replace("/", "_").replace(",", "_").lower()
            reference = nodes.reference(
                '',
                tab_name,
                anchorname=f"#{anchor_name}",
                internal=True,
                refuri=app.env.docname,
            )
            cpara = addnodes.compact_paragraph()
            cpara.append(reference)
            listitem = nodes.list_item()
            listitem.append(cpara)
            #print(f"+++ doctree_read({app.env.docname}): listitem={listitem}")
            if len(app.env.tocs[app.env.docname][0]) == 1:
                app.env.tocs[app.env.docname][0].append(nodes.bullet_list())
            app.env.tocs[app.env.docname][0][1] += listitem
        app.env.sphinx_tabs.pop(app.env.docname)


class TabContainer(nodes.Element):
    """The initial tree-node for holding tab content."""

    def __init__(self, rawsource='', *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self.tagname = "div"


class _GeneralHTMLTagElement(nodes.Element, nodes.General):
    @staticmethod
    def visit(translator, node):
        attributes = node.attributes.copy()
        # Nobody needs this crap.
        attributes.pop("ids")
        attributes.pop("classes")
        attributes.pop("names")
        attributes.pop("dupnames")
        attributes.pop("backrefs")

        if node._endtag:
            text = translator.starttag(node, node._tagname, **attributes)
        else:
            text = translator.emptytag(node, node._tagname, **attributes)

        translator.body.append(text.strip())

    @staticmethod
    def depart(translator, node):
        if node._endtag:
            translator.body.append(f"</{node._tagname}>")


class TabInput(_GeneralHTMLTagElement):
    """Represents a radio button for a tab."""

    _tagname = "input"
    _endtag = False


class TabLabel(_GeneralHTMLTagElement):
    """Represents a label that holds the title for a tab."""

    _tagname = "label"
    _endtag = True


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

        container = TabContainer("", type="tab", new_set="new-set" in self.options)
        self.set_source_info(container)

        # Handle the label (non-plain-text variants allowed)
        textnodes, messages = self.parse_inline(self.arguments[0], lineno=self.lineno)
        # The signature of this object is:
        #     __init__(self, rawsource='', text='', *children, **attributes)
        #
        # We want to directly populate the children here.
        label = nodes.label("", "", *textnodes)

        # Handle the content
        content = nodes.container("", is_div=True, classes=["tab-content"])

        parse_titles = ("parse-titles" in self.options)
        for parsed_node in self.parse_content_to_nodes(allow_section_headings=parse_titles):
            content += parsed_node
        # Sphinx 7.3 and earlier nested_parse_with_titles
        # nested_parse_with_titles(self.state, self.content, content, self.content_offset)
        # Previous parse without titles
        # self.state.nested_parse(self.content, self.content_offset, content)

        # sections_dict: dict[str, list[str]] = self.dump_sections(content)

        container += label
        container += content

        if hasattr(self.env, "sphinx_tabs"):
            if self.env.docname not in self.env.sphinx_tabs:
                self.env.sphinx_tabs[self.env.docname] = []
            self.env.sphinx_tabs[self.env.docname].append(self.arguments[0])

        return [container]

    def dump_sections(self, content: nodes.Node) -> dict[str, list[str]]:
        visited = {}
        for section in content.findall(nodes.section, siblings=False):
            section_title = section.next_node(nodes.title).astext()
            if section_title in visited:
                continue
            print(f"+++ TabDirective({self.env.docname}): section {section_title}")
            visited[section_title] = []
            for sub_section in section.findall(nodes.section, siblings=False):
                sub_section_title = sub_section.next_node(nodes.title).astext()
                if sub_section_title in visited[section_title]:
                    continue
                print(f"+++ TabDirective({self.env.docname}): section {section_title}, sub-section {sub_section_title}")
                visited[section_title].append(sub_section_title)
        return visited

class TabHtmlTransform(SphinxPostTransform):
    """Transform output of TabDirective into usable chunks."""

    default_priority = 200
    formats = ["html"]

    def run(self):
        """Locate and replace `TabContainer`s."""
        self.stack = []  # type: List[List[TabContainer]]
        self.counter = itertools.count(start=0, step=1)

        matcher = NodeMatcher(TabContainer)

        for node in self.document.findall(matcher):  # type: TabContainer
            self._process_one_node(node)

        while self.stack:
            tab_set = self.stack.pop()
            self.finalize_set(tab_set, next(self.counter))

    def _process_one_node(self, node: TabContainer):
        # There is no existing tab set. Let's start a new one.
        if not self.stack:
            self.stack.append([node])
            return

        # There should never be an empty "current" tab set.
        assert self.stack[-1]

        close_till = None
        append = False
        for tab_set in reversed(self.stack[:]):
            last_node = tab_set[-1]

            # Is this node a direct child of the last node in this tab-set?
            is_child = node in last_node.children[1]
            if is_child:
                close_till = tab_set
                append = False
                break

            # Is this node a sibling of the last node in this tab-set?
            is_sibling = (
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

        parent = tab_set[0].parent

        container = nodes.container("", is_div=True, classes=["tab-set"])
        container.parent = parent

        tab_set_name = f"tab-set--{set_counter}"
        node_counter = 0
        for node in tab_set:
            node_counter += 1
            tab_id = tab_set_name + f"-input--{node_counter}"
            title, content = node.children

            # <input>, for storing state in radio boxes.
            input_node = TabInput(
                type="radio", ids=[tab_id], name=tab_set_name, classes=["tab-input"]
            )

            # <label>
            label_node = TabLabel(
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
        start_at = parent.index(tab_set[0])
        end_at = parent.index(tab_set[-1])

        parent.children = (
            parent.children[:start_at] + [container] + parent[end_at + 1 :]
        )
