---
question: "DRAG DROP -
You have a SQL database in Microsoft Fabric that contains a table named WebSite.Logs. WebSite.Logs stores application telemetry data. WebSite.Logs contains a nvarchar (max) column named log that stores JSON documents.


You have a daily report that filters by the \\$.severity JSON property and returns LogId, LogDateTime, and log. The report frequently causes full table scans.

You need to modify WebSite.Logs to support efficient filtering by \\$.severity and avoid key lookups for the columns returned by the report.


How should you complete the Transact-SQL code to avoid full table scans? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."
documentation: "https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server"
---

