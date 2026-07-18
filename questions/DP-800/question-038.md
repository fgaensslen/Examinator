---
question: "You have an Azure SQL database that stores order data.
A reporting query aggregates monthly revenue per customer runs frequently.
You need to reduce how long it takes to retrieve the calculated values. The solution must NOT alter any underlying table structure. What should you do?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]Create a view by using ORDER BY without TOP, and then create a unique clustered index on the view.
- [ ]Create a view without using WITH SCHEMABINDING, and then create a nonclustered index on the view.
- [ ]Create a view by using GROUP BY, and then create a unique clustered index on the view.
- [x]Create a view by using WITH SCHEMABINDING, include COUNT_BIG(*), and then create a unique clustered index on the view.
