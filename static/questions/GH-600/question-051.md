---
question: |
    You have a GitHub repository.

    Developers use the GitHub Copilot CLI and repository-scoped hooks under .github/hooks/*.json.

    You need to allow the Copilot CLI to automatically run low-risk Bash commands. The solution must prevent the autonomous execution of high-risk commands, such as sudo, rm -rf /, and curl ... | bash.

    What should you do?
---

- [ ] Configure a userPromptSubmitted hook that logs prompts and exits nonzero.
- [ ] Add .github/hooks/logs/ to .gitignore.
- [ ] Configure a sessionStart hook that prints a policy banner.
- [x] Configure a preToolUse hook that returns permissionDecision: "deny".