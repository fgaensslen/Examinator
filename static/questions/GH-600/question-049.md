---
question: |
    You have a GitHub repository that uses the GitHub Copilot CLI to run autonomous tasks.

    You need to validate each generated command before it runs. Any commands that attempt to modify paths outside the repository must be blocked.

    How should you complete the YAML? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "YAML"
values_pool:
  - ".copilot/hooks.yaml"
  - ".github/workflows/hooks.yaml"
  - "false"
  - "post-exec"
  - "pre-exec"
  - "true"
correct_mapping:
  blank_1: "pre-exec"
  blank_2: "true"
---
# .copilot/hooks.yaml
version: 1
hooks:
  - name: validate-generated-command
    event: {blank_1}
    language: bash
    run: |
      set -euo pipefail
      cmd="$COPILOT_COMMAND"
      # Block absolute paths or parent traversal
      if echo "$cmd" | grep -Eq '(^|[[:space:]])/(|[[:space:]]*)(|\.\./)'; then
        echo "Blocked by guardrail: command attempts to access paths outside the repo.">&2
        exit 1
      fi
      exit 0
cli:
  hooks:
    enabled: true
    config: {blank_2}