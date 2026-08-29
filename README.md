# AI-Powered IT Troubleshooting Assistant

A practical GenAI assistant for guiding users through common technical issues with an interactive troubleshooting flow. The project was listed on Umer Sajid’s CV as an application deployed on Hugging Face Spaces. This repository provides a separate, reviewable implementation structure with a deterministic troubleshooting workflow, an optional LLM adapter, a notebook, tests, and deployment guidance.

> **Safety boundary:** The assistant provides troubleshooting guidance, not guaranteed diagnosis or autonomous system changes. It must ask for confirmation before destructive commands, avoid collecting secrets, and escalate uncertain or security-sensitive incidents to a qualified human.

## What the project demonstrates

The application combines intent capture, structured troubleshooting steps, user confirmation, and optional LLM-generated explanations. Deterministic playbooks keep common flows predictable; the LLM adapter is isolated so that model availability, prompts, and output validation remain visible to reviewers.

The included notebook walks through the system design, a sample conversation, structured response validation, and an optional provider integration. It does not claim a fixed accuracy benchmark or fabricate user tickets.

## Repository structure

```text
.
├── src/
│   ├── __init__.py
│   ├── playbooks.py       # Safe, deterministic troubleshooting flows
│   ├── assistant.py       # Intent routing and response orchestration
│   └── llm_adapter.py     # Optional OpenAI-compatible JSON adapter
├── notebooks/
│   └── 01_assistant_walkthrough.ipynb
├── tests/
│   └── test_assistant.py
├── docs/
│   └── SAFETY.md
├── requirements.txt
├── LICENSE
└── README.md
```

## Browser demo

Open [`demo.html`](demo.html) for a standalone browser demonstration of the deterministic workflow. It supports Wi-Fi, account-access, slow-device, and unknown-issue examples. The demo runs entirely in the browser, executes no commands, and does not call an LLM service.

## Local setup

```bash
git clone https://github.com/UmerSajid842/ai-it-troubleshooting-assistant.git
cd ai-it-troubleshooting-assistant
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
jupyter notebook notebooks/01_assistant_walkthrough.ipynb
```

The deterministic workflow runs without an API key. The optional LLM adapter requires an OpenAI-compatible endpoint configured through environment variables; never commit credentials.

## Example

```python
from src.assistant import TroubleshootingAssistant

assistant = TroubleshootingAssistant()
reply = assistant.respond("My Wi-Fi is connected but websites will not load")
print(reply)
```

The returned dictionary contains an intent, a user-facing explanation, ordered steps, escalation guidance, and a `requires_confirmation` flag. The assistant does not execute shell commands or change a user’s system.

## Hugging Face deployment note

The CV describes a Hugging Face Spaces deployment. A Gradio UI can call `TroubleshootingAssistant.respond` and display the structured result. Add the verified Space URL only after confirming the Space is public, reproducible, and configured without exposed secrets. The repository intentionally does not include credentials or claim an active deployment URL.

## Limitations and roadmap

Troubleshooting coverage is intentionally narrow and should be expanded through reviewed playbooks and evaluation conversations. Future work could add retrieval over approved internal documentation, multilingual flows, conversation state, red-team tests, human escalation, feedback capture, and an offline evaluation set. Any production deployment would require privacy review, access controls, logging policy, prompt/version tracking, rate limits, and abuse monitoring.

## License

MIT License. See [LICENSE](LICENSE).
