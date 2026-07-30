from __future__ import annotations

from unittest.mock import Mock

from pycvrx.resources.applications import ApplicationResource


def test_create_application():
    client = Mock()

    client.post.return_value = {
        "id": "123",
        "company": "Google",
        "role": "Data Scientist",
    }

    resource = ApplicationResource(client)

    application = {
        "company": "Google",
        "role": "Data Scientist",
        "location": "United States",
        "salary": "",
        "source": "LinkedIn",
        "sourceUrl": "",
        "jobDescription": "Data Science role",
        "notes": "Applied through careers page",
        "resumeFileUrl": "",
        "resumeFileName": "",
        "coverLetterUrl": "",
        "coverLetterName": "",
        "followUpAt": None,
        "followUpNote": "",
        "contacts": [],
        "resumeId": "resume-123",
        "tags": [
            "data-science",
        ],
        "stageEnteredAt": None,
    }

    result = resource.create(application)

    client.post.assert_called_once_with(
        "/applications",
        json=application,
    )

    assert result["id"] == "123"


def test_get_application():
    client = Mock()

    client.get.return_value = {
        "id": "123",
    }

    resource = ApplicationResource(client)

    result = resource.get("123")

    client.get.assert_called_once_with(
        "/applications/123",
    )

    assert result["id"] == "123"


def test_list_applications():
    client = Mock()

    client.get.return_value = [
        {
            "id": "123",
        }
    ]

    resource = ApplicationResource(client)

    result = resource.list()

    client.get.assert_called_once_with(
        "/applications",
    )

    assert len(result) == 1


def test_update_application():
    client = Mock()

    client.put.return_value = {
        "id": "123",
    }

    resource = ApplicationResource(client)

    result = resource.update(
        "123",
        {
            "notes": "Updated",
        },
    )

    client.put.assert_called_once_with(
        "/applications/123",
        json={
            "notes": "Updated",
        },
    )

    assert result["id"] == "123"


def test_delete_application():
    client = Mock()

    client.delete.return_value = {}

    resource = ApplicationResource(client)

    result = resource.delete("123")

    client.delete.assert_called_once_with(
        "/applications/123",
    )

    assert result == {}
