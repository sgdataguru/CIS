# Sentinel Data, AI, and Device Platform Strategy

**Status:** Strategic baseline — validate all provisional choices before production  
**Audience:** Venture sponsors, product, security, hardware, data/AI, engineering, operations, and design-partner stakeholders  
**Related documents:** [Project context](overview.md), [Architecture overview](../architecture/overview.md), [Security and privacy](../admin/security-and-privacy.md), [Value delivery roadmap](value-delivery-roadmap.md), and [Risk and constraint register](risk-constraint-register.md)

## 1. Executive summary

### 1.1 Business context

Sentinel is a Singapore security-service assurance venture for property owners, managers, and the upper tier of security agencies. It addresses a core trust problem: buyers need evidence that a security officer is present, can respond to critical incidents, and follows the site’s approved operating procedures. A managed wearable, rather than an app-only offering, creates a more defensible service by linking officer activity, device identity, location, control-room workflow, and approved operational knowledge.

The initial product must operate where site Wi-Fi cannot be assumed. It therefore depends on a cellular-only wrist wearable with GPS, a basic camera/voice interface, a cloud control platform, and a tightly scoped AI assistant. The target is an initial rollout in three to four months; wearable selection, unit economics, supplier continuity, and security validation are more likely to constrain delivery than basic application development.

### 1.2 Strategic vision

Sentinel will provide an edge-to-cloud assurance platform in which a provisioned device is the trusted operational endpoint for an assigned officer and site. The device sends signed telemetry, location, emergency alerts, and approved voice requests through cellular connectivity. A cloud platform validates the device, tenant, site, user role, scenario, and content before it processes the request or exposes any data.

The platform will deliver two distinct but connected experiences. Officers receive concise, scenario-specific emergency guidance and can ask approved security-domain questions. Control-room teams receive high-priority alerts, operational state, and auditable event history. Supervisors see only authorized site-level information and must not receive officer-to-device transcripts. Azure OpenAI and Azure AI Search will provide retrieval-grounded SOP answers and regulator-format report drafts, but human users remain responsible for operational decisions and report submission.

The target state is a governed, multi-tenant service that can recycle devices between officers, support more than one agency or property client, and produce reliable evidence of device, alert, workflow, and report activity. It must remain deliberately narrow: Sentinel is not a general-purpose consumer assistant, an autonomous incident-management system, or a replacement for existing detailed site SOP repositories.

### 1.3 Expected outcomes

- **Assurance for buyers:** property owners can obtain auditable evidence that assigned services and emergency workflows are active.
- **Faster, more consistent critical response:** officers receive three-to-six essential steps for the approved initial scenarios: fire, medical emergency, intrusion, duress, and suspicious person/package.
- **Higher operational visibility:** control rooms receive authenticated alerts, acknowledgement state, escalation history, and device/location health within authorized site boundaries.
- **Safer knowledge access:** officers can retrieve only approved, site-scoped security SOP content with source references rather than navigating long documents during an event.
- **More efficient reporting:** a human-reviewed report draft reduces administrative effort while retaining accountability.
- **Commercially viable operations:** managed device recycling, cellular SIM control, and fleet records support a subscription model rather than a one-time device sale.

Measured MVP outcomes should include alert-delivery and acknowledgement performance, percentage of active device assignments with valid telemetry, completion rate for critical-workflow evidence, report draft completeness after review, tenant/site authorization failures, battery/cellular availability, and design-partner satisfaction. Specific thresholds require baseline collection during pilot design.

### 1.4 Strategic bets

1. **Managed wearable plus platform is the product boundary.** A cellular GPS wearable linked to a control platform and approved operational corpus is harder to replicate and provides stronger assurance than an app-only workflow.
2. **Safety-critical operational events are event-driven; analytics is not.** Emergency alerts, duress events, device health, and geofence events need near-real-time processing. Analytics, reconciliation, reporting, cost optimization, and AI evaluation can operate in scheduled or micro-batch flows.
3. **AI is assistive, grounded, and constrained.** Azure OpenAI plus Azure AI Search RAG can improve operational access to SOPs and draft reports, but it must enforce tenant/site isolation, cite sources, block off-topic requests, and require human approval before submission.

## 2. Business requirements and strategic response

### REQ-001: Provide verifiable officer and device assurance

