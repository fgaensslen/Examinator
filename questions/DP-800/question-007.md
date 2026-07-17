---
question: "You have an Azure SQL database. 

You need to create a scalar user-defined function (UDF) that returns the number of whole years between an input parameter named @OrderDate and the current date/time as a single positive integer. The function must be created in Azure SQL Database.

You write the following code. 


01 CREATE FUNCTION dbo.ufnYearsSinceOrder (@OrderDate datetime2)

02 RETURNS int

03 AS

04 BEGIN

05

06 END


What should you insert at line 05? "
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]RETURN DATEDIFF(year, GETDATE(), @OrderDate);
- [ ]DATEDIFF(month, @orderdate, GETDATE()) / 12
- [ ]DATEPART(year, GETDATE()) - DATEPART(year, @orderdate)
- [x]RETURN DATEDIFF(year, @OrderDate, GETDATE());
