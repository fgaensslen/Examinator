---
question: "You have an Azure SQL database that contains a table named Sales.Customer. Sales.Customer contains columns named CustomerId, FullName, Email, TaxID, and RegionId.


You have a database role named AppSupport that is used by a support application.


You need to implement a security solution for AppSupport that meets the following requirements:


• AppSupport must be prevented from viewing TaxID.


• AppSupport must be able to query Sales.Customer to troubleshoot issues.


• AppSupport must be able to run a stored procedure named Sales.usp_GetCustomerByCustomerId.


Which Transact-SQL statements should you include in the solution? To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "DENY SELECT ON OBJECT::Sales.Customer TO AppSupport;"
    - "DENY SELECT ON OBJECT::Sales.Customer(TaxID) TO AppSupport;"
    - "GRANT EXECUTE ON OBJECT::Sales.usp_GetCustomerByCustomerId TO AppSupport;"
    - "GRANT SELECT ON OBJECT::Sales.Customer TO AppSupport;"
    - "GRANT SELECT ON OBJECT::Sales.usp_GetCustomerByCustomerId TO AppSupport;"
    - "REVOKE SELECT ON OBJECT::Sales.Customer(TaxID) FROM AppSupport;"
correct_mapping:
    blank_1: "GRANT EXECUTE ON OBJECT::Sales.usp_GetCustomerByCustomerId TO AppSupport;"
    blank_2: "GRANT SELECT ON OBJECT::Sales.Customer TO AppSupport;"
    blank_3: "DENY SELECT ON OBJECT::Sales.Customer(TaxID) TO AppSupport;"
---
To run Sales.usp_GetCustomerByCustomerId:
{blank_1}
To query Sales.Customer:
{blank_2}
To prevent viewing TaxID:
{blank_3}