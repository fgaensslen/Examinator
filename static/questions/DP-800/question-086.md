---
question: |
    You have an Azure SQL database that contains a table named dbo.ManualChunks. dbo.ManualChunks contains product manuals.

    A retrieval query already returns the top five matching chunks as nvarchar (max) text.

    You need to call an Azure OpenAI REST endpoint for chat completions. The request body must include both the user question and the retrieved chunks.

    You write the following Transact-SQL code. What should you insert at line 22?

    ```sql
    01 CREATE DATABASE SCOPED CREDENTIAL AzureOpenAIHeaders
    02 WITH IDENTITY = 'HTTPEndpointHeaders',
    03   SECRET = N'{"api-key":"<YOUR_AZURE_OPENAI_API_KEY>"}';
    04 GO

    05 CREATE OR ALTER PROCEDURE dbo.AskManuals
    06 ...
    07 SELECT @chunks =
    08 (
    09   SELECT TOP (5)
    10     mc.ChunkText AS [text]
    11   FROM dbo.ManualChunks AS mc
    12   ORDER BY mc.Score DESC
    13   FOR JSON PATH
    14 );

    15 SET @payload =
    16 (
    17   SELECT
    18     'system' AS [messages[0].role],
    19     'Use only the provided manual chunks.' AS [messages[0].content],
    20     'user' AS [messages[1].role],
    21     CONCAT(@question, CHAR(10), JSON QUERY(@chunks)) AS [messages[1].content]
    22
    23 );
    24
    25 EXEC @retval =
    26   ...
    27 END;
    28 GO    
---
- [ ]FOR XML AUTO, TYPE, XMLSCHEMA
- [ ]FOR JSON AUTO, INCLUDE_NULL_VALUES
- [ ]FOR XML PATH, INCLUDE_NULL_VALUES
- [x]FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
