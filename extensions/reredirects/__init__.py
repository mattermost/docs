#
# reredirects - The sphinx_reredirects extension with parallel read and write support enabled, and support for
#               intra-page redirects.
#
# Parallel read/write, and intra-page redirect support by Alan Lew <alan@ethereal.cc> (https://github.com/neflyte/)
#
import re
from fnmatch import fnmatch
from pathlib import Path
from string import Template
from typing import Dict, Mapping, Tuple, Any, List
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util import logging
from sphinx.util.console import bold, colorize, term_width_line  # type: ignore

OPTION_REDIRECTS = "redirects"
OPTION_REDIRECTS_DEFAULT: Dict[str, str] = dict()
OPTION_TEMPLATE_FILE = "redirect_html_template_file"
OPTION_TEMPLATE_FILE_DEFAULT = None
REDIRECT_FILE_DEFAULT_TEMPLATE = '<!DOCTYPE html><html lang="en"><head><title>Redirect</title><meta http-equiv="refresh" content="0; url=${to_uri}"></head></html>'  # noqa: E501
DEFAULT_PAGE = "-"
ENV_REDIRECTS_ENABLED = "redirects-enabled"
ENV_COMPUTED_REDIRECTS = "computed-redirects"
ENV_INTRA_PAGE_FRAGMENT_PAGES = "intra-page-fragment-pages"
CTX_HAS_FRAGMENT_REDIRECTS = "has_fragment_redirects"
CTX_FRAGMENT_REDIRECTS = "fragment_redirects"
CONFIG_HTML_BASEURL = "html_baseurl"
CONFIG_MM_URL_PATH_PREFIX = "mm_url_path_prefix"

# Sphinx logger
logger = logging.getLogger(__name__)

wildcard_pattern = re.compile(r"[*?\[\]]")


def setup(app: Sphinx) -> Dict[str, Any]:
    """
    Sphinx extension setup function.

    :param app: The Sphinx Application instance
    :return: A dict of Sphinx extension options
    """
    app.add_config_value(OPTION_REDIRECTS, OPTION_REDIRECTS_DEFAULT, "env")
    app.add_config_value(OPTION_TEMPLATE_FILE, OPTION_TEMPLATE_FILE_DEFAULT, "env")
    app.add_config_value(CONFIG_MM_URL_PATH_PREFIX, "", "env")
    app.connect("builder-inited", builder_inited)
    app.connect("env-purge-doc", env_purge_doc)
    app.connect("env-merge-info", env_merge_info)
    app.connect("env-updated", env_updated)
    app.connect("html-page-context", html_page_context)
    app.connect("html-collect-pages", html_collect_pages)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def builder_inited(app: Sphinx):
    setattr(app.env, ENV_REDIRECTS_ENABLED, True)
    if not app.config[OPTION_REDIRECTS]:
        logger.warning(
            "No redirects configured; disabling redirects extension for this build"
        )
        setattr(app.env, ENV_REDIRECTS_ENABLED, False)
        return
    if len(app.config[OPTION_REDIRECTS]) == 0:
        logger.warning(
            "Empty redirect definition; disabling redirects extension for this build"
        )
        setattr(app.env, ENV_REDIRECTS_ENABLED, False)
        return
    redirects_option: Dict[str, str] = getattr(app.config, OPTION_REDIRECTS)
    setattr(app.env, ENV_COMPUTED_REDIRECTS, compute_redirects(app, redirects_option))


def env_purge_doc(app: Sphinx, env: BuildEnvironment, docname: str):
    """
    Stub function for the `env-purge-doc` event; does nothing
    """
    return


def env_merge_info(
    app: Sphinx, env: BuildEnvironment, docnames: List[str], other: BuildEnvironment
):
    """
    Stub function for the `env-merge-info` event; does nothing
    """
    return


