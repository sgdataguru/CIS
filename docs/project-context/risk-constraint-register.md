# Sentinel Risk and Constraint Register

**Status:** Strategic baseline — review weekly during build and before every pilot gate  
**Related strategy:** [Data, AI, and Device Platform Strategy](data-platform-strategy.md)  
**Related roadmap:** [Value Delivery Roadmap](value-delivery-roadmap.md)

## 1. Overview

This register records the material risks, assumptions, and constraints for Sentinel’s data, AI, connected-device, and control-room platform. It is a working decision tool rather than a compliance assertion. Risk owners must validate ratings with evidence, update mitigations when facts change, and escalate conditions that can make the pilot unsafe, non-compliant, commercially unviable, or unable to meet its core assurance proposition.

The highest-risk areas are wearable supplier/device capability, cellular and GPS performance, privacy and data handling, tenant/site access isolation, AI safety and retrieval quality, and the compressed rollout target. The roadmap requires these to be treated as delivery gates, not as post-pilot enhancements.

## 2. Risk register

| Risk ID | Risk description | Likelihood | Impact | Mitigation strategy | Owner role | Phase affected |
|---|---|---|---|---|---|---|
| R-001 | Selected wearable cannot support secure identity, required LTE/4G/GPS behavior, voice/basic camera interaction, telemetry, or OTA controls. | Medium | Critical | Use a scored vendor shortlist; validate SDK, security model, diagnostics, lifecycle APIs, battery, and OTA capability before commitment; maintain an alternative supplier. | Hardware/edge lead | 0–3 |
| R-002 | Supplier cannot meet the three-to-four-year continuity expectation, quality standards, or security/supply-chain evidence. | Medium | High | Perform supplier diligence, reference checks, manufacturing-capacity review, contractual continuity terms, spare/replacement plan, and component/EOL disclosure. | Hardware/edge lead | 0–3 |
| R-003 | Device unit cost, SIM cost, support cost, or replacement rate makes the subscription model unviable. | Medium | High | Set total-cost model early; negotiate 400+ SIM pricing; field-test battery and failure rates; keep device features within MVP scope; compare vendor options. | Commercial lead | 0–3 |
| R-004 | Cellular coverage, latency, or outages prevent timely alert delivery at pilot sites. | Medium | Critical | Conduct site surveys and live tests; record connectivity status; use idempotent retries, delivery acknowledgements, escalation policies, and defined offline limitations; do not promise connectivity where it is not measured. | Edge/operations lead | 0–3 |
| R-005 | GPS accuracy or indoor conditions cause false geofence departure events and inappropriate operational conclusions. | High | High | Capture confidence/accuracy; make geofence events advisory; calibrate per site; require human/contextual review; document the policy and avoid automated disciplinary action. | Product/operations lead | 1–3 |
| R-006 | Battery life is below the 24-hour target under cellular, GPS, voice, and screen use. | Medium | High | Profile representative workload; configure sampling and transmission rates; test charging behavior; define replacement/charging process; select hardware using measured, not vendor-claimed, results. | Hardware/edge lead | 0–3 |
| R-007 | Device reassignment or recycling exposes prior officer, tenant, or site data. | Medium | Critical | Enforce deactivation, key/token revocation, encrypted storage, reset/wipe evidence, assignment state checks, and post-reset verification before reassignment. | Security and edge leads | 1–3 |
| R-008 | Unauthorized users obtain cross-tenant/site data or supervisors access officer-to-device transcripts. | Medium | Critical | Implement policy enforcement at API and retrieval layers; use least-privilege roles; include automated authorization tests; audit access; perform penetration testing before production. | Security lead | 1–3 |
| R-009 | Voice/location collection, retention, notices, access handling, or deletion practices are not compliant with PDPA or contractual obligations. | Medium | Critical | Complete DPIA and legal review before collection; confirm lawful purpose and notification/consent or other legal basis; minimise data; automate approved retention/deletion; maintain access/audit procedures. | Privacy/legal lead | 0–3 |
| R-010 | Azure Singapore service, model, quota, networking, or data-processing availability does not meet technical or residency requirements. | Medium | High | Verify service availability, contract terms, data processing location, quotas, private connectivity, support model, and fallback design before dependent commitments. | Cloud lead | 0–2 |
| R-011 | Azure OpenAI produces hallucinated, unsafe, uncited, or off-domain security guidance. | Medium | Critical | Use approved scenario guidance for critical steps; require RAG citations for substantive answers; test groundedness and refusals; constrain scope; use human escalation; never allow autonomous commands. | AI safety lead | 2–3 |
| R-012 | RAG retrieval leaks a different tenant/site’s SOP content or confidential material. | Low | Critical | Enforce pre-retrieval authorization and metadata filters; test isolation with adversarial cases; review document ingestion; segregate indexes/data where risk justifies it; log retrieval decisions. | AI and security leads | 2–3 |
| R-013 | Prompt injection or malicious SOP content causes policy bypass, data disclosure, or unsafe output. | Medium | High | Treat retrieved content as untrusted; use prompt-injection tests; constrain tools/actions; validate source approval; redact secrets; enforce output and access policies outside the model. | AI safety lead | 2–3 |
| R-014 | Report drafts omit facts, introduce errors, or are submitted without authorized human review. | Medium | High | Use approved templates, source/citation context, completeness checks, explicit approval state, named approver audit, and user training; block automated submission. | Product/operations lead | 2–3 |
| R-015 | Emergency guidance is incomplete, wrong for a site, or misunderstood under stress. | Medium | Critical | Have security operations and design-partner stakeholders approve scenario steps; version content; test usability and drills; display guidance as concise actions; route uncertainty to control room/emergency services. | Product and operations leads | 0–3 |
| R-016 | Event duplicates, late events, schema changes, or clock drift corrupt alert, audit, or reporting state. | Medium | High | Use immutable event IDs, schema versioning, idempotent consumers, received/occurred timestamps, dead-letter/quarantine workflows, and reconciliation jobs. | Data platform lead | 1–3 |
| R-017 | Loss of raw evidence or overly aggressive retention prevents investigation; excessive retention increases privacy exposure. | Medium | High | Confirm final retention schedule; apply lifecycle rules and legal holds where approved; test deletion and restore; retain provenance, policies, and audit records; review policy changes. | Privacy and data leads | 1–3 |
| R-018 | Monitoring fails to reveal device outages, alert backlog, access anomalies, model errors, or retention-job failure. | Medium | High | Define SLIs/SLOs and alerts for connectivity, event lag, delivery, acknowledgement, authorization failure, AI refusals/errors, storage lifecycle, and OTA outcome; conduct operational drills. | SRE/operations lead | 1–3 |
| R-019 | The three-to-four-month target causes critical security, privacy, hardware, or testing work to be skipped. | High | Critical | Use gated phases; maintain a minimum viable pilot scope; publish stop criteria; assign owners; defer non-essential features; escalate gate failures rather than absorbing them silently. | Venture/product lead | 0–3 |
| R-020 | Team lacks skills in connected-device security, Azure AI safety, data engineering, or operational control-room design. | Medium | High | Identify skill gaps in Phase 0; retain specialists; use vendor support; pair implementation with review; create targeted test plans and documentation. | Technical lead | 0–3 |
| R-021 | Control-room roles, escalation ownership, or user training are unclear, leading to missed or mishandled alerts. | Medium | Critical | Define RACI, escalation timers, shift handover, training, drills, support processes, and audit review; demonstrate flows with the design partner before pilot. | Operations lead | 0–3 |
| R-022 | Commercial claims exceed what the platform or pilot evidence can demonstrate. | Medium | High | Align sales messaging to measured outcomes; label pilot results and limitations; avoid claims about compliance, detection, or officer behavior not supported by evidence. | Commercial and product leads | 2–3 |
| R-023 | Vendor lock-in to device SDKs, Azure AI/search, or proprietary event formats raises migration cost. | Medium | Medium | Use documented domain contracts, portable event schemas, infrastructure as code, exportable data, provider adapters, and periodic option reviews; avoid premature multi-cloud implementation. | Technical lead | 1–3 |
| R-024 | Unauthorized OTA update, failed rollout, or inability to roll back disrupts deployed devices. | Low | Critical | Require signed packages, provenance, staged cohorts, approval, health monitoring, tested rollback, release audit, and hardware-in-loop evidence. | Hardware/edge and security leads | 1–3 |
| R-025 | Source SOPs become outdated, contradictory, unapproved, or semantically drift from site operations. | Medium | High | Establish content ownership, approval, validity dates, versioning, review cadence, withdrawal process, and retrieval evaluation after corpus changes. | Content/operations lead | 0–3 |

