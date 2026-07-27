---
question: "You have an Azure SQL database that supports an OLTP application.
You need to write Transact-SQL code that returns blocking chain details. The output must return only sessions that are blocked or are blocking other sessions.


How should you complete the code? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "CROSS APPLY sys.dm_exec_sql_text (r.sql_handle)"
    - "FROM sys.dm_exec_requests"
    - "FROM sys.dm_tran_locks"
    - "INNER JOIN sys.dm_tran_locks"
    - "LEFT OUTER JOIN sys.dm_exec_requests"
    - "OUTER APPLY sys.dm_exec_input_buffer(r.session_id, 0)"
    - "OUTER APPLY sys.dm_exec_input_buffer(s.session_id, NULL)"
    - "OUTER APPLY sys.dm_exec_sql_text (r.sql_handle)"
correct_mapping:
    blank_1: "FROM sys.dm_exec_requests"
    blank_2: "LEFT OUTER JOIN sys.dm_exec_requests"
    blank_3: "OUTER APPLY sys.dm_exec_sql_text (r.sql_handle)"
    blank_4: "OUTER APPLY sys.dm_exec_input_buffer(s.session_id, NULL)"
---
WITH cteBL (session_id, blocking_these) AS
(
    SELECT
        s.session_id,
        blocking_these = x.blocking_these
    FROM sys.dm_exec_sessions AS s
    CROSS APPLY
    (
        SELECT
            ISNULL(CONVERT(varchar(6), er.session_id), '') + ', '
        {blank_1} AS er
        WHERE er.blocking_session_id = ISNULL(s.session_id, 0)
        AND er.blocking_session_id <> 0
        FOR XML PATH('')
    ) AS x(blocking_these)
)
SELECT
    s.session_id,
    blocked_by = r.blocking_session_id,
    bl.blocking_these,
    batch_text = t.text,
    input_buffer = ib.event_info
FROM sys.dm_exec_sessions AS s
{blank_2} AS r ON r.session_id = s.session_id
INNER JOIN cteBL AS bl ON s.session_id = bl.session_id
{blank_3} AS t
{blank_4} AS ib
WHERE bl.blocking_these IS NOT NULL
OR r.blocking_session_id > 0
ORDER BY LEN(bl.blocking_these) DESC, r.blocking_session_id DESC, r.session_id;