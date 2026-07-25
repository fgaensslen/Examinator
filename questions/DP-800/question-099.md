---
question: "You have an Azure SQL managed instance that supports a gaming leaderboard API and contains a table named dbo.Leaderboard.


You plan to reduce write latency during peak events of dbo.Leaderboard.


You need to ensure that dbo.Leaderboard supports point lookups. The leaderboard information does NOT need to persist after a restart.


Which type of table and index should you configure?


To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "Rowstore disk-based"
    - "SCHEMA_AND_DATA in-memory"
    - "SCHEMA_ONLY in-memory"
    - "HASH"
    - "Nonclustered"
    - "Nonclustered columnstore"
correct_mapping:
    blank_1: "SCHEMA_ONLY in-memory"
    blank_2: "HASH"
---
Table type:
{blank_1}
Index type:
{blank_2}