---
question: "You need to create a solution that meets the development requirements for retrieving the patient transaction data. The solution must ensure that database developers use the resulting data to join to other tables.


How should you complete the Transact-SQL code? To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "FUNCTION"
    - "PROCEDURE"
    - "VIEW"
    - "GROUP BY t.CustomerId"
    - "GROUP BY t.TransactionDate"
    - "PARTITION BY t.CustomerId"
    - "PARTITION BY t.TransactionDate"
    - "HAVING DATEDIFF(DAY, t.TransactionDate, GETDATE()) = 1"
    - "HAVING SUM (t.Amount) > 0"
    - "ORDER BY t.TransactionDate, t.TransactionId"
    - "ORDER BY t.TransactionId, t.CustomerId"
correct_mapping:
    blank_1: "FUNCTION"
    blank_2: "PARTITION BY t.CustomerId"
    blank_3: "ORDER BY t.TransactionDate, t.TransactionId"
---
CREATE
{blank_1} dbo.CustomerTransactionsBetweenDates
(
    @CustomerId INT,
    @StartDate DATETIME2,
    @EndDate DATETIME2
)
RETURNS TABLE
AS
RETURN
(
    SELECT
        t.TransactionId,
        t.CustomerId,
        t.TransactionDate,
        t.Amount,
        SUM(t.Amount) OVER (
            {blank_2}
            {blank_3}
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS RunningTotal
    FROM dbo.Transactions AS t
    WHERE t.CustomerId = @CustomerId
    AND t.TransactionDate >= @StartDate
    AND t.TransactionDate <= @EndDate
);