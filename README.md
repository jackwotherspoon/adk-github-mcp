# GitHub ADK Agent

This repository contains a simple agent built with Agent Development Kit (ADK).
The agent is designed to interact with the new GitHub remote MCP server,
allowing you to ask questions and get information about GitHub repositories, users, and more.

## Overview

The agent leverages the power of Google's Gemini model to understand and respond to your queries.
It uses the `MCPToolset` from the Google ADK to connect to the GitHub remote MCP server,
providing a natural language interface to GitHub's vast dataset.

## Pre-requisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.10+**
- **uv**: A fast Python package installer and resolver. You can install it by following the official instructions: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

## Setup

Follow these steps to set up the project locally.

### 1. Clone the Repository

First, clone the repository to your local machine and navigate into the project directory:

```bash
git clone https://github.com/jackwotherspoon/adk-github-mcp.git
cd adk-github-mcp
```

### 2. Get API Keys

This project requires two API keys to function:

#### Google AI Studio API Key

You'll need a Google AI Studio API key to use the Gemini model.

1.  Go to [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey).
2.  Click on "Create API key".
3.  Copy the generated API key.
4.  Set it as an environment variable named `GOOGLE_API_KEY`:

```bash
export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
```

#### GitHub Personal Access Token (PAT)

To authenticate with the GitHub MCP server, you need a GitHub Personal Access Token.

1.  Go to your GitHub [Developer settings](https://github.com/settings/tokens).
2.  Click on "Personal access tokens" -> "Tokens (classic)".
3.  Click "Generate new token" -> "Generate new token (classic)".
4.  Give your token a descriptive name.
5.  Set an expiration date for your token.
6.  **Important**: For security, grant your token the most limited scopes necessary.
For read-only access to repositories, the `repo:status`, `public_repo`, and
`read:user` scopes are often sufficient. Avoid granting full `repo` or
`admin` permissions unless absolutely necessary.
7.  Click "Generate token".
8.  Copy the generated token.
9.  Set it as an environment variable named `GITHUB_PERSONAL_ACCESS_TOKEN`:

```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"
```

## Running the Agent

Once you have completed the setup, you can run the agent's development UI.

```bash
uv run adk web
```

This will start a local web server, and you can interact with the agent through your browser.

## Example Queries

Here are some example queries you can try to test the agent's capabilities:

- "Find the top 5 most starred repositories for the topic 'python'."
- "List the open issues for the 'tensorflow/tensorflow' repository."
- "What are the latest commits in the 'google/adk-python' repository?"

These examples showcase how you can use natural language to query the GitHub MCP server through the agent. 

Feel free to experiment with your own questions!
