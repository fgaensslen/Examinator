---
question: "You have an Azure SQL database that contains a table named stores. stores contains a column named description and a vector column named embedding.


You need to implement a hybrid search query that meets the following requirements:


Uses full-text search on description for the keyword portion


Returns the top 20 results based on a combined score that uses a weighted formula of 60% vector distance and 40% full-text rank


How should you configure the query components? To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "VECTOR_DISTANCE and order by distance ascending"
    - "VECTOR_SEARCH with METRIC cosine and TOP_N"
    - "VECTORPROPERTY to calculate the similarity between two vectors"
    - "CONTAINSTABLE on description and return ranked matches"
    - "FREETEXTTABLE on description for keyword scoring"
    - "JSON_VALUE extraction from description for keyword scoring"
    - "order by (distance * 0.6) + ((1.0 - RANK/1000.0) * 0.4)"
    - "order by (distance * 0.6) + (RANK * 0.4)"
    - "order by (distance + RANK), and then apply TOP 20"
correct_mapping:
    blank_1: "VECTOR_DISTANCE and order by distance ascending"
    blank_2: "CONTAINSTABLE on description and return ranked matches"
    blank_3: "order by (distance * 0.6) + ((1.0 - RANK/1000.0) * 0.4)"
---
Semantic query operator/function:
{blank_1}
Keyword retrieval operator/function:
{blank_2}
Final ranking expression:
{blank_3}