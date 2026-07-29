# Sentinel security and governance architecture

**Related:** [Architecture overview](overview.md), [Data flows](data-flows.md), [Security and privacy](../admin/security-and-privacy.md), and [Risk register](../project-context/risk-constraint-register.md).

## 1. Security model

Sentinel uses a zero-trust model: no device, user, workload, network path, document, or AI response is trusted solely because it is inside a named environment. Authorization is enforced at each request, event, query, and retrieval boundary. The system separates tenant, site, role, device assignment, and operational purpose.

| Principal | Authentication direction | Authorization boundary |
|---|---|---|
| Wearable | Vendor-supported certificate, key, token, or equivalent device identity; final mechanism requires validation. | Device is active, assigned, and authorized for tenant/site/action. |
| Officer | Device-mediated interaction and, where applicable, user identity. | Assigned device and site actions only. |
| Control-room operator | Enterprise identity provider with MFA, subject to customer decision. | Authorized active sites, alerts, and escalations. |
| Supervisor | Enterprise identity provider with MFA. | Site-level operational views; no officer-to-device transcripts. |
| Tenant/platform administrator | Privileged enterprise identity with separated duties. | Explicit administration scope, audited changes. |
| Application workloads | Managed identities. | Minimum service-to-service permissions. |
| CI/CD workloads | Federated GitHub Actions identity. | Environment-scoped deployment rights; no static cloud credentials. |

## 2. Device and API security

The device-to-cloud connection must use encrypted transport and a per-device identity. Ingress validates certificate/token status, device lifecycle state, request integrity where supported, freshness, nonce/sequence, message size, schema version, tenant/site context, and permitted scenario. Rejected requests create minimal security/audit events and must not trigger a control-room workflow.

Keys and certificates require issuance, rotation, revocation, inventory, and compromise-response processes. Device reset/deactivation must revoke prior credentials before reassignment. The device vendor’s support for secure storage, attestation, signed firmware, and remote wipe is a required validation item.

## 3. Tenant, site, and role authorization

Authorization must be evaluated in the Sentinel API before commands, reads, event publication, report actions, and retrieval requests. Downstream event consumers must revalidate the context needed for their action rather than trusting arbitrary payload fields. Data-query and control-room services apply tenant/site filters server-side; clients do not choose unrestricted scopes.

| Layer | Required enforcement |
|---|---|
| API ingress | Device/user identity, lifecycle/assignment, tenant, site, role, scenario, freshness, schema. |
| Event consumers | Allowed event type, producer identity, schema/version, deduplication, tenant/site partition or filter. |
| Operational store | Row/document-level tenant/site constraints where supported; application authorization remains mandatory. |
| Control room | Role and site scope, least-privilege fields, audit of sensitive views/actions. |
| Analytics | Curated, purpose-limited, aggregated access; raw location/audio/transcript access restricted. |
| RAG retrieval | Pre-retrieval caller policy plus tenant/site/approval/validity metadata filters. |

Automated tests must cover cross-tenant, cross-site, supervisor-transcript, deactivated-device, stale-token, and report-approval bypass attempts.

## 4. Secrets, encryption, and network controls

Use Azure Key Vault and managed identities for production secrets. Repositories, device configuration artifacts, logs, and test fixtures must not include production credentials, SIM data, device keys, client data, raw audio, or transcripts. Encrypt data in transit and at rest using supported platform capabilities; customer-managed key requirements, key jurisdiction, and backup-key handling remain validation items.

Proposed network controls include internet-facing device ingress through a protected API gateway, rate limits and DDoS/WAF capabilities where applicable, private connectivity for supported internal managed services, restricted workload egress, and central diagnostic export. Final VNet, subnet, private endpoint, DNS, and firewall controls are described in [network security](../../infra/docs/architecture/network-security.md) and require regional/service validation.

## 5. Data governance, privacy, lineage, and retention

Classify data at minimum as: public operational metadata, internal platform configuration, confidential tenant/site operations, sensitive personal data (officer location/voice/transcripts), and restricted security/credential material. Tag data with tenant, site, purpose, source, owner, retention class, and approval/version where relevant.

Lineage must connect a curated metric, report draft, alert state, or AI answer to source event IDs, transformation version, content version, and policy/configuration version. Quality controls validate device/event schema, timestamp plausibility, assignment validity, duplicate handling, required metadata, retrieval citations, and retention/deletion execution.

Audio is provisionally 30 days; transcripts and reports are provisionally two years. These periods require DPIA, legal, customer, and operational confirmation before production. Retention automation must support approved legal holds, deletion evidence, backup/restore policy, and access/correction processes appropriate to the final policy.

## 6. AI governance

Approved SOPs enter the knowledge corpus only after owner approval, tenant/site classification, validity/date control, and versioning. The application applies domain classification and caller authorization before it retrieves content. Search uses tenant/site/approval/validity filters. Model requests include only data required for the purpose and produce source citations for substantive answers.

Controls include refusal of personal/non-work requests, prompt-injection testing, untrusted-document handling, model/prompt/retrieval version tracking, output safety checks, rate limits, audit records, and human approval for reports. Critical emergency steps remain fixed approved content rather than unconstrained generated advice. A release requires evaluation of groundedness, citation correctness, tenant isolation, refusal quality, response latency, report completeness, and regression against the approved test suite.

## 7. Audit and compliance evidence

Audit records must cover authentication outcomes, authorization decisions, device lifecycle changes, configuration changes, SOP approval/indexing, AI retrieval/generation metadata, report approval/submission, access to sensitive views, retention/deletion jobs, OTA releases, and privileged deployment activity. Audit design should favor tamper-evident/append-oriented records, time synchronization, correlation IDs, restricted access, and documented review procedures.

This architecture supports PDPA-oriented safeguards but does not determine legal compliance. Required pre-production evidence includes DPIA/privacy review, legal basis/notice decisions, threat model, Azure configuration review, penetration testing, device supply-chain review, and OTA update security review.

## Open decisions and validation items

- Select the enterprise identity provider, MFA/conditional-access baseline, and customer federation model.
- Confirm device credential/attestation, key storage, certificate rotation, reset/wipe, and signed-firmware features.
- Confirm final data classification, retention, legal-hold, backup, deletion, and access/correction policies.
- Validate Azure private connectivity, diagnostic retention, SIEM integration, encryption/key options, and service data-processing location.
- Define security incident ownership, notification, evidence preservation, and access-review cadence.
