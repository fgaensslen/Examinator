---
question: "You have an SDK-style SQL database project named MyDatabaseProject.sqlproj stored in a private GitHub repository. The repository contains the following GitHub Actions workflow."
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