---
question: "You need to recommend a solution to resolve the slow dashboard query issue. What should you recommend?"
documentation: "https://learn.microsoft.com/en-us/azure/cognitive-services/responsible-use-of-ai"
---
- [ ]Create a clustered index on LastUpdatedUtc.
- [x]On FleetId, create a nonclustered index that includes LastUpdatedUtc, EngineStatus, and BatteryHealth.
- [ ]On LastUpdatedUtc, create a nonclustered index that includes FleetId.
- [ ]On FleetId, create a filtered index where LastUpdatedUtc > DATEADD(DAY, -7, SYSUTCDATETIME()).
