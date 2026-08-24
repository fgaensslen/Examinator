---
question: |
    You have a GitHub repository that contains the following custom agent files:

    - A file named planner.agent.md that includes YAML frontmatter with a handoffs entry that has label: Start Implementation, agent: implementer, and prompt: Now implement the plan outlined above
    - A file named implementer.agent.md that is in the same directory as planner.agent.md and includes YAML frontmatter that has name: IMPLEMENTER
    
    You add a third agent file named review.agent.md.review.agent.md includes YAML frontmatter that has name: code-review.

    You make the following changes to planner.agent.md:
    - Update the existing handoff to include send: true and model: GPT-5.2 (copilot).
    -Add a second handoff that has label: Run Review, agent: code-review, and prompt: Review the code changes made in the previous step.
    - No other agent files are modified.


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
The "Run Review" handoff resolves to "review.agent.md".
{blank_1}
The "Start Implementation" handoff fails to identify the target agent.
{blank_2}
Selectin "Start Implementation" switches the chat to the "implementer" agent and automatically submits the handoff prompt to the agent by using "GPT-5.2 (copilot)".
{blank_3}
