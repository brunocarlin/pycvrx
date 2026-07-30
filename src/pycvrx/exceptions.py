from __future__ import annotations


class PyCVRxError(Exception):
    """Base exception for pycvrx."""


class APIError(PyCVRxError):
    """Raised when the Reactive Resume API returns an error."""

    def __init__(
        self,
        status_code: int,
        message: str,
    ) -> None:
        self.status_code = status_code
        self.message = message
        super().__init__(f"{status_code}: {message}")


class ValidationError(PyCVRxError):
    """Raised when a resume fails schema validation."""
