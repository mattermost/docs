import re
from pathlib import Path

LINK_PATTERN = r"([^>]?)`([^<]*) <([^>]*)>`__"


def process_match(match: re.Match) -> str:
    match_prefix: str = match.group(1)
    link_description: str = match.group(2)
    link_url: str = match.group(3)
    # skip the link if it's to an external location
    if link_url.startswith("http"):
        return match.group(0)
    # if the link has a fragment, return a `ref` directive
    if "#" in link_url:
        toks = link_url.split("#", 1)
        url_part = toks[0].removeprefix("/").removesuffix(".html")
        fragment_part = toks[1].replace("-", " ")
        return f"{match_prefix}:ref:`{link_description} <{url_part}:{fragment_part}>`"
    # return a `doc` directive
    link_url = link_url.removesuffix(".html")
    return f"{match_prefix}:doc:`{link_description} <{link_url}>`"


# grep command: grep -aEon '[^>]?`[^<]* <[^>]*>`__' xxxxx.rst
# rst_file = Path("source/getting-started/admin-onboarding-tasks.rst")
# print(
#     re.sub(
#         LINK_PATTERN,
#         process_match,
#         rst_file.read_text("utf-8")
#     )
# )

source_path = Path("source")
rst_files = sorted(source_path.glob("**/*.rst"))
print(f"Process {len(rst_files)} rST files")
for rst_file in rst_files:
    if "/_static/" in str(rst_file):
        print(f"-  {rst_file}")
        continue
    print(f"o  {rst_file}")
    subbed_content = re.sub(LINK_PATTERN, process_match, rst_file.read_text("utf-8"))
    rst_file.write_text(subbed_content, "utf-8")
print("done.")
