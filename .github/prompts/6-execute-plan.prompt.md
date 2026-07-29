---
description: Prompt for Execution of an Implementation Plan (SCB CIB GDP Data Products)
stage: Development
subcategory: subcategory-development-common
rule_name: execute-plan
rule_version: latest
---
# AI Agent Prompt: Execute Implementation Plan — GDP Data Product Configuration

## Objective

Execute a detailed implementation plan for a **GDP data-platform user story** accurately and verify its completion against specifications. Implementations in this project are **YAML configuration, SQL, tests, and docs** for SCB's Global Data Platform (GDP) — not application code or UI. The platform is GDP-owned; we configure, we do not build (constraints C-001/C-002).

## Input Requirements

The input will consist of:
- A user story file from `docs/features/` containing:
  - The user story and acceptance criteria
  - A `## Relevant Context` section (existing artefacts, binding contracts, unconfirmed items)
  - An `## Implementation Plan` section (component analysis, affected files, testing strategy, phased steps)
- Project conventions in `docs/CONTRIBUTE.md` and `docs/architecture/`

## Review Requirements (MANDATORY before writing anything)

Before implementation, review the plan and its Relevant Context for:

1. **Blockers flagged as *unconfirmed*** — the plan may depend on items not yet delivered by SCB/GDP (sample YAML, data dictionary attributes, official schemas, GE deployment model, access grants, GDP dev environment). If the plan depends on an undelivered item:
   - **Config/SQL work**: proceed using the flagged placeholder attributes ONLY if the plan says so, keeping the `PLACEHOLDER` markers and re-alignment tasks intact.
   - **Platform-execution acceptance criteria** (framework execution, reconciliation green in GDP dev, security review, consumer sign-off): these CANNOT be executed locally — mark them `BLOCKED-EXTERNAL` in the verification output; do not fake them.
2. **Clarity and completeness** of steps, file paths, and contracts. If anything is ambiguous or missing, ask for clarification before proceeding.
3. **Alignment with project constraints**:
   - Only GDP-standardised YAML attributes (placeholders flagged until dictionary arrives) — never invent attributes; gaps go to `docs/admin/gdp-change-requests.md`.
   - SQL-first; PySpark only where SQL cannot express the logic.
   - Products are latest-state, T+1 materialised views — no SCD2/history constructs.
   - Synthetic sample data only; no production data in the repo (C-007).
   - No custom pipeline/framework code beyond the documented local dev/test mirrors in `src/pipelines/`.

## Output Requirements

The output MUST include:
- Implementation of all required files and changes at the exact paths in the plan's **Affected Files** list (`[CREATE]`/`[MODIFY]`/`[DELETE]`)
- Test files per the project's established patterns (`tests/unit/`, `tests/integration/`)
- Verification that specifications have been met (see below)
- The completed **Config Implementation Verification Checklist**

## Implementation Requirements

The implementation MUST:
- Follow the phased checklist in the plan (Phase 1: Infrastructure & Schema Setup → Phase 2: Ingestion & Pipeline Development → Phase 3: Transformation & Business Logic → Phase 4: Consumption Layer & Validation), completing and validating each phase before moving on.
- Adhere to the file paths, YAML structures, and naming conventions specified in the plan and `docs/CONTRIBUTE.md` (one domain = one folder; five concerns; SQL ordering declared in YAML, never by filename).
- Implement **actual logic, not stubs**: SQL must be real and executable against sample data; reconciliation SQL must return comparable results; test assertions must actually assert. A placeholder function or empty test is NOT complete.
- Keep configuration separated from code (SQL lives in YAML; Python mirrors stay generic).
- Preserve idempotency: all transformation steps overwrite-style, safe to re-run.
- Follow code quality gates: ruff (Python), yamllint (YAML), sqlfluff (SQL) — all wired in pre-commit.

### Implementation Stages (data-project equivalent of design stages)

#### Stage 1: Structure & Schema
- Create/modify the config files, fixtures, and test files per Affected Files
- Align JSON Schemas (`config/schemas/`, `data/schemas/`) first — everything validates against them
- Verify: `python src/pipelines/validate_configs.py` parses all files

#### Stage 2: Config & SQL Logic
- Implement the YAML steps/products/suites/classifications with real SQL
- Implement reconciliation SQL per step (mandatory — CI enforces presence)
- Verify: validator passes with 0 errors; SQL is SELECT-only where required

