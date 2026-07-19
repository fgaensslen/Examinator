---
question: "You have an Azure SQL database that supports the OLTP workload of an order-processing application.


During a 10-minute incident window, you run a dynamic management view query and discover the following:


Session 72 is sleeping with open_transaction_count = 1.


Multiple other sessions show blocking_session_id = 72 in sys.dm_exec_requests. sys.dm_exec_input_buffer(72, NULL) returns only BEGIN TRANSACTION UPDATE Sales.Orders.
Users report that updates to Sales.Orders intermittently time out during the incident window. The timeouts stop only after you manually terminate session 72.


What is a possible cause of the blocking?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]A long-running SELECT statement is blocking writers.
- [ ]Session 72 caused a deadlock.
- [x]An explicit transaction was started but not committed or rolled back.
- [ ]A lock escalation occurred.
