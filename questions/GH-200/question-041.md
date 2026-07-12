---
question: "As a developer, how should you enable step debug logging for a workflow?"
documentation: "https://docs.github.com/en/actions/learn-github-actions/variables"
---
- [ ] Include the following code block in your workflow:
    env:
      ACTIONS_STEP_DEBUG: true
- [ ] Use the --actions-step-debug flag when calling the workflow.
- [ ] Include the following code block in your workflow:
    defaults:
      ACTIONS_STEP_DEBUG: true
- [x] Set the ACTIONS_STEP_DEBUG secret or variable at the repository level to true.
