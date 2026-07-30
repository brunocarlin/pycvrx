from __future__ import annotations

import json
from functools import lru_cache
from importlib import resources
from typing import Any

from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

from pycvrx.models.resume import Resume


@lru_cache(maxsize=1)
def _validator() -> Draft202012Validator:
    """Load the bundled Reactive Resume JSON schema."""

    schema_path = resources.files("pycvrx.schema").joinpath(
        "schema.json",
    )

    with schema_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        schema = json.load(file)

    return Draft202012Validator(schema)


def validate_resume(
    resume: Resume | dict[str, Any],
) -> None:
    """
    Validate a Resume against the Reactive Resume JSON Schema.
    """

    if isinstance(resume, Resume):
        data = resume.to_dict()

    elif isinstance(resume, dict):
        data = resume.get(
            "data",
            resume,
        )

    else:
        raise TypeError("validate_resume() expects a Resume or dict.")

    try:
        _validator().validate(data)

    except ValidationError as error:
        print(
            "VALIDATION PATH:",
            list(error.path),
        )

        print(
            "SCHEMA PATH:",
            list(error.schema_path),
        )

        raise
