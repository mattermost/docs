# -*- coding: utf-8 -*-

"""
Validate all URL references which point to other documents in the site.

The links of each doctree file in the ``build/doctrees`` directory will be checked to see if a
doctree file with the same name exists. If a doctree file does not exist, the source doctree file
and the affected link will be output.

usage example: pipenv run python scripts/validate-refuris.py
"""

import pickle
from glob import iglob
from typing import List, cast
from docutils import nodes
from sphinx import addnodes
from os import path


BASE_DIR = "build/doctrees"


def validate_refuri(node: nodes.reference, invalid_refs: List[str]):
    if "refuri" in node.attributes:
        refuri: str = node["refuri"]
        # remove docs.mattermost.com prefix since that's the base URL
        if refuri.startswith("https://docs.mattermost.com"):
            refuri = refuri.removeprefix("https://docs.mattermost.com")
        # if the reference is to the root of the site, it's considered valid
        if refuri == "/":
            return
        # if this reference is an absolute reference to a page
        if refuri.startswith("/"):
            # remove the URI fragment if there is one
            toks = refuri.split("#", 1)
            uri_path = toks[0].removesuffix(".html")
            # remove the URI query if there is one
            toks = uri_path.split("?", 1)
            uri_path = toks[0]
            # construct the target doctree path and filename
            target_doctree = "%s%s.doctree" % (BASE_DIR, uri_path)
            if not path.exists(target_doctree):
                # the target doctree file does not exist
                invalid_refs.append(node["refuri"])


def walk_node(node: nodes.Node, invalid_refs: List[str]):
    # If this is a reference node, it will have a ``refuri`` that we want to validate
    if isinstance(node, nodes.reference):
        validate_refuri(cast(nodes.reference, node), invalid_refs)
    # Walk the node's children
    for child in node.children:
        walk_node(child, invalid_refs)


def main():
    for doctree_file in iglob("**/*.doctree", root_dir=BASE_DIR):
        invalid_refs: List[str] = list()
        doctree_file_path = "%s/%s" % (BASE_DIR, doctree_file)
        with open(doctree_file_path, "rb") as fin:
            doctree: addnodes.document = pickle.load(fin)
        walk_node(doctree, invalid_refs)
        if len(invalid_refs) > 0:
            print("%s:" % doctree_file)
            for invalid_ref in set(invalid_refs):
                print("  - %s" % invalid_ref)


if __name__ == "__main__":
    main()
