from dataclasses import dataclass


@dataclass(slots=True)
class Config:
    """Configuration for the Reactive Resume API client."""

    base_url: str
    api_key: str
    timeout: float = 30.0
