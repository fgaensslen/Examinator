---
question: "You have a GitHub Codespaces environment that has GitHub Copilot Chat installed and is connected to a SQL database in Microsoft Fabric named DB1. DB1 contains tables named Sales.Orders and Sales.Customers.


You use GitHub Copilot Chat in the context of DB1.


A company policy prohibits sharing customer Personally Identifiable Information (PII), secrets, and query result sets with any AI service.


You need to use GitHub Copilot Chat to write and review Transact-SQL code for a new stored procedure that will join Sales.Orders to Sales.Customers and return customer names and email addresses. The solution must NOT share the actual data in the tables with GitHub Copilot Chat.


What should you do?"
documentation: "https://learn.microsoft.com/en-us/azure/cognitive-services/responsible-use-of-ai"
---
- [ ]From Sales.Customers, paste several rows that include email addresses into a chat, so that GitHub Copilot Chat can infer edge cases.
- [ ]Run a SELECT statement that returns customer names and email addresses and provide the result set to GitHub Copilot Chat so that GitHub Copilot Chat can generate the stored procedure
- [ ]Provide the database connection string to GitHub Copilot Chat so that GitHub Copilot Chat can validate the stored procedure.
- [x]Ask GitHub Copilot Chat to generate the stored procedure by using schema details only.
