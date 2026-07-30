from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Award:
    """Award entry."""

    id: str = ""
    title: str = ""
    awarder: str = ""
    date: str = ""
    summary: str = ""
    url: str = ""
    visible: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "awarder": self.awarder,
            "date": self.date,
            "summary": self.summary,
            "url": self.url,
            "visible": self.visible,
        }
