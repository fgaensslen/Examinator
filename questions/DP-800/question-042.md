---
question: "HOTSPOT - You have an Azure SQL database that has Query Store enabled.
Query Performance Insight shows that one stored procedure has the longest runtime. The procedure runs the following parameterized query.


CREATE OR ALTER PROCEDURE dbo.GetRecentOrders


&emsp;@CustomerId int,


&emsp;@SinceDate datetime2


AS


SELECT TOP (50)


&emsp;o.orderId, o.orderDate, o.Status, o.TotalAmount


FROM dbo.Orders AS o


WHERE o.CustomerId = @CustomerId


&emsp;AND o.OrderDate >= @SinceDate


ORDER BY o.OrderDate DESC;


The dbo.Orders table has approximately 120 million rows. CustomerId is highly selective, and OrderDate is used for range filtering and sorting. 


You have the following indexes:


Clustered index: PK_Orders on (OrderId)


Nonclustered index: IX_Orders_OrderDate on (OrderDate) with no included columns


An actual execution plan captured from Query Store for slow runs shows the following:


An index seek on IX_Orders_OrderDate followed by a Key Lookup (Clustered) on PK_Orders for CustomerId, Status, and TotalAmount


A sort operator before Top (50), because the results are ordered by OrderDate DESC


For each of the following statements, select Yes if the statement is true. Otherwise, select No.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "Yes"
    - "No"
correct_mapping:
    blank_1: "Yes"
    blank_2: "No"
    blank_3: "Yes"
---
To avoid the explicit sort for the query, create a nonclustered index on (CustomerId, OrderDate DESC) that includes (Status, TotalAmount).
{blank_1}
To eliminate the sort and make the query use an ordered seek, add CustomerId as an included column to IX_Orders_OrderDate.
{blank_2}
The plan indicates a bottleneck from a suboptimal query plan, rather locking or blocking.
{blank_3}