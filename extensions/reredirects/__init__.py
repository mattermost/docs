#
# reredirects - A Sphinx extension that manages page redirects, including intra-page redirects.
#
# Based on sphinx_reredirects (https://gitlab.com/documatt/sphinx-reredirects)
#
from pathlib import Path
from shutil import copyfile
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util import logging
from sphinx.util.console import bold, colorize, term_width_line  # type: ignore
from typing import Mapping, Any, Optional

# Global Sphinx configuration options
CONFIG_HTML_BASEURL = "html_baseurl"
# Configuration options
CONFIG_OPTION_REDIRECTS = "redirects"
CONFIG_OPTION_TEMPLATE_FILE = "redirect_html_template_file"
CONFIG_MM_URL_PATH_PREFIX = "mm_url_path_prefix"
CONFIG_WRITE_EXTENSIONLESS_PAGES = "redirect_write_extensionless_pages"
# Option defaults
OPTION_REDIRECTS_DEFAULT: dict[str, str] = dict()
OPTION_TEMPLATE_FILE_DEFAULT = None
WRITE_EXTENSIONLESS_PAGES_DEFAULT = False
MM_URL_PATH_PREFIX_DEFAULT = ""
# Environment keys
ENV_REDIRECTS_ENABLED = "redirects-enabled"
ENV_COMPUTED_REDIRECTS = "computed-redirects"
ENV_INTRA_PAGE_FRAGMENT_PAGES = "intra-page-fragment-pages"
ENV_EXTENSIONLESS_PAGES = "extensionless-pages"
# HTML context keys
CTX_HAS_FRAGMENT_REDIRECTS = "has_fragment_redirects"
CTX_FRAGMENT_REDIRECTS = "fragment_redirects"
# Other constants...
DEFAULT_PAGE = "-"

# Sphinx logger
logger = logging.getLogger(__name__)


def setup(app: Sphinx) -> dict[str, Any]:
    """
    Sphinx extension setup function.

    :param app: The Sphinx Application instance
    :return: A dict of Sphinx extension options
    """
    app.add_config_value(CONFIG_OPTION_REDIRECTS, OPTION_REDIRECTS_DEFAULT, "env")
    app.add_config_value(
        CONFIG_OPTION_TEMPLATE_FILE, OPTION_TEMPLATE_FILE_DEFAULT, "env"
    )
    app.add_config_value(CONFIG_MM_URL_PATH_PREFIX, MM_URL_PATH_PREFIX_DEFAULT, "env")
    app.add_config_value(
        CONFIG_WRITE_EXTENSIONLESS_PAGES, WRITE_EXTENSIONLESS_PAGES_DEFAULT, "env"
    )
    app.connect("builder-inited", builder_inited)
    app.connect("env-updated", env_updated)
    app.connect("html-page-context", html_page_context)
    app.connect("html-collect-pages", html_collect_pages)
    app.connect("build-finished", build_finished)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def builder_inited(app: Sphinx):
    setattr(app.env, ENV_REDIRECTS_ENABLED, True)
    if not app.config[CONFIG_OPTION_REDIRECTS]:
        logger.warning(
            "No redirects configured; disabling redirects extension for this build"
        )
        setattr(app.env, ENV_REDIRECTS_ENABLED, False)
        return
    if len(app.config[CONFIG_OPTION_REDIRECTS]) == 0:
        logger.warning(
            "Empty redirect definition; disabling redirects extension for this build"
        )
        setattr(app.env, ENV_REDIRECTS_ENABLED, False)
        return
    redirects_option: dict[str, str] = getattr(app.config, CONFIG_OPTION_REDIRECTS)
    setattr(app.env, ENV_COMPUTED_REDIRECTS, compute_redirects(app, redirects_option))


def env_updated(app: Sphinx, env: BuildEnvironment) -> list[str]:
    is_enabled: bool = getattr(app.env, ENV_REDIRECTS_ENABLED)
    if is_enabled:
        computed_redirects: dict[str, dict[str, str]] = getattr(
            env, ENV_COMPUTED_REDIRECTS
        )
        intra_page_fragments: list[str] = list()
        for page in computed_redirects.keys():
            if page in env.all_docs:
                intra_page_fragments.append(page)
        logger.verbose(
            "env_updated(): found %d intra-page fragment pages"
            % len(intra_page_fragments)
        )
        setattr(app.env, ENV_INTRA_PAGE_FRAGMENT_PAGES, intra_page_fragments)
    return list()


