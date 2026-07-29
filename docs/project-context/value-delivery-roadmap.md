# Sentinel Value Delivery Roadmap

**Status:** Strategic roadmap — dates and release gates require validation  
**Related strategy:** [Data, AI, and Device Platform Strategy](data-platform-strategy.md)  
**Time horizon:** Initial pilot target of approximately 12–16 weeks, subject to device, supplier, legal, security, and Azure readiness

## 1. Overview and phasing philosophy

Sentinel should be delivered as a sequence of working vertical slices, not as a long period of infrastructure-only work followed by a large release. Each phase must prove a real operational outcome for an officer, a control-room operator, or a property/agency stakeholder while strengthening the security, privacy, data, device, and AI foundation needed for the next phase.

The three-to-four-month target is achievable only if scope remains deliberately narrow, vendor wearable selection moves in parallel with cloud work, and decisions are made quickly. The primary schedule risks are device sourcing and security capabilities, SIM/commercial terms, cellular/GPS/battery validation, privacy/legal approval, and approval of the SOP corpus—not basic API development.

### Phasing principles

- **Value first:** Start with the high-value, low-complexity assurance slice: a provisioned device can invoke an approved emergency scenario and an authorized control-room user receives a traceable alert.
- **End-to-end:** Demonstrate the full path from wearable interaction through cellular connectivity, API validation, event capture, control-room visibility, and audit evidence.
- **Foundation early:** Build security, tenant/site boundaries, audit logging, monitoring, data quality, and privacy controls with the first slice.
- **Learn and adapt:** Use field pilots to measure actual cellular availability, GPS accuracy, battery behavior, user interaction, alert response, and AI usefulness before increasing scope.
- **Measurable progress:** Each phase has business-facing evidence, not merely technical completion. Metrics become pilot baselines before contractual targets are set.
- **Human control:** AI support and report drafting can reduce burden, but humans remain responsible for escalation and report approval.

## 2. Strategic phasing approach

The roadmap has four phases. Work within each phase can run in parallel, but a phase may not be declared complete until the end-to-end controls and acceptance evidence are available.

| Phase | Indicative timing | Main value outcome | Critical gate |
|---|---:|---|---|
| 0. Mobilise and de-risk | Weeks 1–2 | Confirm that a viable wearable, supplier, pilot, and cloud/security foundation exist. | NDA, device shortlist, Azure/legal path, pilot scope approved. |
| 1. Secure assurance vertical slice | Weeks 3–7 | A device sends an authenticated critical alert and the control room receives an auditable workflow. | Device-to-cloud and role-boundary field test passes. |
| 2. Guided operations and AI-assisted reporting | Weeks 8–11 | Officers receive approved guidance; authorized users retrieve cited SOP content and review report drafts. | AI safety, retrieval isolation, and human-approval evaluation pass. |
| 3. Pilot readiness and controlled rollout | Weeks 12–16 | A design partner can use the system under monitored operational controls. | Privacy, security, supplier, support, and rollout gates approved. |

The timeline is not a promise of production launch. Any failed safety, privacy, supplier, or operational gate pauses progression until the risk owner accepts a revised plan.

## 3. Phase definitions

### Phase 0: Mobilise and de-risk

**Strategic objectives:** Establish the smallest credible set of commercial, hardware, security, and delivery decisions needed to avoid building against an unvalidated device or operating model. Turn meeting decisions into a design-partner pilot charter and measurable assumptions.

**Key capabilities and work:**

- Finalize the pilot scope: target sites, officer/control-room roles, the five initial emergency scenarios, escalation expectations, and report workflow.
- Execute the agreed NDA before exchanging detailed operational intelligence and confirm retainer/project governance.
- Shortlist vendor wrist wearables against LTE/4G, GPS, basic camera/voice, 24-hour battery target, unit-cost constraint, secure identity, OTA support, and supplier continuity criteria.
- Confirm SIM commercial assumptions and test representative cellular coverage at prospective pilot sites.
- Confirm Azure subscription access, Singapore-region service availability, expected AI/search availability, environment model, identity approach, and Terraform delivery path.
- Start the DPIA/legal assessment, threat model, vendor security questionnaire, and initial data inventory.
- Identify the approved SOP corpus, its owners, update workflow, site metadata, and regulator report templates.
- Define initial metrics, event contracts, data classifications, retention assumptions, test strategy, and acceptance evidence.

**Business value and outcomes:** Sponsors receive an evidence-based go/no-go decision rather than a software prototype detached from hardware and compliance realities. The design partner sees a credible plan for assurance without committing to an unbounded product.

**Success criteria:**

- One or more wearable candidates meet the documented minimum technical criteria or gaps are explicitly accepted/mitigated.
- A pilot design partner, named stakeholders, candidate site(s), and safety escalation path are confirmed.
- Azure/Singapore service and account prerequisites are recorded, with any unavailable service identified before dependent build work begins.
- The initial SOP and report artifacts have owners and an approval path.
- The risk register has named owners for all High or Critical risks.

