import re
from pathlib import Path

from source.conf import redirects

LINK_PATTERN = r"([^>`]?)`([^<`\n]*)<([^>@\n ]+)>`_[_]?"
IGNORE_DIRECTORIES = [
    "_static",
    "archive",
    "images",
    "recipes",
    "repeatable-processes",
    "samples",
    "scripts",
]


def resolve_redirect(filename: str) -> str:
    if filename in redirects:
        target = redirects[filename]
        if target.startswith("https://docs.mattermost.com/"):
            target = target.removeprefix("https://docs.mattermost.com/")
            return resolve_redirect(target)
    return filename


def process_match(match: re.Match) -> str:
    match_prefix: str = match.group(1)
    link_description: str = match.group(2)
    link_url: str = match.group(3)
    if link_url.startswith("https://docs.mattermost.com/"):  # and "|" not in link_url:
        link_url = link_url.removeprefix("https://docs.mattermost.com")
        # print(f"[hardcode] link_url ==> {link_url}")
    # skip the link if it's to an external location or to a different section of the page
    elif (
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
    # If the link is the source of a page redirect, recursively resolve the redirect
    # until an end page is reached; use that end page as the link_url
    link_url_stripped = link_url.removeprefix("/").removesuffix("/")
    if link_url_stripped in redirects:
        link_url_redirect = resolve_redirect(link_url_stripped)
        link_url = f"/{link_url_redirect}"
        # print(f"link_url -> {link_url}")
    # print(
    #     f"match_prefix={match_prefix}, link_url={link_url}, link_description={link_description}"
    # )
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


def should_ignore_file(filename: str) -> bool:
    for ignore_dir in IGNORE_DIRECTORIES:
        if filename.startswith(f"source/{ignore_dir}"):
            return True
    return False


if __name__ == "__main__":
    # grep command: grep -aEon '[^>`]?`[^<`]*<[^>@ ]+>`_[_]?' xxxxx.rst
    # rst_file = Path("source/onboard/shared-channels.rst")
    # raw_content = rst_file.read_text("utf-8")
    # re.sub(LINK_PATTERN, process_match, raw_content)
    source_path = Path("source")
    rst_files = sorted(source_path.glob("**/*.rst"))
    print(f"Process {len(rst_files)} rST files")
    for rst_file in rst_files:
        rst_file_name = str(rst_file)
        if (
            should_ignore_file(rst_file_name)
            or rst_file.name == "version-archive.rst"
            or "changelog" in rst_file.name
        ):
            print(f"-  {rst_file}")
            continue
        # Read the rST file
        print(f"o  {rst_file}")
        raw_content = rst_file.read_text("utf-8")
        # Process rST links in the file
        subbed_content = re.sub(LINK_PATTERN, process_match, raw_content)
        # Write the processed file back to disk
        rst_file.write_text(subbed_content, "utf-8")
    print("done.")