- **Strategic approach:** Treat the wearable as a managed asset with a persistent device identity and an explicit relationship to a supplier, SIM, officer, site, and assignment period. Record operational events as immutable audit-grade facts and distinguish device presence, device health, officer assignment, and reported incident state.
- **Key capabilities:** Device registration, cryptographic device identity, SIM association, assignment lifecycle, signed telemetry, GPS/geofence event handling, event timestamps, audit storage, and role-aware operational views.
- **Success criteria:** A pilot stakeholder can reconstruct an authorized device’s assignment and operational timeline for a selected site and period without relying on unstructured manual evidence. Exceptions—such as missing telemetry, device departure, or an unacknowledged duress alert—are visible and auditable.
- **Dependencies:** Vendor device capabilities, cellular coverage, GPS accuracy, identity design, data-retention policy, and customer agreement on the meaning of assurance events.
- **Strategic rationale:** Device identity and audit events are stronger evidence than an officer’s self-reported mobile-app activity. Video surveillance is not the primary mechanism because the device has only a basic camera and because cost, privacy, power, and operational scope must remain controlled.

### REQ-002: Guide officers through critical emergencies

- **Strategic approach:** Deliver a small approved scenario catalogue instead of full SOP documents. Emergency guidance is a versioned, site-aware content product with concise actions, escalation rules, acknowledgement handling, and a defined fallback when connectivity is degraded.
- **Key capabilities:** Approved scenario catalogue, site/device validation, push or request-response guidance delivery, control-room alerting, acknowledgements, escalation timers, guidance versioning, and content governance.
- **Success criteria:** For each approved scenario, the device displays or returns the relevant three-to-six critical steps; requests outside the catalogue are safely blocked or redirected; and duress alerts reach authorized control-room users as high priority.
- **Dependencies:** Design-partner validation of scenario flows, wearable interaction design, cellular latency testing, control-room operating model, and incident escalation policies.
- **Strategic rationale:** A narrow, rehearsable set of critical actions is more useful in time-sensitive events than a long SOP dump. It also provides clearer safety testing and auditability than an unconstrained natural-language response.

### REQ-003: Deliver secure, site-scoped SOP assistance and reporting

- **Strategic approach:** Ingest only approved SOP content into a governed retrieval corpus. Use retrieval-augmented generation to answer authorized security questions and draft reports, with authorization checks before retrieval and citations after generation. Require a human to review and explicitly approve reports before they leave the platform.
- **Key capabilities:** Document approval workflow, metadata classification, tenant/site retrieval filters, search index, source citation, security-domain classifier/refusal, report templates, audit logs, and human approval state.
- **Success criteria:** Evaluation demonstrates that substantive answers include approved sources; cross-tenant and cross-site content is not returned; personal and non-work requests are refused; and no report is submitted without a named human approval event.
- **Dependencies:** Approved corpus, regulator-report format confirmation, legal review, Azure service availability, model evaluation dataset, and a defined report-submission integration or manual process.
- **Strategic rationale:** A governed RAG pattern produces more transparent and controllable results than relying on a model’s general knowledge. Human approval is necessary because the system cannot establish all factual details or assume legal responsibility for an incident report.

### REQ-004: Protect privacy, security, and access boundaries

- **Strategic approach:** Apply privacy-by-design and zero-trust controls across device, application, data, AI, and administration. Collect only the data needed for the assurance and safety purpose, process production data in Singapore-supported Azure services subject to verification, and make retention, deletion, access, and review policies configurable only after legal and customer validation.
- **Key capabilities:** Managed identities, Key Vault, encryption in transit and at rest, least-privilege RBAC, tenant/site scoping, transcript restrictions, audit logs, retention/deletion jobs, consent/notification support, security monitoring, and incident response integration.
- **Success criteria:** Access tests demonstrate supervisors cannot retrieve officer-to-device transcripts; secrets are absent from source control; access and administrative actions are logged; and required privacy, threat-model, penetration, supply-chain, and OTA security reviews are complete before production.
- **Dependencies:** DPIA/legal advice, customer contracts, Azure subscription architecture, identity provider decisions, supplier security evidence, and operating procedures for access requests and incidents.
- **Strategic rationale:** Security and privacy cannot be deferred in a solution handling voice, location, security operations, and potentially sensitive incident information. Strong boundaries also reduce the risk that a pooled device fleet exposes prior officer or client data.

### REQ-005: Operate a sustainable cellular device fleet

