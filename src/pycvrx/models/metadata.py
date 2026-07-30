from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Metadata:
    """Reactive Resume metadata configuration."""

    layout: dict[str, Any] = field(
        default_factory=lambda: {
            "sidebarWidth": 32,
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
            "locale": "pt-BR",
            "hideLinkUnderline": False,
            "hideIcons": False,
            "hideSectionIcons": True,
        }
    )

    design: dict[str, Any] = field(
        default_factory=lambda: {
            "level": {
                "icon": "",
                "type": "hidden",
            },
            "colors": {
                # LinkedIn inspired palette
                "primary": "#0A66C2",
                "text": "#1F2937",
                "background": "#FFFFFF",
            },
        }
    )

    typography: dict[str, Any] = field(
        default_factory=lambda: {
            "body": {
                "fontFamily": "Inter",
                "fontWeights": [
                    "400",
                    "500",
                ],
                "fontSize": 11,
                "lineHeight": 1.5,
            },
            "heading": {
                "fontFamily": "Inter",
                "fontWeights": [
                    "600",
                    "700",
                ],
                "fontSize": 13,
                "lineHeight": 1.3,
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
