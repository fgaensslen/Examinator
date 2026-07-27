---
question: | 
    You have an Azure SQL database that contains the following tables and columns.

    | Tables | Columns |
    | :--- | :--- |
    | Articles | &bull; ArticleId (int)<br>&bull; Title (nvarchar(200))<br>&bull; Notes (nvarchar(max))<br>&bull; Description (nvarchar(max))  |
    | NotesEmbeddings | &bull; ArticleId (int) <br>&bull; ChunkIndex (int)<br>&bull; Embedding (vector(1536)) |
    | DescriptionEmbeddings | &bull; ArticleId (int) <br>&bull; ChunkIndex (int) <br>&bull; Embedding (vector(1536) |

    Embeddings in the NotesEmbeddings and DescriptionEmbeddings tables have been generated from values in the Description and Notes columns of the Articles table by using different chunk sizes.


    You need to perform approximate nearest neighbor (ANN) queries across both embedding tables. The solution must minimize the impact of using different chunk sizes.


    What should you use? To answer, select the appropriate options in the answer area.


    NOTE: Each correct selection is worth one point.

question_type: "drag_drop"
values_pool:
    - "VECTOR_DISTANCE"
    - "VECTOR_NORM"
    - "VECTOR_SEARCH"
    - "cosine distance"
    - "dot product"
    - "Euclidean distance"
correct_mapping:
    blank_1: "VECTOR_SEARCH"
    blank_2: "cosine distance"
---
Function:
{blank_1}
Distance metric:
{blank_2}