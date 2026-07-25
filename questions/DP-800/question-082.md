---
question: "You have a SQL database in Microsoft Fabric named SalesDB that contains a table named dbo.Products. You need to modify SalesDB to meet the following requirements:


Create a vector index on the appropriate column.


Use a supplied natural language query vector.


How should you complete the Transact-SQL code? To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "distance"
    - "embedding"
    - "product_name"
    - "VECTOR_DISTANCE"
    - "VECTOR_NORMALIZE"
    - "VECTOR_SEARCH"
    - "GROUP BY s.distance"
    - "ORDER BY s.distance"
    - "PARTITION BY s.distance"
correct_mapping:
    blank_1: "embedding"
    blank_2: "VECTOR_SEARCH"
    blank_3: "ORDER BY s.distance"
---
CREATE VECTOR INDEX idx_products_embedding ON dbo.Products ( 
    {blank_1} )
WITH (METRIC = 'cosine', TYPE = 'DiskANN');

DECLARE @query_vector VECTOR(1536) = @SuppliedVector

SELECT
    t.product_id,
    t.product_name,
    s.distance

FROM 
    {blank_2} (
    TABLE = dbo.Products AS t,
    COLUMN = embedding,
    SIMILAR_TO = @query_vector,
    METRIC = 'cosine',
    TOP_N = 10
) AS s

{blank_3};