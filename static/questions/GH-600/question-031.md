---
question: |
    You need to implement agent2 to meet the technical requirements.

    How should you complete the YAML configuration? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
code_lang: "YAML"
values_pool:
  - "'agent',"
  - "'edit',"
  - "'search',"
  - "'execute','"
  - "'read','"
  - "'web',"
correct_mapping:
  blank_1: "'search',"
  blank_2: "'read',"
---
name: implementation-planner
description: Creates detailed implementation plans and technical specifications in markdown format
tools: [
    {blank_1}
    {blank_2}
    'microsoftdocs/mcp/docs_search',
    'microsoftdocs/mcp/docs_fetch',
]