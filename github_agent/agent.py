import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams

root_agent = LlmAgent(
    model="gemini-2.5-pro-preview-06-05",
    name="github_agent",
    instruction="You are a helpful assistant that can answer questions about GitHub.",
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url="https://api.githubcopilot.com/mcp/",
                headers={
                    "Authorization": "Bearer " + os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN"),
                }
            )
        )
    ],
)
