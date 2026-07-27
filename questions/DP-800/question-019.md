---
question: "You have an Azure SQL database named SalesDB that supports an ecommerce application. SalesDB contains a table named dbo.Orders that has a clustered index on a column named OrderId.


dbo.Orders receives continuous OLTP inserts and updates during business hours.


Your analytics team runs hourly aggregate queries that scan dbo.Orders to calculate revenue trends for recent dates.


You need to improve the performance of the hourly analytics queries without significantly affecting OLTP throughput. The solution must meet the following requirements:


• Support near-real-time (NRT) analytics on the dbo.Orders table.


• Reduce read time when retrieving analytical data from dbo.Orders.


• Support indexing only rows that match a predicate, such as Active = 1.


Which type of index should you use for each requirement? To answer, drag the appropriate index types to the correct requirements. Each index type may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "A clustered columnstore index"
    - "A clustered rowstore index ordered by key columns"
    - "A filtered nonclustered index with a WHERE predicate"
    - "A nonclustered columnstore index on an existing rowstore table"
correct_mapping:
    blank_1: "A nonclustered columnstore index on an existing rowstore table"
    blank_2: "A nonclustered columnstore index on an existing rowstore table"
    blank_3: "A filtered nonclustered index with a WHERE predicate"
---
Support NRT analytics on dbo.Orders: 
{blank_1}
Reduce read time when retrieving analytical data: 
{blank_2}
Index only rows that match a predicate: 
{blank_3}