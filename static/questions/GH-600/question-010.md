---
question: |
    You have a GitHub repository that uses the GitHub Copilot coding agent to resolve issues and create draft pull requests.

    You assign an issue to Copilot. Copilot creates a draft pull request. The pull request timeline shows Copilot started work, followed by status updates. The most recent status update is 55 minutes old.

    You discover that the agent is no longer making progress.

    You need to ensure that the work resumes without redoing the completed steps or changing the previously chosen approach.

    What should you do? To answer, select the appropriate options in the answer area.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "TEXT"
values_pool:
    - "Review insights for the repository."
    - "Run git log locally on the default branch."
    - "Select View session from the pull request."
    - "Close and reopen the issue."
    - "Mark the draft pull request as Ready for review."
    - "From GitHub Copilot Chat, open a new pull request."
    - "Post a pull request comment that mentions @copilot."
correct_mapping:
    blank_1: "Select View session from the pull request."
    blank_2: "Post a pull request comment that mentions @copilot."
---
To confirm progress of the agent:
{blank_1}
To resume the work:
{blank_2}
