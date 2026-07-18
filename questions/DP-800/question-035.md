---
question: "HOTSPOT - You have a SQL database in Microsoft Fabric that contains the following functions:
A multi-statement table-valued function (TVF) named Sales.mstvf_OrderStatus() that returns order status information
A scalar user-defined function (UDF) named dbo.ufn_GetTaxMultiplier (@TaxAmt money, @StateCode char(2)) that returns a numeric multiplier used in tax calculations
Reporting queries frequently join Sales.mstvf_OrderStatus() to a table named Sales.SalesOrderHeader and return large result sets. A performance review shows that the queries produce inconsistent execution plans.


During a code review, a developer discovers that the following Transact-SQL statement produced an error.

EXEC @ret = ufn_GetTaxMultiplier @TaxAmt = 100.00, @StateCode = ‘WA’;
For each of the following statements, select Yes if the statement is true. Otherwise, select No.

NOTE: Each correct selection is worth one point."
documentation: "https://learn.microsoft.com/en-us/azure/"
---

