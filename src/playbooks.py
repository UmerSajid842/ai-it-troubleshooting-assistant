"""Small, reviewable troubleshooting playbooks."""

PLAYBOOKS = {
    "wifi": {
        "title": "Wi-Fi connectivity",
        "steps": [
            "Confirm that Wi-Fi is enabled and the device is connected to the intended network.",
            "Restart the router only if you are authorized to do so and no critical service depends on it.",
            "Test one other device to separate a device issue from a network issue.",
        ],
        "escalate": "Escalate if multiple devices remain offline or if the network is business-critical.",
    },
    "password": {
        "title": "Password or account access",
        "steps": [
            "Use the organization’s approved password-reset page rather than sharing a password in chat.",
            "Check that the account identifier and sign-in domain are correct.",
            "Contact the service desk if multi-factor authentication or account lockout persists.",
        ],
        "escalate": "Never request or store the user’s password, recovery code, or MFA secret.",
    },
    "slow": {
        "title": "Slow computer or application",
        "steps": [
            "Save work and note which application or action is slow.",
            "Close only non-essential applications after confirming unsaved work is not at risk.",
            "Record the time, error text, and recent changes for the service desk.",
        ],
        "escalate": "Escalate before deleting files, changing registry settings, or running privileged commands.",
    },
}


def detect_intent(text: str) -> str:
    lowered = text.lower()
    if any(word in lowered for word in ("wifi", "wi-fi", "internet", "network")):
        return "wifi"
    if any(word in lowered for word in ("password", "login", "sign in", "mfa", "locked")):
        return "password"
    if any(word in lowered for word in ("slow", "freezes", "lag", "performance")):
        return "slow"
    return "unknown"
