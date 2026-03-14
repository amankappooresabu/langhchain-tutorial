# LangChain Agents & Workflows

This repository contains experiments and examples for building **LLM workflows and agents using LangChain and Google Gemini models**.
The project explores different chaining techniques, agent reasoning, and interaction with external tools such as databases.

---

## Project Overview

The repository is organized into chapters that demonstrate different LangChain concepts:

* **Chains** – sequential and conditional LLM pipelines
* **Custom runnables** – extending LangChain workflows
* **Parallel chains** – executing tasks concurrently
* **Agents** – LLM-driven reasoning with tools
* **Database interaction** – building an agent that queries a SQL database

The examples are implemented using **Python, LangChain, and Gemini models**.

---

## Project Structure

```
.
├── CH-1/
├── CH-2/
│   ├── 1_First_Chain.ipynb
│   ├── 2_Chain_With_CustomRunnable.ipynb
│   ├── 3_Parallel_chains.ipynb
│   └── 4_Conditional_Chains.ipynb
│
├── CH-3/
│   ├── SalesDB/
│   │   └── sales.db
│   ├── init_db.py
│   ├── ReactAgent.ipynb
│   └── React_Db_Agent.ipynb
│
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

### CH-2 – LangChain Chains

This chapter contains examples demonstrating different **LangChain chain patterns**:

* **First Chain** – basic LLM invocation
* **Custom Runnable** – extending LangChain functionality
* **Parallel Chains** – running multiple chains simultaneously
* **Conditional Chains** – dynamic logic in chains

### CH-3 – Agents

Focuses on **agent-based reasoning** with tools.

Includes:

* **ReAct Agent**
* **Database Agent**
* Querying a **SQLite sales database** using LLM reasoning.

---

## Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/langchain-agents.git
cd langchain-agents
```

---

### 2. Create a virtual environment

```
python -m venv .venv
```

Activate it:

**Windows**

```
.venv\Scripts\activate
```

**Mac/Linux**

```
source .venv/bin/activate
```

---

### 3. Install dependencies

If using **uv**:

```
uv sync
```

Or with pip:

```
pip install -r requirements.txt
```

---

### 4. Environment Variables

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

Do **not commit this file to GitHub**.


## Notes

This repository is primarily for **learning and experimentation with LangChain agents and workflows**.

It demonstrates concepts rather than production-ready implementations.
