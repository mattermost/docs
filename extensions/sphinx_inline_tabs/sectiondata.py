from dataclasses import dataclass


@dataclass(repr=True, slots=True)
class SectionData:
    """
    A dataclass to hold metadata on each section of inline tab content.
    """
    name: str
    level: int
    tab_counter: int
    is_doc_root: bool
    is_section_root: bool
    is_tab: bool
    id: str
    children: list["SectionData"]

    def get_section_type(self) -> str:
        section_type: str = "section"
        if self.is_doc_root:
            section_type = "doc root"
        elif self.is_section_root:
            section_type = "section root"
        elif self.is_tab:
            section_type = "tab"
        return section_type
