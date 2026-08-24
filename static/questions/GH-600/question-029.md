---
question: |
    You have a GitHub repository that runs an agentic software development lifecycle (SDLC) workflow by using GitHub Actions. The workflow uses the following three executors implemented as scripts: spec_analyzer, risk_reviewer, and plan_merger.

    You need to coordinate multiple specialized agents so that analysis and risk review run in parallel, and then a final executor merges the outputs into a single plan. The orchestration pattern must fan out one request to multiple executors, and then fan in the results to a final executor.

    How should you complete the workflow definition?
    
    To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.
    
    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "YAML"
values_pool:
  - "[spec_analyzer, risk_reviewer]"
  - "concurrency"
  - "group"
  - "matrix"
  - "needs"
  - "strategy"
  - "tools"
correct_mapping:
  blank_1: "needs"
  blank_2: "[spec_analyzer, risk_reviewer]"
  blank_3: "concurrency"
---
name: multi-agent-orchestration
on:
  workflow_dispatch:
jobs:
  spec_analyzer:
    runs-on: ubuntu-latest
    steps:
      - name: Run spec analyzer executor
        run: ./executors/spec_analyzer.sh
  risk_reviewer:
    runs-on: ubuntu-latest
    steps:
      - name: Run spec analyzer executor
        run: ./executors/spec_analyzer.sh
  risk_reviewer:
    runs-on: ubuntu-latest
    steps:
      - name: Run risk reviewer executor
        run: ./executors/risk_reviewer.sh
  plan_merger:
    runs-on: ubuntu-latest
    {blank_1}:
    {blank_2}
    steps:
      - name: Merge executor outputs into a single plan
        run: ./executors/plan_merger.sh
      - name: Publish merged plan
        run: echo "publish plan artifact"
    {blank_3}:
      group: multiagent-${{ github.ref }}