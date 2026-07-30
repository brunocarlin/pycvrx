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

applications = client.applications.list()

print(f"Found {len(applications)} applications")

for application in applications:
    print("-" * 50)
    print(f"ID: {application.get('id')}")
    print(f"Company: {application.get('company')}")
    print(f"Role: {application.get('role')}")
    print(f"Location: {application.get('location')}")
    print(f"Stage: {application.get('stage')}")
    print(f"Created: {application.get('createdAt')}")

client.close()
