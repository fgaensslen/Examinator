---
question: "You create an SDK-style SQL database project in Microsoft Visual Studio Code named Database.sqlproj and add the project to a GitHub repository.


You need to configure a GitHub Actions workflow to support the planned changes for DB1.


How should you complete the workflow? To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
code_lang: "YAML"
values_pool:
    - "merge"
    - "pull_request"
    - "push"
    - "build Database.sqlproj -c Release"
    - "pack Database.sqlproj"
    - "publish Database.sqlproj -c Production"
    - "publish Database.sqlproj -c Release"
correct_mapping:
    blank_1: "pull_request"
    blank_2: "build Database.sqlproj -c Release"
---
name: Validate SQL Project
on:
  {blank_1}:
    branches: [ "main" ]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
      - name: Step 1
        run: dotnet {blank_2}