---
question: "Your company has an ecommerce catalog in a Microsoft SQL Server 2025 database named SalesDB. SalesDB contains a table named products. products contains the following columns: product_id (int) product_name (nvarchar(200)) description (nvarchar(max)) category (nvarchar(50)) brand (nvarchar(50)) price (decimal) sku (nvarchar(40))


The description fields are updated daily by a content pipeline, and price can change multiple times per day. You want customers to be able to submit natural language queries and apply structured filters for brand and price.


You plan to store embeddings in a new VECTOR(1536) column and use VECTOR_SEARCH(... METRIC=‘cosine’ ...).


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
Generating an embedding by concatenating product_name, category, and description will support the customer requirements.
{blank_1}
Including price in the text used to generate embeddings is required.
{blank_2}
The underlying base type of the embeddings will be float(32).
{blank_3}