- **Strategic approach:** Make lifecycle management a first-class platform capability. Devices must be provisioned before use, securely associated with a SIM and a site assignment, monitored for firmware and health, remotely deactivated or recycled, and updated through a controlled OTA process.
- **Key capabilities:** Supplier/device records, provisioning, certificate/key rotation, SIM inventory, device status, firmware inventory, OTA release controls, device deactivation, recycling workflow, location-policy configuration, and fleet dashboards.
- **Success criteria:** Every pilot device has a known ownership, firmware version, assigned SIM, operational state, and assignment history. A deactivated or reassigned device cannot access the prior tenant/site scope. OTA releases have approval, rollout, monitoring, and rollback evidence.
- **Dependencies:** Wearable vendor SDK and security features, manufacturer continuity commitment, SIM pricing and provisioning model, device certification, hardware-in-loop testing, and supplier support processes.
- **Strategic rationale:** The subscription model and device recycling depend on reliable fleet controls. Without this, operating cost, privacy exposure, and support effort will undermine the business proposition.

### REQ-006: Create a multi-tenant platform that can expand without premature complexity

- **Strategic approach:** Establish a shared platform with strong logical tenant and site boundaries, standard event contracts, versioned content, and an environment-separated delivery model. Avoid building an enterprise data mesh, custom device operating system, or autonomous workflow engine during the MVP.
- **Key capabilities:** Tenant/site identifiers in every core event, authorization policy enforcement, event schemas, API contracts, environment isolation, infrastructure as code, observability, data-quality checks, and curated operational analytics.
- **Success criteria:** A new pilot site can be onboarded through an explicit configuration process; telemetry and SOP content remain isolated; and engineering can deploy repeatably to development, staging, and production using reviewed infrastructure definitions.
- **Dependencies:** Tenant model, identity/RBAC decisions, data-contract governance, Terraform foundations, CI/CD controls, and operating ownership.
- **Strategic rationale:** A configurable platform provides a path to other agencies and clients while keeping the first implementation focused. Shared capabilities are preferable to bespoke per-customer code, but isolation must be tested rather than assumed.

## 3. Data, AI, device, and control-platform strategy

### 3.1 Edge-to-cloud architecture pattern

Adopt a **managed edge endpoint with cloud-authoritative orchestration** pattern. The wearable performs only the interactions that must occur at the device: secure identity presentation, collection of permitted telemetry and GPS, emergency interaction, local delivery of minimal approved guidance when available, and reporting of device/firmware health. It is not the source of truth for tenancy, authorization, detailed SOPs, report submission, or policy decisions.

Cellular connectivity is the default path. Each request must carry a device identity, message identifier, timestamp, sequence or nonce, and relevant assigned context. Cloud ingress validates identity, transport security, freshness, signature where supported by the vendor, and authorization before invoking downstream services. This protects against replay and reduces reliance on untrusted client-provided site or officer identifiers.

Azure API Management and the Sentinel API form the policy enforcement point. The API validates tenant, site, role, scenario, content domain, and request schema. It publishes operational events for asynchronous handling while returning only the minimal synchronous response required for emergency guidance or acknowledgement. The control-room console consumes authorized read models and alert streams rather than directly querying raw device data.

### 3.2 Data architecture and storage strategy

Use a pragmatic **event-driven operational hub with layered analytical refinement**. The operational hub receives validated device and workflow events. An append-oriented event/audit layer preserves the authoritative sequence required for investigation, reconciliation, and derived views, subject to approved retention rules. Separate operational and analytical stores so response workflows are not coupled to reporting workloads.

Logical data zones are:

| Zone | Purpose | Primary data | Design principle |
|---|---|---|---|
| Ingress/quarantine | Validate structure, identity, schema version, and malware/content controls before use. | Device events, upload metadata, approved document intake. | Reject or quarantine invalid inputs; do not silently normalize them. |
| Raw evidence | Retain permitted original facts for replay and investigation. | Signed event envelopes, audit records, permitted audio references. | Preserve source timestamps and provenance; enforce retention. |
| Cleansed operational | Standardize and deduplicate valid events. | Telemetry, location, alerts, acknowledgements, device status. | Idempotent processing and schema evolution. |
| Curated control | Support near-real-time operational views. | Active alerts, assignment status, escalation state, fleet health. | Optimize for role-scoped queries and predictable latency. |
| Curated analytics | Support assurance, fleet, service, and quality analysis. | Aggregated incident, response, coverage, and device metrics. | Use business-defined metrics with lineage. |
| Knowledge corpus | Serve approved SOP retrieval. | Versioned, classified, tenant/site-scoped documents and embeddings. | Document approval, metadata filters, citations, and access control. |

