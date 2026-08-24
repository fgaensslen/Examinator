---
question: |
    You need to provide access to the API key of MCP1. The solution must meet the security requirements.

    What should you do?
---

- [ ] Store the API key as a GitHub Codespaces user secret scoped to product-api.
- [x] Store the API key as a secret in the Copilot environment of product-api by using a name prefix of COPILOT_MCP_, and then reference the variable name in the mcp.json configuration.
- [ ] In the product-api repository settings, add the API key directly to the .mcp/server.json file by using a plaintext apiKey field.
- [ ] In product-api, add the API key as a GitHub Actions encrypted secret and reference the secret by using ${{ secrets.KEY }} in the workflow YAML of agent1.