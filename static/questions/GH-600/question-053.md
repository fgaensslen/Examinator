---
question: |
    You have a GitHub repository that uses a custom GitHub Copilot coding agent defined in the rollout-bot.agent.md file.

    You need to update a workflow so that agent-profile changes can be rolled back by reverting a single commit and rerunning the workflow. The workflow must check out the exact commit being deployed and apply the agent profile from the repository at that commit.

    How should you complete the workflow? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "YAML"
values_pool:
  - "${{ github.ref }}"
  - "${{ github.sha }}"
  - ".github/agents/rollout-bot.md"
  - "agents/rollout-bot.md"
  - "github.ref"
  - "inputs.ref"
correct_mapping:
  blank_1: "inputs.ref"
  blank_2: ".github/agents/rollout-bot.md"
  blank_3: ".github/agents/rollout-bot.md"
---
name: Deploy custom agent profile
on:
  workflow_dispatch:
    inputs:
      ref:
        description: "Git ref to deploy (commit SHA, tag, or branch)"
        required: true
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout exact ref for rollback safety
        uses: actions/checkout@v4
        with:
          ref: ${{{blank_1}}}
      - name: Validate agent profile exists at this ref
        run: |
          test -f {blank_2}
      - name: Deploy agent profile from repo to internal catalog
        run: |
          ./scripts/deploy-agent-profile.sh {blank_3}