Telemetry, alerts, GPS/geofence events, delivery/acknowledgement status, device lifecycle records, and audit events are distinct record types even when correlated. Audio should not be treated as a default analytical data source. The provisional policy retains audio for 30 days and transcripts/reports for two years, but the actual legal basis, purpose limitation, access controls, and deletion implementation require confirmation before production.

Store hot operational data for active control-room queries in a managed transactional or operational store. Store immutable event streams and approved artifacts in durable object/event storage with lifecycle policies. Store curated analytical data in a governed query layer suited to the eventual reporting tool. The exact Azure services, SKUs, private networking model, and backup configuration belong to the architecture phase after Singapore-region service availability is verified.

### 3.3 Integration and processing approach

Use streaming or event-driven processing for safety and operational state: emergency alerts, duress, device assignment changes, GPS/geofence exceptions, device health, guidance delivery, acknowledgement, and escalation. All consumers must be idempotent because cellular retries and delayed messages are expected. Event schemas must include version, event ID, device ID, tenant ID, site ID, occurred timestamp, received timestamp, and correlation ID.

Use scheduled or micro-batch processing for data-quality reconciliation, compliance reporting, operational analytics, cost analysis, retention/deletion verification, device-fleet trends, and AI evaluation. This avoids overengineering all workloads for real-time processing while maintaining a path to reprocess historical events when schemas or rules change.

Prefer API-first integration for command/request flows and asynchronous messaging for facts and downstream actions. Avoid point-to-point integrations between device vendors, control-room UI, AI services, reporting, and customer systems. Customer or regulator integrations should consume reviewed, versioned outputs rather than raw event streams.

### 3.4 Data modelling, quality, lineage, and observability

The canonical model is a set of versioned domain events: device provisioned, device assigned, device deactivated, device health observed, location observed, site boundary entered/left, emergency initiated, guidance delivered, acknowledgement received, escalation initiated, SOP query requested, report draft created, report approved, and report submitted. The model must separate measured facts from inferred status and from human-entered conclusions.

For analytics, build simple business-aligned dimensions—tenant, site, device, officer assignment, scenario, time, firmware version, and SIM plan—with incident, alert, response, device-health, and workflow fact tables. Introduce more elaborate modelling patterns only when product use or reporting complexity justifies them.

Quality controls occur at three points:

1. **Ingress:** authentication, schema validation, required fields, event-size limits, timestamp plausibility, duplicate detection, and location range checks.
2. **Transformation:** sequence reconciliation, assignment validity, referential integrity, scenario validity, late-arriving event handling, and retention classification.
3. **Consumption:** freshness indicators, metric definitions, completeness checks, access-policy tests, citation coverage, and anomaly detection for fleet and alert behavior.

Every material transformation must retain lineage to source event IDs and ruleset/version identifiers. Operational telemetry must cover device connectivity, API error rates, event lag, queue depth, alert-delivery latency, acknowledgement duration, search retrieval failures, model latency, blocked query rate, and policy enforcement failures. Monitoring is not only a technical concern: it must support business SLAs and pilot support triage.

### 3.5 AI and retrieval strategy

Use Azure AI Search and Azure OpenAI as a managed, retrieval-grounded assistant for approved security content. The retrieval pipeline begins with document intake, review, classification, tenant/site ownership, validity period, version, approval status, and scenario tags. Only approved content is eligible for indexing. Index updates require audit evidence so an answer can be traced to the source corpus version used at the time.

Before retrieval, the application evaluates requester identity, device/site assignment where relevant, tenant/site scope, request purpose, and security-domain eligibility. It then applies metadata filters to prevent cross-tenant or cross-site retrieval. The generation layer should return citations for substantive SOP guidance and state uncertainty when approved sources do not support an answer. It must not expose raw transcripts, secrets, hidden instructions, or inaccessible documents.

The assistant must refuse personal, non-work, and out-of-domain requests. It must not invent emergency actions that conflict with approved guidance, autonomously command the wearable, or submit a report. Report generation uses approved templates and explicit review state; a named authorized human must approve before submission.

Evaluation is a release gate, not an occasional experiment. Maintain a representative test set for each scenario, site-isolation query, off-topic query, prompt-injection attempt, source-citation case, report template, and expected refusal. Measure groundedness, citation correctness, retrieval isolation, refusal quality, critical-action safety, response latency, report field completeness, and regression against previous corpus/model/prompt versions.

### 3.6 Device lifecycle strategy

