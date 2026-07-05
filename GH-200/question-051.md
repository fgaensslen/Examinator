---
question: "As a developer, you need to integrate a GitHub Actions workflow with a third-party code quality provider that uses the Checks API. How should you trigger a follow-up workflow?"
documentation: "https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows"
---
- [ ] Add the workflow_run webhook event as a trigger for the workflow for the code quality integration name
- [x] Add the check_run webhook event as a trigger for the workflow when the code quality integration is completed
- [ ] Add the pull_request webhook event as a trigger for the workflow when the code quality integration is synchronized
- [ ] Add the deployment webhook event as a trigger for
