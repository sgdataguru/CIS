# Sentinel delivery pipeline

GitHub Actions validates pull requests and `main` with Python linting, tests, and Terraform formatting. Add dependency, secret, SAST, infrastructure, container, firmware supply-chain, and license scans before pilot deployment.

Deployments must use federated cloud identity rather than static cloud credentials. Require approvals for staging and production, with a tested rollback plan for API, model/prompt configuration, search index, and device firmware.
