---
question: "HOTSPOT - You have a SQL database in Microsoft Fabric that uses the default settings for a newly created database and contains a table named Sales.Orders. You have an application that uses two stored procedures to access Sales.Orders. While monitoring database activity, you discover the following: • sys.dm_exec_requests shows multiple sessions in a suspended state with wait_type = LCK_M_X. All the sessions show the same wait_resource, which maps to Sales.Orders, and the same nonzero blocking_session_id. • sys.dm_exec_input_buffer(blocking_session_id, NULL) returns a last submitted command of BEGIN TRANSACTION UPDATE Sales.Orders. • sys.dm_exec_sessions for the blocking session shows status = sleeping and open_transaction_count = 1. For each of the following statements, select Yes if the statement is true. Otherwise, select No. NOTE: Each correct selection is worth one point."
documentation: "https://learn.microsoft.com/en-us/azure/"
---

