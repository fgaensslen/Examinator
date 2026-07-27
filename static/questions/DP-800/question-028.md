---
question: |
    You are creating a table that will store customer profiles.

    You have the following Transact-SQL code.

    For each of the following statements, select Yes if the statement is true. Otherwise, select No.

    NOTE: Each correct selection is worth one point.


    ```sql
    CREATE TABLE dbo.CustomerProfiles
    (
      CustomerId BIGINT IDENTITY(1,1) PRIMARY KEY,
      FullName NVARCHAR(200) MASKED WITH (FUNCTION = 'partial(1,"xxxx",1)'),
      EmailAddress NVARCHAR(200) MASKED WITH (FUNCTION = 'email()'),
      PhoneNumber NVARCHAR(50) MASKED WITH (FUNCTION = 'default()'),
      RegionCode NVARCHAR(10) NOT NULL
    );
    GO
    CREATE FUNCTION dbo.fn_FilterByRegion(@RegionCode NVARCHAR(10))
    RETURNS TABLE
    AS
    RETURN
    (
      SELECT 1
      FROM dbo.UserRegionAccess ura
      WHERE ura.UserPrincipalName = SUSER_SNAME()
        AND ura.RegionCode = @RegionCode
    );
    GO
    CREATE SECURITY POLICY CustomerRegionPolicy
    ADD FILTER PREDICATE dbo.fn_FilterByRegion(RegionCode)
    ON dbo.CustomerProfiles
    WITH (STATE = ON);
    GO

question_type: "drag_drop"
values_pool:
    - "Yes"
    - "No"
correct_mapping:
    blank_1: "No"
    blank_2: "Yes"
    blank_3: "Yes"
---
Statements:
The schema meets the security requirements for PII data.
{blank_1}
Administrators of the Azure SQL server can see all the rows in dbo.CustomerProfiles when they use an application.
{blank_2}
The masking rules will apply even when row-level security (RLS) filters out rows.
{blank_3}