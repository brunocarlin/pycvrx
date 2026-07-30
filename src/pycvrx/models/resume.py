from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pycvrx.models.basics import Basics
from pycvrx.models.metadata import Metadata
from pycvrx.models.section import Section


def default_section(title: str) -> Section:
    return Section(
        title=title,
    )


@dataclass(slots=True)
class Resume:
    """Reactive Resume document."""

    name: str = ""
    slug: str = ""
    tags: list[str] = field(
        default_factory=list,
    )
    is_public: bool = False

    basics: Basics = field(
        default_factory=Basics,
    )

    summary: dict[str, Any] = field(
        default_factory=lambda: {
            "title": "Summary",
            "icon": "",
            "columns": 1,
            "hidden": False,
            "keepTogether": False,
            "startOnNewPage": False,
            "content": "",
        }
    )

    sections: dict[str, Section] = field(
        default_factory=lambda: {
            "profiles": default_section("Profiles"),
            "experience": default_section("Experience"),
            "education": default_section("Education"),
            "projects": default_section("Projects"),
            "skills": default_section("Skills"),
            "languages": default_section("Languages"),
            "interests": default_section("Interests"),
            "awards": default_section("Awards"),
            "certifications": default_section("Certifications"),
            "publications": default_section("Publications"),
            "volunteer": default_section("Volunteer"),
            "references": default_section("References"),
        }
    )

    custom_sections: list[dict[str, Any]] = field(
        default_factory=list,
    )

    metadata: Metadata = field(
        default_factory=Metadata,
    )

    picture: dict[str, Any] = field(
        default_factory=lambda: {
            "hidden": False,
            "url": "",
            "size": 128,
            "rotation": 0,
            "aspectRatio": 1,
            "borderRadius": 0,
            "borderColor": "",
            "borderWidth": 0,
            "shadowColor": "",
            "shadowWidth": 0,
        }
    )

    def to_dict(self) -> dict[str, Any]:
        """Convert resume data to Reactive Resume format."""

        return {
            "picture": self.picture,
            "basics": self.basics.to_dict(),
            "summary": self.summary,
            "sections": {
                name: section.to_dict() for name, section in self.sections.items()
            },
            "customSections": self.custom_sections,
            "metadata": self.metadata.to_dict(),
        }

    def to_api_payload(self) -> dict[str, Any]:
        """Convert resume to API create/update payload."""

        return {
            "name": self.name,
            "slug": self.slug,
            "tags": self.tags,
            "isPublic": self.is_public,
            "data": self.to_dict(),
        }
