---
question: |
    You have a SQL database in Microsoft Fabric that uses the default settings for a newly created database and contains a table named Sales.Orders.

    You have an application that uses two stored procedures to access Sales.Orders.

    While monitoring database activity, you discover the following:

    - sys.dm_exec_requests shows multiple sessions in a suspended state with wait_type = LCK_M_X. All the sessions show the same wait_resource, which maps to Sales.Orders, and the same nonzero blocking_session_id.
    - sys.dm_exec_input_buffer(blocking_session_id, NULL) returns a last submitted command of BEGIN TRANSACTION UPDATE Sales.Orders.
    - sys.dm_exec_sessions for the blocking session shows status = sleeping and open_transaction_count = 1.

    For each of the following statements, select Yes if the statement is true. Otherwise, select No.

    NOTE: Each correct selection is worth one point.
    
question_type: "drag_drop"
values_pool:
    - "Yes"
    - "No"
correct_mapping:
    blank_1: "Yes"
    blank_2: "Yes"
    blank_3: "Yes"
---
The blocking is caused by an uncommitted explicit transaction in the blocking session that is holding locks.
{blank_1}
While an UPDATE operation on Sales.Orders is occurring, SELECT statements will be blocked.
{blank_2}
Joining sys.dm_tran_locks to sys.dm_exec_requests will show which session holds locks involved in the blocking chain.
{blank_3}