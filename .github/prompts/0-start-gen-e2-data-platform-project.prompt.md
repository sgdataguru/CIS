---
description: Start a new Gen-e2 Data, AI, and Hardware platform project.
stage: Development
subcategory: subcategory-development-common
rule_name: start-gen-e2-data-ai-hardware-platform-project
rule_version: latest
---

We are starting a new Gen-e2 project that combines data engineering, AI/ML capabilities, and hardware or edge-device integration. Establish the project foundations only after gathering the requirements below.

## Discovery questions

Ask the following questions before creating files or installing dependencies.

## Questions to Ask
1. **Product requirements and features**
   - What outcomes, users, and core features should the platform support?
   - Which data, AI, and hardware capabilities are in scope for the initial release?
   - Are there compliance, security, privacy, safety, reliability, latency, or availability requirements?

2. **Data platform**
   - How will data enter the platform: streaming, batch, or both?
   - What are the data sources, formats, expected volumes, retention requirements, and connection methods?
   - What are the requirements for data quality, lineage, cataloging, access control, governance, and lifecycle management?

3. **AI and ML**
   - Which AI use cases, models, and inference or training workflows are required?
   - Will models use cloud, edge, or hybrid inference? What are the accuracy, latency, explainability, evaluation, and monitoring requirements?
   - What data-labeling, experiment tracking, model registry, human-review, and MLOps requirements apply?

4. **Hardware and edge integration**
   - Which devices, sensors, actuators, gateways, and communication protocols will be supported?
   - What are the device provisioning, authentication, firmware update, telemetry, offline-operation, safety, and fleet-management requirements?
   - Are there hardware constraints such as CPU, memory, power, network bandwidth, real-time deadlines, or supported operating systems?

5. **Infrastructure and delivery**
   - Which cloud provider, regions, and target environments will be used?
   - What is the target architecture, including edge-to-cloud boundaries and data-flow requirements?
   - Should infrastructure files be created? If so, which format should be used (for example Terraform, CloudFormation, or Bicep)?
   - Which CI/CD service, source-control workflow, secrets-management system, and deployment approach are preferred?

## Actions Based on Answers
1. **Design the project structure**
   - Adapt the following base structure to the agreed data, AI, hardware, and infrastructure requirements. Do not create directories that do not serve an identified need.
```
.
├── README.md -- Describe the project and project goals
├── CONTRIBUTING.md
├── requirements.txt -- Python dependencies, when Python is used
├── docker-compose.yml -- Local development environment
├── scripts/ -- Contains scripts to manage the project
│   ├── manage.sh -- Manages servers and services (start,stop,status)
│   ├── setup.sh -- Installs project dependencies
├── docs/ -- Contains project documentation
│   ├── admin/ -- Documentation regarding permissions required and granted for different services
│   ├── architecture/ -- Architecture diagrams & docs
│   ├── features/ -- Contains documentation for project features (one file per feature)
│   ├── infra/ -- Contains an overview of the project
│   ├── project-context/ -- Contains an overview of the project
│   ├── index.md -- Main documentation file, indexing all other documentation
│   └── CONTRIBUTE.md -- Describes the project structure and best practices for contributions
├── data/ -- Contains all definitions of the data
│   ├── schemas/ -- Data schemas (JSON Schema, Avro, etc.)
│   ├── sample-data/ -- Sample datasets for testing
│   └── migrations/ -- Database migrations
├── src/ -- Application and platform source code
│   ├── notebooks/ -- Contains data processing that is performed in notebooks
│   ├── pipelines/ -- Contains scripts for data pipelines
│   ├── serverless/ -- Contains data processing scripts for serverless execution (e.g. Lambda, Functions)
│   ├── ai/ -- Model training, inference, evaluation, and MLOps code
│   ├── edge/ -- Device agents, protocol adapters, and edge inference code
│   └── shared/ -- Shared libraries and domain contracts
├── hardware/ -- Hardware designs, firmware, device configuration, and protocol specifications
│   ├── firmware/
│   ├── device-config/
│   └── docs/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── infra/ -- Contains infrastructure code <refer to `terraform-cloud.instructions.md` for nested structure>
└── DevOps/
    ├── pipeline/
    └── docs/
```
   - Update `README.md`, `docs/index.md`, and the documents in `infra/docs/` with the agreed requirements, architecture, assumptions, and decisions.

2. **Create `TODO.md`**
   - Divide tasks by relevant domains, such as data platform, AI/ML, hardware/firmware, edge, infrastructure, DevOps, security, quality, and documentation.
   - Keep tasks specific enough to complete in a few hours, identify owners where known, and include non-development work.
   - Format:
     ```
     ## Domain
     [ ] Task to be done (owner)
     ```
   - Include tasks to review every generated architecture, API, data-contract, device, and operational document, then update it as implementation evolves.

3. **Documentation and architecture**
   - Propose and create a PlantUML architecture diagram in `infra/docs/` that shows devices and sensors, edge gateways, data ingestion, storage and processing, AI training and inference, operations, security boundaries, and external integrations.
   - Create one document per agreed feature in `docs/features/`, covering its scope, interfaces, data contracts, AI behavior where relevant, hardware dependencies, security, and acceptance criteria.

4. **Tools, dependencies, and local development**
   - Recommend appropriate tools for data storage and processing, model development and MLOps, device communication and fleet management, observability, testing, CI/CD, and security scanning.
   - Create necessary repository files such as `.gitignore`, `.gitattributes`, environment templates, and language-specific manifests.
   - Where Python is selected, recommend and create a virtual environment, then install only the agreed dependencies. Apply the same principle to other language ecosystems.

5. **Infrastructure**
   - Based on the selected approach, create the required infrastructure-as-code in `infra/`, including environment separation, identity and access controls, networking, compute, storage, secrets integration, monitoring, and edge/device services as applicable.

6. **Version control and CI/CD**
   - Initialize Git and create an initial commit only after the user explicitly approves the proposed project name and creation.
   - Set up the selected CI/CD pipeline in `DevOps/pipeline/`, including build, tests, linting, dependency and vulnerability scanning, artifact handling, and environment-aware deployment gates.
   - Document the delivery pipeline in `DevOps/docs/`.

7. **Testing, quality, and security**
   - Establish unit, integration, end-to-end, data-quality, model-evaluation, device/firmware, and hardware-in-the-loop testing as appropriate.
   - Configure code formatting, linting, type checking, and dependency/license checks appropriate to each language.
   - Document environment-variable and secrets-handling practices; never commit secrets or production credentials.
   - Include security and safety practices for cloud resources, data access, models, devices, firmware, OTA updates, supply chain, and vulnerability scanning.

8. **Deployment and operations**
   - Provide deployment guidance for development, staging, and production, including model rollout and rollback, device-fleet rollout strategy, observability, alerting, incident response, backups, and disaster recovery.

## Final Steps

1. Suggest a concise project name that reflects the Data, AI, and Hardware scope. Ask for approval before creating the project.
2. After creation, review ignore rules for generated artifacts, virtual environments, language dependencies, model artifacts, datasets, logs, firmware build outputs, device credentials, and local secrets.
3. Verify that all agreed files and directories have been created and that documentation links are valid.
4. Install dependencies from the selected manifests and configure the local development environment, including `docker-compose.yml` when applicable.