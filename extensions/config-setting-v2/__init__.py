import json
from pathlib import Path
from typing import Optional, Iterable, Any, Final

import docutils.core, docutils.io
from docutils import nodes, SettingsSpec
from docutils.nodes import Element, Node
from docutils.parsers.rst.directives import unchanged
from sphinx.addnodes import pending_xref
from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.domains import Domain
from sphinx.environment import BuildEnvironment
from sphinx.roles import XRefRole
from sphinx.util import logging
from sphinx.util.console import bold  # type: ignore
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import make_refnode
from sphinx.writers.html5 import HTML5Translator


__version__ = "0.3.0"

CONFIG_SETTING_ANCHOR: Final[str] = "anchor"
CONFIG_SETTING_DOCNAME: Final[str] = "docname"
CONFIG_SETTING_ID: Final[str] = "id"
CONFIG_SETTING_DISPLAYNAME: Final[str] = "displayname"
CONFIG_SETTING_SYSTEMCONSOLE: Final[str] = "systemconsole"
CONFIG_SETTING_CONFIGJSON: Final[str] = "configjson"
CONFIG_SETTING_ENVIRONMENT: Final[str] = "environment"
CONFIG_SETTING_DESCRIPTION: Final[str] = "description"

LOG_PREFIX: Final[str] = "[config-setting-v2]"

# Sphinx logger
logger: logging.SphinxLoggerAdapter = logging.getLogger(__name__)


def rst2html(source_string: str) -> str:
    # mostly taken from
    # https://github.com/getpelican/pelican/
    pub: docutils.core.Publisher = docutils.core.Publisher(
        source_class=docutils.io.StringInput, destination_class=docutils.io.StringOutput
    )
    pub.set_components("standalone", "restructuredtext", "html")
    pub.process_programmatic_settings(SettingsSpec(), None, "")
    pub.set_source(source=source_string)
    pub.publish()
    # publish parts are described here: https://docutils.sourceforge.io/docs/api/publisher.html#publish-parts-details
    return pub.writer.parts["fragment"]


class AnchorNode(Element):
    """
    A docutils node that writes an ``<a>`` tag that includes a specific id
    """

    anchor: str

    def __init__(self, href: str):
        super().__init__()
        self.tagname = "a"
        self.anchor = href


def visit_anchor_node(visitor: HTML5Translator, node: AnchorNode) -> None:
    """
    Write the opening HTML tag for the anchor node
      :param visitor: The translator that handles writing HTML bodies
      :param node: The docutils node we're visiting
      :return: None
    """
    visitor.body.append('<%s id="%s">' % (node.tagname, node.anchor))


def depart_anchor_node(visitor: HTML5Translator, node: AnchorNode) -> None:
    """
    Write the closing HTML tag for the anchor node
      :param visitor: The translator that handles writing HTML bodies
      :param node: The docutils node we're departing
      :return: None
    """
    visitor.body.append(f"</{node.tagname}>")


class ConfigSettingNode(Element):
    config_settings: dict[str, str]

    def __init__(self, settings: Optional[dict[str, str]]):
        super().__init__()
        self.config_settings = {}
        if settings is not None:
            self.config_settings = settings


def visit_config_setting_node(
    visitor: HTML5Translator, node: ConfigSettingNode
) -> None:
    return


def depart_config_setting_node(
    visitor: HTML5Translator, node: ConfigSettingNode
) -> None:
    return


