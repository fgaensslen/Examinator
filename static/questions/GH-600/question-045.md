---
question: |
    You have a GitHub repository that uses GitHub Copilot Chat in Microsoft Visual Studio Code. Custom agents are stored in the repository under version control.
    Your team uses a multi-agent workflow where a planner agent produces an implementation plan that is then handed off to an implementation agent to make changes.

    Recent prompts cause the planner agent to start editing files and running commands before the plan is approved.

    You need to configure the planner agent to meet the following requirements:
    Use only read-only tools.

    Hand off to the implementation agent only after the plan is approved.
    How should you configure the agent? To answer, select the appropriate options in the answer area.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "YAML"
values_pool:
  - "['edit','read','commit']"
  - "['fetch','push','merge']"
  - "['search','read','fetch']"
  - "['search','read','publish']"
  - "false"
  - "true"
correct_mapping:
  blank_1: "['search','read','fetch']"
  blank_2: "false"
---
name: planner-agent
description: Planning
tools: {blank_1}
handoffs:
  - label: Start Implementation
    agent: implementer
    prompt: Now implement the plan outlined above.
    send: {blank_2}