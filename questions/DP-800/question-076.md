---
question: "You have an Azure SQL database that supports an AI-enabled product catalog API. The database contains a table named Sales.Orders. Sales.Orders contains 20 million rows and has a nonclustered index on a column named CreateDate.


The API passes a date parameter named @OrderDate.


You have a stored procedure named get_latest_day_orders that filters by running the following query.


WHERE CAST(CreateDate AS date) = @0rderDate.


A review of the query execution reveals that the query causes an index scan.


You need to modify the predicate to ensure that Microsoft SQL Server can use an index seek on CreateDate for a single day.


Which WHERE clause should you use?"
documentation: "https://learn.microsoft.com/en-us/azure/cognitive-services/responsible-use-of-ai"
---
- [x]WHERE CreateDate >= @OrderDate AND CreateDate < DATEADD(day, 1, @0rderDate)
- [ ]WHERE CreateDate LIKE CONVERT(char(10), @0rderDate, 121) + ‘%’
- [ ]WHERE LEFT(CONVERT(varchar(30), CreateDate, 121), 10) = CONVERT(char(10), @0rderDate, 121)
- [ ]WHERE CONVERT(char(10), CreateDate, 121) = CONVERT(char(10), @OrderDate, 121)
