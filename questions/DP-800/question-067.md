---
question: "You have a database that contains production data. The schema is stored in a Git repository as an SDK-style SQL database project and contains the following reference data.


| Name        | Data type     |


| RefId       | int identity  |


| Code        | nvarchar(10)  |


| CreateDate  | datetime2     | 


| Description | nvarchar(255) |


A deployment pipeline can be rerun automatically when a transient failure occurs.


You need to deploy the reference data as part of the same CI/CD process. Rerunning the pipeline must produce the same outcome and must NOT create duplicate rows.


What should you do?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [x]Add a post-deployment script that inserts reference rows by using IF NOT EXISTS or MERGE logic.
- [ ]Restore a backup after each deployment.
- [ ]Store the reference values in GitHub repository secrets.
