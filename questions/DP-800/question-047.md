---
question: "You have an Azure SQL database named SalesDB on a logical server named sales-sql01.


You have an Azure App Service web app named OrderApi that connects to SalesDB by using SQL authentication.


You enable a user-assigned managed identity named OrderApi-Id for OrderApi.
You need to configure OrderApi to connect to SalesDB by using Microsoft Entra authentication. The managed identity must have read and write permissions to SalesDB.
Which Transact-SQL statements should you run in SalesDB?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ] CREATE LOGIN [OrderApi-Id] FROM EXTERNAL PROVIDER; ALTER ROLE db_datareader ADD MEMBER [OrderApi-Id]; ALTER ROLE db_datawriter ADD MEMBER [OrderApi-Id];
- [ ] CREATE USER [OrderApi-Id] WITH PASSWORD = 'P@ssw0rd!'; ALTER ROLE db_datareader ADD MEMBER [OrderApi-Id]; ALTER ROLE db_datawriter ADD MEMBER [OrderApi-Id];
- [x] CREATE USER [OrderApi-Id] FROM EXTERNAL PROVIDER; ALTER ROLE db_datareader ADD MEMBER [OrderApi-Id]; ALTER ROLE db_datawriter ADD MEMBER [OrderApi-Id];
- [ ] CREATE LOGIN [OrderApi-Id] WITH PASSWORD = 'P@ssw0rd!'; ALTER SERVER ROLE sysadmin ADD MEMBER [OrderApi-Id];
