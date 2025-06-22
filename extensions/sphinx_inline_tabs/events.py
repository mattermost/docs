"""
Sphinx event handler implementation.
"""
from typing import Any, Final, Optional

from docutils import nodes
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util import logging
from sphinx.util.nodes import _make_id

from .directive import LOG_PREFIX
from .nodes import TabContainer
from .sectiondata import SectionData
from .tab_id import TabId


logger: logging.SphinxLoggerAdapter = logging.getLogger(__name__)
"""The Sphinx logger"""

FURO_SCRIPT_ASSET_FILENAME: Final[str] = "_static/scripts/furo.js"
"""The file name of the Furo theme JavaScript asset"""


def env_purge_doc(app: Sphinx, _: BuildEnvironment, docname: str) -> None:
    """
    Purge an existing document from the pickled document list.
    This function is called when the Sphinx `env-purge-doc` event is fired.

    :param app: The Sphinx instance
    :param _: The Sphinx BuildEnvironment object; unused
    :param docname: The name of the document to purge
    """
    if hasattr(app.env, "sphinx_tabs"):
        if docname in app.env.sphinx_tabs:
            app.env.sphinx_tabs.pop(docname)


def env_merge_info(
    app: Sphinx, _: BuildEnvironment, docnames: list[str], other: BuildEnvironment
) -> None:
    """
    Merge collected document names from parallel readers (workers) into the master Sphinx environment.
    This function is called when the Sphinx `env-merge-info` event is fired.

    :param app: The Sphinx Application instance
    :param _: The master Sphinx BuildEnvironment object; unused
    :param docnames: A list of the document names to merge
    :param other: The Sphinx BuildEnvironment from the reader worker
    """
    if not hasattr(app.env, "sphinx_tabs"):
        app.env.sphinx_tabs = {}
    if hasattr(other, "sphinx_tabs"):
        for docname in docnames:
            if docname in other.sphinx_tabs:
                if docname not in app.env.sphinx_tabs:
                    app.env.sphinx_tabs[docname] = []
                if (
                    len(app.env.sphinx_tabs[docname]) > 0
                    and len(other.sphinx_tabs[docname]) == 0
                ):
                    logger.warning(
                        f"{LOG_PREFIX} env_merge_info: {docname}; not overwriting app.env with empty list from other"
                    )
                    continue
                app.env.sphinx_tabs[docname] = other.sphinx_tabs[docname].copy()


def doctree_read(app: Sphinx, doctree: nodes.document):
    """
    Construct a new Table of Contents for documents that have inline tabs

    :param app: The Sphinx Application instance
    :param doctree: The parsed document tree; unused
    """
    if not hasattr(app.env, "sphinx_tabs"):
        app.env.sphinx_tabs = {}
    if (
        app.env.docname in app.env.sphinx_tabs
        and len(app.env.sphinx_tabs[app.env.docname]) > 0
    ):
        logger.debug(f"{LOG_PREFIX} doctree_read: {app.env.docname} has tabs")
        updated_tocs: nodes.list_item = sectiondata_to_toc(
            app.env.docname,
            collect_sections(app.env, doctree, app.env.docname, doctree),
        )
        logger.debug(
            f"{LOG_PREFIX} doctree_read({app.env.docname}): updated_tocs[0][1]={updated_tocs}"
        )
        if len(app.env.tocs[app.env.docname][0]) == 1:
            app.env.tocs[app.env.docname][0].append(updated_tocs)
        else:
            app.env.tocs[app.env.docname][0][1] = updated_tocs
        app.env.sphinx_tabs[app.env.docname].clear()


def html_page_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Optional[nodes.document],
) -> Optional[str]:
    """
    Remove Furo's JavaScript asset file for pages that have inline tabs.

    :param app:
    :param pagename:
    :param templatename:
    :param context:
    :param doctree:
    :return:
    """
    if hasattr(app.env, "sphinx_tabs"):
        if pagename in app.env.sphinx_tabs:
            logger.debug(
                f"{LOG_PREFIX} html_page_context: {pagename}; context.keys()={context.keys()}"
            )
            if "script_files" in context and len(context["script_files"]) > 0:
                furo_js_asset_index: int = -1
                for idx, script_asset in enumerate(context["script_files"]):
                    if script_asset.filename == FURO_SCRIPT_ASSET_FILENAME:
                        furo_js_asset_index = idx
                        logger.debug(
                            f"{LOG_PREFIX} html_page_context: {pagename}; furo_js_asset_index={furo_js_asset_index}"
                        )
                        break
                if furo_js_asset_index > -1:
                    logger.debug(
                        f"{LOG_PREFIX} html_page_context: {pagename}; remove furo JS asset"
                    )
                    context["script_files"].pop(furo_js_asset_index)

    return None


