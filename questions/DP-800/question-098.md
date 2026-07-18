---
question: "You have an Azure SQL database that contains tables named dbo.Tickets and dbo.TicketNotes. dbo.Tickets contains support tickets and dbo.TicketNotes contains ticket notes. A retrieval query returns the top five relevant ticket notes for a user question. You plan to implement a Retrieval Augmented Generation (RAG) pattern that meets the following requirements: • Formats the retrieved relational data for large language model (LLM) processing • Sends the user question and retrieved context to an Azure OpenAI REST endpoint for chat completions • Extracts the response text from the LLM response Which Transact-SQL function should you use to extract the response text?"
documentation: "https://learn.microsoft.com/en-us/azure/cognitive-services/responsible-use-of-ai"
---
- [ ]JSON_MODIFY(@response, ‘$.result’)
- [ ]OPENJSON(@response)
- [ ]JSON_QUERY(@response, ‘$.choices’)
- [x]JSON_VALUE(@response, ‘$.choices[0].message.content’)
