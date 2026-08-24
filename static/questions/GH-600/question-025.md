---
question: |
    You have a GitHub repository that uses GitHub Actions to validate pull requests opened by the GitHub Copilot coding agent. The workflow runs unit tests and a linter on pull request triggers, and Copilot opens draft pull requests on dedicated branches while iterating by using commits.

    You discover that when multiple Copilot sessions push updates to the same pull request branch in quick succession, multiple workflow runs execute concurrently.

    You need to enable parallel workflow executions across different pull request branches.

    How should you configure workflow-level concurrency? To answer, select the appropriate options in the answer area.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "TEXT"
values_pool:
    - "Set concurrency at the workflow level."
    - "Set cocurrency at each job level only."
    - "Set strategy.matrx to limit parallelism."
    - "group: ${{ github.head_ref || github.run_id }}"
    - "group: ${{ github.ref }}"
    - "group: ${{ github.run_id }}"
    - "group: ${{ github.workflow }}-${{ github.ref }}"
correct_mapping:
    blank_1: "Set concurrency at the workflow level."
    blank_2: "group: ${{ github.ref }}"
---
Concurrency scope:
{blank_1}
Concurrency expression:
{blank_2}