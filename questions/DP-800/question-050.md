---
question: "You have a GitHub Actions workflow that builds and deploys an Azure SQL database. The schema is stored in a GitHub repository as an SDK-style SQL database project.


Following a code review, you discover that you need to generate a report that shows whether the production schema has diverged from the model in source control.
Which action should you add to the pipeline?"
documentation: "https://docs.github.com/en/actions"
---
- [x]SqlPackage.exe /Action:DriftReport
- [ ]SqlPackage.exe /Action:DeployReport
- [ ]SqlPackage.exe /Action:Extract
- [ ]SqlPackage.exe /Action:Script
