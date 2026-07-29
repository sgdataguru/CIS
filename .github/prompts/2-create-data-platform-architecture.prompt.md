# Sentinel Data, AI, Device, and Control Platform Architecture Prompt

You are an expert architect for cloud data platforms, AI systems, connected devices, and security operations. Design a complete, modern architecture for Sentinel: a Singapore-hosted security wearable ecosystem that combines cellular wrist devices, a control-room platform, event-driven data processing, governed analytics, and constrained AI assistance.

Base the architecture on these required inputs:

- `docs/project-context/data-platform-strategy.md` — strategic decisions, requirements, risks, constraints, and principles.
- `docs/architecture/overview.md` — current logical flow and trust boundaries.
- `docs/project-context/risk-constraint-register.md` — risks, assumptions, and constraints that must be reflected in design choices.
- `docs/admin/security-and-privacy.md` — PDPA-oriented safeguards and access restrictions.

Treat unconfirmed Azure service availability, regulatory interpretation, supplier capability, network connectivity, service quotas, and costs as validation items. Do not state that any service is compliant, available, certified, or contractually approved without supporting evidence.

## Architecture objectives and non-negotiable boundaries

The architecture must:

- Support a vendor wrist wearable using cellular LTE/4G connectivity, GPS, basic camera/voice capability, secure device identity, remote management, and OTA updates.
- Handle signed telemetry, GPS/location, alerts, guidance delivery, acknowledgement, escalation, device lifecycle, and audit events through an event-driven operational flow.
- Validate device identity, request freshness, replay protection, tenant, site, role, scenario, and request schema before processing.
- Separate operational control-room data from immutable event/audit evidence, analytical data, and approved knowledge content.
- Use Azure Singapore as the intended cloud region, Terraform for infrastructure as code, and GitHub Actions for delivery, subject to design validation.
- Use Azure AI Search and Azure OpenAI only behind application-level guardrails for approved, tenant/site-scoped security SOP retrieval and human-reviewed incident-report drafting.
- Enforce a security-domain-only AI scope, source citations, off-topic refusal, prompt-injection defences, retrieval isolation, and explicit human approval before report submission.
- Enforce role separation: officers use assigned site actions; control-room users see authorized active sites and escalations; supervisors see site-level operational data but not officer-to-device transcripts; tenant and platform administrators have separate scopes.
- Protect voice, location, incident, device, SIM, and customer data. Audio retention is provisionally 30 days; transcripts and reports are provisionally two years, pending DPIA, legal, customer, and operational approval.
- Support device provisioning, SIM association, assignment, health, firmware inventory, staged OTA rollout, rollback, deactivation, reset/wipe, and recycling.
- Design for intermittent cellular connectivity, delayed and duplicate events, time drift, and GPS uncertainty.
- Avoid unnecessary complexity: do not introduce custom device firmware, edge AI inference, multi-cloud, or unvalidated services into the MVP architecture without a documented rationale.

## Architecture Design Deliverables

Create the following documentation files in the specified locations:

### High-Level Architecture (docs/architecture/)

**1. `docs/architecture/overview.md`**
- Replace the existing overview with an executive summary of the Sentinel edge-to-cloud platform.
- Add a high-level Mermaid logical architecture diagram showing wearable, cellular network, device-management integration, Azure ingress/API policy enforcement, event processing, operational/control-room services, data zones, AI Search/OpenAI RAG, identity/secrets, monitoring/SIEM, and authorized users.
- Describe major components, trust boundaries, data classifications, and their relationships.
- State the key design principles and architectural decisions, including managed edge endpoint/cloud-authoritative orchestration, event-driven critical operations, human-controlled AI, zero-trust access, tenant/site isolation, and resilience to intermittent connectivity.

**2. `docs/architecture/data-flows.md`**
- Provide end-to-end Mermaid sequence or flow diagrams for:
	- Emergency scenario invocation through device, cellular network, API validation, event processing, control-room alert, acknowledgement, escalation, and audit evidence.
	- Device provisioning, SIM association, assignment, health reporting, deactivation/recycling, and OTA rollout/rollback.
	- SOP document approval and ingestion, site-scoped retrieval, Azure OpenAI response generation with citations, report drafting, human approval, and submission.
	- Data retention/deletion processing and analytical refinement.
- Specify real-time/event-driven, synchronous request-response, and batch/micro-batch processing boundaries.
- Define canonical event envelope requirements: event ID, schema version, device ID, tenant ID, site ID, correlation ID, occurred timestamp, received timestamp, signature or integrity evidence, and idempotency strategy.
- Define storage zones and access patterns for ingress/quarantine, raw evidence, cleansed operational data, curated control data, curated analytics, and the approved knowledge corpus.
- Explain hot/warm/cold lifecycle intent without inventing retention schedules beyond the provisional policies already documented.