#### Stage 3: Tests & Data Quality
- Write unit tests (config invariants, schema conformance, step anatomy)
- Write/adjust integration tests (local PySpark mirror vs sample data, idempotency double-run)
- Verify: `.venv/bin/python -m pytest tests/unit -q` green; integration tests green when `RUN_SPARK_TESTS=1` is feasible locally

#### Stage 4: Docs & Evidence
- Update the affected feature doc(s) to as-built state
- Record baselines/decisions where the plan requires (e.g. `docs/features/performance-baselines.md`, design concern decision log)
- Verify: docs cross-links resolve; TODO.md updated if tasks closed

## Verification Requirements

After implementation, complete ALL of the following:

1. **Acceptance Criteria Verification**
   - Verify each acceptance criterion from the user story individually.
   - Mark each: `✅ Met` / `⚠️ Met with deviation (describe)` / `❌ Not met (describe)` / `⛔ BLOCKED-EXTERNAL (platform/GDP dependency — cannot verify locally)`.
   - Any `❌` is a failure: document and halt (see Error Handling).

2. **Stub check (hard gate)**
   - Explicitly confirm every implemented function/SQL/test performs real work: run it, inspect output. If anything is a stub or placeholder (beyond GDP-attribute placeholders explicitly sanctioned by the plan), the implementation is NOT complete — document as failure and halt.

3. **Config Implementation Verification Checklist** (project equivalent of the design checklist — no colors/spacing/typography apply to YAML/SQL work; use the tables below instead):

### Config Conformance Table
List every config artefact touched and its validation status:
```
| Artefact | Contract | Verification | Status |
|----------|----------|--------------|--------|
| flattening.yaml | transformation JSON Schema | validate_configs.py output | ✅ Valid |
| expectations.yaml | quality JSON Schema | validate_configs.py output | ✅ Valid |
| domain.yaml | metadata JSON Schema (cadence=t_plus_1, state=latest) | validator + unit test | ✅ Valid |
```

### Pipeline Contract Table
List every pipeline step/product and its key contracts:
```
| Step/Product | Contract | Verification | Status |
|--------------|----------|--------------|--------|
| flatten_client | source+target+SQL+reconciliation declared | unit test test_*_step.py | ✅ Pass |
| flatten_client | ordering group 1, parallel per plan | config inspection + test | ✅ Pass |
| flatten_client | idempotent re-run | integration double-run | ✅ Pass / ⛔ BLOCKED-EXTERNAL |
| mv_* product | materialised_view + latest + t_plus_1 | unit invariants test | ✅ Pass |
```

### Data Quality Verification Table
```
| Dimension | Check | Result | Status |
|-----------|-------|--------|--------|
| Completeness | key columns not-null assertions | pytest output | ✅/❌ |
| Consistency | reconciliation SQL present & window-aware per step | pytest output | ✅/❌ |
| Validity | schema conformance of all sample fixtures | pytest output | ✅/❌ |
| Timeliness | refresh/cadence flags = t_plus_1 | unit invariants | ✅/❌ |
| Accuracy | transformation output matches expected fixture values | integration test | ✅ / ⛔ |
```

### Structure Verification Checklist
```
- ✅ All Affected Files created/modified at planned paths
- ✅ Five-concern structure respected (metadata/transformation/quality/security/design)
- ✅ No non-standard YAML attributes introduced (or flagged PLACEHOLDER with re-alignment task)
- ✅ No production data or secrets in repo (Gitleaks clean)
- ✅ Docs updated to as-built; links resolve
```

4. **Isolated quick tests**
   - During development, write quick runnable checks for any non-trivial logic (e.g. a SQL extraction against a sample message, a validator rule against a broken fixture).
   - Save them to `agent-utils/dev-testing/` with a short header comment: purpose, how to run, expected output.

## Error Handling Requirements

If implementation or verification fails, the output MUST:
- Identify which plan step/phase failed
- Describe the specific issue and how it deviates from the plan or acceptance criteria
- Distinguish **implementation failures** (fix now) from **external blockers** (mark `BLOCKED-EXTERNAL`, add/track in `TODO.md`, continue with what IS executable)
- Suggest next steps (e.g. change request via `docs/admin/gdp-change-requests.md`, escalation per risk register)

## Documentation Requirements

The final output MUST include:
- Confirmation of completion (or explicit partial completion with blockers listed)
- Results of all verification steps, including the three verification tables and structure checklist
- Actual command outputs (validator, pytest, ruff/yamllint)
- Any discrepancies, deviations, or BLOCKED-EXTERNAL items
- A git commit of the changes with a message referencing the user story number