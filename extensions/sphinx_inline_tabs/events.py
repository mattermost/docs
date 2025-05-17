import re
from dataclasses import dataclass
from typing import Any, Optional

from docutils import nodes
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.builders.html._assets import _JavaScript
from sphinx.util.nodes import _make_id

from .nodes import TabContainer


def env_purge_doc(app: Sphinx, _: BuildEnvironment, docname: str) -> None:
    if hasattr(app.env, "sphinx_tabs"):
        if docname in app.env.sphinx_tabs:
            app.env.sphinx_tabs.pop(docname)


def env_merge_info(
    app: Sphinx, _: BuildEnvironment, docnames: list[str], other: BuildEnvironment
) -> None:
    if not hasattr(app.env, "sphinx_tabs"):
        app.env.sphinx_tabs = {}
    if hasattr(other, "sphinx_tabs"):
        for docname in docnames:
            if docname in other.sphinx_tabs:
                if docname not in app.env.sphinx_tabs:
                    app.env.sphinx_tabs[docname] = []
                if len(app.env.sphinx_tabs[docname]) > 0 and len(other.sphinx_tabs[docname]) == 0:
                    print(f"+++ env_merge_info: {docname}; not overwriting app.env with empty list from other")
                    continue
                app.env.sphinx_tabs[docname] = other.sphinx_tabs[docname].copy()


def doctree_read(app: Sphinx, doctree: nodes.document):
    if not hasattr(app.env, "sphinx_tabs"):
        #print('+++ doctree_read: create app.env.sphinx_tabs')
        app.env.sphinx_tabs = {}
    if app.env.docname in app.env.sphinx_tabs and len(app.env.sphinx_tabs[app.env.docname]) > 0:
        #print(f"+++ doctree_read: {app.env.docname} has tabs")
        sd: SectionData = collect_sections(
            app.env, doctree, app.env.docname, doctree
        )
        #dump_sections(app.env.docname, sd)
        updated_tocs: nodes.bullet_list = sectiondata_to_toc(app.env.docname, sd)
        #print(f"+++ doctree_read({app.env.docname}): updated_tocs[0][1]={updated_tocs.children[0]}")
        if len(app.env.tocs[app.env.docname][0]) == 1:
            app.env.tocs[app.env.docname][0].append(updated_tocs.children[0])
        else:
            app.env.tocs[app.env.docname][0][1] = updated_tocs.children[0]
        app.env.sphinx_tabs[app.env.docname] = []


def html_page_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Optional[nodes.document],
) -> Optional[str]:
    if hasattr(app.env, "sphinx_tabs"):
        if pagename in app.env.sphinx_tabs:
            #print(f"+++ html_page_context: {pagename}; context.keys()={context.keys()}")
            if "script_files" in context:
                furo_js_asset: Optional[_JavaScript] = None
                for script_asset in context["script_files"]:
                    if script_asset.filename == "_static/scripts/furo.js":
                        furo_js_asset = script_asset
                        #print(f"+++ html_page_context: {pagename}; furo_js_asset={str(furo_js_asset)}")
                        break
                if furo_js_asset is not None:
                    #print(f"+++ html_page_context: {pagename}; remove furo JS asset")
                    context["script_files"].remove(furo_js_asset)

    return None


@dataclass(repr=True)
class SectionData:
    name: str
    level: int
    is_doc_root: bool
    is_section_root: bool
    is_tab: bool
    id: str
    children: list["SectionData"]


