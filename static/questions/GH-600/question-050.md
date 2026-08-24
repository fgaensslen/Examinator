---
question: |
    Your company uses GitHub Copilot custom agents in Microsoft Visual Studio Code.

    The company also uses the Copilot coding agent on GitHub issues.

    You have a file named .planner.agent.md that defines an agent named planner.planner has tools set to ['search', 'read', 'fetch']. There are explicit instructions NOT to write or modify any code. The file also defines a handoff labeled Start Implementation to an agent named implementer and sets send to false.

    Developers report that after the planner agent produces a plan, implementation sometimes starts immediately in the same conversation, and code changes appear without an explicit agent switch.

    When Copilot-created pull requests stall, maintainers review the pull request timeline and session logs. Several stalled sessions show outbound network commands blocked by a firewall, and the repositories do NOT contain a .github/copilot-instructions.md file.

    For each of the following statements, select Yes if the statement is true. Otherwise, select No.

    NOTE: Each correct selection is worth one point.

question_type: "drag_drop"
code_lang: "TEXT"
values_pool:
  - "Yes"
  - "No"
correct_mapping:
  blank_1: "Yes"
  blank_2: "No"
  blank_3: "Yes"
---
The configuration of the "planner" agent explicitly prevents code changes from being produced in the same conversation.
{blank_1}
The "planner" agent is violating its allowed tools by attempting internet access, and removing "search" will resolve the issue.
{blank_2}
Adding a repository-level ".github/copilot-instructions.md" file that requires the agent to run tests and linters will mitigate the stalled pull request that has a failing CI anti-pattern.
{blank_3}