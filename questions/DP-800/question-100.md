---
question: "DRAG DROP -


You have an Azure SQL database named SalesDB. SalesDB contains a table named dbo.Articles. dbo.Articles contains the following columns:


• ArticleId


• Title


• Body


• LastModifiedUtc


• EmbeddingVector


You have an application that generates embeddings from the concatenation of Title and Body and stores the results in EmbeddingVector.


You plan to implement an incremental embedding maintenance method that will use change data capture (CDC) to update embeddings only for rows that change, without scanning the entire table.


You need to ensure that only the columns required to generate the embeddings are captured. The solution must support querying net changes.


How should you complete the Transact-SQL script? To answer, drag the appropriate values to the correct targets. Each value may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."
documentation: "https://learn.microsoft.com/en-us/azure/"
---

