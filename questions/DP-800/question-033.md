---
question: "You have an Azure SQL database named SalesDB that contains a table named dbo.Articles. dbo.Articles contains two million articles with embeddings. The articles are updated frequently throughout the day.

You query the embeddings by using VECTOR_SEARCH.

Users report that semantic search results do NOT reflect the updates until the following day.

You need to ensure that the embeddings are updated whenever the articles change. The solution must minimize CPU usage on SalesDB.

Which embedding maintenance method should you implement?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]Modify the query to use VECTOR_DISTANCE instead of VECTOR_SEARCH.
- [x]Enable change data capture (CDC) on dbo.Articles and use an Azure Functions app to process CDC changes.
- [ ]Run an hourly Transact-SQL job that regenerates embeddings for all the rows in dbo.Articles.
- [ ]On dbo.Articles, create a trigger that calls AI_GENERATE_EMBEDDINGS for each inserted or updated row.
