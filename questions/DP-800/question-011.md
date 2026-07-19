---
question: "Your development team uses GitHub Copilot Chat in Microsoft SQL Server Management Studio (SSMS) to generate and run Transact-SQL queries against an Azure SQL database named DB1. DB1 contains tables that store sensitive customer data. 


You need to ensure that any Transact-SQL queries that run from GitHub Copilot Chat in SSMS are restricted by the same permissions as the developer’s database login.


What prevents the GitHub Copilot Chat-run queries from accessing data beyond the developer's access?"
documentation: "https://docs.github.com/en/actions"
---
- [ ]GitHub Copilot Chat runs queries in a read-only sandbox that is isolated from production database permissions.
- [x]GitHub Copilot Chat runs queries by using the developer’s database identity and permissions.
- [ ]GitHub Copilot Chat filters query results on the client side to remove rows the developer is unauthorized to see.
- [ ]GitHub Copilot Chat uses different row-level security (RLS) policies than the developer.
