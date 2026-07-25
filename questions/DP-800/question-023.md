---
question: "You have an Azure SQL database that contains a table named Table1. Table1 contains 25,000,000 rows of data and a datetime2 column named DateKey. The data in Table1 spans the years 2020 through 2021.


You need to partition the data in Table1 by year. The solution must minimize how long it takes to rebuild or reindex the table.


How should you complete the Transact-SQL code? To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "PARTITION"
    - "RANGE LEFT"
    - "RANGE RIGHT"
    - "'2019-01-01 00:00:00', '2020-01-01 00:00:00', '2021-12-31 23:59:59'"
    - "'2019-12-31 23:59:59', '2020-12-31 23:59:59'"
    - "'2020-01-01 00:00:00', '2020-02-01 00:00:00', '2020-03-01 00:00:00'"
    - "'2020-01-01 00:00:00', '2021-01-01 00:00:00'"
correct_mapping:
    blank_1: "RANGE RIGHT"
    blank_2: "'2020-01-01 00:00:00', '2021-01-01 00:00:00'"
---
CREATE PARTITION FUNCTION PartitionByYear (datetime2)
AS
{blank_1}
FOR VALUES
( {blank_2} );