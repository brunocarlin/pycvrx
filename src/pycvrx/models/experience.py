from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Experience:
    """Work experience entry."""

    id: str = ""
    company: str = ""
    position: str = ""
    location: str = ""
    url: str = ""
    start_date: str = ""
    end_date: str = ""
    summary: str = ""
    visible: bool = True

    highlights: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "company": self.company,
            "position": self.position,
            "location": self.location,
            "url": self.url,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "summary": self.summary,
            "highlights": self.highlights,
            "visible": self.visible,
        }
