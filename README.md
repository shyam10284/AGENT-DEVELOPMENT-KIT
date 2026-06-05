# AGENT-DEVELOPMENT-KIT

# Google ADK - Multipurpose Agent Workflow

This repository contains a modular AI agent system built using the Google Agent Development Kit (ADK) and powered by Gemini models. It includes a multi-agent sequential workflow for content creation and a localized Retrieval-Augmented Generation (RAG) agent for document analysis.

## 🚀 Features

- **YouTube Shorts Workflow**: A sequential chain of three specialized agents (`scriptwriter_agent`, `visualizer_agent`, and `formatter_agent`) that collaborate to produce production-ready video blueprints from a single prompt idea.
- **Local RAG Agent**: A localized research assistant (`rag_research_agent`) equipped with a python-native tool to scan, parse, and answer domain-specific questions based entirely on documents placed inside a local directory.
- **Interactive UI Panel**: Fully integrated with the native Google ADK Web Developer Interface for tracing, tracking agent states, and monitoring model invocations.

---

## 🛠️ Project Architecture

The architecture relies on configuring a `root_agent` control switch within `agent.py` to route user interaction between the sequential workflow or the tool-enabled single agent:

              ┌───────────────┐ 
              │  root_agent   │
              └───────┬───────┘
                      │ (Control Switch)
        ┌─────────────┴─────────────┐
        ▼                           ▼
┌──────────────────────┐    ┌──────────────────────┐
│ youtube_shorts_agent │    │  rag_research_agent  │
└───────────┬──────────┘    └───────────┬──────────┘
            │                           │
   ┌────────┼────────┐                  ▼
   ▼        ▼        ▼          ┌───────────────┐
[Agent]  [Agent]  [Agent]       │ read_my_files │ (Local Tool)
Script   Visual  Format         └───────┬───────┘
▼
📂 ./data/*.txt

## 💻 Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.11+** installed on your system.

### 2. Clone and Setup Environment
Navigate to your repository directory and activate your virtual environment:
```bash
# Navigate to the project directory
cd AGENT-DEVELOPMENT-KIT/google_adk/my_workflow

# Activate the virtual environment (Windows)
..\venv\Scripts\activate

3. Dependencies
Install the required base utilities to manage environment configurations securely:

Bash:
pip install python-dotenv pydantic

4. API Configuration
Create a file named .env in the root of the my_workflow directory to store your secret Google AI Studio token securely. Never commit this file to GitHub.

Plaintext
GEMINI_API_KEY=your_actual_gemini_api_key_here

⚙️ How to Run
You can toggle which agent is active by altering the root_agent configuration block at the bottom of agent.py.

Step 1: Set the Target Agent
Open agent.py and modify the control switches:

To run the YouTube Short generator:

Python
root_agent = youtube_shorts_agent
# root_agent = rag_agent
To run the Local Document Search Engine:

Python
# root_agent = youtube_shorts_agent
root_agent = rag_agent
Step 2: Launch the Web UI Dashboard
Run the ADK internal server command to initialize the visual developer layout:

Bash
..\venv\Scripts\adk web .
Open the local URL displayed in your terminal terminal

📂 Documenting local Data (For RAG Mode)
When using the rag_research_agent, place any reference materials or documentation files inside a subfolder named ./data/ formatted as plain text files:

./data/knowledge.txt

./data/README.md

The local file handler function will compile these documents dynamically to give the LLM customized reference data.
