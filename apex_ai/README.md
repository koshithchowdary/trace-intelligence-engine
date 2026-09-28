# Apex AI

Production-oriented agentic AI application:
- OpenAI Responses API
- configurable model gateway
- web research
- persistent SQLite conversation memory
- file context for TXT/MD/PDF
- Streamlit UI
- automated tests and live E2E smoke test
- Docker deployment

This is an AI application, not a foundation model trained from scratch. It combines a frontier model with tools, memory, retrieval context and evaluation. It cannot honestly guarantee superiority on every benchmark; the included E2E/evaluation harness lets you measure it.

Run:
1. cd apex_ai
2. python -m venv .venv
3. activate the virtual environment
4. pip install -r requirements.txt
5. copy .env.example to .env and add OPENAI_API_KEY
6. streamlit run app.py

Tests:
python -m pytest tests -q
python tests/e2e_smoke.py

Streamlit Cloud:
- Main file: apex_ai/app.py
- Add OPENAI_API_KEY as a secret
- APEX_MODEL defaults to gpt-5.6-sol
- APEX_ENABLE_WEB defaults to true

Docker:
docker build -t apex-ai ./apex_ai
docker run --rm -p 8501:8501 --env-file apex_ai/.env apex-ai
