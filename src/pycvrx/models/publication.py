from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Publication:
    """Publication entry."""

    id: str = ""
    name: str = ""
    publisher: str = ""
    url: str = ""
    date: str = ""
    summary: str = ""
    visible: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "publisher": self.publisher,
            "url": self.url,
            "date": self.date,
            "summary": self.summary,
            "visible": self.visible,
        }
