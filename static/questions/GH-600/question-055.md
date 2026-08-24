---
question: |
    You have a GitHub Enterprise organization that uses GitHub Copilot.

    You discover that GitHub Copilot Chat responses in Microsoft Visual Studio Code are influenced by earlier, unrelated troubleshooting prompts from the same conversation.

    You need to ensure that the Copilot Chat conversation context is limited to information relevant to the current work item. The solution must minimize effort.

    What should you do? To answer, select the appropriate options in the answer area.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "TEXT"
values_pool:
  - "Start a new chat."
  - "Delete the repository memories."
  - "Delete the irrelevant request from the conversation."
  - "Change from chat mode to agent mode."
  - "Open related files and close unrelated files."
  - "Disable all Copilot features for the repository."
correct_mapping:
  blank_1: "Start a new chat."
  blank_2: "Open related files and close unrelated files."
---
When a previous prompt is no longer relevant:
{blank_1}
To keep Copilot Chat focused in the IDE:
{blank_2}