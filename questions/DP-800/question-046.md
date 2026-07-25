---
question: "You have a SQL database in Microsoft Fabric that contains the following functions:


A multi-statement table-valued function (TVF) named Sales.mstvf_OrderStatus() that returns order status information


A scalar user-defined function (UDF) named dbo.ufn_GetTaxMultiplier (@TaxAmt money, @StateCode char(2)) that returns a numeric multiplier used in tax calculations


Reporting queries frequently join Sales.mstvf_OrderStatus() to a table named Sales.SalesOrderHeader and return large result sets. A performance review shows that the queries produce inconsistent execution plans.


During a code review, a developer discovers that the following Transact-SQL statement produced an error.


EXEC @ret = ufn_GetTaxMultiplier @TaxAmt = 100.00, @StateCode = 'WA';


For each of the following statements, select Yes if the statement is true. Otherwise, select No.

NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "Yes"
    - "No"
correct_mapping:
    blank_1: "No"
    blank_2: "Yes"
    blank_3: "No"
---
You can use GETDATE() in dbo.ufn_GetTaxMultiplier to produce nondeterministic results.
{blank_1}
Rewriting sales.mstvf_OrderStatus() as an inline table TVF will reduce the number of inconsistent execution plans.
{blank_2}
Replacing ufn_GetTaxMultiplier with dbo.ufn_GetTaxMultiplier in the EXEC function statement will resolve the error.
{blank_3}