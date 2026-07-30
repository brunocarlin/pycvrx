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

resume_id = os.environ["RESUME_ID"]

resume = client.resumes.get(resume_id)

print("Resume:")
print(resume)

client.close()
