# MediMind


---

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![License](https://img.shields.io/badge/License-Pending-lightgrey)
![GitHub stars](https://img.shields.io/github/stars/walidad007/MediMind-Ai-Therapist?style=social)

---


**MediMind** is an agentic AI-powered mental health support system that combines an LLM-based reasoning agent with tool modules and a simple Streamlit UI. It provides empathetic conversational support, evidence-grounded suggestions, and transparent tool usage while emphasizing safety and clear medical disclaimers.

---

![MediMind Screenshot](assets/medimind_preview.png)

---

## Key Features
- **Agentic architecture**: planner + tool manager + tool calls (retrieval, checks, etc.).  
- **Streamlit frontend** for simple chat interaction.  
- **FastAPI backend** that runs the agent and returns structured JSON (assistant response + tool used).  
- **Safety-first design**: includes disclaimers and system prompts to reduce harmful or misleading outputs.  

---

## Architecture Overview
- **Frontend (Streamlit)**: Captures user input and posts to the backend (`/ask`), displays chat history.  
- **Backend (FastAPI)**: Accepts requests, wraps user input with system instructions, runs the agent graph, parses streamed output, and returns JSON with `response` and `tool_called`.  
- **Agent module (`ai_agent`)**: orchestrates LLM reasoning (graph), includes `SYSTEM_PROMPT`, and a `parse_response` helper to extract final answer and tools used.  

---

## Quickstart (local)

### 1. Clone the repo
```bash
git clone https://github.com/walidad007/MediMind-Ai-Therapist.git
cd MediMind-Ai-Therapist


---




