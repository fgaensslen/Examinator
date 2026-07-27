---
question: "You have an Azure SQL database that contains a table named dbo.Orders. 


You have an application that calls a stored procedure named dbo.usp_CreateOrder to insert rows into dbo.Orders.


When an insert fails, the application receives inconsistent error details.


You need to implement error handling to ensure that any failures inside the procedure abort the transaction and return a consistent error to the
caller.


How should you complete the stored procedure? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
- "BEGIN CATCH"
- "IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION"
- "RAISERROR('CreateOrder failed', 16, 1)"
- "ROLLBACK TRANSACTION"
- "SET @OrderId = SCOPE_IDENTITY()"
- "THROW"
correct_mapping:
    blank_1: "SET @OrderId = SCOPE_IDENTITY()"
    blank_2: "IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION"
---
CREATE OR ALTER PROCEDURE dbo.usp_CreateOrder
    @CustomerId int,
    @Amount decimal(10,2),
    @OrderId int OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    BEGIN TRY
        BEGIN TRANSACTION;
        INSERT INTO dbo.Orders(CustomerId, Amount, CreatedAt)
        VALUES (@CustomerId, @Amount, SYSUTCDATETIME());
        {blank_1};
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        {blank_2};
        THROW;
    END CATCH
END

