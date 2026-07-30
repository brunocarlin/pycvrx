from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Location:
    """Resume location."""

    address: str = ""
    postal_code: str = ""
    city: str = ""
    region: str = ""
    country: str = ""

    def to_string(self) -> str:
        parts = [
            self.city,
            self.region,
            self.country,
        ]

        return ", ".join(part for part in parts if part)

    def to_dict(self) -> dict[str, str]:
        return {
            "address": self.address,
            "postalCode": self.postal_code,
            "city": self.city,
            "region": self.region,
            "country": self.country,
        }