def env_updated(app: Sphinx, env: BuildEnvironment) -> List[str]:
    is_enabled: bool = getattr(app.env, ENV_REDIRECTS_ENABLED)
    if not is_enabled:
        return list()
    computed_redirects: Dict[str, Dict[str, str]] = getattr(env, ENV_COMPUTED_REDIRECTS)
    intra_page_fragments: List[str] = list()
    for page in computed_redirects.keys():
        if page in env.all_docs:
            intra_page_fragments.append(page)
    logger.debug(
        "env_updated(): found %d intra-page fragment pages" % len(intra_page_fragments)
    )
    setattr(app.env, ENV_INTRA_PAGE_FRAGMENT_PAGES, intra_page_fragments)
    return list()


def html_page_context(
    app: Sphinx, pagename: str, templatename: str, context: Dict, doctree: Dict
) -> str:
    is_enabled: bool = getattr(app.env, ENV_REDIRECTS_ENABLED)
    if not is_enabled:
        return templatename
    context[CTX_HAS_FRAGMENT_REDIRECTS] = False
    intra_page_fragments: List[str] = getattr(app.env, ENV_INTRA_PAGE_FRAGMENT_PAGES)
    if pagename in intra_page_fragments:
        logger.info(
            "html_page_context(): page %s has intra-page redirects; adding redirects to HTML context" % pagename
        )
        computed_redirects: Dict[str, Dict[str, str]] = getattr(
            app.env, ENV_COMPUTED_REDIRECTS
        )
        context[CTX_FRAGMENT_REDIRECTS] = build_js_object(computed_redirects[pagename])
        context[CTX_HAS_FRAGMENT_REDIRECTS] = True
    return templatename


def html_collect_pages(app: Sphinx) -> List[Tuple[str, Dict[str, Any], str]]:
    """
    Collect the redirect page information and generate a list of redirect pages to write.

    :param app: The Sphinx Application instance
    :return: The list of redirect pages to create
    """
    is_enabled: bool = getattr(app.env, ENV_REDIRECTS_ENABLED)
    if not is_enabled:
        return list()
    redirect_pages: List[Tuple[str, Dict[str, Any], str]] = list()
    redirectmap: Dict[str, Dict[str, str]] = getattr(app.env, ENV_COMPUTED_REDIRECTS)
    for page in redirectmap.keys():
        # if page is a real page in the doctree, we've already handled it elsewhere
        if page in app.env.all_docs:
            logger.info("html_collect_pages(): page %s has intra-page redirects; skipping it" % page)
            continue
        # Handle the case where there is a single redirect defined for a source page
        if len(redirectmap[page]) == 1:
            # if this page only has a redirect to the DEFAULT_PAGE, then use a simple redirect template
            if DEFAULT_PAGE in redirectmap[page]:
                logger.info(
                    "html_collect_pages(): simple redirect from %s to %s"
                    % (page, redirectmap[page][DEFAULT_PAGE])
                )
                redirect_pages.append(
                    (
                        page,
                        {"to_uri": redirectmap[page][DEFAULT_PAGE]},
                        "simpleredirect.html",  # TODO: move this into a config variable
                    )
                )
                continue
            # there's only one fragment redirect, and it's not DEFAULT_PAGE. if someone browses to the page, they
            # will see a blank screen. we add a DEFAULT_PAGE redirect in that case.
            default_page_url = ""
            for frag in redirectmap[page].keys():
                default_page_url = redirectmap[page][frag]
                break
            if default_page_url != "":
                redirectmap[page][DEFAULT_PAGE] = default_page_url
                logger.debug(
                    "html_collect_pages(): added DEFAULT_PAGE redirect for " + page
                )
        # build a JS object that will hold the fragment redirect map
        jsobject = build_js_object(redirectmap[page])
        logger.info(
            "html_collect_pages(): redirect from %s; %s"
            % (page, jsobject)
        )
        redirect_pages.append(
            (
                page,
                {"redirects_object": jsobject},
                "redirect.html",  # TODO: move this into a config variable
            )
        )
    # return the iterable of pages to write
    return redirect_pages