**3. `docs/architecture/security-governance.md`**
- Define device, workload, user, and administrator authentication; managed identities; certificate/key lifecycle; and least-privilege RBAC.
- Describe tenant/site authorization enforcement at API, event-consumer, data-query, control-room, and RAG retrieval layers.
- Specify encryption in transit and at rest, secret handling through Azure Key Vault, key rotation, audit logging, and prohibited source-control content.
- Define network isolation, private endpoint/service-access validation requirements, inbound/outbound policy, and monitoring/SIEM integration.
- Describe data classification, lineage, data-quality controls, document approval, retention/deletion, legal-hold validation, audit evidence, access review, and PDPA-oriented privacy controls.
- Include AI-specific governance: corpus ownership, metadata filtering, source citations, model/prompt/version evaluation, refusal policy, human approval, and red-team testing.

### Detailed Architecture (infra/docs/architecture/)

**4. `infra/docs/architecture/component-specifications.md`**
- Detail every proposed component, including wearable/vendor integration, cellular/SIM management integration, API Management, Sentinel API/application hosting, identity, secrets, event streaming/queueing, operational store, event/audit/object storage, analytics store, Azure AI Search, Azure OpenAI, device-management integration, monitoring/SIEM, control-room experience, and CI/CD/IaC.
- For each component, provide:
	- Purpose and boundary of responsibility.
	- Proposed technology category and Azure service candidate where appropriate; label it **subject to availability and architecture validation**.
	- Rationale and viable alternatives.
	- Required configuration, identity, authorization, encryption, observability, and data-classification considerations.
	- Dependencies, integration contracts, and failure behavior.
	- Scalability, availability, performance, data-residency, operational, and cost drivers.
- Explicitly separate MVP-required components from later optional capabilities.

**5. `infra/docs/architecture/network-security.md`**
- Define the proposed Azure network topology, segmentation, ingress/egress paths, and trust boundaries for internet-connected wearables, control-room users, build agents, and managed services.
- Describe virtual networks, subnets, network security groups, route controls, firewall rules, private endpoints, private DNS, and service endpoints where they are applicable and supported.
- State which public endpoints are unavoidable for device connectivity and how API gateway, WAF/DDoS controls, rate limiting, mutual device authentication, request validation, and logging reduce exposure.
- Define outbound restrictions, DNS resolution, certificate management, and the treatment of vendor device-management and third-party cellular/SIM integrations.
- Address VPN/ExpressRoute only as a future/customer integration option; do not make it an MVP dependency unless required by a validated design partner.
- Include a validation checklist for regional availability, private connectivity support, IP allowlists, firewall rules, and penetration testing.

**6. `infra/docs/architecture/operations.md`**
- Define monitoring and logging for device connectivity, battery/firmware health, cellular delivery, API errors, identity failures, event lag/queue depth, alert delivery, acknowledgement and escalation time, geofence exceptions, data-quality failures, RAG retrieval, AI latency/refusals/citations, retention jobs, OTA outcomes, and security events.
- Define operational alert priorities, ownership, escalation, audit review, support expectations, and test/drill requirements. Do not invent SLA values; list values that need validation.
- Describe backup, restore, disaster recovery, resilience, event replay, idempotent recovery, rollback, and device deactivation processes.
- Design CI/CD around GitHub Actions, Terraform, federated cloud identity, separate development/staging/production environments, automated tests, linting, secret scanning, SAST, dependency/license scanning, infrastructure scanning, AI evaluation regression tests, and gated production deployment.
- Include staged OTA release, hardware-in-loop validation, monitoring, stop conditions, and rollback requirements.
- Identify major cost drivers—device/SIM, event volume, location/audio retention, storage lifecycle, AI/search usage, monitoring, and support—and optimization levers that do not weaken safety, privacy, or auditability.

## Instructions

- Create each document as a separate markdown file in the specified location
- Use clear headings and consistent formatting across all documents
- Use Mermaid syntax for diagrams. Diagrams must be readable in GitHub Markdown and include trust boundaries and major data/control flows where relevant.
- Cross-reference related documents when needed
- Distinguish confirmed decisions, provisional policies, and validation items. Include an explicit **Open Decisions and Validation Items** section in each document.
- Ensure technical accuracy, traceability to the strategy, and consistency with the stated trust boundaries.
- Do not include timelines, roadmaps, implementation schedules, or detailed task breakdowns.
- Do not replace policy, legal, security, hardware-certification, supplier, or Azure service-availability validation with assumptions.

