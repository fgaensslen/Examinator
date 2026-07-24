---
question: "You have an Azure SQL database that contains a table named dbo.Orders. dbo.Orders contains a column named CreateDate that stores order creation dates.


You need to create a stored procedure that filters Orders by CreateDate for a single calendar day. The solution must be SARGable. 


How should you complete the Transact-SQL code? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "@EndDate"
    - "@StartDate"
    - "CONVERT(char(10), CreateDate, 121)"
    - "CONVERT(date, @StartDate)"
    - "DATEADD(day, 1, @StartDate)"
    - "GETDATE()"
correct_mapping:
    blank_1: "DATEADD(day, 1, @StartDate)"
    blank_2: "@StartDate"
    blank_3: "@EndDate"
---
CREATE PROCEDURE dbo.usp_SearchOrders
    @StartDate date
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @EndDate date;
    SET @EndDate = 
    {blank_1}
    SELECT  o.CreateDate,
            o.OrderId,
            o.ShipDate
    FROM    dbo.Orders AS o
    WHERE   o.CreateDate >= 
    {blank_2}
    AND o.CreateDate <  
    {blank_3} ;
END;
GO