**Dependencies and prerequisites:** Commercial and NDA progress, vendor access, design-partner availability, Azure access, legal/security participation, and the ability to test cellular service.

**Strategic enablers:** Prevents hardware and policy surprises from surfacing after application work; provides the fixed boundaries needed for a focused vertical slice.

### Phase 1: Secure assurance vertical slice

**Strategic objectives:** Prove that Sentinel can securely connect a provisioned wearable to an authorized control-room workflow while recording trustworthy operational evidence.

**Key capabilities and work:**

- Register device, SIM, supplier, firmware, tenant, site, and officer assignment information.
- Provision device identity and establish encrypted cellular device-to-cloud transport with replay/duplicate handling.
- Deploy API ingress, request validation, tenant/site/role checks, event schema validation, audit logging, and operational monitoring.
- Implement emergency initiation and a minimum alert workflow for fire, medical emergency, intrusion, duress, and suspicious person/package.
- Deliver a basic control-room view for active alert, site/device context, acknowledgement, escalation, and assignment status.
- Capture GPS/location and geofence-policy events with accuracy/confidence indicators; do not treat a departure event as proof of misconduct.
- Establish separate development and staging environments, CI checks, infrastructure-as-code review, secrets handling, and access logging.
- Perform early device, API, integration, and hardware-in-loop tests.

**Business value and outcomes:** Stakeholders can observe a real wearable-to-control-room path rather than a conceptual demo. The first assurance evidence is available: device identity, assignment, event time, delivery/acknowledgement, and role-scoped operational visibility.

**Success criteria:**

- An authorized device can initiate each initial scenario in a controlled field test.
- The system rejects invalid device, tenant/site, scenario, or duplicated/replayed requests.
- An authorized control-room user receives and acknowledges a duress alert with timestamps and audit evidence.
- Supervisors cannot retrieve officer-to-device transcripts or other prohibited information in access-control tests.
- Monitoring identifies device connectivity, API failure, event-processing delay, and alert delivery failures.
- Baseline measures for cellular availability, device battery, GPS accuracy, alert delivery, and acknowledgement latency are captured.

**Dependencies and prerequisites:** Phase 0 pilot scope, candidate device with integration capability, SIM activation, control-room stakeholders, Azure foundation, and approved basic workflows.

**Strategic enablers:** Establishes reliable event contracts, identity boundaries, operations telemetry, and fleet records needed for AI, reporting, and multi-site onboarding.

### Phase 2: Guided operations and AI-assisted reporting

**Strategic objectives:** Add safe, controlled assistance to the verified operational path. Make the emergency guidance experience useful without replacing detailed SOPs or placing operational authority in the model.

**Key capabilities and work:**

- Configure approved, versioned critical guidance with three-to-six steps per scenario and clear escalation/acknowledgement behavior.
- Build SOP intake, document approval, classification, tenant/site metadata, and index-update audit records.
- Integrate Azure AI Search and Azure OpenAI behind application-level authorization and content guardrails.
- Enforce security-domain-only usage, off-topic refusal, tenant/site retrieval filters, citations, rate/abuse controls, and secret isolation.
- Implement incident-report drafting from approved templates with explicit human review, approval, revision, and submission states.
- Create AI evaluation suites for groundedness, citations, safe scenario answers, refusal behavior, prompt injection, cross-tenant/site isolation, response latency, and report-field completeness.
- Extend data quality and analytics for workflow completion, guidance version, retrieval outcome, model response, and report approval evidence.

**Business value and outcomes:** Officers receive rapid, consistent critical direction; authorized operations users can access relevant SOP knowledge with citations; report preparation becomes faster without eliminating human accountability.

**Success criteria:**

- Every guidance response in the MVP maps to an approved scenario and content version.
- Retrieval tests demonstrate tenant/site isolation and include citations for substantive answers.
- A test suite confirms refusal of personal, non-work, and prompt-injection attempts.
- A report cannot be submitted without an authorized human approval record.
- Design-partner review finds the guidance and report format operationally understandable and usable.

**Dependencies and prerequisites:** Secure vertical slice, approved SOP corpus, report template, access model, Azure AI/search availability, and named content owners.

**Strategic enablers:** Establishes content governance and AI quality controls that can support future sites without uncontrolled document or prompt growth.

### Phase 3: Pilot readiness and controlled rollout

**Strategic objectives:** Convert the prototype capabilities into a monitored, supportable pilot with explicit readiness gates and evidence for operational, privacy, security, and supplier stakeholders.

**Key capabilities and work:**

