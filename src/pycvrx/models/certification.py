from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Certification:
    """Certification entry."""

    id: str = ""
    name: str = ""
    issuer: str = ""
    url: str = ""
    date: str = ""
    summary: str = ""
    visible: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "issuer": self.issuer,
            "url": self.url,
            "date": self.date,
            "summary": self.summary,
            "visible": self.visible,
        }