Select a vendor wearable rather than developing custom hardware for the MVP. The candidate device must support LTE/4G cellular connectivity, GPS, basic camera/voice interaction, secure device identity, remote management, firmware version reporting, and controlled OTA updates. A 24-hour battery target, SGD 20–30 preferred unit cost, SGD 100 hard ceiling, India or Shenzhen sourcing, and a three-to-four-year supplier continuity commitment are decision constraints.

The lifecycle is: supplier approval → device registration → identity/key provisioning → SIM association → configuration baseline → officer/site assignment → health monitoring → alert/telemetry operation → update or repair → deactivation → data wipe/reset where supported → reassignment/recycling or retirement. A device reassigned to a new officer or tenant must not retain prior scopes, cached content, credentials, or accessible records.

OTA update management needs signed packages, vendor provenance, test evidence, staged rollout groups, health monitoring, rollback strategy, release approval, and audit logs. Hardware-in-loop testing is mandatory for critical wearable interactions before a release is promoted. The platform should flag—but not automatically assume misconduct from—geofence departure; customer policy, safety, GPS confidence, and operational context determine follow-up.

### 3.7 Security and governance approach

Security is based on least privilege, defence in depth, and separation of duties. Production access uses managed identities and Key Vault rather than stored application credentials. Data is encrypted in transit and at rest. Every tenant/site access, administrative change, device lifecycle action, document approval, model request, report approval, and configuration update generates an auditable record.

Roles are deliberately bounded: officers perform assigned site actions; control-room operators see authorized active sites and escalations; supervisors see site-level operational information without officer-to-device transcripts; tenant and platform administrators have distinct scopes. Use explicit policy tests for each prohibited cross-role and cross-tenant access path.

Governance includes data classification, retention, deletion, access request handling, source-document ownership, model/content change management, incident response, supplier risk management, and review evidence. Before production, conduct the required DPIA/privacy review, threat model, Azure configuration review, penetration test, device supply-chain review, and OTA update security review.

## 4. Technology approach

### 4.1 Cloud platform rationale

Azure Singapore is the proposed cloud location because it supports the stated Singapore-hosted data objective and provides a managed ecosystem for API, identity, messaging, storage, search, AI, monitoring, and security operations. This reduces undifferentiated operational effort during an ambitious MVP timeline. It also aligns with the current decision to use Terraform and GitHub Actions.

This is a strategic preference, not evidence of compliance or service availability. The architecture phase must confirm Azure service availability, model availability, data-processing locations, contractual terms, network design, private connectivity support, costs, quotas, and disaster-recovery capabilities before a production decision.

### 4.2 Required capability map

| Capability | Strategic need | Direction |
|---|---|---|
| API and policy enforcement | Validate device and user requests before processing. | Managed API gateway plus application services. |
| Identity and secrets | Limit access and remove embedded credentials. | Enterprise identity, managed identities, Key Vault, certificate/device identity. |
| Event processing | Process urgent facts independently and reliably. | Managed event streaming/queueing and idempotent consumers. |
| Operational and analytical storage | Serve control-room workflows, audit evidence, and governed reporting. | Separate operational, immutable/event, object, and curated analytical stores. |
| AI and search | Ground answers in approved SOPs and support report drafting. | Azure AI Search plus Azure OpenAI behind application guardrails. |
| Device management | Provision, monitor, update, deactivate, and recycle wearables. | Vendor-compatible device-management integration, not vendor-specific logic embedded across the application. |
| Observability and security | Detect operational failure and suspicious activity. | Central monitoring, logging, alerting, and SIEM integration. |
| Delivery and infrastructure | Repeatable, reviewed changes across environments. | Terraform, GitHub Actions, environment approvals, and federated cloud identity. |

### 4.3 Analytics and reporting approach

Operational views and analytics have different purposes. The control room needs current, role-scoped information: active alerts, acknowledgement/escalation status, assigned device state, and potentially live location under approved policy. Analytics users need governed measures such as response time distribution, guidance delivery success, device availability, coverage exceptions, incident volumes, fleet health, and service subscription indicators.

Define each metric in a curated semantic layer or documented metric catalogue, including owner, formula, data-quality checks, period, exclusions, and privacy classification. Do not give analytical users unrestricted access to raw audio, transcripts, or raw location history. Start with a small set of assurance metrics validated with the design partner, then expand only when use cases prove value.

### 4.4 Infrastructure as code and delivery

Use Terraform for declarative Azure infrastructure, with separate development, staging, and production environments, distinct identities/secrets/telemetry, and reviewable plans. GitHub Actions runs baseline linting, tests, security checks, and infrastructure validation. Deployment should use federated identity, not static cloud credentials, and production needs explicit security, privacy, and operational approval.

