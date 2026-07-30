from __future__ import annotations

from typing import Any

from pydantic import Field

from pycvrx.models.common import CVRXBaseModel


class APIResponse(CVRXBaseModel):
    success: bool = True
    message: str = ""
    data: dict[str, Any] = Field(default_factory=dict)


class APIListResponse(CVRXBaseModel):
    success: bool = True
    message: str = ""
    data: list[dict[str, Any]] = Field(default_factory=list)
