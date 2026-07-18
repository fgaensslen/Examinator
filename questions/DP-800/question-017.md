---
question: "You have an Azure SQL database named ToDo that contains a table named dbo.ToDo.

Your company plans to develop an Azure Functions app to run whenever the rows in dbo.ToDo change. The app will process INSERT, UPDATE, and DELETE events by using the Azure SQL trigger binding.

You need to configure ToDo to support the planned app.

What should you do?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [x]Enable change tracking on ToDo and dbo.ToDo.
- [ ]On dbo.ToDo, create a Data Manipulation Language (DML) trigger that calls the Azure Functions HTTP endpoint.
- [ ]Enable change data capture (CDC) on ToDo and dbo.ToDo.
- [ ]On dbo.ToDo, create a Data Definition Language (DDL) trigger that calls the Azure Functions HTTP endpoint.
