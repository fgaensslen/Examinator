---
question: |
    You have a GitHub repository that uses the GitHub Copilot coding agent to resolve issues and create draft pull requests. The repository uses GitHub Actions for CI, and reviewers rely on pull request timelines and workflow artifacts to understand what the agent did.

    During long-running agent tasks, the reviewers lose track of decisions and validation steps, which causes repeated questions and reworks when context drifts between iterations.

    You need to persist task progress and decisions as durable artifacts and ensure that the reviewers can verify what the agent did during and after execution by using GitHub as the system of record.
    
    What should you do for each requirement? To answer, drag the appropriate actions to the correct requirements. Each action may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "TEXT"
values_pool:
    - "Select View session to stream live agent logs."
    - "Assign an issue and wait for the agent to view the issue."
    - "Select Approve and run workflows in the pull request merge box."
    - "Mention @copilot in the merged pull request to restart the agent."
    - "Watch for pull request body updates and pull request timeline events."
    - "Use the upload-artifact action and configure artifact retention in the CI workflow."
correct_mapping:
    blank_1: "Use the upload-artifact action and configure artifact retention in the CI workflow."
    blank_2: "Watch for pull request body updates and pull request timeline events."
    blank_3: "Select View session to stream live agent logs."
---
Create durable run outputs that are downloadable after completion:
{blank_1}
Provide ongoing, human-reviewable task progress signals inside the pull request:
{blank_2}
Provide a real-time view of agent actions for audit and troubleshooting:
{blank_3}