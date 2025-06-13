# 🤖 GitHub MCP Agent

This repository contains the source code for a GitHub-aware AI agent that interfaces with the GitHub MCP (Model-Centric Programming) server. It allows natural language queries to be executed against GitHub repositories, providing powerful developer assistance and repository insights.

---

## 📌 Overview

This project uses the **OpenAI SDK**, **uv** package manager, and **ADK (Agent Development Kit)** to run a local development UI where you can interact with the GitHub MCP agent. It supports advanced prompt engineering, GitHub Copilot integration, and real-time querying of GitHub projects.

---

## 🧰 Pre-requisites

Before getting started, ensure you have the following installed:

- **Python** ≥ 3.10
- **uv** (Universal Virtualenv) – a modern Python package manager  
  Install via:  
  ```bash
  pip install uv


# 🚀 Set Up

## 1.Clone the Repository

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

## 2.Get an API Key

To use the AI Studio backend (for natural language capabilities), you’ll need an API key:

1. Visit: https://aistudio.google.com/apikey

2. Generate an API key

3. Add it to your environment:
    
    export GOOGLE_API_KEY="your-api-key"

## 3. Enable GitHub Copilot Integration
If you want GitHub Copilot integration for better code context:

1. Create a GitHub Personal Access Token (PAT)

   Follow the guide: https://github.com/settings/tokens

2. Export the token:
    
    export GITHUB_TOKEN="your-pat-token"

# 🧪 Running the Agent

Start the development UI to interact with the GitHub MCP agent:
     
     uv run adk web

This will launch a local UI (typically at http://localhost:3000) where you can chat with the agent.

# 💬 Example Queries
Try asking the agent:

1. "List all challenges that offer prizes."

2. "What does the Makefile in the project do?"

3. "Summarize recent pull requests in the repo."

4. "Which files handle authentication?"

5. "What dependencies are used in the backend?"

6. "List all Python files that use the 'requests' library."

These queries showcase the GitHub MCP server's ability to analyze and understand code, PRs, issues, and other metadata across repositories.