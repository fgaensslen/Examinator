---
question: "You have an Azure AI Search service and an index named hotels that includes a vector field named DescriptionVector.


You query hotels by using the Search Documents REST API.


You need to implement a hybrid search query that uses DescriptionVector and includes captions.


How should you complete the REST request body?


To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "\"default\""
    - "\"full\""
    - "\"generative\""
    - "\"hybrid\""
    - "\"none\""
    - "\"simple\""
    - "\"semantic\""
    - "\"extractive\""
    - "\"hotels\""
correct_mapping:
    blank_1: "\"semantic\""
    blank_2: "\"hotels\""
    blank_3: "\"extractive\""
---
{
    "search": "ocean view",
    "queryType": {blank_1},
    "semanticConfiguration": {blank_2},
    "captions": {blank_3},
    "top": 10,
    "hybridSearch": { "maxTextRecallSize": 50 },
    "vectorQueries": [
        {
            "kind": "vector",
            "vector": [/* embedding array */],
            "fields": "DescriptionVector",
            "k": 50
        }
    ]
}