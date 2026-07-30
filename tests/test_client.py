from __future__ import annotations

import httpx
import pytest

from pycvrx.client import Client
from pycvrx.config import Config
from pycvrx.exceptions import APIError


def test_client_initialization():
    client = Client(
        Config(
            api_key="test-key",
            base_url="https://example.com/api",
        )
    )

    assert client is not None

    client.close()


def test_client_context_manager():
    with Client(
        Config(
            api_key="test-key",
            base_url="https://example.com/api",
        )
    ) as client:
        assert client is not None


def test_get_request(monkeypatch):
    client = Client(
        Config(
            api_key="test-key",
            base_url="https://example.com/api",
        )
    )

    def mock_request(*args, **kwargs):
        return httpx.Response(
            200,
            json={"id": "123"},
        )

    monkeypatch.setattr(
        client._client,
        "request",
        mock_request,
    )

    response = client.get("/resumes")

    assert response == {"id": "123"}

    client.close()


def test_post_request(monkeypatch):
    client = Client(
        Config(
            api_key="test-key",
            base_url="https://example.com/api",
        )
    )

    def mock_request(*args, **kwargs):
        return httpx.Response(
            201,
            json={"id": "123"},
        )

    monkeypatch.setattr(
        client._client,
        "request",
        mock_request,
    )

    response = client.post(
        "/resumes",
        json={"name": "Test"},
    )

    assert response == {"id": "123"}

    client.close()


def test_put_request(monkeypatch):
    client = Client(
        Config(
            api_key="test-key",
            base_url="https://example.com/api",
        )
    )

    def mock_request(*args, **kwargs):
        return httpx.Response(
            200,
            json={"id": "123"},
        )

    monkeypatch.setattr(
        client._client,
        "request",
        mock_request,
    )

    response = client.put(
        "/resumes/123",
        json={"name": "Updated"},
    )

    assert response == {"id": "123"}

    client.close()


def test_api_error(monkeypatch):
    client = Client(
        Config(
            api_key="test-key",
            base_url="https://example.com/api",
        )
    )

    def mock_request(*args, **kwargs):
        return httpx.Response(
            404,
            text="Not Found",
        )

    monkeypatch.setattr(
        client._client,
        "request",
        mock_request,
    )

    with pytest.raises(APIError):
        client.get("/invalid")

    client.close()


def test_post_request_with_string_response(monkeypatch):
    client = Client(
        Config(
            api_key="test-key",
            base_url="https://example.com/api",
        )
    )

    def mock_request(*args, **kwargs):
        return httpx.Response(
            201,
            json="123",
        )

    monkeypatch.setattr(
        client._client,
        "request",
        mock_request,
    )

    response = client.post(
        "/resumes",
        json={"name": "Test"},
    )

    assert response == "123"

    client.close()
