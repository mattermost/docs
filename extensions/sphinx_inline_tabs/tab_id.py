import re
from dataclasses import dataclass
from typing import Final, Optional
from sphinx.util import logging
from sphinx.util.nodes import _make_id

TAB_ID_PATTERN: Final[str] = "itab--([a-zA-Z0-9-.:,'() ]+)--([0-9]+)_([0-9]+)-(.*)"
"""Regex pattern for validating tab identifiers."""

logger: logging.SphinxLoggerAdapter = logging.getLogger(__name__)
LOG_PREFIX: Final[str] = "[sphinx_inline_tabs]"


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
        """
        Check if the given string is a valid tab identifier.

        :param id_string: The string to check.
        :return: True if the string is a valid tab identifier, False otherwise.
        """
        return re.match(TAB_ID_PATTERN, id_string) is not None

    @classmethod
    def from_str(cls, id_string: str) -> Optional["TabId"]:
        """
        Create a TabId instance from a string representation.

        :param id_string: The string representation of the tab identifier.
        :return: A TabId instance if the string is valid, None otherwise.
        """
        match: Optional[re.Match[str]] = re.match(TAB_ID_PATTERN, id_string)
        if match is not None:
            return cls(
                tab_name=match.group(1),
                level=int(match.group(2)),
                tab_count=int(match.group(3)),
                node_id=match.group(4),
            )
        return None

    def ensure_unique(self, existing_ids: Optional[set[str]]) -> None:
        """
        Ensure that the tab identifier is unique within the given set of existing IDs.

        :param existing_ids: The set of existing tab IDs to check against.
        :raises ValueError: If existing_ids is None.
        """
        if existing_ids is None:
            raise ValueError("existing_ids cannot be None")
        if str(self) not in existing_ids:
            return
        logger.debug(f"{LOG_PREFIX} TabId.ensure_unique: {str(self)} is already in the set")
        is_unique: bool = False
        ctr: int = 1
        original_node_id: str = self.node_id
        while not is_unique:
            self.node_id = f"{original_node_id}_{ctr}"
            if str(self) not in existing_ids:
                logger.debug(f"{LOG_PREFIX} TabId.ensure_unique: {str(self)} is unique after appending {ctr}")
                is_unique = True
            ctr += 1
