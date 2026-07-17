---
question: "You have a Microsoft SQL Server 2025 instance that contains a database named SalesDB. SalesDB supports a Retrieval Augmented Generation (RAG) pattern for internal support tickets. The SQL Server instance runs without any outbound network connectivity.
You plan to generate embeddings inside the SQL Server instance and store them in a table for vector similarity queries.

You need to ensure that only a database user account named AIApplicationUser can run embedding generation by using the model.

Which two actions should you perform? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point."
documentation: "https://learn.microsoft.com/en-us/azure/cognitive-services/responsible-use-of-ai"
---
- [ ]Grant the CONTROL permission on SalesDB to AIApplicationUser.
- [ ]Create a database audit specification on SalesDB owned by AIApplicationUser.
- [x]Grant the EXECUTE permission on the external model project to AIApplicationUser.
- [x]Create an external model project by using ONNX runtime and local paths.
- [ ]Create an external model project that points to a Microsoft Foundry REST endpoint.
