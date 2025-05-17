"""The actual implementation."""

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import _make_id

from .nodes import TabContainer


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

        # re.match('inlinetab--([a-zA-Z0-9-]+)--([0-9]+)-(.*)', id)
        tab_id: str = _make_id(self.arguments[0])
        container.attributes["tab_name"] = self.arguments[0]
        container.attributes["inline_tab_id"] = f"inlinetab--{tab_id}--0-{self.arguments[0]}"

        # Handle the label (non-plain-text variants allowed)
        textnodes, messages = self.parse_inline(self.arguments[0], lineno=self.lineno)
        # The signature of this object is:
        #     __init__(self, rawsource='', text='', *children, **attributes)
        #
        # We want to directly populate the children here.
        label = nodes.label("", "", *textnodes)

        # Handle the content
        content = nodes.container("", is_div=True, classes=["tab-content"])

        parse_titles = "parse-titles" in self.options
        parsed_nodes = self.parse_content_to_nodes(allow_section_headings=parse_titles)
        #if self.env.docname == "deploy/server/deploy-kubernetes":
        self.walk_parsed_nodes(parsed_nodes, tab_name=_make_id(self.arguments[0]))
        for parsed_node in parsed_nodes:
            content += parsed_node

        container += label
        container += content

        if not hasattr(self.env, "sphinx_tabs"):
            self.env.sphinx_tabs = {}
        if self.env.docname not in self.env.sphinx_tabs:
            self.env.sphinx_tabs[self.env.docname] = []
        self.env.sphinx_tabs[self.env.docname].append(self.arguments[0])

        return [container]

    def walk_parsed_nodes(self, parsed_nodes: list[nodes.Node], level: int = 0, tab_name: str = ""):
        for parsed_node in parsed_nodes:
            #print(f"+++ parsed_node: {parsed_node.astext()}")
            if isinstance(parsed_node, nodes.section):
                node_id: str = parsed_node.attributes["ids"][0]
                #print(f"+++ [{level}] section: {node_id}")
                prefixed_id: str = f"inlinetab--{tab_name}--{level}-{node_id}"
                #if re.match('id[0-9]+', node_id):
                #    print(f"+++ [{level}] replace id with '{prefixed_id}'")
                #    parsed_node.attributes["ids"] = [prefixed_id]
                #else:
                #print(f"+++ [{level}] add id '{prefixed_id}' as first id")
                #parsed_node.append_attr_list("ids", [prefixed_id])
                existing_ids: list[str] = parsed_node.attributes["ids"]
                if existing_ids:
                    new_ids: list[str] = [prefixed_id]
                    for existing_id in existing_ids:
                        new_ids.append(existing_id)
                    parsed_node.attributes["ids"] = new_ids
            if parsed_node.children is not None:
                #print(f"+++ [{level}] parse {len(parsed_node.children)} children")
                self.walk_parsed_nodes(parsed_node.children, level + 1, tab_name)
