# -*- coding: utf-8 -*-

"""
Produce a list of redirect definitions based on what configuration settings moved from
configuration-settings.rst to the various settings pages

Requires changing BASE_DIR to the root of the docs repo to scan, and OLD_FILE to the
location of the "old" configuration-settings.doctree file.

This script makes the assumption that the files in the NEW_FILES list are located in
the ``build/doctrees/configure`` subdirectory.

usage example: pipenv run python scripts/config-redirects.py
"""

import pickle
from typing import List, Dict, Tuple
from docutils import nodes
from docutils.nodes import make_id
from sphinx import addnodes


BASE_DIR = "/home/alan/src/docs-alan"
OLD_FILE = "/home/alan/src/configuration-settings.doctree"
NEW_FILES: List[str] = [
    "authentication-configuration-settings",
    "cloud-billing-account-settings",
    "compliance-configuration-settings",
    "database-configuration-settings",
    "deprecated-configuration-settings",
    "developer-mode-configuration-settings",
    "elasticsearch-configuration-settings",
    "environment-configuration-settings",
    "experimental-configuration-settings",
    "file-storage-configuration-settings",
    "high-availability-configuration-settings",
    "image-proxy-configuration-settings",
    "integrations-configuration-settings",
    "logging-configuration-settings",
    "performance-monitoring-configuration-settings",
    "plugins-configuration-settings",
    "push-notification-server-configuration-settings",
    "rate-limiting-configuration-settings",
    "reporting-configuration-settings",
    "self-hosted-account-settings",
    "session-lengths-configuration-settings",
    "site-configuration-settings",
    "smtp-configuration-settings",
    "user-management-configuration-settings",
    "web-server-configuration-settings",
]


def has_title_and_table(node: nodes.section) -> bool:
    if len(node.children) == 0:
        return False
    foundtitle = False
    foundtable = False
    for child in node.children:
        if isinstance(child, nodes.title):
            foundtitle = True
        elif isinstance(child, nodes.table):
            foo: str = child.astext()
            try:
                if foo.index("config.json"):
                    foundtable = True
            except ValueError:
                pass
    return foundtitle and foundtable


def get_title_and_table(node: nodes.section) -> Tuple[str, str]:
    if len(node.children) == 0:
        return "", ""
    section_title = ""
    section_table = ""
    for child in node.children:
        if isinstance(child, nodes.title):
            section_title = child.astext()
        elif isinstance(child, nodes.table):
            section_table = child.astext()
    return section_title, section_table


def pick_config_settings(node: nodes.Node, config_settings: Dict[str, Tuple[str, str]]):
    if isinstance(node, nodes.section):
        if has_title_and_table(node):
            sec_title, sec_table = get_title_and_table(node)
            title_frag = make_id(sec_title)
            # store title and table info in config_settings dict with fragment as key
            config_settings[title_frag] = (sec_title, sec_table)
    for child in node.children:
        pick_config_settings(child, config_settings)


def main():
    # load old file
    with open(OLD_FILE, "rb") as f:
        old_doctree: addnodes.document = pickle.load(f)
    # pick out config settings as best as possible
    config_settings: Dict[str, Tuple[str, str]] = dict()
    pick_config_settings(old_doctree, config_settings)
    redirects: Dict[str, str] = dict()
    seen_frags: Dict[str, List[str, str]] = dict()
    new_frags: Dict[str, List[str, str]] = dict()
    dupe_frags: Dict[str, List[str]] = dict()
    # for each new file:
    for new_file in NEW_FILES:
        filepath: str = "build/doctrees/configure/%s.doctree" % new_file
        # load new file
        with open(filepath, "rb") as f:
            doctree: addnodes.document = pickle.load(f)
        # pick out config settings
        doctree_config_settings: Dict[str, Tuple[str, str]] = dict()
        pick_config_settings(doctree, doctree_config_settings)
        for key in doctree_config_settings:
            if key in seen_frags:
                if key not in dupe_frags:
                    dupe_frags[key] = list()
                dupe_frags[key].append(new_file)
                seen_frags[key].append(new_file)
                continue
            else:
                seen_frags[key] = list()
                seen_frags[key].append(new_file)
            if key in config_settings:
                redirect_key = "configure/configuration-settings.html#%s" % key
                redirect_target = "https://docs.mattermost.com/configure/%s.html#%s" % (new_file, key)
                redirects[redirect_key] = redirect_target
            else:
                if key not in new_frags:
                    new_frags[key] = list()
                new_frags[key].append(new_file)
    # print redirects
    for redirect_key in redirects:
        print("\"%s\": \"%s\"," % (redirect_key, redirects[redirect_key]))
    # print dupe frags
    print("<<< Duplicate URL Fragments >>>")
    for key in dupe_frags:
        print("%s: [%s],%s" % (key, seen_frags[key][0], ",".join(dupe_frags[key])))
    # print new frags
    print("<<< New URL Fragments >>>")
    for key in new_frags:
        print("%s: %s" % (key, ",".join(new_frags[key])))


if __name__ == "__main__":
    main()
