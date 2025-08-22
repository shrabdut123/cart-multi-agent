# agent.py
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from pathlib import Path
from service_coordinator_agent.prompt import MCP_PROMPT

# IMPORTANT: Dynamically compute the absolute path to your server.py script
PATH_TO_YOUR_MCP_SERVER_SCRIPT = str((Path(__file__).parent / "server.py").resolve())


root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="db_mcp_client_agent",
    instruction=MCP_PROMPT,
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="python3",
                args=[PATH_TO_YOUR_MCP_SERVER_SCRIPT],
            )
        )
    ],
)