- Complete pilot device provisioning, site configuration, officer assignments, control-room training, support model, and runbook validation.
- Validate battery performance, cellular coverage, GPS behavior, device recycling, SIM lifecycle, firmware inventory, and OTA update/rollback process in representative conditions.
- Implement retention/deletion controls for the final approved policy, and test access, audit, backup/restore, and incident-response processes.
- Complete DPIA/privacy review, threat model, Azure configuration review, penetration test or appropriately scoped assessment, device supply-chain review, and OTA security review.
- Configure production-like monitoring, alerting, dashboarding, support ownership, on-call/escalation, and release controls.
- Execute a staged rollout with a small device cohort, predefined success measures, stop conditions, feedback loops, and rollback criteria.
- Prepare commercial evidence: device and SIM cost baseline, supplier continuity status, support effort, and measurable assurance outcomes for client-facing positioning.

**Business value and outcomes:** The design partner can assess Sentinel in operational use with known limitations and support paths. Sponsors gain data for go/no-go, pricing, supplier commitment, product refinement, and customer conversations.

**Success criteria:**

- Pilot-readiness checklist is approved by product, operations, security, privacy/legal, and device owners.
- All pilot devices have known identity, assignment, firmware, SIM association, and support status.
- Security, privacy, and device-release issues have documented disposition; unresolved High/Critical risks have an accepted mitigation or halt decision.
- The pilot reports baseline outcome metrics and qualitative feedback without exposing prohibited data.
- A controlled rollback/deactivation process is demonstrated.

**Dependencies and prerequisites:** Completion of Phases 0–2, supplier support availability, signed customer/design-partner arrangements, retention/legal decisions, and release-owner availability.

**Strategic enablers:** Produces the operational proof and cost data required to expand to additional sites or agencies without making untested claims.

## 4. Cross-phase dependencies and parallel workstreams

### Dependencies

- **Wearable selection gates Phase 1.** The candidate must support secure onboarding, the required interaction path, and diagnostics. A weak vendor SDK or lack of OTA/security features materially changes the product scope.
- **SOP ownership gates Phase 2.** AI retrieval cannot be validated without approved, classified content and named owners.
- **Privacy/legal decisions gate recording and retention.** No pilot should collect voice or location data beyond an approved purpose, policy, and notice/consent/legal basis.
- **Identity and tenant model gate every phase.** Retrofitting authorization after building control-room views or RAG is high risk.
- **Operational ownership gates Phase 3.** A control-room workflow needs named responsibilities for acknowledgement, escalation, support, device replacement, and reporting.

### Parallel workstreams

| Workstream | Starts | Runs through | Outcome |
|---|---|---|---|
| Device and supplier diligence | Phase 0 | Phase 3 | Selected wearable, continuity evidence, support and OTA readiness. |
| Data, identity, and infrastructure foundation | Phase 0 | Phase 2 | Secure event, storage, authorization, monitoring, and environment foundation. |
| Emergency workflow and control-room design | Phase 0 | Phase 2 | Validated scenarios, UI/operating rules, acceptance evidence. |
| AI/SOP content governance | Phase 0 | Phase 3 | Approved corpus, evaluation set, update process, report templates. |
| Privacy, security, and compliance | Phase 0 | Phase 3 | DPIA/threat model/review evidence, retention policy, release approval. |
| Commercial and pilot operations | Phase 0 | Phase 3 | SIM pricing, customer pilot charter, training, support, and outcome narrative. |

## 5. Value milestones

| Milestone | Indicative timing | Evidence | Stakeholder decision |
|---|---:|---|---|
| Pilot charter and wearable shortlist | End of Week 2 | Scope, risk owners, supplier scorecard, Azure/legal prerequisite record. | Continue, change scope, or halt. |
| First authenticated device event | Week 4 | Device-to-cloud event with identity, schema, and audit record. | Validate integration direction. |
| End-to-end emergency workflow demo | Weeks 5–7 | Controlled alert, control-room acknowledgement, role-boundary and monitoring evidence. | Approve guided-operation build. |
| RAG and report safety demonstration | Weeks 9–11 | Cited SOP answers, isolation/refusal tests, human report approval. | Approve pilot-readiness work. |
| Pilot readiness review | Weeks 12–14 | Security/privacy/device/support/rollback evidence and cohort plan. | Approve limited controlled rollout. |
| Pilot outcome review | Weeks 15–16 and ongoing | Metrics, field feedback, cost/supplier findings, risk update. | Expand, iterate, or stop. |

## 6. Roadmap governance

The product/venture lead owns the roadmap; the technical lead owns technical feasibility and release evidence; security/privacy owners own their approval gates; the hardware/edge owner owns device and OTA readiness; and the design partner validates workflows and business value. Review progress weekly during Phases 0–2 and at least twice weekly during pilot rollout preparation.

A phase is complete only when its business outcome and safety/security evidence are demonstrated. Schedule pressure must not bypass controls involving emergency escalation, tenant/site isolation, transcript access, voice/location handling, device identity, OTA updates, or report approval.
