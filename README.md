# Sentinel

Sentinel is a Singapore-focused security wearable ecosystem. It combines a cellular, GPS-enabled wrist device with an Azure-hosted control platform that delivers guided emergency workflows, secure incident reporting, and AI-assisted SOP retrieval.

## MVP scope

- LTE/4G vendor wearable with GPS, basic camera, and 24-hour battery target.
- Cellular-only communications; no site Wi-Fi dependency.
- Emergency prompts for fire, medical emergency, intrusion, duress, and suspicious person/package.
- Azure OpenAI with Azure AI Search retrieval for security-domain SOP queries.
- Regulator-format incident-report drafting with human review before submission.
- Site-scoped supervisor access; supervisors cannot access officer-to-device transcripts.
- Singapore-hosted processing, provisional audio retention of 30 days, and transcript/report retention of two years, subject to legal review.

## Technology decisions

- **Cloud:** Azure Singapore
- **AI:** Azure OpenAI and Azure AI Search (RAG)
- **Infrastructure:** Terraform
- **CI/CD:** GitHub Actions, trunk-based development
- **Backend:** Python / FastAPI

## Local development

1. Copy `.env.example` to `.env` and provide non-production credentials.
2. Create a Python environment and install `requirements.txt`.
3. Run the API with `uvicorn src.sentinel_api.main:app --reload`.
4. Run checks with `pytest` and `ruff check .`.

Never add real client data, device credentials, SIM details, or cloud secrets to the repository.

See [documentation index](docs/index.md) and [TODO.md](TODO.md).
