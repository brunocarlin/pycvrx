from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


def default_section() -> dict[str, Any]:
    return {
        "icon": "",
        "columns": 1,
        "keepTogether": False,
        "startOnNewPage": False,
    }


@dataclass(slots=True)
class Sections:
    """Reactive Resume section layout configuration."""

    profiles: dict[str, Any] = field(
        default_factory=default_section,
    )

    experience: dict[str, Any] = field(
        default_factory=default_section,
    )

    education: dict[str, Any] = field(
        default_factory=default_section,
    )

    projects: dict[str, Any] = field(
        default_factory=default_section,
    )

    skills: dict[str, Any] = field(
        default_factory=default_section,
    )

    languages: dict[str, Any] = field(
        default_factory=default_section,
    )

    interests: dict[str, Any] = field(
        default_factory=default_section,
    )

    awards: dict[str, Any] = field(
        default_factory=default_section,
    )

    certifications: dict[str, Any] = field(
        default_factory=default_section,
    )

    publications: dict[str, Any] = field(
        default_factory=default_section,
    )

    volunteer: dict[str, Any] = field(
        default_factory=default_section,
    )

    references: dict[str, Any] = field(
        default_factory=default_section,
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "profiles": self.profiles,
            "experience": self.experience,
            "education": self.education,
            "projects": self.projects,
            "skills": self.skills,
            "languages": self.languages,
            "interests": self.interests,
            "awards": self.awards,
            "certifications": self.certifications,
            "publications": self.publications,
            "volunteer": self.volunteer,
            "references": self.references,
        }
