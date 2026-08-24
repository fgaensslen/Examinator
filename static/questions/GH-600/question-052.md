---
question: |
    Your company uses Microsoft Visual Studio Code and GitHub Copilot Chat.

    You have a GitHub repository that uses main as the default branch. The repository contains a workspace custom agent stored at .github/agents/release-notes.agent.md.

    A developer switches to a branch named branch1 where the agent file does NOT exist. In the same session, the developer switches to a user profile named profile1.profile1 contains a custom agent file named release-notes.agent.md that has user-invokable set to false.

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
  blank_3: "No"
---
On "main", the agent will appear in the agents dropdown with a display name of "release-notes".
{blank_1}
When the developer is on "branch2", the workspace version of the "release-notes" agent will be available in the agents dropdown.
{blank_2}
When the developer switches to "profile1", the user profile agent will appear in the agents dropdown and will override the workspace agent that has the same file name.
{blank_3}