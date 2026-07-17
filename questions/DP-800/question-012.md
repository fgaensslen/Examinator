---
question: "You have an Azure SQL database named AdventureWorksDB that contains a table named dbo.Employee. 

You have a C# Azure Functions app that uses an HTTP-triggered function with an Azure SQL input binding to query dbo.Employee. 

You are adding a second function that will react to row changes in dbo.Employee and write structured logs. 

You need to configure AdventureWorksDB and the app to meet the following requirements: 

Changes to dbo.Employee must trigger the new function within five seconds.

Each invocation must process no more than 100 changes.

Which two database configurations should you perform? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point."
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]Create an AFTER trigger on dbo.Employee for Data Manipulation Language (DML).
- [ ]Set Sql_Trigger_MaxBatchSize to 100.
- [x]Enable change tracking on the dbo.Employee table.
- [x]Enable change tracking at the database level.
- [ ]Set Sql_Trigger_PollingIntervalMs to 5000.
- [ ]Enable change data capture (CDC) for dbo.Employee table changes.