---
question: "You have an Azure SQL database named SalesDB that contains tables named Sales.Orders and Sales.OrderLines. Both tables contain sales data. You have a Retrieval Augmented Generation (RAG) service that queries SalesDB to retrieve order details and passes the results to a large language model (LLM) as JSON text.


You need to return one JSON document per order that includes the order header fields and an array of related order lines. The LLM must receive a single JSON array of orders, where each order contains a lines property that is a JSON array of line items.


Which Transact-SQL commands should you use to produce the required JSON shape from the relational tables? To answer, drag the appropriate commands to the correct operations. Each command may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point.


The following is a simple of the JSON.


```json
[


  {


    \"orderHeaderId\": 102348,


    \"orderNumber\": \"SO-2026-000912\",


    \"orderDateUtc\": \"2026-01-28T14:22:09Z\",


    \"customerId\": 77821,


    \"currencyCode\": \"EUR\",


    \"orderTotal\": 149.97,


    \"lines\": [


      {
        \"lineNumber\": 1,


        \"productId\": 5012,


        \"sku\": \"CBL-USB-C-1M\",


        \"quantity\": 2,


        \"unitPrice\": 19.99,


        \"lineTotal\": 39.98


      },


      {


        \"lineNumber\": 2,


        \"productId\": 8841,


        \"sku\": \"HUB-USB-C-7P\",


        \"quantity\": 1,


        \"unitPrice\": 109.99,


        \"lineTotal\": 109.99


      }


    ]


  }


]"
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