class ConfigSettingDirective(SphinxDirective):
    has_content = True
    required_arguments = 1
    option_spec = {
        CONFIG_SETTING_DISPLAYNAME: unchanged,
        CONFIG_SETTING_SYSTEMCONSOLE: unchanged,
        CONFIG_SETTING_CONFIGJSON: unchanged,
        CONFIG_SETTING_ENVIRONMENT: unchanged,
        CONFIG_SETTING_DESCRIPTION: unchanged,
    }

    def run(self) -> list[Node]:
        # Add an anchor node, so we can refer to this section later
        replacement_nodes: list[Node] = [AnchorNode(self.arguments[0])]
        # If there is content, then collect it into a string and append it to the short description
        long_description: str = ""
        for content_line in self.content:
            if content_line != "":
                long_description += content_line.rstrip()
            long_description += "\n"
        short_description: str = ""
        if CONFIG_SETTING_DESCRIPTION in self.options:
            short_description = self.options[CONFIG_SETTING_DESCRIPTION]
        # If the short description is non-empty, append two newlines so that it is treated as a new paragraph
        if short_description != "":
            short_description += "\n\n"
        # Parse RST content in the description into HTML, so it can be displayed richly on the browser side
        description: str = rst2html(short_description + long_description.rstrip())
        # Add a ConfigSettingNode that contains the metadata for the setting
        config_setting: dict[str, str] = {
            CONFIG_SETTING_ID: self.arguments[0],
            CONFIG_SETTING_DISPLAYNAME: self.options[CONFIG_SETTING_DISPLAYNAME],
            CONFIG_SETTING_SYSTEMCONSOLE: self.options[CONFIG_SETTING_SYSTEMCONSOLE],
            CONFIG_SETTING_CONFIGJSON: self.options[CONFIG_SETTING_CONFIGJSON],
            CONFIG_SETTING_ENVIRONMENT: self.options[CONFIG_SETTING_ENVIRONMENT],
            CONFIG_SETTING_DESCRIPTION: description,
        }
        replacement_nodes.append(ConfigSettingNode(config_setting))
        # Get the domain and add a reference to this config setting, so we can process XRefs
        config_domain: Domain = self.env.domains["config"]
        if isinstance(config_domain, ConfigSettingDomain):
            config_domain.add_config_setting(config_setting)
        return replacement_nodes


class ConfigSettingDomain(Domain):
    """
    A domain to hold references to individual config settings.
    """

    name = "config"
    label = "Mattermost configuration setting"
    roles = {
        "ref": XRefRole(),
    }
    directives = {
        "setting": ConfigSettingDirective,
    }
    initial_data = {
        # List[Tuple[str, str, str, str, str, int]] ==> List[Tuple[name, dispname, type, docname, anchor, priority]]
        "configs": list(),
    }

    def get_full_qualified_name(self, node: Element) -> Optional[str]:
        if isinstance(node, ConfigSettingNode):
            return f"config.setting_{node.config_settings[CONFIG_SETTING_ID]}"
        return f"config.{node.arguments[0]}"

    def get_objects(self) -> Iterable[tuple[str, str, str, str, str, int]]:
        # yield from an empty list, so we do not add anything to the Sphinx search index
        yield from []

    def merge_domaindata(self, docnames: list[str], otherdata: dict[str, Any]) -> None:
        self.data["configs"].extend(otherdata["configs"])

    def resolve_any_xref(
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        target: str,
        node: pending_xref,
        contnode: Element,
    ) -> list[tuple[str, Element]]:
        return []

    def resolve_xref(
        self, env, fromdocname, builder, typ, target, node, contnode
    ) -> Optional[Node]:
        match: list[tuple[str, str]] = [
            (docname, anchor)
            for name, sig, typ, docname, anchor, prio in self.data["configs"]
            if sig == target
        ]
        if len(match) > 0:
            todocname: str = match[0][0]
            targ: str = match[0][1]
            return make_refnode(builder, fromdocname, todocname, targ, contnode, targ)
        else:
            logger.warning(
                f"{LOG_PREFIX} ConfigSettingDomain: resolve_xref(): "
                f"unable to resolve crossreference; fromdocname={fromdocname}, typ={typ}, target={target}"
            )
            return None

    def add_config_setting(self, setting: dict[str, str]) -> None:
        """
        Add a config setting to the list of config settings
          :param setting: Setting metadata
          :return: None
        """
        name: str = f"config.setting_{setting[CONFIG_SETTING_ID]}"
        anchor: str = setting[CONFIG_SETTING_ID]
        config_setting: tuple[str, str, str, str, str, int] = (
            name,
            setting[CONFIG_SETTING_DISPLAYNAME],
            "setting",
            self.env.docname,
            anchor,
            0,
        )
        logger.verbose(
            f"{LOG_PREFIX} ConfigSettingDomain: add_config_setting(): "
            "appending config: name=%s, dispname=%s, type=%s, docname=%s, anchor=%s, priority=%d"
            % config_setting
        )
        self.data["configs"].append(config_setting)


