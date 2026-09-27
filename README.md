# PUCIT GPA/CGPA Assistant

A conversational agent that helps PUCIT BS(CS) students with GPA and CGPA
questions. All arithmetic runs through tools in `tools.py` — the agent
never does math itself, and never guesses a number it hasn't been given.

## Setup

1. Install dependencies:
   ```bash
   pip install python-dotenv langchain langchain-groq streamlit
   ```
2. Copy `.env.example` to `.env` and add your Groq API key:
   ```
   GROQ_API_KEY=your_key_here
   ```

## Run (terminal)

```bash
python agent.py
```

## Run (web UI)

```bash
streamlit run app.py
```

Or install everything at once:
```bash
pip install -r requirements.txt
```

## Files

- `llm.py` — Groq model setup
- `tools.py` — all calculation/lookup tools (no arithmetic happens outside these)
- `agent.py` — system prompt, agent creation, terminal chat loop
- `app.py` — Streamlit GUI, reuses the same `agent` from `agent.py`
- `.streamlit/config.toml` — dark green theme for the Streamlit UI 
- `.env.example` — template for the required environment variable
- `requirements.txt` — dependencies

