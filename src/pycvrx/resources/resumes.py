from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pycvrx.models.resume import Resume
from pycvrx.validation import validate_resume

if TYPE_CHECKING:
    from pycvrx.client import Client


class ResumeResource:
    """Resume API resource."""

    def __init__(self, client: Client):
        self._client = client

    def create(
        self,
        resume: Resume,
    ) -> dict[str, Any]:
        """
        Create a resume.

        Reactive Resume creates a resume in two steps:
        1. Create metadata
        2. Upload resume data
        """

        validate_resume(resume)

        created = self._client.post(
            "/resumes",
            json={
                "name": resume.name,
                "slug": resume.slug,
                "tags": resume.tags,
                "withSampleData": False,
            },
        )

        # API may return:
        # - {"id": "..."}
        # - "resume-id"
        # - other response formats
        if isinstance(created, str):
            resume_id = created
        elif isinstance(created, dict):
            resume_id = created.get("id")
        else:
            return {
                "response": created,
            }

        if resume_id is None:
            if isinstance(created, dict):
                return created

            return {
                "response": created,
            }

        return self.update(
            resume_id,
            resume,
        )

    def get(
        self,
        resume_id: str,
    ) -> dict[str, Any]:
        """Get a resume by ID."""

        return self._client.get(
            f"/resumes/{resume_id}",
        )

    def list(self) -> list[dict[str, Any]]:
        """List resumes."""

        response = self._client.get(
            "/resumes",
        )

        if isinstance(response, list):
            return response

        if isinstance(response, dict):
            data = response.get("data")

            if isinstance(data, list):
                return data

        return []

    def update(
        self,
        resume_id: str,
        resume: Resume,
    ) -> dict[str, Any]:
        """Update resume content."""

        validate_resume(resume)

        return self._client.put(
            f"/resumes/{resume_id}",
            json=resume.to_api_payload(),
        )

    def delete(
        self,
        resume_id: str,
    ) -> dict[str, Any]:
        """Delete a resume."""

        return self._client.delete(
            f"/resumes/{resume_id}",
        )
