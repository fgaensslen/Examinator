---
question: |
  You have an Azure SQL database that contains a table named Sales.Orders. Sales.Orders contains the following columns.

  | Column | Data type |
  | :--- | :--- |
  | OrderId | int |
  | CustomerId | int |
  | OrderDate | datetime2 |
  | TotalAmount | decimal(18,2) |

  Reporting queries frequently repeat logic to calculate the number of days since an order was placed.
  
  You need to create a scalar user-defined function (UDF) that returns the number of days between an input value of @OrderDate and the current date and time.
  
  How should you complete the Transact-SQL code? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.
  
  NOTE: Each correct selection is worth one point.

question_type: "drag_drop"
values_pool:
    - "AS RETURN"
    - "DATEADD(day, @OrderDate, GETDATE())"
    - "DATEDIFF(day, @OrderDate, GETDATE())"
    - "RETURNS INT"
    - "RETURNS TABLE"
    - "WITH SCHEMABINDING"
correct_mapping:
    blank_1: "RETURNS INT"
    blank_2: "DATEDIFF(day, @OrderDate, GETDATE())"
---
CREATE FUNCTION dbo.ufn_DaysSinceOrder
(
    @OrderDate datetime2(0)
)
{blank_1}
BEGIN
    DECLARE @Days int;
    SELECT @Days = {blank_2};
    RETURN @Days;
END;
GO