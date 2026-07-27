---
question: "You need to meet the development requirements for the FeedbackJson column.


How should you complete the Transact-SQL query? To answer, select the appropriate options in the answer area."

question_type: "drag_drop"
values_pool:
    - "CONTAINS(FeedbackJson, @Keyword)"
    - "EDIT_DISTANCE(JSON_VALUE(f.FeedbackJson, '$.details.comment'), @Keyword) < 3"
    - "EDIT_DISTANCE(JSON_VALUE(f.FeedbackJson, '$.text'), @Keyword) < 3"
    - "JSON_QUERY(f.FeedbackJson, '$.text', @KnownIssueDescription) AS FeedbackText"
    - "JSON_VALUE(f.FeedbackJson, '$.text') AS FeedbackText"
    - "SimilarityScore"
correct_mapping:
  blank_1: "JSON_VALUE(f.FeedbackJson, '$.text') AS FeedbackText"
  blank_2: "CONTAINS(FeedbackJson, @Keyword)"
  blank_3: "SimilarityScore"
---
SELECT
    f.FeedbackId,
    f.VehicleId,
    {blank_1}
    EDIT_DISTANCE_SIMILARITY(
        JSON_VALUE(f.FeedbackJson, '$.text'),
        @KnownIssueDescription
    ) AS SimilarityScore
FROM
    dbo.CustomerFeedback f
WHERE
    {blank_2}
ORDER BY
    {blank_3}
    DESC;
