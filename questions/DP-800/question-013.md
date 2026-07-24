---
question: "DRAG DROP - 


You have a Microsoft SQL Server 2025 database that contains a table named dbo.CustomerMessages. dbo.CustomerMessages contains two columns named MessageID (int) and MessageRaw (nvarchar(max)). 


MessageRaw can contain a phone number in multiple formats, and some rows do NOT contain a phone number. 


You need to write a single SELECT query that meets the following requirements: 


The query must return MessageID, RawNumber, DigitsOnly, and PhoneStatus. 


RawNumber must contain the first substring that matches a phone-number pattern, or NULL if no match exists. 


DigitsOnly must remove all non-digit characters from RawNumber, or return NULL.


PhoneStatus must return valid when a phone number exists in MessageRaw, otherwise return Missing.


How should you complete the Transact-SQL query? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."

question_type: "drag_drop"
values_pool:
  - "REGEXP_COUNT("
  - "REGEXP_INSTR("
  - "REGEXP_LIKE("
  - "REGEXP_REPLACE( REGEXP_SUBSTR("
  - "REGEXP_SUBSTR("
  - "STRING_SIMILARITY("
correct_mapping:
  blank_1: "REGEXP_SUBSTR("
  blank_2: "REGEXP_REPLACE( REGEXP_SUBSTR("
  blank_3: "REGEXP_COUNT("
---
SELECT
    MessageID,
    {blank_1}
    MessageRaw, '\d{3}[()\-\s]*\d{3}[\-\s]*\d{4}' ) AS RawNumber,
    {blank_2}
    MessageRaw, '\d{3}[()\-\s]*\d{3}[\-\s]*\d{4}' ),'\D', '') AS DigitsOnly,
    CASE
    WHEN 
    {blank_3}
    MessageRaw, '\d{3}[()\-\s]*\d{3}[\-\s]*\d{4}') = 1
    THEN 'Valid'
    ELSE 'Missing'
    END AS PhoneStatus
FROM dbo.CustomerMessages;
