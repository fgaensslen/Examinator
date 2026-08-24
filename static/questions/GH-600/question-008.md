---
question: |
    You have a GitHub repository that uses GitHub Actions for CI.

    Your team is piloting the GitHub Copilot coding agent to autonomously create branches and open pull requests. The repository follows trunk-based development that uses main as the default branch.

    You need to ensure that the agent meets the following requirements:
    - Changes to main can occur only by using pull requests that have at least one approval.
    - When a pull request is opened, a validation workflow runs, and the agent can still create branches and open pull requests autonomously.

    How should you configure the repository? To answer, select the appropriate options in the answer area.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "TEXT"
values_pool:
    - "Disabled"
    - "Enabled"
    - "Enabled with bypass for direct pushes"
    - "on: pull_request"
    - "on: push"
    - "on: schedule"
    - "on: workflow_dispatch"
correct_mapping:
    blank_1: "Enabled"
    blank_2: "on: pull_request"
---
Branch protection rules (main) - Require pull request before merging:
{blank_1}
Workflow trigger for validation checks:
{blank_2}