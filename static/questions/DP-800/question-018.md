---
question: |
    You have an Azure SQL database that contains a table named dbo.Customers. dbo.Customers contains the following columns:

    - CustomerId (int)(primary key)
    - ProfileJson (nvarchar(max))

    You have an application that returns phone numbers in a format of +000 000-000-0000. The phone numbers are stored in ProfileJson.

    You need to write a query that returns:

    - One row per customer
    - A PhoneNUmerals column that contains only the digits

    How should you complete the Transact-SQL query? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

    NOTE: Each correct selection is worth one point.
    
question_type: "drag_drop"
values_pool:
    - "JSON_QUERY(c.ProfileJson, '$.contact.phone')"
    - "JSON_VALUE(c.ProfileJson, '$.contact.phone')"
    - "OPENJSON(c.ProfileJson, '$.contact.phone')"
    - "p.PhoneRaw"
    - "REGEXP_LIKE(p.PhoneRaw, '[^0-9]', '')"
    - "REGEXP_REPLACE(p.PhoneRaw, '[^0-9]', '')"
    - "REGEXP_SUBSTR(p.PhoneRaw, '[0-9]+')"
correct_mapping:
    blank_1: "JSON_VALUE(c.ProfileJson, '$.contact.phone')"
    blank_2: "REGEXP_REPLACE(p.PhoneRaw, '[^0-9]', '')"
    blank_3: "p.PhoneRaw"
---
WITH PhoneCTE AS
(
    SELECT  DISTINCT c.CustomerId,
        {blank_1} AS PhoneRaw
    FROM dbo.Customers AS c
)
SELECT
    p.CustomerId,
    {blank_2} AS PhoneNUmerals
FROM PhoneCTE AS p
WHERE 
{blank_3} IS NOT NULL;