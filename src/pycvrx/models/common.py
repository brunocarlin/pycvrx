from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class CVRXBaseModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        extra="ignore",
    )


class Picture(CVRXBaseModel):
    url: str = ""
    visible: bool = True


class Summary(CVRXBaseModel):
    content: str = ""
    visible: bool = True


class Section(CVRXBaseModel):
    name: str = ""
    columns: int = 1
    visible: bool = True
    separateLinks: bool = True


class CustomSection(CVRXBaseModel):
    id: str = ""
    name: str = ""
    columns: int = 1
    visible: bool = True
    items: list[Any] = Field(default_factory=list)
