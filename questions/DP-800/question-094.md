---
question: "You have a Microsoft SQL Server 2025 database that contains a table named products. products contains two columns named description and embedding. embedding is generated from description. You have an application named App1. App1 has a feature that uses the following query. VECTOR_DISTANCE(‘cosine’, @query_vector, embedding) Users report that the feature is slow during peak usage times. You discover that during peak usage times, the semantic search latency increases and CPU utilization spikes. You need to reduce latency and CPU utilization related to the App1 feature. What should you do?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]Create a vector index on products.embedding and change the query to use VECTOR_NORMALIZE and NORM_TYPE = ‘norm1’.
- [ ]Use CONTAINSTABLE against description only and remove the vector search.
- [x]Create a vector index on products.embedding and change the query to use VECTOR_SEARCH and METRIC = ‘cosine’.
- [ ]Add a nonclustered index on products.embedding.
- [ ]Change embedding to VARBINARY(8000).
