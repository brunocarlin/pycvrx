from __future__ import annotations

import os

from dotenv import load_dotenv

from pycvrx import Client, Config, Resume
from pycvrx.models.basics import Basics
from pycvrx.models.location import Location

load_dotenv()

client = Client(
    Config(
        api_key=os.environ["API_KEY"],
        base_url=os.environ["BASE_URL"],
    )
)

resume_id = os.environ["RESUME_ID"]

resume = Resume(
    name="Bruno Testaguzza Carlin",
    slug="bruno-testaguzza-carlin",
    tags=[
        "Data Science",
        "Machine Learning",
        "Pricing",
    ],
    is_public=True,
)

resume.basics = Basics(
    name="Bruno Testaguzza Carlin",
    headline=("Cientista de Dados | Machine Learning | Modelagem Estatística"),
    summary=(
        "Cientista de Dados com experiência em "
        "machine learning, pricing, crédito e "
        "modelagem estatística."
    ),
    location=Location(
        city="São Paulo",
        region="SP",
        country="Brasil",
    ),
)

response = client.resumes.update(
    resume_id,
    resume,
)

print("Resume updated:")
print(response)

client.close()
