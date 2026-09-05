---
question: |
    You have an Azure SQL database that contains a table named dbo.SupportTickets. dbo.SupportTickets contains a JSON column named Payload and a datetime column CreatedAt. You need to generate a report for the last seven days that meets the following requirements:

    - Returns exactly one row per customer per day
    - For each customer and day, returns the earliest ticket
    - Includes the customer ID stored in Payload

    How should you complete the Transact-SQL query? To answer, select the appropriate options in the answer area.

    NOTE: Each correct selection is worth one point.
    
question_type: "drag_drop"
values_pool:
    - "DENSE_RANK"
    - "JSON_VALUE"
    - "OPENJSON"
    - "ROW_NUMBER"
    - "1"
    - "7"
    - "DATEDIFF(day, -7, SYSUTCDATETIME())"
correct_mapping:
    blank_1: "JSON_VALUE"
    blank_2: "ROW_NUMBER"
    blank_3: "1"
---
WITH TicketRanks AS
(
SELECT
    t.TicketId,
    CAST(t.CreatedAt AS date) AS TicketDate,
    {blank_1} (t.Payload, '$.customer.id') AS CustomerId,
    t.CreatedAt,
    {blank_2}() OVER
    (
        PARTITION BY
            CAST(t.CreatedAt AS date),
            JSON_VALUE(t.Payload, '$.customer.id')
        ORDER BY t.CreatedAt ASC
    ) AS rn
FROM dbo.SupportTickets AS t
WHERE t.CreatedAt >= DATEADD(day, -7, SYSUTCDATETIME())
)
SELECT
    TicketDate,
    CustomerId,
    TicketId,
    CreatedAt
FROM TicketRanks
WHERE rn = {blank_3}
ORDER BY TicketDate, CustomerId;