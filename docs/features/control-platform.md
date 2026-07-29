# Feature: control platform

## Scope

The control platform manages the device fleet, sites, emergency alerts, incident workflow, and operational audit records.

## Access model

- Officers access only their assigned device and site actions.
- Control-room operators access authorized active sites and escalations.
- Supervisors access site-level operational information, but not officer-to-device transcripts.
- Tenant and platform administrators have explicitly separated administration roles.

## Device lifecycle

The platform must record supplier, device identifier, SIM association, assignment, activation, deactivation, recycling, firmware version, and OTA update status. A device leaving its configured site boundary is recorded and evaluated according to customer policy.
