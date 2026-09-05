---
question: |
    Your team uses a remote GitHub Model Context Protocol (MCP) server for workflows in the software development life cycle (SDLC).

    You need to commit a workspace-scoped MCP configuration to ensure that GitHub Copilot can connect to the GitHub-hosted MCP endpoint and authenticate by using a GitHub personal access token (PAT).

    How should you complete the mcp.json configuration file? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "JSON"
values_pool:
  - "Bearer"
  - "Digest"
  - "http"
  - "local"
  - "stdio"
  - "Token"
  - "x-api-key"
correct_mapping:
  blank_1: "http"
  blank_2: "Bearer"
---
{
  "servers": {
    "github": {
      "type": "{blank_1}",
      "url": "https://api.githubcopilot.com/mcp/",
      "requestInit": {
        "headers": {
          "Authorization": "{blank_2} ${env:GITHUB_PAT}"
        }
      }
    }
  }
}
