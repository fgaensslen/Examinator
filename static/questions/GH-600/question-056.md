---
question: |
    Your company uses GitHub Copilot Enterprise.

    Developers use GitHub Copilot agent mode in Microsoft Visual Studio Code on their laptops and Copilot Chat on github.com when they are away from their laptops.

    When switching between environments, the developers notice that agent workflows lose continuity because the tools available in Visual Studio Code are unavailable on github.com.

    You need to ensure that the agent tools and state are available consistently across environments and can be used from any device without local setup.

    What should you do for each requirement? To answer, drag the appropriate actions to the correct requirements. Each action may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "TEXT"
values_pool:
  - "Enable the MCP servers in Copilot policy."
  - "From Visual Studio Code, change the Copilot mode."
  - "Run a Model Context Protocol (MCP) server in Docker."
  - "Configure toolsets to disable unused GitHub API groups."
  - "Use a GitHub-hosted Model Context Protocol (MCP) server for cloud-based workflows."
  - "Add third-party Model Context Protocol (MCP) servers by using the /mcp add command."
correct_mapping:
  blank_1: "Use a GitHub-hosted Model Context Protocol (MCP) server for cloud-based workflows."
  blank_2: "Enable the MCP servers in Copilot policy."
---
To allow cross-device tool access without local setup:
{blank_1}
To enable organization-wide agent tools across all Copilot environments:
{blank_2}