def collect_sections(
    env: BuildEnvironment,
    document: nodes.document,
    docname: str,
    node: nodes.Element,
    level=0,
    tab_counter=0,
) -> SectionData:
    """
    Recursively collect subsection metadata from inline tab content.

    :param env:
    :param document:
    :param docname:
    :param node:
    :param level:
    :param tab_counter:
    :return:
    """
    logger.debug(
        f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] node={type(node)}"
    )
    secdata = SectionData(
        name=docname if level == 0 else "",
        level=level,
        tab_counter=tab_counter,
        is_doc_root=level == 0,
        is_section_root=level == 1,
        is_tab=isinstance(node, TabContainer),
        id="",
        children=[],
    )

    if isinstance(node, nodes.section):
        secdata.name = node.next_node(nodes.title).astext()
        logger.debug(
            f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] Section: {secdata.name}"
        )
    elif isinstance(node, TabContainer):
        secdata.name = node.next_node(nodes.label).astext()
        logger.debug(
            f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] TabContainer: {secdata.name}"
        )

    section_id: str = ""
    #if isinstance(node, TabContainer) and "inline_tab_id" in node.attributes:
    #    section_id = node.attributes["inline_tab_id"]
    #else:
    if node.attributes["ids"]:
        logger.debug(
            f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] node ids: {node.attributes['ids']}"
        )
        if len(node.attributes["ids"]) == 1 and node.attributes["ids"][0] != "":
            section_id = node.attributes["ids"][0]
            logger.debug(
                f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] using ids[0] attribute: {section_id}"
            )
        elif len(node.attributes["ids"]) > 1:
            for id in node.attributes["ids"]:
                if TabId.is_tab_id(id):
                    section_id = id
                    logger.debug(
                        f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] using TabId attribute: {section_id}"
                    )
                    break
                else:
                    logger.debug(f"+++ {LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] id {id} is not a TabId")
    if section_id == "":
        section_id = _make_id(secdata.name)
        logger.debug(
            f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] make section_id from secdata.name({secdata.name}): {section_id}"
        )
    secdata.id = section_id
    logger.debug(
        f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] secdata.id: {secdata.id}"
    )

    # FIXME: is this still necessary?
    # parent_node: nodes.Element = (
    #     node.next_node(nodes.container) if isinstance(node, TabContainer) else node
    # )

    #for child in parent_node.children:
    for idx, child in enumerate(node.children):
        logger.debug(
            f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] child[{idx}]={type(child)}"
        )
        if isinstance(child, nodes.section):
            secdata.children.append(
                collect_sections(env, document, docname, child, level + 1, tab_counter)
            )
        elif isinstance(child, TabContainer):
            secdata.children.append(
                collect_sections(env, document, docname, child, level + 1, tab_counter + 1)
            )

    return secdata


def dump_sections(docname: str, secdata: SectionData):
    """
    Recursively display subsection metadata collected from inline tab content.
    Useful for extension debugging.

    :param docname:
    :param secdata:
    :return:
    """
    logger.debug(
        f"{LOG_PREFIX} dump_sections(): ({docname}) [{secdata.level}/{secdata.tab_counter}] "
        f"{secdata.name}/{secdata.id}: {secdata.get_section_type()}, "
        f"{len(secdata.children)} children"
    )
    for child in secdata.children:
        dump_sections(docname, child)


def sectiondata_to_toc(docname: str, secdata: SectionData) -> nodes.list_item:
    """
    Convert collected subsection metadata into a new Table of Contents for a document
    with inline tabs.

    :param docname:
    :param secdata:
    :return:
    """
    logger.debug(
        f"{LOG_PREFIX} sectiondata_to_toc(): "
        f"({docname}): [{secdata.level}/{secdata.tab_counter}] {secdata.name}<{secdata.id}>, {len(secdata.children)} children"
    )
    if secdata.is_doc_root:
        logger.debug(
            f"{LOG_PREFIX} sectiondata_to_toc(): "
            f"({docname}): [{secdata.level}/{secdata.tab_counter}] return sectiondata_to_toc(..., secdata.children[0])"
        )
        return sectiondata_to_toc(docname, secdata.children[0])

    list_item: nodes.list_item = nodes.list_item()

    if not secdata.is_section_root:
        # Don't add a reference for the section root since it will be displayed in the ToC
        logger.debug(
            f"{LOG_PREFIX} sectiondata_to_toc(): "
            f"({docname}): [{secdata.level}/{secdata.tab_counter}] add reference for {secdata.name}<{secdata.id}>"
        )
        list_item.append(make_compact_reference(secdata.id, secdata.name, docname))

    if len(secdata.children) > 0:
        logger.debug(
            f"{LOG_PREFIX} sectiondata_to_toc(): "
            f"({docname}): [{secdata.level}/{secdata.tab_counter}] children: {','.join([sd.name for sd in secdata.children])}"
        )
        bullet_list: nodes.bullet_list = nodes.bullet_list()
        for idx, child in enumerate(secdata.children):
            logger.debug(
                f"{LOG_PREFIX} sectiondata_to_toc(): "
                f"({docname}): [{secdata.level}/{secdata.tab_counter}] child {idx+1}/{len(secdata.children)}"
            )
            bullet_list.append(sectiondata_to_toc(docname, child))
        list_item.append(bullet_list)

    return list_item


def make_compact_reference(
    section_id: str, section_name: str, docname: str
) -> addnodes.compact_paragraph:
    """
    Create a subsection reference node using the Sphinx compact_paragraph
    node.

    :param section_id:
    :param section_name:
    :param docname:
    :return:
    """
    cpara: addnodes.compact_paragraph = addnodes.compact_paragraph()
    cpara.append(
        nodes.reference(
            "",
            section_name,
            refuri=docname,
            anchorname=f"#{section_id}",
            internal=True,
        )
    )
    return cpara
