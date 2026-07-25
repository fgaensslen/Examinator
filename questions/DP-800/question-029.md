---
question: "You may need to drag the split bar between panes or scroll to view content. NOTE: Each correct selection is worth one point."
question_type: "drag_drop"
values_pool:
    - "i.MaintenanceId IS NOT NULL"
    - "m.LastModifiedUtc <> i.LastModifiedUtc"
    - "m.MaintenanceId = i.MaintenanceId"
    - "m.VehicleId = i.VehicleId"
correct_mapping:
    blank_1: "m.MaintenanceId = i.MaintenanceId"
    blank_2: "m.LastModifiedUtc <> i.LastModifiedUtc"
---
CREATE TRIGGER dbo.trgMaintenanceEvents_UpdateTimestamp
ON dbo.MaintenanceEvents
AFTER UPDATE
AS
BEGIN
    UPDATE m
    SET LastModifiedUtc = SYSUTCDATETIME()
    FROM dbo.MaintenanceEvents m
    INNER JOIN inserted i
    ON
    {blank_1}
    WHERE
    {blank_2}
END;
GO