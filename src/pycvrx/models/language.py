from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Language:
    """Language entry."""

    id: str = ""
    name: str = ""
    description: str = ""
    level: str = ""
    visible: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "level": self.level,
            "visible": self.visible,
        }
