from __future__ import annotations

from unittest.mock import Mock

from pycvrx.models.resume import Resume
from pycvrx.resources.resumes import ResumeResource


def test_create_resume():
    client = Mock()

    client.post.return_value = {
        "id": "123",
    }

    client.put.return_value = {
        "id": "123",
    }

    client.get.return_value = {
        "id": "123",
        "name": "Test Resume",
    }

    resource = ResumeResource(client)

    resume = Resume(
        name="Test Resume",
        slug="test-resume",
    )

    result = resource.create(resume)

    client.post.assert_called_once_with(
        "/resumes",
        json={
            "name": "Test Resume",
            "slug": "test-resume",
            "tags": [],
            "withSampleData": False,
        },
    )

    client.put.assert_called_once()

    assert result["id"] == "123"


def test_get_resume():
    client = Mock()

    client.get.return_value = {
        "id": "123",
        "name": "Test Resume",
    }

    resource = ResumeResource(client)

    result = resource.get("123")

    client.get.assert_called_once_with("/resumes/123")

    assert result["id"] == "123"


def test_list_resumes():
    client = Mock()

    client.get.return_value = [
        {
            "id": "123",
            "name": "Test Resume",
        }
    ]

    resource = ResumeResource(client)

    result = resource.list()

    client.get.assert_called_once_with("/resumes")

    assert len(result) == 1


def test_update_resume():
    client = Mock()

    client.put.return_value = {
        "id": "123",
    }

    resource = ResumeResource(client)

    resume = Resume(
        name="Updated Resume",
        slug="updated-resume",
    )

    result = resource.update(
        "123",
        resume,
    )

    client.put.assert_called_once()

    assert result["id"] == "123"


def test_delete_resume():
    client = Mock()

    client.delete.return_value = {}

    resource = ResumeResource(client)

    result = resource.delete("123")

    client.delete.assert_called_once_with("/resumes/123")

    assert result == {}


def test_create_resume_with_string_id_response():
    client = Mock()

    client.post.return_value = "123"

    client.put.return_value = {
        "id": "123",
    }

    resource = ResumeResource(client)

    resume = Resume(
        name="Test Resume",
        slug="test-resume",
    )

    result = resource.create(resume)

    client.post.assert_called_once_with(
        "/resumes",
        json={
            "name": "Test Resume",
            "slug": "test-resume",
            "tags": [],
            "withSampleData": False,
        },
    )

    client.put.assert_called_once()

    assert result["id"] == "123"