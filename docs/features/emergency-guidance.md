# Feature: emergency guidance

## Purpose

Provide officers with short, scenario-specific actions for fire, medical emergency, intrusion, duress, and suspicious person/package events.

## Flow

1. Officer selects or invokes an approved scenario from the wearable.
2. Device sends a signed event with device, site, and location context.
3. Platform validates device assignment and site scope.
4. Device receives the relevant three-to-six critical steps and the control room receives an alert.
5. All prompts, delivery status, acknowledgements, and escalation events are audit logged.

## Acceptance criteria

- Requests outside the approved security scenarios are blocked.
- Guidance is available through cellular connectivity and contains no unverified long-form SOP.
- A duress request triggers a high-priority control-room alert.
- Guidance is associated with the correct site and device identity.
