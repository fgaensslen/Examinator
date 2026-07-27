---
question: "You need to create a table in the database to store the telemetry data.


You have the following Transact-SQL code.


For each of the following statements, select Yes if the statement is true. Otherwise, select No.


NOTE: Each correct selection is worth one point.


CREATE TABLE dbo.VehicleTelemetry


(


  TelemetryId BIGINT IDENTITY(1,1) NOT NULL,


  VehicleId NVARCHAR(50) NOT NULL,


  TelemetryTimeUtc DATETIME2(3) NOT NULL,


  BatteryPercent TINYINT NULL,


  SpeedKmh SMALLINT NULL,


  LocationJson JSON NULL,


  ErrorCodesJson JSON NULL,


  RawPayload NVARCHAR(MAX) NULL,


  SysStartTime DATETIME2(7) GENERATED ALWAYS AS ROW START NOT NULL,


  SysEndTime DATETIME2(7) GENERATED ALWAYS AS ROW END NOT NULL,


  PERIOD FOR SYSTEM_TIME (SysStartTime, SysEndTime),


  CONSTRAINT PK_VehicleTelemetry PRIMARY KEY CLUSTERED (TelemetryId)


)


WITH


(


  SYSTEM_VERSIONING = ON


  (


    HISTORY_TABLE = dbo.VehicleTelemetryHistory


  )


);


GO


CREATE INDEX IX_VehicleTelemetry_Time ON dbo.VehicleTelemetry (TelemetryTimeUtc);


CREATE JSON INDEX JI_VehicleTelemetry_Location ON dbo.VehicleTelemetry (LocationJson)


FOR


(
  '\\$.location. latitude', '\\$.location. longitude',


  '\\$.location. accuracy'


);


"

question_type: "drag_drop"
values_pool:
    - "Yes"
    - "No"
correct_mapping:
    blank_1: "No"
    blank_2: "Yes"
    blank_3: "No"
---
The code meets the database performance requirements for partitioning.
{blank_1}
The code meets the database performance requirements for JSON property querying.
{blank_2}
Queries that filter on $.location.heading will use the JI_VehicleTelemetry_Location index.
{blank_3}