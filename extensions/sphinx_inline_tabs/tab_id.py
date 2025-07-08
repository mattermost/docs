import re
from dataclasses import dataclass
from typing import Final, Optional
from sphinx.util.nodes import _make_id

TAB_ID_PATTERN: Final[str] = "itab--([a-zA-Z0-9-]+)--([0-9]+)_([0-9]+)-(.*)"


@dataclass(slots=True)
class TabId:
    """
    Represents a unique identifier for a tab with attributes describing its properties.

    This class provides functionality to encode and decode tab-related information, such as
    its name, level, count, and associated node identifier. It includes methods to generate
    representations and parse identifiers from a string format. The class is designed to
    facilitate structured handling of tab identifiers.

    :ivar tab_name: Name of the tab.
    :type tab_name: str
    :ivar level: Level of the tab in its hierarchy.
    :type level: int
    :ivar tab_count: Number of tabs.
    :type tab_count: int
    :ivar node_id: Unique identifier for the associated node.
    :type node_id: str
    """
    tab_name: str
    level: int
    tab_count: int
    node_id: str

    def __repr__(self):
        return f"itab--{_make_id(self.tab_name)}--{self.level}_{self.tab_count}-{self.node_id}"

    @classmethod
    def is_tab_id(cls, id_string: str) -> bool:
        return re.match(TAB_ID_PATTERN, id_string) is not None

    @classmethod
    def from_str(cls, id_string: str) -> Optional["TabId"]:
        match: Optional[re.Match[str]] = re.match(TAB_ID_PATTERN, id_string)
        if match is not None:
            return cls(
                tab_name=match.group(1),
                level=int(match.group(2)),
                tab_count=int(match.group(3)),
                node_id=match.group(4),
            )
        return None
