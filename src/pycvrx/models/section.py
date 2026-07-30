from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Section:
    """Reactive Resume section configuration."""

    title: str = ""
    icon: str = ""
    columns: int = 1
    hidden: bool = False
    keep_together: bool = False
    start_on_new_page: bool = False
    items: list[dict[str, Any]] = field(
        default_factory=list,
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "icon": self.icon,
            "columns": self.columns,
            "hidden": self.hidden,
            "keepTogether": self.keep_together,
            "startOnNewPage": self.start_on_new_page,
            "items": self.items,
        }
