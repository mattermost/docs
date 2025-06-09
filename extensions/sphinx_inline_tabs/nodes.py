from docutils import nodes
from sphinx.writers.html5 import HTML5Translator


class TabContainer(nodes.container):
    """
    The initial tree-node for holding tab content.
    """

    def __init__(self, rawsource="", *children, **attributes):
        super().__init__(rawsource, *children, **attributes)
        self.tagname = "div"


class _GeneralHTMLTagElement(nodes.Element, nodes.General):

    _tagname: str = ""
    _endtag: bool = False

    @staticmethod
    def visit(translator: HTML5Translator, node: "_GeneralHTMLTagElement"):
        attributes = node.attributes.copy()
        # Remove unused attributes
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
    def depart(translator, node: "_GeneralHTMLTagElement"):
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


class TabSpan(nodes.Element):
    """
    A docutils node that writes a ``<span>`` tag that includes a specific id
    """

    span_id: str

    def __init__(self, span_id: str):
        super().__init__()
        self.tagname = "span"
        self.span_id = span_id

    @classmethod
    def visit(cls, visitor: HTML5Translator, node: "TabSpan") -> None:
        """
        Write the opening HTML tag for the span node
          :param visitor: The translator that handles writing HTML bodies
          :param node: The docutils node we're visiting
          :return: None
        """
        visitor.body.append(f'<{node.tagname} id="{node.span_id}">')

    @classmethod
    def depart(cls, visitor: HTML5Translator, node: "TabSpan") -> None:
        """
        Write the closing HTML tag for the anchor node
          :param visitor: The translator that handles writing HTML bodies
          :param node: The docutils node we're departing
          :return: None
        """
        visitor.body.append(f"</{node.tagname}>")
