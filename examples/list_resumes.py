from __future__ import annotations

import os

from dotenv import load_dotenv

from pycvrx import Client, Config

load_dotenv()

client = Client(
    Config(
        api_key=os.environ["API_KEY"],
        base_url=os.environ["BASE_URL"],
    )
)

resumes = client.resumes.list()

print(f"Found {len(resumes)} resumes")

for resume in resumes:
    print("-" * 50)
    print(f"ID: {resume.get('id')}")
    print(f"Name: {resume.get('name')}")
    print(f"Slug: {resume.get('slug')}")
    print(f"Public: {resume.get('isPublic')}")
    print(f"Created: {resume.get('createdAt')}")
    print(f"Updated: {resume.get('updatedAt')}")

client.close()
