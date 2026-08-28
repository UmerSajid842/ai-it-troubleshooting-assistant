"""Non-executing troubleshooting assistant orchestration."""
from .playbooks import PLAYBOOKS, detect_intent


class TroubleshootingAssistant:
    def respond(self, user_text: str) -> dict:
        intent = detect_intent(user_text)
        if intent == "unknown":
            return {
                "intent": "unknown",
                "message": "I could not confidently classify the issue. Please provide the application, symptom, and exact error text without sharing credentials.",
                "steps": [],
                "escalate": "Escalate security-sensitive, privileged, or business-critical incidents to a qualified human.",
                "requires_confirmation": True,
            }
        playbook = PLAYBOOKS[intent]
        return {
            "intent": intent,
            "title": playbook["title"],
            "message": f"Here is a safe first-pass checklist for {playbook['title'].lower()}.",
            "steps": playbook["steps"],
            "escalate": playbook["escalate"],
            "requires_confirmation": True,
            "executed_actions": [],
        }
