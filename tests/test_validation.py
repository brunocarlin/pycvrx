from __future__ import annotations

from typing import Any

from pycvrx.models.resume import Resume
from pycvrx.validation import validate_resume


def test_validate_resume_model() -> None:
    resume = Resume(
        name="Test Resume",
        slug="test-resume",
    )

    validate_resume(resume)


def test_validate_resume_dict() -> None:
    resume: dict[str, Any] = {
        "picture": {
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
        },
        "basics": {
            "name": "Test",
            "headline": "",
            "email": "",
            "phone": "",
            "website": {
                "url": "",
                "label": "",
            },
            "location": "",
            "customFields": [],
        },
        "summary": {
            "title": "Summary",
            "icon": "",
            "columns": 1,
            "hidden": False,
            "keepTogether": False,
            "startOnNewPage": False,
            "content": "",
        },
        "sections": {
            key: {
                "title": key.title(),
                "icon": "",
                "columns": 1,
                "hidden": False,
                "keepTogether": False,
                "startOnNewPage": False,
                "items": [],
            }
            for key in [
                "profiles",
                "experience",
                "education",
                "projects",
                "skills",
                "languages",
                "interests",
                "awards",
                "certifications",
                "publications",
                "volunteer",
                "references",
            ]
        },
        "customSections": [],
        "metadata": {
            "template": "onyx",
            "layout": {
                "sidebarWidth": 35,
                "pages": [
                    {
                        "fullWidth": False,
                        "main": [],
                        "sidebar": [],
                    }
                ],
            },
            "page": {
                "gapX": 1,
                "gapY": 1,
                "marginX": 14,
                "marginY": 12,
                "format": "a4",
                "locale": "en-US",
                "hideLinkUnderline": False,
                "hideIcons": False,
                "hideSectionIcons": True,
            },
            "design": {
                "level": {
                    "icon": "",
                    "type": "progress-bar",
                },
                "colors": {
                    "primary": "",
                    "text": "",
                    "background": "",
                },
            },
            "typography": {
                "body": {
                    "fontFamily": "Inter",
                },
                "heading": {
                    "fontFamily": "Inter",
                },
            },
            "notes": "",
            "styleRules": [],
            "stylesheet": {
                "mode": "legacy",
                "source": {
                    "languageVersion": 1,
                    "text": "",
                },
                "applied": {
                    "languageVersion": 1,
                    "text": "",
                },
            },
        },
    }

    validate_resume(resume)


def test_validate_resume_with_full_data() -> None:
    resume = Resume(
        name="Bruno",
        slug="bruno-test",
    )

    validate_resume(resume)