def html_page_context(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: dict,
) -> str:
    logger.verbose(
        f"html_page_context(): pagename={pagename}, templatename={templatename}"
    )
    is_enabled: bool = getattr(app.env, ENV_REDIRECTS_ENABLED)
    if is_enabled:
        context[CTX_HAS_FRAGMENT_REDIRECTS] = False
        intra_page_fragments: list[str] = getattr(
            app.env, ENV_INTRA_PAGE_FRAGMENT_PAGES
        )
        if (
            intra_page_fragments
            and len(intra_page_fragments) > 0
            and pagename in intra_page_fragments
        ):
            logger.verbose(
                f"html_page_context(): page {pagename} has intra-page redirects; adding redirects to HTML context"
            )
            computed_redirects: dict[str, dict[str, str]] = getattr(
                app.env, ENV_COMPUTED_REDIRECTS
            )
            context[CTX_FRAGMENT_REDIRECTS] = build_js_object(
                computed_redirects[pagename]
            )
            context[CTX_HAS_FRAGMENT_REDIRECTS] = True
    return templatename


def toctree_returns_none(
    collapse: bool, titles_only: bool, maxdepth: int, includehidden: bool
) -> Optional[str]:
    """
    A "stub" function that returns None.
    This function exists to short-cut the html-page-context event in the `furo` theme, so it
    doesn't deepcopy the real toctree for templates that are not based on a real doc.

    :param collapse: Unused.
    :param titles_only: Unused.
    :param maxdepth: Unused.
    :param includehidden: Unused.
    :return: None.
    """
    return None


def html_collect_pages(app: Sphinx) -> list[tuple[str, dict[str, Any], str]]:
    """
    Collect the redirect page information and generate a list of redirect pages to write.

    :param app: The Sphinx Application instance
    :return: The list of redirect pages to create
    """
    is_enabled: bool = getattr(app.env, ENV_REDIRECTS_ENABLED)
    if not is_enabled:
        return list()
    redirect_pages: list[tuple[str, dict[str, Any], str]] = list()
    extensionless_pages: list[str] = list()
    write_extensionless_pages: bool = getattr(
        app.config, CONFIG_WRITE_EXTENSIONLESS_PAGES
    )
    computed_redirects: dict[str, dict[str, str]] = getattr(
        app.env, ENV_COMPUTED_REDIRECTS
    )
    for page in computed_redirects.keys():
        # if page is a real page in the doctree, we've already handled it elsewhere
        if page in app.env.all_docs:
            logger.verbose(
                f"html_collect_pages(): page {page} has intra-page redirects; skipping it"
            )
            continue
        # Handle the case where there is a single redirect defined for a source page
        if len(computed_redirects[page]) == 1:
            # if this page only has a redirect to the DEFAULT_PAGE, then use a simple redirect template
            if DEFAULT_PAGE in computed_redirects[page]:
                logger.verbose(
                    f"html_collect_pages(): simple redirect from {page} to {computed_redirects[page][DEFAULT_PAGE]}"
                )
                redirect_pages.append(
                    (
                        page,
                        {
                            "to_uri": computed_redirects[page][DEFAULT_PAGE],
                            "toctree": toctree_returns_none,  # short-cut for the `furo` theme
                        },
                        "simpleredirect.html",  # TODO: move this into a config variable
                    )
                )
                if write_extensionless_pages:
                    extensionless_pages.append(page)
                continue
            # there's only one fragment redirect, and it's not DEFAULT_PAGE. if someone browses to the page, they
            # will see a blank screen. we add a DEFAULT_PAGE redirect in that case.
            default_page_url = ""
            for frag in computed_redirects[page].keys():
                default_page_url = computed_redirects[page][frag]
                break
            if default_page_url != "":
                computed_redirects[page][DEFAULT_PAGE] = default_page_url
                logger.debug(
                    f"html_collect_pages(): added DEFAULT_PAGE redirect for {page}"
                )
        # build a JS object that will hold the fragment redirect map
        jsobject = build_js_object(computed_redirects[page])
        logger.verbose(f"html_collect_pages(): redirect from {page}; {jsobject}")
        redirect_pages.append(
            (
                page,
                {
                    CTX_FRAGMENT_REDIRECTS: jsobject,
                    "toctree": toctree_returns_none,  # short-cut for the `furo` theme
                },
                "redirect.html",  # TODO: move this into a config variable
            )
        )
        if write_extensionless_pages:
            extensionless_pages.append(page)
    # if we're configured to write extensionless pages, save the list of pages to the environment for later processing
    if write_extensionless_pages:
        setattr(app.env, ENV_EXTENSIONLESS_PAGES, extensionless_pages)
    # return the iterable of pages to write
    return redirect_pages


def build_finished(app: Sphinx, exception: Exception):
    if exception is None:
        write_extensionless_pages: bool = getattr(
            app.config, CONFIG_WRITE_EXTENSIONLESS_PAGES
        )
        if write_extensionless_pages:
            extensionless_pages: list[str] = getattr(app.env, ENV_EXTENSIONLESS_PAGES)
            for pagename in list_status_iterator(
                extensionless_pages,
                "writing extensionless redirect pages... ",
                "darkgreen",
                len(extensionless_pages),
            ):
                target_file = Path(app.outdir).joinpath(pagename)
                if target_file.is_dir():
                    logger.warning(
                        "target extensionless redirect '%s' is a directory; cannot write this page"
                        % target_file
                    )
                    continue
                source_file = str(target_file) + ".html"
                logger.verbose(
                    "build_finished(): extensionless redirect; %s -> %s"
                    % (source_file, target_file)
                )
                copyfile(source_file, target_file)


