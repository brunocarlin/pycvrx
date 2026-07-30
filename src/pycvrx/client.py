from __future__ import annotations

from typing import Any, cast

import httpx

from pycvrx.config import Config
from pycvrx.exceptions import APIError
from pycvrx.resources.applications import ApplicationResource
from pycvrx.resources.resumes import ResumeResource


class Client:
    """Reactive Resume API client."""

    def __init__(self, config: Config):
        self._config = config

        self._client = httpx.Client(
            base_url=config.base_url.rstrip("/"),
            headers={
                "x-api-key": config.api_key,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            timeout=config.timeout,
        )

        self.resumes = ResumeResource(self)
        self.applications = ApplicationResource(self)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def get(self, path: str) -> dict[str, Any]:
        return self._request("GET", path)

    def post(
        self,
        path: str,
        json: dict[str, Any],
    ) -> dict[str, Any]:
        return self._request(
            "POST",
            path,
            json=json,
        )

    def put(
        self,
        path: str,
        json: dict[str, Any],
    ) -> dict[str, Any]:
        return self._request(
            "PUT",
            path,
            json=json,
        )

    def patch(
        self,
        path: str,
        json: dict[str, Any],
    ) -> dict[str, Any]:
        return self._request(
            "PATCH",
            path,
            json=json,
        )

    def delete(self, path: str) -> dict[str, Any]:
        return self._request(
            "DELETE",
            path,
        )

    def _request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> dict[str, Any]:
        response = self._client.request(
            method,
            path,
            **kwargs,
        )

        if response.is_error:
            raise APIError(
                status_code=response.status_code,
                message=response.text,
            )

        if not response.content:
            return {}

        return cast(
            dict[str, Any],
            response.json(),
        )
