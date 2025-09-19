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

from .directive import LOG_PREFIX, INLINE_TAB_DOCNAMES
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
    if hasattr(app.env, INLINE_TAB_DOCNAMES):
        tab_docnames: list[str] = getattr(app.env, INLINE_TAB_DOCNAMES)
        if docname in tab_docnames:
            tab_docnames.remove(docname)


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
    if not hasattr(app.env, INLINE_TAB_DOCNAMES):
        setattr(app.env, INLINE_TAB_DOCNAMES, [])
    tab_docnames: list[str] = getattr(app.env, INLINE_TAB_DOCNAMES)
    if hasattr(other, INLINE_TAB_DOCNAMES):
        other_tab_docnames: list[str] = getattr(other, INLINE_TAB_DOCNAMES)
        for docname in docnames:
            if docname in other_tab_docnames:
                if docname not in tab_docnames:
                    tab_docnames.append(docname)


def doctree_read(app: Sphinx, doctree: nodes.document):
    """
    Construct a new Table of Contents for documents that have inline tabs

    :param app: The Sphinx Application instance
    :param doctree: The parsed document tree; unused
    """
    if not hasattr(app.env, INLINE_TAB_DOCNAMES):
        setattr(app.env, INLINE_TAB_DOCNAMES, [])
    tab_docnames: list[str] = getattr(app.env, INLINE_TAB_DOCNAMES)
    if app.env.docname in tab_docnames:
        logger.debug(f"{LOG_PREFIX} doctree_read: {app.env.docname} has tabs")
        
        # Generate the tab-based TOC (includes headings from within tabs)
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
    if hasattr(app.env, INLINE_TAB_DOCNAMES):
        tab_docnames: list[str] = getattr(app.env, INLINE_TAB_DOCNAMES)
        if pagename in tab_docnames:
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
    Recursively collect TabContainer and section metadata from inline tab content.

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
                    logger.debug(
                        f"+++ {LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] id {id} is not a TabId"
                    )
    if section_id == "":
        section_id = _make_id(secdata.name)
        logger.debug(
            f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] make section_id from secdata.name({secdata.name}): {section_id}"
        )
    secdata.id = section_id
    logger.debug(
        f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] secdata.id: {secdata.id}"
    )

    # Handle TabContainer specially - need to look inside the content container for sections
    if isinstance(node, TabContainer):
        logger.debug(
            f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] TabContainer with {len(node.children)} children"
        )
        # TabContainer structure: child[0] = label, child[1] = content container
        if len(node.children) >= 2:
            content_container = node.children[1]  # The content container
            logger.debug(
                f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] TabContainer content_container type: {type(content_container)}"
            )
            # Look for sections within the content container
            if hasattr(content_container, "children"):
                for idx, child in enumerate(content_container.children):
                    logger.debug(
                        f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] TabContainer content child[{idx}]={type(child)}"
                    )
                    if isinstance(child, nodes.section):
                        secdata.children.append(
                            collect_sections(
                                env, document, docname, child, level + 1, tab_counter
                            )
                        )
                    elif isinstance(child, TabContainer):
                        secdata.children.append(
                            collect_sections(
                                env,
                                document,
                                docname,
                                child,
                                level + 1,
                                tab_counter + 1,
                            )
                        )
    else:
        # For non-TabContainer nodes, process children normally
        for idx, child in enumerate(node.children):
            logger.debug(
                f"{LOG_PREFIX} collect_sections({docname}): [{level}/{tab_counter}] child[{idx}]={type(child)}"
            )
            if isinstance(child, nodes.section):
                secdata.children.append(
                    collect_sections(
                        env, document, docname, child, level + 1, tab_counter
                    )
                )
            elif isinstance(child, TabContainer):
                secdata.children.append(
                    collect_sections(
                        env, document, docname, child, level + 1, tab_counter + 1
                    )
                )

    return secdata


def dump_sections(docname: str, secdata: SectionData):
    """
    Recursively display subsection metadata collected from inline tab content.
    Useful for extension debugging.

    :param docname: The name of the current document
    :param secdata: The subsection data to display
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
    Convert collected TabContent and section metadata into a new Table of Contents for a document
    with inline tabs.

    :param docname: The name of the current document
    :param secdata: The subsection data to process
    :return:
    """
    logger.debug(
        f"{LOG_PREFIX} sectiondata_to_toc(): "
        f"({docname}): [{secdata.level}/{secdata.tab_counter}] {secdata.name}<{secdata.id}>, {len(secdata.children)} children"
    )
    if secdata.is_doc_root:
        logger.debug(
            f"{LOG_PREFIX} sectiondata_to_toc(): "
            f"({docname}): [{secdata.level}/{secdata.tab_counter}] processing doc root with {len(secdata.children)} children"
        )

        # For doc root, we need to process ALL children, not just the first one
        if len(secdata.children) == 0:
            return nodes.list_item()  # Empty if no children

        # If there's only one child, delegate to it
        if len(secdata.children) == 1:
            return sectiondata_to_toc(docname, secdata.children[0])

        # Multiple children - create a list containing all of them
        list_item: nodes.list_item = nodes.list_item()
        bullet_list: nodes.bullet_list = nodes.bullet_list()

        for idx, child in enumerate(secdata.children):
            logger.debug(
                f"{LOG_PREFIX} sectiondata_to_toc(): "
                f"({docname}): processing doc root child {idx+1}/{len(secdata.children)}: {child.name}"
            )
            child_item = sectiondata_to_toc(docname, child)
            bullet_list.append(child_item)

        list_item.append(bullet_list)
        return list_item

    # For non-doc-root sections, create a proper list item
    list_item: nodes.list_item = nodes.list_item()

    # Add a reference for this section (including tabs and regular sections)
    # Only skip adding reference if this is a section root with no meaningful name
    if secdata.name and not (secdata.is_section_root and secdata.name == secdata.id):
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

    :param section_id: Node ID of the section to link to
    :param section_name: Name of the section to link to
    :param docname: Name of the current document
    :return: A compact_paragraph node containing a reference to the section
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
