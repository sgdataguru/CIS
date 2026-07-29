# Sentinel operations architecture

**Related:** [Component specifications](component-specifications.md), [Network security](network-security.md), [Data flows](../../../docs/architecture/data-flows.md), and [Risk register](../../../docs/project-context/risk-constraint-register.md).

## 1. Observability model

Observability must support safe operations, security investigation, pilot measurement, and audit evidence. Every signal includes environment, tenant/site where appropriate, device or workload identifier, correlation ID, event time, received time, software/firmware/configuration version, and privacy classification. Logs must not contain production secrets or unrestricted raw audio/transcripts.

| Domain | Required signals | Operational use |
|---|---|---|
| Device/fleet | Last seen, connectivity, battery, firmware, assignment, SIM state, OTA state, reset/deactivation. | Identify unavailable, stale, unsupported, or wrongly assigned devices. |
| Cellular and delivery | Send/receive outcomes, retry count, delayed/duplicate events, latency, delivery/acknowledgement state. | Diagnose alert reliability and field coverage limitations. |
| API and identity | Request volume, latency, errors, rate limits, device/user auth failures, authorization denials, replay/schema rejects. | Detect outages, abuse, misconfiguration, and policy failure. |
| Event/data | Queue depth, consumer lag, dead letters, replay, data-quality failures, retention/deletion job outcomes. | Protect alert processing, audit integrity, and data lifecycle. |
| Control room | Alert creation, display, acknowledgement, escalation, assignment changes, privileged views. | Review operational response and ownership. |
| AI/RAG | Retrieval filters/outcomes, citations, latency, token/cost use, refusals, safety failures, evaluation results. | Detect isolation, quality, performance, and cost regressions. |
| Security | Privileged changes, key/certificate events, network policy changes, suspicious requests, SIEM alerts. | Investigate and contain security events. |

## 2. Alerting, ownership, and drills

Define alert severity by risk to safety, security, service integrity, or data lifecycle. The exact SLOs, response times, on-call coverage, escalation timers, and notification channels require validation with the design partner and operations owner.

- **Critical:** loss or suspected compromise of device identity; unprocessed duress/emergency alert; cross-tenant data exposure; failed mandatory security control; unauthorized OTA; material retention/deletion failure affecting regulated data.
- **High:** sustained API/event failure, control-room visibility failure, widespread device connectivity/battery issue, AI retrieval isolation failure, or unapproved corpus change.
- **Medium:** individual device/sim degradation, elevated retries, GPS confidence issue, latency trend, model refusal/citation regression, or failed non-critical job.
- **Low:** capacity trend, configuration drift warning, documentation/metadata gap, or planned maintenance issue.

Every alert needs an owner, runbook, evidence source, escalation destination, and closure criteria. Exercise emergency-alert delivery, device compromise/revocation, tenant-access denial, cloud dependency failure, OTA rollback, backup/restore, and retention/deletion failure before pilot readiness. Drills must produce findings and tracked remediations.

## 3. Resilience, recovery, and data protection

The architecture favors durable events and rebuildable projections. If a control read model fails, it can be reconstructed from validated event evidence; if a downstream notification fails, delivery state and retry/escalation remain visible. Consumers are idempotent, preserve correlation, handle late events, and use dead-letter/quarantine flows rather than discarding invalid data.

Backups, point-in-time restore, object versioning, event retention, geographical resilience, RPO/RTO, and failover options depend on selected Azure services and must be defined per data class. Test restores without bypassing tenant/site authorization or retention controls. Legal holds, approved deletion, backup expiry, and restoration must be consistent; a restored dataset must not reintroduce data that has been permanently deleted under the approved policy.

For a device incident, operations can deactivate the device, revoke credentials, suspend its SIM/assignment where integrated, preserve permitted evidence, issue a replacement, and verify reset/wipe before recycling. The actual remote-wipe and recovery steps depend on vendor capability and must be field-tested.

## 4. Delivery, infrastructure, and release controls

Use GitHub Actions for CI/CD and Terraform for infrastructure. Workflows use federated cloud identity with environment-specific permissions; static Azure client secrets and broad subscription credentials are not an acceptable target design. Development, staging, and production use separate identities, configuration, telemetry, secrets, approval gates, and deployment evidence.

Required controls:

- Branch protection, pull-request review, code ownership for security/infra/AI/device changes, and reproducible builds.
- Linting, unit/integration/end-to-end tests, API contract tests, event-schema compatibility tests, data-quality tests, and hardware-in-loop tests for device interaction.
- Secret scanning, SAST, dependency/vulnerability scanning, license checks, container scanning where applicable, infrastructure scanning, and Terraform plan review.
- AI evaluation regression for corpus, retrieval filter, prompt, model/deployment, and report-template changes.
- Staging validation, production approval by relevant product/security/privacy/operations owners, smoke checks, monitored rollout, and documented rollback.

Existing workflow files must be aligned to Sentinel before use. Any legacy Databricks-specific deployment or static `AZURE_CREDENTIALS`/client-secret pattern is not a valid production delivery mechanism for this architecture and must be replaced after federated identity and target services are confirmed.

## 5. Device and OTA operations

An OTA release begins with signed artifact provenance, vulnerability review, test evidence, hardware-in-loop validation, compatibility checks, an approved target cohort, and a documented rollback image/procedure. Roll out in stages, monitor device health, battery, connectivity, firmware version, crashes, and critical workflow success, and stop automatically or manually when validated thresholds are exceeded. Thresholds and emergency communications ownership require definition.

Device fleet operations include inventory reconciliation, assignment change review, SIM lifecycle reconciliation, firmware compliance, physical-loss process, replacement handling, periodic reset/wipe verification, and supplier support escalation. No device release is promoted based solely on simulated testing.

## 6. Cost and performance management

Major cost drivers are devices and replacements, SIM plans, field data transfer, GPS sampling, API/event throughput, raw/audio/document retention, operational stores, analytics compute, search capacity, AI tokens, log/SIEM volume, private connectivity, and support staffing. Optimize through measured sampling, event payload limits, data lifecycle tiers, retention minimisation, aggregation, log filtering with retained security evidence, query budgets, model/token budgets, cached approved fixed guidance, staged OTA, and rightsizing.

Performance tuning prioritises emergency event acceptance, durable persistence, control-room state freshness, authorization latency, and safe fallback over non-critical analytics or AI response time. Capacity planning must use measured pilot load, not assumptions based on a mobile consumer application.

## 7. Open decisions and validation items

- Define SLOs, alert thresholds, on-call coverage, control-room escalation timers, support hours, and operational runbooks.
- Select backup/DR capabilities and set validated RPO/RTO per selected Azure service and data class.
- Confirm final federated GitHub-to-Azure identity configuration, Terraform state backend, environment gates, and scanning toolchain.
- Replace or retire legacy CI/CD workflows that assume Databricks or static Azure credentials.
- Define OTA stop/rollback thresholds, supplier escalation commitments, device replacement process, and pilot support staffing.
- Validate monitoring/SIEM data residency, retention, access, cost, and alert-routing requirements.
