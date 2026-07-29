---
question: "You have an Azure SQL database that contains a table named knowledge_base. knowledge_base stores human resources (HR) policy documents and contains columns named title, content, category, and embedding.


You have an application named App1. App1 queries two relational tables named employee_profiles and benefits_enrollment that contain HR data. App1 hosts a chatbot that calls a large language model (LLM) directly.


Users report that the chatbot answers general HR questions correctly but provides outdated or incorrect answers when policies change. The chatbot also fails to answer questions that reference internal policy documents by title or category.


You need to recommend a Retrieval Augmented Generation (RAG) solution to resolve the chatbot issues.


What should you recommend? To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
code_lang: "TEXT"
values_pool:
    - "employee_profiles and benefits_enrollment"
    - "knowledge_base"
    - "PDF exports of the policies"
    - "The LLM training data"
    - "Perform keyword searches."
    - "Call the LLM first, and then store the response."
    - "Fine-tune the LLM by using the data in knowledge_base."
    - "Generate query embeddings, and then run a vector similarity search."
correct_mapping:
    blank_1: "knowledge_base"
    blank_2: "Generate query embeddings, and then run a vector similarity search."
---
Retrieve grounding data from:
{blank_1}
Inference step to perform the retrieval:
{blank_2}