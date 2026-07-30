from __future__ import annotations

import os

import httpx
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.environ["BASE_URL"].rstrip("/")
API_KEY = os.environ["API_KEY"]

response = httpx.post(
    f"{BASE_URL}/resumes",
    headers={
        "x-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    },
    json={
        "name": "SDK Test",
        "slug": "sdk-test",
        "tags": [],
        "withSampleData": False,
    },
    timeout=30,
)

print("Status:", response.status_code)
print(response.text)
