---
question: |
    You have an Azure SQL database named ProductsDB.

    You deploy Data API builder (DAB) to Azure Container Apps.

    You discover that the container app cannot connect to ProductsDB.

    Your development team reports that the container app is unreachable from the internet for integration tests.

    You need to update Azure SQL Database and Container Apps to meet the following requirements:

    - Ensure that the Azure SQL logical server allows connections from Azure services.
    - Ensure that the Container Apps environment accepts inbound requests from the public internet.

    What should you configure? To answer, select the appropriate options in the answer area.

    NOTE: Each correct selection is worth one point.

question_type: "drag_drop"
values_pool:
    - "0.0.0.0 to 0.0.0.0."
    - "127.0.0.1 to 127.0.0.1"
    - "10.0.0.0 to 10.255.255.255"
    - "Restrict ingress to internal traffic only."
    - "Set ingress to external and target port 5000."
    - "Set ingress to internal and target port 5000."
correct_mapping:
    blank_1: "0.0.0.0 to 0.0.0.0."
    blank_2: "Set ingress to external and target port 5000."
---
Start IP address and end IP address of the Azure SQL firewall rule:
{blank_1}
Container Apps ingress:
{blank_2}