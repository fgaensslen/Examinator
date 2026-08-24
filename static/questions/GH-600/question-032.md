---
question: |
    You have a GitHub Enterprise Cloud Organization that uses the GitHub Copilot coding agent to resolve issues asynchronously.

    When an issue is assigned to GitHub Copilot, the agent creates a draft pull request, but your team cannot always tell whether the agent is actively working, has completed its session, or is awaiting workflow approval.

    Which execution context does each signal indicate? To answer, drag the appropriate context to the correct signals. Each signal may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "TEXT"
values_pool:
  - "The agent session timed out and must be reassigned."
  - "A human must manually approve and run the workflows."
  - "The agent cannot see the repository content due to exclusions."
  - "The agent session is actively running and generating live logs."
  - "The agent comment was ignored because the user lacks write access."
  - "The agent acknowledges the assignment and will create the draft pull request."
correct_mapping:
  blank_1: "The agent acknowledges the assignment and will create the draft pull request."
  blank_2: "The agent session is actively running and generating live logs."
  blank_3: "A human must manually approve and run the workflows."
---
The eyes emoji (👀) reaction appears on the issue:
{blank_1}
The pull request timeline shows Copilot started work:
{blank_2}
A draft pull request exists, but GitHub Actions checks are not running:
{blank_3}