def collect_sections(
    env: BuildEnvironment,
    document: nodes.document,
    docname: str,
    node: nodes.Element,
    level=0,
) -> SectionData:
    # print(f">>> ({docname}) [{level}] node={type(node)}")
    secdata = SectionData(
        name=docname if level == 0 else "",
        level=level,
        is_doc_root=True if level == 0 else False,
        is_section_root=True if level == 1 else False,
        is_tab=True if isinstance(node, TabContainer) else False,
        id="",
        children=[],
    )

    if isinstance(node, nodes.section):
        secdata.name = node.next_node(nodes.title).astext()
        # print(f">>> ({docname}) [{level}] Section: {localsecdata.name}")
    elif isinstance(node, TabContainer):
        secdata.name = node.next_node(nodes.label).astext()
        # print(f">>> ({docname}) [{level}] Tab: {localsecdata.name}")

    section_id: str = ""
    if isinstance(node, TabContainer) and "inline_tab_id" in node.attributes:
       section_id = node.attributes["inline_tab_id"]
    else:
        if "ids" in node.attributes:
            if len(node.attributes["ids"]) == 1 and node.attributes["ids"][0] != "":
                section_id = node.attributes["ids"][0]
            elif len(node.attributes["ids"]) > 1:
                for id in node.attributes["ids"]:
                    if re.match('inlinetab--([a-zA-Z0-9-]+)--([0-9]+)-(.*)', id):
                        section_id = id
                        break
    if section_id == "":
        section_id = _make_id(secdata.name)
    secdata.id = section_id

    parent_node = (
        node.next_node(nodes.container) if isinstance(node, TabContainer) else node
    )

    for child in parent_node.children:
        # print(f"   >>> ({docname}) [{level}] child={type(child)}")
        if isinstance(child, nodes.section) or isinstance(child, TabContainer):
            secdata.children.append(
                collect_sections(env, document, docname, child, level + 1)
            )

    return secdata


def dump_sections(docname: str, secdata: SectionData):
    section_type: str = "section"
    if secdata.is_doc_root:
        section_type = "doc root"
    elif secdata.is_section_root:
        section_type = "section root"
    elif secdata.is_tab:
        section_type = "tab"
    print(
        f"!!! ({docname}) [{secdata.level}] {secdata.name}/{secdata.id}: {section_type}, {len(secdata.children)} children"
    )
    for child in secdata.children:
        dump_sections(docname, child)


# def dump_sections_v1(self, content: nodes.Node) -> dict[str, list[str]]:
#     visited = {}
#     for section in content.findall(nodes.section, siblings=False):
#         section_title = section.next_node(nodes.title).astext()
#         if section_title in visited:
#             continue
#         print(f"+++ TabDirective({self.env.docname}): section {section_title}")
#         visited[section_title] = []
#         for sub_section in section.findall(nodes.section, siblings=False):
#             sub_section_title = sub_section.next_node(nodes.title).astext()
#             if sub_section_title in visited[section_title]:
#                 continue
#             print(
#                 f"+++ TabDirective({self.env.docname}): section {section_title}, sub-section {sub_section_title}"
#             )
#             visited[section_title].append(sub_section_title)
#     return visited


def sectiondata_to_toc(docname: str, secdata: SectionData) -> nodes.bullet_list:
    # print(
    #     f"### ({docname}): [{secdata.level}] {secdata.name}<{secdata.id}>, {len(secdata.children)} children"
    # )

    if secdata.is_doc_root:
        # print(
        #     f"### ({docname}): [{secdata.level}] return sectiondata_to_toc(..., secdata.children[0])"
        # )
        return sectiondata_to_toc(docname, secdata.children[0])
    elif secdata.is_section_root:
        list_item: nodes.list_item = nodes.list_item()
        for idx, child in enumerate(secdata.children):
            # print(
            #     f"### ({docname}): [{secdata.level}] top section {idx+1}/{len(secdata.children)}"
            # )
            list_item.append(sectiondata_to_toc(docname, child))
        bullet_list: nodes.bullet_list = nodes.bullet_list()
        bullet_list.append(list_item)
        return bullet_list

    # print(
    #     f"### ({docname}): [{secdata.level}] add reference for {secdata.name}<{secdata.id}>"
    # )
    bullet_list: nodes.bullet_list = nodes.bullet_list()
    list_item: nodes.list_item = nodes.list_item()
    anchor_name: str = f"#{secdata.id}"
    reference = nodes.reference(
        "",
        secdata.name,
        refuri=docname,
        anchorname=anchor_name,
        internal=True,
    )
    cpara: addnodes.compact_paragraph = addnodes.compact_paragraph()
    cpara.append(reference)
    list_item.append(cpara)
    bullet_list.append(list_item)

    if len(secdata.children) > 0:
        # child_names = [sd.name for sd in secdata.children]
        # print(f"### ({docname}): [{secdata.level}] children: {','.join(child_names)}")
        for idx, child in enumerate(secdata.children):
            # print(
            #     f"### ({docname}): [{secdata.level}] child {idx+1}/{len(secdata.children)}"
            # )
            child_toc = sectiondata_to_toc(docname, child)
            child_list_item = nodes.list_item()
            child_list_item.append(child_toc)
            bullet_list.append(child_list_item)

    return bullet_list
