import re
from pathlib import Path

from source.conf import redirects

LINK_PATTERN = r"([^>`]?)`([^<`]*)<([^>@ ]+)>`_[_]?"


def process_match(match: re.Match) -> str:
    match_prefix: str = match.group(1)
    link_description: str = match.group(2)
    link_url: str = match.group(3)
    # skip the link if it's to an external location or to a different section of the page
    if (
        link_url == "/"
        or link_url.startswith("#")
        or link_url.startswith("../")
        or link_url.startswith("http")
        or link_url.startswith("/http")
        or link_url.startswith("mailto:")
        or link_url.endswith(".html/")
        or "?" in link_url
    ):
        # print(f"SKIP -> {match.group(0)}")
        return match.group(0)
    # if the link is the source of a page redirect, skip it
    if link_url.removeprefix("/").removesuffix("/") in redirects:
        # print(f"REDIRECT -> {match.group(0)}")
        return match.group(0)
    # print(f"match_prefix={match_prefix}, link_url={link_url}, link_description={link_description}")
    # if the link has a fragment, return a `ref` directive
    if "#" in link_url:
        toks = link_url.split("#", 1)
        url_part = toks[0].removeprefix("/").removesuffix("/").removesuffix(".html")
        fragment_part = toks[1].replace("-", " ")
        # print(f"{match_prefix}:ref:`{link_description}<{url_part}:{fragment_part}>`")
        return f"{match_prefix}:ref:`{link_description}<{url_part}:{fragment_part}>`"
    # return a `doc` directive
    link_url = link_url.removesuffix(".html")
    # print(f"{match_prefix}:doc:`{link_description}<{link_url}>`")
    return f"{match_prefix}:doc:`{link_description}<{link_url}>`"


if __name__ == "__main__":
    # grep command: grep -aEon '[^>`]?`[^<`]*<[^>@ ]+>`_[_]?' source/comply/electronic-discovery.rst
    # rst_file = Path("source/comply/electronic-discovery.rst")
    # subbed = re.sub(LINK_PATTERN, process_match, rst_file.read_text("utf-8"))
    # print(subbed)
    source_path = Path("source")
    rst_files = sorted(source_path.glob("**/*.rst"))
    print(f"Process {len(rst_files)} rST files")
    for rst_file in rst_files:
        # Skip any files in a /_static/ directory and skip any 'version-archive.rst' files
        if "/_static/" in str(rst_file) or rst_file.name == "version-archive.rst":
            print(f"-  {rst_file}")
            continue
        # Read the rST file
        raw_content = rst_file.read_text("utf-8")
        # If we read an orphan document, skip to the next file
        if raw_content.startswith(":orphan:"):
            print(f"#  {rst_file}")
            continue
        print(f"o  {rst_file}")
        # Process rST links in the file
        subbed_content = re.sub(LINK_PATTERN, process_match, raw_content)
        # Write the processed file back to disk
        rst_file.write_text(subbed_content, "utf-8")
    print("done.")
