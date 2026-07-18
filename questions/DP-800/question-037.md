---
question: "You have an Azure SQL database that contains tables named dbo.ProductDocs and dbo.ProductDocsEmbeddings. dbo.ProductDocs contains product documentation and the following columns:


DocID (int)

Title (nvarchar(200))

Body (nvarchar(max))

LastModified (datetime2)

The documentation is edited throughout the day.

dbo.ProductDocsEmbeddings contains the following columns:

DocID (int)

ChunkOrder (int)

ChunkText (nvarchar(max))

Embedding (vector(1536))


The current embedding pipeline runs once per night.

You need to ensure that embeddings are updated every time the underlying documentation content changes. The solution must NOT require a nightly batch process.
What should you include in the solution?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]fixed-size chunking
- [ ]a smaller embedding model
- [x]table triggers
- [ ]change tracking on dbo.ProductDocs