def compute_redirects(
    app: Sphinx, redirects_option: dict[str, str]
) -> dict[str, dict[str, str]]:
    computed_redirects: dict[str, dict[str, str]] = dict()
    # read parameters from config
    html_baseurl: str = getattr(app.config, CONFIG_HTML_BASEURL)
    html_baseurl = html_baseurl.removesuffix("/")
    mm_url_path_prefix: str = getattr(app.config, CONFIG_MM_URL_PATH_PREFIX)
    mm_url_path_prefix = mm_url_path_prefix.removesuffix("/")
    # process each record in the redirects dict
    for source in redirects_option.keys():
        # split the URL on # so we get the path and page name + the fragment, if any
        tokens = source.split("#")
        if len(tokens) == 2:
            pagename = tokens[0].removesuffix(
                ".html"
            )  # ensure pagename does not end with ".html"
            fragment = tokens[1].removesuffix(
                ".html"
            )  # if the fragment ends in ".html", remove it
        elif len(tokens) == 1:
            pagename = tokens[0].removesuffix(
                ".html"
            )  # ensure pagename does not end with ".html"
            fragment = ""
        else:
            logger.warning("compute_redirects(): invalid redirect: %s" % source)
            continue
        # if the source page is the empty string then the redirect is invalid. warn the user and continue on.
        if pagename == "":
            logger.warning("compute_redirects(): empty page name: %s" % source)
            continue
        # add a new dict to redirect_map if the page has not been seen before
        if pagename not in computed_redirects:
            computed_redirects[pagename] = dict()
        # if the target page has the same prefix as html_baseurl, remove the prefix so intra-site redirects work
        target = redirects_option[source].removeprefix(html_baseurl)
        # if the target is the empty string then the redirect is invalid. warn the user and continue on
        if target == "":
            logger.warning("compute_redirects(): empty target for source %s" % source)
            continue
        # if mm_url_path_prefix is defined and the target path starts with '/', prepend it to the target path.
        if mm_url_path_prefix != "" and target.startswith("/"):
            target = mm_url_path_prefix + target
        # if there's no fragment then we're redirecting to the "default page", which is
        # the `pagename` without any fragment.
        if fragment == "":
            computed_redirects[pagename][DEFAULT_PAGE] = target
            continue
        # redirect the fragment to the desired page
        computed_redirects[pagename][fragment] = target
    # remove empty keys from the map
    empty_keys: list[str] = list()
    for key in computed_redirects.keys():
        if len(computed_redirects[key]) == 0:
            empty_keys.append(key)
    for key in empty_keys:
        computed_redirects.pop(key)
    return computed_redirects


def build_js_object(pagemap: dict[str, str]) -> str:
    jsobject = f"const {CTX_FRAGMENT_REDIRECTS} = Object.freeze(" + "{"
    for frag in pagemap.keys():
        jsobject += f'"{frag}":"{pagemap[frag]}",'
    return jsobject.rstrip(",") + "});"


def old_status_iterator(
    mapping: Mapping[str, str], summary: str, color: str = "darkgreen"
) -> tuple[str, str]:
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
) -> tuple[str, str]:
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


def old_list_status_iterator(
    mapping: list[str], summary: str, color: str = "darkgreen"
) -> str:
    """
    Displays the status of iterating through a List of strings. Adapted from the Sphinx sources.

    :param mapping: The List to iterate through
    :param summary: A description of the action or operation
    :param color: The color of the status text; defaults to `darkgreen`
    :return: A tuple containing the next value from the List
    """
    line_count = 0
    for item in mapping:
        if line_count == 0:
            logger.info(bold(summary), nonl=True)
            line_count = 1
        logger.info(item, color=color, nonl=True)
        logger.info(" ", nonl=True)
        yield item
    if line_count == 1:
        logger.info("")


def list_status_iterator(
    mapping: list[str],
    summary: str,
    color: str = "darkgreen",
    length: int = 0,
    verbosity: int = 0,
) -> str:
    """
    Displays the status of iterating through a List of strings. Adapted from the Sphinx sources.
    Status includes percent of records in the List that have been iterated through.

    :param mapping: The List to iterate through
    :param summary: A description of the action or operation
    :param color:  The color of the status text; defaults to `darkgreen`
    :param length: The number of records in the List
    :param verbosity: Flag which writes a newline after each status message
    :return: A tuple containing the next value from the List
    """
    if length == 0:
        yield from old_list_status_iterator(mapping, summary, color)
        return
    line_count = 0
    summary = bold(summary)
    for item in mapping:
        line_count += 1
        s = "%s[%3d%%] %s" % (
            summary,
            100 * line_count / length,
            colorize(color, item),
        )
        if verbosity:
            s += "\n"
        else:
            s = term_width_line(s)
        logger.info(s, nonl=True)
        yield item
    if line_count > 0:
        logger.info("")
