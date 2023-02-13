# -*- coding: utf-8 -*-

"""
Dump one or more doctrees to the screen in pseudo-XML format

usage example: pipenv run python scripts/dump-doctree.py xxxx.doctree [yyyy.doctree] ...
"""

from docutils import nodes
from sphinx import addnodes

IGNORE_NODES = (
    # comment
    nodes.comment,
    # substitution definition (|..|)
    nodes.substitution_definition,
    # object description directives (like `py:function`)
    addnodes.desc_signature,
    # `productionlist` directive
    addnodes.productionlist,
    # literal block
    nodes.literal_block,
    nodes.doctest_block,
    nodes.raw,
)

PENDING_NODES = (
    # docutils
    nodes.term,
    nodes.field_name,
    nodes.field_body,
    nodes.reference,
    nodes.line_block,
    nodes.compound,  # impl-detail
    # Sphinx
    addnodes.centered,
    addnodes.versionmodified,
)


def has_rawsource(node: nodes.Element) -> bool:
    msg = node.rawsource.replace("\n", " ").strip()
    return bool(msg)


def translatable(node: nodes.Element) -> bool:
    from sphinx.util.nodes import IGNORED_NODES

    if not isinstance(node, nodes.TextElement):
        return False
    if not node.source:
        return False
    if isinstance(node, IGNORED_NODES):
        return False
    if isinstance(node, nodes.field_name) and node.children[0] == "orphan":
        return False
    return True


def is_leaf_node(node: nodes.Element) -> bool:
    if translatable(node) and has_rawsource(node):
        return True
    if isinstance(node, IGNORE_NODES + PENDING_NODES):
        return True
    if isinstance(node, nodes.label) and isinstance(node.parent, nodes.footnote):
        # footnote > label
        return True
    if isinstance(node, nodes.label) and isinstance(node.parent, nodes.citation):
        # citation > label
        return True
    if isinstance(node, nodes.title) and isinstance(node.parent, nodes.sidebar):
        # sidebar > title
        return True
    if isinstance(node, nodes.title) and isinstance(node.parent, nodes.topic):
        # topic > title
        return True
    if isinstance(node, nodes.title) and isinstance(node.parent, addnodes.seealso):
        # seealso > title
        return True
    if isinstance(node, nodes.paragraph) and isinstance(node.parent, addnodes.seealso):
        # seealso > paragraph
        return True

    return False


def quote(text: str) -> str:
    # Use single quotes instead of double-quotes to avoid issues with partial HTML tags
    return "'%s'" % text.replace('"', r"\"")


def truncate(text: str, size=20, ellipse="...", inline=True, strip=True):
    if inline:
        text = text.replace("\n", " ")
    if strip:
        text = text.strip()
    if len(text) < size:
        return text
    else:
        return text[:size] + ellipse


def truncate_path(text: str, level=2, ellipse=".../"):
    import os

    head, tail = text, ""
    components = []
    for i in range(level):
        head, tail = os.path.split(head)
        components.append(tail)
    return ellipse + os.path.join(*reversed(components))


def starttag(node: nodes.Element):
    parts = ["%s.%s" % (node.__class__.__module__, node.__class__.__name__)]
    for attr, truncate_func in [
        ("source", truncate_path),
        ("line", str),
        ("rawsource", truncate),
    ]:
        value = getattr(node, attr, None)
        if value is not None:
            parts.append("%s=%s" % (attr, quote(truncate_func(value))))
    if translatable(node):
        parts.append('translatable="yes"')
    return "<%s>" % " ".join(parts)


def pformat(node: nodes.Node, indent="  ", level=0):
    if isinstance(node, nodes.Text):
        return "%s[#Text] %s\n" % (indent * level, quote(truncate(node.astext())))
    elif isinstance(node, nodes.raw):
        # Comment-out raw nodes so partial HTML tags don't mess up the output
        return "<!-- %s[#raw] %s -->\n" % (indent * level, quote(truncate(node.astext())))
    elif isinstance(node, nodes.Element):
        if is_leaf_node(node):
            children = []
        else:
            children = [pformat(child, indent, level + 1) for child in node.children]
        return "".join(["%s%s\n" % (indent * level, starttag(node))] + children)
    else:
        raise NotImplementedError


def show_messages(doctree: addnodes.document):
    print(pformat(doctree))


def main():
    import sys
    import pickle

    for name in sys.argv[1:]:
        with open(name, "rb") as f:
            doctree: addnodes.document = pickle.load(f)
        show_messages(doctree)


if __name__ == "__main__":
    main()
