from src.assistant import TroubleshootingAssistant


def test_wifi_issue_returns_safe_structured_steps():
    result = TroubleshootingAssistant().respond("Wi-Fi is connected but internet is unavailable")
    assert result["intent"] == "wifi"
    assert result["steps"]
    assert result["requires_confirmation"] is True
    assert result["executed_actions"] == []


def test_unknown_issue_does_not_guess():
    result = TroubleshootingAssistant().respond("Something strange happened")
    assert result["intent"] == "unknown"
    assert result["requires_confirmation"] is True
    assert result["steps"] == []
