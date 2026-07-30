from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from pycvrx.client import Client


class ApplicationResource:
    """Job application API resource."""

    def __init__(self, client: Client):
        self._client = client

    def create(
        self,
        application: dict[str, Any],
    ) -> dict[str, Any]:
        """Create a job application."""

        return self._client.post(
            "/applications",
            json=application,
        )

    def get(
        self,
        application_id: str,
    ) -> dict[str, Any]:
        """Get a job application."""

        return self._client.get(
            f"/applications/{application_id}",
        )

    def list(self) -> list[dict[str, Any]]:
        """List job applications."""

        response = self._client.get("/applications")

        if isinstance(response, list):
            return cast(
                list[dict[str, Any]],
                response,
            )

        data = response.get("data")

        if isinstance(data, list):
            return cast(
                list[dict[str, Any]],
                data,
            )

        return []

    def update(
        self,
        application_id: str,
        application: dict[str, Any],
    ) -> dict[str, Any]:
        """Update a job application."""

        return self._client.put(
            f"/applications/{application_id}",
            json=application,
        )

    def delete(
        self,
        application_id: str,
    ) -> dict[str, Any]:
        """Delete a job application."""

        return self._client.delete(
            f"/applications/{application_id}",
        )
