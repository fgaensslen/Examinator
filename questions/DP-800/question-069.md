---
question: "You have an Azure SQL database named SalesDB and an Azure App Service app named sales-api. SalesDB contains a table named dbo.Customers. dbo.Customers contains two columns named CreditCardNumber and TenantId. Currently, sales-api connects to SalesDB by using SQL authentication with stored username and password. You need to recommend a solution that meets the following requirements: • Provides a passwordless method for sales-api to access SalesDB. • Ensures that credit card numbers are NOT stored as plain text. What should you include in the recommendation?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]Azure Key Vault and Always Encrypted
- [ ]Transparent Data Encryption (TDE) and row-level security (RLS)
- [ ]managed identities and dynamic data masking
- [x]managed identities and Always Encrypted
