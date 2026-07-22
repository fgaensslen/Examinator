---
question: "You have an Azure SQL database that contains a table named dbo.ManualChunks. dbo.ManualChunks contains product manuals.


A retrieval query already returns the top five matching chunks as nvarchar (max) text.


You need to call an Azure OpenAI REST endpoint for chat completions. The request body must include both the user question and the retrieved chunks.


You write the following Transact-SQL code. What should you insert at line 22?"
documentation: "https://learn.microsoft.com/en-us/azure/cognitive-services/responsible-use-of-ai"
---
- [ ]FOR XML AUTO, TYPE, XMLSCHEMA
- [ ]FOR JSON AUTO, INCLUDE_NULL_VALUES
- [ ]FOR XML PATH, INCLUDE_NULL_VALUES
- [x]FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
