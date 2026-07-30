from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Metadata:
    """Reactive Resume metadata configuration."""

    layout: dict[str, Any] = field(
        default_factory=lambda: {
            "sidebarWidth": 35,
            "pages": [
                {
                    "fullWidth": False,
                    "main": [],
                    "sidebar": [],
                }
            ],
        }
    )

    page: dict[str, Any] = field(
        default_factory=lambda: {
            "gapX": 1,
            "gapY": 1,
            "marginX": 14,
            "marginY": 12,
            "format": "a4",
            "locale": "en-US",
            "hideLinkUnderline": False,
            "hideIcons": False,
            "hideSectionIcons": True,
        }
    )

    design: dict[str, Any] = field(
        default_factory=lambda: {
            "level": {
                "icon": "",
                "type": "progress-bar",
            },
            "colors": {
                "primary": "",
                "text": "",
                "background": "",
            },
        }
    )

    typography: dict[str, Any] = field(
        default_factory=lambda: {
            "body": {
                "fontFamily": "Inter",
            },
            "heading": {
                "fontFamily": "Inter",
            },
        }
    )

    notes: str = ""

    template: str = "onyx"

    style_rules: list[dict[str, Any]] = field(
        default_factory=list,
    )

    stylesheet: dict[str, Any] = field(
        default_factory=lambda: {
            "mode": "legacy",
            "source": {
                "languageVersion": 1,
                "text": "",
            },
            "applied": {
                "languageVersion": 1,
                "text": "",
            },
        }
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "template": self.template,
            "layout": self.layout,
            "page": self.page,
            "design": self.design,
            "typography": self.typography,
            "notes": self.notes,
            "styleRules": self.style_rules,
            "stylesheet": self.stylesheet,
        }
