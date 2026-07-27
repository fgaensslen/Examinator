---
question: |
  You have a database named db1. The schema is stored in a Git repository as an SDK-style SQL database project. The repository contains the following GitHub Action workflow.

  ```yaml
  name: Database CI/CD
  on:
    push:
      branches:
        - main
    pull_request:
      branches:
        - main
  jobs:
    build-and-deploy:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout code
          uses: actions/checkout@v3
        - name: Setup .NET
          uses: actions/setup-dotnet@v3
          with:
            dotnet-version: '8.x'
        - name: Build
          run: dotnet build db1.sqlproj --configuration Release
        - name: Deploy
          run: |
            SqlPackage /Action:Publish
              /SourceFile:./bin/Release/db1.dacpac
              /TargetConnectionString:"${{ secrets.Target_Connection_String }}"
    unit-tests:
      runs-on: ubuntu-latest
      needs: build-and-deploy
      if: github.ref == 'refs/heads/main'
      steps:
        - name: Checkout code
          uses: actions/checkout@v3
        - name: Setup .NET
          uses: actions/setup-dotnet@v3
          with:
            dotnet-version: '8.x'
        - name: Run unit tests
          run: dotnet test UnitTests.csproj --configuration Release
  ```

  For each of the following statements, select Yes if the statement is true. Otherwise, select No.

  NOTE: Each correct selection is worth one point.
question_type: "drag_drop"
values_pool:
    - "Yes"
    - "No"
correct_mapping:
  blank_1: "Yes"
  blank_2: "Yes"
  blank_3: "No"
---
Unit tests run automatically whenever changes are pushed to main.
{blank_1}
Schema validation occurs during the Build step.
{blank_2}
Schema validation occurs during the Deploy step.
{blank_3}