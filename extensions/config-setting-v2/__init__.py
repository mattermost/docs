import json
import pathlib
import docutils.core, docutils.io
from docutils import nodes
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
from sphinx.util.docutils import SphinxTranslator, SphinxDirective
from sphinx.util.nodes import make_refnode
from typing import Optional, Iterable, Tuple, List, Dict, Any

__version__ = "0.2.0"

CONFIG_SETTING_ANCHOR = "anchor"
CONFIG_SETTING_DOCNAME = "docname"
CONFIG_SETTING_ID = "id"
CONFIG_SETTING_DISPLAYNAME = "displayname"
CONFIG_SETTING_SYSTEMCONSOLE = "systemconsole"
CONFIG_SETTING_CONFIGJSON = "configjson"
CONFIG_SETTING_ENVIRONMENT = "environment"
CONFIG_SETTING_DESCRIPTION = "description"

# Sphinx logger
logger = logging.getLogger(__name__)


def rst2html(source_string: str) -> str:
    # mostly taken from
    # https://github.com/getpelican/pelican/
    pub: docutils.core.Publisher = docutils.core.Publisher(
        source_class=docutils.io.StringInput, destination_class=docutils.io.StringOutput
    )
    pub.set_components("standalone", "restructuredtext", "html")
    pub.process_programmatic_settings(None, None, None)
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


def visit_anchor_node(visitor: SphinxTranslator, node: AnchorNode) -> None:
    """
    Write the opening HTML tag for the anchor node
      :param visitor: The translator that handles writing HTML bodies
      :param node: The docutils node we're visiting
      :return: None
    """
    visitor.body.append('<%s id="%s">' % (node.tagname, node.anchor))


def depart_anchor_node(visitor: SphinxTranslator, node: AnchorNode) -> None:
    """
    Write the closing HTML tag for the anchor node
      :param visitor: The translator that handles writing HTML bodies
      :param node: The docutils node we're departing
      :return: None
    """
    visitor.body.append(f"</{node.tagname}>")


class ConfigSettingNode(Element):
    config_settings: Dict[str, str]

    def __init__(self, settings: Optional[Dict[str, str]]):
        super().__init__()
        self.config_settings = dict()
        if settings is not None:
            self.config_settings = settings


def visit_config_setting_node(
    visitor: SphinxTranslator, node: ConfigSettingNode
) -> None:
    return