## 3. Assumptions

The following assumptions must be validated or replaced with decisions. An assumption is not approval to proceed without evidence.

- **A-001:** A design partner can provide named stakeholders, candidate pilot sites, control-room participation, and timely workflow feedback.
- **A-002:** A vendor wrist wearable meeting the LTE/4G, GPS, basic camera/voice, secure identity, OTA, battery, and cost requirements is available from a viable India or Shenzhen supplier.
- **A-003:** Cellular service can be procured at acceptable commercial terms and provides adequate coverage at selected pilot sites.
- **A-004:** The initial five scenarios—fire, medical emergency, intrusion, duress, and suspicious person/package—are sufficient to prove the MVP’s operational value.
- **A-005:** Detailed SOPs and regulator report formats can be supplied, classified, approved, and maintained by accountable content owners.
- **A-006:** Azure services required for the validated architecture are available in, or meet the agreed processing/residency requirements for, the Singapore deployment model.
- **A-007:** The project can obtain Azure subscription permissions, identity integration decisions, and network/security review support in Phase 0.
- **A-008:** A human control-room/report-review process exists and can own alert acknowledgement, escalation, and final report approval.
- **A-009:** The venture can access data, hardware, AI safety, cloud, security, privacy/legal, and operations expertise for the required reviews.
- **A-010:** The provisional retention policy—audio for 30 days and transcripts/reports for two years—will be confirmed, amended, or replaced before production collection.
- **A-011:** Device-vendor documentation permits the integration, monitoring, and security testing needed for a managed fleet.
- **A-012:** Customer contracts and operational policies will define how GPS/geofence signals may be used and prohibit unsupported inferences about officer conduct.

