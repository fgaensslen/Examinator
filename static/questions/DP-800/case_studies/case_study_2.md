---
linked_questions:
  - question-016.md
  - question-026.md
  - question-057.md
  - question-058.md
  - question-059.md
  - question-060.md
  - question-091.md
  - question-092.md
---

# Case Study
This is a case study. Case studies are not timed separately. You can use as much exam time as you would like to complete each case. However, there may be additional case studies and sections on this exam. You must manage your time to ensure that you are able to complete all questions included on this exam in the time provided.


To answer the questions included in a case study, you will need to reference information that is provided in the case study. Case studies might contain exhibits and other resources that provide more information about the scenario that is described in the case study. Each question is independent of the other questions in this case study.


At the end of this case study, a review screen will appear. This screen allows you to review your answers and to make changes before you move to the next section of the exam. After you begin a new section, you cannot return to this section.

# Azure Environment
Fabrikam has a single Azure subscription in the East US 2 Azure region. The subscription contains an Azure SQL database named DB1. DB1 contains the following tables:


- Patients
- Employees
- Procedures
- Transactions
- UsefulPrompts
- ProcedureDocuments

You store a column master key as a secret in Azure Key Vault.
You have an on-premises application named TransactionProcessing that uses a hard-coded username and password in a connection string to access DB1.

# Planned Changes
Fabrikam plans to manage all changes to Azure SQL Database objects by using source control in GitHub. Every pull request submitted to production will be validated before it can be merged. Deployments must use the Release configuration.

# Security Requirements
Fabrikam identifies the following security requirements:


- The TransactionProcessing application must use a passwordless connection to DB1.
- The Employees table contains two columns named TaxID and Salary that must be encrypted at rest.
- Auditors must have a tamper-evident history of transactions with cryptographic proof of changes to the employee data.


Database Performance Requirements


Records accessed by using sp_UpdateProcedureForPatient must NOT be changed by other transactions while the stored procedure runs.


AI Search, Embeddings, and Vector Indexing


Fabrikam identifies the following AI-related requirements:


- Queries to the ProcedureDocuments table must use Reciprocal Rank Fusion (RRF).
- Users must be able to query the data in DB1 by using prompts in Copilot in Microsoft Fabric.
- The UsefulPrompts table will store prompts that doctors can use to help diagnose patient illness by connecting to an Azure OpenAI endpoint.

# Development Requirements
Fabrikam identifies the following development requirements:


- Provide the functionality to retrieve all the transactions of a given patient between two dates, showing a running total.
- Expose a Data API builder (DAB) configuration file to enable Azure services to perform the following operations over a REST API:
  - Read data from the procedures table without authentication.
  - Read and insert data into the Transactions table once authenticated.
  - Execute the sp_UpdateProcedurePatient stored procedure.
- Provide the functionality to retrieve a list of the names of patients who underwent medical procedures during the last 30 days.
- Information for each medical procedure will be stored in a table. The table will be used with a large language model (LLM) for user querying and
will have the following structure.

```SQL
CREATE TABLE dbo.ProcedureDocuments (
    DocumentId INT IDENTTITY PRIMARY KEY,
    SourceId NVARCHAR(200) NULL,
    Content NVARCHAR(MAX) NOT NULL,
    Embedding VECTOR(1536) NOT NULL,
    CreatedAt DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);
```

# DAB
You create a DAB configuration file that meets the development requirements for DB1 and includes the following entities.

```json
{
  "entities": {
    "Procedures": {
      "source": "dbo.Procedures",
      "rest": true,
      "graphql": true,
      "permissions": [
        {
          "role": "anonymous",
          "actions": [ "read" ]
        }
      ]
    },
    "Transactions": {
      "source": "dbo.Transactions",
      "rest": true,
      "graphql": true,
      "permissions": [
        {
          "role": "authenticated",
          "actions": [ "read", "create" ]
        }
      ]
    },
    "UpdateProcedurePatient": {
      "source": "dbo.sp_UpdateProcedurePatient",
      "rest": {
        "enabled": true,
        "method": "post",
        "path": "/procedurepatient"
      },
      "graphql": false,
      "permissions": [
        {
          "role": "authenticated",
          "actions": [ "execute" ]
        }
      ]
    }
  }
}
```