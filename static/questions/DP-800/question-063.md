---
question: |
    You have an SDK-style SQL database project named MyDatabaseProject.sqlproj stored in a private GitHub repository. The repository contains the following GitHub Actions workflow.

    ```yaml
    name: Build and Deploy SQL Project
    on:
      push:
        branches:
          - main
      workflow_dispatch:
    jobs:
      build-and-deploy:
        runs-on: ubuntu-latest
        permissions:
          id-token: write
          contents: read
        steps:
          - uses: actions/checkout@v4
          - name: Build SQL project
            run: dotnet build MyDatabaseProject.sqlproj
          - name: Publish DACPAC
            uses: azure/sql-action@v2
            with:
              action: publish
              path: bin/Debug/MyDatabaseProject.dacpac
              connection-string: ${{ secrets.AZURE_SQL_CONNECTION_STRING }}
    ```

    The repository contains the AZURE_SQL_CONNECTION_STRING secrets.

    The target is an Azure SQL database that allows access to Azure services and is configured to support mixed authentication.

    The workflow runs successfully.
    
    For each of the following statements, select Yes if the statement is true. Otherwise, select No.

    NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
values_pool:
    - "Yes"
    - "No"
correct_mapping:
    blank_1: "No"
    blank_2: "No"
    blank_3: "Yes"
---
The workflow relies on a Microsoft Entra workload identity to access the target Azure SQL database.
{blank_1}
Changing the Build SQL project step to run: dotnet build MyDatabaseProject.sqlproj -c Release will result in a successful deployment.
{blank_2}
The workflow can be triggered manually, without making changes to the repository.
{blank_3}