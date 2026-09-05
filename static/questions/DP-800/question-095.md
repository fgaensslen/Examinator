---
question: "You have a SQL database in Microsoft Fabric that contains a table named dbo.Products. dbo.Products contains product catalog data.


You need to create a stored procedure that performs hybrid search. The solution must meet the following requirements:


- Use approximate nearest neighbor (ANN) to retrieve the top 20 candidate products.


- Re-rank only the candidates that also match a full-text query.


- Generate the query embedding.


How should you complete the Transact-SQL code? To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "AI_GENERATE_EMBEDDINGS"
    - "SEMANTICKEYPHRASETABLE"
    - "VECTOR_NORMALIZE"
    - "VECTOR_SEARCH"
    - "CONTAINSTABLE"
    - "SEMANTICSIMILARITYTABLE"
    - "VECTOR_DISTANCE"
    - "FREETEXTTABLE"
    - "SEMANTICSIMILARITYDETAILSTABLE"
correct_mapping:
    blank_1: "AI_GENERATE_EMBEDDINGS"
    blank_2: "VECTOR_SEARCH"
    blank_3: "CONTAINSTABLE"
---
CREATE OR ALTER PROCEDURE dbo.SearchProducts
    @query_text NVARCHAR(4000),
    @keywords   NVARCHAR(4000)
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @qv VECTOR(1536) = 
    {blank_1}(@query_text USE MODEL Ada2Embeddings);
    ;WITH ann AS
    (
        SELECT t.product_id, t.product_name, s.distance
        FROM {blank_2} (
            TABLE = dbo.Products AS t,
            COLUMN = embedding,
            SIMILAR_TO = @qv,
            TOP_N = 20,
            METRIC = 'cosine'
        ) AS s
    )
    SELECT TOP (20)
        t.product_id,
        t.product_name,
        ann.distance,
        fts.RANK AS text_rank
    FROM ann
    JOIN dbo.Products AS t
        ON t.product_id = ann.product_id
    JOIN 
    {blank_3} (dbo.Products, description, @keywords) AS fts
        ON t.product_id = fts.[KEY]
    ORDER BY (ann.distance * 0.6) + ((1.0 - fts.RANK/1000.0) * 0.4);
END;
GO