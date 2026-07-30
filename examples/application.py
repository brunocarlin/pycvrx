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

application = {
    "company": "Google",
    "role": "Data Scientist",
    "location": "United States",
    "salary": "",
    "source": "LinkedIn",
    "sourceUrl": "https://careers.google.com",
    "jobDescription": (
        "Data Scientist role focused on machine learning, "
        "experimentation, and analytics."
    ),
    "notes": ("Applied through careers page. Follow up after one week."),
    "resumeFileUrl": "",
    "resumeFileName": "",
    "coverLetterUrl": "",
    "coverLetterName": "",
    "followUpAt": None,
    "followUpNote": ("Check application status."),
    "contacts": [
        {
            "name": "Recruiter Name",
            "role": "Recruiter",
            "type": "recruiter",
        }
    ],
    "resumeId": "",
    "tags": [
        "data-science",
        "machine-learning",
    ],
    "stageEnteredAt": None,
}

response = client.applications.create(application)

print("Application created:")
print(response)

client.close()
