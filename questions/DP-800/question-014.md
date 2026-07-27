---
question: "You have an Azure SQL database that contains a table named Rooms. Rooms was created by using the following Transact-SQL statement. 


You discover that some records in the Rooms table contain NULL values for the Owner field. 


You need to ensure that all future records have a value for the Owner field. What should you add?


```sql

CREATE TABLE Rooms (

RoomID int PRIMARY KEY,
    
Owner nvarchar(100),

Capactiy int

);"
---
- [ ]a foreign key
- [x]a check constraint
- [ ]a nonclustered index
- [ ]a unique constraint
