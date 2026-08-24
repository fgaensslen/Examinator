---
question: |
    You need to implement the security requirements for agent1.

    Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.
question_type: "drag_drop"
code_lang: "TEXT"
values_pool:
  - "Add an execute job that has needs: [plan] and environment: plan-review."
  - "Configure the plan job to advance to execution automatically if the job completes without any workflow errors."
  - "On the main branch of product-api, configure a branch protection ruleset that requires two approvals before agent1 can push changes."
  - "Add SG_Dev as additional required reviewers for the plan-review environment."
  - "In the product-api repository settings, create a GitHub Actions environment named plan-review and add SG_Review as the required reviewers."
  - "To the agent1 workflow, add a plan job that runs first and uploads the plan output as a workflow artifact."
correct_mapping:
  blank_1: "In the product-api repository settings, create a GitHub Actions environment named plan-review and add SG_Review as the required reviewers."
  blank_2: "To the agent1 workflow, add a plan job that runs first and uploads the plan output as a workflow artifact."
  blank_3: "Add an execute job that has needs: [plan] and environment: plan-review."
---
Step 1:
{blank_1}
Step 2:
{blank_2}
Step 3:
{blank_3}