---
question: "You have an Azure SQL database that contains a table named Customer. Customer contains the following columns:


• NationalIDNumber is unique per customer.


• InvestigationNotes contains free-form text.


You have a stored procedure that performs point lookups by NationalIDNumber and returns InvestigationNotes in the query results without filtering on InvestigationNotes.


You need to encrypt both columns by using Always Encrypted and the highest security possible.


Which type of Always Encrypted encryption should you use for each column?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [x]deterministic for NationalIDNumber and randomized for InvestigationNotes
- [ ]deterministic for NationalIDNumber and deterministic for InvestigationNotes
- [ ]randomized for NationalIDNumber and randomized for InvestigationNotes
- [ ]randomized for NationalIDNumber and deterministic for InvestigationNotes
