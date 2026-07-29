# Architecture overview

## Logical flow

1. A provisioned wearable sends signed telemetry, GPS, alerts, and approved voice requests over cellular connectivity.
2. Azure API Management authenticates requests and routes them to the Sentinel API.
3. The API applies tenant, site, role, scenario, and content guardrails before processing.
4. Event streams persist audit-grade telemetry and incident events. Audio is retained provisionally for 30 days; transcripts and reports for two years.
5. Azure AI Search retrieves only approved, site-scoped security SOP content. Azure OpenAI produces guided responses and report drafts.
6. A control-room console and supervisor views use site-scoped authorization. Officers' transcripts are not exposed to supervisors.
7. Azure Monitor and Microsoft Sentinel capture operational and security signals. Device lifecycle services control provisioning and OTA updates.

## Trust boundaries

- Device-to-cloud traffic must use mutual device identity, encrypted transport, and replay protection.
- The RAG index must separate tenants and sites, enforce document approvals, and preserve source citations.
- AI output must be constrained to the security domain and must not autonomously submit reports or command devices.
- Secrets belong in Azure Key Vault; client applications and repositories receive no production credentials.

See `infra/docs/sentinel-architecture.puml` for the proposed implementation diagram.
