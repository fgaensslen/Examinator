---
question: "You have an Azure SQL database that contains a table named Rooms. Rooms was created by using the following Transact-SQL statement. 


CREATE TABLE Rooms (


&emsp;RoomID int PRIMARY KEY,

    
 &emsp;Owner nvarchar(100),


 &emsp;Capactiy int


);


You discover that some records in the Rooms table contain NULL values for the Owner field. 


You need to ensure that all future records have a value for the Owner field. What should you add?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]a foreign key
- [x]a check constraint
- [ ]a nonclustered index
- [ ]a unique constraint
