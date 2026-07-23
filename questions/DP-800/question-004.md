---
question: "You have an Azure SQL database that contains the following SQL graph tables:


A NODE table named dbo.Person -


An EDGE table named dbo.Knows -


Each row in dbo.Person contains the following columns:


PersonID (int)


DisplayName (nvarchar(100))


You need to use a MATCH operator and exactly two directed Knows relationships to return the PersonID and DisplayName of people that are reachable from the person identified by an input parameter named @StartPersonId.


Which Transact-SQL query should you use?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---
- [ ]SELECT p2.PersonId, @StartPersonId FROM dbo.Person AS p1, dbo.Knows AS k1, dbo.Person AS p2, dbo.Knows AS k2, dbo.Person AS p3 WHERE p1.DisplayName = p2.DisplayName AND MATCH(p1-(k1)->p2-(k2)->p3);
- [ ]SELECT p3.PersonId, p3.DisplayName FROM dbo.Person AS p1 JOIN dbo.Knows AS k1 ON 1 = 1 JOIN dbo.Person AS p2 ON 1 = 1 JOIN dbo.Knows AS k2 ON 1 = 1 JOIN dbo.Person AS p3 ON 1 = 1 WHERE p1.PersonId = @StartPersonId AND MATCH(p3<-(k2)-p2<-(k1)-p1);
- [ ]SELECT p3.PersonId, p3.DisplayName FROM dbo.Person AS p1, dbo.Knows AS k1, dbo.Person AS p2, dbo.Knows AS k2, dbo.Person AS p3 WHERE p1.PersonId = @StartPersonId AND MATCH(p1-(k1)->p2) AND MATCH(p2-(k2)->p3);
- [x]SELECT p3.PersonId, p3.DisplayName FROM dbo.Person AS p1, dbo.Knows AS k1, dbo.Person AS p2, dbo.Knows AS k2, dbo.Person AS p3 WHERE p1.PersonId = @StartPersonId AND MATCH(p1-(k1)->p2-(k2)->p3);
