---
question: "You have a Microsoft SQL Server 2025 instance that has a managed identity enabled.

You have a database that contains a table named dbo.ManualChunks. dbo.ManualChunks contains product manuals.

A retrieval query already returns the top five matching chunks as nvarchar(max) text.
You need to call an Azure OpenAI REST endpoint for chat completions. The solution must provide the highest level of security.

You write the following Transact-SQL code.


01 CREATE DATABASE SCOPED CREDENTIAL AzureOpenAIHeaders

02

03 GO

04 CREATE OR ALTER PROCEDURE dbo.AskManuals

05 ...

06 SELECT @chunks =

07 ...

08 SET @payload =

09 ...

10 EXEC @retval = sys.sp_invoke_external_rest_endpoint

11 @url = N'https://<your-resource>.openai.azure.com/openai/deployments/<your-deployment>/chat/completions?api-version=2024-02-15-preview',

12 @method = N'POST',

13 @credential = N'AzureOpenAIHeaders',

14 @payload = @payload,

15 @response = @response OUTPUT;

16 END;

17 GO


What should you insert at line 02?"
documentation: "https://learn.microsoft.com/en-us/azure/cognitive-services/responsible-use-of-ai"
---

