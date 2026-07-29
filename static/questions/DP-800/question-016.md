---
question: "You need to create a solution that meets the development requirements for retrieving the patient lists.


How should you complete the Transact-SQL code? To answer, select the appropriate options in the answer area

NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "WHERE EXISTS"
    - "WHERE NOT EXISTS"
    - "WHERE p.PatientId IN"
    - "WHERE p.PatientId NOT IN"
    - "HAVING p.PatientId = pr.PatientId"
    - "HAVING p.TransactionId = pr.TransactionId"
    - "WHERE p.PatientId = pr.PatientId"
    - "WHERE p.TransactionId = pr.TransactionId"
correct_mapping:
    blank_1: "WHERE p.PatientId IN"
    blank_2: "WHERE p.PatientId = pr.PatientId"
---
CREATE PROCEDURE dbo.GetActivePatients
AS
BEGIN
    SET NOCOUNT ON;
    SELECT p.Name
    FROM dbo.Patients AS p
    {blank_1}(
        SELECT PatientId
        FROM dbo.Procedures AS pr
        {blank_2}
        AND pr.TransactionDate >= DATEADD(DAY, -30, SYSUTCDATETIME())
    );
END;