def compute_redirects(app: Sphinx, redirects_option: Dict[str, str]) -> Dict[str, Dict[str, str]]:
    redirect_map: Dict[str, Dict[str, str]] = dict()
    # read parameters from config
    html_baseurl: str = getattr(app.config, CONFIG_HTML_BASEURL)
    html_baseurl = html_baseurl.removesuffix("/")
    mm_url_path_prefix: str = getattr(app.config, CONFIG_MM_URL_PATH_PREFIX)
    mm_url_path_prefix = mm_url_path_prefix.removesuffix("/")
    # process each record in the redirects dict
    for source in redirects_option.keys():
        # split the URL on # so we get the path and page name + the fragment, if any
        toks = source.split("#", 1)
        if len(toks) == 2:
            pagename = toks[0].removesuffix(".html")  # ensure pagename does not end with ".html"
            fragment = toks[1].removesuffix(".html")  # if the fragment ends in ".html", remove it
        elif len(toks) == 1:
            pagename = toks[0].removesuffix(".html")  # ensure pagename does not end with ".html"
            fragment = ""
        else:
            logger.warning("compute_redirects(): invalid redirect: %s" % source)
            continue
        # add a new dict to redirect_map if the page has not been seen before
        if pagename not in redirect_map:
            redirect_map[pagename] = dict()
        # if the target page has the same prefix as html_baseurl, remove the prefix so intra-site redirects work
        target = redirects_option[source].removeprefix(html_baseurl)
        # if mm_url_path_prefix is defined and the target path starts with '/', prepend it to the target path.
        if mm_url_path_prefix != "" and target.startswith("/"):
            target = mm_url_path_prefix + target
        # if there's no fragment then we're redirecting to the "default page", which is
        # the `pagename` without any fragment.
        if fragment == "":
            redirect_map[pagename][DEFAULT_PAGE] = target
            continue
        # redirect the fragment to the desired page
        redirect_map[pagename][fragment] = target
    return redirect_map


def build_js_object(pagemap: Dict[str, str]) -> str:
    jsobject = "const redirects = Object.freeze({"
    for frag in pagemap.keys():
        jsobject += '"' + frag + '":"' + pagemap[frag] + '",'
    jsobject = jsobject.rstrip(",")
    jsobject += "});"
    return jsobject


def old_status_iterator(
    mapping: Mapping[str, str], summary: str, color: str = "darkgreen"
) -> Tuple[str, str]:
    """
    Displays the status of iterating through a Dict/Mapping of strings. Taken from the Sphinx sources.

    :param mapping: The iterable to iterate through
    :param summary: A description of the action or operation
    :param color: The color of the status text; defaults to `darkgreen`
    :return: A tuple containing the next key-value pair from the iterable
    """
    line_count = 0
    for item in mapping.items():
        if line_count == 0:
            logger.info(bold(summary), nonl=True)
            line_count = 1
        logger.info(item[0], color=color, nonl=True)
        logger.info(" ", nonl=True)
        yield item
    if line_count == 1:
        logger.info("")


def status_iterator(
    mapping: Mapping[str, str],
    summary: str,
    color: str = "darkgreen",
    length: int = 0,
    verbosity: int = 0,
) -> Tuple[str, str]:
    """
    Displays the status of iterating through a Dict/Mapping of strings. Taken from the Sphinx sources.
    Status includes percent of records in the iterable that have been iterated through.

    :param mapping: The iterable to iterate through
    :param summary: A description of the action or operation
    :param color:  The color of the status text; defaults to `darkgreen`
    :param length: The number of records in the iterable
    :param verbosity: Flag which writes a newline after each status message
    :return: A tuple containing the next key-value pair from the iterable
    """
    if length == 0:
        yield from old_status_iterator(mapping, summary, color)
        return
    line_count = 0
    summary = bold(summary)
    for item in mapping.items():
        line_count += 1
        s = "%s[%3d%%] %s" % (
            summary,
            100 * line_count / length,
            colorize(color, item[0]),
        )
        if verbosity:
            s += "\n"
        else:
            s = term_width_line(s)
        logger.info(s, nonl=True)
        yield item
    if line_count > 0:
        logger.info("")


