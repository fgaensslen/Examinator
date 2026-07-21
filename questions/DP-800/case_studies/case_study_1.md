---
title: "Case Study 1: Cloud Architecture Scaling & Security"
exam: "exam_folder_name"
linked_questions:
  - "question_001.md"
  - "question_002.md"
  - "question_003.md"
---

## Executive Summary
Briefly describe the scenario, enterprise context, or system architecture setup that the student needs to understand before answering the related questions.

---

## Architecture Diagram / Scenario Visual
You can embed images using standard markdown syntax, which your code can parse:

![System Architecture Overview](architecture_diagram.png)

---

## Key Technical Specifications
* **Infrastructure Provider:** AWS / Kubernetes
* **Traffic Load:** 50,000 requests per second peak
* **Constraint:** Zero downtime deployment requirement

---

## Detailed Scenario Description
Provide the core details, background logs, or configuration files relevant to the case:

```json
{
  "service": "api-gateway",
  "timeout_ms": 3000,
  "retry_policy": "exponential_backoff"
}