def env_purge_doc(app: Sphinx, env: BuildEnvironment, docname: str) -> None:
    if hasattr(env, "config_settings"):
        if docname in env.config_settings:
            logger.verbose(
                f"{LOG_PREFIX} env_purge_doc(): removing doc {docname} from config_settings"
            )
            env.config_settings.pop(docname)


def env_merge_info(
    app: Sphinx, env: BuildEnvironment, docnames: list[str], other: BuildEnvironment
) -> None:
    if not hasattr(env, "config_settings"):
        env.config_settings = {}
    if hasattr(other, "config_settings"):
        for docname in docnames:
            if docname in other.config_settings:
                logger.verbose(
                    f"{LOG_PREFIX} env_merge_info(): "
                    f"adding {len(other.config_settings[docname])} settings to config_settings[{docname}]"
                )
                if len(other.config_settings[docname]) > 0:
                    env.config_settings[docname] = other.config_settings[docname]


def doctree_read(app: Sphinx, doctree: nodes.document):
    if not hasattr(app.env, "config_settings"):
        app.env.config_settings = {}
    # Check if this document has the :nosearch: metadata attribute; skip if it does
    if app.env.docname in app.env.metadata:
        if "nosearch" in app.env.metadata[app.env.docname]:
            logger.debug(
                f"{LOG_PREFIX} doctree_read(): doc {app.env.docname} has :nosearch: attribute; skipping it"
            )
            return
    config_nodes: list[ConfigSettingNode] = []
    for config_node in doctree.findall(ConfigSettingNode, False, True, False, False):
        config_nodes.append(config_node)
    if len(config_nodes) == 0:
        return
    logger.verbose(
        f"{LOG_PREFIX} doctree_read(): found {len(config_nodes)} ConfigSettingNodes in doc {app.env.docname}"
    )
    doc_config_settings: list[dict[str, str]] = []
    for config_node in config_nodes:
        doc_config_settings.append(config_node.config_settings)
    if len(doc_config_settings) > 0:
        logger.info(
            f"{LOG_PREFIX} {len(doc_config_settings)} config settings in {app.env.docname}"
        )
        if app.env.docname not in app.env.config_settings:
            app.env.config_settings[app.env.docname] = []
        app.env.config_settings[app.env.docname].extend(doc_config_settings)
    else:
        logger.verbose(
            f"{LOG_PREFIX} doctree_read(): no config settings in doc {app.env.docname}"
        )


def build_finished(app: Sphinx, exception: Exception):
    if exception is not None:
        return
    if hasattr(app.env, "config_settings"):
        logger.info(bold("writing config setting search index... "), nonl=True)
        # create config setting search index
        settings_index: list[dict[str, str]] = []
        for docname in app.env.config_settings:
            for config_setting in app.env.config_settings[docname]:
                config_setting[CONFIG_SETTING_DOCNAME] = docname
                config_setting[CONFIG_SETTING_ANCHOR] = (
                    f"{docname}.html#{config_setting[CONFIG_SETTING_ID]}"
                )
                settings_index.append(config_setting)
        # dump to a JSON file
        outfile: Path = Path(app.outdir) / "config-settings-index.json"
        with outfile.open("w") as fout:
            json.dump(settings_index, fout)
        logger.info("done")


def setup(app: Sphinx) -> dict[str, Any]:
    """
    Sphinx extension entry point
      :param app: The Sphinx application instance
      :return: A dict of extension options
    """
    app.add_node(AnchorNode, html=(visit_anchor_node, depart_anchor_node))
    app.add_node(
        ConfigSettingNode, html=(visit_config_setting_node, depart_config_setting_node)
    )
    app.add_domain(ConfigSettingDomain)
    app.connect("env-purge-doc", env_purge_doc)
    app.connect("env-merge-info", env_merge_info)
    app.connect("doctree-read", doctree_read)
    app.connect("build-finished", build_finished)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
