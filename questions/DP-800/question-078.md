---
question: "Development Requirements -


The development team at Contoso will use Microsoft Visual Studio Code and GitHub Copilot and will retrieve live metadata from the databases. Contoso identifies the following requirements for querying data in the FeedbackJson column of the CustomerFeedback table:


Extract the customer feedback text from the JSON document. Filter rows where the JSON text contains a keyword.


Calculate a fuzzy similarity score between the feedback text and a known issue description.


Order the results by similarity score, with the highest score first.


You need to enable similarity search to provide the analysts with the ability to retrieve the most relevant health summary reports.


The solution must minimize latency.


What should you include in the solution?"
documentation: "https://learn.microsoft.com/en-us/azure/cognitive-services/responsible-use-of-ai"
---
- [ ]a computed column that manually compares vector values
- [ ]a standard nonclustered index on the Embeddings (vector (1536)) column
- [ ]a full-text index on the Embeddings (vector (1536)) column
- [x]a vector index on the Embeddings (vector (1536)) column
