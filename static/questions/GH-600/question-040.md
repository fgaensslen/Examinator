---
question: |
    You have a GitHub repository that uses GitHub Actions for CI on pull requests.

    You have a GitHub Copilot coding agent that opens pull requests for backlog items, and your company requires automated checks for agent-generated changes.

    You plan to standardize success criteria so that pull requests created by agents only succeed when unit tests pass and CodeQL analysis completes.
    You need to configure a GitHub Actions workflow that runs on pull requests, executes unit tests, and performs CodeQL analysis.

    How should you complete the workflow? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "YAML"
values_pool:
  - "analyze"
  - "build"
  - "init"
  - "npm test"
  - "python -m unittest"
  - "upload-sarif"
correct_mapping:
  blank_1: "npm test"
  blank_2: "init"
  blank_3: "analyze"
---
name: agent-success-criteria
on:
  pull_request:
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: {blank_1}
  codeql:
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write
    steps:
      - uses: actions/checkout@v4
      - name: Prepare CodeQL
        uses: github/codeql-action/{blank_2}@v3
      - name: Run CodeQL
        uses: github/codeql-action/{blank_3}@v3