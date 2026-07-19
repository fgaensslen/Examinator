---
question: "Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution. After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen. You have a SQL database in Microsoft Fabric that contains a table named dbo.Orders. dbo.Orders has a clustered index, contains three years of data, and is partitioned by a column named OrderDate by month. You need to remove all the rows for the oldest month.


The solution must minimize the impact on other queries that access the data in dbo.Orders.


Solution: Run the following Transact-SQL statement.


DELETE FROM dbo.Orders -


WHERE OrderDate < DATEADD(month, -36, SYSUTCDATETIME());


Does this meet the goal?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]Yes
- [x]No
