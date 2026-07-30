from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pycvrx.models.location import Location
from pycvrx.models.profile import Profile


@dataclass(slots=True)
class Basics:
    """Personal information."""

    name: str = ""
    headline: str = ""
    email: str = ""
    phone: str = ""
    url: str = ""

    location: Location = field(
        default_factory=Location,
    )

    profiles: list[Profile] = field(
        default_factory=list,
    )

    custom_fields: list[dict[str, Any]] = field(
        default_factory=list,
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "headline": self.headline,
            "email": self.email,
            "phone": self.phone,
            "location": self.location.to_string(),
            "website": {
                "url": self.url,
                "label": "",
            },
            "customFields": self.custom_fields,
        }
