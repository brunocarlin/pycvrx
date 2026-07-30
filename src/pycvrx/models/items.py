from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ResumeItem:
    """Base item used by resume sections."""

    id: str = ""
    hidden: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "hidden": self.hidden,
        }


@dataclass(slots=True)
class ExperienceItem(ResumeItem):
    """Work experience item."""

    company: str = ""
    position: str = ""
    location: str = ""
    period: str = ""
    description: str = ""

    website: dict[str, Any] = field(
        default_factory=lambda: {
            "url": "",
            "label": "",
            "inlineLink": False,
        }
    )

    roles: list[dict[str, Any]] = field(
        default_factory=list,
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "company": self.company,
            "position": self.position,
            "location": self.location,
            "period": self.period,
            "description": self.description,
            "website": self.website,
            "roles": self.roles,
        }


@dataclass(slots=True)
class EducationItem(ResumeItem):
    """Education item."""

    school: str = ""
    degree: str = ""
    area: str = ""
    grade: str = ""
    location: str = ""
    period: str = ""
    description: str = ""

    website: dict[str, Any] = field(
        default_factory=lambda: {
            "url": "",
            "label": "",
            "inlineLink": False,
        }
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "school": self.school,
            "degree": self.degree,
            "area": self.area,
            "grade": self.grade,
            "location": self.location,
            "period": self.period,
            "website": self.website,
            "description": self.description,
        }


@dataclass(slots=True)
class ProjectItem(ResumeItem):
    """Project item."""

    name: str = ""
    description: str = ""
    period: str = ""
    location: str = ""

    website: dict[str, Any] = field(
        default_factory=lambda: {
            "url": "",
            "label": "",
            "inlineLink": False,
        }
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self.name,
            "description": self.description,
            "period": self.period,
            "location": self.location,
            "website": self.website,
        }


@dataclass(slots=True)
class SkillItem(ResumeItem):
    """Skill item."""

    icon: str = ""
    icon_color: str = ""
    name: str = ""
    proficiency: str = ""
    level: float = 0
    keywords: list[str] = field(
        default_factory=list,
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "icon": self.icon,
            "iconColor": self.icon_color,
            "name": self.name,
            "proficiency": self.proficiency,
            "level": self.level,
            "keywords": self.keywords,
        }


@dataclass(slots=True)
class LanguageItem(ResumeItem):
    """Language item."""

    language: str = ""
    fluency: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "language": self.language,
            "fluency": self.fluency,
        }


@dataclass(slots=True)
class ProfileItem(ResumeItem):
    """Profile/social link item."""

    network: str = ""
    username: str = ""
    website: dict[str, Any] = field(
        default_factory=lambda: {
            "url": "",
            "label": "",
            "inlineLink": False,
        }
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "network": self.network,
            "username": self.username,
            "website": self.website,
        }


@dataclass(slots=True)
class CertificationItem(ResumeItem):
    """Certification item."""

    name: str = ""
    issuer: str = ""
    date: str = ""
    description: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "name": self.name,
            "issuer": self.issuer,
            "date": self.date,
            "description": self.description,
        }


@dataclass(slots=True)
class AwardItem(ResumeItem):
    """Award item."""

    title: str = ""
    issuer: str = ""
    date: str = ""
    description: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "title": self.title,
            "issuer": self.issuer,
            "date": self.date,
            "description": self.description,
        }
