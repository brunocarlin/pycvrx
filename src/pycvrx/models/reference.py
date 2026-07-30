from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Reference:
    """Professional reference."""

    id: str = ""
    name: str = ""
    relationship: str = ""
    company: str = ""
    email: str = ""
    phone: str = ""
    summary: str = ""
    visible: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "relationship": self.relationship,
            "company": self.company,
            "email": self.email,
            "phone": self.phone,
            "summary": self.summary,
            "visible": self.visible,
        }