def depart_config_setting_node(
    visitor: SphinxTranslator, node: ConfigSettingNode
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

    def run(self) -> List[Node]:
        replacement_nodes: List[Node] = list()
        # Add an anchor node, so we can refer to this section later
        replacement_nodes.append(AnchorNode(self.arguments[0]))
        # If there is content, then collect it into a string and append it to the short description
        long_description = ""
        for content_line in self.content:
            if content_line != "":
                long_description += content_line.rstrip()
            long_description += "\n"
        short_description = ""
        if CONFIG_SETTING_DESCRIPTION in self.options:
            short_description = self.options[CONFIG_SETTING_DESCRIPTION]
        # If the short description is non-empty, append two newlines so that it is treated as a new paragraph
        if short_description != "":
            short_description += "\n\n"
        # Parse RST content in the description into HTML, so it can be displayed richly on the browser side
        description = rst2html(short_description + long_description.rstrip())
        # Add a ConfigSettingNode that contains the metadata for the setting
        config_setting = {
            CONFIG_SETTING_ID: self.arguments[0],
            CONFIG_SETTING_DISPLAYNAME: self.options[CONFIG_SETTING_DISPLAYNAME],
            CONFIG_SETTING_SYSTEMCONSOLE: self.options[CONFIG_SETTING_SYSTEMCONSOLE],
            CONFIG_SETTING_CONFIGJSON: self.options[CONFIG_SETTING_CONFIGJSON],
            CONFIG_SETTING_ENVIRONMENT: self.options[CONFIG_SETTING_ENVIRONMENT],
            CONFIG_SETTING_DESCRIPTION: description,
        }
        replacement_nodes.append(ConfigSettingNode(config_setting))
        # Get the domain and add a reference to this config setting, so we can process XRefs
        config_domain = self.env.domains["config"]
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
            return "config.setting_%s" % node.config_settings[CONFIG_SETTING_ID]
        return "{}.{}".format("config", node.arguments[0])

    def get_objects(self) -> Iterable[Tuple[str, str, str, str, str, int]]:
        # yield from an empty list, so we do not add anything to the Sphinx search index
        yield from list()

    def merge_domaindata(self, docnames: List[str], otherdata: Dict) -> None:
        self.data["configs"].extend(otherdata["configs"])

    def resolve_any_xref(
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        target: str,
        node: pending_xref,
        contnode: Element,
    ) -> List[Tuple[str, Element]]:
        return list()

    def resolve_xref(
        self, env, fromdocname, builder, typ, target, node, contnode
    ) -> Optional[Node]:
        match = [
            (docname, anchor)
            for name, sig, typ, docname, anchor, prio in self.data["configs"]
            if sig == target
        ]
        if len(match) > 0:
            todocname = match[0][0]
            targ = match[0][1]
            return make_refnode(builder, fromdocname, todocname, targ, contnode, targ)
        else:
            logger.warning(
                "ConfigSettingDomain: resolve_xref(): "
                "unable to resolve crossreference; fromdocname=%s, typ=%s, target=%s"
                % (fromdocname, typ, target)
            )
            return None

    def add_config_setting(self, setting: dict[str, str]) -> None:
        """
        Add a config setting to the list of config settings
          :param setting: Setting metadata
          :return: None
        """
        name = "config.setting_%s" % setting[CONFIG_SETTING_ID]
        anchor = setting[CONFIG_SETTING_ID]
        config_setting = (
            name,
            setting[CONFIG_SETTING_DISPLAYNAME],
            "setting",
            self.env.docname,
            anchor,
            0,
        )
        logger.verbose(
            "ConfigSettingDomain: add_config_setting(): "
            "appending config: name=%s, dispname=%s, type=%s, docname=%s, anchor=%s, priority=%d"
            % config_setting
        )
        self.data["configs"].append(config_setting)


def env_purge_doc(app: Sphinx, env: BuildEnvironment, docname: str) -> None:
    if hasattr(env, "config_settings"):
        if docname in env.config_settings:
            logger.verbose(
                "config-setting-v2: env_purge_doc(): removing doc %s from config_settings"
                % docname
            )
            env.config_settings.pop(docname)


def env_merge_info(
    app: Sphinx, env: BuildEnvironment, docnames: List[str], other: BuildEnvironment
) -> None:
    if not hasattr(env, "config_settings"):
        env.config_settings = dict()
    if hasattr(other, "config_settings"):
        for docname in docnames:
            if docname in other.config_settings:
                logger.verbose(
                    "config-setting-v2: env_merge_info(): adding %d settings to config_settings[%s]"
                    % (len(other.config_settings[docname]), docname)
                )
                if len(other.config_settings[docname]) > 0:
                    env.config_settings[docname] = other.config_settings[docname]


def doctree_read(app: Sphinx, doctree: nodes.document):
    if not hasattr(app.env, "config_settings"):
        app.env.config_settings = dict()
    # Check if this document has the :nosearch: metadata attribute; skip if it does
    if app.env.docname in app.env.metadata:
        if "nosearch" in app.env.metadata[app.env.docname]:
            logger.debug(
                "config-setting-v2: doctree_read(): doc %s has :nosearch: attribute; skipping it"
                % app.env.docname
            )
            return
    config_nodes = doctree.traverse(ConfigSettingNode, False, True, False, False)
    if len(config_nodes) == 0:
        return
    logger.verbose(
        "config-setting-v2: doctree_read(): found %d ConfigSettingNodes in doc %s"
        % (len(config_nodes), app.env.docname)
    )
    doc_config_settings: List[Dict[str, str]] = list()
    for config_node in config_nodes:
        doc_config_settings.append(config_node.config_settings)
    if len(doc_config_settings) > 0:
        logger.info(
            "config-setting-v2: %d config settings in %s"
            % (len(doc_config_settings), app.env.docname)
        )
        if app.env.docname not in app.env.config_settings:
            app.env.config_settings[app.env.docname] = list()
        app.env.config_settings[app.env.docname].extend(doc_config_settings)
    else:
        logger.verbose(
            "config-setting-v2: doctree_read(): no config settings in doc %s"
            % app.env.docname
        )


def build_finished(app: Sphinx, exception: Exception):
    if exception is not None:
        return
    if hasattr(app.env, "config_settings"):
        logger.info(bold("writing config setting search index... "), nonl=True)
        # create config setting search index
        settings_index: List[Dict[str, str]] = list()
        for docname in app.env.config_settings:
            for config_setting in app.env.config_settings[docname]:
                config_setting[CONFIG_SETTING_DOCNAME] = docname
                config_setting[CONFIG_SETTING_ANCHOR] = (
                    docname + ".html#" + config_setting[CONFIG_SETTING_ID]
                )
                settings_index.append(config_setting)
        # dump to a JSON file
        outfile = pathlib.PurePath(app.outdir, "config-settings-index.json")
        with open(outfile, "w") as fout:
            json.dump(settings_index, fout)
        logger.info("done")


def setup(app: Sphinx) -> Dict[str, Any]:
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
