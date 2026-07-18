---
question: "You have an Azure SQL database that contains a table named dbo.Products. dbo.Products contains three columns named Embedding, Category, and Price. The Embedding column is defined as VECTOR(1536). You use AI_GENERATE_EMBEDDINGS and VECTOR_SEARCH to support semantic search and apply additional filters on two columns named Category and Price. You plan to change the embedding model from text-embedding-ada-002 to text-embedding-3-small. Existing rows already contain embeddings in the Embedding column. You need to implement the model change. Applications must be able to use VECTOR_SEARCH without runtime errors. What should you do first?"
documentation: "https://learn.microsoft.com/en-us/azure/cognitive-services/responsible-use-of-ai"
---
- [ ]Regenerate embeddings for the existing rows.
- [ ]Normalize the vector lengths before storing new embeddings.
- [ ]Convert the Embedding column to nvarchar(max).
- [x]Create a vector index on dbo.Products.Embedding.
