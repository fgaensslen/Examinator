---
question: | 
    You have a GitHub repository that has a GitHub Actions workflow. The workflow runs an AI agent.

    You need to ensure that the default GITHUB_TOKEN permissions are read-only, and write access is granted to only the job that performs repository write operations. The workflow must be able to create and approve pull requests only when explicitly enabled.

    How should you complete the workflow? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "YAML"
values_pool:
    - "contents: read"
    - "contents: write"
    - "issues: write"
    - "permissions: read-all"
    - "pull_requests: read"
    - "pull_requests: write"
correct_mapping:
    blank_1: "permissions: read-all"
    blank_2: "contents: write"
    blank_3: "pull_requests: write"
---
name: agent-pr
on:
  pull_request:
permissions:
  {blank_1}
jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - name: Read-only analysis
        run: echo "Analyze PR content and post a comment via API"
  update_artifacts:
    runs-on: ubuntu-latest
    permissions:
      {blank_2}
    steps:
      - uses: actions/checkout@v5
      - name: Update generated artifacts
        run: |
          echo "regenerate"
      - name: Create pull request
          {blank_3}
        run: echo "create PR"