"""Sentinel control-platform API entry point."""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Sentinel API", version="0.1.0")


class EmergencyPromptRequest(BaseModel):
    scenario: str = Field(description="Approved security emergency scenario")
    site_id: str


APPROVED_SCENARIOS = {
    "fire": ["Raise the alarm", "Call emergency services", "Guide people to safety"],
    "medical": ["Assess immediate danger", "Call emergency services", "Alert the control room"],
    "intrusion": ["Move to a safe position", "Alert the control room", "Preserve observations"],
    "duress": ["Activate duress alert", "Move to a safe position", "Await control-room support"],
    "suspicious-person-package": [
        "Keep a safe distance",
        "Alert the control room",
        "Do not handle the item",
    ],
}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/emergency-prompts")
def emergency_prompt(request: EmergencyPromptRequest) -> dict[str, object]:
    scenario = request.scenario.lower().strip()
    if scenario not in APPROVED_SCENARIOS:
        return {"status": "blocked", "reason": "Only approved security scenarios are supported."}
    return {"status": "ok", "site_id": request.site_id, "steps": APPROVED_SCENARIOS[scenario]}
