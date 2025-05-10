from docutils import nodes
from sphinx.util.docutils import SphinxTranslator


class TabContainer(nodes.Element):
    """The initial tree-node for holding tab content."""

    def __init__(self, rawsource="", *children, **attributes):
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


class TabAnchor(nodes.Element):
    """
    A docutils node that writes an ``<a>`` tag that includes a specific id
    """

    anchor: str

    def __init__(self, href: str):
        super().__init__()
        self.tagname = "a"
        self.anchor = href


def visit_anchor_node(visitor: SphinxTranslator, node: TabAnchor) -> None:
    """
    Write the opening HTML tag for the anchor node
      :param visitor: The translator that handles writing HTML bodies
      :param node: The docutils node we're visiting
      :return: None
    """
    visitor.body.append('<%s id="%s">' % (node.tagname, node.anchor))


def depart_anchor_node(visitor: SphinxTranslator, node: TabAnchor) -> None:
    """
    Write the closing HTML tag for the anchor node
      :param visitor: The translator that handles writing HTML bodies
      :param node: The docutils node we're departing
      :return: None
    """
    visitor.body.append(f"</{node.tagname}>")
