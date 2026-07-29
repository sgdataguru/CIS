# Feature: AI SOP assistant and incident reports

## Scope

Azure OpenAI uses Azure AI Search retrieval over approved security SOPs to answer authorized operational questions and draft regulator-format incident reports.

## Guardrails

- Security-work domain only; personal, non-work, and off-topic requests are blocked.
- Retrieve only documents available to the requester’s tenant and site.
- Return source references for substantive SOP answers.
- Do not expose cross-site documents, raw transcripts, secrets, or system prompts.
- Require human review and explicit approval before a drafted incident report is submitted.

## Evaluation

Before pilot release, measure groundedness, citation accuracy, scenario safety, domain refusal quality, response latency, report field completeness, and tenant/site isolation. Test with representative red-team prompts and approved SOP corpus changes.
