# Security, privacy, and access

## PDPA-oriented principles

- Confirm lawful purpose, notification, consent/other applicable legal basis, retention, access, correction, and deletion procedures with legal counsel.
- Process and store production data in Singapore-supported Azure services, subject to contract and service verification.
- Minimise data collection: retain voice audio provisionally for 30 days and transcripts/reports for two years only pending legal and customer confirmation.
- Encrypt data in transit and at rest; use Azure Key Vault and managed identities for secrets and service access.

## Prohibited practices

- No production credentials, audio, client data, SIM information, or device keys in source control.
- No supervisor access to officer-to-device transcripts.
- No general-purpose AI usage or personal-call use through the platform.
- No unattended AI submission of incident reports.

## Required reviews

Perform a DPIA/privacy review, threat model, Azure configuration review, device supply-chain review, penetration test, and OTA update security review before production.
