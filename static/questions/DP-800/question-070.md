---
question: "You have an Azure SQL database named sqldb-ai-prod that stores customer support tickets for a multitenant software as a service (SaaS) application. sqldb-ai-prod contains a table named Tickets. Tickets contains columns named TenantId, TicketId, CustomerEmail, CustomerPhone, and Notes.


You plan to harden data access, since a new support team will use ad hoc reporting tools that connect directly to sqldb-ai-prod.


You need to configure security to meet the following requirements:


• Support agents must see only the rows of their own TenantId column.


• Support agents must see only the domain name portion of the CustomerEmail column.


What should you do for each requirement? To answer, drag the appropriate actions to the correct requirements. Each action may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "Enable Transparent Data Encryption (TDE) and customer-managed keys."
    - "Encrypt sensitive columns by using Always Encrypted with Azure Key Vault."
    - "Create a row-level security (RLS) predicate that uses the user context."
    - "Configure dynamic data masking on selected columns."
correct_mapping:
    blank_1: "Create a row-level security (RLS) predicate that uses the user context."
    blank_2: "Configure dynamic data masking on selected columns."
---
Support agents must see only the rows of their own TenantId:
{blank_1}
Support agents must see only the domain name portion of CustomerEmail:
{blank_2}