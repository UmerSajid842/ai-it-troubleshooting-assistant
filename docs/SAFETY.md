# Safety and Privacy Guide

The assistant is intentionally non-executing. It returns guidance and escalation notes but does not run shell commands, change configuration, delete files, reset passwords, or access a user’s device.

Users should never share passwords, MFA codes, private keys, access tokens, customer records, or confidential incident details in prompts. Any production deployment should add authentication, rate limiting, redaction, retention controls, structured logging policy, prompt/version tracking, and human review for security-sensitive issues.

LLM-generated guidance must be treated as untrusted text until reviewed. The deterministic playbooks are the safer default for common issues. Any new playbook should be reviewed by a qualified support or security professional before it is exposed to users.
