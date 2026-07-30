from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Education:
    """Education entry."""

    id: str = ""
    institution: str = ""
    study_type: str = ""
    area: str = ""
    score: str = ""
    url: str = ""
    start_date: str = ""
    end_date: str = ""
    summary: str = ""
    visible: bool = True

    courses: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "institution": self.institution,
            "studyType": self.study_type,
            "area": self.area,
            "score": self.score,
            "url": self.url,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "summary": self.summary,
            "courses": self.courses,
            "visible": self.visible,
        }
