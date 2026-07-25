---
question: "You have an Azure SQL database named SalesDB that has Query Store enabled. SalesDB supports an AI-driven product search API.


Users report that the latency of the API increased immediately after the API was deployed and remains high.


You need to identify whether the latency increase was caused by an execution plan regression and, if so, decide which corrective action will restore a previous plan. The solution must prevent any changes to the API code.


What should you use? To answer, drag the appropriate tools to the correct step. Each tool may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "Azure Monitor"
    - "Log Analytics"
    - "The Query Store plan store"
    - "Query Performance Insight"
    - "The Regressed Queries pane in Query Store"
    - "Plan forcing in Query Store"
correct_mapping:
    blank_1: "Query Performance Insight"
    blank_2: "The Regressed Queries pane in Query Store"
    blank_3: "Plan forcing in Query Store"
---
To identify long-running queries:
{blank_1}
To verify that the query has multiple persisted plans over time:
{blank_2}
To restore a previous plan without changing the code:
{blank_3}