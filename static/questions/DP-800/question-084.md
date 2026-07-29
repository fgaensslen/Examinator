---
question: "You have an Azure SQL database named DB1 that contains two tables named knowledge_base and query_cache. knowledge_base contains support articles and embeddings. query_cache contains chat questions, responses, and embeddings. DB1 supports an AI-enabled chat agent.


You need to design a solution that meets the following requirements:


Serializes the retrieved rows from knowledge_base


Extracts the answer field from the response


Extracts the embeddings to store in query_cache


You will call the external large language model (LLM) by using the sp_invoke_external_rest_endpoint stored procedure.


Which Transact-SQL commands should you use for each requirement? To answer, drag the appropriate commands to the correct requirements. Each command may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
code_lang: "TEXT"
values_pool:
    - "AI_GENERATE_CHUNKS"
    - "FOR XML PATH"
    - "OPENJSON"
    - "VECTOR_DISTANCE"
    - "FOR JSON PATH"
    - "JSON_VALUE"
    - "JSON_QUERY"
correct_mapping:
    blank_1: "FOR JSON PATH"
    blank_2: "JSON_VALUE"
    blank_3: "JSON_QUERY"
---
Serialize the retrieved rows from knowledge_base:
{blank_1}
Extract the answer field from the response:
{blank_2}
Extract the embeddings to store in query_cache:
{blank_3}