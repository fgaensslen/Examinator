---
question: "You have an Azure subscription. The subscription contains an Azure SQL database named SalesDB and an Azure App Service app named sales-api. sales-api uses virtual network integration to a subnet named vnet-prod/subnet-app and reads from SalesDB.


You need to configure authentication and network access to meet the following requirements:


Ensure that sales-api connects to SalesDB by using passwordless authentication.


Ensure that all the database traffic remains within the subscription.


The solution must minimize administrative effort.


What should you configure? To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "Configure client certificate authentication for sales-api."
    - "Use a connection string with rotated SQL credentials weekly."
    - "Enable a managed identity and use Microsoft Entra authentication."
    - "Create a SQL login and store the SQL credentials in Azure Key Vault."
    - "Allow Azure services and keep the public endpoint enabled."
    - "Create a private endpoint and disable public network access."
    - "Add IP firewall rules for the App Service outbound IP addresses."
    - "Configure a database-level firewall rule for support IP addresses."
correct_mapping:
    blank_1: "Enable a managed identity and use Microsoft Entra authentication."
    blank_2: "Create a private endpoint and disable public network access."
---
Authentication for sales-api:
{blank_1}
Network access for SalesDB:
{blank_2}