## 4. Constraints

These are known boundaries shaping the strategic options.

- **C-001:** The solution is a wrist-worn wearable ecosystem, not an app-only product.
- **C-002:** Devices use cellular SIM connectivity; Wi-Fi cannot be assumed at security sites.
- **C-003:** GPS is required for location and site-departure events; it must be treated with accuracy and contextual limitations.
- **C-004:** The device camera is basic and is not a high-spec video analytics platform.
- **C-005:** Preferred unit cost is SGD 20–30 with a hard ceiling of SGD 100, limiting custom hardware and on-device compute choices.
- **C-006:** Device production/prototyping is expected from India or Shenzhen, with a desired three-to-four-year supplier continuity commitment.
- **C-007:** The initial rollout ambition is three to four months; this is a planning constraint, not a reason to bypass safety/security/privacy gates.
- **C-008:** The platform is Singapore-hosted on Azure subject to service, contractual, and data-processing verification.
- **C-009:** Infrastructure is defined with Terraform and delivered through GitHub Actions using trunk-based development.
- **C-010:** AI use is limited to approved security-domain assistance, SOP retrieval, and report drafting. Personal, non-work, and off-topic usage is blocked.
- **C-011:** Supervisors may access authorized site-level information but must not access officer-to-device transcripts.
- **C-012:** AI cannot autonomously submit incident reports or command devices; authorized humans retain decision authority.
- **C-013:** Production secrets, client data, audio, device keys, and SIM information must not enter source control.

## 5. Risk monitoring and review

### Cadence and ownership

- Review the register weekly during Phases 0–2 and at least twice weekly during pilot readiness and rollout.
- The venture/product lead owns the overall register; each listed owner updates evidence and mitigation status.
- Hardware, cloud, AI safety, privacy/legal, security, data, and operations leads must attend reviews when their High or Critical risks are open.

### Escalation

Escalate immediately to venture sponsors and the pilot decision group when a Critical risk materializes, when a High risk has no credible mitigation by its required phase gate, or when a control involving emergency response, privacy, tenant isolation, device identity, OTA, or human report approval fails. The decision group must explicitly choose to remediate, reduce scope, defer the affected feature, change supplier/architecture, or halt the pilot.

### Risk retirement criteria

A risk can be reduced or retired only with objective evidence: approved documentation, field-test results, security-test results, legal/privacy sign-off where required, supplier commitments, successful operational drills, automated test results, or production-like monitoring evidence. A statement that a feature is implemented is not sufficient evidence that the associated risk is controlled.
