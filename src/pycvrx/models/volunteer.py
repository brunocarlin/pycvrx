from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Volunteer:
    """Volunteer experience entry."""

    id: str = ""
    organization: str = ""
    position: str = ""
    url: str = ""
    start_date: str = ""
    end_date: str = ""
    summary: str = ""
    visible: bool = True

    highlights: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "organization": self.organization,
            "position": self.position,
            "url": self.url,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "summary": self.summary,
            "highlights": self.highlights,
            "visible": self.visible,
        }
