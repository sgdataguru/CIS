# Sentinel infrastructure overview

The proposed MVP uses Azure's Singapore region, Terraform, and GitHub Actions. The reference design includes API Management, a Python application service, Azure OpenAI, Azure AI Search, Event Hubs, storage, database services, Key Vault, monitoring, and device-management integration.

## Environment model

Maintain separate development, staging, and production subscriptions or resource groups with distinct identities, secrets, telemetry, and approval gates. Production deployment requires security, privacy, and operational sign-off.

## Provisioning sequence

1. Create networking, private endpoints where supported, identities, Key Vault, and diagnostic destinations.
2. Provision data, messaging, and application services.
3. Configure search indexes, approved SOP ingestion, and Azure OpenAI deployments.
4. Deploy the API and control-platform components.
5. Configure monitoring, alerting, retention/deletion jobs, and backup/restore procedures.

Terraform implementation is intentionally a secure starter skeleton until subscription, network, SKU, and service-availability details are confirmed.
