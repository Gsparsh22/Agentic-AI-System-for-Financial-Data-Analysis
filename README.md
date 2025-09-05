# Phidata Financial Agent

**What this is:**  
A Financial Agent.
The project creates two agents (a web-search agent and a finance agent using yfinance tools) and composes them into a multi-agent team.

---

## Files
- `finance_agent.py` - main script
- `requirements.txt` - dependencies
- `.env.example` - example environment variables

---

## Prerequisites
- Python 3.10+ recommended
- pip
- (Optional) A Python virtual environment
- An OpenAI API key or access to any model provider configured for Phidata (see notes below)

---

## Setup

1. Create & activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate     # Windows
