---
question: "You have a SQL database in Microsoft Fabric that contains a table named WebSite.Logs. WebSite.Logs stores application telemetry data. WebSite.Logs contains a nvarchar (max) column named log that stores JSON documents.


You have a daily report that filters by the \\$.severity JSON property and returns LogId, LogDateTime, and log. The report frequently causes full table scans.


You need to modify WebSite.Logs to support efficient filtering by \\$.severity and avoid key lookups for the columns returned by the report.


How should you complete the Transact-SQL code to avoid full table scans? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "AS JSON_QUERY([log], '$.severity')"
    - "AS JSON_VALUE([log], '$.severity') PERSISTED"
    - "INCLUDE (log)"
    - "INCLUDE (LogId, LogDateTime, [log])"
correct_mapping:
    blank_1: "AS JSON_VALUE([log], '$.severity') PERSISTED"
    blank_2: "INCLUDE (LogId, LogDateTime, [log])"
---
ALTER TABLE WebSite.Logs
ADD severity 
{blank_1};
GO
CREATE INDEX ix_severity
ON WebSite.Logs(severity)
    {blank_2};
GO
