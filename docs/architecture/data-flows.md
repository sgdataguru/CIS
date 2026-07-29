# Sentinel data flows

**Related:** [Architecture overview](overview.md), [Platform strategy](../project-context/data-platform-strategy.md), and [Security governance](security-governance.md).

## 1. Emergency alert and acknowledgement

```mermaid
sequenceDiagram
  participant W as Wearable
  participant G as API gateway
  participant A as Sentinel API
  participant E as Event stream
  participant C as Control room
  participant R as Audit store
  W->>G: Signed emergency event + nonce + context
  G->>A: Authenticated, rate-limited request
  A->>A: Validate device, assignment, tenant/site, scenario, freshness
  alt invalid or replayed
    A-->>W: Reject without workflow action
    A->>R: Policy/audit event
  else valid
    A->>E: EmergencyInitiated (durable)
    A-->>W: Approved critical guidance / receipt
    E->>C: Authorized alert view
    C->>A: Acknowledge or escalate
    A->>E: Acknowledged / Escalated
    E->>R: Immutable audit evidence
  end
```

The device interaction uses synchronous request/response only for a limited receipt or approved guidance path. Alert delivery, control-room updates, escalation, notifications, audit persistence, and analytics consume durable events. Acknowledgement state must distinguish requested, delivered, displayed, acknowledged, and escalated outcomes.

## 2. Device lifecycle and OTA flow

```mermaid
flowchart LR
  V[Approved vendor device] --> P[Register device and supplier record]
  P --> I[Provision device identity and configuration]
  I --> SIM[Associate SIM]
  SIM --> AS[Assign officer and site]
  AS --> H[Health / telemetry events]
  H --> D[Deactivate or reassign]
  D --> W[Revoke credentials and wipe/reset evidence]
  W --> R[Recycle or retire]
  O[Signed approved OTA release] --> T[Hardware-in-loop test]
  T --> S[Staged cohort rollout]
  S --> M[Monitor health and version]
  M -->|failure threshold| RB[Rollback / stop]
```

The vendor adapter owns protocol-specific behaviour. Sentinel owns lifecycle state, authorization, evidence, rollout policy, and tenant/site reassignment controls. A device cannot act for a prior assignment after deactivation or reassignment.

## 3. SOP retrieval and human-reviewed reporting

```mermaid
sequenceDiagram
  participant Owner as SOP owner
  participant K as Knowledge intake
  participant S as AI Search
  participant A as Sentinel API
  participant L as Azure OpenAI
  participant U as Authorized user
  Owner->>K: Submit document, metadata, approval
  K->>K: Validate ownership, version, tenant/site, validity
  K->>S: Index approved content only
  U->>A: Security-domain question / report request
  A->>A: Authenticate and apply tenant/site/purpose policy
  A->>S: Filtered retrieval
  S-->>A: Approved source passages and metadata
  A->>L: Guardrailed generation request
  L-->>A: Draft response with sources
  A-->>U: Cited answer or report draft
  U->>A: Explicit authorized approval
  A->>A: Validate approval and template state
  A-->>U: Submit or export approved report
```

The application rejects off-topic requests and treats retrieved text as untrusted input. No model output can submit a report or command a device. Corpus, prompt, model/deployment, retrieval, output, and approval versions require audit evidence.

## 4. Data refinement, retention, and deletion

```mermaid
flowchart LR
  IN[Ingress and quarantine] --> RAW[Raw permitted evidence]
  RAW --> CL[Cleanse, deduplicate, reconcile]
  CL --> CTRL[Curated control read models]
  CL --> ANA[Curated analytics]
  RAW --> RET[Retention / legal-hold evaluation]
  CTRL --> RET
  ANA --> RET
  RET --> DEL[Approved deletion or archival action]
  DEL --> AUD[Deletion audit evidence]
```

Audio is provisionally retained for 30 days; transcripts and reports are provisionally retained for two years. These are not final policies. Retention, legal-hold, archival, backup, restoration, and deletion behaviour must be validated with privacy/legal, customers, and operations before production.

## 5. Processing boundaries and canonical event envelope

| Processing mode | Appropriate workloads |
|---|---|
| Synchronous | Device authentication outcome, emergency receipt, constrained guidance, user acknowledgement requests. |
| Event-driven | Alerts, telemetry, location, geofence, assignment, delivery, escalation, OTA, audit, notifications. |
| Batch/micro-batch | Reconciliation, quality checks, analytics, cost reporting, retention verification, model evaluation. |

All canonical events must include `event_id`, `schema_version`, `event_type`, `device_id` where applicable, `tenant_id`, `site_id`, `correlation_id`, `occurred_at`, `received_at`, producer identity, integrity/signature evidence or validation outcome, and a payload version. Consumers deduplicate on event ID, preserve source order when available, tolerate late events, and route invalid events to quarantine/dead letter with review evidence.

## 6. Storage zones and consumption

| Zone | Access pattern | Primary consumers |
|---|---|---|
| Ingress/quarantine | Restricted write and reviewer read. | Validation and security/data operations. |
| Raw evidence | Append/replay; tightly restricted. | Reconciliation, authorized investigation, retention control. |
| Cleansed operational | Event/state processing. | Control projections, lifecycle services, quality controls. |
| Curated control | Low-latency, role-scoped reads. | Control-room and authorized supervisor views. |
| Curated analytics | Governed aggregate/query access. | Product, operations, and commercial analysis. |
| Knowledge corpus | Approval-managed retrieval only. | RAG service through Sentinel API. |

## Open decisions and validation items

- Define delivery and acknowledgement semantics with the wearable vendor and control-room team.
- Validate field retry/backoff, duplicate, offline, clock, location precision, and cellular failure behaviour.
- Confirm the final retention, backup, legal-hold, and deletion obligations per data class.
- Confirm report-submission integration versus controlled manual export and required regulator formats.