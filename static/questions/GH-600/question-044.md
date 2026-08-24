---
question: |
    You have a GitHub Enterprise repository that uses the GitHub Copilot coding agent and opens draft pull requests for assigned issues.

    Evaluation results show that the agent repeatedly opens pull requests that modify .github/workflows/*.yml to bypass failing checks instead of fixing the underlying code.

    You need to ensure that the agent fixes the underlying code instead of bypassing the failing checks.

    What should you do?
---

- [ ] Start the GitHub Copilot CLI by using --allow-all.
- [x] Update .github/copilot-instructions.md.
- [ ] Create a branch ruleset.
- [ ] Disable GitHub Actions workflows for pull requests created by the agent.