class Reredirects:
    def __init__(self, app: Sphinx):
        """
        Class constructor.
        Retrieves configuration values from the supplied Sphinx Application instance.

        :param app: The Sphinx Application instance
        """
        self.app = app
        self.redirects_option: Dict[str, str] = getattr(app.config, OPTION_REDIRECTS)
        self.template_file_option: str = getattr(app.config, OPTION_TEMPLATE_FILE)

    def grab_redirects(self) -> Mapping[str, str]:
        """
        Inspect redirects option in conf.py and returns dict mapping docname
        to target (with expanded placeholder).

        :return: A mapping of docname to target
        """
        # docname-target dict
        to_be_redirected = {}

        # For each source-target redirect pair in conf.py
        for source, target in self.redirects_option.items():
            # no wildcard, append source as-is
            if not self._contains_wildcard(source):
                to_be_redirected[source] = target
                continue

            # wildcarded source, expand to docnames
            expanded_docs = [
                doc for doc in self.app.env.found_docs if fnmatch(doc, source)
            ]

            if not expanded_docs:
                logger.warning(f"No documents match to '{source}' redirect.")
                continue

            for doc in expanded_docs:
                new_target = self._apply_placeholders(doc, target)
                to_be_redirected[doc] = new_target

        return to_be_redirected

    def create_redirects(self, to_be_redirected: Mapping[str, str]):
        """
        Create a redirect file for each pair in passed mapping of docnames to targets.

        :param to_be_redirected: A mapping of docnames to targets to create redirect files for
        """
        for doc, target in status_iterator(
            to_be_redirected,
            "writing redirects...",
            "darkgreen",
            len(to_be_redirected.items()),
        ):
            if not str(doc).endswith(".html"):
                doc += ".html"
            redirect_file_abs = Path(self.app.outdir).joinpath(doc)
            self._create_redirect_file(redirect_file_abs, target)

    @staticmethod
    def _contains_wildcard(text: str) -> bool:
        """
        Tells whether passed argument contains wildcard characters.

        :param text: The string to search for wildcard characters
        :return: True if wildcard characters were found; False otherwise
        """
        return bool(wildcard_pattern.search(text))

    @staticmethod
    def _apply_placeholders(source: str, target: str) -> str:
        """
        Expand `source` placeholder in target and return it

        :param source: The string value of the `source` parameter to render
        :param target: The template to render
        :return: The rendered template
        """
        return Template(target).substitute({"source": source})

    def _create_redirect_file(self, at_path: Path, to_uri: str):
        """
        Create a redirect file according to the redirect template

        :param at_path: The Path in which to write the redirect file
        :param to_uri: The value of the `to_uri` parameter to render in the redirect template
        """
        content = self._render_redirect_template(to_uri)
        # create any missing parent folders
        at_path.parent.mkdir(parents=True, exist_ok=True)
        at_path.write_text(content)

    def _render_redirect_template(self, to_uri: Any) -> str:
        """
        Render the redirect template by substituting the `to_uri` parameter

        :param to_uri: The value of the `to_uri` parameter to render
        :return: The rendered redirect template
        """
        # HTML used as redirect file content
        redirect_template = REDIRECT_FILE_DEFAULT_TEMPLATE
        if self.template_file_option:
            redirect_file_abs = Path(self.app.srcdir, self.template_file_option)
            redirect_template = redirect_file_abs.read_text()

        content = Template(redirect_template).substitute({"to_uri": to_uri})

        return content
