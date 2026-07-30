from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Profile:
    """Social profile."""

    network: str = ""
    username: str = ""
    url: str = ""
    icon: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "network": self.network,
            "username": self.username,
            "url": self.url,
            "icon": self.icon,
        }
