from __future__ import annotations

import pytest

from pycvrx.config import Config


def test_config_defaults():
    config = Config(
        api_key="test-key",
        base_url="https://rxresu.me/api/openapi",
    )

    assert config.api_key == "test-key"
    assert config.base_url == "https://rxresu.me/api/openapi"
    assert config.timeout == 30


def test_config_custom_timeout():
    config = Config(
        api_key="test-key",
        base_url="https://rxresu.me/api/openapi",
        timeout=60,
    )

    assert config.timeout == 60


def test_config_requires_api_key():
    with pytest.raises(Exception):
        Config(
            api_key="",
            base_url="https://rxresu.me/api/openapi",
        )