Infrastructure modules should reflect capability boundaries—networking/security foundation, identity/secrets, ingress/API, messaging/data, AI/search, monitoring, and application hosting. Avoid prematurely creating every possible Azure service; provision only what the validated MVP requires. Configuration, policy, and retention changes must be version controlled and auditable.

## 5. Strategic decision framework

### D-001: Event-driven versus batch processing

- **Decision point:** What processing model should support device and business data?
- **Options considered:** (1) event-driven processing for all workloads; (2) daily batch for all workloads; (3) event-driven operational processing with batch/micro-batch analytics.
- **Recommended strategy:** Option 3. Emergency, duress, telemetry, location, acknowledgement, and escalation events require near-real-time flows. Analytics, reconciliation, retention verification, and AI evaluation do not.
- **Decision criteria:** safety response latency, cellular reliability, cost, operational skill, reprocessing needs, and auditability.
- **Decision timing:** Confirm event latency budgets and vendor message semantics in the Phase 1 pilot design.
- **Reversibility:** Core event handling is difficult to reverse without degrading the safety proposition; analytical frequency is a two-way decision.

### D-002: Cloud-only versus edge AI inference

- **Decision point:** Where should AI retrieval and generation run?
- **Options considered:** (1) cloud-only RAG and generation; (2) on-device inference; (3) hybrid cached/edge and cloud inference.
- **Recommended strategy:** Cloud-only AI for MVP, with a minimal device fallback of approved fixed emergency prompts. This matches the constrained wearable, 24-hour battery target, low hardware cost target, and need for centralized content governance.
- **Decision criteria:** connectivity, latency, battery, device compute, content updates, privacy, model quality, and cost.
- **Decision timing:** Reassess after pilot measurements of cellular availability and operational latency.
- **Reversibility:** A hybrid design can be added later if device hardware supports it, but cloud governance remains required.

### D-003: Audio retention versus transient processing

- **Decision point:** How much voice data should Sentinel retain?
- **Options considered:** (1) retain audio for a limited period; (2) process audio transiently and retain only structured outcomes/transcripts; (3) retain audio and transcripts long term.
- **Recommended strategy:** Use the current provisional limit—audio 30 days, transcripts/reports two years—only until DPIA, legal, client, security, and operational reviews validate a final policy. Apply purpose limitation, access controls, deletion automation, and audit evidence.
- **Decision criteria:** PDPA obligations, incident investigation needs, customer expectations, storage cost, access risk, and model-quality needs.
- **Decision timing:** Before any production recording or pilot data collection.
- **Reversibility:** Retention expansion is a high-risk one-way decision; reducing retention is easier but may affect investigations.

### D-004: Shared multi-tenant platform versus isolated deployment per customer

- **Decision point:** What isolation model should be used for early customers?
- **Options considered:** (1) shared platform with logical tenant/site isolation; (2) dedicated deployment per customer; (3) hybrid dedicated data/security boundaries for selected customers.
- **Recommended strategy:** Start with a shared logically isolated platform, with architecture that permits stronger isolation for a future justified customer. Validate isolation through automated authorization and retrieval tests.
- **Decision criteria:** time to market, operating cost, customer security expectations, supportability, scalability, and contract requirements.
- **Decision timing:** Confirm during design-partner security and commercial review.
- **Reversibility:** Shared-to-hybrid migration is feasible but needs planned data and identity boundaries; it should not be left to an emergency retrofit.

## 6. Strategic principles

1. **Safety and human control first:** AI assists; authorized people decide and approve.
2. **Managed device, not unmanaged app:** device identity, fleet management, and lifecycle evidence are product capabilities.
3. **Security and privacy by default:** least privilege, tenant/site isolation, encryption, audit logs, and minimised data collection begin in Phase 1.
4. **Event facts are durable; derived views are replaceable:** retain permissible original events and ruleset versions so workflows can be reconciled and improved.
5. **Design for intermittent connectivity:** cellular delay, retry, duplication, and loss are normal operating conditions, not exceptional cases.
6. **Use approved content:** guidance and retrieval are sourced, versioned, scoped, and testable.
7. **Keep the MVP deliberately narrow:** deliver measurable assurance and emergency value before expanding device features, AI scope, integrations, or analytics.
8. **Automate evidence:** tests, deployment controls, access checks, retention jobs, supplier reviews, and AI evaluations must produce reviewable records.
