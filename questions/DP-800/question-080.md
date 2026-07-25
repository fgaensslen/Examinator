---
question: "You have an Azure SQL database named SalesDB that contains tables named Sales.Orders and Sales.OrderLines. Both tables contain sales data. You have a Retrieval Augmented Generation (RAG) service that queries SalesDB to retrieve order details and passes the results to a large language model (LLM) as JSON text. The following is a simple of the JSON."
question_type: "drag_drop"
values_pool:
    - "JSON_MODIFY"
    - "OPENJSON"
    - "FOR JSON PATH"
    - "JSON_QUERY"
    - "JSON_VALUE"
correct_mapping:
    blank_1: "FOR JSON PATH"
    blank_2: "JSON_QUERY"
    blank_3: "JSON_VALUE"
---
Serialize the order-level JSON:
{blank_1}
Generate a nested lines array:
{blank_2}
Extract a single scalar value from the JSON text:
{blank_3}