# CI/CD operations

## Branching

Use trunk-based development with short-lived branches and pull requests to `main`. Every pull request requires automated checks and review.

## Checks

- Python linting and tests
- Terraform formatting and later validate/plan checks
- Secret scanning, dependency scanning, SAST, container/IaC scanning, and license scanning before pilot
- AI evaluation and retrieval-isolation tests for changes to prompts, models, or SOP content
- Firmware signing and device test evidence for OTA releases

## Deployment

Development deploys automatically only after baseline controls are approved. Staging and production require environment approvals, federated Azure identity, deployment evidence, monitoring checks, and rollback readiness.
