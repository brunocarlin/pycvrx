# pycvrx

Python SDK for the Reactive Resume API.

[![Python](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

`pycvrx` provides a typed Python interface for creating, updating, and managing resumes using the Reactive Resume OpenAPI.

## Features

- Typed Python models
- Environment-based configuration
- Resume CRUD operations
- Automatic two-step resume creation
- Full Reactive Resume JSON schema support
- Schema validation before API requests
- Python 3.14 support
- mypy + ruff clean

## Installation

```bash
pip install pycvrx
```

or:

```bash
uv add pycvrx
```

## Configuration

Create a `.env` file:

```env
API_KEY=your_api_key
BASE_URL=https://rxresu.me/api/openapi
```

## Quick Start

```python
from dotenv import load_dotenv
import os

from pycvrx import Client, Config, Resume

load_dotenv()

client = Client(
    Config(
        api_key=os.environ["API_KEY"],
        base_url=os.environ["BASE_URL"],
    )
)

resume = Resume(
    name="Bruno Testaguzza Carlin",
    slug="bruno-testaguzza-carlin",
)

created = client.resumes.create(resume)

print(created["id"])

client.close()
```

## Creating a Resume

Reactive Resume creates resumes in two API steps:

1. Create resume metadata:

```http
POST /resumes
```

2. Upload resume content:

```http
PUT /resumes/{id}
```

`pycvrx` handles both operations internally.

Example:

```python
resume = Resume(
    name="My Resume",
    slug="my-resume",
)

created = client.resumes.create(resume)
```

## Updating a Resume

```python
client.resumes.update(
    resume_id="resume-id",
    resume=resume,
)
```

## Listing Resumes

```python
resumes = client.resumes.list()

for resume in resumes:
    print(resume["name"])
```

## Getting a Resume

```python
resume = client.resumes.get(
    "resume-id"
)
```

## Deleting a Resume

```python
client.resumes.delete(
    "resume-id"
)
```

## Models

Available models:

- `Resume`
- `Basics`
- `Location`
- `Profile`
- `Section`
- `Metadata`
- `Experience`
- `Education`
- `Project`
- `Skill`
- `Language`
- `Certification`
- `Award`
- `Interest`
- `Publication`
- `Reference`
- `Volunteer`

Example:

```python
from pycvrx import Resume
from pycvrx.models.basics import Basics

resume = Resume(
    name="Bruno",
    slug="bruno",
)

resume.basics = Basics(
    name="Bruno Testaguzza Carlin",
    headline="Data Scientist",
)
```

## Examples

A complete Portuguese resume example is included:

```bash
uv run examples/portuguese_resume.py
```

The example:

- Creates a complete resume
- Validates against the Reactive Resume schema
- Generates JSON output
- Uploads directly to Reactive Resume

## Development

Install development dependencies:

```bash
uv sync --extra dev
```

Run tests:

```bash
pytest
```

Run type checking:

```bash
mypy src
```

Run linting:

```bash
ruff check .
```

Format code:

```bash
ruff format .
```

Build package:

```bash
uv build
```

Publish package:

```bash
uv publish
```

## License

MIT License