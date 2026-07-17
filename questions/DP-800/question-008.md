---
question: "You have an Azure SQL database. 

You deploy Data API builder (DAB) to Azure Container Apps by using the mcr.microsoft.com/azure-databases/data-api-builder:latest image.

You have the following Container Apps secrets:

MSSQL_CONNECTION_STRING that maps to the SQL connection string

DAB_CONFIG_BASE64 that maps to the DAB configuration

You need to initialize the DAB configuration to read the SQL connection string.

Which command should you run?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]dab init --database-type mssql --connection-string "secretref:DAB_CONFIG_BASE64” --host-mode Production --config dab-config.json
- [x]dab init --database-type mssql --connection-string "@env('MSSQL_CONNECTION_STRING’)” --host-mode Production --config dab-config.json
- [ ]dab init --database-type mssql --connection-string "secretref:mssql-connection-string” --host-mode Production --config dab-config.json
- [ ]dab init --database-type mssql --connection-string "@env('DAB_CONFIG_BASE64’)” --host-mode Production --config dab-config.json
