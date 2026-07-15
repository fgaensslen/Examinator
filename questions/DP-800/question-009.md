---
question: "You have a SQL database in Microsoft Fabric that contains a nvarchar (max) column named MessageText. An ID is always contained within the first paragraph of MessageText. 

You need to write a Transact-SQL query that uses REGEXP_SUBSTR to extract the ID from MessageText. 

What should you include in the query?"
documentation: "https://learn.microsoft.com/en-us/azure/"
---

- [x] A. Apply STRING_ESCAPE(MessageText, ‘json’) before calling REGEXP_SUBSTR.
- [ ] B. Cast MessageText to nvarchar (4000) before calling REGEXP_SUBSTR.
- [ ] C. Add a COLLATE Latin1_General_CS_AS clause to MessageText before calling REGEXP_SUBSTR.
- [ ] D. Run TRY_CONVERT(varchar(max), MessageText) before calling REGEXP_SUBSTR.
