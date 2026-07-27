---
question: |
    You have a Microsoft Fabric workspace named Workspace1 that contains a SQL database named SalesDB and an API for GraphQL item named SalesApi.

    You have a Microsoft Entry group named SqlUsers.

    From Workspace1, you assign permission to SalesApi as shown in the following exhibit.
    ![](question-044_1.png)

    The connection to SalesDB has the connectivity option configured as shown in the following exhibit.
    ![](question-044_2.png)

    SqlUsers has the Viewer role for Workspace1.
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
The members of SqlUsers can modify the data in SalesDB via SalesAPI.
{blank_1}
The members of SqlUsers can view the data in SalesDB via SalesAPI.
{blank_2}
The members of SqlUsers can change the field mappings of SalesAPI.
{blank_3}