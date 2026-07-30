from __future__ import annotations

import json
import os
from datetime import datetime

from dotenv import load_dotenv

from pycvrx import Client, Config
from pycvrx.models.items import (
    EducationItem,
    ExperienceItem,
    LanguageItem,
    ProfileItem,
    ProjectItem,
    SkillItem,
)
from pycvrx.models.resume import Resume
from pycvrx.validation import validate_resume


def build_resume() -> Resume:
    resume = Resume(
        name="Bruno Testaguzza Carlin",
        slug=(f"bruno-testaguzza-carlin-{datetime.now():%Y%m%d%H%M%S}"),
    )

    # =====================
    # Basics
    # =====================

    resume.basics.name = "Bruno Testaguzza Carlin"

    resume.basics.headline = (
        "Cientista de Dados | Machine Learning | Modelagem Financeira"
    )

    resume.basics.email = "bruno@example.com"
    resume.basics.phone = "+55 11 99999-9999"
    resume.basics.url = "https://github.com/brunocarlin"

    resume.basics.location.city = "São Paulo"
    resume.basics.location.region = "SP"
    resume.basics.location.country = "Brasil"

    resume.basics.profiles.append(
        ProfileItem(
            network="LinkedIn",
            username="brunocarlin",
            website={
                "url": ("https://linkedin.com/in/brunocarlin"),
                "label": "LinkedIn",
                "inlineLink": False,
            },
        )
    )

    # =====================
    # Summary
    # =====================

    resume.summary["content"] = (
        "Cientista de Dados especializado em "
        "machine learning, modelagem estatística "
        "e soluções analíticas para negócios "
        "financeiros."
    )

    # =====================
    # Experience
    # =====================

    resume.sections["experience"].items.append(
        ExperienceItem(
            company="BTG Pactual",
            position="Diretor de Pricing",
            location="São Paulo, Brasil",
            period="2022 - 2025",
            description=(
                "Responsável por modelos de "
                "precificação, avaliação de "
                "carteiras de crédito e "
                "estratégias quantitativas."
            ),
        ).to_dict()
    )

    # =====================
    # Education
    # =====================

    resume.sections["education"].items.append(
        EducationItem(
            school="Universidade",
            degree="Pós-graduação",
            area="Data Science e Decision Making",
            grade="",
            location="Brasil",
            period="2024 - 2025",
            description=("Especialização em ciência de dados e tomada de decisão."),
        ).to_dict()
    )

    # =====================
    # Projects
    # =====================

    resume.sections["projects"].items.append(
        ProjectItem(
            name=("Modelos de Machine Learning para Crédito"),
            location="Brasil",
            period="2024 - 2025",
            description=(
                "Pipeline completo de dados e "
                "modelos para previsão e "
                "avaliação de risco."
            ),
            website={
                "url": ("https://github.com/brunocarlin"),
                "label": "GitHub",
                "inlineLink": False,
            },
        ).to_dict()
    )

    # =====================
    # Skills
    # =====================

    resume.sections["skills"].items.extend(
        [
            SkillItem(
                name="Python",
                level=5,
                keywords=[
                    "Pandas",
                    "PySpark",
                    "PyTorch",
                    "Scikit-learn",
                ],
            ).to_dict(),
            SkillItem(
                name="Machine Learning",
                level=5,
                keywords=[
                    "XGBoost",
                    "Modelagem Estatística",
                    "Experimentação",
                ],
            ).to_dict(),
        ]
    )

    # =====================
    # Languages
    # =====================

    resume.sections["languages"].items.extend(
        [
            LanguageItem(
                language="Português",
                fluency="Nativo",
            ).to_dict(),
            LanguageItem(
                language="Inglês",
                fluency="Fluente",
            ).to_dict(),
        ]
    )

    return resume


def main() -> None:
    load_dotenv()

    resume = build_resume()

    validate_resume(resume)

    payload = resume.to_api_payload()

    with open(
        "portuguese_resume.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            payload,
            file,
            ensure_ascii=False,
            indent=2,
        )

    print("Resume validated successfully.")
    print("Saved portuguese_resume.json")

    config = Config(
        api_key=os.environ["API_KEY"],
        base_url=os.environ["BASE_URL"],
    )

    with Client(config) as client:
        created = client.resumes.create(
            resume,
        )

    print("Resume created successfully:")
    print(
        json.dumps(
            created,
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
