---
question: "You have an Azure SQL database that supports a customer-facing API. The API calls a stored procedure named dbo.GetCustomerOrders thousands of times per hour.

After a deployment that updated indexes and statistics, users report that the API endpoint backed by dbo.GetCustomerOrders is slower. In Query Store, the same query now has two persisted execution plans. During the last hour, the newer plan had a significantly higher average duration and CPU time than the older plan.

You need to restore the previous performance quickly, without changing the API code.
Which Transact-SQL command should you run?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]EXEC sys.sp_query_store_set_hints
- [ ]DBCC FREEPROCCACHE
- [x]EXEC sp_query_store_force_plan
- [ ]ALTER DATABASE
