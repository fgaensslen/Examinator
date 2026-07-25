---
question: "You have an Azure SQL database that supports an AI-driven product search API.


You need to identify the top CPU-consuming queries from the last two hours by using Query Store data. The solution must aggregate CPU consumption across executions and return only the top 15 query hashes.


How should you complete the Transact-SQL code? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "DATEADD(DAY, -2, GETDATE())"
    - "DATEADD(HOUR, -2, GETUTCDATE())"
    - "rs.last_cpu_time"
    - "rs.avg_cpu_time"
    - "sys.dm_exec_query_stats"
    - "sys.query_store_runtime_stats_interval"
correct_mapping:
    blank_1: "rs.avg_cpu_time"
    blank_2: "sys.query_store_runtime_stats_interval"
    blank_3: "DATEADD(HOUR, -2, GETUTCDATE())"
---
WITH AggregatedCPU AS
(
    SELECT
        q.query_hash,
        SUM(count_executions *
        {blank_1} / 1000.0) AS total_cpu_ms
    FROM sys.query_store_query_text AS qt
    INNER JOIN sys.query_store_query AS q
        ON qt.query_text_id = q.query_text_id
    INNER JOIN sys.query_store_plan AS p
        ON q.query_id = p.query_id
    INNER JOIN sys.query_store_runtime_stats AS rs
        ON rs.plan_id = p.plan_id
    INNER JOIN
        {blank_2} AS rsi
        ON rsi.runtime_stats_interval_id = rs.runtime_stats_interval_id
    WHERE rs.execution_type_desc IN ('Regular', 'Aborted', 'Exception')
    AND rsi.start_time >= {blank_3}
    GROUP BY q.query_hash
),
OrderedCPU AS
(
    SELECT
        query_hash,
        total_cpu_ms,
        ROW_NUMBER() OVER (ORDER BY total_cpu_ms DESC, query_hash ASC) AS rn
    FROM AggregatedCPU
)
SELECT query_hash, total_cpu_ms
FROM OrderedCPU
WHERE rn <= 15
ORDER BY total_cpu_ms DESC;