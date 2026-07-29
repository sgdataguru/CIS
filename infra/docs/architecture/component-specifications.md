# Sentinel component specifications

**Status:** Proposed component design. Azure service candidates are **subject to availability and architecture validation** in the target subscription and Singapore deployment model.

## 1. MVP component map

| Component | MVP? | Purpose and boundary | Proposed technology direction | Key dependencies and failure behaviour |
|---|---:|---|---|---|
| Vendor wearable | Yes | Collect permitted interactions, GPS, telemetry, basic voice/camera input, and receive constrained guidance. Does not decide tenant policy or submit reports. | Vendor LTE/4G wearable; vendor SDK. | Cellular/device health failure must be surfaced; supports only validated offline/fallback behaviour. |
| Device-management adapter | Yes | Normalise vendor provisioning, identity, firmware, health, OTA, reset, and lifecycle APIs. | Sentinel adapter to vendor platform; Azure-hosted integration candidate. | Vendor API/SDK; queue retries; failed OTA stops or rolls back. |
| Cellular/SIM integration | Yes | Maintain SIM association, connectivity metadata, and lifecycle evidence. | Carrier/vendor integration; exact API subject to commercial agreement. | SIM activation, coverage, provider API; no assumed real-time carrier data. |
| API gateway | Yes | Internet ingress, request policy, rate limit, routing, authentication integration. | Azure API Management candidate. | Public device endpoint; gateway outage requires monitored failure and fallback operating policy. |
| Sentinel API | Yes | Enforce business authorization, scenario, workflow, report, and retrieval policies. | FastAPI service on a managed Azure compute candidate. | Identity, event stream, control store, search/AI; deny by default on dependency/security failure. |
| Identity and secrets | Yes | Workload identity, privileged access, secret/certificate storage. | Microsoft Entra ID, managed identities, Azure Key Vault candidates. | Tenant identity model, private connectivity; secret access failure blocks protected operations. |
| Event stream / queue | Yes | Durable facts for alerts, telemetry, lifecycle, audit, and asynchronous work. | Azure Event Hubs and/or Service Bus candidates. | Schema registry/contract governance; consumers are idempotent, dead-letter invalid events. |
| Operational control store | Yes | Current alert, assignment, escalation, and fleet read models. | Managed transactional/document store candidate. | Event projection; stale-state indicators and replay/rebuild process required. |
| Raw evidence and object store | Yes | Permitted append evidence, approved artifacts, audio references, audit export. | Azure Storage candidate. | Retention/legal-hold policy, encryption, restricted access; lifecycle failure alerts. |
| Curated analytics store | Pilot-minimum | Governed aggregate assurance, fleet, and workflow metrics. | Managed query/lakehouse/warehouse candidate. | Curated events, metric catalogue; no direct raw sensitive-data access by default. |
| Knowledge intake and corpus | Yes | Approve, classify, version, and index SOPs. | Application workflow plus Azure AI Search candidate. | Content owner approval; invalid/unapproved content is not indexed. |
| AI generation | Yes | Produce cited SOP answers and report drafts after external guardrails. | Azure OpenAI candidate. | Approved retrieval, model availability, evaluation suite; failure returns controlled non-AI response. |
| Control-room services | Yes | Authorized alert and operational user experience. | Web application/API-backed service candidate. | Enterprise identity, control projections; role/site filters enforced server-side. |
| Monitoring and SIEM | Yes | Operational telemetry, security events, alerting, investigation evidence. | Azure Monitor, Application Insights, Microsoft Sentinel candidates. | Diagnostic routing, retention, on-call ownership; monitoring outage is an incident. |
| Terraform and GitHub Actions | Yes | Repeatable infrastructure and software delivery. | Terraform, GitHub Actions, federated Azure identity. | Environment approvals, state backend, branch protections; no long-lived deployment secrets. |
| Advanced edge inference / custom firmware | No | Future enhancement only. | Deferred. | Requires hardware, battery, security, and value validation. |

## 2. Configuration and integration requirements

### Device and vendor integration

- Persist a Sentinel device record, vendor identifier, device state, firmware version, SIM association, tenant/site/officer assignment history, capability profile, and reset/deactivation evidence.
- Require device identity binding before operational use. Device key/certificate, attestation, encrypted storage, remote wipe, signed OTA, and vendor diagnostics require evidence during supplier selection.
- Standardise vendor events into Sentinel canonical contracts. Keep vendor payloads isolated from domain consumers through the adapter.
- Configure OTA by signed package, approval, target cohort, release version, rollout percentage, health criteria, stop condition, rollback plan, and audit record.

### API, events, and data

- The API gateway must apply TLS, request-size limits, rate limits, gateway logging, route policy, and device authentication integration.
- The application must enforce tenant/site/role/scenario and fresh-request checks; it must not trust device-provided authorization claims without validation.
- Event consumers require schema version compatibility, idempotency, dead-letter handling, correlation IDs, retry policy, ordering assumptions, and replay/reconciliation controls.
- Operational stores need role/site query boundaries and projection freshness status. Raw evidence stores need immutable/append-oriented design, lifecycle management, and restricted investigation access.

### AI and knowledge

- SOP documents require owner, tenant/site scope, approval status, version, validity period, scenario tags, classification, source location, and withdrawal process.
- Retrieval uses application-enforced policy and metadata filters before generation. The model receives only required contextual information and must return source references.
- Prompt, model/deployment, search-index, retrieval, evaluation-suite, and report-template versions must be auditable.

## 3. Scalability, availability, and cost drivers

Scale independent paths rather than coupling them: API ingress by request volume; event ingestion/consumers by telemetry and alert rate; control read models by active operators/sites; storage by event/audio/document retention; AI/search by queries, corpus size, and tokens; monitoring by log volume; and device operations by fleet size and OTA cohorts.

Availability design prioritises alert acceptance, durable event persistence, control-room visibility, and restricted safe failure over optional AI features. AI/search unavailability must not block fixed approved emergency guidance or essential alert capture. A device/network outage is recorded as an operational condition, not concealed.

Major cost drivers are wearable purchase/replacement, SIM plans, data transfer, GPS sampling, event throughput, storage/retention, monitoring logs, search index capacity, AI tokens, support staffing, and private-networking choices. Manage cost through sampling rules, lifecycle policies, retention minimisation, archive tiers, query controls, token budgets, staged OTA, and measured capacity—not through removal of required safety, privacy, or audit controls.

## 4. Alternatives and rationale

- **Cloud-authoritative versus on-device AI:** cloud AI is preferred for MVP because it centralises policy/content and avoids device compute, battery, update, and cost burdens. Device fallback should be fixed approved guidance only.
- **Event stream versus direct synchronous integrations:** durable events are preferred for alert/audit workflows because cellular retries and downstream failures are expected.
- **Shared logical tenancy versus per-customer stacks:** shared logical tenancy improves early operating cost and speed, but must be tested rigorously; architecture must preserve a path to stronger isolation if justified.
- **Vendor adapter versus embedding vendor SDK calls:** the adapter prevents vendor specifics from becoming the platform’s core domain model and reduces future replacement cost.

## Open decisions and validation items

- Select specific Azure compute, transactional store, analytics store, queue/event-stream, and private-networking services after requirements, costs, quotas, and regional support are confirmed.
- Determine the minimum vendor wearable capabilities and integration contract from field tests and supplier evidence.
- Confirm scale forecasts, alert latency targets, control-room concurrency, data volumes, RPO/RTO, and service-level objectives.
- Confirm whether any customer requires dedicated data/security boundaries or private connectivity.
