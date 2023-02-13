"""
compass-icons - a Sphinx extension that adds the ability to display Compass Icons using a directive or a role

examples:

1. Role:

   ```rst
   :compass-icon:`icon-name,Icon Description`
   ```

2. Directive:

   ```rst
   .. compass-icon:: icon-name
     :description: Icon Description
   ```
"""
from docutils import nodes
from docutils.nodes import NodeVisitor
from docutils.parsers.rst.directives import unchanged
from docutils.parsers.rst.states import Inliner
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective
from typing import Dict, Any, List, Tuple


# The name of the directive
DIRECTIVE_NAME = "compass-icon"
# The name of the `description` directive option
OPTION_DESCRIPTION = "description"


def setup(app: Sphinx) -> Dict[str, Any]:
    """
    Sphinx extension setup function
      :param app: The Sphinx app instance
      :return: A dict of extension options to send back to Sphinx
    """
    # Register the directive and role
    app.add_directive(DIRECTIVE_NAME, CompassIconDirective)
    app.add_role(DIRECTIVE_NAME, compass_icon_role)
    # Register the docutils container node
    app.add_node(CompassIconContainer, html=(visit, depart))
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


class CompassIconContainer(nodes.Element):
    """
    A docutils Node class that is added to the document by the compass icon role or directive
    """

    # Set this container's tag to <span>
    tagname = "span"
    # Contains the name of the icon (e.g. icon-mattermost)
    icon_name: str = ""
    # Contains the optional description of the icon (e.g. Mattermost logo)
    icon_description: str = ""

    def __init__(self, name: str, description: str = ""):
        super().__init__()
        self.icon_name = name
        if description != "":
            self.icon_description = description


def visit(visitor: NodeVisitor, node: CompassIconContainer):
    """
    Docutils node visitor that renders a CompassIconContainer node into HTML. This function creates the opening
    HTML tag.
      :param visitor: The docutils NodeVisitor
      :param node: The CompassIconContainer node to visit
    """
    # Copy the existing attributes from the container node
    node_attributes = node.attributes.copy()
    # Remove the default node attributes since we don't need them
    node_attributes.pop("classes")
    node_attributes.pop("backrefs")
    node_attributes.pop("names")
    node_attributes.pop("dupnames")
    # Set the appropriate HTML tag attributes
    node_attributes["class"] = node.icon_name
    node_attributes["role"] = "image"
    node_attributes["aria-label"] = node.icon_description
    node_attributes["title"] = node.icon_description
    # Generate the starting HTML tag
    text = visitor.starttag(node, node.tagname, **node_attributes)
    # Add the tag to the rendered document
    visitor.body.append(text.strip())


def depart(visitor: NodeVisitor, node: CompassIconContainer):
    """
    Docutils node visitor that renders a CompassIconContainer node into HTML. This function creates the closing
    HTML tag.
      :param visitor: The docutils NodeVisitor
      :param node: The CompassIconContainer to depart
    """
    visitor.body.append(f"</{node.tagname}>")


def compass_icon_role(
    name: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Dict = None,
    content: List = None,
) -> Tuple[List[nodes.Node], List[nodes.system_message]]:
    """
    A docutils Role which adds a CompassIconContainer node to the document.
      :param name: (unused)
      :param rawtext: (unused)
      :param text: The text parameter of the role
      :param lineno:  (unused)
      :param inliner: (unused)
      :param options: (unused)
      :param content: (unused)
      :return: A tuple containing the list of nodes to add to the document
    """
    icon_name = ""
    icon_description = ""
    """
    Split the text parameter on a comma (,). The first token is the icon name. If there is a second token,
    then it will be used as the icon description.
    """
    tokens = text.split(",", 1)
    if len(tokens) == 2:
        icon_name = tokens[0]
        icon_description = tokens[1]
    elif len(tokens) == 1:
        icon_name = tokens[0]
    # Return a new CompassIconContainer object that includes the icon name and optional description
    return [CompassIconContainer(icon_name, icon_description)], list()


class CompassIconDirective(SphinxDirective):
    """
    A docutils directive class which adds a CompassIconContainer node to the document
    """

    # Do not allow content in the directive
    has_content = False
    # One argument must be specified (i.e. the icon name)
    required_arguments = 1
    # The one argument can contain whitespace, if needed
    final_argument_whitespace = True
    # Define the `description` directive option
    option_spec = {OPTION_DESCRIPTION: unchanged}

    def run(self) -> List[nodes.Node]:
        """
        Replace the directive with an appropriate CompassIconContainer node
          :return: A list of nodes to insert into the documednt
        """
        icon_name = self.arguments[0]
        icon_description = ""
        if OPTION_DESCRIPTION in self.options:
            icon_description = self.options[OPTION_DESCRIPTION]
        return [CompassIconContainer(icon_name, icon_description)]
