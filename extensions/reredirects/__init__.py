#
# reredirects - The sphinx_reredirects extension with parallel read and write support enabled
#
# Parallel read/write support by Alan Lew <alan@ethereal.cc> (https://github.com/neflyte/)
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
REDIRECT_FILE_DEFAULT_TEMPLATE = '<html><head><meta http-equiv="refresh" content="0; url=${to_uri}"></head></html>'  # noqa: E501

# Sphinx logger
logger = logging.getLogger(__name__)

wildcard_pattern = re.compile(r"[*?\[\]]")


def setup(app: Sphinx) -> Dict[str, Any]:
    """
    Sphinx extension setup function.
    It adds config values and connects Sphinx events to the sitemap builder.

    :param app: The Sphinx Application instance
    :return: A dict of Sphinx extension options
    """
    app.add_config_value(OPTION_REDIRECTS, OPTION_REDIRECTS_DEFAULT, "env")
    app.add_config_value(OPTION_TEMPLATE_FILE, OPTION_TEMPLATE_FILE_DEFAULT, "env")
    """
    Write the redirect pages when the `html-collect-pages` event fires.
    https://www.sphinx-doc.org/en/master/extdev/appapi.html#event-html-collect-pages
    """
    app.connect("html-collect-pages", write_redirect_pages)
    # Extra events to conform to Sphinx parallel read requirements. Both event functions do nothing.
    app.connect("env-purge-doc", env_purge_doc)
    app.connect("env-merge-info", env_merge_info)
    return {
        # Enable parallel reading and writing
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }


def write_redirect_pages(app: Sphinx) -> List[Tuple[str, Dict[str, Any], str]]:
    """
    Write the redirect page files.

    :param app: The Sphinx Application instance
    :return: An empty list
    """
    if not app.config[OPTION_REDIRECTS]:
        logger.debug('No redirects configured')
        return list()

    rr = Reredirects(app)
    to_be_redirected = rr.grab_redirects()
    rr.create_redirects(to_be_redirected)

    # html-collect-pages requires to return iterable of pages to write,
    # we have no additional pages to write
    return list()


def env_purge_doc(_: Sphinx, __: BuildEnvironment, ___: str):
    """
    Stub function for the `env-purge-doc` event; does nothing
    """
    return


def env_merge_info(_: Sphinx, __: BuildEnvironment, ___: List[str], ____: BuildEnvironment):
    """
    Stub function for the `env-merge-info` event; does nothing
    """
    return


def old_status_iterator(mapping: Mapping[str, str], summary: str, color: str = "darkgreen") -> Tuple[str, str]:
    line_count = 0
    for item in mapping.items():
        if line_count == 0:
            logger.info(bold(summary), nonl=True)
            line_count = 1
        logger.info(item[0], color=color, nonl=True)
        logger.info(" ", nonl=True)
        yield item
    if line_count == 1:
        logger.info('')


def status_iterator(mapping: Mapping[str, str], summary: str, color: str = "darkgreen",
                    length: int = 0, verbosity: int = 0) -> Tuple[str, str]:
    if length == 0:
        yield from old_status_iterator(mapping, summary, color)
        return
    line_count = 0
    summary = bold(summary)
    for item in mapping.items():
        line_count += 1
        s = '%s[%3d%%] %s' % (summary, 100 * line_count / length, colorize(color, item[0]))
        if verbosity:
            s += '\n'
        else:
            s = term_width_line(s)
        logger.info(s, nonl=True)
        yield item
    if line_count > 0:
        logger.info('')


class Reredirects:
    def __init__(self, app: Sphinx):
        self.app = app
        self.redirects_option: Dict[str,
                                    str] = getattr(app.config,
                                                   OPTION_REDIRECTS)
        self.template_file_option: str = getattr(app.config,
                                                 OPTION_TEMPLATE_FILE)

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
            expanded_docs = [doc for doc in self.app.env.found_docs
                             if fnmatch(doc, source)]

            if not expanded_docs:
                logger.warning(f"No documents match to '{source}' redirect.")
                continue

            for doc in expanded_docs:
                new_target = self._apply_placeholders(doc, target)
                to_be_redirected[doc] = new_target

        return to_be_redirected

    def create_redirects(self, to_be_redirected: Mapping[str, str]):
        """
        Create actual redirect file for each pair in passed mapping of
        docnames to targets.
        """
        for doc, target in status_iterator(to_be_redirected, 'writing redirects...', 'darkgreen',
                                           len(to_be_redirected.items())):
            redirect_file_abs = Path(self.app.outdir).joinpath(doc).with_suffix(".html")
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
        """Expand "source" placeholder in target and return it"""
        return Template(target).substitute({"source": source})

    def _create_redirect_file(self, at_path: Path, to_uri: str):
        """Actually create a redirect file according to redirect template"""

        content = self._render_redirect_template(to_uri)

        # create any missing parent folders
        at_path.parent.mkdir(parents=True, exist_ok=True)

        at_path.write_text(content)

    def _render_redirect_template(self, to_uri) -> str:
        # HTML used as redirect file content
        redirect_template = REDIRECT_FILE_DEFAULT_TEMPLATE
        if self.template_file_option:
            redirect_file_abs = Path(self.app.srcdir,
                                     self.template_file_option)
            redirect_template = redirect_file_abs.read_text()

        content = Template(redirect_template).substitute({"to_uri": to_uri})

        return content
