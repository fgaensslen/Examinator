---
question: "You have an Azure AI Search service and an index named hotels that includes a vector field named DescriptionVector. You query hotels by using the Search Documents REST API.


You add semantic ranking to the hybrid search query and discover that some queries return fewer results than expected, and captions and answers are missing.


You need to complete the hybrid search request to meet the following requirements:


Include more documents when ranking.


Always include captions and answers.


How should you complete the REST request body? To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "-50,"
    - "10,"
    - "50,"
    - "\"full\","
    - "\"semantic\","
    - "\"simple\","
    - "\"extractive\","
    - "\"generative\","
    - "\"none\","
correct_mapping:
    blank_1: "50,"
    blank_2: "\"semantic\","
    blank_3: "\"extractive\","
    blank_4: "\"extractive\","
---
{
    "search": "ocean view",
    "vectorqueries": [
        {
            "vector": [/* embedding array */],
            "fields": "DescriptionVector",
            "k": {blank_1}
            "kind": "vector"
        }
    ],
    "queryType": {blank_2}
    "semanticConfiguration": "hotels",
    "captions": {blank_3}
    "answers": {blank_4}
    "top": 10,
    "hybridSearch": { "maxTextRecallSize": 50 }
}