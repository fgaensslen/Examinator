---
question: "You have an Azure SQL database named ProductsDB


You deploy Data API builder (DAB) to Azure Container Apps by using the mcr.microsoft.com/azure-databases /data-api-builder:latest image.


The container app has the following configurations:


• Secrets: mssql-connection-string, dab-config-base64

• Environment variables:

• MSSQL_CONNECTION_STRING=secretref:mssql-connection-string

• DAB_CONFIG_BASE64=secretref:dab-config-base64

• Ingress: External on port 5000


Users report that the /health endpoint returns a healthy response, but all requests that query an entity named Products fail and generate a connection error.


You confirm that the SQL login in the connection string is correct and the database exists.


You need to ensure that the container app can establish connections to the Azure SQL logical server without changing the container app deployment settings or the DAB configuration file.


What should you do on the Azure SQL logical server?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]Create an auto-failover group for ProductsDB.
- [ ]Run DBCC CHECKDB on ProductsDB.
- [x]Create a firewall rule that allows a start and end IP address of 0.0.0.0.
- [ ]Enable FORCE_LAST_GOOD_PLAN automatic tuning for ProductsDB.
