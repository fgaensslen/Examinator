---
question: |
    You have a GitHub Copilot coding agent named CodeAgent. The .agent.md file of CodeAgent contains the following YAML frontmatter.

    ```
    name: CodeAgent
    description: Performs repository analysis and code review tasks. tools: ['edit', 'execute', 'read', 'search']
    ```

    You need to issue a GitHub Copilot CLI command that preserves execution velocity for read-only tasks by eliminating approval prompts for low-risk tools. The solution must ensure that high-risk tools that can make changes remain available but still require explicit user approval before running.

    Which command should you run?
---

- [ ] copilot agent run CodeAgent --deny-tool 'edit,execute'
- [ ] copilot agent run CodeAgent --allow-all-tools
- [ ] copilot agent run CodeAgent
- [x] copilot agent run CodeAgent --allow-tool 'read,search'
- [ ] copilot agent run CodeAgent --allow-tool 'read,search' --deny-tool 'edit,execute'