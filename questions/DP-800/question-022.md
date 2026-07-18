---
question: "You are developing an Azure SQL database solution from a locally cloned GitHub repository by using Microsoft Visual Studio Code and GitHub Copilot Chat.


You need to ensure that GitHub Copilot Chat can call the hosted GitHub MCP Server tools by using OAuth. The MCP server configuration must be scoped to the repository.


What should you do in Visual Studio Code?"
documentation: "https://docs.github.com/en/actions"
---
- [ ]Create a personal access token (PAT) that has the repo scope and store the PAT in the .vscode\mcp.json file as the Authorization header.
- [x]From the Command Palette, enter MCP: add server, select HTTP (HTTP or Server-Sent Events), enter https://api.githubcopilot.com/mcp/, and then save the configuration to the workspace settings. and then save the configuration to the user settings.
- [ ]From the Command Palette, enter MCP: add server, select HTTP (HTTP or Server-Sent Events), enter https://api.githubcopilot.com/mcp/,
- [ ]Create a personal access token (PAT) that has the repo scope and store the PAT in the .github\mcp.json file as the Authorization header.
